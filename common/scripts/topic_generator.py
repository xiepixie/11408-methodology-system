#!/usr/bin/env python3
"""
topic_generator.py — 从 topic_spec.md 生成专题课骨架文件。

用法:
  python3 topic_generator.py common/topics/解三角形_边角互化
  python3 topic_generator.py common/topics/解三角形_边角互化 --compile

生成的文件:
  - questions.tex     (题目引入清单，需手动填入具体题目路径)
  - 学案.tex          (学生版讲义骨架)
  - 教案.tex          (教师版讲义骨架)

依赖: Python 3.10+, 无第三方库。
编译: 需要 xelatex + ctex。
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
POOL_REL = "../../../common/pool"


def _latex_escape(text: str) -> str:
    """转义 LaTeX 特殊字符，用于标题等文本。"""
    return text.replace("_", r"\_").replace("&", r"\&").replace("%", r"\%")


# ── spec 解析 ──────────────────────────────────────────
def parse_spec(spec_path: Path) -> dict:
    """从 topic_spec.md 提取结构化信息。"""
    text = spec_path.read_text(encoding="utf-8")
    spec: dict = {}

    # 基本信息
    for key, pattern in [
        ("title", r"专题名称:\s*(.+)"),
        ("duration", r"时长:\s*(.+)"),
        ("audience", r"适用对象:\s*(.+)"),
    ]:
        m = re.search(pattern, text)
        spec[key] = m.group(1).strip() if m else ""

    # 教学目标
    spec["objectives"] = [
        m.strip() for m in re.findall(r"\- \[ \]\s*(.+)", text)
    ]

    # 专题边界
    spec["includes"] = _extract_list(text, "覆盖范围")
    spec["excludes"] = _extract_list(text, "不覆盖")

    # 方法链条（保留缩进格式）
    chain_match = re.search(
        r"方法链条.*?```\n(.*?)```", text, re.DOTALL
    )
    spec["method_chain"] = chain_match.group(1).strip() if chain_match else ""

    # 例题规划表格
    spec["examples"] = _parse_example_table(text)

    # 公式
    spec["formulas"] = [
        m.strip() for m in re.findall(r"- (.+)", _extract_section(text, "核心公式"))
        if m.strip()
    ]

    # 易错点
    spec["pitfalls"] = _extract_list(text, "易错点")

    # 学生常见问题
    spec["student_issues"] = _extract_list(text, "学生常见问题")

    return spec


def _extract_list(text: str, header: str) -> list[str]:
    """提取某小节下方的列表项（到下一个 ## 或 ### 为止）。"""
    pattern = rf"{re.escape(header)}.*?\n((?:- .+\n?)+)"
    m = re.search(pattern, text)
    if not m:
        return []
    return [
        line.lstrip("- ").strip()
        for line in m.group(1).strip().splitlines()
        if line.strip().startswith("-")
    ]


def _extract_section(text: str, header: str) -> str:
    """提取某小节的全部内容，到下一个 ## 为止。"""
    pattern = rf"## {re.escape(header)}.*?\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL)
    return m.group(1) if m else ""


def _parse_example_table(text: str) -> list[dict]:
    """解析例题规划 markdown 表格。"""
    examples = []
    in_table = False
    for line in text.splitlines():
        if "例题规划" in line:
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 4 and cols[0].isdigit():
                examples.append({
                    "num": int(cols[0]),
                    "role": cols[1],
                    "desc": cols[2],
                    "difficulty": cols[3],
                })
        elif in_table and not line.startswith("|") and line.strip():
            break
    return examples


# ── questions.tex 生成 ──────────────────────────────────
def gen_questions(spec: dict) -> str:
    """生成 questions.tex 骨架（需手动填入路径）。"""
    title_esc = _latex_escape(spec['title'])
    lines = [
        f"% =====================================================",
        f"% {title_esc} 题目组装",
        f"% =====================================================",
        f"",
        f"% TODO: 将以下占位替换为 pool 中的实际题目路径",
        f"% 格式: \\input{{{POOL_REL}}}/专题/难度/q_xxx.tex",
        f"",
    ]
    for ex in spec["examples"]:
        lines.append(f"% 例题 {ex['num']}: {ex['desc']} ({ex['role']}, {ex['difficulty']})")
        lines.append(f"% \\input{{{POOL_REL}}}/??/??/q_???.tex")
        lines.append("")
    return "\n".join(lines) + "\n"


