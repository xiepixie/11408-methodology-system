#!/usr/bin/env python3
"""Daily Reading compilation engine.

This tool provides single-article, template, and batch compilation for the
Daily Reading system. It sets up the domain-specific search path for
``ipara-reading.sty`` and calls the shared compiler ``infra/scripts/compile_tex.py``.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

SYSTEM_TOOLS_DIR = Path(__file__).resolve().parent
SYSTEM_DIR = SYSTEM_TOOLS_DIR.parent
DAILY_READING_ROOT = SYSTEM_DIR.parent
REPO_ROOT = DAILY_READING_ROOT.parents[3]
TEMPLATES_DIR = SYSTEM_DIR / "templates"
ARTICLES_DIR = DAILY_READING_ROOT / "01_articles"
COMPILER_SCRIPT = REPO_ROOT / "infra" / "scripts" / "compile_tex.py"

sys.path.insert(0, str(REPO_ROOT / "infra" / "scripts"))
try:
    from compile_tex import clean_aux_files, compile_single_tex
except ImportError:
    compile_single_tex = None  # type: ignore[assignment]
    clean_aux_files = None  # type: ignore[assignment]


def set_daily_reading_env() -> None:
    """Inject Daily Reading templates directory into TEXINPUTS."""
    existing = os.environ.get("TEXINPUTS", "")
    os.environ["TEXINPUTS"] = f".:{TEMPLATES_DIR}:{existing}:"


def compile_target(
    tex_path: Path,
    *,
    warnings_as_errors: bool = False,
) -> bool:
    """Compile a single reading_view.tex or template."""
    tex_path = tex_path.resolve()
    if not tex_path.is_file():
        print(f"[ERROR] TeX file not found: {tex_path}")
        return False

    set_daily_reading_env()
    if compile_single_tex is None:
        print("[ERROR] Failed to import compile_single_tex from infra/scripts/compile_tex.py")
        return False

    success = compile_single_tex(
        tex_path,
        warnings_as_errors=warnings_as_errors,
    )
    if clean_aux_files:
        clean_aux_files(tex_path.parent, verbose=False)
    return success


def find_article_tex_files(year: str | None = None) -> list[Path]:
    """Find all reading_view.tex files in 01_articles."""
    search_root = ARTICLES_DIR / year if year else ARTICLES_DIR
    if not search_root.is_dir():
        return []
    return sorted(search_root.rglob("reading_view.tex"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile Daily Reading articles or template.")
    parser.add_argument(
        "target",
        nargs="?",
        help="Path to an article directory, a .tex file, or omit when using flags.",
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Compile 00_system/templates/reading_view_template.tex.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Compile all reading_view.tex files under 01_articles/.",
    )
    parser.add_argument(
        "--year",
        help="Filter articles by year (e.g. 2026).",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Treat LaTeX warnings as fatal errors.",
    )

    args = parser.parse_args()

    if args.template:
        template_tex = TEMPLATES_DIR / "reading_view_template.tex"
        print(f"[Daily Reading] Compiling template: {template_tex.relative_to(REPO_ROOT)}")
        ok = compile_target(template_tex, warnings_as_errors=args.warnings_as_errors)
        return 0 if ok else 1

    if args.all or args.year:
        tex_files = find_article_tex_files(args.year)
        if not tex_files:
            print(f"[Daily Reading] No reading_view.tex files found (year={args.year}).")
            return 0
        print(f"[Daily Reading] Found {len(tex_files)} articles to compile.")
        failures = 0
        for tex in tex_files:
            print(f"\n--- Compiling {tex.relative_to(REPO_ROOT)} ---")
            if not compile_target(tex, warnings_as_errors=args.warnings_as_errors):
                failures += 1
        if failures > 0:
            print(f"\n[Daily Reading] {failures}/{len(tex_files)} compilation(s) failed.")
            return 1
        print(f"\n[Daily Reading] All {len(tex_files)} article(s) compiled successfully.")
        return 0

    if args.target:
        target_path = Path(args.target).resolve()
        if target_path.is_dir():
            target_path = target_path / "reading_view.tex"
        if not target_path.is_file():
            print(f"[ERROR] Target is not a valid TeX file: {target_path}")
            return 1
        ok = compile_target(target_path, warnings_as_errors=args.warnings_as_errors)
        return 0 if ok else 1

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
