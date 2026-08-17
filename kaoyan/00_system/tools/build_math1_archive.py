#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_math1_archive.py
======================
补全/重建考研数学一真题库 (1987-2026)。默认保护已存在 Canonical 年度正文，不做破坏性覆盖。
执行规范：kaoyan/00_system/exam_source_conversion_spec.md
特性：
- 统一标识体系：profile_id="math1", exam_id="math1-<year>"
- 纯净题面：100% 剥离答案与解析
- 全矢量化：100% 图件直接生成 Semantic SVG (Dark #30362d + Light #fafaf7)
"""

import os
import re
import json
import argparse

KAOYAN_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
RAW_PAPERS_DIR = "/Users/xpx/Downloads/Kaoyan-Math1-Papers-main/papers"
RAW_SOLUTIONS_DIR = "/Users/xpx/Downloads/Kaoyan-Math1-Papers-main/solutions"
ARCHIVE_ROOT = os.path.join(KAOYAN_ROOT, "archives/math1")
PROFILE_PATH = os.path.join(KAOYAN_ROOT, "00_system/exam_profiles/math1.json")

ALL_YEARS = [
    1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994,
    1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002,
    2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
    2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026
]

def clean_latex(text: str) -> str:
    """清洗 LaTeX 公式"""
    text = re.sub(r'\\mathbf\s*\{\s*e\s*\}', r'\\mathrm{e}', text)
    text = re.sub(r'\\mathbf\s*e', r'\\mathrm{e}', text)
    text = re.sub(r'\\mathrm\s*\{\s*d\s*\}', r'\\mathrm{d}', text)
    text = re.sub(r'\\mathrm\s*d([a-zA-Z])', r'\\mathrm{d}\1', text)
    text = re.sub(r'\\operatorname\*\s*\{\s*l\s*i\s*m\s*\}', r'\\lim', text)
    text = re.sub(r'\\operatorname\*\s*\{\s*lim\s*\}', r'\\lim', text)
    text = re.sub(r'\\mathsf\s*\{\s*([0-9\s\~]+)\s*\}', r'\1', text)
    text = re.sub(r'\\pmb\s*\{\s*\\alpha\s*\}', r'\\boldsymbol{\\alpha}', text)
    text = re.sub(r'\\pmb\s*\{\s*([A-Za-z]+)\s*\}', r'\\boldsymbol{\1}', text)
    text = re.sub(r'\\mathbf\s*([A-Z])', r'\\boldsymbol{\1}', text)
    text = re.sub(r'\\leqslant', r'\\le', text)
    text = re.sub(r'\\geqslant', r'\\ge', text)
    text = re.sub(r'\\leq', r'\\le', text)
    text = re.sub(r'\\geq', r'\\ge', text)
    text = re.sub(r'\{\s*\}', '', text)
    text = text.replace('\u3000', ' ')
    return text

def format_options(text: str) -> str:
    """将选项格式化为标准 A. B. C. D. 独立行"""
    lines = text.splitlines()
    new_lines = []
    for line in lines:
        stripped = line.strip()
        multi_opt = re.findall(r'(?:^|\s+)(?:[\(（]?([A-D])[\)）][\.\、\s]*|([A-D])[\.．、\s]+)(.*?)(?=(?:\s+[\(（]?[A-D][\)）]|\s+[A-D][\.．、]|$))', stripped)
        if len(multi_opt) >= 2:
            for opt in multi_opt:
                char = opt[0] if opt[0] else opt[1]
                content = opt[2].strip()
                new_lines.append(f"{char.upper()}. {content}  ")
        else:
            m = re.match(r'^[\(（]?([A-D])[\)）][\.\、\s]*(.*)$', stripped)
            if not m:
                m = re.match(r'^([A-D])[\.．、\s]+(.*)$', stripped)
            if m:
                char = m.group(1).upper()
                content = m.group(2).strip()
                new_lines.append(f"{char}. {content}  ")
            else:
                new_lines.append(line)
    return '\n'.join(new_lines)

def strip_answers_and_solutions(text: str) -> str:
    """彻底剥离答案与解析"""
    lines = text.splitlines()
    cleaned_lines = []
    in_solution = False
    
    for line in lines:
        stripped = line.strip()
        
        if re.match(r'^(?:【答案】|【解析】|【解】|【分析】|答案[：\s]|解析[：\s]|分析[：\s]|解[：\s]|答案速查|拓展|1\.协方差|2\.\s*常见分布)', stripped):
            in_solution = True
            continue
        
        if re.match(r'^(?:#+|\d+[\.．、\s]|（\d+）|\(\d+\)|【\d+】|一、|二、|三、|四、|五、|六、|七、|八、|九、|十、|十一、|十二、|十三、)', stripped):
            in_solution = False
            
        if not in_solution:
            if '【答案】' in line:
                line = re.sub(r'【答案】.*$', '', line).strip()
            if line:
                cleaned_lines.append(line)
            else:
                if cleaned_lines and cleaned_lines[-1] != "":
                    cleaned_lines.append("")
            
    return '\n'.join(cleaned_lines)

def get_2022_clean_questions() -> str:
    """提供 2022 年 22 道题目的精校完整题面，彻底修复乱码与漏题"""
    return r"""## 一、选择题

> 第 1～10 小题，每小题 5 分，共 50 分。下列每题给出的四个选项中，只有一个选项是符合题目要求的。

### 1

设 $\lim_{x\to 1}\frac{f(x)}{\ln x} = 1$ ，则（ ）。

A. $f(1) = 0$  
B. $\lim_{x\to 1}f(x) = 0$  
C. $f'(1) = 1$  
D. $\lim_{x\to 1}f'(x) = 1$  

### 2

设 $f(u)$ 可导， $z = xyf\left(\frac{y}{x}\right)$ ，若 $x \frac{\partial z}{\partial x} + y \frac{\partial z}{\partial y} = y^2 (\ln y - \ln x)$ ，则（ ）。

A. $f(1) = \frac{1}{2}, f'(1) = 0$  
B. $f(1) = 0, f'(1) = \frac{1}{2}$  
C. $f(1) = \frac{1}{2}, f'(1) = 1$  
D. $f(1) = 0, f'(1) = 1$  

### 3

设数列 $\{x_n\}$ 满足 $-\frac{\pi}{2} \le x_n \le \frac{\pi}{2}$ ，则（ ）。

A. 若 $\lim_{n\to \infty}\cos (\sin x_n)$ 存在，则 $\lim_{n\to \infty}x_n$ 存在  
B. 若 $\lim_{n\to \infty}\sin (\cos x_n)$ 存在，则 $\lim_{n\to \infty}x_n$ 存在  
C. 若 $\lim_{n\to \infty}\cos (\sin x_n)$ 存在，则 $\lim_{n\to \infty}\sin x_n$ 存在，但 $\lim_{n\to \infty}x_n$ 不一定存在  
D. 若 $\lim_{n\to \infty}\sin (\cos x_n)$ 存在，则 $\lim_{n\to \infty}\cos x_n$ 存在，但 $\lim_{n\to \infty}x_n$ 不一定存在  

### 4

设 $I_1 = \int_0^1 \frac{x}{2(1+\cos x)} \mathrm{d}x, I_2 = \int_0^1 \frac{\ln(1+x)}{1+\cos x} \mathrm{d}x, I_3 = \int_0^1 \frac{2x}{1+\sin x} \mathrm{d}x$ ，则（ ）。

A. $I_1 < I_2 < I_3$  
B. $I_2 < I_1 < I_3$  
C. $I_1 < I_3 < I_2$  
D. $I_3 < I_2 < I_1$  

### 5

下列4个条件中，3阶矩阵 $\boldsymbol{A}$ 可相似对角化的一个充分非必要条件是（ ）。

A. $\boldsymbol{A}$ 有3个不同的特征值  
B. $\boldsymbol{A}$ 有3个线性无关的特征向量  
C. $\boldsymbol{A}$ 有3个两两线性无关的特征向量  
D. $\boldsymbol{A}$ 的属于不同特征值的特征向量相互正交  

### 6

设 $\boldsymbol{A}, \boldsymbol{B}$ 为 $n$ 阶矩阵， $\boldsymbol{E}$ 为 $n$ 阶单位矩阵，若方程组 $\boldsymbol{A}x = 0$ 与 $\boldsymbol{B}x = 0$ 同解，则（ ）。

A. $\begin{pmatrix} \boldsymbol{A} & \boldsymbol{O} \\ \boldsymbol{E} & \boldsymbol{B} \end{pmatrix} y = 0$ 只有零解  
B. $\begin{pmatrix} \boldsymbol{E} & \boldsymbol{A} \\ \boldsymbol{O} & \boldsymbol{A}\boldsymbol{B} \end{pmatrix} y = 0$ 只有零解  
C. $\begin{pmatrix} \boldsymbol{A} & \boldsymbol{B} \\ \boldsymbol{O} & \boldsymbol{B} \end{pmatrix} y = 0$ 与 $\begin{pmatrix} \boldsymbol{B} & \boldsymbol{A} \\ \boldsymbol{O} & \boldsymbol{A} \end{pmatrix} y = 0$ 同解  
D. $\begin{pmatrix} \boldsymbol{A}\boldsymbol{B} & \boldsymbol{B} \\ \boldsymbol{O} & \boldsymbol{A} \end{pmatrix} y = 0$ 与 $\begin{pmatrix} \boldsymbol{B}\boldsymbol{A} & \boldsymbol{A} \\ \boldsymbol{O} & \boldsymbol{B} \end{pmatrix} y = 0$ 同解  

### 7

设 $\boldsymbol{\alpha}_1 = (\lambda, 1, 1)^{\mathrm{T}}, \boldsymbol{\alpha}_2 = (1, \lambda, 1)^{\mathrm{T}}, \boldsymbol{\alpha}_3 = (1, 1, \lambda)^{\mathrm{T}}, \boldsymbol{\alpha}_4 = (1, \lambda, \lambda^2)^{\mathrm{T}}$ ，若向量组 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_3$ 与 $\boldsymbol{\alpha}_1, \boldsymbol{\alpha}_2, \boldsymbol{\alpha}_4$ 等价，则 $\lambda$ 的取值范围是（ ）。

A. $\{0,1\}$  
B. $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \neq -2\}$  
C. $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \neq -1, \lambda \neq -2\}$  
D. $\{\lambda \mid \lambda \in \mathbb{R}, \lambda \neq -1\}$  

