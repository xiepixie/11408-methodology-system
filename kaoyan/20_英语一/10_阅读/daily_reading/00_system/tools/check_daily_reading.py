#!/usr/bin/env python3
"""Daily Reading repository integrity gate.

Validates structural invariants, Cornell dual-column link integrity,
article purity, build cleanliness, and template compilability for
the English Daily Reading system.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SYSTEM_TOOLS_DIR = Path(__file__).resolve().parent
SYSTEM_DIR = SYSTEM_TOOLS_DIR.parent
DAILY_READING_ROOT = SYSTEM_DIR.parent
REPO_ROOT = DAILY_READING_ROOT.parents[3]
TEMPLATES_DIR = SYSTEM_DIR / "templates"
ARTICLES_DIR = DAILY_READING_ROOT / "01_articles"
COMPILER_TOOL = SYSTEM_TOOLS_DIR / "compile_daily_reading.py"

ARTICLE_DIR_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-zA-Z0-9_-]+$")
KW_PATTERN = re.compile(r"\\kw\{[^}]*\}\{([^}]+)\}")
OBS_PATTERN = re.compile(r"\\obs\{[^}]*\}\{([^}]+)\}")
NOTEITEM_PATTERN = re.compile(r"\\noteitem\{([^}]+)\}")
NOTEOBS_PATTERN = re.compile(r"\\noteobs\{([^}]+)\}")

AUX_EXTENSIONS = {
    ".aux", ".log", ".out", ".toc", ".synctex", ".synctex.gz", ".xdv",
    ".fls", ".fdb_latexmk",
}

FORBIDDEN_ARTICLE_MD_TOKENS = (
    "## 单词讲解",
    "## 词汇精析",
    "## 长难句解析",
    "## 全文翻译",
    "## AI 点评",
    "## 参考复述",
    "\\kw{",
    "\\noteitem{",
)

REQUIRED_SECTION_PATTERNS = (
    (r"\\readingsection\{一、.*?双栏.*?\}", "一、双栏精读"),
    (r"\\readingsection\{二、.*?结构.*?\}", "二、文章结构与主旨复原"),
    (r"\\readingsection\{三、.*?(语[音调]|韵律).*?\}", "三、语音与韵律训练"),
    (r"\\readingsection\{四、.*?脱稿.*?\}", "四、脱稿输出与对照"),
    (r"\\readingsection\{五、.*?对谈.*?\}", "五、对谈与关键反馈"),
    (r"\\readingsection\{六、.*?沉淀.*?\}", "六、本篇沉淀与跨层引用"),
)


def rel_path(p: Path) -> Path:
    try:
        return p.relative_to(REPO_ROOT)
    except ValueError:
        return p


def check_build_cleanliness() -> list[str]:
    errors: list[str] = []
    for root, _, files in os.walk(DAILY_READING_ROOT):
        for f in files:
            path = Path(root) / f
            if path.suffix in AUX_EXTENSIONS or "synctex" in path.name:
                errors.append(f"Stray build artifact found: {rel_path(path)}")
    return errors


def check_templates() -> list[str]:
    errors: list[str] = []
    style_file = TEMPLATES_DIR / "ipara-reading.sty"
    template_tex = TEMPLATES_DIR / "reading_view_template.tex"

    if not style_file.is_file():
        errors.append(f"Missing style file: {rel_path(style_file)}")
    if not template_tex.is_file():
        errors.append(f"Missing template: {rel_path(template_tex)}")
    else:
        text = template_tex.read_text(encoding="utf-8")
        if "ipara-reading" not in text:
            errors.append("Template must load ipara-reading package")
        if "\\articleheader" not in text:
            errors.append("Template missing \\articleheader")

        for pattern, label in REQUIRED_SECTION_PATTERNS:
            if not re.search(pattern, text):
                errors.append(f"Template missing required section: {label} (pattern: {pattern})")
    return errors


def check_article_dir(article_dir: Path) -> list[str]:
    errors: list[str] = []
    rel = rel_path(article_dir)

    if not ARTICLE_DIR_PATTERN.match(article_dir.name):
        errors.append(f"Article directory name must match YYYY-MM-DD_<slug>: {rel}")

    article_md = article_dir / "article.md"
    reading_tex = article_dir / "reading_view.tex"
    reading_pdf = article_dir / "reading_view.pdf"

    if not article_md.is_file():
        errors.append(f"Missing article.md in: {rel}")
    else:
        md_text = article_md.read_text(encoding="utf-8")
        for token in FORBIDDEN_ARTICLE_MD_TOKENS:
            if token in md_text:
                errors.append(f"{rel_path(article_md)} contains forbidden preview spoiler: {token}")

    if not reading_tex.is_file():
        errors.append(f"Missing reading_view.tex in: {rel}")
    else:
        tex_text = reading_tex.read_text(encoding="utf-8")
        if "ipara-reading" not in tex_text:
            errors.append(f"{rel_path(reading_tex)} must use ipara-reading package")

        kw_ids = KW_PATTERN.findall(tex_text)
        obs_ids = OBS_PATTERN.findall(tex_text)
        note_ids = NOTEITEM_PATTERN.findall(tex_text)
        noteobs_ids = NOTEOBS_PATTERN.findall(tex_text)

        if len(note_ids) != len(set(note_ids)):
            duplicates = [x for x in note_ids if note_ids.count(x) > 1]
            errors.append(f"{rel_path(reading_tex)} contains duplicate \\noteitem IDs: {set(duplicates)}")

        if len(noteobs_ids) != len(set(noteobs_ids)):
            duplicates = [x for x in noteobs_ids if noteobs_ids.count(x) > 1]
            errors.append(f"{rel_path(reading_tex)} contains duplicate \\noteobs IDs: {set(duplicates)}")

        missing_notes = set(kw_ids) - set(note_ids)
        if missing_notes:
            errors.append(f"{rel_path(reading_tex)} has \\kw without matching \\noteitem: {missing_notes}")

        missing_obs_notes = set(obs_ids) - set(noteobs_ids)
        if missing_obs_notes:
            errors.append(f"{rel_path(reading_tex)} has \\obs without matching \\noteobs: {missing_obs_notes}")

    if not reading_pdf.is_file():
        errors.append(f"Missing compiled reading_view.pdf in: {rel}")

    return errors


def check_all_articles() -> list[str]:
    errors: list[str] = []
    if not ARTICLES_DIR.is_dir():
        return [f"Missing articles directory: {rel_path(ARTICLES_DIR)}"]

    article_dirs: list[Path] = []
    for year_dir in sorted(ARTICLES_DIR.iterdir()):
        if year_dir.is_dir() and year_dir.name.isdigit():
            for item in sorted(year_dir.iterdir()):
                if item.is_dir():
                    article_dirs.append(item)

    if not article_dirs:
        errors.append("No article directories found under 01_articles/YYYY/")
        return errors

    for adir in article_dirs:
        errors.extend(check_article_dir(adir))
    return errors


def check_smoke_compile() -> list[str]:
    errors: list[str] = []
    template_tex = TEMPLATES_DIR / "reading_view_template.tex"
    if not template_tex.is_file():
        return ["Template file missing for smoke compile"]

    result = subprocess.run(
        [
            sys.executable,
            str(COMPILER_TOOL),
            "--template",
            "--warnings-as-errors",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        errors.append(f"Template smoke compilation failed:\n{result.stdout.strip()}\n{result.stderr.strip()}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Daily Reading system invariants.")
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Run strict smoke compilation on template in addition to static checks.",
    )
    args = parser.parse_args()

    print("=" * 80)
    print("English Daily Reading Steady-State Gate")
    print("=" * 80)

    all_errors: list[str] = []
    all_errors.extend(check_build_cleanliness())
    all_errors.extend(check_templates())
    all_errors.extend(check_all_articles())

    if args.smoke and not all_errors:
        all_errors.extend(check_smoke_compile())

    # Ensure no aux files left in templates after smoke test
    template_pdf = TEMPLATES_DIR / "reading_view_template.pdf"
    if template_pdf.is_file():
        try:
            template_pdf.unlink()
        except OSError:
            pass

    if all_errors:
        print(f"[FAIL] Daily Reading gate failed with {len(all_errors)} error(s):")
        for err in all_errors:
            print(f"  [ERROR] {err}")
        return 1

    print("Template & Style     : OK")
    print("Article Hierarchy    : OK")
    print("Cornell Linkages     : OK")
    print("Build Cleanliness    : OK")
    if args.smoke:
        print("Template Compilation : OK")
    print("-" * 80)
    print("PASSED: all Daily Reading steady-state invariants hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