# ── 学案.tex 生成 ──────────────────────────────────────
def gen_student(spec: dict, rel_ipara: str) -> str:
    """生成学案 .tex 骨架。"""
    title_esc = _latex_escape(spec['title'])
    formulas_block = _gen_formula_table(spec)
    objectives_block = "\n".join(
        f"  \\item {obj}" for obj in spec["objectives"]
    )
    examples_block = "\n\n".join(
        _student_example(ex) for ex in spec["examples"]
    )

    # 空 pitfalls 时不生成空 itemize
    pitfalls_items = "\n".join(
        f"  \\item {p}" for p in spec["pitfalls"]
    )
    if pitfalls_items:
        pitfalls_section = (
            f"\\begin{{itemize}}[itemsep=0.4em]\n{pitfalls_items}\n\\end{{itemize}}"
        )
    else:
        pitfalls_section = "\\textit{待补充易错点}"

    return f"""\
\\documentclass[11pt,a4paper]{{ctexart}}
\\usepackage[student]{{{rel_ipara}}}
\\input{{questions.tex}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\lhead{{\\small {title_esc} 学案}}
\\rhead{{\\small {spec.get('audience', '')}}}
\\cfoot{{\\small 第 \\thepage\\ 页\\quad 共 \\pageref{{LastPage}} 页}}
\\renewcommand{{\\headrulewidth}}{{0.4pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}

\\newcommand{{\\sessionformulas}}{{%
  \\arrayrulecolor{{rulecolor}}
  \\begin{{tabularx}}{{\\textwidth}}{{p{{4.2cm}}X}}
  \\toprule[1.2pt]
{formulas_block}  \\bottomrule[1.2pt]
  \\end{{tabularx}}
}}

\\begin{{document}}

\\begin{{center}}
  {{\\Large\\bfseries {title_esc} 学案}}\\\\
  \\vspace{{0.5em}}
  姓名：\\blank{{2.6cm}}
  \\quad
  日期：\\blank{{2.6cm}}
  \\quad
  时长：{spec.get('duration', '120 分钟')}
\\end{{center}}

\\section{{本讲目标}}

\\begin{{itemize}}[itemsep=0.3em]
{objectives_block}
\\end{{itemize}}

\\section{{公式准备}}

\\begingroup
\\large
\\renewcommand{{\\arraystretch}}{{1.55}}
\\linespread{{1.35}}\\selectfont
\\showprompttrue
\\sessionformulas
\\endgroup

\\newpage

\\section{{课堂题目}}

{examples_block}

\\newpage

\\section{{易错自查}}

{pitfalls_section}

\\vspace{{1em}}
\\noindent\\textbf{{本讲我最需要记住的一句话是：}}
\\vspace{{0.5em}}

\\blank{{14cm}}

\\end{{document}}
"""


def _gen_formula_table(spec: dict) -> str:
    """生成公式表格行，每行带 \\fblank 空白。使用 \\midrule 兼容 booktabs。"""
    rows = []
    for f in spec["formulas"]:
        # 简单处理：把等号左边当标签，右边留空让学生填
        parts = f.split(":", 1) if ":" in f else f.split("=", 1)
        if len(parts) == 2:
            label = parts[0].strip()
            content = parts[1].strip()
            rows.append(
                f"  {label} & {content}\\\\ \\midrule"
            )
        else:
            rows.append(f"  {f} & \\fblank[4cm]{{}}\\\\ \\midrule")
    return "\n".join(rows) + "\n" if rows else ""


def _student_example(ex: dict) -> str:
    """生成单道例题的学案区块。"""
    num = ex["num"]
    role = ex["role"]
    return f"""\\subsection{{例题 {num}（{role}）}}

\\studentproblem{{{num}}}
\\answerblank[5cm]{{解：}}

\\studentthink{{\\item 待补充}}
"""


