#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_math1_exam_source.py
==========================
数学一 Canonical Exam Source 的语义洁净度检查。

职责边界：
- Archive 目录结构、题量、SVG 暗/亮配对与 solution 回链由
  validate_exam_archive_spec.py 负责；
- 本脚本只验证每年 exam.json 指向的唯一主题面是否自洽、无答案解析泄露、
  Frontmatter/H1 是否正确，以及主题面图片引用是否存在。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


KAOYAN_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_ROOT = KAOYAN_ROOT / "archives" / "math1"
PROFILE_PATH = KAOYAN_ROOT / "00_system" / "exam_profiles" / "math1.json"
MAIN_EXCLUDE_PREFIXES = ("q", "00_")
ANSWER_PATTERNS = (r"【答案】", r"【解析】", r"【分析】", r"答案速查", r"【解】")


def _year_dirs() -> list[Path]:
    return sorted(
        (path for path in ARCHIVE_ROOT.iterdir() if path.is_dir() and re.fullmatch(r"\d{4}年真题", path.name)),
        key=lambda path: int(path.name[:4]),
    )


def _main_candidates(year_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in year_dir.glob("*.md")
        if path.name != "README.md" and not path.name.startswith(MAIN_EXCLUDE_PREFIXES)
    )


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def check_math1_archive(*, quiet: bool = False) -> bool:
    print("=" * 72)
    print("Math1 Canonical Exam Source Semantic Gate")
    print("=" * 72)

    if not ARCHIVE_ROOT.is_dir():
        print(f"[FATAL] Archive root not found: {ARCHIVE_ROOT}")
        return False
    if not PROFILE_PATH.is_file():
        print(f"[FATAL] Canonical profile not found: {PROFILE_PATH}")
        return False

    year_dirs = _year_dirs()
    print(f"[*] 年度目录: {len(year_dirs)}")

    total_errors = 0
    total_warnings = 0

    for year_dir in year_dirs:
        year = int(year_dir.name[:4])
        errors: list[str] = []
        warnings: list[str] = []
        exam_json_path = year_dir / "exam.json"
        exam_data: dict = {}

        if not exam_json_path.is_file():
            errors.append("缺失 exam.json")
        else:
            try:
                exam_data = _read_json(exam_json_path)
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"exam.json 解析失败: {exc}")

        for field in ("schema_version", "exam_id", "profile_id", "year", "title", "main_file", "status", "total_score"):
            if exam_data and field not in exam_data:
                errors.append(f"exam.json 缺失必填字段: {field}")

        if exam_data:
            if exam_data.get("year") != year:
                errors.append(f"exam.json year={exam_data.get('year')} 与目录年份 {year} 不一致")
            if exam_data.get("profile_id") != "math1":
                errors.append(f"exam.json profile_id={exam_data.get('profile_id')}，期望 math1")

        main_file_name = str(exam_data.get("main_file", "")).strip()
        main_path = year_dir / main_file_name if main_file_name else None
        candidates = _main_candidates(year_dir)

        if len(candidates) != 1:
            errors.append(f"年度主题面候选必须唯一，当前为 {[path.name for path in candidates]}")
        if not main_file_name:
            errors.append("exam.json 缺少有效 main_file")
        elif main_path is None or not main_path.is_file():
            errors.append(f"exam.json main_file 不存在: {main_file_name}")
        elif candidates and main_path.resolve() != candidates[0].resolve():
            errors.append(f"exam.json main_file 不是年度唯一主题面: {main_file_name}")

        md_text = ""
        if main_path is not None and main_path.is_file():
            md_text = main_path.read_text(encoding="utf-8")
            expected_title = main_path.stem
            h1_match = re.search(r"^#\s*(.*?)$", md_text, flags=re.MULTILINE)
            if not h1_match:
                errors.append(f"{main_path.name} 缺失 H1")
            elif h1_match.group(1).strip() != expected_title:
                errors.append(
                    f"H1 与文件名不一致: '# {h1_match.group(1).strip()}' != '{expected_title}'"
                )

            if not md_text.startswith("---"):
                errors.append("主题面缺失 YAML Frontmatter")
            else:
                fm_match = re.match(r"^---\n(.*?)\n---", md_text, re.DOTALL)
                if not fm_match:
                    errors.append("YAML Frontmatter 未正确闭合")
                else:
                    fm = fm_match.group(1)
                    if "type: exam-source" not in fm:
                        errors.append("Frontmatter 缺失 type: exam-source")
                    if f"exam_id: math1-{year}" not in fm:
                        errors.append(f"Frontmatter exam_id 错误，期望 math1-{year}")
                    if "exam_profile: math1" not in fm:
                        errors.append("Frontmatter exam_profile 错误，期望 math1")

            for pattern in ANSWER_PATTERNS:
                if re.search(pattern, md_text):
                    errors.append(f"主题面发现答案/解析泄露: {pattern}")

            for ref in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md_text):
                ref_clean = ref.strip().split()[0]
                if ref_clean.startswith(("http://", "https://", "data:")):
                    continue
                if not (year_dir / ref_clean).resolve().exists():
                    errors.append(f"主题面图片引用不存在: {ref_clean}")

        status = "PASS" if not errors and not warnings else ("WARN" if not errors else "FAIL")
        if errors:
            total_errors += len(errors)
            for error in errors:
                print(f"  [ERROR][{year}] {error}")
        if warnings:
            total_warnings += len(warnings)
            for warning in warnings:
                print(f"  [WARN][{year}] {warning}")
        if status == "PASS" and not quiet:
            print(f"  [PASS][{year}] {main_file_name}")

    print("-" * 72)
    print(f"完成: {len(year_dirs)} 年 | errors={total_errors} | warnings={total_warnings}")
    print("-" * 72)
    return total_errors == 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Math1 Canonical Exam Source semantic gate")
    parser.add_argument("--quiet", action="store_true", help="成功年份不逐条展开；保留错误与最终汇总")
    args = parser.parse_args()
    return 0 if check_math1_archive(quiet=args.quiet) else 1


if __name__ == "__main__":
    raise SystemExit(main())
