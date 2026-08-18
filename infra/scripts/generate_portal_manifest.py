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
        "英语统一方法论",
        "英语写作",
        "阅读理解",
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
}

SUBJECT_COLORS = {
    "math1": "#2563eb",
    "408": "#0d9488",
    "english1": "#d97706",
    "system": "#7c3aed",
    "interview": "#e11d48",
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
    elif "桥梁" in stem or "-B" in code or code.startswith("X-B") or "Bridge" in code:
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
        if "线性代数" in stem or code.startswith("LA"):
            return "线性代数"
        elif "概率" in stem or "统计" in stem:
            return "概率论与数理统计"
        elif "高等数学" in stem or "微积分" in stem:
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


def build_manifest() -> dict:
    items = []
    subject_counts: dict[str, int] = {k: 0 for k in SUBJECT_NAMES}
    type_counts: dict[str, int] = {
        "Atlas": 0,
        "Topic": 0,
        "Bridge": 0,
        "Integration": 0,
        "Control": 0,
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

        rel_web_url = f"../90_publish/{rel_to_pub.as_posix()}"
        local_rel_path = f"kaoyan/90_publish/{rel_to_pub.as_posix()}"

        item = {
            "id": f"{subject_key}_{pdf_path.stem}",
            "subject": subject_key,
            "subject_name": SUBJECT_NAMES.get(subject_key, subject_key),
            "sub_subject": sub_subject,
            "type": doc_type,
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
        items.append(item)

    # Canonical Multi-tier Deterministic Sorting
    def get_sort_tuple(item: dict) -> tuple:
        sub_key = item["subject"]
        sub_idx = SUBJECT_ORDER.index(sub_key) if sub_key in SUBJECT_ORDER else 99
        
        sub_sub_list = SUB_SUBJECT_ORDER.get(sub_key, [])
        sub_sub_idx = sub_sub_list.index(item["sub_subject"]) if item["sub_subject"] in sub_sub_list else 99
        
        type_idx = TYPE_ORDER.get(item["type"], 99)
        
        # Natural alphanumeric sorting for code / title
        code_key = natural_sort_key(item["code"]) if item["code"] else natural_sort_key(item["title"])
        title_key = item["title"]

        return (sub_idx, sub_sub_idx, type_idx, code_key, title_key)

    items.sort(key=get_sort_tuple)

    manifest = {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_documents": len(items),
            "subject_counts": subject_counts,
            "type_counts": type_counts,
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
        "documents": items,
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
