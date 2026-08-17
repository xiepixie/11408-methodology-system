#!/usr/bin/env python3
"""Teaching Domain Evergreen Hygiene Audit.

This script audits Teaching-domain hygiene invariants:
1. Zero generated LaTeX artifacts in teaching/ content trees.
2. Zero temporary/build scratch directories in teaching/.
3. Zero derived PDFs in public pool/topic source trees.

Cross-domain dependency and Kaoyan repository integrity are owned by their respective gates; this script does not pretend to validate them.

Usage:
    python3 teaching/audit_hygiene.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TEACHING_ROOT = REPO_ROOT / "teaching"

GENERATED_SUFFIXES = {
    ".aux",
    ".log",
    ".out",
    ".toc",
    ".xdv",
    ".synctex",
    ".synctex.gz",
    ".fls",
    ".fdb_latexmk",
    ".nav",
    ".snm",
    ".vrb",
    ".bbl",
    ".blg",
    ".synctex(busy)",
}


def audit_hygiene() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    # Single pass traversal for files and directories
    for path in TEACHING_ROOT.rglob("*"):
        if path.is_dir():
            if path.name in {"__pycache__", "tmp", ".venv"} or path.name.startswith("tmp_"):
                errors.append(f"Quarantined temporary directory found in content tree: {path.relative_to(REPO_ROOT)}")
            continue

        if not path.is_file():
            continue

        # Skip hidden files
        if any(part.startswith(".") for part in path.parts):
            continue

        for gen_ext in GENERATED_SUFFIXES:
            if path.name.endswith(gen_ext):
                errors.append(f"Generated build artifact detected: {path.relative_to(REPO_ROOT)}")

        # Check for stray PDFs in pool or topics
        if path.suffix == ".pdf":
            rel = path.relative_to(TEACHING_ROOT)
            if rel.parts[0] in ("pool", "topics") and "legacy" not in rel.parts:
                warnings.append(f"Stray PDF in active source directory (should be derived elsewhere): {path.relative_to(REPO_ROOT)}")

    return errors, warnings


def main() -> int:
    print("=" * 80)
    print("Teaching Domain Evergreen Hygiene Audit")
    print("=" * 80)

    errors, warnings = audit_hygiene()

    if warnings:
        print("\nWARNINGS:")
        for warn in warnings:
            print(f"  - {warn}")

    if errors:
        print("\nERRORS:")
        for err in errors:
            print(f"  - {err}")
        print("-" * 80)
        print(f"FAILED: {len(errors)} hygiene violation(s) found.")
        return 1

    print("SUCCESS: 0 hygiene violations found. Teaching content tree is clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