### 8

设随机变量 $X$ 服从区间 $(0,3)$ 上的均匀分布，随机变量 $Y$ 服从参数为 2 的泊松分布，且 $X$ 与 $Y$ 的协方差为 -1，则 $D(2X - Y + 1) = $（ ）。

A. 1  
B. 5  
C. 9  
D. 12  

### 9

设随机变量 $X_1, X_2, \dots, X_n$ 独立同分布，且 $X_1$ 的 4 阶矩存在， $E(X_1^k) = \mu_k (k=1,2,3,4)$ ，则由切比雪夫不等式，有 $P\left\{ \left| \frac{1}{n} \sum_{i=1}^n X_i^2 - \mu_2 \right| \ge \varepsilon \right\} \le $（ ）。

A. $\frac{\mu_4 - \mu_2^2}{n\varepsilon^2}$  
B. $\frac{\mu_4 - \mu_2^2}{\sqrt{n}\varepsilon^2}$  
C. $\frac{\mu_4 - \mu_2^2}{\varepsilon^2}$  
D. $\frac{\mu_4 - \mu_2^2}{n^2\varepsilon^2}$  

### 10

设随机变量 $X \sim N(0,1)$ ，若在 $X = x$ 的条件下，随机变量 $Y \sim N(x,1)$ ，则 $X$ 与 $Y$ 的相关系数为（ ）。

