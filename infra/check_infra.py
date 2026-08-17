#!/usr/bin/env python3
"""I.P.A.R.A Infra steady-state verification gate.

This gate proves machine-checkable invariants owned by ``infra/``:
1. Canonical LaTeX/script public entrypoints exist.
2. ``ipara.sty`` remains a thin Lesson compatibility shim.
3. Standard/Margin Handbook wrappers consume the same semantic body.
4. Both Handbook profiles compile with zero final-pass diagnostics.
5. The generic TikZ->SVG mechanism produces valid dark/light SVGs from an
   explicit temporary source without touching repository content.

Domain policy belongs to ``teaching/`` and ``kaoyan/`` and is intentionally
not reimplemented here.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


INFRA_ROOT = Path(__file__).resolve().parent
REPO_ROOT = INFRA_ROOT.parent
LATEX_ROOT = INFRA_ROOT / "latex"
SCRIPTS_ROOT = INFRA_ROOT / "scripts"
COMPILER = SCRIPTS_ROOT / "compile_tex.py"
TIKZ_COMPILER = SCRIPTS_ROOT / "compile_tikz_to_svg.py"

REQUIRED_PATHS = (
    LATEX_ROOT / "ipara-core.sty",
    LATEX_ROOT / "ipara-handbook.cls",
    LATEX_ROOT / "ipara.sty",
    LATEX_ROOT / "legacy" / "ipara-legacy.sty",
    LATEX_ROOT / "specimens" / "handbook-body.tex",
    LATEX_ROOT / "specimens" / "handbook.tex",
    LATEX_ROOT / "specimens" / "handbook-margin.tex",
    COMPILER,
    TIKZ_COMPILER,
)


def fail(message: str) -> None:
    print(f"[ERROR] {message}")


def check_required_paths() -> list[str]:
    return [f"Missing canonical infra asset: {path.relative_to(REPO_ROOT)}" for path in REQUIRED_PATHS if not path.is_file()]


def check_lesson_shim() -> list[str]:
    path = LATEX_ROOT / "ipara.sty"
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if "legacy/ipara-legacy.sty" not in text:
        errors.append("infra/latex/ipara.sty no longer routes to the Lesson compatibility implementation")
    if "\\RequirePackage{" in text:
        errors.append("infra/latex/ipara.sty must not accumulate package implementation logic")
    return errors


def check_handbook_specimen_contract() -> list[str]:
    standard = (LATEX_ROOT / "specimens" / "handbook.tex").read_text(encoding="utf-8")
    margin = (LATEX_ROOT / "specimens" / "handbook-margin.tex").read_text(encoding="utf-8")
    body = (LATEX_ROOT / "specimens" / "handbook-body.tex").read_text(encoding="utf-8")
    errors: list[str] = []

    if "profile=standard" not in standard:
        errors.append("handbook.tex must explicitly exercise profile=standard")
    if "profile=margin" not in margin:
        errors.append("handbook-margin.tex must explicitly exercise profile=margin")
    for name, text in (("handbook.tex", standard), ("handbook-margin.tex", margin)):
        if text.count("\\input{handbook-body.tex}") != 1:
            errors.append(f"{name} must consume handbook-body.tex exactly once")
    if "\\documentclass" in body:
        errors.append("handbook-body.tex must remain class-agnostic semantic content")
    return errors


def run_handbook_regression(tmp_root: Path) -> list[str]:
    errors: list[str] = []
    for specimen in ("handbook.tex", "handbook-margin.tex"):
        source = LATEX_ROOT / "specimens" / specimen
        outdir = tmp_root / source.stem
        result = subprocess.run(
            [sys.executable, str(COMPILER), str(source), "--outdir", str(outdir), "--warnings-as-errors"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            errors.append(
                f"Handbook regression failed for {source.relative_to(REPO_ROOT)}:\n"
                f"{result.stdout.strip()}\n{result.stderr.strip()}"
            )
            continue
        expected_pdf = outdir / f"{source.stem}.pdf"
        if not expected_pdf.is_file():
            errors.append(f"Handbook regression did not produce {expected_pdf}")
    return errors


def run_tikz_regression(tmp_root: Path) -> list[str]:
    smoke_source = tmp_root / "tikz-smoke.tex"
    dark_svg = tmp_root / "tikz-smoke-dark.svg"
    light_svg = tmp_root / "tikz-smoke-light.svg"
    smoke_source.write_text(
        "\\begin{tikzpicture}\n"
        "  \\draw[->] (0,0) -- (1,0);\n"
        "  \\node at (0.5,0.25) {Smoke};\n"
        "\\end{tikzpicture}\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [
            sys.executable,
            str(TIKZ_COMPILER),
            str(smoke_source),
            "--dark-output",
            str(dark_svg),
            "--light-output",
            str(light_svg),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return [f"TikZ->SVG regression failed:\n{result.stdout.strip()}\n{result.stderr.strip()}"]

    errors: list[str] = []
    for svg in (dark_svg, light_svg):
        if not svg.is_file():
            errors.append(f"TikZ regression missing output: {svg.name}")
            continue
        try:
            ET.parse(svg)
        except ET.ParseError as exc:
            errors.append(f"TikZ regression produced invalid XML ({svg.name}): {exc}")
    return errors


def main() -> int:
    print("=" * 80)
    print("I.P.A.R.A Infra Steady-State Gate")
    print("=" * 80)

    errors: list[str] = []
    errors.extend(check_required_paths())
    if not errors:
        errors.extend(check_lesson_shim())
        errors.extend(check_handbook_specimen_contract())

    if not errors:
        with tempfile.TemporaryDirectory(prefix="ipara_infra_gate_") as tmp:
            tmp_root = Path(tmp)
            errors.extend(run_handbook_regression(tmp_root))
            errors.extend(run_tikz_regression(tmp_root))

    if errors:
        for error in errors:
            fail(error)
        print("-" * 80)
        print(f"FAILED: {len(errors)} infra invariant(s) violated.")
        return 1

    print("Canonical entrypoints : OK")
    print("Lesson thin shim      : OK")
    print("Handbook same-body    : OK")
    print("Standard/Margin build : OK (warnings-as-errors)")
    print("TikZ dark/light SVG   : OK")
    print("-" * 80)
    print("PASSED: all infra steady-state invariants hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
