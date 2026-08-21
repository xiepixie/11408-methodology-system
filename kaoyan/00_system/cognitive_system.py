#!/usr/bin/env python3
"""考研认知仓库的路由、进度、硬检查与维护审计工具。

本脚本只做能够稳定自动判断的事情：
- `start`：为当前任务给出最小阅读范围；
- `progress`：从各入口文件的状态生成进度快照；
- `check`：拦截确定违反仓库契约的问题；
- `audit`：列出允许暂时存在、但会增加后续维护成本的过渡状态；
- `publish`：只发布本项目已经确认的 Canonical `.tex`，并验证最终 PDF 路由。

脚本不判断知识内容本身是否正确，也不自动修改 Handbook 正文。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote, urlparse


PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = PROJECT_ROOT.parent
CURRENT_PATH = PROJECT_ROOT / "CURRENT.md"
PROGRESS_PATH = PROJECT_ROOT / "PROGRESS.md"
PUBLISH_DIR = PROJECT_ROOT / "90_publish"


SHARED_COMPILE_SCRIPT = REPO_ROOT / "infra" / "scripts" / "compile_tex.py"
SYSTEM_TEX_TEMPLATES = {PROJECT_ROOT / "00_system" / "handbook_template.tex"}

# README 是导航页，不是正文。行数阈值只用于发现明显越界，不用于判断内容质量。
COURSE_OR_SUBJECT_README_MAX_LINES = 600
HANDBOOK_README_MAX_LINES = 250

CURRENT_REQUIRED_HEADINGS = (
    "## 当前已完成",
    "## 下一步候选",
    "## 待人工决定",
    "## 当前阻塞",
)


@dataclass(frozen=True)
class Finding:
    """一次检查发现。ERROR 阻止 check；AUDIT 只提示人工维护。"""

    severity: str
    code: str
    message: str
    fix: str = ""

    def render(self) -> str:
        line = f"[{self.severity}][{self.code}] {self.message}"
        if self.fix:
            line += f"\n  修复：{self.fix}"
        return line

STATUS_RE = re.compile(
    r"^\s*>?\s*(?:当前)?状态[：:]\s*(.+?)\s*$", re.MULTILINE
)
TYPE_RE = re.compile(
    r"^\s*>?\s*(?:类型|身份)[：:]\s*(Atlas|Topic|Bridge|Integration)\s*$",
    re.MULTILINE | re.IGNORECASE,
)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
TRAINING_NAV_HEADING_RE = re.compile(r"^##\s+训练导航\s*$", re.MULTILINE)
LOCAL_TRAINING_RULE_RE = re.compile(r"^#{2,4}\s+局部规则(?:[：:].*)?$", re.MULTILINE)
TRAINING_FIGURE_PLACEHOLDER_RE = re.compile(
    r"^>\s*\*\*(待补图|候选配图)｜([^*\n]+)\*\*[：:]\s*(\S.*)$",
    re.MULTILINE,
)
TRAINING_FIGURE_PLACEHOLDER_PREFIX_RE = re.compile(
    r"^>\s*\*\*(?:待补图|候选配图)", re.MULTILINE
)
REQUIRED_TRAINING_FIGURE_RE = re.compile(
    r"^>\s*\*\*待补图｜([^*\n]+)\*\*[：:]\s*(\S.*)$",
    re.MULTILINE,
)
LEGACY_ROUTE_RE = re.compile(
    r"(?:comm" + r"on/考研|comm" + r"on/scripts|408_Exam_Archive|Math1_Exam_Archive)(?:/|\\b)|(?:\.\./)+kaoyan/"
)
LEGACY_ROUTE_SCAN_ROOTS = (
    "00_system",
    "01_control",
    "10_数学一",
    "20_英语一",
    "30_408",
    "40_复试",
    "archives",
)
LEGACY_ROUTE_SCAN_SUFFIXES = {".md", ".json", ".py", ".tex"}

EXAM_SOLUTION_ROOT = PROJECT_ROOT / "archives" / "408"
EXAM_PROFILE_408 = PROJECT_ROOT / "00_system" / "exam_profiles" / "408.json"
EXAM_SOLUTION_FRONTMATTER_FIELDS = (
    "type",
    "exam_id",
    "question_id",
    "question_number",
    "subject",
    "status",
    "source_exam",
    "legacy_reference",
)
EXAM_SOLUTION_OBJECTIVE_HEADINGS = (
    "模型锚点",
    "解题链",
    "选项判断",
    "校验",
    "压缩",
    "易错边界",
)
EXAM_SOLUTION_COMPREHENSIVE_HEADINGS = (
    "模型锚点",
    "问题表征",
    "关键决策",
    "求解链",
    "校验",
    "压缩",
    "易错边界",
)
# 旧题解批量迁移期间的兼容结构。新写题解不得再使用这些英文栏目名；
# 待 2015～2026 全量迁移完成后删除这一兼容层。
EXAM_SOLUTION_LEGACY_OBJECTIVE_HEADINGS = (
    "Model Anchor",
    "解题链",
    "选项判断",
    "Verification",
    "Compression",
    "易错边界",
)
EXAM_SOLUTION_LEGACY_COMPREHENSIVE_HEADINGS = (
    "Model Anchor",
    "Problem Representation",
    "Decision Points",
    "Solution Chain",
    "Verification",
    "Compression",
    "易错边界",
)
EXAM_SOLUTION_H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
EXAM_SOLUTION_ANCHOR_OWNER_RE = re.compile(
    r"^-\s+(?:模型归属|主题|桥梁|规则|所有者|Topic(?:\s*/\s*(?:Owner|Bridge|Rules))?|Owner|Model Owner|Bridge|Rules)\s*[:：]",
    re.MULTILINE,
)
EXAM_SOLUTION_ANSWER_RE = re.compile(r"^answer:\s*([ABCD])\s*$", re.MULTILINE)
EXAM_INDEX_ANSWER_RE = re.compile(r"\*\*Q(\d{2})\*\*\s*\|\s*`([ABCD])`")

EXCLUDED_PROGRESS_SOURCES = {
    Path("CURRENT.md"),
    Path("PROGRESS.md"),
}

# ---------------------------------------------------------------------------
# Interaction routing: scenario metadata, subject aliases, and Context Packs.
# The executable scenario contract lives in SCENARIOS; long-form instructions
# live in 00_system/agent_context_protocol.md and the scenario-specific specs.
# ---------------------------------------------------------------------------

SUBJECTS = {
    "general": {
        "label": "通用",
        "aliases": {"general", "通用"},
        "root": Path("."),
        "context": [Path("README.md"), Path("01_control/problem_solving_kernel.md")],
    },
    "math": {
        "label": "数学一 / Cross-Subject",
        "aliases": {"math", "数学", "数学一", "数学综合"},
        "root": Path("10_数学一"),
        "context": [
            Path("10_数学一/README.md"),
            Path("10_数学一/50_桥梁专题/README.md"),
            Path("10_数学一/60_综合专题/README.md"),
        ],
    },
    "calculus": {
        "label": "数学一 / 高等数学",
        "aliases": {"calculus", "高数", "高等数学"},
        "root": Path("10_数学一/10_高等数学"),
        "context": [
            Path("10_数学一/README.md"),
            Path("10_数学一/10_高等数学/README.md"),
            Path("10_数学一/90_学科做题规则/README.md"),
        ],
    },
    "linear-algebra": {
        "label": "数学一 / 线性代数",
        "aliases": {"linear-algebra", "linear", "线代", "线性代数"},
        "root": Path("10_数学一/20_线性代数"),
        "context": [
            Path("10_数学一/README.md"),
            Path("10_数学一/20_线性代数/README.md"),
            Path("10_数学一/90_学科做题规则/README.md"),
            Path("10_数学一/90_学科做题规则/线性代数.md"),
        ],
    },
    "probability": {
        "label": "数学一 / 概率论与数理统计",
        "aliases": {"probability", "prob", "概率", "概率论", "概率统计", "数理统计"},
        "root": Path("10_数学一/30_概率论"),
        "context": [
            Path("10_数学一/README.md"),
            Path("10_数学一/30_概率论/README.md"),
            Path("10_数学一/90_学科做题规则/概率统计.md"),
        ],
    },
    "english": {
        "label": "英语一",
        "aliases": {"english", "英语", "英语一"},
        "root": Path("20_英语一"),
        "context": [Path("20_英语一/README.md")],
    },
    "408": {
        "label": "408 / Cross-Subject",
        "aliases": {"408", "计算机", "408通用", "跨科"},
        "root": Path("30_408"),
        "context": [
            Path("30_408/README.md"),
            Path("30_408/50_桥梁专题/README.md"),
            Path("30_408/60_综合专题/README.md"),
            Path("30_408/90_408做题规则/README.md"),
        ],
    },
    "data-structure": {
        "label": "408 / 数据结构",
        "aliases": {"data-structure", "ds", "数据结构"},
        "root": Path("30_408/10_数据结构"),
        "context": [
            Path("30_408/README.md"),
            Path("30_408/10_数据结构/README.md"),
            Path("30_408/10_数据结构/90_做题规则/README.md"),
        ],
    },
    "computer-organization": {
        "label": "408 / 计算机组成原理",
        "aliases": {"computer-organization", "co", "计组", "计算机组成原理"},
        "root": Path("30_408/20_计算机组成原理"),
        "context": [
            Path("30_408/README.md"),
            Path("30_408/20_计算机组成原理/README.md"),
            Path("30_408/20_计算机组成原理/90_做题规则/README.md"),
        ],
    },
    "os": {
        "label": "408 / 操作系统",
        "aliases": {"os", "操作系统"},
        "root": Path("30_408/30_操作系统"),
        "context": [
            Path("30_408/README.md"),
            Path("30_408/30_操作系统/README.md"),
            Path("30_408/30_操作系统/90_做题规则/README.md"),
        ],
    },
    "network": {
        "label": "408 / 计算机网络",
        "aliases": {"network", "net", "网络", "计算机网络"},
        "root": Path("30_408/40_计算机网络"),
        "context": [
            Path("30_408/README.md"),
            Path("30_408/40_计算机网络/README.md"),
            Path("30_408/40_计算机网络/90_做题规则/README.md"),
        ],
    },
}


SCENARIOS = {
    "explore": {
        "role": "Mapper + Socratic Tutor",
        "minimum": "专题 + 目前的直觉或最困惑的问题",
        "first": "先给母问题、仓库现有基线和第一个关键区分。",
    },
    "model-diff": {
        "role": "Socratic Tutor + Mapper",
        "minimum": "自己对专题的解释",
        "first": "先指出正确主干，再指出混淆、缺口和边界。",
    },
    "solve": {
        "role": "Model-Grounded Solver",
        "minimum": "题目 + 卡住的位置；已有尝试可选",
        "first": "先给 Model Anchor 和起手，再展开完整解题链。",
    },
    "exam-source": {
        "role": "Editor + Source Reconstructor",
        "minimum": "考试科目 + 年份 + 原始材料；若有最高质量题图，明确其优先级",
        "first": "先确定题源权威顺序、目标 Exam Archive 与对应 Exam Profile，再开始恢复题面。",
        "context": [
            Path("00_system/exam_source_agent_prompt.md"),
            Path("00_system/exam_source_conversion_spec.md"),
        ],
    },
    "exam-solution": {
        "role": "Model-Grounded Solver + Editor",
        "minimum": "年度 / 题号范围；题面从 Canonical Exam Source 读取",
        "first": "先锁定 Canonical Exam Source 与模型 Owner，再独立求解并执行题解质量门。",
        "context": [
            Path("00_system/exam_solution_agent_prompt.md"),
            Path("00_system/exam_solution_authoring_spec.md"),
            Path("00_system/exam_solution_quality_assurance.md"),
            Path("01_control/problem_solving_kernel.md"),
        ],
    },
    "wrong": {
        "role": "Debugger",
        "minimum": "题目 + 原始过程 + 自己答案；用时可选",
        "first": "先给 Observable Facts 和 First Divergence，不先重做。",
    },
    "adversary": {
        "role": "Adversary",
        "minimum": "候选理解/规则 + 已知成功或失败场景",
        "first": "先给最小反例或最强竞争解释。",
    },
    "practice": {
        "role": "Coach",
        "minimum": "已确认断点 + 训练难度或时间限制",
        "first": "先说明诊断目标，再给少量题。",
    },
    "import": {
        "role": "Mapper + Editor",
        "minimum": "来源文件 + 认为可能属于的专题",
        "first": "先判断产品类型和可能 Owner。",
    },
    "review": {
        "role": "Adversary + Editor + Coach",
        "minimum": "Inbox + 待验证 Rules + 真实表现",
        "first": "先删除噪声，再判断候选和冲突。",
    },
    "publish": {
        "role": "Editor",
        "minimum": "Canonical Owner + 要发布的 LaTeX",
        "first": "先检查模型是否已采用和依赖是否同步。",
    },
}


def resolve_subject(value: str) -> tuple[str, dict[str, object]]:
    normalized = value.strip().casefold()
    for key, config in SUBJECTS.items():
        aliases = {str(alias).casefold() for alias in config["aliases"]}
        if normalized == key.casefold() or normalized in aliases:
            return key, config
    valid = ", ".join(sorted(SUBJECTS))
    raise ValueError(f"unknown subject: {value!r}; use one of: {valid}")


def topic_candidates(root: Path, query: str, limit: int = 8) -> list[tuple[Path, str, str]]:
    base = PROJECT_ROOT / root
    if not base.exists():
        return []

    needle = query.strip().casefold()
    if not needle:
        return []

    candidates: list[tuple[int, Path, str, str]] = []
    for path in base.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        title_match = TITLE_RE.search(text)
        title = title_match.group(1).strip() if title_match else path.stem
        relative = path.relative_to(PROJECT_ROOT)
        searchable_title = title.casefold()
        searchable_path = relative.as_posix().casefold()
        if needle not in searchable_title and needle not in searchable_path:
            continue

        status_match = STATUS_RE.search(text)
        status = status_match.group(1).strip().rstrip("。") if status_match else "未声明状态"
        if path.name == "README.md":
            score = 0 if needle in searchable_title else 1
        else:
            score = 2 if needle in searchable_title else 3
        candidates.append((score, relative, title, status))

    candidates.sort(key=lambda item: (item[0], len(item[1].parts), item[1].as_posix()))
    return [(relative, title, status) for _, relative, title, status in candidates[:limit]]


def command_start(scenario: str, subject: str, topic: str | None) -> int:
    try:
        subject_key, subject_config = resolve_subject(subject)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    scenario_config = SCENARIOS[scenario]
    label = str(subject_config["label"])
    context_paths = [Path(path) for path in scenario_config.get("context", [])]
    context_paths.extend(Path(path) for path in subject_config["context"])

    if scenario in {"exam-source", "exam-solution"}:
        if subject_key in {"math", "calculus", "linear-algebra", "probability"}:
            context_paths.append(Path("00_system/exam_profiles/math1.json"))
        elif subject_key in {"408", "data-structure", "computer-organization", "os", "network"}:
            context_paths.append(Path("00_system/exam_profiles/408.json"))

    context_paths = list(dict.fromkeys(context_paths))

    print(f"场景：{scenario}")
    print(f"主要角色：{scenario_config['role']}")
    print(f"范围：{label}")
    if topic:
        print(f"专题查询：{topic}")
    print(f"首屏动作：{scenario_config['first']}")
    print(f"最少输入：{scenario_config['minimum']}")

    print("\nContext Pack：")
    for relative in context_paths:
        marker = "OK" if (PROJECT_ROOT / relative).exists() else "MISSING"
        print(f"- [{marker}] {relative.as_posix()}")

    if topic:
        matches = topic_candidates(Path(subject_config["root"]), topic)
        if subject_key == "math":
            preferred = {"50_桥梁专题", "60_综合专题"}
            matches.sort(
                key=lambda item: (
                    0 if len(item[0].parts) > 1 and item[0].parts[1] in preferred else 1,
                    len(item[0].parts),
                    item[0].as_posix(),
                )
            )
        print("\n候选 Topic / Bridge / Integration：")
        if matches:
            for relative, title, status in matches:
                print(f"- {title} | 状态：{status} | {relative.as_posix()}")
                absolute = PROJECT_ROOT / relative
                if absolute.name == "README.md":
                    if is_atlas_readme(absolute):
                        print(f"  Canonical Atlas: {relative.as_posix()} (Markdown map)")
                    else:
                        tex_candidates = sorted(absolute.parent.glob("*.tex"))
                        if len(tex_candidates) == 1:
                            tex_relative = tex_candidates[0].relative_to(PROJECT_ROOT)
                            print(f"  Canonical .tex: {tex_relative.as_posix()}")
                        elif len(tex_candidates) > 1:
                            names = ", ".join(p.name for p in tex_candidates)
                            print(f"  Canonical .tex: AMBIGUOUS ({names})")
                        else:
                            print("  Canonical .tex: MISSING — Landing/Source 不等于深度 Handbook 正文")
        else:
            print("- 未找到直接命中；先使用上述 Atlas 建立临时工作模型（provisional model），不要冒充成熟 Topic。")

    return 0


# ---------------------------------------------------------------------------
# Repository state: progress, hard checks, audit debt, and safe publication.
# Keep this section dependency-free and limited to machine-verifiable facts.
# ---------------------------------------------------------------------------


NON_HANDBOOK_DIRS = {"sources", "archives", "tmp", ".venv", ".git", "legacy", "daily_reading"}


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in PROJECT_ROOT.rglob("*.md")
        if not any(part in NON_HANDBOOK_DIRS for part in path.parts)
    )


def source_area(relative_path: Path) -> str:
    parts = relative_path.parts
    if not parts:
        return "系统"

    top_level = {
        "10_数学一": "数学一",
        "20_英语一": "英语一",
        "30_408": "408",
    }
    area = top_level.get(parts[0], "系统")

    if parts[0] == "10_数学一" and len(parts) > 1:
        subject = {
            "00_学科总图": "旧发布总图",
            "10_高等数学": "高等数学",
            "20_线性代数": "线性代数",
            "30_概率论": "概率统计",
            "50_桥梁专题": "跨科 Bridge",
            "60_综合专题": "跨科 Integration",
            "90_学科做题规则": "数学 Rules",
        }.get(parts[1])
        if subject:
            return f"数学一 / {subject}"

    if parts[0] == "30_408" and len(parts) > 1:
        subject = {
            "00_统一总图": "总图",
            "10_数据结构": "数据结构",
            "20_计算机组成原理": "计组",
            "30_操作系统": "OS",
            "40_计算机网络": "网络",
            "50_桥梁专题": "跨科 Bridge",
            "60_综合专题": "跨科 Integration",
            "90_408做题规则": "408 Rules",
        }.get(parts[1])
        if subject:
            return f"408 / {subject}"
    return area


def asset_records() -> list[tuple[str, str, str, Path]]:
    records: list[tuple[str, str, str, Path]] = []
    for path in markdown_files():
        relative = path.relative_to(PROJECT_ROOT)
        if relative in EXCLUDED_PROGRESS_SOURCES:
            continue

        text = path.read_text(encoding="utf-8")
        status_match = STATUS_RE.search(text)
        if not status_match:
            continue

        title_match = TITLE_RE.search(text)
        title = title_match.group(1).strip() if title_match else path.stem
        status = status_match.group(1).strip().rstrip("。")
        status = INLINE_LINK_RE.sub(r"\1", status)
        records.append((source_area(relative), title, status, relative))
    return records


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def status_bucket(status: str) -> str:
    normalized = status.strip().strip("*_ ")
    explicit_source_status = normalized == "Source" or normalized.startswith(
        ("Source；", "Source;", "Source：", "Source:")
    )
    explicit_working_draft = normalized.startswith(("工作稿", "LaTeX 工作稿", "Atlas 工作稿", "工作梳理稿"))

    if "工作稿待迁" in status or "旧工作稿待迁移" in status or explicit_source_status:
        return "Handbook Source 待迁移"
    if "需修订" in status:
        return "需修订"
    if "legacy-unregistered" in status or "发布物待纳管" in status or "旧发布物" in status:
        return "旧发布物待纳管"
    if "已发布" in status or "Published PDF" in status:
        return "已发布"
    if "废弃入口" in status or "废弃分组入口" in status or "Source Navigation" in status:
        return "废弃/Source 导航"
    if normalized.startswith("Candidate") or "Candidate Core" in status:
        return "Candidate"
    if normalized.startswith("待验证"):
        return "待验证"
    if "待人工确认" in status:
        return "待人工确认"
    if explicit_working_draft:
        return "工作稿"
    if any(
        marker in status
        for marker in (
            "框架已采用",
            "架构已采用",
            "目录已建立",
            "Landing Page 已建立",
            "Source Routing 已确认",
        )
    ) or normalized == "规划":
        return "框架/目录已建立"
    if "已采用" in status:
        return "已采用"
    return "其他"


def current_body() -> str:
    if not CURRENT_PATH.exists():
        return "`CURRENT.md` 尚未建立。"
    text = CURRENT_PATH.read_text(encoding="utf-8").strip()
    return TITLE_RE.sub("", text, count=1).strip()


def render_progress() -> str:
    records = asset_records()
    counts = Counter(status_bucket(status) for _, _, status, _ in records)

    lines = [
        "# 项目进度",
        "",
        "> 本文件由 `python3 00_system/cognitive_system.py progress --write` 生成，请勿手工修改。",
        "",
        "## 当前焦点",
        "",
        current_body(),
        "",
        "## 状态汇总",
        "",
        "| 状态 | 数量 |",
        "|---|---:|",
    ]
    if counts:
        for status, count in sorted(counts.items()):
            lines.append(f"| {markdown_escape(status)} | {count} |")
    else:
        lines.append("| 尚无带状态的资产 | 0 |")

    lines.extend(
        [
            "",
            "## 资产明细",
            "",
            "| 范围 | 资产 | 状态 |",
            "|---|---|---|",
        ]
    )
    for area, title, status, relative in records:
        # Evidence filenames are historical provenance. Keep their original files
        # addressable on disk, but do not leak a legacy source-brand name into the
        # reader-facing progress note.
        if "codebrick" in relative.as_posix().lower() or "codebrick" in title.lower():
            neutral_title = title.replace("计组 CodeBrick 全量 Source Diff", "计组全量 Source Diff")
            neutral_title = neutral_title.replace("CodeBrick OS 全量 Source Diff", "操作系统全量 Source Diff")
            neutral_title = neutral_title.replace("CodeBrick", "外部来源").replace("codebrick", "外部来源")
            asset_cell = markdown_escape(neutral_title)
        else:
            link = quote(relative.as_posix(), safe="/._-")
            asset_cell = f"[{markdown_escape(title)}]({link})"
        lines.append(
            f"| {markdown_escape(area)} | {asset_cell} | "
            f"{markdown_escape(status)} |"
        )

    lines.extend(
        [
            "",
            "## 怎样更新",
            "",
            "1. 当前工作方向变化时，修改 `CURRENT.md`；",
            "2. 某项资产的物理文件或人工决定发生真实变化时，修改其入口顶部的 `状态：...`；",
            "3. 运行进度生成与系统检查；",
            "4. 不为了让数字增长而修改状态。",
            "",
        ]
    )
    return "\n".join(lines)


def write_progress() -> bool:
    rendered = render_progress()
    previous = PROGRESS_PATH.read_text(encoding="utf-8") if PROGRESS_PATH.exists() else None
    if previous == rendered:
        return False
    PROGRESS_PATH.write_text(rendered, encoding="utf-8")
    return True


def normalize_link(raw_link: str) -> str:
    value = raw_link.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    return value


def status_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = STATUS_RE.search(text)
    return match.group(1).strip().rstrip("。") if match else ""


def find_published_pdf(stem: str) -> Path | None:
    if not PUBLISH_DIR.exists():
        return None
    flat = PUBLISH_DIR / f"{stem}.pdf"
    if flat.is_file():
        return flat
    for path in PUBLISH_DIR.rglob(f"{stem}.pdf"):
        if path.is_file():
            return path
    return None


def publish_target_dir(source_path: Path) -> Path:
    try:
        rel = source_path.relative_to(PROJECT_ROOT)
        top = rel.parts[0]
    except (ValueError, IndexError):
        return PUBLISH_DIR
    if top == "10_数学一":
        return PUBLISH_DIR / "math1"
    if top == "20_英语一":
        return PUBLISH_DIR / "english1"
    if top == "30_408":
        return PUBLISH_DIR / "408"
    if top == "40_复试":
        return PUBLISH_DIR / "interview"
    if top in {"00_system", "01_control"}:
        return PUBLISH_DIR / "system"
    return PUBLISH_DIR


def declared_handbook_type(path: Path) -> str:
    """Return an explicitly declared Handbook type; never infer from path/title."""
    text = path.read_text(encoding="utf-8")
    match = TYPE_RE.search(text)
    return match.group(1).capitalize() if match else ""


def is_atlas_readme(path: Path) -> bool:
    return path.name == "README.md" and declared_handbook_type(path) == "Atlas"


def all_tex_files() -> list[Path]:
    return sorted(
        path
        for path in PROJECT_ROOT.rglob("*.tex")
        if "90_publish" not in path.parts and not any(part in NON_HANDBOOK_DIRS for part in path.parts)
    )


def tex_files() -> list[Path]:
    """Canonical/legacy deep-body candidates; Atlas poster sources under assets are excluded."""
    return [path for path in all_tex_files() if "assets" not in path.parts]


def handbook_tex_files(readme: Path) -> list[Path]:
    return sorted(readme.parent.glob("*.tex"))


def status_is_source_only(status: str) -> bool:
    normalized = status.strip().strip("*_ ")
    explicit_source_status = normalized == "Source" or normalized.startswith(
        ("Source；", "Source;", "Source：", "Source:")
    )
    return explicit_source_status or any(
        marker in status
        for marker in (
            "README 旧工作稿待迁移",
            "旧工作稿待迁移",
            "legacy-unregistered",
            "正文未建",
            "正文待建",
            "正文待逐册",
            "待建设",
            "待迁移",
            "旧发布物待纳管",
        )
    )


def status_claims_handbook_body(status: str) -> bool:
    """Return True only when the status claims a maintainable Handbook body exists."""
    if not status or status_is_source_only(status):
        return False
    if any(
        marker in status
        for marker in (
            "LaTeX 工作稿",
            "第一版正文已建立",
            "完整正文已建立",
            "待人工确认",
            "已发布",
            "Published PDF",
        )
    ):
        return True
    if (
        "已采用" in status
        and "框架已采用" not in status
        and "架构已采用" not in status
        and "尚无已采用" not in status
        and "无已采用" not in status
    ):
        return True
    return False


def status_claims_published(status: str) -> bool:
    if status_is_source_only(status):
        return False
    return "已发布" in status or "Published PDF" in status


def status_claims_adopted(status: str) -> bool:
    """Return True only when the status claims current content has been adopted."""
    if not status or status_is_source_only(status):
        return False
    return (
        "已采用" in status
        and "框架已采用" not in status
        and "架构已采用" not in status
        and "尚无已采用" not in status
        and "无已采用" not in status
    )


def broken_link_findings() -> list[Finding]:
    findings: list[Finding] = []
    ownership_file = PROJECT_ROOT / "00_system" / "ownership_matrix.md"
    for path in markdown_files():
        if path == ownership_file:
            continue
        text = path.read_text(encoding="utf-8")
        for raw_link in LINK_RE.findall(text):
            link = normalize_link(raw_link)
            parsed = urlparse(link)
            if parsed.scheme or link.startswith("#"):
                continue
            target_text = unquote(parsed.path)
            if not target_text:
                continue
            target = (path.parent / target_text).resolve()
            if not target.exists():
                relative = path.relative_to(PROJECT_ROOT)
                findings.append(
                    Finding(
                        "ERROR",
                        "E-LINK",
                        f"断链：{relative} -> {link}",
                        "修正链接或恢复目标文件。",
                    )
                )
    return findings


def legacy_route_findings() -> list[Finding]:
    """Reject routes back into retired legacy locations."""
    findings: list[Finding] = []
    candidates: list[Path] = []
    for name in ("README.md", "AGENTS.md", "CURRENT.md", "PROGRESS.md", "QUICK_START.md"):
        path = PROJECT_ROOT / name
        if path.is_file():
            candidates.append(path)
    for root_name in LEGACY_ROUTE_SCAN_ROOTS:
        root = PROJECT_ROOT / root_name
        if not root.is_dir():
            continue
        candidates.extend(
            path
            for path in root.rglob("*")
            if path.is_file() and path.suffix in LEGACY_ROUTE_SCAN_SUFFIXES
        )

    rule_owner = PROJECT_ROOT / "00_system" / "repository_integrity.md"
    self_path = Path(__file__).resolve()
    for path in sorted(set(candidates)):
        if path.resolve() in {rule_owner.resolve(), self_path}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = LEGACY_ROUTE_RE.search(text)
        if match:
            findings.append(
                Finding(
                    "ERROR",
                    "E-LEGACY-ROUTE",
                    f"迁移完成后的活动资产仍引用退休路径 `{match.group(0).rstrip('/')}`：{path.relative_to(PROJECT_ROOT)}。",
                    "改为 kaoyan/ 或 infra/ 下的 Canonical 路径；历史 provenance 只保留在 evidence/source 语境。",
                )
            )
    return findings


def handbook_status_findings() -> list[Finding]:
    findings: list[Finding] = []
    for readme in markdown_files():
        if readme.name != "README.md":
            continue
        status = status_text(readme)
        if not status or not status_claims_handbook_body(status):
            continue

        relative = readme.relative_to(PROJECT_ROOT)
        if not is_handbook_area(relative) or is_atlas_readme(readme):
            continue
        sources = handbook_tex_files(readme)
        if len(sources) != 1:
            detail = "没有 .tex" if not sources else "存在多个 .tex：" + ", ".join(p.name for p in sources)
            findings.append(
                Finding(
                    "ERROR",
                    "E-STATUS-TEX",
                    f"{relative} 的状态“{status}”表示正文已经存在，但目录中{detail}。",
                    "建立唯一 Canonical .tex，或把状态改成明确的 README 旧工作稿待迁移 / Source。",
                )
            )
            continue

        if status_claims_published(status):
            source = sources[0]
            pdf = find_published_pdf(source.stem)
            if pdf is None:
                expected_dest = publish_target_dir(source) / f"{source.stem}.pdf"
                findings.append(
                    Finding(
                        "ERROR",
                        "E-PUBLISH-MISSING",
                        f"{relative} 声称已有发布视图，但缺少 {expected_dest.relative_to(PROJECT_ROOT)}。",
                        f"用 compile_tex.py 编译 {source.relative_to(PROJECT_ROOT)}，或取消发布状态。",
                    )
                )
            elif pdf.stat().st_mtime < source.stat().st_mtime:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-PUBLISH-STALE",
                        f"{pdf.relative_to(PROJECT_ROOT)} 比 Canonical Source {source.relative_to(PROJECT_ROOT)} 更旧。",
                        "重新编译发布，确保 PDF 反映当前 .tex。",
                    )
                )
    return findings


def publish_collision_findings() -> list[Finding]:
    findings: list[Finding] = []
    by_stem: dict[str, list[Path]] = defaultdict(list)
    for source in all_tex_files():
        by_stem[source.stem].append(source)
    for stem, sources in sorted(by_stem.items()):
        if len(sources) <= 1:
            continue
        paths = ", ".join(str(p.relative_to(PROJECT_ROOT)) for p in sources)
        findings.append(
            Finding(
                "ERROR",
                "E-PUBLISH-COLLISION",
                f"多个 .tex 会发布为同一个 90_publish/{stem}.pdf：{paths}",
                "为这些 Canonical Source 使用不同 stem，避免发布时互相覆盖。",
            )
        )
    return findings


def ownership_findings() -> list[Finding]:
    findings: list[Finding] = []
    ownership_file = PROJECT_ROOT / "00_system" / "ownership_matrix.md"
    if not ownership_file.exists():
        return [
            Finding(
                "ERROR",
                "E-OWNERSHIP-LINK",
                "缺少 00_system/ownership_matrix.md。",
                "恢复 Ownership 台账。",
            )
        ]

    text = ownership_file.read_text(encoding="utf-8")
    for raw_link in LINK_RE.findall(text):
        link = normalize_link(raw_link)
        parsed = urlparse(link)
        if parsed.scheme or link.startswith("#"):
            continue
        target_text = unquote(parsed.path)
        if not target_text:
            continue
        target = (ownership_file.parent / target_text).resolve()
        if not target.exists():
            findings.append(
                Finding(
                    "ERROR",
                    "E-OWNERSHIP-LINK",
                    f"Ownership 台账引用不存在：{link}",
                    "修正为当前真实 Owner 路径，或明确删除已废弃登记。",
                )
            )
    return findings


def current_findings() -> list[Finding]:
    if not CURRENT_PATH.exists():
        return [
            Finding(
                "ERROR",
                "E-CURRENT",
                "CURRENT.md 不存在。",
                "恢复当前焦点文件。",
            )
        ]

    findings: list[Finding] = []
    text = CURRENT_PATH.read_text(encoding="utf-8")
    title_match = TITLE_RE.search(text)
    if not title_match or title_match.group(1).strip() != "当前焦点":
        findings.append(
            Finding(
                "ERROR",
                "E-CURRENT",
                "CURRENT.md 缺少唯一入口标题“# 当前焦点”。",
                "恢复固定 H1；具体计划内容仍由人工维护。",
            )
        )
    for heading in CURRENT_REQUIRED_HEADINGS:
        if heading not in text:
            findings.append(
                Finding(
                    "ERROR",
                    "E-CURRENT",
                    f"CURRENT.md 缺少维护区块“{heading}”。",
                    "恢复该区块；脚本不判断其中计划是否合理。",
                )
            )
    return findings


def progress_findings() -> list[Finding]:
    expected = render_progress()
    if not PROGRESS_PATH.exists():
        return [
            Finding(
                "ERROR",
                "E-PROGRESS",
                "PROGRESS.md 不存在。",
                "运行 python3 00_system/cognitive_system.py progress --write。",
            )
        ]
    if PROGRESS_PATH.read_text(encoding="utf-8") != expected:
        return [
            Finding(
                "ERROR",
                "E-PROGRESS",
                "PROGRESS.md 已过期。",
                "运行 python3 00_system/cognitive_system.py progress --write。",
            )
        ]
    return []


def exam_solution_frontmatter(text: str) -> str | None:
    """Return the leading YAML-like frontmatter body without parsing arbitrary YAML."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    return text[4:end]