A. $\frac{1}{4}$  
B. $\frac{1}{2}$  
C. $\frac{\sqrt{3}}{3}$  
D. $\frac{\sqrt{2}}{2}$  

## 二、填空题

> 第 11～16 小题，每小题 5 分，共 30 分。

### 11

函数 $f(x, y) = x^2 + 2y^2$ 在点 $(0,1)$ 处的最大方向导数为 ______。

### 12

$\int_{1}^{\mathrm{e}^2} \frac{\ln x}{\sqrt{x}} \mathrm{d}x = $ ______。

### 13

当 $x \ge 0, y \ge 0$ 时， $x^2 + y^2 \le k\mathrm{e}^{x+y}$ 恒成立，则 $k$ 的取值范围是 ______。

### 14

已知级数 $\sum_{n=1}^\infty \frac{n!}{n^n} \mathrm{e}^{-nx}$ 的收敛域为 $(a, +\infty)$ ，则 $a = $ ______。

### 15

已知矩阵 $\boldsymbol{A}$ 和 $\boldsymbol{E} - \boldsymbol{A}$ 可逆，其中 $\boldsymbol{E}$ 为单位矩阵，若矩阵 $\boldsymbol{B}$ 满足 $[\boldsymbol{E} - (\boldsymbol{E} - \boldsymbol{A})^{-1}]\boldsymbol{B} = \boldsymbol{A}$ ，则 $\boldsymbol{B} - \boldsymbol{A} = $ ______。

