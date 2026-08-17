#!/usr/bin/env python3
"""Teaching Topics Steady-State Integrity Audit.

This script audits canonical delivery topics (teaching/topics/):
1. No-loss floor: the initial steady-state snapshot may grow, but existing topic/source inventory must never shrink silently.
2. Privacy Boundary: zero student names (刘亚博, 谭俊文) in public topics.
3. Input Resolution: all \\input and \\include references must resolve.
4. Clean Dependencies: zero legacy routes.

Usage:
    python3 teaching/audit_topics.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TOPICS_ROOT = REPO_ROOT / "teaching" / "topics"

NO_LOSS_FLOOR_TOPIC_COUNTS = {
    "legacy": 6,
    "一元二次方程根的分布": 1,
    "三角函数_omega范围问题": 3,
    "三角函数_公式推导与几何直观": 4,
    "不等式专题": 3,
    "代数条件的几何意义": 1,
    "函数同构与指对同构": 1,
    "函数性态分析": 1,
    "函数的对称性与周期性": 3,
    "卷面表达_思路译为采分点": 3,
    "向量与函数_期末测试": 3,
    "圆锥曲线的代数结构与硬解定理": 2,
    "圆锥曲线的四种定义": 3,
    "复合方程根的个数": 1,
    "对数函数综合": 1,
    "平面向量_图解讲义": 3,
    "排列组合与概率_七题讲义": 4,
    "排列组合与概率_六题讲义": 4,
    "极值点偏移": 1,
    "特殊值与估算专题": 3,
    "立体几何": 2,
    "立体几何_几何直觉": 4,
    "立体几何_外接球与内切球": 3,
    "立体几何_总复习": 4,
    "立体几何_折叠与折痕问题": 1,
    "立体几何_球的截面": 4,
    "立体几何_空间线段与极值计算": 2,
    "立体几何_线面平行垂直与书写规范": 2,
    "立体几何_轨迹问题": 4,
    "解三角形_自由度方法论": 4,
    "解三角形_边角互化": 4,
    "高一数学期末": 4,
}
NO_LOSS_FLOOR_ROOT_HOLD = {"重难点培优01_集合与逻辑_OCR校订版.tex"}
NO_LOSS_FLOOR_TOTAL = sum(NO_LOSS_FLOOR_TOPIC_COUNTS.values()) + len(NO_LOSS_FLOOR_ROOT_HOLD)

PERSONAL_FACT_RE = re.compile(r"刘亚博|谭俊文")
LEGACY_ROUTE_RE = re.compile(r"comm" + r"on/(?:pool|ipara)|(?:\.\./)+ipara|(?:\.\./)+pool/")
TEX_INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")


def source_files(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix in {".tex", ".md"} and not path.name.startswith(".")
    )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not TOPICS_ROOT.is_dir():
        print(f"[ERROR] Teaching topics directory missing: {TOPICS_ROOT}")
        return 1

    sources = source_files(TOPICS_ROOT)
    counts_by_topic: Counter[str] = Counter()

    for spath in sources:
        rel = spath.relative_to(TOPICS_ROOT)
        if len(rel.parts) == 1:
            # Root hold file
            if spath.name not in NO_LOSS_FLOOR_ROOT_HOLD:
                errors.append(f"Unexpected root topic source: {rel}")
            continue

        topic = rel.parts[0]
        counts_by_topic[topic] += 1

        text = spath.read_text(encoding="utf-8", errors="ignore")

        # Privacy check for non-legacy files
        if topic != "legacy":
            privacy_match = PERSONAL_FACT_RE.search(text)
            if privacy_match:
                errors.append(f"Student privacy leak '{privacy_match.group(0)}' in public topic: {spath.relative_to(REPO_ROOT)}")

        # Legacy route check
        route_match = LEGACY_ROUTE_RE.search(text)
        if route_match:
            errors.append(f"Legacy route in topic source: {spath.relative_to(REPO_ROOT)}")

        # Validate input paths if TeX
        if spath.suffix == ".tex":
            for line in text.splitlines():
                line_str = line.strip()
                if line_str.startswith("%"):
                    continue
                for match in TEX_INPUT_RE.finditer(line_str):
                    target = match.group(1).strip()
                    if target.startswith("%") or target.startswith("\\"):
                        continue
                    target_with_ext = target if target.endswith(".tex") else target + ".tex"
                    cand1 = spath.parent / target_with_ext
                    cand2 = REPO_ROOT / target_with_ext
                    if not cand1.exists() and not cand2.exists():
                        errors.append(f"Unresolved \\input{{{target}}} in {spath.relative_to(REPO_ROOT)}")

    for topic in NO_LOSS_FLOOR_TOPIC_COUNTS:
        if not (TOPICS_ROOT / topic).is_dir():
            errors.append(f"Baseline topic directory missing: teaching/topics/{topic}")
    root_source_names = {path.name for path in sources if len(path.relative_to(TOPICS_ROOT).parts) == 1}
    for expected_root in NO_LOSS_FLOOR_ROOT_HOLD:
        if expected_root not in root_source_names:
            errors.append(f"Baseline root topic source missing: teaching/topics/{expected_root}")

    print("=" * 80)
    print("Teaching Topics Steady-State Audit")
    print("=" * 80)
    print(f"{'Topic':<35} {'Expected':<10} {'Found':<10} {'Status':<10}")
    print("-" * 80)

    for topic, baseline in NO_LOSS_FLOOR_TOPIC_COUNTS.items():
        found = counts_by_topic[topic]
        status = "OK" if found >= baseline else "DEFICIT"
        print(f"{topic:<35} {baseline:<10} {found:<10} {status:<10}")
        if found < baseline:
            errors.append(f"Topic '{topic}' fell below steady-state no-loss floor: floor {baseline}, found {found}")

    for topic in sorted(set(counts_by_topic) - set(NO_LOSS_FLOOR_TOPIC_COUNTS)):
        print(f"{topic:<35} {0:<10} {counts_by_topic[topic]:<10} {'NEW':<10}")

    print("-" * 80)
    print(f"Total Sources: {len(sources)} / no-loss floor {NO_LOSS_FLOOR_TOTAL}")
    if len(sources) < NO_LOSS_FLOOR_TOTAL:
        errors.append(f"Topics fell below steady-state no-loss floor: floor {NO_LOSS_FLOOR_TOTAL}, found {len(sources)}")
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

    print(f"SUCCESS: steady-state no-loss floor preserved; {len(sources)} current topic source assets verified. All topic invariants hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