def exam_solution_field(frontmatter: str, field: str) -> str | None:
    match = re.search(rf"^{re.escape(field)}:\s*(.*?)\s*$", frontmatter, re.MULTILINE)
    return match.group(1) if match else None


def expected_408_subject(profile: dict, year: int, question: int) -> str | None:
    if question <= 40:
        routes = profile.get("objective_routing", [])
    else:
        routes = profile.get("routing_overrides", {}).get(
            str(year), profile.get("comprehensive_routing_default", [])
        )
    for route in routes:
        questions = route.get("questions")
        if isinstance(questions, dict):
            if questions.get("from", question + 1) <= question <= questions.get("to", question - 1):
                return route.get("subject")
        elif isinstance(questions, list) and question in questions:
            return route.get("subject")
    return None


def solution_year_declared_complete(solutions_dir: Path, numbers: list[int]) -> bool:
    """Return whether a Derived Solution year has entered annual completion state."""
    expected_numbers = list(range(1, 48))
    return (
        (solutions_dir / "README.md").exists()
        or (solutions_dir / "solution_review.md").exists()
        or numbers == expected_numbers
    )


def exam_solution_findings() -> list[Finding]:
    """Hard-check machine-provable invariants for partial and complete 408 solution years."""
    findings: list[Finding] = []
    if not EXAM_SOLUTION_ROOT.exists() or not EXAM_PROFILE_408.exists():
        return findings

    try:
        profile = json.loads(EXAM_PROFILE_408.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [
            Finding(
                "ERROR",
                "E-EXAM-SOLUTION-PROFILE",
                f"无法读取 408 Exam Profile：{exc}",
                "恢复 00_system/exam_profiles/408.json 后再运行题解检查。",
            )
        ]

    for year_dir in sorted(EXAM_SOLUTION_ROOT.glob("[0-9][0-9][0-9][0-9]年真题")):
        solutions_dir = year_dir / "solutions"
        if not solutions_dir.exists():
            continue
        qfiles = sorted(solutions_dir.glob("q[0-9][0-9].md"))
        if not qfiles:
            continue

        year_match = re.match(r"(\d{4})年真题", year_dir.name)
        if not year_match:
            continue
        year = int(year_match.group(1))
        rel_solutions = solutions_dir.relative_to(PROJECT_ROOT)

        numbers = []
        for path in qfiles:
            match = re.fullmatch(r"q(\d{2})\.md", path.name)
            if match:
                numbers.append(int(match.group(1)))
        expected_numbers = list(range(1, 48))
        annual_readme = solutions_dir / "README.md"
        year_declared_complete = solution_year_declared_complete(solutions_dir, numbers)

        if year_declared_complete and numbers != expected_numbers:
            findings.append(
                Finding(
                    "ERROR",
                    "E-EXAM-SOLUTION-COVERAGE",
                    f"{rel_solutions} 已进入整年完成态，但 Coverage 不是 Q01～Q47：当前 {len(numbers)} 个文件。",
                    "补齐或去重 solutions/qNN.md；若仍是 partial work，不要提前创建年度完成 README / solution_review。",
                )
            )

        if year_declared_complete:
            for support in ("README.md", "solution_review.md"):
                if not (solutions_dir / support).exists():
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-EXAM-SOLUTION-SUPPORT",
                            f"{rel_solutions} 已进入整年完成态，但缺少 {support}。",
                            "补回年度阅读入口/审阅记录，保持题解正文与审计证据分层。",
                        )
                    )

        if annual_readme.exists():
            readme_text = annual_readme.read_text(encoding="utf-8")
            if "exam_solution_quality_assurance.md" not in readme_text:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-SUPPORT",
                        f"{annual_readme.relative_to(PROJECT_ROOT)} 未引用统一题解 QA Owner。",
                        "链接 00_system/exam_solution_quality_assurance.md，避免年度目录形成第二套质量合同。",
                    )
                )

        index_candidates = sorted(year_dir.glob("00_*408真题全景索引.md"))
        index_answers: dict[int, str] = {}
        if index_candidates:
            index_text = index_candidates[0].read_text(encoding="utf-8")
            index_answers = {
                int(question): answer
                for question, answer in EXAM_INDEX_ANSWER_RE.findall(index_text)
            }

        for path in qfiles:
            question = int(path.stem[1:])
            rel_path = path.relative_to(PROJECT_ROOT)
            text = path.read_text(encoding="utf-8")
            frontmatter = exam_solution_frontmatter(text)
            if frontmatter is None:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-FRONTMATTER",
                        f"{rel_path} 缺少完整 Frontmatter。",
                        "恢复题解最低元数据合同。",
                    )
                )
                continue

            required_fields = list(EXAM_SOLUTION_FRONTMATTER_FIELDS)
            if question <= 40:
                required_fields.append("answer")
            missing_fields = [
                field
                for field in required_fields
                if exam_solution_field(frontmatter, field) is None
            ]
            if missing_fields:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-FRONTMATTER",
                        f"{rel_path} 缺少字段：{', '.join(missing_fields)}。",
                        "按 exam_solution_quality_assurance.md 的最低 Frontmatter 补齐。",
                    )
                )

            expected_values = {
                "type": "exam-solution",
                "exam_id": f"408-{year}",
                "question_id": f"408-{year}-Q{question:02}",
                "question_number": str(question),
                "status": "model-grounded-v1",
            }
            for field, expected in expected_values.items():
                actual = exam_solution_field(frontmatter, field)
                if actual is not None and actual != expected:
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-EXAM-SOLUTION-FRONTMATTER",
                            f"{rel_path} 的 {field}={actual!r}，应为 {expected!r}。",
                            "统一稳定题解元数据；Source/Review 条件说明放入 solution_review.md。",
                        )
                    )

            expected_subject = expected_408_subject(profile, year, question)
            actual_subject = exam_solution_field(frontmatter, "subject")
            if expected_subject and actual_subject and actual_subject != expected_subject:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-ROUTING",
                        f"{rel_path} subject={actual_subject!r}，Exam Profile 期望 {expected_subject!r}。",
                        "先应用年度 routing override，再更新题解学科路由。",
                    )
                )

            if question <= 40:
                answer_match = EXAM_SOLUTION_ANSWER_RE.search(frontmatter)
                if not answer_match:
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-EXAM-SOLUTION-ANSWER",
                            f"{rel_path} 的 answer 不是 A/B/C/D。",
                            "恢复单项选择题答案字段。",
                        )
                    )
                elif index_answers and index_answers.get(question) != answer_match.group(1):
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-EXAM-SOLUTION-ANSWER",
                            f"{rel_path} answer={answer_match.group(1)} 与年度索引 {index_answers.get(question)} 不一致。",
                            "独立核题后让年度索引与 Derived Solution 收口到同一答案。",
                        )
                    )

            for field in ("source_exam", "legacy_reference"):
                raw_target = exam_solution_field(frontmatter, field)
                if not raw_target:
                    continue
                target = (path.parent / raw_target).resolve()
                if not target.exists():
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-EXAM-SOLUTION-LINK",
                            f"{rel_path} 的 {field} 指向不存在：{raw_target}",
                            "修复为当前 Canonical Source / legacy reference 的真实相对路径。",
                        )
                    )

            expected_headings = (
                EXAM_SOLUTION_OBJECTIVE_HEADINGS
                if question <= 40
                else EXAM_SOLUTION_COMPREHENSIVE_HEADINGS
            )
            legacy_headings = (
                EXAM_SOLUTION_LEGACY_OBJECTIVE_HEADINGS
                if question <= 40
                else EXAM_SOLUTION_LEGACY_COMPREHENSIVE_HEADINGS
            )
            actual_headings = tuple(EXAM_SOLUTION_H2_RE.findall(text))
            # 2015～2026 是中文栏目合同建立前已完成的历史批次，迁移期间仅兼容其旧英文栏目；
            # 2014 及之后新处理的更早年份必须直接使用中文栏目。
            allowed_headings = {expected_headings}
            if 2015 <= year <= 2026:
                allowed_headings.add(legacy_headings)
            if actual_headings not in allowed_headings:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-FORMAT",
                        f"{rel_path} 的 H2 结构为 {actual_headings}，中文规范期望 {expected_headings}。",
                        "题解栏目统一使用中文；额外细分使用 H3，审计说明移入 solution_review.md。",
                    )
                )
            else:
                matches = list(EXAM_SOLUTION_H2_RE.finditer(text))
                empty_sections = []
                for index, match in enumerate(matches):
                    end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
                    if not text[match.end():end].strip():
                        empty_sections.append(match.group(1))
                if empty_sections:
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-EXAM-SOLUTION-FORMAT",
                            f"{rel_path} 存在空 H2：{', '.join(empty_sections)}。",
                            "固定结构不能只占位；每节必须承担 exam_solution_quality_assurance.md 规定的学习责任。",
                        )
                    )

            h1_match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
            expected_h1 = f"408-{year}-Q{question:02}"
            if not h1_match or h1_match.group(1) != expected_h1:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-FORMAT",
                        f"{rel_path} H1 不是 {expected_h1!r}。",
                        "恢复统一 QID 标题。",
                    )
                )

            anchor_heading = "## 模型锚点" if "## 模型锚点" in text else "## Model Anchor"
            anchor_start = text.find(anchor_heading)
            anchor_end = text.find("\n## ", anchor_start + len(anchor_heading))
            anchor_text = text[anchor_start : anchor_end if anchor_end >= 0 else len(text)]
            missing_anchor = [
                label for label in ("题目信号", "第一动作") if label not in anchor_text
            ]
            if not EXAM_SOLUTION_ANCHOR_OWNER_RE.search(anchor_text):
                missing_anchor.insert(0, "模型归属（主题 / 桥梁 / 规则）")
            if missing_anchor:
                findings.append(
                    Finding(
                        "ERROR",
                        "E-EXAM-SOLUTION-ANCHOR",
                        f"{rel_path} 的模型锚点缺少：{', '.join(missing_anchor)}。",
                        "先用中文字段显式定位模型归属（主题 / 桥梁 / 规则），再补成可执行的题目信号与第一动作；不要只写知识点名称。", 
                    )
                )

    return findings