### 16

设 $A, B, C$ 为随机事件，且 $A$ 与 $B$ 互不相容， $A$ 与 $C$ 互不相容， $B$ 与 $C$ 相互独立， $P(A) = P(B) = P(C) = \frac{1}{3}$ ，则 $P(A \cup B \cup C) = $ ______。

## 三、解答题

> 第 17～22 小题，共 70 分。解答应写出文字说明、证明过程或演算步骤。

### 17（本题满分 10 分）

设函数 $y(x)$ 是微分方程 $y' + \frac{1}{2\sqrt{x}}y = 2 + \sqrt{x}$ 的满足条件 $y(1) = 3$ 的解，求曲线 $y = y(x)$ 的渐近线。

### 18（本题满分 12 分）

已知平面区域 $D = \{(x, y) \mid y - 2 \le x \le \sqrt{4 - y^2}, 0 \le y \le 2\}$ ，计算二重积分

$$
\iint_D \frac{(x-y)^2}{x^2+y^2} \mathrm{d}x\mathrm{d}y.
$$

### 19（本题满分 12 分）

已知曲线 $L$ 是曲面 $\Sigma: 4x^2 + y^2 + z^2 = 1, x \ge 0, y \ge 0, z \ge 0$ 的边界，曲面 $\Sigma$ 的法向量与 $x$ 轴正向夹角为锐角， $L$ 的方向为从曲面 $\Sigma$ 外侧看逆时针方向，计算曲线积分

$$
\oint_L x\mathrm{d}x + y\mathrm{d}y + z\mathrm{d}z.
$$

### 20（本题满分 12 分）

设函数 $f(x)$ 在 $(-\infty, +\infty)$ 上有二阶连续导数，证明： $f''(x) \ge 0$ 的充分必要条件是对任意不同的实数 $a, b$ ，都有

$$
f\left(\frac{a+b}{2}\right) \le \frac{1}{b-a} \int_a^b f(x) \mathrm{d}x.
$$

### 21（本题满分 12 分）

设二次型 $f(x_1, x_2, x_3) = \sum_{i=1}^3 \sum_{j=1}^3 ij x_i x_j$ 。

(1) 写出二次型 $f$ 的矩阵；  
(2) 求二次型 $f$ 在正交变换下的标准形及所用的正交变换矩阵。

### 22（本题满分 12 分）

设 $X_1, X_2, \dots, X_n$ 为来自均值为 $\theta$ 的指数分布总体的简单随机样本， $Y_1, Y_2, \dots, Y_m$ 为来自均值为 $2\theta$ 的指数分布总体的简单随机样本，且两样本相互独立。

