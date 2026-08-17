#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=============================================================================
Exam Archive 全架构规范性核验脚本 (Conformity to exam_source_conversion_spec.md)
=============================================================================
迁移完成后只接受 kaoyan/archives/* 与 kaoyan/00_system/exam_profiles/* Canonical 路径。
"""

import os
import json
import re
import argparse
import xml.etree.ElementTree as ET

def main():
    parser = argparse.ArgumentParser(description="Exam Archive 规范校验工具")
    parser.add_argument('--exam', choices=['408', 'math1'], default='408', help="选择校验考试科目")
    parser.add_argument('--archive-dir', type=str, help="自定义真题库根目录")
    parser.add_argument('--quiet', action='store_true', help="成功年份不逐条展开；保留错误与最终汇总")
    args = parser.parse_args()

    exam_type = args.exam
    if args.archive_dir:
        root_dir = os.path.abspath(args.archive_dir)
    else:
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../../archives/{exam_type}'))

    profile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'../exam_profiles/{exam_type}.json'))
    if not os.path.isdir(root_dir):
        parser.error(f"Canonical archive root not found: {root_dir}")
    if not os.path.isfile(profile_path):
        parser.error(f"Canonical exam profile not found: {profile_path}")

    with open(profile_path, 'r', encoding='utf-8') as f:
        profile = json.load(f)

    years = sorted([d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and "年真题" in d])

    total_issues = 0
    year_stats = []

    # Root-level machine index is optional, but once present its contract paths must resolve.
    archive_index_path = os.path.join(root_dir, "archive.json")
    if os.path.isfile(archive_index_path):
        try:
            with open(archive_index_path, 'r', encoding='utf-8') as f:
                archive_index = json.load(f)
            for key in ("exam_profile", "conversion_spec"):
                raw_path = archive_index.get(key)
                if raw_path:
                    resolved = os.path.abspath(os.path.join(root_dir, raw_path))
                    if not os.path.exists(resolved):
                        print(f"❌ [archive.json] {key} points to missing target: {raw_path}")
                        total_issues += 1
        except Exception as e:
            print(f"❌ [archive.json] parse error: {e}")
            total_issues += 1

    for y in years:
        ydir = os.path.join(root_dir, y)
        y_num = re.search(r'\d{4}', y).group(0)
        y_int = int(y_num)
        issues = []

        # 1. Check required files
        main_md_files = [f for f in os.listdir(ydir) if f.endswith('.md') and not f.startswith('q') and f != 'README.md' and not f.startswith('00_')]
        if not main_md_files:
            issues.append("Missing canonical main markdown file")
            main_md_path = ""
        else:
            if len(main_md_files) > 1:
                issues.append(f"Multiple canonical main markdown candidates: {sorted(main_md_files)}")
            main_md_path = os.path.join(ydir, main_md_files[0])
            # Check Zero-Deviation H1 Contract
            with open(main_md_path, 'r', encoding='utf-8') as mf:
                h1 = ""
                for line in mf:
                    if line.startswith('# '):
                        h1 = line.strip()
                        break
            expected_h1 = f"# {os.path.splitext(main_md_files[0])[0]}"
            if h1 != expected_h1:
                issues.append(f"H1 vs Filename mismatch: '{h1}' != '{expected_h1}'")

        exam_json_path = os.path.join(ydir, "exam.json")
        readme_path = os.path.join(ydir, "README.md")
        assets_dir = os.path.join(ydir, "assets")
        light_dir = os.path.join(assets_dir, "light")

        if not main_md_path or not os.path.exists(main_md_path):
            if "Missing canonical main markdown file" not in issues:
                issues.append("Missing canonical main markdown file")
        # 1. Basic structural files
        if not os.path.exists(exam_json_path):
            issues.append("Missing exam.json")

        if exam_type == '408':
            expected_q_count = 47
            expected_total_score = 150
        else:
            if y_int >= 2021:
                expected_q_count = 22
            elif y_int == 2007:
                expected_q_count = 24
            elif 2008 <= y_int <= 2020:
                expected_q_count = 23
            else:
                expected_q_count = None  # 1987~2006 由试卷本身自洽定义
            expected_total_score = 100 if y_int <= 2002 else 150

        has_figures = False

        # 2. Check exam.json
        ej = {}
        if os.path.exists(exam_json_path):
            try:
                with open(exam_json_path, 'r', encoding='utf-8') as f:
                    ej = json.load(f)
                if ej.get('exam_id') != f"{exam_type}-{y_num}":
                    issues.append(f"exam.json exam_id mismatch: {ej.get('exam_id')} != {exam_type}-{y_num}")
                if ej.get('profile_id') != exam_type:
                    issues.append(f"exam.json profile_id mismatch: {ej.get('profile_id')} != {exam_type}")
                if expected_q_count is not None and ej.get('question_count') != expected_q_count:
                    issues.append(f"exam.json question_count: {ej.get('question_count')} != {expected_q_count}")
                if ej.get('total_score') != expected_total_score:
                    issues.append(f"exam.json total_score: {ej.get('total_score')} != {expected_total_score}")
                if ej.get('year') != int(y_num):
                    issues.append(f"exam.json year: {ej.get('year')} != {y_num}")
                has_figures = bool(ej.get('figures') or ej.get('figure_assets'))
            except Exception as e:
                issues.append(f"exam.json parse error: {e}")

        # 3. Check assets only if year has figures or assets/ directory exists
        dark_count = 0
        if has_figures and not os.path.exists(assets_dir):
            issues.append("Year has figures but missing assets/ directory")
        elif os.path.exists(assets_dir):
            dark_svgs = set()
            light_svgs = set()
            if not os.path.exists(light_dir):
                issues.append("Missing assets/light/ directory")
            else:
                dark_svgs = set([f for f in os.listdir(assets_dir) if f.endswith('.svg')])
                light_svgs = set([f for f in os.listdir(light_dir) if f.endswith('.svg')])
                dark_count = len(dark_svgs)

                diff_d = dark_svgs - light_svgs
                diff_l = light_svgs - dark_svgs
                if diff_d:
                    issues.append(f"Dark SVGs missing in light/: {diff_d}")
                if diff_l:
                    issues.append(f"Light SVGs missing in dark/: {diff_l}")

                for s in dark_svgs:
                    try:
                        ET.parse(os.path.join(assets_dir, s))
                    except Exception as e:
                        issues.append(f"Dark SVG XML error in {s}: {e}")
                for s in light_svgs:
                    try:
                        ET.parse(os.path.join(light_dir, s))
                    except Exception as e:
                        issues.append(f"Light SVG XML error in {s}: {e}")

            # Check assets/src/ TikZ sources if present
            src_dir = os.path.join(assets_dir, "src")
            if os.path.exists(src_dir):
                tex_files = [f for f in os.listdir(src_dir) if f.endswith('.tex')]
                for tf in tex_files:
                    svg_counterpart = f"{os.path.splitext(tf)[0]}.svg"
                    if svg_counterpart not in dark_svgs:
                        issues.append(f"TikZ source {tf} missing compiled Dark SVG: {svg_counterpart}")
                    if svg_counterpart not in light_svgs:
                        issues.append(f"TikZ source {tf} missing compiled Light SVG: {svg_counterpart}")

        # 4. Check Markdown question files
        q_files = [f for f in os.listdir(ydir) if re.match(r'^q\d{2}_.*\.md$', f)]
        target_count = expected_q_count if expected_q_count is not None else ej.get('question_count', len(q_files))
        if len(q_files) != target_count:
            issues.append(f"Question markdown count mismatch: {len(q_files)} != {target_count}")

        # 5. Check markdown asset links
        for qf in q_files:
            qfp = os.path.join(ydir, qf)
            with open(qfp, 'r', encoding='utf-8') as f:
                content = f.read()
            links = re.findall(r'!\[[^\]]*\]\(\./assets/([^\)]+\.svg)\)', content)
            for lk in links:
                if not os.path.exists(os.path.join(assets_dir, lk)):
                    issues.append(f"Broken asset link in {qf}: ./assets/{lk}")

        # 6. Derived solution frontmatter must resolve back to this year's Canonical Source.
        solutions_dir = os.path.join(ydir, "solutions")
        if os.path.isdir(solutions_dir) and main_md_path:
            canonical_main = os.path.abspath(main_md_path)
            for solution_name in sorted(f for f in os.listdir(solutions_dir) if re.match(r'^q\d{2}\.md$', f)):
                solution_path = os.path.join(solutions_dir, solution_name)
                with open(solution_path, 'r', encoding='utf-8') as f:
                    solution_text = f.read()
                source_match = re.search(r'^source_exam:\s*(.+?)\s*$', solution_text, re.MULTILINE)
                if not source_match:
                    issues.append(f"Solution {solution_name} missing source_exam frontmatter")
                else:
                    source_ref = source_match.group(1).strip().strip('"\'')
                    source_resolved = os.path.abspath(os.path.join(solutions_dir, source_ref))
                    if not os.path.exists(source_resolved):
                        issues.append(f"Solution {solution_name} broken source_exam: {source_ref}")
                    elif source_resolved != canonical_main:
                        issues.append(f"Solution {solution_name} source_exam is not this year's Canonical main: {source_ref}")

                legacy_match = re.search(r'^legacy_reference:\s*(.+?)\s*$', solution_text, re.MULTILINE)
                if legacy_match:
                    legacy_ref = legacy_match.group(1).strip().strip('"\'')
                    legacy_resolved = os.path.abspath(os.path.join(solutions_dir, legacy_ref))
                    if not os.path.exists(legacy_resolved):
                        issues.append(f"Solution {solution_name} broken legacy_reference: {legacy_ref}")

                # Obsidian relative wiki links are also executable navigation and must resolve.
                for wiki_raw in re.findall(r'\[\[([^\]]+)\]\]', solution_text):
                    wiki_target = wiki_raw.split('|', 1)[0].split('#', 1)[0].strip()
                    if not wiki_target.startswith('.'):
                        continue
                    wiki_path = os.path.abspath(os.path.join(solutions_dir, wiki_target))
                    candidates = [wiki_path]
                    if not os.path.splitext(wiki_path)[1]:
                        candidates.append(wiki_path + '.md')
                    if not any(os.path.exists(candidate) for candidate in candidates):
                        issues.append(f"Solution {solution_name} broken relative wiki link: {wiki_target}")

        if issues:
            total_issues += len(issues)
            print(f"❌ [{y}] 发现 {len(issues)} 处违规/问题:")
            for iss in issues:
                print(f"    - {iss}")
            year_stats.append((y, target_count, len(q_files), dark_count, f"❌ {len(issues)} 处待修"))
        else:
            year_stats.append((y, target_count, len(q_files), dark_count, "✅ 完美合规"))

    print("\n" + "="*70)
    print(f"{exam_type.upper()}_Exam_Archive 整体架构合规性报告 (Conformity Report)")
    print("="*70)
    if not args.quiet:
        for y, tc, qc, sc, status in year_stats:
            print(f"{y:<14} | {tc}道分题: {qc}/{tc} | SVG题图(暗/亮配对): {sc}对 | {status}")
    print("="*70)
    print(f"总计年份: {len(years)} 年 | 违规/异常数: {total_issues}")
    print("="*70)
    return 1 if total_issues else 0


if __name__ == '__main__':
    raise SystemExit(main())
