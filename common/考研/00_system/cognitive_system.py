#!/usr/bin/env python3
"""Small, dependency-free helpers for the cognitive learning repository."""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse, quote


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CURRENT_PATH = PROJECT_ROOT / "CURRENT.md"
PROGRESS_PATH = PROJECT_ROOT / "PROGRESS.md"

STATUS_RE = re.compile(
    r"^\s*>?\s*(?:当前)?状态[：:]\s*(.+?)\s*$", re.MULTILINE
)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")

EXCLUDED_PROGRESS_SOURCES = {
    Path("CURRENT.md"),
    Path("PROGRESS.md"),
}

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
                    tex_files = sorted(absolute.parent.glob("*.tex"))
                    if len(tex_files) == 1:
                        tex_relative = tex_files[0].relative_to(PROJECT_ROOT)
                        print(f"  Canonical .tex: {tex_relative.as_posix()}")
                    elif len(tex_files) > 1:
                        names = ", ".join(p.name for p in tex_files)
                        print(f"  Canonical .tex: AMBIGUOUS ({names})")
                    else:
                        print("  Canonical .tex: MISSING — README/Source 不等于 Handbook 正文")
        else:
            print("- 未找到直接命中；先使用上述 Atlas 建立 provisional model，不冒充成熟 Topic。")

    return 0


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
    if "旧工作稿待迁移" in status:
        return "Handbook Source 待迁移"
    if "需修订" in status:
        return "需修订"
    if "旧发布物" in status or "旧综合发布物" in status:
        return "旧发布物待纳管"
    if "待人工确认" in status:
        return "待人工确认"
    if "工作稿" in status or "工作梳理稿" in status:
        return "工作稿"
    if "已发布" in status:
        return "已发布"
    if "框架已采用" in status or "目录已建立" in status or status == "规划":
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
            "2. 某项资产真实推进时，修改其入口顶部的 `状态：...`；",
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


def broken_links() -> list[str]:
    issues: list[str] = []
    for path in markdown_files():
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
                issues.append(f"broken link: {relative} -> {link}")
    return issues


def check_handbook_package_and_status() -> list[str]:
    issues: list[str] = []
    for path in markdown_files():
        relative = path.relative_to(PROJECT_ROOT)
        text = path.read_text(encoding="utf-8")
        status_match = STATUS_RE.search(text)
        if not status_match:
            continue
        status = status_match.group(1).strip()

        # 1. Status claim vs .tex existence check
        is_canonical_claim = any(kw in status for kw in ["已采用", "Canonical", "已发布"]) and not any(
            kw in status for kw in [
                "旧", "legacy", "工作稿", "草稿", "框架", "目录", "未建", "规划",
                "待确认", "待解耦", "待建", "分阶段", "正文待", "架构已采用", "Landing Page", "已建立"
            ]
        )
        if is_canonical_claim:
            has_tex = any(path.parent.glob("*.tex"))
            if not has_tex:
                issues.append(
                    f"status mismatch: {relative} claims '{status}' but missing canonical .tex file in {relative.parent.as_posix()} (must be marked as legacy/provisional working draft)"
                )

        # 2. README bloat / Landing Page limit check
        if path.name == "README.md" and relative != Path("README.md"):
            is_legacy_or_draft = any(kw in status for kw in ["旧", "legacy", "工作稿", "草稿"])
            is_subject_portal = relative.parent in {Path("10_数学一"), Path("20_英语一"), Path("30_408")}
            line_count = len(text.splitlines())
            if line_count > 200 and not is_legacy_or_draft and not is_subject_portal:
                issues.append(
                    f"README bloat: {relative} ({line_count} lines > 200 limit); README must be a concise Landing Page, move mechanism details to .tex or mark as legacy working draft"
                )

    return issues


def check_ownership_matrix_and_duplicates() -> list[str]:
    issues: list[str] = []
    ownership_path = PROJECT_ROOT / "00_system" / "ownership_matrix.md"
    if ownership_path.exists():
        text = ownership_path.read_text(encoding="utf-8")
        for raw_link in LINK_RE.findall(text):
            link = normalize_link(raw_link)
            parsed = urlparse(link)
            if parsed.scheme or link.startswith("#"):
                continue
            target_text = unquote(parsed.path)
            if not target_text:
                continue
            target = (ownership_path.parent / target_text).resolve()
            if not target.exists():
                issues.append(f"ownership matrix broken reference: 00_system/ownership_matrix.md -> {link}")

    title_to_files: dict[str, list[Path]] = {}
    for path in markdown_files():
        relative = path.relative_to(PROJECT_ROOT)
        text = path.read_text(encoding="utf-8")
        status_match = STATUS_RE.search(text)
        status = status_match.group(1).strip() if status_match else ""
        if any(kw in status for kw in ["旧", "legacy"]):
            continue
        title_match = TITLE_RE.search(text)
        if title_match:
            title = title_match.group(1).strip()
            if title and title not in {"项目进度", "当前焦点", "通用解题控制内核", "AGENTS", "README"}:
                title_to_files.setdefault(title, []).append(relative)

    for title, files in title_to_files.items():
        if len(files) > 1:
            file_list = ", ".join(f.as_posix() for f in files)
            issues.append(f"duplicate H1 title / canonical owner conflict: '{title}' in [{file_list}]")

    return issues


def check_current_freshness() -> list[str]:
    issues: list[str] = []
    if not CURRENT_PATH.exists():
        issues.append("CURRENT.md is missing; must exist as current focus entry")
    else:
        text = CURRENT_PATH.read_text(encoding="utf-8").strip()
        if not text:
            issues.append("CURRENT.md is empty")
        elif "# 当前焦点" not in text:
            issues.append("CURRENT.md missing '# 当前焦点' section")
    return issues


def structural_issues() -> list[str]:
    issues = broken_links()
    for path in markdown_files():
        text = path.read_text(encoding="utf-8")
        if STATUS_RE.search(text) and not TITLE_RE.search(text):
            relative = path.relative_to(PROJECT_ROOT)
            issues.append(f"status without H1 title: {relative}")

    issues.extend(check_handbook_package_and_status())
    issues.extend(check_ownership_matrix_and_duplicates())
    issues.extend(check_current_freshness())

    expected_progress = render_progress()
    if not PROGRESS_PATH.exists():
        issues.append("PROGRESS.md is missing; run progress --write")
    elif PROGRESS_PATH.read_text(encoding="utf-8") != expected_progress:
        issues.append("PROGRESS.md is stale; run progress --write")
    return issues


def command_progress(write: bool) -> int:
    if write:
        changed = write_progress()
        action = "updated" if changed else "already current"
        print(f"{PROGRESS_PATH.relative_to(PROJECT_ROOT)}: {action}")
    else:
        print(render_progress(), end="")
    return 0


def command_check() -> int:
    issues = structural_issues()
    if not issues:
        print("OK: links, status entries, and generated progress are consistent.")
        return 0
    for issue in issues:
        print(f"ERROR: {issue}")
    print(f"{len(issues)} issue(s) found.")
    return 1


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
    if args.command == "start":
        return command_start(args.scenario, args.subject, args.topic)
    if args.command == "prompt":
        return command_prompt(args.name)
    return 2


if __name__ == "__main__":
    sys.exit(main())
