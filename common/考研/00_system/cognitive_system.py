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
import re
import subprocess
import sys
import textwrap
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote, unquote, urlparse


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CURRENT_PATH = PROJECT_ROOT / "CURRENT.md"
PROGRESS_PATH = PROJECT_ROOT / "PROGRESS.md"
PUBLISH_DIR = PROJECT_ROOT / "90_publish"
COMMON_COMPILE_SCRIPT = PROJECT_ROOT.parent / "scripts" / "compile_tex.py"

# README 是导航页，不是正文。行数阈值只用于发现明显越界，不用于判断内容质量。
COURSE_OR_SUBJECT_README_MAX_LINES = 600
HANDBOOK_README_MAX_LINES = 150

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

EXCLUDED_PROGRESS_SOURCES = {
    Path("CURRENT.md"),
    Path("PROGRESS.md"),
}

# ---------------------------------------------------------------------------
# Interaction routing: scenario prompts, subject aliases, and Context Packs.
# ---------------------------------------------------------------------------

PROMPTS = {
    "explore": """
        当前角色：Mapper + Socratic Tutor。

        我还没有形成这个专题的稳定心智模型。下面是我目前的直觉和困惑。
        请先读取现有学科复习总览与导航和 Atlas，并明确仓库当前是否已有成熟 Topic。

        不要直接写完整讲义。请从母问题开始，建立最小对象/关系/过程，
        用一个生成性例子运行它，再改变条件攻击它，最后让我重新解释。
        请区分仓库已有模型、你的工作假设和我已经确认的理解。
    """,
    "model-diff": """
        当前角色：Socratic Tutor + Mapper。

        这是我先用自己的话形成的理解，以及对应的现有 Handbook。
        不要重新讲整章，也不要先给标准总结。

        请依次完成：
        1. 标出我已经抓住的正确主干；
        2. 标出层次混淆、缺失连接和边界错误；
        3. 区分事实问题与只是表达不清；
        4. 给出最少但有区分力的反例或边界问题；
        5. 等我重新解释后，再判断 No Update、Inbox 还是需要挑战 Handbook。
    """,
    "first-divergence": """
        当前角色：Debugger。

        我会提供题目、原始过程、答案和用时。不要先重做整题，不要补造缺失思路。

        请依次完成：
        1. 复原我实际识别了什么、选择了什么路径；
        2. 定位第一次偏离有效路径的位置，而不是最后写错的位置；
        3. 区分观察事实、主要假设和至少一个竞争解释；
        4. 判断最有用的一类：模型、识别、路径、执行/检查/表达、考试决策；
        5. 给出能区分解释的最小复测；
        6. 建议 No Update、Inbox 或待验证 Rule，但不要替我做最终晋升决定。
    """,
    "solve": """
        当前角色：Model-Grounded Solver。

        这道题我不会，请先读取我们已有的 Atlas、Topic 和 Subject Rules。
        如果 Topic 尚无成熟正文，请明确说明，不要把临时解释冒充项目模型。

        请按以下顺序回答：
        1. Model Anchor；
        2. 题面到模型的表示；
        3. 路径选择理由；
        4. 逐步解题链，并标出每一步调用的机制；
        5. Verification；
        6. 下次可调用的压缩信号；
        7. 一个让我复原起手或关键转折的问题。
    """,
    "adversary": """
        当前角色：Adversary。

        下面是一条候选规则及已有表现。请不要因为它听起来合理就接受。

        请检查：
        1. 最小反例；
        2. 表面形式变化后是否仍可调用；
        3. 缺少哪个条件会失效；
        4. 它是机制结论、通用动作还是局部技巧；
        5. 时间和注意力成本；
        6. 是否有更简单的竞争规则；
        7. 下一次最小验证动作。

        最后给出“采用 / 收窄后验证 / 局部保留 / 否定 / No Update”的建议，决定权留给我。
    """,
    "import-handbook": """
        当前角色：Mapper + Editor。

        我要导入一份新手册、旧 LaTeX 或外部材料。它目前只是输入，不自动成为 Canonical Owner。

        请依次完成：
        1. 判断它属于 Atlas、Topic、Bridge、Integration、Rules 还是 Publication；
        2. 查找当前 Canonical Owner；
        3. 做 Handbook Diff：重复、真正新增、冲突、越界、Control/Evidence 混入；
        4. 列出需要我人工确认的模型选择；
        5. 确认后再更新正确 Owner；
        6. 说明必须更新、条件更新和不应更新的文件；
        7. 更新资产状态，运行 progress 和 check。

        不要为了完整阅读体验复制其他 Topic 的完整机制。
    """,
    "weekly-review": """
        当前角色：Adversary + Editor + Coach。

        下面是本周 Inbox、待验证 Rules 和真实表现。

        请找出：
        1. 可以删除的一次性或重复记录；
        2. 重复出现但仍有竞争解释的模式；
        3. 值得继续攻击的候选规则；
        4. 已有迁移证据、可由我决定采用的规则；
        5. 与 Handbook 冲突的证据；
        6. 最少的下一轮诊断题；
        7. CURRENT.md 应更新的当前焦点和下一步。

        不以新增文档数量作为进度。
    """,
    "practice": """
        当前角色：Coach。

        下面是已经确认的具体断点。请读取相关 Topic 和 Subject Rules，
        只设计少量有区分力的诊断题，不继续堆同质练习。

        对每道题说明：观察目标、为什么能区分当前假设、何时停止基础训练，
        以及下一步升级或降阶条件。不要预先给完整答案。
    """,
    "publish": """
        当前角色：Editor。

        我要编译并发布一个 Handbook。

        请先检查：
        1. 目标 .tex 是否就是该 Handbook 的 Canonical Source；
        2. README 是否只承担 Landing Page，而没有复制正文；
        3. 受影响的 Uses、Bridge、Integration 和发布链接；
        4. 是否还有待人工确认的模型结论；
        5. 使用项目 compile_tex.py 后的引用、页数和警告；
        6. PDF 是否进入 90_publish/，专题目录是否保持零同名 PDF；
        7. 发布后需要更新的状态与进度。

        不在 PDF 或 README 中创造 Canonical .tex 尚未拥有的新结论。
    """,
}


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
    context_paths = [Path(path) for path in subject_config["context"]]

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


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in PROJECT_ROOT.rglob("*.md")
        if ".git" not in path.parts
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
        link = quote(relative.as_posix(), safe="/._-")
        lines.append(
            f"| {markdown_escape(area)} | "
            f"[{markdown_escape(title)}]({link}) | "
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
        if ".git" not in path.parts and "90_publish" not in path.parts
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
            pdf = PUBLISH_DIR / f"{source.stem}.pdf"
            if not pdf.exists():
                findings.append(
                    Finding(
                        "ERROR",
                        "E-PUBLISH-MISSING",
                        f"{relative} 声称已有发布视图，但缺少 {pdf.relative_to(PROJECT_ROOT)}。",
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


def structural_findings() -> list[Finding]:
    findings: list[Finding] = []
    findings.extend(broken_link_findings())
    findings.extend(handbook_status_findings())
    findings.extend(publish_collision_findings())
    findings.extend(ownership_findings())
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
                "publish 只允许处理 common/考研 内部的 Canonical Handbook Source。",
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

    if not COMMON_COMPILE_SCRIPT.is_file():
        findings.append(
            Finding(
                "ERROR",
                "P-NO-COMPILER",
                f"找不到共享编译脚本：{COMMON_COMPILE_SCRIPT}",
                "恢复 common/scripts/compile_tex.py 或更新本项目安全入口。",
            )
        )

    return findings


def publish_view_preflight(tex_path: Path) -> list[Finding]:
    """Validate an optional Atlas visual poster under assets/."""
    findings: list[Finding] = []
    try:
        relative = tex_path.relative_to(PROJECT_ROOT)
    except ValueError:
        return [Finding("ERROR", "PV-PATH", f"拒绝发布项目外视觉稿：{tex_path}", "视觉稿必须位于 common/考研 内。")]

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
    if not COMMON_COMPILE_SCRIPT.is_file():
        findings.append(Finding("ERROR", "PV-NO-COMPILER", f"找不到共享编译脚本：{COMMON_COMPILE_SCRIPT}"))
    return findings


def command_publish(raw_path: str, keep_aux: bool = False) -> int:
    tex_path = resolve_publish_target(raw_path)
    findings = publish_preflight(tex_path)
    if findings:
        for finding in findings:
            print(finding.render())
        print(f"{len(findings)} publish preflight error(s) found.")
        return 1

    command = [sys.executable, str(COMMON_COMPILE_SCRIPT), str(tex_path)]
    if keep_aux:
        command.append("--keep-aux")

    print(f"[PUBLISH] preflight passed: {tex_path.relative_to(PROJECT_ROOT)}")
    result = subprocess.run(command, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print(f"[ERROR][P-COMPILE] shared compiler exited with code {result.returncode}.")
        return result.returncode or 1

    expected_pdf = PUBLISH_DIR / f"{tex_path.stem}.pdf"
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

    command = [sys.executable, str(COMMON_COMPILE_SCRIPT), str(tex_path)]
    if keep_aux:
        command.append("--keep-aux")

    print(f"[PUBLISH-VIEW] preflight passed: {tex_path.relative_to(PROJECT_ROOT)}")
    result = subprocess.run(command, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print(f"[ERROR][PV-COMPILE] shared compiler exited with code {result.returncode}.")
        return result.returncode or 1

    expected_pdf = PUBLISH_DIR / f"{tex_path.stem}.pdf"
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
        if is_atlas_readme(readme):
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
                "把旧 .tex 明确降为 legacy/source；真正的 Atlas 视觉海报放入 assets/，且不得拥有 README 中没有的新结论。",
            )
        )
    return findings


def audit_tex_without_readme() -> list[Finding]:
    findings: list[Finding] = []
    for source in tex_files():
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
    if not PUBLISH_DIR.exists():
        return findings
    for pdf in sorted(PUBLISH_DIR.glob("*.pdf")):
        if pdf.stem not in stems:
            findings.append(
                Finding(
                    "AUDIT",
                    "A-ORPHAN-PDF",
                    f"{pdf.relative_to(PROJECT_ROOT)} 找不到当前仓库中的同 stem .tex。",
                    "把它视为 legacy-unregistered；只在真实重构该手册时决定纳管或删除。",
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
        pdf = PUBLISH_DIR / f"{source.stem}.pdf"
        if not pdf.exists():
            findings.append(
                Finding(
                    "AUDIT",
                    "A-PUBLISH-NOT-BUILT",
                    f"{source.relative_to(PROJECT_ROOT)} 已是当前 Canonical 正文，但还没有 {pdf.relative_to(PROJECT_ROOT)}。",
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


def command_prompt(name: str) -> int:
    print(textwrap.dedent(PROMPTS[name]).strip())
    return 0


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
    publish_parser.add_argument("tex", help="Canonical .tex path inside common/考研")
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

    prompt_parser = subparsers.add_parser("prompt", help="print a reusable AI prompt")
    prompt_parser.add_argument("name", choices=sorted(PROMPTS))
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
    if args.command == "prompt":
        return command_prompt(args.name)
    return 2


if __name__ == "__main__":
    sys.exit(main())
