#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compile TikZ sources into dark/light semantic SVG assets.

This is a domain-agnostic rendering mechanism. It accepts an explicit TeX file
or directory and knows nothing about Math1/408 archive layout or exam policy.
Domain-specific batch selection belongs to ``kaoyan/00_system/tools``.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from functools import lru_cache
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
LATEX_ROOT = REPO_ROOT / "infra" / "latex"

TIKZ_STANDALONE_TEMPLATE = r"""\documentclass[dvisvgm,tikz,border=3pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{CJKutf8}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathreplacing,patterns}

\definecolor{themebg}{HTML}{__BG_HEX__}
\definecolor{themefg}{HTML}{__FG_HEX__}
\definecolor{themegray}{HTML}{__GRAY_HEX__}
\definecolor{themecurve}{HTML}{__CURVE_HEX__}
\definecolor{themealert}{HTML}{__ALERT_HEX__}
\definecolor{themeamber}{HTML}{__AMBER_HEX__}
\definecolor{themepurple}{HTML}{__PURPLE_HEX__}
\definecolor{themegreen}{HTML}{__GREEN_HEX__}

\begin{document}
\begin{CJK*}{UTF8}{gbsn}
\pagecolor{themebg}
\begin{tikzpicture}[
  >=Stealth,
  line cap=round,
  line join=round,
  scale=1.2,
  color=themefg,
  text=themefg,
  every node/.style={color=themefg}
]
__TIKZ_BODY__
\end{tikzpicture}
\end{CJK*}
\end{document}
"""


@lru_cache(maxsize=1)
def get_tex_bin() -> tuple[str, str]:
    """Resolve latex and dvisvgm from PATH or common TeX installation roots."""
    tex_dirs = [
        "/Library/TeX/texbin",
        "/usr/local/bin",
        "/opt/homebrew/bin",
        "/usr/bin",
    ]
    latex_path = shutil.which("latex")
    dvisvgm_path = shutil.which("dvisvgm")

    if not latex_path:
        for directory in tex_dirs:
            candidate = os.path.join(directory, "latex")
            if os.path.exists(candidate):
                latex_path = candidate
                break

    if not dvisvgm_path:
        for directory in tex_dirs:
            candidate = os.path.join(directory, "dvisvgm")
            if os.path.exists(candidate):
                dvisvgm_path = candidate
                break

    if not latex_path or not dvisvgm_path:
        raise RuntimeError(
            f"latex/dvisvgm not found (latex={latex_path}, dvisvgm={dvisvgm_path})"
        )

    return latex_path, dvisvgm_path


def build_environment(source_dir: Path) -> dict[str, str]:
    """Expose source-local, shared LaTeX, and repository-relative inputs."""
    env = os.environ.copy()
    existing = env.get("TEXINPUTS", "")
    env["TEXINPUTS"] = ".:" + ":".join(str(path) for path in (source_dir, LATEX_ROOT, REPO_ROOT)) + f":{existing}:"
    return env


def default_outputs(tex_src_path: Path) -> tuple[Path, Path]:
    """Map assets/src/foo.tex to assets/foo.svg and assets/light/foo.svg."""
    source_dir = tex_src_path.parent
    if source_dir.name in {"src", "tikz"}:
        asset_root = source_dir.parent
    else:
        asset_root = source_dir
    return asset_root / f"{tex_src_path.stem}.svg", asset_root / "light" / f"{tex_src_path.stem}.svg"


UNSAFE_MIXING_RE = re.compile(
    r"\b(themecurve|themealert|themeamber|themepurple|themegreen|blue|red|green|yellow|orange|cyan|magenta)!\d+(?![\w]*!)\b"
)


