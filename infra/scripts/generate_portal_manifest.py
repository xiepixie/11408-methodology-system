#!/usr/bin/env python3
"""Kaoyan Portal Manifest Generator.

Scans `kaoyan/90_publish/` and extracts structured metadata for the Web Delivery Portal.
Generates both `kaoyan/portal/data/manifest.json` and `manifest.js` (for direct file:// support).
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
KAOYAN_DIR = REPO_ROOT / "kaoyan"
PUBLISH_DIR = KAOYAN_DIR / "90_publish"
PORTAL_DIR = KAOYAN_DIR / "portal"
MANIFEST_PATH = PORTAL_DIR / "data" / "manifest.json"

SUBJECT_NAMES = {
    "math1": "数学一",
    "408": "408 计算机",
    "english1": "英语一",
    "system": "系统与控制",
    "interview": "复试准备",
}

SUBJECT_ORDER = ["math1", "408", "english1", "system", "interview"]

SUB_SUBJECT_ORDER = {
    "math1": [
        "高等数学",
        "线性代数",
        "概率论与数理统计",
        "数学一桥梁专题",
        "数学一做题规则",
    ],
    "408": [
        "408 综合与跨科",
        "数据结构",
        "计算机组成原理",
        "操作系统",
        "计算机网络",
    ],
    "english1": [
        "每日外刊精读",
        "高频学术表达库",
        "英语能力与输出",
        "英语统一方法论",
        "阅读理解",
        "英语写作",
        "英汉翻译",
        "完形与新题型",
    ],
    "system": [
        "解题控制核",
        "LaTeX 模板规范",
        "系统方法论",
    ],
}

TYPE_ORDER = {
    "Atlas": 0,        # 🗺️ 顶层总图与心智模型全景（最高优先级置顶）
    "Topic": 1,        # 📘 核心章节专题与基础推导
    "Bridge": 2,       # 🌉 跨科跨章桥梁与机制接口
    "Integration": 3,  # 🧩 端到端大综合手册
    "Control": 4,      # 📋 做题规则与考场控制
    "Drill": 5,        # 🛠️ 实战训练手册与母题
}

SUBJECT_COLORS = {
    "math1": "#2563eb",
    "408": "#0d9488",
    "english1": "#d97706",
    "system": "#7c3aed",
    "interview": "#e11d48",
}

MATH1_BRIDGE_MAP = {
    # Math 1 Cross-Subject Bridges (kaoyan/10_数学一/50_桥梁专题)
    "内积正交与投影": ("MATH-B00", "内积、正交与投影 · 高数空间几何 ↔ 线代向量空间", "数学一桥梁专题"),
    "局部线性化_微分与线性映射": ("MATH-B01", "局部线性化 · 高数微分 ↔ 线代线性映射", "数学一桥梁专题"),
    "Jacobian与行列式_坐标变换与局部体积缩放": ("MATH-B02", "Jacobian与行列式 · 多元微积分 ↔ 线代行列式", "数学一桥梁专题"),
    "Hessian与二次型_二阶局部形状与正定性": ("MATH-B03", "Hessian与二次型 · 多元二阶模型 ↔ 线代二次型", "数学一桥梁专题"),
    "梯度正交与Lagrange_约束极值与子空间几何": ("MATH-B04", "梯度正交与Lagrange · 约束极值 ↔ 子空间几何", "数学一桥梁专题"),
    "线性方程与线性微分方程_一点加Kernel": ("MATH-B05", "线性方程与线性微分方程 · 线代方程 ↔ 高数线性ODE", "数学一桥梁专题"),
    "PDF与CDF_局部概率密度与累积": ("MATH-B06A", "PDF与CDF · 高数FTC ↔ 概率分布", "数学一桥梁专题"),
    "期望联合概率与边缘化_概率的积分语言": ("MATH-B06B", "期望联合概率与边缘化 · 高数积分 ↔ 概率质量汇总", "数学一桥梁专题"),
    "随机变量变换与Jacobian_概率质量守恒": ("MATH-B07", "随机变量变换与Jacobian · 概率质量守恒", "数学一桥梁专题"),
    "Fourier与正交基_函数表示与正交投影": ("MATH-B08", "Fourier与正交基 · 函数展开 ↔ 正交坐标", "数学一桥梁专题"),
    
    # Higher Math Intra-Subject Bridges (kaoyan/10_数学一/10_高等数学/50_桥梁专题)
    "函数结构在运算中的传播": ("H-B01", "函数结构在运算中的传播 · 周期奇偶对称", "高等数学"),
    "局部模型与区间定理_中值点余项与误差控制": ("H-B02", "局部模型与区间定理 · 中值点余项与误差控制", "高等数学"),
    "微分与累积_基本定理及正则性边界": ("H-B03", "微分与累积 · 基本定理及正则性边界", "高等数学"),
    "连续无限累积与离散无限累积": ("H-B04", "连续无限累积与离散无限累积 · 积分判别法与Euler求和", "高等数学"),
    "有限Taylor模型与无限Taylor表示": ("H-B05", "有限Taylor模型与无限Taylor表示", "高等数学"),
}

MATH1_TOPICS = {
    "高等数学": [
        "微积分", "一元", "多元", "微分", "累积", "极限", "连续", "导数", "Taylor",
        "中值", "常微分方程", "级数", "Fourier", "正交基", "定向积分", "向量场",
        "空间对象", "高维累积", "区间定理", "局部线性化", "局部模型", "局部到整体"
    ],
    "线性代数": [
        "线性", "向量空间", "矩阵", "行列式", "特征结构", "对角化", "二次型",
        "秩", "子空间", "内积", "正交", "投影", "Hessian", "Jacobian", "Subject_Atlas"
    ],
    "概率论与数理统计": [
        "随机", "概率", "分布", "数字特征", "大数定律", "中心极限", "样本",
        "抽样", "参数估计", "假设检验", "PDF", "CDF", "Bayes", "联合分布"
    ],
}


def natural_sort_key(code_or_title: str) -> list[int | str]:
    """Splits string into alphanumeric tokens for natural sorting (e.g. DS02 before DS10)."""
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", code_or_title)]


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def infer_type_and_code(filename: str) -> tuple[str, str, str]:
    """Returns (type, code, clean_title)."""
    stem = Path(filename).stem
    code = ""
    clean_title = stem

    # 0. Check Math 1 Bridge map first
    if stem in MATH1_BRIDGE_MAP:
        code, clean_title, _ = MATH1_BRIDGE_MAP[stem]
        doc_type = "Bridge"
        return doc_type, code, clean_title

    # 1. Multi-code like OS-01_OS-02_... or OS-06_OS-07_...
    multi_code = re.match(r"^([A-Z0-9]+-\d{2})_([A-Z0-9]+-\d{2})_(.*)$", stem)
    # 2. Standard hyphen codes: CO-01, DS-A01, NET-B05, X-B01, OS-B1, OS-I02
    hyphen_code = re.match(r"^([A-Z0-9]+-[A-Z0-9]+)_(.*)$", stem)
    # 3. Direct alphanumeric code: DS01, DS12
    alpha_num_code = re.match(r"^(DS\d{2})_(.*)$", stem)

    if multi_code:
        code = f"{multi_code.group(1)}/{multi_code.group(2)}"
        clean_title = multi_code.group(3)
    elif hyphen_code:
        code = hyphen_code.group(1)
        clean_title = hyphen_code.group(2)
    elif alpha_num_code:
        code = alpha_num_code.group(1)
        clean_title = alpha_num_code.group(2)
    elif stem.startswith("OS_科内桥梁"):
        code = "OS-Bridge"
        clean_title = "科内桥梁与跨科接口"
    elif "408_Course_Atlas" in stem:
        code = "408-Atlas"
        clean_title = "408 课程全景总图 (Poster)"
    elif "408统一总图" in stem:
        code = "408-Atlas"
        clean_title = "408 统一总图心智模型"
    elif "408四科统一" in stem:
        code = "408-Core"
        clean_title = "408 四科统一方法论"
    elif "线性代数_Subject_Atlas" in stem:
        code = "LA-Atlas"
        clean_title = "线性代数 Subject Atlas"
    elif "数学一_高等数学_心智模型手册" in stem:
        code = "MATH-Atlas"
        clean_title = "高等数学统一心智模型总图 (高数 Atlas)"
    elif "数学一_线性代数_心智模型手册" in stem:
        code = "LA-Atlas"
        clean_title = "线性代数统一心智模型总图 (线代 Atlas)"
    elif "数学一_概率论与数理统计_心智模型手册" in stem:
        code = "PROB-Atlas"
        clean_title = "概率论与数理统计统一总图 (概率 Atlas)"
    elif "英语语言学习与考试_统一心智模型" in stem:
        code = "ENG-Atlas"
        clean_title = "英语统一心智模型总图 (英语 Atlas)"
    elif "英语语言学习与考试统一方法论" in stem:
        code = "ENG-Core"
        clean_title = "英语统一方法论 · 从语言系统到任务执行"

    # Infer Type
    if (
        "Atlas" in stem
        or "总图" in stem
        or "Poster" in stem
        or "心智模型手册" in stem
        or code.endswith("Atlas")
        or code.endswith("Core")
    ):
        doc_type = "Atlas"
    elif "桥梁" in stem or "-B" in code or code.startswith("X-B") or "Bridge" in code or code.startswith("MATH-B"):
        doc_type = "Bridge"
    elif "综合" in stem or "-I" in code:
        doc_type = "Integration"
    elif "做题" in stem or "控制" in stem or "规则" in stem:
        doc_type = "Control"
    else:
        doc_type = "Topic"

    # Clean title formatting
    clean_title = re.sub(r"_方法论手册.*$", "", clean_title)
    clean_title = re.sub(r"_桥梁手册.*$", "", clean_title)
    clean_title = re.sub(r"_综合手册.*$", "", clean_title)
    clean_title = re.sub(r"_心智模型手册.*$", "", clean_title)
    clean_title = re.sub(r"_v\d+$", "", clean_title)
    clean_title = clean_title.replace("_", " · ")

    return doc_type, code, clean_title


def infer_sub_subject(subject: str, filename: str, code: str) -> str:
    stem = Path(filename).stem
    if subject == "408":
        if code.startswith("DS") or "数据结构" in stem:
            return "数据结构"
        elif code.startswith("CO") or "组成原理" in stem or "Cache" in stem or "ISA" in stem or "主存" in stem:
            return "计算机组成原理"
        elif code.startswith("OS") or "操作系统" in stem:
            return "操作系统"
        elif code.startswith("NET") or "网络" in stem or "TCP" in stem or "IP" in stem:
            return "计算机网络"
        elif code.startswith("X-") or "四科统一" in stem or "跨科" in stem or "Course" in stem:
            return "408 综合与跨科"
        return "408 综合与跨科"

    elif subject == "math1":
        if stem in MATH1_BRIDGE_MAP:
            return MATH1_BRIDGE_MAP[stem][2]
        elif "50_桥梁专题" in stem or (code and code.startswith("MATH-B")):
            return "数学一桥梁专题"
        elif "线性代数" in stem or code.startswith("LA"):
            return "线性代数"
        elif "概率" in stem or "统计" in stem or code.startswith("PROB"):
            return "概率论与数理统计"
        elif "高等数学" in stem or "微积分" in stem or code.startswith("H"):
            return "高等数学"
        
        # Keyword matching
        for sub, keywords in MATH1_TOPICS.items():
            for kw in keywords:
                if kw in stem:
                    return sub
        return "高等数学"

    elif subject == "english1":
        if "写作" in stem:
            return "英语写作"
        elif "阅读" in stem:
            return "阅读理解"
        elif "翻译" in stem:
            return "英汉翻译"
        elif "完形" in stem or "新题型" in stem:
            return "完形与新题型"
        return "英语统一方法论"

    elif subject == "system":
        if "控制" in stem or "做题" in stem:
            return "解题控制核"
        elif "template" in stem:
            return "LaTeX 模板规范"
        return "系统方法论"

    return "其他"


def extract_tags(subject: str, sub_subject: str, doc_type: str, code: str, title: str) -> list[str]:
    tags = [SUBJECT_NAMES.get(subject, subject), sub_subject, doc_type]
    if code:
        tags.append(code)
    # Split title parts
    parts = re.split(r" · |_|与|到|及", title)
    for p in parts:
        p_clean = p.strip()
        if len(p_clean) >= 2 and p_clean not in tags:
            tags.append(p_clean)
    return tags[:8]


def scan_markdown_drills(pdf_items: list[dict]) -> list[dict]:
    drill_items = []
    
    # Map for resolving model_owner to existing PDF item ID
    pdf_lookup = {}
    for item in pdf_items:
        clean_key = re.sub(r"[_\s·\(\)（）v\d\-]+", "", item["title"]).lower()
        pdf_lookup[clean_key] = item["id"]
        pdf_lookup[item["full_name"].lower()] = item["id"]
        pdf_lookup[item["filename"].lower()] = item["id"]
        if item.get("code"):
            pdf_lookup[item["code"].lower()] = item["id"]

    search_dirs = [
        (KAOYAN_DIR / "10_数学一", "math1"),
        (KAOYAN_DIR / "20_英语一", "english1"),
        (KAOYAN_DIR / "30_408", "408"),
        (KAOYAN_DIR / "01_control", "system"),
    ]

    for base_dir, subject_key in search_dirs:
        if not base_dir.exists():
            continue
        for md_path in sorted(base_dir.rglob("*.md")):
            # Ignore non-training files and system directories
            path_str = md_path.as_posix()
            if any(skip in path_str for skip in [
                "/assets/", "/code/", "/tests/", "/tools/", "/skills/",
                "/00_system/", "/.venv/", "/tmp/", "README.md", "SOURCE_DIFF.md",
                "00_迁移与重构规划.md", "AGENTS.md"
            ]):
                continue

            try:
                content = md_path.read_text(encoding="utf-8")
            except Exception:
                continue

            # Extract title from H1 or filename
            h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
            title = h1_match.group(1).strip() if h1_match else md_path.stem

            # Extract Training Scope (> 训练定位: ...)
            scope_match = re.search(r">\s*(?:\[!TRAIN\]|\*?\*?训练定位\*?\*?)[：:]\s*([^\n\r]+)", content)
            training_scope = scope_match.group(1).strip() if scope_match else ""

            # Extract Model Owner (> 模型归属: ...)
            owner_match = re.search(r">\s*(?:\[!MODEL\]|\*?\*?模型归属\*?\*?)[：:]\s*([^\n\r]+)", content)
            model_owner = owner_match.group(1).strip() if owner_match else ""

            # Try to resolve model_owner to a PDF ID
            model_owner_id = None
            if model_owner:
                owner_clean = re.sub(r"[\[\]《》\(\)\.tex\.pdf_\s·\-]+", "", model_owner).lower()
                for k, v in pdf_lookup.items():
                    if k and (k in owner_clean or owner_clean in k):
                        model_owner_id = v
                        break

            # Infer sub_subject from relative directory hierarchy
            rel_to_kaoyan = md_path.relative_to(KAOYAN_DIR)
            parts = rel_to_kaoyan.parts
            sub_subject = "其他"
            if subject_key == "math1":
                if "50_桥梁专题" in path_str and "10_高等数学" not in path_str:
                    sub_subject = "数学一桥梁专题"
                elif "10_高等数学" in path_str:
                    sub_subject = "高等数学"
                elif "20_线性代数" in path_str:
                    sub_subject = "线性代数"
                elif "30_概率" in path_str:
                    sub_subject = "概率论与数理统计"
                elif "90_学科做题规则" in path_str:
                    sub_subject = "数学一做题规则"
            elif subject_key == "408":
                if "10_数据结构" in path_str:
                    sub_subject = "数据结构"
                elif "20_计算机组成原理" in path_str:
                    sub_subject = "计算机组成原理"
                elif "30_操作系统" in path_str:
                    sub_subject = "操作系统"
                elif "40_计算机网络" in path_str:
                    sub_subject = "计算机网络"
                elif "00_统一总图" in path_str or "跨科" in path_str:
                    sub_subject = "408 综合与跨科"
            elif subject_key == "english1":
                if "daily_reading/01_articles" in path_str:
                    sub_subject = "每日外刊精读"
                elif "daily_reading/02_expressions" in path_str:
                    sub_subject = "高频学术表达库"
                elif "daily_reading/03_capabilities" in path_str:
                    sub_subject = "英语能力与输出"
                elif "10_阅读" in path_str:
                    sub_subject = "阅读理解"
                elif "20_完形" in path_str:
                    sub_subject = "完形与新题型"
                elif "30_翻译" in path_str:
                    sub_subject = "英汉翻译"
                elif "40_写作" in path_str:
                    sub_subject = "英语写作"
                else:
                    sub_subject = "英语统一方法论"
            elif subject_key == "system":
                sub_subject = "解题控制核"

            # Derive clean code and id
            doc_id = f"drill_{subject_key}_{md_path.stem}"
            code = "DRILL"
            parent_name = md_path.parent.name
            
            if "daily_reading/01_articles" in path_str:
                date_match = re.search(r"(\d{4}-\d{2}-\d{2})", parent_name)
                date_str = date_match.group(1) if date_match else ""
                clean_date = date_str.replace("-", "")
                code = f"ENG-READ-{clean_date}" if clean_date else "ENG-READ"
                doc_id = f"drill_english1_reading_{parent_name}"
                source_match = re.search(r"^source:\s*([^\n\r]+)", content, re.MULTILINE)
                source_val = source_match.group(1).strip() if source_match else ""
                if source_val and date_str:
                    title = f"{title} · {source_val} ({date_str})"
                elif date_str:
                    title = f"{title} ({date_str})"
                if not training_scope:
                    fm_match = re.search(r"^---\n([\s\S]*?)\n---", content)
                    topics_str = "语篇精读与语块吸收"
                    if fm_match:
                        topics_match = re.findall(r"^\s*-\s*([^\n\r]+)", fm_match.group(1), re.MULTILINE)
                        if topics_match:
                            topics_str = " · ".join(topics_match)
                    training_scope = f"外刊语篇首读诊断、深读分析与高频表达沉淀（Topics: {topics_str}）"
            elif "daily_reading/02_expressions" in path_str:
                num_match = re.match(r"^(\d{2})_", md_path.stem)
                code = f"ENG-EXP-{num_match.group(1)}" if num_match else "ENG-EXP"
                doc_id = f"drill_english1_exp_{md_path.stem}"
                if not training_scope:
                    intro_match = re.search(r">\s*([^\n\r]+)", content)
                    if intro_match:
                        training_scope = intro_match.group(1).strip()
            elif "daily_reading/03_capabilities" in path_str:
                code = "ENG-CAP"
                doc_id = f"drill_english1_cap_{md_path.stem}"
            else:
                b_match = re.match(r"^(B\d{2}[A-Z]?)_", parent_name)
                hb_match = re.match(r"^(H-B\d{2})_", parent_name)
                num_match = re.match(r"^(\d{2})_", parent_name)
                if b_match:
                    code = f"MATH-{b_match.group(1)}-Drill"
                elif hb_match:
                    code = f"{hb_match.group(1)}-Drill"
                elif num_match:
                    if "高等数学" in sub_subject:
                        prefix = "H"
                    elif "线性代数" in sub_subject:
                        prefix = "LA"
                    elif "概率" in sub_subject:
                        prefix = "PR"
                    elif "数据结构" in sub_subject:
                        prefix = "DS"
                    elif "计算机组成原理" in sub_subject:
                        prefix = "CO"
                    elif "操作系统" in sub_subject:
                        prefix = "OS"
                    elif "计算机网络" in sub_subject:
                        prefix = "NET"
                    else:
                        prefix = "TR"
                    code = f"{prefix}{num_match.group(1)}-Drill"
                elif "50_科内桥梁" in path_str or "DS-B" in parent_name or "CO-B" in parent_name:
                    bridge_match = re.search(r"((?:DS|CO|OS|NET)-B\d{2})", parent_name)
                    if bridge_match:
                        code = f"{bridge_match.group(1)}-Drill"
                elif "60_综合专题" in path_str or "DS-I" in parent_name or "CO-I" in parent_name:
                    int_match = re.search(r"((?:DS|CO|OS|NET)-I\d{2})", parent_name)
                    if int_match:
                        code = f"{int_match.group(1)}-Drill"
                elif "70_算法扩展" in path_str or "DS-A" in parent_name:
                    alg_match = re.search(r"(DS-A\d{2})", parent_name)
                    if alg_match:
                        code = f"{alg_match.group(1)}-Drill"

            if not model_owner_id:
                # Fallback: try matching twin PDF by parent directory name
                clean_parent = re.sub(r"[_\s·\(\)（）v\d\-]+", "", parent_name).lower()
                for k, v in pdf_lookup.items():
                    if k and (k in clean_parent or clean_parent in k):
                        model_owner_id = v
                        break

            stat = md_path.stat()
            mtime_dt = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
            mtime_iso = mtime_dt.isoformat()
            mtime_formatted = mtime_dt.strftime("%Y-%m-%d")

            tags = extract_tags(subject_key, sub_subject, "训练", code, title)
            if "50_桥梁专题" in path_str or "科内桥梁" in path_str or "Bridge" in code or sub_subject == "数学一桥梁专题":
                if "桥梁" not in tags:
                    tags.append("桥梁")
                if "跨科桥梁" not in tags and "50_桥梁专题" in path_str:
                    tags.append("跨科桥梁")
            if "daily_reading/01_articles" in path_str:
                if "外刊精读" not in tags:
                    tags.append("外刊精读")
                if "Spotlight" not in tags and "Spotlight" in content:
                    tags.append("Spotlight")
            if "daily_reading/02_expressions" in path_str:
                if "表达库" not in tags:
                    tags.append("表达库")
            if "训练手册" not in tags:
                tags.append("训练手册")

            rel_web_url = f"../{rel_to_kaoyan.as_posix()}"
            local_rel_path = f"kaoyan/{rel_to_kaoyan.as_posix()}"

            drill_item = {
                "id": doc_id,
                "subject": subject_key,
                "subject_name": SUBJECT_NAMES.get(subject_key, subject_key),
                "sub_subject": sub_subject,
                "type": "Drill",
                "format": "markdown",
                "code": code,
                "title": title,
                "full_name": md_path.stem,
                "filename": md_path.name,
                "training_scope": training_scope,
                "model_owner": model_owner,
                "model_owner_id": model_owner_id,
                "url": rel_web_url,
                "local_path": local_rel_path,
                "size_bytes": stat.st_size,
                "size_human": format_size(stat.st_size),
                "modified_at": mtime_iso,
                "modified_date": mtime_formatted,
                "tags": tags[:8],
                "content": content,
            }
            drill_items.append(drill_item)

    return drill_items


def build_manifest() -> dict:
    pdf_items = []
    subject_counts: dict[str, int] = {k: 0 for k in SUBJECT_NAMES}
    type_counts: dict[str, int] = {
        "Atlas": 0,
        "Topic": 0,
        "Bridge": 0,
        "Integration": 0,
        "Control": 0,
        "Drill": 0,
    }
    format_counts: dict[str, int] = {
        "pdf": 0,
        "markdown": 0,
    }

    if not PUBLISH_DIR.exists():
        raise FileNotFoundError(f"Missing publish directory: {PUBLISH_DIR}")

    seen_filenames = set()
    sub_dirs = ["math1", "408", "english1", "system", "interview"]

    # Traverse subdirectories first
    pdf_paths: list[Path] = []
    for sub in sub_dirs:
        target_dir = PUBLISH_DIR / sub
        if target_dir.is_dir():
            for p in sorted(target_dir.rglob("*.pdf")):
                pdf_paths.append(p)
    
    # Also check root level if any unique PDF exists
    for p in sorted(PUBLISH_DIR.glob("*.pdf")):
        if p.name not in [x.name for x in pdf_paths]:
            pdf_paths.append(p)

    for pdf_path in pdf_paths:
        if pdf_path.name in seen_filenames:
            continue
        seen_filenames.add(pdf_path.name)

        rel_to_pub = pdf_path.relative_to(PUBLISH_DIR)
        parts = rel_to_pub.parts

        if len(parts) > 1:
            subject_key = parts[0]
        else:
            # Root level of 90_publish -> math1 or system
            subject_key = "math1"

        if subject_key not in SUBJECT_NAMES:
            subject_key = "math1"

        stat = pdf_path.stat()
        mtime_dt = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc)
        mtime_iso = mtime_dt.isoformat()
        mtime_formatted = mtime_dt.strftime("%Y-%m-%d")

        doc_type, code, clean_title = infer_type_and_code(pdf_path.name)
        sub_subject = infer_sub_subject(subject_key, pdf_path.name, code)
        tags = extract_tags(subject_key, sub_subject, doc_type, code, clean_title)

        subject_counts[subject_key] = subject_counts.get(subject_key, 0) + 1
        type_counts[doc_type] = type_counts.get(doc_type, 0) + 1
        format_counts["pdf"] += 1

        rel_web_url = f"../90_publish/{rel_to_pub.as_posix()}"
        local_rel_path = f"kaoyan/90_publish/{rel_to_pub.as_posix()}"

        item = {
            "id": f"{subject_key}_{pdf_path.stem}",
            "subject": subject_key,
            "subject_name": SUBJECT_NAMES.get(subject_key, subject_key),
            "sub_subject": sub_subject,
            "type": doc_type,
            "format": "pdf",
            "code": code,
            "title": clean_title,
            "full_name": pdf_path.stem,
            "filename": pdf_path.name,
            "url": rel_web_url,
            "local_path": local_rel_path,
            "size_bytes": stat.st_size,
            "size_human": format_size(stat.st_size),
            "modified_at": mtime_iso,
            "modified_date": mtime_formatted,
            "tags": tags,
        }
        pdf_items.append(item)

    # Scan Markdown Drills
    drill_items = scan_markdown_drills(pdf_items)
    for d in drill_items:
        sub_k = d["subject"]
        subject_counts[sub_k] = subject_counts.get(sub_k, 0) + 1
        type_counts["Drill"] = type_counts.get("Drill", 0) + 1
        format_counts["markdown"] += 1

    all_items = pdf_items + drill_items

    # Canonical Multi-tier Deterministic Sorting
    def get_sort_tuple(item: dict) -> tuple:
        sub_key = item["subject"]
        sub_idx = SUBJECT_ORDER.index(sub_key) if sub_key in SUBJECT_ORDER else 99
        
        sub_sub_list = SUB_SUBJECT_ORDER.get(sub_key, [])
        sub_sub_idx = sub_sub_list.index(item["sub_subject"]) if item["sub_subject"] in sub_sub_list else 99
        
        type_idx = TYPE_ORDER.get(item["type"], 99)
        
        # Natural alphanumeric sorting for code / title
        code_key = natural_sort_key(item["code"]) if item.get("code") else natural_sort_key(item["title"])
        title_key = item["title"]

        return (sub_idx, sub_sub_idx, type_idx, code_key, title_key)

    all_items.sort(key=get_sort_tuple)

    manifest = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_documents": len(all_items),
            "subject_counts": subject_counts,
            "type_counts": type_counts,
            "format_counts": format_counts,
        },
        "subjects": [
            {
                "id": k,
                "name": name,
                "color": SUBJECT_COLORS.get(k, "#2563eb"),
                "count": subject_counts.get(k, 0),
            }
            for k, name in SUBJECT_NAMES.items()
            if subject_counts.get(k, 0) > 0
        ],
        "documents": all_items,
    }

    return manifest


def main():
    PORTAL_DIR.mkdir(parents=True, exist_ok=True)
    data_dir = PORTAL_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    manifest = build_manifest()
    
    # 1. Output standard manifest.json
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # 2. Output manifest.js (window.__KAOYAN_MANIFEST__) for direct file:// protocol compatibility
    js_manifest_path = data_dir / "manifest.js"
    with open(js_manifest_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by generate_portal_manifest.py. Do not edit directly.\n")
        f.write("window.__KAOYAN_MANIFEST__ = ")
        json.dump(manifest, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"✅ Portal manifest successfully generated at:")
    print(f"   - JSON: {MANIFEST_PATH}")
    print(f"   - JS  : {js_manifest_path}")
    print(f"   Total Published Documents: {manifest['meta']['total_documents']}")
    for sub, count in manifest['meta']['subject_counts'].items():
        if count > 0:
            print(f"   - {SUBJECT_NAMES.get(sub, sub)}: {count} 篇")
    for t, count in manifest['meta']['type_counts'].items():
        if count > 0:
            print(f"   - [{t}]: {count} 篇")


if __name__ == "__main__":
    main()
