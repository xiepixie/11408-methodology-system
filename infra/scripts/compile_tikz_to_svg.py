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

TIKZ_STANDALONE_TEMPLATE = r"""\documentclass[dvisvgm,tikz,border=8pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathreplacing,patterns}

\definecolor{themebg}{HTML}{__BG_HEX__}
\definecolor{themefg}{HTML}{__FG_HEX__}
\definecolor{themegray}{HTML}{__GRAY_HEX__}

\begin{document}
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
    is_full_doc = r"\documentclass" in src_code
    default_dark, default_light = default_outputs(source)
    dark_output = Path(out_dark_svg).resolve() if out_dark_svg else default_dark
    light_output = Path(out_light_svg).resolve() if out_light_svg else default_light
    latex_bin, dvisvgm_bin = get_tex_bin()
    env = build_environment(source.parent)

    themes = [
        ("dark", "30362d", "edf4e8", "9ea897", dark_output),
        ("light", "fafaf7", "111111", "666666", light_output),
    ]

    print(f"[tikz] {source.name} -> dark/light SVG")
    with tempfile.TemporaryDirectory(prefix="ipara-tikz-") as tmp:
        build_dir = Path(tmp)

        for theme_name, bg_hex, fg_hex, gray_hex, destination in themes:
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
            else:
                content = (
                    TIKZ_STANDALONE_TEMPLATE
                    .replace("__BG_HEX__", bg_hex)
                    .replace("__FG_HEX__", fg_hex)
                    .replace("__GRAY_HEX__", gray_hex)
                    .replace("__TIKZ_BODY__", src_code)
                )

            build_tex.write_text(content, encoding="utf-8")

            latex_result = subprocess.run(
                [latex_bin, "-interaction=nonstopmode", build_tex.name],
                cwd=build_dir,
                capture_output=True,
                text=True,
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
            )
            if dvisvgm_result.returncode != 0:
                print(f"[error] dvisvgm failed ({theme_name})\n{dvisvgm_result.stdout}\n{dvisvgm_result.stderr}")
                return False

            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(build_dir / svg_name, destination)
            print(f"  [{theme_name}] {destination}")

    return True


def compile_all_in_dir(directory: str | Path) -> bool:
    """Compile every TeX source below an explicit directory."""
    root = Path(directory).resolve()
    files = sorted(path for path in root.rglob("*.tex") if not path.name.endswith(".tmp.tex"))
    print(f"[scan] {root}: {len(files)} TeX sources")
    ok = True
    for source in files:
        ok &= compile_tikz_source(source)
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description="TikZ -> paired semantic SVG compiler")
    parser.add_argument("file", nargs="?", help="TikZ .tex source")
    parser.add_argument("--dir", help="explicit directory to compile recursively")
    parser.add_argument("--dark-output", help="custom dark SVG output path (single-file mode)")
    parser.add_argument("--light-output", help="custom light SVG output path (single-file mode)")
    args = parser.parse_args()

    if args.file:
        return 0 if compile_tikz_source(args.file, args.dark_output, args.light_output) else 1
    if args.dir:
        return 0 if compile_all_in_dir(args.dir) else 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