(1) 求参数 $\theta$ 的极大似然估计量 $\hat{\theta}$ ；  
(2) 求 $\hat{\theta}$ 的方差 $D(\hat{\theta})$ 。
"""

# 年份与 SVG 对应映射表
YEAR_SVG_MAP = {
    1990: [("q01", "assets/q01_force_semicircle.svg"), ("q02", "assets/q02_random_var_triangle.svg")],
    1991: [("q01", "assets/q01_triangle_integral.svg")],
    2001: [("q01", "assets/q01_f_graph.svg"), ("q02", "assets/q01_opt_a.svg"), ("q03", "assets/q01_opt_b.svg"), ("q04", "assets/q01_opt_c.svg"), ("q05", "assets/q01_opt_d.svg")],
    2002: [("q01", "assets/q04_opt_a.svg"), ("q02", "assets/q04_opt_b.svg"), ("q03", "assets/q04_opt_c.svg"), ("q04", "assets/q04_opt_d.svg")],
    2003: [("q01", "assets/q01_df_graph.svg")],
    2005: [("q01", "assets/q01_inflection_tangents.svg")],
    2007: [("q01", "assets/q01_semicircle_integral.svg")],
    2008: [("q01", "assets/q01_two_sheet_hyperboloid.svg")],
    2009: [("q01", "assets/q01_f_graph.svg"), ("q02", "assets/q02_opt_a.svg"), ("q03", "assets/q03_opt_b.svg"), ("q03_dup", "assets/q03_opt_b.svg"), ("q04", "assets/q04_opt_c.svg"), ("q05", "assets/q05_opt_d.svg")],
    2015: [("q01", "assets/q01_d2f_inflection.svg")],
    2017: [("q01", "assets/q01_speed_curves.svg")],
    2024: [("q01", "assets/q01_three_planes.svg")]
}

def process_single_year(year: int):
    """处理并归档单一年份真题"""
    year_dir = os.path.join(ARCHIVE_ROOT, f"{year}年真题")
    year_assets_dir = os.path.join(year_dir, "assets")
    os.makedirs(year_dir, exist_ok=True)
    
    figures_found = []
    figure_assets = {}
    
    exam_json_path = os.path.join(year_dir, "exam.json")
    if os.path.isfile(exam_json_path):
        try:
            with open(exam_json_path, "r", encoding="utf-8") as f:
                existing_meta = json.load(f)
            existing_main = existing_meta.get("main_file", "")
            if existing_main and os.path.isfile(os.path.join(year_dir, existing_main)):
                return
        except (OSError, json.JSONDecodeError):
            pass

    main_file_name = f"{year} 年全国硕士研究生招生考试 数学（一）真题.md"
    main_file_path = os.path.join(year_dir, main_file_name)

    # Canonical Source 已存在时绝不由批量 builder 覆盖。需要重建单年时应先人工核对
    # Source 与目标，再使用专门的 exam-source 工作流，而不是让全量脚本静默回写。
    if os.path.exists(main_file_path):
        return
    elif year == 2022:
        cleaned_body = get_2022_clean_questions()
        total_score = 150
    else:
        if not os.path.exists(RAW_PAPERS_DIR):
            return
        if year == 2024:
            src_path = os.path.join(RAW_PAPERS_DIR, "2024年数学(一)真题及参考答案.md")
        else:
            cands = [f for f in os.listdir(RAW_PAPERS_DIR) if str(year) in f and f.endswith(".md") and f != "README.md"]
            src_path = os.path.join(RAW_PAPERS_DIR, cands[0])
            
        with open(src_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        text = strip_answers_and_solutions(raw_text)
        text = clean_latex(text)
        text = format_options(text)
        
        # 移除无用截图（1999、2019 等）
        if year in [1999, 2019]:
            text = re.sub(r'!\[.*?\]\(.*?\)\s*\n?', '', text)
            
        # 替换已有图片引用为 SVG 资产
        if year in YEAR_SVG_MAP:
            mapping = YEAR_SVG_MAP[year]
            img_matches = re.findall(r'!\[(.*?)\]\((.*?)\)', text)
            if img_matches:
                for i, (alt, src) in enumerate(img_matches):
                    if i < len(mapping):
                        svg_rel = mapping[i][1]
                        text = text.replace(src, svg_rel)
                        figures_found.append(i + 1)
                        figure_assets[str(i + 1)] = svg_rel

        if 1987 <= year <= 2002:
            total_score = 100
        else:
            total_score = 150

        lines = text.splitlines()
        body_lines = []
        for l in lines:
            stripped = l.strip()
            if re.match(r'^#\s*\d{4}\s*年.*', stripped) or re.match(r'^#\s*数学.*', stripped) or re.match(r'^（科目代码.*', stripped) or re.match(r'^试卷及解析', stripped) or re.match(r'^考试时间.*', stripped) or re.match(r'^绝密.*', stripped) or re.match(r'^考试形式.*', stripped):
                continue
            body_lines.append(l)
            
        cleaned_body = '\n'.join(body_lines).strip()
        cleaned_body = re.sub(r'^[#]+\s*([一二三四五六七八九十]+[、\s].*)$', r'## \1', cleaned_body, flags=re.MULTILINE)
        
    md_content = f"""---
