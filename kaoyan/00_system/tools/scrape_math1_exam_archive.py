#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=============================================================================
考研数学（一）历年真题高保真纯净一站式爬取与 Markdown 编译引擎 (Math1 Compiler)
=============================================================================
严格遵循: kaoyan/00_system/exam_source_conversion_spec.md
元数据依据: kaoyan/00_system/exam_profiles/math1.json
=============================================================================
"""

import os
import re
import ssl
import json
import time
import random
import argparse
import urllib.request
from html.parser import HTMLParser

DEFAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../archives/math1'))
PROFILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../exam_profiles/math1.json'))
BASE_URL = 'https://www.csgraduates.com/study_methods/math/math1'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.csgraduates.com/',
}

ssl_context = ssl.create_default_context()

# =============================================================================
# 1. 学科与题型路由（依据 math1.json）
# =============================================================================

def get_math1_metadata(year, q_num):
    """根据年份与题号获取题型、学科与默认分值"""
    if year >= 2021:
        # 2021~Present (22题)
        if 1 <= q_num <= 10:
            q_type = '单项选择题'
            score = 5
        elif 11 <= q_num <= 16:
            q_type = '填空题'
            score = 5
        else:
            q_type = '解答题'
            score = 10 if q_num <= 19 else 12

        if q_num in [1, 2, 3, 4, 11, 12, 13, 14, 17, 18, 19, 20]:
            subject = '高等数学'
        elif q_num in [5, 6, 15, 21]:
            subject = '线性代数'
        else:
            subject = '概率论与数理统计'
    elif 2008 <= year <= 2020:
        # 2008~2020 (23题)
        if 1 <= q_num <= 8:
            q_type = '单项选择题'
            score = 4
        elif 9 <= q_num <= 14:
            q_type = '填空题'
            score = 4
        else:
            q_type = '解答题'
            score = 10 if q_num in [15, 16, 17, 18, 19] else 11

        if q_num in [1, 2, 3, 4, 9, 10, 11, 12, 15, 16, 17, 18, 19]:
            subject = '高等数学'
        elif q_num in [5, 6, 13, 20, 21]:
            subject = '线性代数'
        else:
            subject = '概率论与数理统计'
    elif year == 2007:
        # 2007 (24题: 选择 10 + 填空 6 + 解答 8)
        if 1 <= q_num <= 10:
            q_type = '单项选择题'
            score = 4
        elif 11 <= q_num <= 16:
            q_type = '填空题'
            score = 4
        else:
            q_type = '解答题'
            score = 10 if q_num in [17, 20] else 11

        if q_num in [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 17, 18, 19, 20]:
            subject = '高等数学'
        elif q_num in [7, 8, 15, 21, 22]:
            subject = '线性代数'
        else:
            subject = '概率论与数理统计'
    elif 1991 <= year <= 2006:
        # 1991~2006：已逐年核对的历史结构。年度大题分值并不统一，不能用单一默认值覆盖。
        audited_scores = {
            1991: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 6, 8, 7, 8, 6, 8, 3, 3, 6],
            1992: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 6, 8, 7, 8, 7, 7, 3, 3, 6],
            1993: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 6, 7, 5, 5, 8, 6, 6, 3, 3, 6],
            1994: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 6, 9, 8, 6, 8, 6, 3, 3, 6],
            1995: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 6, 6, 7, 8, 8, 7, 6, 3, 3, 6],
            1996: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 6, 6, 7, 7, 8, 6, 8, 3, 3, 6],
            1997: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 6, 7, 6, 8, 5, 6, 5, 7, 5],
            1998: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6, 6, 7, 6, 5, 6, 6, 4, 5, 6, 4, 4],
            1999: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 6, 6, 6, 7, 7, 8, 6, 8, 6],
            2000: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 6, 7, 6, 7, 6, 6, 8, 8, 6],
            2001: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 6, 8, 7, 7, 8, 6, 8, 7, 7],
            2002: [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 7, 7, 8, 7, 7, 6, 8, 7, 7],
            2003: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 10, 12, 10, 10, 10, 10, 10, 10, 10, 10],
            2004: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 12, 11, 12, 11, 12, 9, 9, 9, 9],
            2005: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 11, 12, 11, 12, 12, 9, 9, 9, 9],
            2006: [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 10, 12, 12, 12, 12, 9, 9, 9, 9],
        }
        score_list = audited_scores[year]
        if not 1 <= q_num <= len(score_list):
            raise ValueError(f"{year} 年数学一不存在题号 Q{q_num:02d}")
        score = score_list[q_num - 1]

        if year == 1991:
            if q_num <= 5 or q_num in {20, 21}:
                q_type = '填空题'
            elif q_num <= 10:
                q_type = '单项选择题'
            else:
                q_type = '解答题'
        elif year == 1992:
            if q_num <= 5 or q_num in {20, 21}:
                q_type = '填空题'
            elif q_num <= 10:
                q_type = '单项选择题'
            else:
                q_type = '解答题'
        elif year == 1993:
            if q_num <= 5 or q_num in {21, 22}:
                q_type = '填空题'
            elif q_num <= 10:
                q_type = '单项选择题'
            else:
                q_type = '解答题'
        elif year in {1994, 1995, 1996}:
            if q_num <= 5 or q_num in {20, 21}:
                q_type = '填空题'
            elif q_num <= 10:
                q_type = '单项选择题'
            else:
                q_type = '解答题'
        elif year <= 2002:
            if q_num <= 5:
                q_type = '填空题'
            elif q_num <= 10:
                q_type = '单项选择题'
            else:
                q_type = '解答题'
        elif year == 2003:
            if q_num <= 6:
                q_type = '填空题'
            elif q_num <= 12:
                q_type = '单项选择题'
            else:
                q_type = '解答题'
        else:
            if q_num <= 6:
                q_type = '填空题'
            elif q_num <= 14:
                q_type = '单项选择题'
            else:
                q_type = '解答题'

        linear_algebra = {
            1991: {5, 10, 17, 18},
            1992: {5, 10, 18, 19},
            1993: {5, 10, 18, 19},
            1994: {5, 10, 18, 19},
            1995: {5, 10, 18, 19},
            1996: {5, 10, 18, 19},
            1997: {4, 9, 18, 19, 20},
            1998: {4, 9, 18, 19, 20},
            1999: {4, 9, 18, 19},
            2000: {4, 9, 18, 19},
            2001: {4, 9, 17, 18},
            2002: {4, 9, 17, 18},
            2003: {4, 10, 11, 19},
            2004: {5, 11, 12, 20, 21},
            2005: {5, 11, 12, 20, 21},
            2006: {5, 11, 12, 20, 21},
        }
        probability = {
            1991: {20, 21, 22},
            1992: {20, 21, 22},
            1993: {21, 22, 23},
            1994: {20, 21, 22},
            1995: {20, 21, 22},
            1996: {20, 21, 22},
            1997: {5, 10, 21, 22},
            1998: {5, 10, 21, 22, 23},
            1999: {5, 10, 20, 21},
            2000: {5, 10, 20, 21},
            2001: {5, 10, 19, 20},
            2002: {5, 10, 19, 20},
            2003: {5, 6, 12, 21, 22},
            2004: {6, 13, 14, 22, 23},
            2005: {6, 13, 14, 22, 23},
            2006: {6, 13, 14, 22, 23},
        }
        if q_num in linear_algebra[year]:
            subject = '线性代数'
        elif q_num in probability[year]:
            subject = '概率论与数理统计'
        else:
            subject = '高等数学'
    else:
        # 1987~1990 尚未完成逐年人工核定：fail closed，禁止静默写入猜测元数据。
        raise ValueError(
            f"{year} 年数学一历史题型/分值/学科路由尚未人工核定；"
            "请先校准年度 exam.json，再扩展 get_math1_metadata。"
        )

    return {
        'subject': subject,
        'type': q_type,
        'score': score
    }

# =============================================================================
# 2. KaTeX DOM 树节点解析与高精度 LaTeX 生成引擎
# =============================================================================

class Node:
    def __init__(self, tag, attrs=None):
        self.tag = tag.lower()
        self.attrs = dict(attrs or [])
        self.classes = self.attrs.get('class', '').split()
        self.style = self.attrs.get('style', '')
        self.children = []
        self.text = ""

    def add_child(self, child):
        self.children.append(child)

class KatexDOMBuilder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node('root')
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].add_child(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        if len(self.stack) > 1:
            self.stack.pop()

    def handle_data(self, data):
        data_clean = data.replace('\u200b', '').replace('\u00a0', ' ')
        if data_clean:
            self.stack[-1].text += data_clean

def has_class_recursive(node, class_name):
    if class_name in node.classes:
        return True
    for ch in node.children:
        if has_class_recursive(ch, class_name):
            return True
    return False

def find_first_vlist(node):
    for ch in node.children:
        if 'vlist' in ch.classes:
            return ch
        sub = find_first_vlist(ch)
        if sub:
            return sub
    return None

def find_node_recursive(node, class_name):
    if class_name in node.classes:
        return node
    for ch in node.children:
        found = find_node_recursive(ch, class_name)
        if found:
            return found
    return None

def render_katex_node(node):
    classes = node.classes
    tag = node.tag

    # 1. 忽略布局占位 strut、pstrut、vlist-s、frac-line 与 nulldelimiter
    if 'strut' in classes or 'pstrut' in classes or 'vlist-s' in classes or 'frac-line' in classes or 'nulldelimiter' in classes:
        return ""

    # 2. KaTeX vertical bar SVG 字符 (如条件概率 | 或 矩阵边界)
    if tag == 'svg':
        vb = node.attrs.get('viewbox', '')
        if '333' in vb or '1200' in vb or '2400' in vb:
            return " \\mid "
        return ""

    # 3. 极限 / 极值 / 求和 / 求积算符 op-limits (如 \lim_{x \to 0}, \sum_{i=1}^n)
    if 'op-limits' in classes:
        vlist = find_first_vlist(node)
        if vlist:
            direct_items = []
            for ch in vlist.children:
                if ch.style and 'top:' in ch.style:
                    top_m = re.search(r'top:\s*(-?[\d\.]+)em', ch.style)
                    top_val = float(top_m.group(1)) if top_m else 0.0
                    direct_items.append((top_val, ch))
            if len(direct_items) == 3:
                direct_items.sort(key=lambda x: x[0])
                sup_tex = render_katex_node(direct_items[0][1]).strip()
                op_tex = render_katex_node(direct_items[1][1]).strip()
                sub_tex = render_katex_node(direct_items[2][1]).strip()
                if not op_tex or op_tex in ['∑', 'sum']:
                    op_tex = "\\sum "
                elif op_tex in ['∏', 'prod']:
                    op_tex = "\\prod "
                return f"{op_tex}_{{{sub_tex}}}^{{{sup_tex}}}"
            elif len(direct_items) == 2:
                direct_items.sort(key=lambda x: x[0])
                t0 = render_katex_node(direct_items[0][1]).strip()
                t1 = render_katex_node(direct_items[1][1]).strip()
                if t0 in ['\\lim', '\\sum', '\\prod', '\\max', '\\min', '∑', 'lim', 'sum']:
                    if t0 in ['∑', 'sum']: t0 = "\\sum "
                    return f"{t0}_{{{t1}}}"
                elif t1 in ['\\lim', '\\sum', '\\prod', '\\max', '\\min', '∑', 'lim', 'sum']:
                    if t1 in ['∑', 'sum']: t1 = "\\sum "
                    return f"{t1}^{{{t0}}}"
                else:
                    return f"{t0}_{{{t1}}}"

    # 3.5 估计量 / 重音符号 accent (如 \hat{\theta}, \bar{X}, \tilde{X})
    # 3.5 估计量 / 重音符号 accent (如 \hat{\theta}, \bar{x}, \bar{y}, \bar{z}, \bar{X}, \tilde{X})
    if 'accent' in classes:
        vlist = find_first_vlist(node)
        if vlist:
            accent_node = None
            base_node = None
            for ch in vlist.children:
                if find_node_recursive(ch, 'accent-body') or 'accent-body' in ch.classes:
                    accent_node = ch
                else:
                    base_node = ch
            if accent_node and base_node:
                accent_tex = render_katex_node(accent_node).strip()
                base_tex = render_katex_node(base_node).strip()
                if '^' in accent_tex:
                    return f"\\hat{{{base_tex}}}"
                elif any(c in accent_tex for c in ['ˉ', '¯', '-', '\u02c9', '\u0304', '\u00af']):
                    return f"\\bar{{{base_tex}}}"
                elif '~' in accent_tex:
                    return f"\\tilde{{{base_tex}}}"
                elif '→' in accent_tex:
                    return f"\\vec{{{base_tex}}}"
                else:
                    return f"\\bar{{{base_tex}}}" if 'ˉ' in accent_tex else f"\\hat{{{base_tex}}}"

    # 4. minner 容器：分段函数 cases / 矩阵 pmatrix 处理
    if 'minner' in classes:
        mtable = find_node_recursive(node, 'mtable')
        if mtable:
            has_left_brace = False
            for ch in node.children:
                if 'mopen' in ch.classes:
                    txt = ch.text + "".join(gc.text for gc in ch.children)
                    if '{' in txt:
                        has_left_brace = True
                        break
            env_name = "cases" if has_left_brace else "pmatrix"

            cols = [c for c in mtable.children if any('col-align' in cls for cls in c.classes)]
            if cols:
                col_cells = []
                for col in cols:
                    vlist = find_first_vlist(col)
                    cells = []
                    if vlist:
                        for ch in vlist.children:
                            if ch.style and 'top:' in ch.style:
                                top_m = re.search(r'top:\s*(-?[\d\.]+)em', ch.style)
                                top_val = float(top_m.group(1)) if top_m else 0.0
                                cells.append((top_val, ch))
                    cells.sort(key=lambda x: x[0])
                    col_cells.append(cells)

                num_rows = max(len(c) for c in col_cells) if col_cells else 0
                rows_tex = []
                for r in range(num_rows):
                    row_items = []
                    for c in range(len(col_cells)):
                        if r < len(col_cells[c]):
                            cell_tex = render_katex_node(col_cells[c][r][1]).strip()
                            row_items.append(cell_tex)
                        else:
                            row_items.append("")
                    rows_tex.append(" & ".join(row_items))
                return f"\\begin{{{env_name}}} " + " \\\\ ".join(rows_tex) + f" \\end{{{env_name}}}"

    # 5. 矩阵 / 表格 mtable (\begin{pmatrix} ... \end{pmatrix})
    if 'mtable' in classes:
        cols = [c for c in node.children if any('col-align' in cls for cls in c.classes)]
        if cols:
            col_cells = []
            for col in cols:
                vlist = find_first_vlist(col)
                cells = []
                if vlist:
                    for ch in vlist.children:
                        if ch.style and 'top:' in ch.style:
                            top_m = re.search(r'top:\s*(-?[\d\.]+)em', ch.style)
                            top_val = float(top_m.group(1)) if top_m else 0.0
                            cells.append((top_val, ch))
                cells.sort(key=lambda x: x[0])
                col_cells.append(cells)

            num_rows = max(len(c) for c in col_cells) if col_cells else 0
            rows_tex = []
            for r in range(num_rows):
                row_items = []
                for c in range(len(col_cells)):
                    if r < len(col_cells[c]):
                        cell_tex = render_katex_node(col_cells[c][r][1]).strip()
                        row_items.append(cell_tex)
                    else:
                        row_items.append("")
                rows_tex.append(" & ".join(row_items))
            return "\\begin{pmatrix} " + " \\\\ ".join(rows_tex) + " \\end{pmatrix}"

    # 6. 分式 mfrac (\frac{numerator}{denominator})
    if 'mfrac' in classes:
        vlist = find_first_vlist(node)
        if vlist:
            direct_items = []
            for ch in vlist.children:
                if ch.style and 'top:' in ch.style and not has_class_recursive(ch, 'frac-line'):
                    top_m = re.search(r'top:\s*(-?[\d\.]+)em', ch.style)
                    top_val = float(top_m.group(1)) if top_m else 0.0
                    direct_items.append((top_val, ch))
            if len(direct_items) >= 2:
                direct_items.sort(key=lambda x: x[0])
                numer_node = direct_items[0][1]
                denom_node = direct_items[-1][1]
                numer_tex = render_katex_node(numer_node).strip()
                denom_tex = render_katex_node(denom_node).strip()
                return f"\\frac{{{numer_tex}}}{{{denom_tex}}}"

    # 7. 上下标 msupsub
    if 'msupsub' in classes:
        vlist = find_first_vlist(node)
        if vlist:
            direct_items = []
            for ch in vlist.children:
                if ch.style and 'top:' in ch.style:
                    top_m = re.search(r'top:\s*(-?[\d\.]+)em', ch.style)
                    top_val = float(top_m.group(1)) if top_m else 0.0
                    direct_items.append((top_val, ch))
            if len(direct_items) == 1:
                top_val, item_node = direct_items[0]
                item_tex = render_katex_node(item_node).strip()
                if item_tex in ['′', '′′', '′′′', "'", "''", "'''"]:
                    return item_tex.replace('′', "'")
                if top_val < -2.6:
                    return f"^{{{item_tex}}}"
                else:
                    return f"_{{{item_tex}}}"
            elif len(direct_items) >= 2:
                direct_items.sort(key=lambda x: x[0])
                sup_node = direct_items[0][1]
                sub_node = direct_items[-1][1]
                sup_tex = render_katex_node(sup_node).strip()
                sub_tex = render_katex_node(sub_node).strip()
                return f"_{{{sub_tex}}}^{{{sup_tex}}}"

    # 8. 根号 sqrt
    if 'sqrt' in classes:
        body = []
        for ch in node.children:
            if 'sqrt-sign' not in ch.classes:
                body.append(render_katex_node(ch))
        inner = "".join(body).strip()
        return f"\\sqrt{{{inner}}}"

    # 9. 数学算符 mop
    if 'mop' in classes:
        t = node.text.strip()
        if t in ['lim', 'ln', 'log', 'lg', 'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'arcsin', 'arccos', 'arctan', 'max', 'min', 'det', 'tr', 'exp', 'inf', 'sup']:
            return f"\\{t} "
        if t == '∫': return "\\int "
        if t == '∬': return "\\iint "
        if t == '∭': return "\\iiint "
        if t == '∮': return "\\oint "
        if t == '∑': return "\\sum "
        if t == '∏': return "\\prod "

    # 10. 常用数学符号与希腊字母映射
    symbol_map = {
        '→': '\\to ', '∞': '\\infty ', '∈': '\\in ', '∉': '\\notin ',
        '⊂': '\\subset ', '⊆': '\\subseteq ', '∪': '\\cup ', '∩': '\\cap ',
        '≤': '\\le ', '≥': '\\ge ', '≠': '\\ne ', '≈': '\\approx ',
        '≡': '\\equiv ', '∼': '\\sim ', '±': '\\pm ', '×': '\\times ',
        '÷': '\\div ', '⋅': '\\cdot ', '−': '-', '′': "'", '′′': "''", '′′′': "'''",
        'λ': '\\lambda ', 'α': '\\alpha ', 'β': '\\beta ', 'γ': '\\gamma ',
        'θ': '\\theta ', 'ξ': '\\xi ', 'η': '\\eta ', 'μ': '\\mu ',
        'σ': '\\sigma ', 'τ': '\\tau ', 'φ': '\\varphi ', 'ω': '\\omega ',
        'π': '\\pi ', 'ρ': '\\rho ', 'ε': '\\varepsilon ', 'δ': '\\delta ',
        'Δ': '\\Delta ', 'Σ': '\\Sigma ', 'Ω': '\\Omega ', 'Φ': '\\Phi ',
        '∇': '\\nabla ', '∂': '\\partial ', '∀': '\\forall ', '∃': '\\exists ',
        '⋱': '\\ddots ', '⋮': '\\vdots ', '⋯': '\\cdots ', '…': '\\dots '
    }

    t = node.text
    # 核心修复：叶子节点中所有原始 { 和 } 必须转义为 \{ 和 \}，确保 \{f(x_n)\} 等集合/数列不残缺
    t = t.replace('{', '\\{').replace('}', '\\}')
    for k, v in symbol_map.items():
        if k in t:
            t = t.replace(k, v)

    # 递归遍历子节点
    res = ""
    for ch in node.children:
        res += render_katex_node(ch)
    if not node.children:
        res += t
    return res

def extract_balanced_katex_spans(html_str):
    """提取所有顶层平衡的 KaTeX span 节点"""
    pos = 0
    results = []
    start_pattern = re.compile(r"<span\s+class=[\"\']?(katex(?:-display)?)[\"\']?[^>]*>", re.I)
    while pos < len(html_str):
        m = start_pattern.search(html_str, pos)
        if not m:
            break
        start_idx = m.start()
        is_display = "katex-display" in m.group(1)
        open_tags = 1
        idx = m.end()
        tag_pattern = re.compile(r"</?span\b[^>]*>", re.I)
        while open_tags > 0 and idx < len(html_str):
            tm = tag_pattern.search(html_str, idx)
            if not tm:
                break
            tag_text = tm.group(0).lower()
            if tag_text.startswith("</span"):
                open_tags -= 1
            else:
                open_tags += 1
            idx = tm.end()
        full_span = html_str[start_idx:idx]
        results.append((start_idx, idx, is_display, full_span))
        pos = idx
    return results

def convert_katex_in_html(html_str):
    """将 HTML 中所有的 KaTeX 节点准确替换为 $...$ 或 $$...$$"""
    spans = extract_balanced_katex_spans(html_str)
    if not spans:
        return html_str

    out = []
    last_idx = 0
    for s_idx, e_idx, is_display, span_html in spans:
        out.append(html_str[last_idx:s_idx])
        parser = KatexDOMBuilder()
        parser.feed(span_html)
        tex = render_katex_node(parser.root).strip()
        tex = re.sub(r'\s+', ' ', tex).strip()
        tex = tex.replace("^{′}", "'").replace("^{''}", "''")
        if is_display:
            out.append(f"\n\n$$\n{tex}\n$$\n\n")
        else:
            out.append(f"${tex}$")
        last_idx = e_idx
    out.append(html_str[last_idx:])
    return "".join(out)

# =============================================================================
# 3. HTML 到 Markdown 纯净清洗转换管线
# =============================================================================

def html_to_math_markdown(html_content):
    """数学真题专用 HTML -> Markdown 转换流水线"""
    # 1. 剪枝层：移除第三方 wrapper (保留 KaTeX 内部 svg 用于 glyph 解析)
    html_content = re.sub(r'<div class=[\"\']?svg-wrapper[\"\']?.*?</svg>\s*</div>\s*</div>', '', html_content, flags=re.DOTALL | re.I)

    # 2. KaTeX 转换层：精准生成 LaTeX 公式
    html_content = convert_katex_in_html(html_content)

    # 3. 移除残余的非 KaTeX SVG
    html_content = re.sub(r'<svg[^>]*>.*?</svg>', '', html_content, flags=re.DOTALL | re.I)

    # 4. 表格层：转换 HTML table 为 Markdown table
    def convert_table(m):
        table_html = m.group(0)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL | re.I)
        md_rows = []
        is_first = True
        for r in rows:
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, re.DOTALL | re.I)
            clean_cells = []
            for c in cells:
                c_clean = re.sub(r'<[^>]+>', '', c).strip().replace('|', '\\|')
                clean_cells.append(c_clean)
            if clean_cells:
                md_rows.append('| ' + ' | '.join(clean_cells) + ' |')
                if is_first:
                    md_rows.append('| ' + ' | '.join(['---'] * len(clean_cells)) + ' |')
                    is_first = False
        return '\n\n' + '\n'.join(md_rows) + '\n\n'

    html_content = re.sub(r'<table[^>]*>.*?</table>', convert_table, html_content, flags=re.DOTALL | re.I)

    # 5. 选项层：转换选择题选项
    def convert_option(m):
        opt_html = m.group(0)
        label_m = re.search(r'class=[\"\']?choice-label[\"\']?>\s*([A-D]\.?)\s*<', opt_html)
        lbl = label_m.group(1) if label_m else ""
        if lbl and not lbl.endswith('.'):
            lbl = f"{lbl}."
        text_m = re.search(r'class=[\"\']?choice-text[\"\']?>(.*?)</span>', opt_html, re.DOTALL)
        txt = text_m.group(1) if text_m else ""
        txt_clean = re.sub(r'<[^>]+>', '', txt).strip()
        if not lbl and not txt_clean:
            return ""
        if not txt_clean:
            letter = lbl.rstrip('.')
            txt_clean = f"见选项图示 ({letter})"
        if re.match(r'^\d+$', txt_clean):
            txt_clean = f"${txt_clean}$"
        # 选项标号后标点与逗号间距规范化
        txt_clean = re.sub(r'([，,])\s*则', r'，则', txt_clean)
        return f"\n- **{lbl}** {txt_clean}"

    html_content = re.sub(r'<label class=[\"\']?choice-option[\"\']?[^>]*>.*?</label>', convert_option, html_content, flags=re.DOTALL | re.I)
    math_tokens = []
    def save_math_token(m):
        math_tokens.append(m.group(0))
        return f"___MATH_BLOCK_TOKEN_{len(math_tokens)-1}___"

    html_content = re.sub(r'\$\$[\s\S]+?\$\$|\$[^\$\n]+?\$', save_math_token, html_content)

    # 7. 清理非内容 UI 元素
    html_content = re.sub(r'<button[^>]*>.*?</button>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<div class=[\"\']?quiz-actions[\"\']?[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<div class=[\"\']?quiz-tag-container[\"\']?[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<div class=[\"\']?feedback-area[\"\']?[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'</?form[^>]*>', '', html_content, flags=re.I)

    # 8. 转换结构性排版标签
    html_content = re.sub(r'</?(?:p|div|h\d)[^>]*>', '\n\n', html_content, flags=re.I)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.I)
    html_content = re.sub(r'</?(?:strong|b)\b[^>]*>', '**', html_content, flags=re.I)
    html_content = re.sub(r'</?(?:em|i)\b[^>]*>', '*', html_content, flags=re.I)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<img[^>]+>', '', html_content)
    # 安全移除标准 HTML 标签
    html_content = re.sub(r'</?[a-zA-Z][a-zA-Z0-9]*\b[^>]*>', '', html_content)

    # 9. 还原受保护的数学公式
    for idx, tok in enumerate(math_tokens):
        html_content = html_content.replace(f"___MATH_BLOCK_TOKEN_{idx}___", tok)

    # 10. 实体与字符转义解码
    html_content = html_content.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
    html_content = html_content.replace('\u200b', '').replace('\u00a0', ' ')

    # 11. 数学语法深度后处理与规范化
    greek_map = {
        'π': r'\pi', 'ρ': r'\rho', 'α': r'\alpha', 'β': r'\beta',
        'γ': r'\gamma', 'θ': r'\theta', 'λ': r'\lambda', 'μ': r'\mu',
        'σ': r'\sigma', 'τ': r'\tau', 'φ': r'\varphi', 'ω': r'\omega',
        'ε': r'\varepsilon', 'δ': r'\delta', 'η': r'\eta', 'ξ': r'\xi',
        'Δ': r'\Delta', 'Σ': r'\Sigma', 'Ω': r'\Omega', 'Φ': r'\Phi'
    }
    for k, v in greek_map.items():
        html_content = html_content.replace(k, v)

    html_content = html_content.replace('′′′', "'''").replace('′′', "''").replace('′', "'")
    html_content = html_content.replace('Xˉ', r'\bar{X}').replace('X\u0304', r'\bar{X}').replace('X\u02c9', r'\bar{X}')
    html_content = html_content.replace('∣', '|')
    # Unicode 不等号 / 否定号修复
    html_content = html_content.replace('=', r'\ne ').replace('\u0338=', r'\ne ').replace('\uE020=', r'\ne ').replace('\uE020', r'\ne ')

    # 填空题下划线处理: 规范化 math 模式内连缀下划线为 \underline{\hspace{2.5em}}
    def clean_math_blanks(m):
        math_str = m.group(0)
        if re.search(r'_{2,}', math_str):
            math_str = re.sub(r'_{2,}[\.．]?', r'\\underline{\\hspace{2.5em}}', math_str)
        return math_str

    html_content = re.sub(r'\$\$[\s\S]+?\$\$|\$[^\$\n]+?\$', clean_math_blanks, html_content)

    # 修复数列、集合、概率花括号匹配与上下标清洗
    html_content = re.sub(r'_\{([^{}]+?)\\\}', r'_{\1}', html_content)
    html_content = re.sub(r'\^\{([^{}]+?)\\\}', r'^{\1}', html_content)

    # 12. 消除多余孤立 A/B/C/D 悬空行（通常为图片选项丢失后的残留）
    html_content = re.sub(r'\n\s*[A-D]\s*\n(?=\s*[A-D]\s*\n|\s*- \*\*[A-D]\*\*)', '', html_content)
    html_content = re.sub(r'(\n\s*[A-D]\s*\n)+', '\n', html_content)

    # 13. cases 分段函数 / 方程组转换: { \begin{pmatrix} -> \begin{cases}
    html_content = re.sub(r'\{\s*\\begin\{pmatrix\}(.*?)\\end\{pmatrix\}', r'\\begin{cases}\1\\end{cases}', html_content, flags=re.DOTALL)

    # 14. 文本清理与规范化
    html_content = re.sub(r'\*{4,}', '**', html_content)
    html_content = re.sub(r'[ \t]+\n', '\n', html_content)
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)
    html_content = re.sub(r'-\s*\n+\*\*([A-D]\.?)\*\*\s*', r'- **\1** ', html_content)

    # 15. 全量消除（填空题）与（本题满分 XX 分）
    html_content = re.sub(r'[（\(]\s*填空题\s*[）\)]\s*', '', html_content)
    html_content = re.sub(r'[（\(]\s*本题满分\s*\\?\$?\d+\\?\$?\s*分\s*[）\)]\s*', '', html_content)

    # 16. 段落平滑流式化（合并同一段落内被 KaTeX 打断的行折断）
    paragraphs = html_content.split('\n\n')
    cleaned_paras = []
    for p in paragraphs:
        p_str = p.strip()
        if not p_str:
            continue
        if p_str.startswith('- **') or p_str.startswith('$$') or p_str.startswith('```') or p_str.startswith('|') or p_str.startswith('#'):
            if p_str.startswith('- **'):
                lines = p_str.split('\n')
                smoothed_lines = []
                for ln in lines:
                    ln_s = ln.strip()
                    if ln_s.startswith('- **'):
                        smoothed_lines.append(ln_s)
                    elif smoothed_lines:
                        smoothed_lines[-1] += ' ' + ln_s
                    else:
                        smoothed_lines.append(ln_s)
                cleaned_paras.append('\n'.join(smoothed_lines))
            else:
                cleaned_paras.append(p_str)
        else:
            lines = [ln.strip() for ln in p_str.split('\n') if ln.strip()]
            cleaned_paras.append(' '.join(lines))

    res = '\n\n'.join(cleaned_paras).strip()
    res = re.sub(r'\s+([，。、；：！？）])', r'\1', res)
    res = re.sub(r'([（])\s+', r'\1', res)
    return res

# =============================================================================
# 4. 一站式单年份真题爬取与编译
# =============================================================================

def process_math1_year(year, output_root=DEFAULT_ROOT, *, force=False):
    year_dir = os.path.join(output_root, f"{year}年真题")
    exam_json_path = os.path.join(year_dir, "exam.json")
    if os.path.isfile(exam_json_path) and not force:
        try:
            with open(exam_json_path, "r", encoding="utf-8") as f:
                existing_meta = json.load(f)
            existing_main = existing_meta.get("main_file", "")
            canonical_path = os.path.join(year_dir, existing_main) if existing_main else ""
            if canonical_path and os.path.isfile(canonical_path):
                print(f"[skip] Canonical source already exists: {canonical_path}. Use --force for an intentional rebuild.")
                return True
        except (OSError, json.JSONDecodeError):
            pass

    if year <= 2007:
        year_url = f"https://www.csgraduates.com/study_methods/math_old/{year}/1/"
    else:
        year_url = f"{BASE_URL}/{year}/"

    req = urllib.request.Request(year_url, headers=HEADERS)
    try:
        raw = urllib.request.urlopen(req, context=ssl_context, timeout=15).read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"❌ 下载数学（一）{year} 年真题失败: {e}")
        return False

    os.makedirs(year_dir, exist_ok=True)
    # 清理旧命名的分题文件以防学科重名残留
    for old_f in os.listdir(year_dir):
        if re.match(r'^q\d{2}_.*\.md$', old_f):
            os.remove(os.path.join(year_dir, old_f))

    print(f"🚀 开始一步到位高保真编译: {year} 年全国硕士研究生招生考试 数学（一）真题...")

    # 探测总题量 (2021+ 22题, 2007 24题, 2008-2020 23题)
    q_ids = [int(x) for x in re.findall(r'<h5[^>]*id=[\"\']?(\d+)[\"\']?>\1</h5>', raw)]
    total_q_count = max(q_ids) if q_ids else (22 if year >= 2021 else (24 if year == 2007 else 23))

    questions_data = []
    figure_assets = {}
    content_figures = []
    content_code = []
    content_tables = []
    question_scores = {}

    for q in range(1, total_q_count + 1):
        if q < total_q_count:
            pattern = rf'<h5[^>]*id=[\"\']?{q}[\"\']?>{q}</h5>(.*?)(?=<h5[^>]*id=[\"\']?{q+1}[\"\']?>{q+1}</h5>)'
        else:
            pattern = rf'<h5[^>]*id=[\"\']?{total_q_count}[\"\']?>{total_q_count}</h5>(.*?)(?=<footer|<div class=[\"\']td-content-footer|<div class=[\"\']feedback-area)'

        m = re.search(pattern, raw, re.DOTALL)
        if not m:
            continue

        block = m.group(1)
        meta = get_math1_metadata(year, q)
        subject = meta['subject']
        q_type = meta['type']
        
        # 动态判定题型与分值
        if 'choice-container' in block:
            q_type = "单项选择题"
            score = 5 if year >= 2021 else (4 if year >= 2003 else (3 if year >= 1999 else 4))
        else:
            score_m = re.search(r'[（\(]\s*本题满分\s*\\?\$?(\d+)\\?\$?\s*分\s*[）\)]', block)
            if score_m:
                q_type = "解答题"
                score = int(score_m.group(1))
            else:
                meta = get_math1_metadata(year, q)
                if meta['type'] == '解答题' or (year <= 2006 and q >= 13):
                    q_type = "解答题"
                    score = 10 if year >= 2003 else (7 if year >= 1999 else 8)
                else:
                    q_type = "填空题"
                    score = 5 if year >= 2021 else (4 if year >= 2003 else 3)

        # 从 data-tags 标签精准提取学科属性
        tag_m = re.search(r'data-tags=[\"\']?([^\"\'>]+)', block)
        if tag_m:
            tag_str = tag_m.group(1)
            if '线性代数' in tag_str or '矩阵' in tag_str or '向量' in tag_str or '二次型' in tag_str:
                subject = "线性代数"
            elif '概率' in tag_str or '数理统计' in tag_str or '随机变量' in tag_str or '分布' in tag_str or '方差' in tag_str:
                subject = "概率论与数理统计"
            elif '高等数学' in tag_str or '微积分' in tag_str or '级数' in tag_str or '导数' in tag_str or '积分' in tag_str:
                subject = "高等数学"

        question_scores[str(q)] = score

        # 1. 题图处理 (已知真实几何图映射与挂载)
        svg_links = []
        known_figures = {
            (1990, 19): "q19_semicircle_work.svg",
            (1999, 15): "q15_well_cable_lifting.svg",
            (2003, 7): "q07_derivative_graph.svg",
            (2005, 17): "q17_spline_tangents.svg",
            (2007, 3): "q03_four_semicircles.svg",
            (2008, 6): "q06_two_sheet_hyperboloid.svg",
            (2009, 2): "q02_square_regions.svg",
            (2009, 3): ["q03_piecewise_curve.svg", "q03_options_grid.svg"],
            (2015, 1): "q01_second_derivative.svg",
            (2017, 4): "q04_velocity_curves.svg",
            (2019, 6): "q06_three_planes_intersection.svg",
            (2024, 5): "q05_three_planes_pencil.svg",
        }

        if (year, q) in known_figures:
            figs = known_figures[(year, q)]
            if isinstance(figs, list):
                for f_item in figs:
                    figure_assets[f"{q}_{f_item}"] = f"assets/{f_item}"
                    svg_links.append(f"\n\n![题目图示](./assets/{f_item})\n\n")
            else:
                figure_assets[str(q)] = f"assets/{figs}"
                svg_links.append(f"\n\n![题目图示](./assets/{figs})\n\n")
            content_figures.append(q)

        # 2. 分离题干与题解
        correct_ans = ""
        stem_html = ""
        ans_html = ""

        if q_type == '单项选择题':
            ans_m = re.search(r'data-answer=[\"\']?([A-D])[\"\']?', block)
            correct_ans = ans_m.group(1) if ans_m else ""
            stem_split = re.split(r'<div class=[\"\']choice-container', block, maxsplit=1)
            stem_html = stem_split[0]
            form_m = re.search(r'<form[^>]*>(.*?)</form>', block, re.DOTALL)
            if form_m:
                stem_html += f"\n{form_m.group(0)}"
            exp_split = re.split(r'<div class=[\"\']?explanation[\"\']?[^>]*>', block, maxsplit=1)
            ans_html = exp_split[1] if len(exp_split) > 1 else ""
        else:
            stem_split = re.split(r'<div class=[\"\']answer-container', block, maxsplit=1)
            stem_html = stem_split[0]
            sol_split = re.split(r'<div class=[\"\']?solution-detail[^\"\']*[\"\']?[^>]*>', block, maxsplit=1)
            ans_html = sol_split[1] if len(sol_split) > 1 else ""

        stem_md = html_to_math_markdown(stem_html)
        ans_md = html_to_math_markdown(ans_html)

        if svg_links:
            stem_md += "".join(svg_links)

        if '```' in stem_md:
            content_code.append(q)
        if '| --- |' in stem_md:
            content_tables.append(q)

        # 3. 产出单题 Markdown (核心契约：文件名与正文一级标题 1:1 绝对一致)
        base_name = f"q{q:02d}_{subject}"
        file_name = f"{base_name}.md"

        frontmatter = (
            f"---\n"
            f"year: {year}\n"
            f"question_id: {q}\n"
            f"subject: {subject}\n"
            f"type: {q_type}\n"
            f"score: {score}\n"
        )
        if correct_ans:
            frontmatter += f"answer: {correct_ans}\n"
        frontmatter += f"---\n\n"

        full_q_content = (
            f"{frontmatter}"
            f"# {base_name}\n\n"
            f"## 📋 题目要求 (题面)\n\n"
            f"{stem_md}\n\n"
            f"---\n\n"
            f"## 💡 答案与深度解析\n\n"
        )
        if correct_ans:
            full_q_content += f"**【正确答案】**：`{correct_ans}`\n\n"
        full_q_content += f"{ans_md}\n"

        file_path = os.path.join(year_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(full_q_content)

        questions_data.append({
            'q': q,
            'subject': subject,
            'type': q_type,
            'score': score,
            'stem_md': stem_md
        })

    # =========================================================================
    # 5. 生成合一的 Canonical 正式版试卷 (<year> 年全国硕士研究生招生考试 数学（一）真题.md)
    # 核心契约：文件名与正文一级标题 1:1 绝对一致 (Zero-Deviation H1 Contract)
    # =========================================================================
    formal_title = f"{year} 年全国硕士研究生招生考试 数学（一）真题"
    formal_filename = f"{formal_title}.md"
    formal_path = os.path.join(year_dir, formal_filename)

    total_exam_score = 100 if year <= 2002 else 150

    formal_frontmatter = (
        f"---\n"
        f"type: exam-source\n"
        f"exam_id: math1-{year}\n"
        f"exam_profile: math1\n"
        f"year: {year}\n"
        f"status: ready\n"
        f"total_score: {total_exam_score}\n"
        f"question_count: {len(questions_data)}\n"
        f"metadata_file: exam.json\n"
        f"---\n\n"
    )

    # 按照题目真实出现顺序动态组织大题分节
    sections = []
    current_type = None
    current_group = []

    for qd in questions_data:
        if qd['type'] != current_type:
            if current_group:
                sections.append((current_type, current_group))
            current_type = qd['type']
            current_group = [qd]
        else:
            current_group.append(qd)
    if current_group:
        sections.append((current_type, current_group))

    section_titles = ["一", "二", "三", "四", "五"]
    formal_body = f"# {formal_title}\n\n"

    for idx, (stype, s_qs) in enumerate(sections):
        s_num = section_titles[idx] if idx < len(section_titles) else str(idx + 1)
        s_start = s_qs[0]['q']
        s_end = s_qs[-1]['q']
        s_score = sum(qd['score'] for qd in s_qs)
        if stype == '单项选择题':
            each_score = s_qs[0]['score']
            formal_body += f"## {s_num}、单项选择题（第 {s_start}～{s_end} 小题，每小题 {each_score} 分，共 {s_score} 分）\n\n"
        elif stype == '填空题':
            each_score = s_qs[0]['score']
            formal_body += f"## {s_num}、填空题（第 {s_start}～{s_end} 小题，每小题 {each_score} 分，共 {s_score} 分）\n\n"
        elif stype == '解答题':
            formal_body += f"## {s_num}、解答题（第 {s_start}～{s_end} 小题，共 {s_score} 分）\n\n"

        for qd in s_qs:
            if stype == '解答题':
                formal_body += f"### {qd['q']}（本题满分 {qd['score']} 分）\n\n{qd['stem_md']}\n\n"
            else:
                formal_body += f"### {qd['q']}\n\n{qd['stem_md']}\n\n"

    with open(formal_path, 'w', encoding='utf-8') as ffp:
        ffp.write(formal_frontmatter + formal_body)

    # 移除历史旧命名的文件以防冗余
    legacy_files = [os.path.join(year_dir, f"{year}_数一真题_正式版.md"), os.path.join(year_dir, f"{year}_408真题_正式版.md")]
    for lf in legacy_files:
        if os.path.exists(lf) and lf != formal_path:
            os.remove(lf)

    # =========================================================================
    # 6. 生成 exam.json
    # =========================================================================
    exam_json = {
        "schema_version": 1,
        "exam_id": f"math1-{year}",
        "profile_id": "math1",
        "year": year,
        "language": "zh-CN",
        "title": formal_title,
        "main_file": formal_filename,
        "status": "ready",
        "question_count": len(questions_data),
        "total_score": total_exam_score,
        "question_scores": question_scores,
        "content_features": {
            "figures": sorted(content_figures),
            "code": sorted(content_code),
            "tables": sorted(content_tables)
        },
        "figure_assets": figure_assets,
        "routing": "profile-default",
        "open_items": []
    }

    with open(os.path.join(year_dir, 'exam.json'), 'w', encoding='utf-8') as ejf:
        json.dump(exam_json, ejf, ensure_ascii=False, indent=2)
        ejf.write('\n')

    print(f"✅ {year} 年数学（一）编译完毕: 产出题目 {len(questions_data)} 篇，正式整卷已生成，沉淀真实题图 {len(content_figures)} 张。")
    return True

# =============================================================================
# 7. 主入口
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="考研数学（一）历年统考真题一站式高保真爬取与编译工具")
    parser.add_argument('--year', type=int, help="指定爬取的年份 (例如 2007)")
    parser.add_argument('--historical', action='store_true', help="爬取 1987-2007 历史数学（一）真题")
    parser.add_argument('--all', action='store_true', help="全量检查/补抓 1987-2026；已有 Canonical 年份默认跳过")
    parser.add_argument('--force', action='store_true', help="允许覆盖已有 Canonical Source；属于显式破坏性操作")
    args = parser.parse_args()

    print("=" * 70)
    print("考研数学（一）统考真题一站式纯净爬取与编译引擎 (Math1 Compiler)")
    print("=" * 70)

    if args.year:
        process_math1_year(args.year, force=args.force)
    elif args.historical:
        for y in range(1987, 2008):
            process_math1_year(y, force=args.force)
            time.sleep(random.uniform(0.2, 0.5))
    elif args.all:
        for y in range(1987, 2027):
            process_math1_year(y, force=args.force)
            time.sleep(random.uniform(0.2, 0.5))
    else:
        parser.print_help()
        return 2

    print("=" * 70)
    print("🎉 任务执行完毕！")
    print("=" * 70)

if __name__ == '__main__':
    raise SystemExit(main())