def training_markdown_findings() -> list[Finding]:
    """Validate Markdown files explicitly registered under a README 训练导航 section.

    This is intentionally opt-in through navigation rather than a blind scan of every
    legacy Markdown file. Once a file becomes an official training entry, the minimal
    header and local-rule tuple become hard contracts.
    """
    findings: list[Finding] = []

    for readme in PROJECT_ROOT.rglob("README.md"):
        text = readme.read_text(encoding="utf-8")
        nav_match = TRAINING_NAV_HEADING_RE.search(text)
        if not nav_match:
            continue

        section_start = nav_match.end()
        next_h2 = re.search(r"^##\s+", text[section_start:], re.MULTILINE)
        section_end = section_start + next_h2.start() if next_h2 else len(text)
        nav_text = text[section_start:section_end]

        for raw_link in LINK_RE.findall(nav_text):
            parsed = urlparse(raw_link)
            if parsed.scheme or parsed.netloc:
                continue
            link_path = unquote(parsed.path)
            if not link_path.endswith(".md"):
                continue

            target = (readme.parent / link_path).resolve()
            try:
                target_rel = target.relative_to(PROJECT_ROOT)
            except ValueError:
                continue
            if not target.is_file():
                # broken_link_findings owns the missing-target error.
                continue

            training_text = target.read_text(encoding="utf-8")
            head = "\n".join(training_text.splitlines()[:12])

            if not re.search(r"\A#\s+\S", training_text):
                findings.append(
                    Finding(
                        "ERROR",
                        "E-TRAINING-HEADER",
                        f"{target_rel} 已进入训练导航，但文件开头没有唯一 H1。",
                        "按 topic_practice_writing_spec.md《专题训练写作规范》补成‘# 问题族名称’。",
                    )
                )
            if not re.search(r"^>\s*训练定位[：:]", head, re.MULTILINE):
                findings.append(
                    Finding(
                        "ERROR",
                        "E-TRAINING-HEADER",
                        f"{target_rel} 已进入训练导航，但头部缺少‘训练定位’。",
                        "在 H1 后补最小头部契约，说明这份文件负责什么训练场景。",
                    )
                )
            if not re.search(r"^>\s*模型归属[：:]", head, re.MULTILINE):
                findings.append(
                    Finding(
                        "ERROR",
                        "E-TRAINING-HEADER",
                        f"{target_rel} 已进入训练导航，但头部缺少‘模型归属’。",
                        "链接真实 Canonical .tex Owner；训练 Markdown 不拥有第二套理论正文。",
                    )
                )

            placeholder_lines = [
                line
                for line in training_text.splitlines()
                if re.match(r"^>\s*\*\*(?:待补图|候选配图)", line)
            ]
            for line in placeholder_lines:
                if not TRAINING_FIGURE_PLACEHOLDER_RE.fullmatch(line):
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-TRAINING-FIGURE-PLACEHOLDER",
                            f"{target_rel} 的图意图占位格式不完整：{line}",
                            "统一写成‘> **待补图｜图名**：图的解释责任。’或‘> **候选配图｜图名**：图的解释责任。’，不要提前创建不存在的图片链接。",
                        )
                    )

            required_figures = list(REQUIRED_TRAINING_FIGURE_RE.finditer(training_text))
            if required_figures and status_claims_adopted(status_text(readme)):
                names = ", ".join(match.group(1).strip() for match in required_figures)
                findings.append(
                    Finding(
                        "ERROR",
                        "E-TRAINING-FIGURE-TODO",
                        f"{target_rel} 所属专题已采用，但仍有必要图未闭环：{names}。",
                        "在‘已采用’前把每个待补图处理为删除、复用既有图、链接 Canonical 图或建立真实图源并替换为图片引用；候选配图不阻塞采用。",
                    )
                )

            rule_matches = list(LOCAL_TRAINING_RULE_RE.finditer(training_text))
            for index, match in enumerate(rule_matches):
                block_end = (
                    rule_matches[index + 1].start()
                    if index + 1 < len(rule_matches)
                    else len(training_text)
                )
                block = training_text[match.start():block_end]
                missing = [
                    label
                    for label in ("**触发信号**", "**第一动作**", "**检查与退出**")
                    if label not in block
                ]
                if missing:
                    heading = match.group(0).lstrip("# ")
                    findings.append(
                        Finding(
                            "ERROR",
                            "E-TRAINING-RULE-TUPLE",
                            f"{target_rel} 的‘{heading}’缺少：{', '.join(missing)}。",
                            "局部规则统一使用‘触发信号—第一动作—检查与退出’三元组；纯母题/反例不要硬写成规则。",
                        )
                    )

    return findings