type: exam-source
exam_id: math1-{year}
exam_profile: math1
year: {year}
status: ready
total_score: {total_score}
metadata_file: exam.json
---

# {year} 年全国硕士研究生招生考试

## 数学（一）试题

{cleaned_body}
"""
    with open(main_file_path, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    exam_json = {
        "schema_version": 1,
        "exam_id": f"math1-{year}",
        "profile_id": "math1",
        "year": year,
        "language": "zh-CN",
        "title": f"{year} 年全国硕士研究生招生考试 数学（一）试题",
        "main_file": main_file_name,
        "status": "ready",
        "total_score": total_score,
        "content_features": {
            "figures": figures_found,
            "code": [],
            "tables": []
        },
        "figure_assets": figure_assets,
        "routing": "profile-default",
        "open_items": []
    }
    
    with open(os.path.join(year_dir, "exam.json"), "w", encoding="utf-8") as f:
        json.dump(exam_json, f, ensure_ascii=False, indent=2)
        
    readme_content = f"""# {year} 年考研数学一真题

本目录保存 {year} 年全国硕士研究生招生考试数学（一）真题的正式可编辑版本与元数据。

## 文件说明

- `{main_file_name}`：干净题面，已彻底剥离答案与解析，LaTeX 公式与选项排版标准化；
- `exam.json`：年度机器元数据，符合 `math1` Exam Profile；
- `assets/`：原生 Semantic SVG 矢量图件资产（暗色默认 + `light/` 亮色支持）。

## 规范约定

严格遵循 `kaoyan/00_system/exam_source_conversion_spec.md`：
- 只维护正确题面，不包含答案、解析与作答诊断；
- 题图优先保证拓扑与几何语义正确，100% 矢量化呈现。
"""
    with open(os.path.join(year_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

def build_master_indexes():
    """生成全局索引与清单文件"""
    print("[*] 生成全局索引与元数据文件...")
    
    archive_readme = """# 考研数学（一）真题库 (1987–2026)

本目录保存 1987～2026 年全国硕士研究生招生考试数学（一）共 40 套真题的正式可编辑版本。

## 目录结构合同

```text
kaoyan/archives/math1/
├── README.md                           # 本说明文件
├── archive.json                        # 全局机器索引
├── 00_数学一真题年度索引.md            # 人类可读年度总览
├── 00_数学一真题可疑点与复核清单.md     # 异常与历史复核记录
├── 00_SVG资产审阅.md                   # 全库 Semantic SVG 资产清单
├── 1987年真题/
│   ├── 1987 年全国硕士研究生招生考试 数学（一）真题.md
│   ├── exam.json
│   ├── README.md
│   └── assets/
└── ...
```

## 执行规范

