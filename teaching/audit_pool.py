#!/usr/bin/env python3
"""Teaching Question Pool Steady-State Integrity Audit.

This script audits the canonical mathematical question pool (teaching/pool/):
1. No-loss floor: the initial steady-state snapshot (138 questions across 9 subjects) may grow but must never shrink silently.
2. Taxonomy: subject folders and difficulty levels (基础, 中档, 难题).
3. Syntax & Macros: valid LaTeX macro declarations, unique macro stems.
4. Privacy Boundary: zero student names (刘亚博, 谭俊文) or individual facts.

Usage:
    python3 teaching/audit_pool.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
POOL_ROOT = REPO_ROOT / "teaching" / "pool"

NO_LOSS_FLOOR_TOPIC_COUNTS = {
    "集合": 1,
    "复数": 1,
    "数列": 2,
    "函数与图象": 4,
    "平面向量": 13,
    "概率与统计": 16,
    "解析几何": 19,
    "解三角形": 28,
    "立体几何": 54,
}
NO_LOSS_FLOOR_TOTAL = sum(NO_LOSS_FLOOR_TOPIC_COUNTS.values())

PERSONAL_FACT_RE = re.compile(r"学生得分率|刘亚博|谭俊文|本次课(?:次)?|已掌握")
STEM_MACRO_RE = re.compile(r"\\newcommand\{\\([A-Za-z0-9]+Stem)\}")
FORBIDDEN_ROUTE_RE = re.compile(r"comm" + r"on/(?:pool|ipara)|(?:\.\./)+ipara")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not POOL_ROOT.is_dir():
        print(f"[ERROR] Teaching pool directory missing: {POOL_ROOT}")
        return 1

    questions = sorted(POOL_ROOT.rglob("*.tex"))
    counts_by_topic: Counter[str] = Counter()
    macro_to_file: dict[str, Path] = {}

    for qpath in questions:
        rel_parts = qpath.relative_to(POOL_ROOT).parts
        if len(rel_parts) < 3:
            errors.append(f"Invalid pool taxonomy path: {qpath.relative_to(REPO_ROOT)} (expected [subject]/[difficulty]/q_*.tex)")
            continue

        topic = rel_parts[0]
        difficulty = rel_parts[1]
        counts_by_topic[topic] += 1

        if difficulty not in ("基础", "中档", "难题"):
            warnings.append(f"Non-standard difficulty level '{difficulty}': {qpath.relative_to(REPO_ROOT)}")

        text = qpath.read_text(encoding="utf-8", errors="ignore")

        # Privacy check
        privacy_match = PERSONAL_FACT_RE.search(text)
        if privacy_match:
            errors.append(f"Student privacy leak '{privacy_match.group(0)}' in public question: {qpath.relative_to(REPO_ROOT)}")

        # Legacy route check
        route_match = FORBIDDEN_ROUTE_RE.search(text)
        if route_match:
            errors.append(f"Legacy route reference in public question: {qpath.relative_to(REPO_ROOT)}")

        # Macro stem extraction
        macros = STEM_MACRO_RE.findall(text)
        if not macros:
            warnings.append(f"No standard \\q*Stem macro found: {qpath.relative_to(REPO_ROOT)}")
        for macro in macros:
            if macro in macro_to_file:
                errors.append(f"Duplicate macro stem \\{macro} in {qpath.name} (already in {macro_to_file[macro].name})")
            else:
                macro_to_file[macro] = qpath

    # Inventory baseline checks
    print("=" * 80)
    print("Teaching Question Pool Audit")
    print("=" * 80)
    print(f"{'Topic':<25} {'Expected':<10} {'Found':<10} {'Status':<10}")
    print("-" * 80)

    for topic, baseline in NO_LOSS_FLOOR_TOPIC_COUNTS.items():
        found = counts_by_topic[topic]
        status = "OK" if found >= baseline else "DEFICIT"
        print(f"{topic:<25} {baseline:<10} {found:<10} {status:<10}")
        if found < baseline:
            errors.append(f"Topic '{topic}' fell below steady-state no-loss floor: floor {baseline}, found {found}")

    for topic in sorted(set(counts_by_topic) - set(NO_LOSS_FLOOR_TOPIC_COUNTS)):
        print(f"{topic:<25} {0:<10} {counts_by_topic[topic]:<10} {'NEW':<10}")

    print("-" * 80)
    print(f"Total Questions: {len(questions)} / no-loss floor {NO_LOSS_FLOOR_TOTAL}")
    if len(questions) < NO_LOSS_FLOOR_TOTAL:
        errors.append(f"Pool fell below steady-state no-loss floor: floor {NO_LOSS_FLOOR_TOTAL}, found {len(questions)}")
    print(f"Unique Macro Stems: {len(macro_to_file)}")
    print("=" * 80)

    if errors:
        print("\nERRORS:")
        for err in errors:
            print(f"  - {err}")
        return 1

    if warnings:
        print("\nWARNINGS:")
        for warn in warnings:
            print(f"  - {warn}")

    print(f"SUCCESS: steady-state no-loss floor preserved; {len(questions)} current questions verified. All pool invariants hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