# ── 教案.tex 生成 ──────────────────────────────────────
def gen_teacher(spec: dict, rel_ipara: str) -> str:
    """生成教案 .tex 骨架。"""
    title_esc = _latex_escape(spec['title'])
    objectives_block = "\n".join(
        f"  \\item {obj}" for obj in spec["objectives"]
    )
    schedule_block = _gen_schedule(spec)
    examples_block = "\n\n".join(
        _teacher_example(ex) for ex in spec["examples"]
    )
    chain_block = _format_chain(spec.get("method_chain", ""))

    # 空 student_issues 时不生成空 itemize
    student_issues_items = "\n".join(
        f"  \\item {s}" for s in spec.get("student_issues", [])
    )
    if student_issues_items:
        student_issues_section = (
            f"\\begin{{itemize}}[itemsep=0.4em]\n{student_issues_items}\n\\end{{itemize}}"
        )
    else:
        student_issues_section = "\\textit{待补充学生常见问题}"

    return f"""\
\\documentclass[11pt,a4paper]{{ctexart}}
\\usepackage[teacher]{{{rel_ipara}}}
\\input{{questions.tex}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\lhead{{\\small {title_esc} 教案}}
\\rhead{{\\small 数学一对一}}
\\cfoot{{\\small 第 \\thepage\\ 页\\quad 共 \\pageref{{LastPage}} 页}}
\\renewcommand{{\\headrulewidth}}{{0.4pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}

\\begin{{document}}

\\begin{{center}}
  {{\\Large\\bfseries {title_esc} 教案}}\\\\
  \\vspace{{0.5em}}
  时长：{spec.get('duration', '120 分钟')}
\\end{{center}}

\\section{{备课指导}}

\\teachblock{{本讲目标}}{{%
\\begin{{itemize}}[itemsep=0.3em]
{objectives_block}
\\end{{itemize}}
}}

\\teachblock{{专题边界}}{{%
\\textbf{{覆盖:}} {', '.join(spec.get('includes', ['待补充']))}\\\\
\\textbf{{不覆盖:}} {', '.join(spec.get('excludes', ['待补充']))}
}}

\\section{{120 分钟课堂流程}}

\\begin{{tabularx}}{{\\textwidth}}{{p{{2.8cm}}p{{3.2cm}}X}}
\\toprule
时间 & 环节 & 教师动作\\\\
\\midrule
{schedule_block}\\bottomrule
\\end{{tabularx}}

\\section{{方法链条}}

{chain_block}

\\newpage

\\section{{课堂题目与讲法}}

{examples_block}

\\section{{学生常见问题}}

{student_issues_section}

\\section{{课后落实}}

\\teachblock{{重做安排}}{{%
从本节课题目中选 2--3 道作为课后重做，每道写清重做目的。
}}

\\teachblock{{画像更新}}{{%
如果本节课发现稳定问题，课后更新 \\texttt{{profile.md}}。
}}

\\end{{document}}
"""