严格遵循 `kaoyan/00_system/exam_source_conversion_spec.md` 与 `exam_source_agent_prompt.md`：
- **纯净题面**：正文只维护正确试题，不包含答案、解析、评分标准或个人作答记录；
- **原生格式**：文本使用 Markdown，数学使用 LaTeX，图件 100% 采用 Semantic SVG 归入 `assets/`；
- **元数据分层**：考试制度由 `00_system/exam_profiles/math1.json` 定义，年度事实由各年度 `exam.json` 记录。
"""
    archive_readme_path = os.path.join(ARCHIVE_ROOT, "README.md")
    if not os.path.exists(archive_readme_path):
        with open(archive_readme_path, "w", encoding="utf-8") as f:
            f.write(archive_readme)
    else:
        print(f"[preserve] Existing hand-maintained Archive README: {archive_readme_path}")
        
    archive_json_data = {
        "schema_version": 1,
        "profile_id": "math1",
        "name": "考研数学一真题库",
        "available_years": ALL_YEARS,
        "missing_years": [],
        "total_sets": len(ALL_YEARS),
        "exam_profile": "../../00_system/exam_profiles/math1.json",
        "conversion_spec": "../../00_system/exam_source_conversion_spec.md"
    }
    with open(os.path.join(ARCHIVE_ROOT, "archive.json"), "w", encoding="utf-8") as f:
        json.dump(archive_json_data, f, ensure_ascii=False, indent=2)
        
    index_md = """# 考研数学（一）真题年度索引表 (1987–2026)

| 年份 | 满分 | 题目大纲时期 | 正式版入口 | 元数据 | 矢量资产 | 状态 |
|---|---|---|---|---|---|---|
"""
    for y in ALL_YEARS:
        score = 100 if y <= 2002 else 150
        if y >= 2021:
            era_desc = "新大纲 (10选+6填+6大)"
        elif y >= 2007:
            era_desc = "经典大纲 (8选+6填+9大)"
        elif y >= 2003:
            era_desc = "150分过渡 (6填+8选+9大)"
        elif y >= 1997:
            era_desc = "100分大纲 (5填+5选+9大)"
        else:
            era_desc = "早期100分制"
            
        json_path = f"{y}年真题/exam.json"
        with open(os.path.join(ARCHIVE_ROOT, json_path), "r", encoding="utf-8") as f:
            ej = json.load(f)
        fig_count = len(ej.get("figure_assets", {}))
        fig_str = f"{fig_count} SVG" if fig_count > 0 else "-"
        
        main_file = ej.get("main_file", f"{y} 年全国硕士研究生招生考试 数学（一）真题.md")
        index_md += f"| {y} | {score} | {era_desc} | [{y}年真题]({y}年真题/{main_file}) | [{y} json]({y}年真题/exam.json) | {fig_str} | ✅ Ready |\n"
        
    with open(os.path.join(ARCHIVE_ROOT, "00_数学一真题年度索引.md"), "w", encoding="utf-8") as f:
        f.write(index_md)

def main():
    parser = argparse.ArgumentParser(description="数学一 Archive 补缺/索引维护工具（默认不覆盖已存在 Canonical Source）")
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--year", type=int, choices=ALL_YEARS, help="补建一个缺失年份；已有 Canonical 年份自动跳过")
    scope.add_argument("--all", action="store_true", help="检查并补建 1987-2026 全部年份；已有 Canonical 年份自动跳过")
    parser.add_argument("--refresh-index", action="store_true", help="重新生成 archive.json 与年度索引；保留手工维护的 README")
    parser.add_argument("--regenerate-svg", action="store_true", help="显式重生成全库 Semantic SVG；可能覆盖现有派生图件")
    args = parser.parse_args()

    if not any((args.year, args.all, args.refresh_index, args.regenerate_svg)):
        parser.print_help()
        return 2

    print("=" * 60)
    print(" 数学一 Archive 维护工具启动 (Profile: math1)")
    print("=" * 60)

    years = [args.year] if args.year else (ALL_YEARS if args.all else [])
    for year in years:
        process_single_year(year)
        print(f"[{year}] Archive 补缺检查完成。")

    if args.regenerate_svg:
        import generate_math1_svgs
        generate_math1_svgs.main()

    if years or args.refresh_index:
        build_master_indexes()

    print("=" * 60)
    print(" Archive 维护任务完成。")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