def lint_tikz_source(src_code: str, filename: str = "") -> list[str]:
    """Check TikZ source for dark-mode anti-patterns and unsafe color mixing."""
    errors = []
    for idx, line in enumerate(src_code.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("%"):
            continue
        for match in UNSAFE_MIXING_RE.finditer(line):
            matched_str = match.group(0)
            errors.append(
                f"{filename}:{idx} [UNSAFE_COLOR_MIXING] '{matched_str}' mixes with pure white in xcolor, "
                f"causing glaring white patches in dark mode. Use '{matched_str}!themebg' or 'fill opacity=...' instead."
            )
    return errors


def compile_tikz_source(
    tex_src_path: str | Path,
    out_dark_svg: str | Path | None = None,
    out_light_svg: str | Path | None = None,
) -> bool:
    """Compile one TikZ source into paired dark/light path-only SVGs."""
    source = Path(tex_src_path).resolve()
    if not source.is_file():
        print(f"[error] source does not exist: {source}")
        return False

    src_code = source.read_text(encoding="utf-8")
    lint_errors = lint_tikz_source(src_code, source.name)
    if lint_errors:
        print(f"[tikz-lint] Found {len(lint_errors)} anti-pattern(s) in {source.name}:")
        for err in lint_errors:
            print(f"  [error] {err}")
        return False

    is_full_doc = r"\documentclass" in src_code
    default_dark, default_light = default_outputs(source)
    dark_output = Path(out_dark_svg).resolve() if out_dark_svg else default_dark
    light_output = Path(out_light_svg).resolve() if out_light_svg else default_light
    latex_bin, dvisvgm_bin = get_tex_bin()
    env = build_environment(source.parent)

    # (theme_name, bg, fg, gray, curve, alert, amber, purple, green, destination)
    themes = [
        ("dark", "2e362c", "edf4e8", "a4af9d", "7eb6ff", "ff7b7b", "f5b942", "c084fc", "4ade80", dark_output),
        ("light", "faf8f5", "111111", "666666", "1d63b8", "c53030", "b86e00", "7c3aed", "15803d", light_output),
    ]

    print(f"[tikz] {source.name} -> dark/light SVG")
    with tempfile.TemporaryDirectory(prefix="ipara-tikz-") as tmp:
        build_dir = Path(tmp)
        svg_files: dict[str, Path] = {}

        for theme_name, bg_hex, fg_hex, gray_hex, curve_hex, alert_hex, amber_hex, purple_hex, green_hex, _ in themes:
            prefix = f"{source.stem}_{theme_name}"
            build_tex = build_dir / f"{prefix}.tex"

            if is_full_doc:
                content = re.sub(
                    r"\\definecolor\{themebg\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themebg}}{{HTML}}{{{bg_hex}}}",
                    src_code,
                )
                content = re.sub(
                    r"\\definecolor\{themefg\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themefg}}{{HTML}}{{{fg_hex}}}",
                    content,
                )
                content = re.sub(
                    r"\\definecolor\{themegray\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themegray}}{{HTML}}{{{gray_hex}}}",
                    content,
                )
                content = re.sub(
                    r"\\definecolor\{themecurve\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themecurve}}{{HTML}}{{{curve_hex}}}",
                    content,
                )
                content = re.sub(
                    r"\\definecolor\{themealert\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themealert}}{{HTML}}{{{alert_hex}}}",
                    content,
                )
                content = re.sub(
                    r"\\definecolor\{themeamber\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themeamber}}{{HTML}}{{{amber_hex}}}",
                    content,
                )
                content = re.sub(
                    r"\\definecolor\{themepurple\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themepurple}}{{HTML}}{{{purple_hex}}}",
                    content,
                )
                content = re.sub(
                    r"\\definecolor\{themegreen\}\{HTML\}\{[0-9a-fA-F]+\}",
                    rf"\\definecolor{{themegreen}}{{HTML}}{{{green_hex}}}",
                    content,
                )
            else:
                content = (
                    TIKZ_STANDALONE_TEMPLATE
                    .replace("__BG_HEX__", bg_hex)
                    .replace("__FG_HEX__", fg_hex)
                    .replace("__GRAY_HEX__", gray_hex)
                    .replace("__CURVE_HEX__", curve_hex)
                    .replace("__ALERT_HEX__", alert_hex)
                    .replace("__AMBER_HEX__", amber_hex)
                    .replace("__PURPLE_HEX__", purple_hex)
                    .replace("__GREEN_HEX__", green_hex)
                    .replace("__TIKZ_BODY__", src_code)
                )

            build_tex.write_text(content, encoding="utf-8")

            latex_result = subprocess.run(
                [latex_bin, "-interaction=nonstopmode", build_tex.name],
                cwd=build_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
            )
            if latex_result.returncode != 0:
                print(f"[error] latex failed ({theme_name})\n{latex_result.stdout}\n{latex_result.stderr}")
                return False

            dvi_name = f"{prefix}.dvi"
            svg_name = f"{prefix}.svg"
            dvisvgm_result = subprocess.run(
                [dvisvgm_bin, "--no-fonts", "--exact-bbox", "-v0", dvi_name, "-o", svg_name],
                cwd=build_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
            if dvisvgm_result.returncode != 0:
                print(f"[error] dvisvgm failed ({theme_name})\n{dvisvgm_result.stdout}\n{dvisvgm_result.stderr}")
                return False

            svg_files[theme_name] = build_dir / svg_name

        # Generate comprehensive adaptive style mapping for dark SVG
        if "dark" in svg_files and "light" in svg_files:
            dark_file = svg_files["dark"]
            light_file = svg_files["light"]
            dark_text = dark_file.read_text(encoding="utf-8")
            light_text = light_file.read_text(encoding="utf-8")

            base_pairs = [
                ("2e362c", "faf8f5"),
                ("30362d", "faf8f5"),
                ("edf4e8", "111111"),
                ("a4af9d", "666666"),
                ("9ea897", "666666"),
                ("7eb6ff", "1d63b8"),
                ("ff7b7b", "c53030"),
                ("f5b942", "b86e00"),
                ("c084fc", "7c3aed"),
                ("4ade80", "15803d"),
            ]
            fill_map: dict[str, str] = {f"#{d}": f"#{l}" for d, l in base_pairs}
            stroke_map: dict[str, str] = {f"#{d}": f"#{l}" for d, l in base_pairs}

            try:
                import xml.etree.ElementTree as ET
                dark_tree = ET.fromstring(dark_text)
                light_tree = ET.fromstring(light_text)

                tags = ('path', 'rect', 'g', 'circle', 'line', 'polygon', 'polyline', 'text', 'use')
                d_elems = [e for e in dark_tree.iter() if any(e.tag.endswith(t) for t in tags)]
                l_elems = [e for e in light_tree.iter() if any(e.tag.endswith(t) for t in tags)]

                if len(d_elems) == len(l_elems):
                    for d_el, l_el in zip(d_elems, l_elems):
                        d_f = d_el.attrib.get("fill")
                        l_f = l_el.attrib.get("fill")
                        if d_f and l_f and d_f not in ("none", "transparent") and l_f not in ("none", "transparent") and d_f != l_f:
                            d_norm = d_f.lower()
                            l_norm = l_f.lower()
                            if l_norm == "#111": l_norm = "#111111"
                            if l_norm == "#666": l_norm = "#666666"
                            if l_norm == "#fff": l_norm = "#ffffff"
                            fill_map[d_norm] = l_norm

                        d_s = d_el.attrib.get("stroke")
                        l_s = l_el.attrib.get("stroke")
                        if d_s and l_s and d_s not in ("none", "transparent") and l_s not in ("none", "transparent") and d_s != l_s:
                            d_norm = d_s.lower()
                            l_norm = l_s.lower()
                            if l_norm == "#111": l_norm = "#111111"
                            if l_norm == "#666": l_norm = "#666666"
                            if l_norm == "#fff": l_norm = "#ffffff"
                            stroke_map[d_norm] = l_norm
            except Exception as e:
                print(f"[warning] Element mapping failed ({e}), falling back to base palette")

            rules = []
            for d_col, l_col in fill_map.items():
                rules.append(f"    [fill='{d_col}'], [fill='{d_col.upper()}'], [fill='{d_col}' i] {{ fill: {l_col} !important; }}")
            for d_col, l_col in stroke_map.items():
                rules.append(f"    [stroke='{d_col}'], [stroke='{d_col.upper()}'], [stroke='{d_col}' i] {{ stroke: {l_col} !important; }}")

            adaptive_style = (
                "\n<style>\n"
                "  svg { max-width: 100%; height: auto; }\n"
                "  @media print, (prefers-color-scheme: light) {\n"
                "    svg { max-width: 100% !important; height: auto !important; }\n"
                + "\n".join(rules)
                + "\n  }\n</style>\n"
            )

            if "<style>" not in dark_text:
                dark_text = re.sub(r"(<defs|<path|<g)", rf"{adaptive_style}\1", dark_text, count=1)
                dark_file.write_text(dark_text, encoding="utf-8")

        for theme_tuple in themes:
            theme_name = theme_tuple[0]
            destination = theme_tuple[-1]
            svg_file = svg_files[theme_name]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(svg_file, destination)
            print(f"  [{theme_name}] {destination}")

    return True


def is_tikz_source(path: Path) -> bool:
    """Check whether a TeX file is a standalone TikZ figure source."""
    if path.name.endswith(".tmp.tex"):
        return False
    parts = set(path.parts)
    return "src" in parts or "tikz" in parts


def compile_all_in_dir(directory: str | Path) -> bool:
    """Compile every TikZ source below an explicit directory in parallel."""
    import concurrent.futures

    root = Path(directory).resolve()
    files = sorted(path for path in root.rglob("*.tex") if is_tikz_source(path))
    total = len(files)
    print(f"[scan] {root}: Found {total} TikZ TeX sources", flush=True)

    if total == 0:
        return True

    success_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        future_to_file = {executor.submit(compile_tikz_source, f): f for f in files}
        for i, future in enumerate(concurrent.futures.as_completed(future_to_file), 1):
            f = future_to_file[future]
            try:
                ok = future.result()
                if ok:
                    success_count += 1
                    print(f"[{i}/{total}] [ok] {f.name}", flush=True)
                else:
                    print(f"[{i}/{total}] [fail] {f.name}", flush=True)
            except Exception as e:
                print(f"[{i}/{total}] [error] {f.name}: {e}", flush=True)

    print(f"[summary] Completed {success_count}/{total} TikZ figures successfully.", flush=True)
    return success_count == total


def main() -> int:
    parser = argparse.ArgumentParser(description="TikZ -> paired semantic SVG compiler")
    parser.add_argument("file", nargs="?", help="TikZ .tex source")
    parser.add_argument("--dir", help="explicit directory to compile recursively")
    parser.add_argument("--all", action="store_true", help="compile all TikZ sources in repository")
    parser.add_argument("--lint", action="store_true", help="lint TikZ sources for color mixing issues without compiling")
    parser.add_argument("--dark-output", help="custom dark SVG output path (single-file mode)")
    parser.add_argument("--light-output", help="custom light SVG output path (single-file mode)")
    args = parser.parse_args()

    if args.lint:
        target_dir = Path(args.dir).resolve() if args.dir else REPO_ROOT / "kaoyan"
        files = sorted(path for path in target_dir.rglob("*.tex") if is_tikz_source(path))
        all_errors = []
        for f in files:
            all_errors.extend(lint_tikz_source(f.read_text(encoding="utf-8"), f.name))
        if all_errors:
            print(f"[tikz-lint] Found {len(all_errors)} anti-pattern(s):")
            for err in all_errors:
                print(f"  [error] {err}")
            return 1
        print(f"[tikz-lint] PASSED: All {len(files)} TikZ sources follow safe color mixing contracts.")
        return 0

    if args.all:
        return 0 if compile_all_in_dir(REPO_ROOT / "kaoyan") else 1
    if args.file:
        return 0 if compile_tikz_source(args.file, args.dark_output, args.light_output) else 1
    if args.dir:
        return 0 if compile_all_in_dir(args.dir) else 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