def structural_findings() -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(broken_link_findings())
    findings.extend(legacy_route_findings())
    findings.extend(handbook_status_findings())
    findings.extend(publish_collision_findings())
    findings.extend(ownership_findings())
    findings.extend(exam_solution_findings())
    findings.extend(training_markdown_findings())
    findings.extend(current_findings())

    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if STATUS_RE.search(text) and not TITLE_RE.search(text):
            findings.append(
                Finding(
                    "ERROR",
                    "E-STATUS-TITLE",
                    f"{path.relative_to(PROJECT_ROOT)} 有状态但没有 H1 标题。",
                    "补回唯一 H1，避免进度资产无法识别。",
                )
            )

    findings.extend(progress_findings())
    return findings


def command_progress(write: bool) -> int:
    if write:
        changed = write_progress()
        action = "updated" if changed else "already current"
        print(f"{PROGRESS_PATH.relative_to(PROJECT_ROOT)}: {action}")
    else:
        print(render_progress(), end="")
    return 0


def command_check() -> int:
    findings = structural_findings()
    if not findings:
        print("OK: repository hard checks passed.")
        return 0
    for finding in findings:
        print(finding.render())
    print(f"{len(findings)} hard error(s) found.")
    return 1


def is_handbook_area(relative: Path) -> bool:
    if not relative.parts:
        return False
    if relative.parts[0] not in {"10_数学一", "20_英语一", "30_408"}:
        return False
    return not any("做题规则" in part or part.startswith("90_") for part in relative.parts)