def _gen_schedule(spec: dict) -> str:
    """根据例题数量生成时间分配表。使用 \\midrule 兼容 booktabs。"""
    n = len(spec.get("examples", []))
    total = int(re.search(r"\d+", spec.get("duration", "120")).group()) if spec.get("duration") else 120

    # 基本分配：回顾 10min，引入 15min，每道例题分时间，总结 15min
    review = 10
    intro = 15
    summary = 15
    practice = 20
    remaining = total - review - intro - summary - practice
    per_example = max(remaining // max(n, 1), 10)

    rows = []
    t = 0
    rows.append(f"0--{review} 分钟 & 课前回顾 & 公式快速检测，确认学生掌握情况。\\\\ \\midrule")
    t = review
    rows.append(f"{t}--{t+intro} 分钟 & 专题引入 & 梳理方法链条，明确本讲核心。\\\\ \\midrule")
    t += intro
    for i, ex in enumerate(spec.get("examples", []), 1):
        end = t + per_example
        rows.append(f"{t}--{end} 分钟 & 例题 {i}（{ex['role']}）& 讲解 {ex['desc']}。\\\\ \\midrule")
        t = end
    rows.append(f"{t}--{t+practice} 分钟 & 巩固练习 & 学生独立练习，教师巡视点拨。\\\\ \\midrule")
    t += practice
    rows.append(f"{t}--{total} 分钟 & 总结 & 方法链条复盘，布置课后重做。\\\\")
    return "\n".join(rows) + "\n"


def _teacher_example(ex: dict) -> str:
    """生成单道例题的教案区块。"""
    num = ex["num"]
    role = ex["role"]
    desc = ex["desc"]
    return f"""\\teacherproblem{{例题 {num}}}{{{role}: {desc}}}

{{\\small 待填入题干}}

\\begin{{paracol}}{{2}}
\\teachblock{{标准解答}}{{%
本处填写标准解答和多解法。
}}

\\switchcolumn
\\teachblock{{学生问题分析}}{{%
根据学情预判学生可能遇到的问题。
}}

\\teachblock{{课堂追问}}{{%
设计 1--2 个追问，帮助学生突破思维卡点。
}}
\\end{{paracol}}

"""


def _format_chain(chain: str) -> str:
    """将方法链条文本转为 LaTeX itemize。"""
    if not chain:
        return "\\textit{待补充方法链条}\n"
    items = []
    for line in chain.splitlines():
        line = line.strip()
        if line and not line.startswith("```"):
            items.append(f"  \\item {line}")
    if items:
        return "\\begin{itemize}[itemsep=0.2em]\n" + "\n".join(items) + "\n\\end{itemize}\n"
    return "\\textit{待补充方法链条}\n"


# ── 编译 ────────────────────────────────────────────────
def compile_pdf(topic_dir: Path, filename: str) -> bool:
    """编译单个 .tex 文件为 PDF。"""
    tex_file = topic_dir / f"{filename}.tex"
    if not tex_file.exists():
        print(f"  [跳过] {tex_file} 不存在")
        return False
    print(f"  [编译] {filename}.tex ...")
    result = subprocess.run(
        ["xelatex", "-interaction=nonstopmode", "-halt-on-error", filename + ".tex"],
        cwd=str(topic_dir),
        capture_output=True,
        text=True,
        timeout=120,
    )
    if result.returncode == 0:
        print(f"  [完成] {filename}.pdf")
        return True
    else:
        # 提取关键错误信息
        for line in result.stdout.splitlines():
            if line.startswith("!"):
                print(f"  [错误] {line}")
                break
        return False


# ── 主流程 ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="从 topic_spec.md 生成专题课骨架")
    parser.add_argument("topic_dir", help="专题目录路径，如 common/topics/解三角形_边角互化")
    parser.add_argument("--compile", action="store_true", help="生成后立即编译 PDF")
    parser.add_argument("--force", action="store_true", help="覆盖已有文件")
    args = parser.parse_args()

    topic_dir = ROOT / args.topic_dir
    spec_path = topic_dir / "topic_spec.md"

    if not spec_path.exists():
        print(f"[错误] 找不到 {spec_path}")
        sys.exit(1)

    print(f"[解析] {spec_path}")
    spec = parse_spec(spec_path)

    # 计算 ipara.sty 的相对路径
    depth = len(topic_dir.relative_to(ROOT).parts)
    rel_ipara = "/".join([".."] * depth) + "/common/ipara"

    # 生成 questions.tex
    q_path = topic_dir / "questions.tex"
    if q_path.exists() and not args.force:
        print(f"  [跳过] questions.tex 已存在（使用 --force 覆盖）")
    else:
        q_path.write_text(gen_questions(spec), encoding="utf-8")
        print(f"  [写入] questions.tex")

    # 生成学案.tex
    s_path = topic_dir / "学案.tex"
    if s_path.exists() and not args.force:
        print(f"  [跳过] 学案.tex 已存在（使用 --force 覆盖）")
    else:
        s_path.write_text(gen_student(spec, rel_ipara), encoding="utf-8")
        print(f"  [写入] 学案.tex")

    # 生成教案.tex
    t_path = topic_dir / "教案.tex"
    if t_path.exists() and not args.force:
        print(f"  [跳过] 教案.tex 已存在（使用 --force 覆盖）")
    else:
        t_path.write_text(gen_teacher(spec, rel_ipara), encoding="utf-8")
        print(f"  [写入] 教案.tex")

    print(f"\n[完成] 骨架文件已生成到 {topic_dir}")
    print(f"  下一步:")
    print(f"  1. 编辑 questions.tex，填入 pool 中的题目路径")
    print(f"  2. 编辑 教案.tex，补入标准解答和课堂处理")
    print(f"  3. 编辑 学案.tex，调整公式默写区和思考题")

    if args.compile:
        print(f"\n[编译]")
        compile_pdf(topic_dir, "学案")
        compile_pdf(topic_dir, "教案")


if __name__ == "__main__":
    main()