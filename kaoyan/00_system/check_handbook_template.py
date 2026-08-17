#!/usr/bin/env python3
"""Kaoyan Handbook Forward Template hard gate.

The global Family implementation belongs to infra/. This gate owns only the
Kaoyan rule that *new* Topic/Bridge/Integration Handbooks start from the formal
Handbook Family rather than the legacy Prototype compatibility surface.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parent
KAOYAN_ROOT = SYSTEM_ROOT.parent
REPO_ROOT = KAOYAN_ROOT.parent
TEMPLATE = SYSTEM_ROOT / "handbook_template.tex"
COMPILER = REPO_ROOT / "infra" / "scripts" / "compile_tex.py"

FORWARD_CLASS = r"\documentclass[profile=standard,twoside=false]{ipara-handbook}"
FORBIDDEN_COMPATIBILITY_TOKENS = (
    r"\usepackage{ipara-handbook}",
    r"\begin{corebox}",
    r"\begin{methodbox}",
    r"\begin{warnbox}",
    r"\begin{examplebox}",
    r"\begin{boundarybox}",
)
REQUIRED_SEMANTIC_TOKENS = (
    r"\begin{mentalmodel}",
    r"\begin{mechanism}",
    r"\begin{boundary}",
    r"\begin{warning}",
)


def main() -> int:
    print("=" * 80)
    print("Kaoyan Handbook Forward Template Gate")
    print("=" * 80)

    errors: list[str] = []
    if not TEMPLATE.is_file():
        errors.append("Missing kaoyan/00_system/handbook_template.tex")
    if not COMPILER.is_file():
        errors.append("Missing infra/scripts/compile_tex.py")

    if not errors:
        text = TEMPLATE.read_text(encoding="utf-8")
        if FORWARD_CLASS not in text:
            errors.append("Forward template must use profile=standard ipara-handbook class")
        for token in FORBIDDEN_COMPATIBILITY_TOKENS:
            if token in text:
                errors.append(f"Forward template contains Prototype compatibility API: {token}")
        for token in REQUIRED_SEMANTIC_TOKENS:
            if token not in text:
                errors.append(f"Forward template missing Canonical semantic API: {token}")

    if not errors:
        with tempfile.TemporaryDirectory(prefix="ipara_kaoyan_template_gate_") as tmpdir:
            result = subprocess.run(
                [
                    sys.executable,
                    str(COMPILER),
                    str(TEMPLATE),
                    "--outdir",
                    tmpdir,
                    "--warnings-as-errors",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                errors.append(
                    "Forward template strict compilation failed:\n"
                    + result.stdout.strip()
                    + "\n"
                    + result.stderr.strip()
                )
            elif not (Path(tmpdir) / "handbook_template.pdf").is_file():
                errors.append("Forward template compiler returned success without PDF output")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        print("-" * 80)
        print(f"FAILED: {len(errors)} forward-template invariant(s) violated.")
        return 1

    print("Formal Standard class : OK")
    print("Canonical semantic API: OK")
    print("Strict XeLaTeX build  : OK")
    print("-" * 80)
    print("PASSED: Kaoyan Forward Template is executable and canonical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