def resolve_publish_target(raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    return path.resolve()


def publish_preflight(tex_path: Path) -> list[Finding]:
    """Validate that a target can safely use the shared compile script."""
    findings: list[Finding] = []

    try:
        relative = tex_path.relative_to(PROJECT_ROOT)
    except ValueError:
        return [
            Finding(
                "ERROR",
                "P-PATH",
                f"拒绝发布项目外文件：{tex_path}",
                "publish 只允许处理 kaoyan/ 内部的 Canonical Handbook Source。",
            )
        ]

    if tex_path.suffix != ".tex" or not tex_path.is_file():
        return [
            Finding(
                "ERROR",
                "P-TARGET",
                f"目标不存在或不是 .tex：{relative}",
                "传入一个真实存在的 Handbook .tex 文件。",
            )
        ]

    if PUBLISH_DIR in tex_path.parents:
        findings.append(
            Finding(
                "ERROR",
                "P-PATH",
                f"Canonical Source 不能放在发布目录：{relative}",
                "把 .tex 保留在 Handbook 目录，90_publish 只放 PDF。",
            )
        )

    readme = tex_path.parent / "README.md"
    if not readme.exists():
        findings.append(
            Finding(
                "ERROR",
                "P-NO-README",
                f"{relative} 所在目录没有 README Landing Page。",
                "先完成 Handbook package 与 Owner 纳管，再使用正式 publish。",
            )
        )
    else:
        if is_atlas_readme(readme):
            findings.append(
                Finding(
                    "ERROR",
                    "P-ATLAS-VIEW",
                    f"{readme.relative_to(PROJECT_ROOT)} 是 Canonical Atlas README；同目录 .tex 不能作为第二份知识正文发布。",
                    "Atlas 地图直接维护 README。若需要视觉海报，把派生 .tex 放入 assets/ 并保持它不拥有新结论。",
                )
            )

        status = status_text(readme)
        if not status:
            findings.append(
                Finding(
                    "ERROR",
                    "P-NO-STATUS",
                    f"{readme.relative_to(PROJECT_ROOT)} 没有状态行。",
                    "先明确当前是 LaTeX 工作稿 / 待人工确认 / 已采用等真实状态。",
                )
            )
        elif status_is_source_only(status) or not status_claims_handbook_body(status):
            findings.append(
                Finding(
                    "ERROR",
                    "P-NOT-CANONICAL",
                    f"{readme.relative_to(PROJECT_ROOT)} 当前状态“{status}”没有声明可维护的 Canonical LaTeX 正文。",
                    "先完成 Source Diff，并把该 .tex 确认为当前 Handbook Source；不要直接发布 legacy/source。",
                )
            )

        sibling_tex = handbook_tex_files(readme)
        if len(sibling_tex) != 1 or sibling_tex[0].resolve() != tex_path:
            names = ", ".join(path.name for path in sibling_tex) or "无"
            findings.append(
                Finding(
                    "ERROR",
                    "P-AMBIGUOUS-SOURCE",
                    f"{readme.parent.relative_to(PROJECT_ROOT)} 无法确定唯一 Canonical .tex（当前：{names}）。",
                    "每个正式 Handbook package 只保留一个当前正文 Source；其他版本降为明确 Source/legacy。",
                )
            )

    collisions = [
        source
        for source in tex_files()
        if source.resolve() != tex_path and source.stem == tex_path.stem
    ]
    if collisions:
        findings.append(
            Finding(
                "ERROR",
                "P-STEM-COLLISION",
                f"{relative} 与其他 .tex 共享发布 stem："
                + ", ".join(str(path.relative_to(PROJECT_ROOT)) for path in collisions),
                "重命名 Source，确保 90_publish/<stem>.pdf 不会被覆盖。",
            )
        )

    if not PUBLISH_DIR.is_dir():
        findings.append(
            Finding(
                "ERROR",
                "P-NO-PUBLISH-DIR",
                "缺少 90_publish/ 发布目录。",
                "恢复项目发布目录；安全入口不会静默把 PDF 留在源码目录。",
            )
        )

    if not SHARED_COMPILE_SCRIPT.is_file():
        findings.append(
            Finding(
                "ERROR",
                "P-NO-COMPILER",
                f"找不到共享编译脚本：{SHARED_COMPILE_SCRIPT}",
                "恢复 infra/scripts/compile_tex.py 或更新本项目安全入口。",
            )
        )

    return findings


def publish_view_preflight(tex_path: Path) -> list[Finding]:
    """Validate an optional Atlas visual poster under assets/."""
    findings: list[Finding] = []
    try:
        relative = tex_path.relative_to(PROJECT_ROOT)
    except ValueError:
        return [Finding("ERROR", "PV-PATH", f"拒绝发布项目外视觉稿：{tex_path}", "视觉稿必须位于 kaoyan/ 内。")]


    if tex_path.suffix != ".tex" or not tex_path.is_file():
        return [Finding("ERROR", "PV-TARGET", f"目标不存在或不是 .tex：{relative}", "传入 Atlas assets/ 下真实存在的海报 .tex。")]

    if tex_path.parent.name != "assets":
        findings.append(
            Finding(
                "ERROR",
                "PV-LOCATION",
                f"Atlas 视觉稿必须位于 assets/：{relative}",
                "把视觉派生源放在 <Atlas>/assets/，避免和 Canonical Handbook Source 混淆。",
            )
        )
        atlas_readme = None
    else:
        if not tex_path.stem.endswith("_Poster"):
            findings.append(
                Finding(
                    "ERROR",
                    "PV-NAME",
                    f"Atlas 视觉稿必须使用 <Atlas>_Poster.tex 命名：{relative}",
                    "统一 Poster 后缀，避免 visual/poster/atlas-map 多套命名长期漂移。",
                )
            )
        atlas_readme = tex_path.parent.parent / "README.md"
        if not atlas_readme.exists() or not is_atlas_readme(atlas_readme):
            findings.append(
                Finding(
                    "ERROR",
                    "PV-NO-ATLAS",
                    f"{relative} 找不到上级 Canonical Atlas README。",
                    "视觉稿只能从显式声明 类型：Atlas 的 README 派生。",
                )
            )
        elif tex_path.stat().st_mtime < atlas_readme.stat().st_mtime:
            findings.append(
                Finding(
                    "ERROR",
                    "PV-STALE-SOURCE",
                    f"{relative} 早于 Canonical Atlas {atlas_readme.relative_to(PROJECT_ROOT)}。",
                    "先确认 README 的最新地图已经同步到海报源，再发布视觉稿。",
                )
            )

    collisions = [
        source for source in all_tex_files()
        if source.resolve() != tex_path and source.stem == tex_path.stem
    ]
    if collisions:
        findings.append(
            Finding(
                "ERROR",
                "PV-STEM-COLLISION",
                f"{relative} 与其他 .tex 共享发布 stem："
                + ", ".join(str(path.relative_to(PROJECT_ROOT)) for path in collisions),
                "为海报使用唯一 stem，例如 <Atlas>_Poster。",
            )
        )

    if not PUBLISH_DIR.is_dir():
        findings.append(Finding("ERROR", "PV-NO-PUBLISH-DIR", "缺少 90_publish/ 发布目录。"))
    if not SHARED_COMPILE_SCRIPT.is_file():
        findings.append(Finding("ERROR", "PV-NO-COMPILER", f"找不到共享编译脚本：{SHARED_COMPILE_SCRIPT}"))
    return findings


def project_compile_env() -> dict[str, str]:
    """Expose the project root to nested LaTeX sources without hard-coded ../../ paths."""
    env = os.environ.copy()
    existing = env.get("TEXINPUTS", "")
    env["TEXINPUTS"] = f"{PROJECT_ROOT}:{existing}"
    return env


def command_publish(raw_path: str, keep_aux: bool = False) -> int:
    tex_path = resolve_publish_target(raw_path)
    findings = publish_preflight(tex_path)
    if findings:
        for finding in findings:
            print(finding.render())
        print(f"{len(findings)} publish preflight error(s) found.")
        return 1

    target_dir = publish_target_dir(tex_path)
    command = [
        sys.executable,
        str(SHARED_COMPILE_SCRIPT),
        str(tex_path),
        "--publish-dir",
        str(target_dir),
    ]
    if keep_aux:
        command.append("--keep-aux")

    print(f"[PUBLISH] preflight passed: {tex_path.relative_to(PROJECT_ROOT)}")
    result = subprocess.run(command, cwd=PROJECT_ROOT, env=project_compile_env())
    if result.returncode != 0:
        print(f"[ERROR][P-COMPILE] shared compiler exited with code {result.returncode}.")
        return result.returncode or 1

    expected_pdf = target_dir / f"{tex_path.stem}.pdf"
    local_pdf = tex_path.with_suffix(".pdf")
    postflight: list[Finding] = []
    if not expected_pdf.is_file():
        postflight.append(
            Finding(
                "ERROR",
                "P-OUTPUT-MISSING",
                f"编译返回成功，但没有生成 {expected_pdf.relative_to(PROJECT_ROOT)}。",
                "不要把这次编译视为发布成功；检查共享 compile_tex.py 的路由。",
            )
        )
    elif expected_pdf.stat().st_mtime < tex_path.stat().st_mtime:
        postflight.append(
            Finding(
                "ERROR",
                "P-OUTPUT-STALE",
                f"{expected_pdf.relative_to(PROJECT_ROOT)} 仍旧于 {tex_path.relative_to(PROJECT_ROOT)}。",
                "检查编译是否真的覆盖了当前发布视图。",
            )
        )

    if local_pdf.exists():
        postflight.append(
            Finding(
                "ERROR",
                "P-LOCAL-PDF",
                f"源码目录仍残留同名 PDF：{local_pdf.relative_to(PROJECT_ROOT)}",
                "正式发布链要求 PDF 只保留在 90_publish/。",
            )
        )

    if postflight:
        for finding in postflight:
            print(finding.render())
        print(f"{len(postflight)} publish postflight error(s) found.")
        return 1

    print(f"OK: published {expected_pdf.relative_to(PROJECT_ROOT)}")
    return 0


def command_publish_view(raw_path: str, keep_aux: bool = False) -> int:
    tex_path = resolve_publish_target(raw_path)
    findings = publish_view_preflight(tex_path)
    if findings:
        for finding in findings:
            print(finding.render())
        print(f"{len(findings)} publish-view preflight error(s) found.")
        return 1

    target_dir = publish_target_dir(tex_path)
    command = [
        sys.executable,
        str(SHARED_COMPILE_SCRIPT),
        str(tex_path),
        "--publish-dir",
        str(target_dir),
    ]
    if keep_aux:
        command.append("--keep-aux")

    print(f"[PUBLISH-VIEW] preflight passed: {tex_path.relative_to(PROJECT_ROOT)}")
    result = subprocess.run(command, cwd=PROJECT_ROOT, env=project_compile_env())
    if result.returncode != 0:
        print(f"[ERROR][PV-COMPILE] shared compiler exited with code {result.returncode}.")
        return result.returncode or 1

    expected_pdf = target_dir / f"{tex_path.stem}.pdf"
    local_pdf = tex_path.with_suffix(".pdf")
    postflight: list[Finding] = []
    if not expected_pdf.is_file():
        postflight.append(
            Finding(
                "ERROR",
                "PV-OUTPUT-MISSING",
                f"编译返回成功，但没有生成 {expected_pdf.relative_to(PROJECT_ROOT)}。",
                "检查共享编译器的 PDF 路由。",
            )
        )
    elif expected_pdf.stat().st_mtime < tex_path.stat().st_mtime:
        postflight.append(
            Finding(
                "ERROR",
                "PV-OUTPUT-STALE",
                f"{expected_pdf.relative_to(PROJECT_ROOT)} 仍旧于 {tex_path.relative_to(PROJECT_ROOT)}。",
                "重新检查海报编译是否覆盖当前视觉稿。",
            )
        )
    if local_pdf.exists():
        postflight.append(
            Finding(
                "ERROR",
                "PV-LOCAL-PDF",
                f"视觉稿目录仍残留同名 PDF：{local_pdf.relative_to(PROJECT_ROOT)}",
                "派生 PDF 只保留在 90_publish/。",
            )
        )
    if postflight:
        for finding in postflight:
            print(finding.render())
        print(f"{len(postflight)} publish-view postflight error(s) found.")
        return 1

    print(f"OK: published Atlas visual {expected_pdf.relative_to(PROJECT_ROOT)}")
    return 0


def audit_readme_length() -> list[Finding]:
    findings: list[Finding] = []
    for readme in markdown_files():
        if readme.name != "README.md":
            continue
        relative = readme.relative_to(PROJECT_ROOT)
        if not is_handbook_area(relative):
            continue
        line_count = len(readme.read_text(encoding="utf-8").splitlines())
        max_lines = (
            COURSE_OR_SUBJECT_README_MAX_LINES
            if is_atlas_readme(readme) or len(relative.parts) <= 3
            else HANDBOOK_README_MAX_LINES
        )
        if line_count > max_lines:
            findings.append(
                Finding(
                    "AUDIT",
                    "A-README-LONG",
                    f"{relative} 有 {line_count} 行，超过当前 README 解释粒度审计阈值 {max_lines} 行。",
                    "Atlas 检查是否展开了 Topic 机制；Landing Page 检查是否把深度正文留在 README。行数本身不要求机械删减。",
                )
            )
    return findings


def audit_missing_tex() -> list[Finding]:
    findings: list[Finding] = []
    for readme in markdown_files():
        if readme.name != "README.md":
            continue
        relative = readme.relative_to(PROJECT_ROOT)
        if not is_handbook_area(relative) or not STATUS_RE.search(readme.read_text(encoding="utf-8")):
            continue
        status = status_text(readme)
        if is_atlas_readme(readme) or status_is_source_only(status):
            continue
        if handbook_tex_files(readme):
            continue

        # 深层目录若只是收纳多个子 Handbook 的索引，不把“没有自己的 .tex”当作债务。
        child_handbooks = [
            child / "README.md"
            for child in readme.parent.iterdir()
            if child.is_dir() and (child / "README.md").exists()
        ]
        if len(relative.parts) >= 4 and child_handbooks:
            continue

        findings.append(
            Finding(
                "AUDIT",
                "A-NO-TEX",
                f"{relative} 有深度 Handbook 状态入口，但当前目录没有 .tex 正文。",
                "若它只是索引，保持索引职责；若它是 Topic/Bridge/Integration，后续迁入唯一 Canonical .tex。Atlas 应显式声明 类型：Atlas，而不是补 .tex。",
            )
        )
    return findings


def audit_atlas_duplicate_tex() -> list[Finding]:
    """Flag root-level LaTeX beside a Canonical Atlas README as duplicate-truth risk."""
    findings: list[Finding] = []
    for readme in markdown_files():
        if not is_atlas_readme(readme):
            continue
        siblings = handbook_tex_files(readme)
        if not siblings:
            continue
        findings.append(
            Finding(
                "AUDIT",
                "A-ATLAS-DUPLICATE-TEX",
                f"{readme.relative_to(PROJECT_ROOT)} 已是 Canonical Atlas，但同目录仍有根级 .tex："
                + ", ".join(path.name for path in siblings),
                "把这些根级 .tex 视为待吸收 Source：先完成逐项 Source Diff，并确认有效信息已被 Canonical Owner 无损承接；在此之前默认保留，不得因 Atlas README 已存在就删除。真正的 Atlas 视觉海报放入 assets/。",
            )
        )
    return findings


def audit_tex_without_readme() -> list[Finding]:
    findings: list[Finding] = []
    for source in tex_files():
        if source in SYSTEM_TEX_TEMPLATES:
            continue
        if not (source.parent / "README.md").exists():
            findings.append(
                Finding(
                    "AUDIT",
                    "A-TEX-NO-README",
                    f"{source.relative_to(PROJECT_ROOT)} 所在目录没有 README Landing Page。",
                    "若它仍是有效 Handbook Source，补稳定入口；若只是 legacy/source，明确其过渡角色。",
                )
            )
    return findings


def audit_orphan_pdfs() -> list[Finding]:
    findings: list[Finding] = []
    stems = {source.stem for source in all_tex_files()}
    for pdf in sorted(PUBLISH_DIR.rglob("*.pdf")):
        if pdf.stem not in stems:
            findings.append(
                Finding(
                    "AUDIT",
                    "A-ORPHAN-PDF",
                    f"{pdf.relative_to(PROJECT_ROOT)} 找不到当前仓库中的同 stem .tex。",
                    "把它视为待吸收的 legacy/source：先做 Source Diff，确认有效信息已进入唯一 Canonical Owner；完成前默认保留，之后再决定重新纳管、退休或删除。",
                )
            )
    return findings


def audit_current_publication() -> list[Finding]:
    """Report current Canonical bodies whose reading view is missing or stale."""
    findings: list[Finding] = []
    for readme in markdown_files():
        if readme.name != "README.md":
            continue
        relative = readme.relative_to(PROJECT_ROOT)
        if not is_handbook_area(relative) or is_atlas_readme(readme):
            continue

        status = status_text(readme)
        if not status_claims_handbook_body(status) or status_is_source_only(status):
            continue
        if status_claims_published(status):
            # The same condition is a hard error when the README explicitly claims publication.
            continue

        sources = handbook_tex_files(readme)
        if len(sources) != 1:
            continue
        source = sources[0]
        pdf = find_published_pdf(source.stem)
        if pdf is None:
            expected_dest = publish_target_dir(source) / f"{source.stem}.pdf"
            findings.append(
                Finding(
                    "AUDIT",
                    "A-PUBLISH-NOT-BUILT",
                    f"{source.relative_to(PROJECT_ROOT)} 已是当前 Canonical 正文，但还没有 {expected_dest.relative_to(PROJECT_ROOT)}。",
                    f"需要阅读版时运行 python3 00_system/cognitive_system.py publish \"{source.relative_to(PROJECT_ROOT)}\"。",
                )
            )
        elif pdf.stat().st_mtime < source.stat().st_mtime:
            findings.append(
                Finding(
                    "AUDIT",
                    "A-PUBLISH-STALE",
                    f"{pdf.relative_to(PROJECT_ROOT)} 旧于当前 Canonical Source {source.relative_to(PROJECT_ROOT)}。",
                    f"稳定修订完成后重新运行 python3 00_system/cognitive_system.py publish \"{source.relative_to(PROJECT_ROOT)}\"。",
                )
            )
    return findings


def audit_training_figure_todos() -> list[Finding]:
    """Surface unresolved required figure intents in official training navigation."""
    findings: list[Finding] = []
    for readme in PROJECT_ROOT.rglob("README.md"):
        text = readme.read_text(encoding="utf-8")
        nav_match = TRAINING_NAV_HEADING_RE.search(text)
        if not nav_match:
            continue

        section_start = nav_match.end()
        next_h2 = re.search(r"^##\s+", text[section_start:], re.MULTILINE)
        section_end = section_start + next_h2.start() if next_h2 else len(text)
        nav_text = text[section_start:section_end]

        for raw_link in LINK_RE.findall(nav_text):
            parsed = urlparse(raw_link)
            if parsed.scheme or parsed.netloc:
                continue
            link_path = unquote(parsed.path)
            if not link_path.endswith(".md"):
                continue
            target = (readme.parent / link_path).resolve()
            if not target.is_file():
                continue
            try:
                target_rel = target.relative_to(PROJECT_ROOT)
            except ValueError:
                continue

            training_text = target.read_text(encoding="utf-8")
            matches = list(REQUIRED_TRAINING_FIGURE_RE.finditer(training_text))
            if not matches:
                continue
            names = ", ".join(match.group(1).strip() for match in matches)
            findings.append(
                Finding(
                    "AUDIT",
                    "A-TRAINING-FIGURE-TODO",
                    f"{target_rel} 还有 {len(matches)} 个必要图意图未闭环：{names}。",
                    "正文语义可以先完成；专题集中图审时逐项决定删除、复用、链接 Canonical 图或新建 assets/src 图源。父专题进入‘已采用’前必须清零。",
                )
            )
    return findings


def audit_duplicate_titles() -> list[Finding]:
    findings: list[Finding] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    for path in markdown_files():
        if path.name == "README.md" or path.relative_to(PROJECT_ROOT) in EXCLUDED_PROGRESS_SOURCES:
            continue
        title_match = TITLE_RE.search(path.read_text(encoding="utf-8"))
        if title_match:
            titles[title_match.group(1).strip()].append(path.relative_to(PROJECT_ROOT))
    for title, paths in sorted(titles.items()):
        if len(paths) <= 1:
            continue
        findings.append(
            Finding(
                "AUDIT",
                "A-DUPLICATE-TITLE",
                f"标题“{title}”出现在多个 Markdown 文件：" + ", ".join(p.as_posix() for p in paths),
                "人工判断它们是合法 Source 重复、不同职责同名，还是需要收敛 Owner；不要仅凭标题自动删文件。",
            )
        )
    return findings


def audit_findings() -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(audit_readme_length())
    findings.extend(audit_missing_tex())
    findings.extend(audit_atlas_duplicate_tex())
    findings.extend(audit_tex_without_readme())
    findings.extend(audit_orphan_pdfs())
    findings.extend(audit_current_publication())
    findings.extend(audit_training_figure_todos())
    findings.extend(audit_duplicate_titles())
    return findings


def command_audit(show_all: bool = False) -> int:
    findings = audit_findings()
    if not findings:
        print("OK: no maintenance debt detected by current audit rules.")
        return 0

    counts = Counter(finding.code for finding in findings)
    print("AUDIT SUMMARY: " + ", ".join(f"{code}={count}" for code, count in sorted(counts.items())))

    visible = findings if show_all else [
        finding for finding in findings if finding.code != "A-NO-TEX"
    ]
    for finding in visible:
        print(finding.render())

    omitted = counts.get("A-NO-TEX", 0) if not show_all else 0
    if omitted:
        print(
            f"[AUDIT][A-NO-TEX] {omitted} 个待建设 Handbook 目录未逐条展开；"
            "需要完整建设库存时运行 audit --all。"
        )
    return 0


# ---------------------------------------------------------------------------
# CLI surface.
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Progress, consistency, and interaction helpers."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    progress_parser = subparsers.add_parser("progress", help="render project progress")
    progress_parser.add_argument(
        "--write", action="store_true", help="write the generated PROGRESS.md"
    )

    subparsers.add_parser("check", help="check links, status entries, and progress")
    audit_parser = subparsers.add_parser(
        "audit", help="report maintainability debt without failing"
    )
    audit_parser.add_argument(
        "--all", action="store_true", help="also list every A-NO-TEX construction backlog item"
    )

    publish_parser = subparsers.add_parser(
        "publish", help="safely compile one Canonical Handbook and verify its published PDF"
    )
    publish_parser.add_argument("tex", help="Canonical .tex path inside kaoyan/")
    publish_parser.add_argument(
        "--keep-aux", action="store_true", help="pass through to the shared compiler"
    )

    publish_view_parser = subparsers.add_parser(
        "publish-view", help="safely compile an Atlas visual poster from <Atlas>/assets/"
    )
    publish_view_parser.add_argument("tex", help="derived Atlas poster .tex under assets/")
    publish_view_parser.add_argument(
        "--keep-aux", action="store_true", help="pass through to the shared compiler"
    )

    start_parser = subparsers.add_parser(
        "start", help="render a scenario-specific Context Pack without modifying files"
    )
    start_parser.add_argument("scenario", choices=sorted(SCENARIOS))
    start_parser.add_argument(
        "--subject",
        required=True,
        help="subject key or alias, e.g. calculus, 高数, linear-algebra, probability, math",
    )
    start_parser.add_argument(
        "--topic", help="optional topic/bridge/integration keyword used to find nearby assets"
    )

    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "progress":
        return command_progress(args.write)
    if args.command == "check":
        return command_check()
    if args.command == "audit":
        return command_audit(args.all)
    if args.command == "publish":
        return command_publish(args.tex, args.keep_aux)
    if args.command == "publish-view":
        return command_publish_view(args.tex, args.keep_aux)
    if args.command == "start":
        return command_start(args.scenario, args.subject, args.topic)
    return 2


if __name__ == "__main__":
    sys.exit(main())
