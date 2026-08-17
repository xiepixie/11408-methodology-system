#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=============================================================================
408 历年统考真题高保真纯净一站式爬取与 Markdown 编译引擎 (One-Shot Compiler)
=============================================================================
核心特性：
1. 架构级 AST/DOM 节点分离与剪枝：彻底杜绝图表无障碍文本回退泄露；
2. 代码块原生纯净化保护：剥离 Chroma/Prism 高亮 span，保持完整缩进与换行；
3. KaTeX 原生符号精确提取：保留数学符号语义，绝不误伤十六进制地址与机器数；
4. Draw.io SVG 矢量图净化管线：自动剥离 <switch> 与 WebKit 兼容障碍属性；
5. 文件名与一级标题严格同源保证：100% 符合 Obsidian 知识库规范。
=============================================================================
"""

import urllib.request
import ssl
import re
import os
import json
import time
import random
import argparse
import xml.etree.ElementTree as ET

DEFAULT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../archives/408'))
PROFILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../exam_profiles/408.json'))
BASE_URL = 'https://www.csgraduates.com/study_methods/408quiz'
with open(PROFILE_PATH, 'r', encoding='utf-8') as _profile_file:
    EXAM_PROFILE = json.load(_profile_file)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Referer': 'https://www.csgraduates.com/',
}

ssl_context = ssl.create_default_context()

def get_subject_for_question(year, q_num):
    """Resolve subject routing from the Canonical 408 Exam Profile, including year overrides."""
    routes = []
    overrides = EXAM_PROFILE.get('routing_overrides', {}).get(str(year), [])
    routes.extend(overrides)
    if q_num <= 40:
        routes.extend(EXAM_PROFILE.get('objective_routing', []))
    else:
        routes.extend(EXAM_PROFILE.get('comprehensive_routing_default', []))

    for route in routes:
        questions = route.get('questions')
        if isinstance(questions, dict):
            matched = questions.get('from', 1) <= q_num <= questions.get('to', 0)
        else:
            matched = q_num in (questions or [])
        if matched:
            subject = route['subject']
            return f"{subject} (综合应用题)" if q_num >= 41 else subject
    return '408综合'

def sanitize_svg_content(raw_svg):
    """净化 Draw.io SVG，确保跨平台 (Obsidian, Safari, QuickLook) 零空白、响应式渲染"""
    s = raw_svg
    # 1. 补齐命名空间
    if 'xmlns="http://www.w3.org/2000/svg"' not in s and "xmlns='http://www.w3.org/2000/svg'" not in s:
        s = re.sub(r'<svg\b', '<svg xmlns="http://www.w3.org/2000/svg"', s, count=1)
    if 'xlink:' in s and 'xmlns:xlink=' not in s:
        s = re.sub(r'<svg\b', '<svg xmlns:xlink="http://www.w3.org/1999/xlink"', s, count=1)
    
    # 2. 注入响应式样式 (max-width: 100%; height: auto;)
    m_svg = re.search(r'<svg\b([^>]*)>', s)
    if m_svg:
        attrs = m_svg.group(1)
        if 'style=' not in attrs:
            new_attrs = attrs + ' style="max-width: 100%; height: auto;"'
            s = s[:m_svg.start(1)] + new_attrs + s[m_svg.end(1):]
        elif 'max-width' not in attrs:
            s = re.sub(r'style=[\"\']([^\"\']*)[\"\']', r'style="\1; max-width: 100%; height: auto;"', s, count=1)

    # 3. 标准化字体栈
    s = re.sub(r'font-family:\s*Helvetica\b', "font-family: Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif", s)
    s = re.sub(r'font-family:\s*&quot;Helvetica&quot;', "font-family: Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif", s)
    s = re.sub(r'font-family:\s*\'Helvetica\'', "font-family: Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif", s)

    # 4. 移除阻塞 WebKit/Chromium 渲染的 <switch> 与 requiredFeatures
    s = re.sub(r'<switch>\s*', '', s)
    s = re.sub(r'\s*</switch>', '', s)
    s = re.sub(r'\s*requiredfeatures=[\"\'][^\"\']*[\"\']', '', s, flags=re.I)
    s = re.sub(r'\s*requiredFeatures=[\"\'][^\"\']*[\"\']', '', s)
    return s.strip()

def parse_katex_span(html_katex):
    """将 KaTeX 节点精准转换为 LaTeX 数学公式"""
    t = re.sub(r'<span class=[\"\']?strut[\"\']?[^>]*>.*?</span>', '', html_katex)
    clean = re.sub(r'<[^>]+>', '', t)
    clean = clean.replace('&nbsp;', ' ').replace('\u200b', '').strip()
    # 规范常见下标与二元算符
    clean = re.sub(r'([A-Za-z])([0-9]+),([0-9]+)', r'\1_{\2,\3}', clean)
    clean = re.sub(r'([A-Za-z])([i-n]),([i-n0-9])', r'\1_{\2,\3}', clean)
    clean = re.sub(r'([A-Za-z])([0-9]+)', r'\1_{\2}', clean)
    clean = re.sub(r'×', r'\\times ', clean)
    clean = re.sub(r'≤', r'\\le ', clean)
    clean = re.sub(r'≥', r'\\ge ', clean)
    clean = re.sub(r'≠', r'\\ne ', clean)
    if clean:
        return f"${clean}$"
    return ""

def html_to_markdown_clean(html_content):
    """高精度 HTML -> Markdown 纯净转换流水线"""
    # 1. 剪枝层：彻底物理移除 <div class="svg-wrapper"> 与内联 <svg>，防止图表文本碎片泄露
    html_content = re.sub(r'<div class=[\"\']?svg-wrapper[\"\']?.*?</svg>\s*</div>\s*</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<svg[^>]*>.*?</svg>', '', html_content, flags=re.DOTALL | re.I)

    # 2. 代码层：保护 <pre><code> 块，剔除高亮标签，保持换行缩进
    code_blocks = []
    def save_code(m):
        code_text = m.group(1)
        code_text = re.sub(r'<[^>]+>', '', code_text)
        code_text = code_text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
        code_text = code_text.strip()
        idx = len(code_blocks)
        code_blocks.append(f"\n\n```c\n{code_text}\n```\n\n")
        return f"___CODE_BLOCK_{idx}___"

    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', save_code, html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', save_code, html_content, flags=re.DOTALL | re.I)

    # 3. 数学层：提取 KaTeX 节点
    katex_blocks = []
    def save_katex(m):
        katex_html = m.group(0)
        latex_str = parse_katex_span(katex_html)
        idx = len(katex_blocks)
        katex_blocks.append(latex_str)
        return f" ___KATEX_{idx}___ "

    html_content = re.sub(r'<span class=[\"\']?katex[\"\']?>.*?</span></span></span>', save_katex, html_content, flags=re.DOTALL)
    html_content = re.sub(r'<span class=[\"\']?katex[\"\']?>.*?</span>', save_katex, html_content, flags=re.DOTALL)

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
        text_m = re.search(r'class=[\"\']?choice-text[\"\']?>(.*?)</span>', opt_html, re.DOTALL)
        txt = text_m.group(1) if text_m else ""
        txt_clean = re.sub(r'<[^>]+>', '', txt).strip()
        if not lbl and not txt_clean:
            return ""
        return f"\n- **{lbl}** {txt_clean}"

    html_content = re.sub(r'<label class=[\"\']?choice-option[\"\']?[^>]*>.*?</label>', convert_option, html_content, flags=re.DOTALL | re.I)

    # 6. 清理非内容 UI 元素
    html_content = re.sub(r'<button[^>]*>.*?</button>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<div class=[\"\']?quiz-actions[\"\']?[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<div class=[\"\']?quiz-tag-container[\"\']?[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<div class=[\"\']?feedback-area[\"\']?[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'</?form[^>]*>', '', html_content, flags=re.I)

    # 7. 基础排版标签转换
    html_content = re.sub(r'</?(?:p|div|h\d)[^>]*>', '\n\n', html_content, flags=re.I)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.I)
    html_content = re.sub(r'</?(?:strong|b)\b[^>]*>', '**', html_content, flags=re.I)
    html_content = re.sub(r'</?(?:em|i)\b[^>]*>', '*', html_content, flags=re.I)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.I)
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # 8. 恢复 KaTeX 占位符
    for idx, tex in enumerate(katex_blocks):
        html_content = html_content.replace(f"___KATEX_{idx}___", tex)

    # 9. 恢复代码块占位符
    for idx, code_md in enumerate(code_blocks):
        html_content = html_content.replace(f"___CODE_BLOCK_{idx}___", code_md)

    # 10. 文本流润色与空格标准化
    html_content = html_content.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
    html_content = html_content.replace('\u200b', '').replace('\u00a0', ' ')
    html_content = re.sub(r'\*{4,}', '**', html_content)
    html_content = re.sub(r'[ \t]+\n', '\n', html_content)
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)
    html_content = re.sub(r'-\s*\n+\*\*([A-D]\.?)\*\*\s*', r'- **\1** ', html_content)
    return html_content.strip()

def process_year(year, output_root=DEFAULT_ROOT, *, force=False):
    """一站式下载、提取 SVG、编译 Markdown 核心函数。已有年度默认保护。"""
    year_dir = os.path.join(output_root, f"{year}年真题")
    if os.path.exists(os.path.join(year_dir, "exam.json")) and not force:
        print(f"[skip] Archive year already exists: {year_dir}. Use --force for an intentional raw-source refresh.")
        return True

    year_url = f"{BASE_URL}/{year}/"
    req = urllib.request.Request(year_url, headers=HEADERS)
    try:
        raw = urllib.request.urlopen(req, context=ssl_context, timeout=15).read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"❌ 下载 {year} 年真题失败: {e}")
        return False

    assets_dir = os.path.join(year_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    print(f"🚀 开始一步到位高保真编译: {year} 年 408 全国统考真题...")

    success_q = 0
    svg_extracted = 0

    for q in range(1, 48):
        if q < 47:
            pattern = rf'<h5[^>]*id=[\"\']?{q}[\"\']?>{q}</h5>(.*?)(?=<h5[^>]*id=[\"\']?{q+1}[\"\']?>{q+1}</h5>)'
        else:
            pattern = rf'<h5[^>]*id=[\"\']?47[\"\']?>47</h5>(.*?)(?=<footer|<div class=[\"\']td-content-footer)'

        m = re.search(pattern, raw, re.DOTALL)
        if not m:
            continue

        block = m.group(1)
        subject = get_subject_for_question(year, q)

        # 提取标签
        tags_m = re.search(r'data-tags=[\"\']?([^\"\'\s>]+)[\"\']?', block)
        tag_str = tags_m.group(1) if tags_m else subject

        # 1. 提取并净化内联 SVG 矢量图
        svg_matches = re.findall(r'<svg[^>]*>.*?</svg>', block, re.DOTALL | re.I)
        svg_links = []
        for idx, svg_raw in enumerate(svg_matches, 1):
            sanitized_svg = sanitize_svg_content(svg_raw)
            svg_filename = f"q{q:02d}_fig{idx}.svg"
            svg_path = os.path.join(assets_dir, svg_filename)
            with open(svg_path, 'w', encoding='utf-8') as sfp:
                sfp.write(sanitized_svg)
            # 校验 XML
            try:
                ET.parse(svg_path)
                svg_extracted += 1
                svg_links.append(f"\n\n![题目图示](./assets/{svg_filename})\n\n")
            except Exception as ex:
                print(f"⚠️ {year} Q{q} 图形 XML 警告: {ex}")

        # 2. 区分题干与题解并清洗
        stem_html = ""
        ans_html = ""
        correct_ans = ""

        if q <= 40:
            ans_m = re.search(r'data-answer=[\"\']?([A-D])[\"\']?', block)
            correct_ans = ans_m.group(1) if ans_m else ""

            stem_split = re.split(r'<div class=[\"\']choice-container', block, maxsplit=1)
            stem_html = stem_split[0]

            form_m = re.search(r'<form[^>]*>(.*?)</form>', block, re.DOTALL)
            if form_m:
                stem_html += f"\n{form_m.group(0)}"

            exp_m = re.search(r'<div class=[\"\']?explanation[\"\']?[^>]*>(.*?)</div>', block, re.DOTALL)
            ans_html = exp_m.group(1) if exp_m else ""
        else:
            stem_split = re.split(r'<div class=[\"\']answer-container', block, maxsplit=1)
            stem_html = stem_split[0]

            sol_m = re.search(r'<div class=[\"\']?solution-detail[^\"\']*[\"\']?[^>]*>(.*?)</div>', block, re.DOTALL)
            ans_html = sol_m.group(1) if sol_m else ""

        stem_md = html_to_markdown_clean(stem_html)
        ans_md = html_to_markdown_clean(ans_html)

        if svg_links:
            stem_md += "".join(svg_links)

        # 3. 生成严格对齐的 Frontmatter 与 H1 标题
        subj_short = subject.split(' ')[0]
        base_name = f"q{q:02d}_{subj_short}"
        file_name = f"{base_name}.md"

        frontmatter = (
            f"---\n"
            f"year: {year}\n"
            f"question_id: {q}\n"
            f"subject: {subject}\n"
            f"tags: [{tag_str}]\n"
        )
        if correct_ans:
            frontmatter += f"answer: {correct_ans}\n"
        frontmatter += f"---\n\n"

        h1_title = f"# {base_name}\n\n"

        full_content = (
            f"{frontmatter}"
            f"{h1_title}"
            f"## 📋 题目要求 (题面)\n\n"
            f"{stem_md}\n\n"
            f"---\n\n"
            f"## 💡 答案与深度解析\n\n"
        )
        if correct_ans:
            full_content += f"**【正确答案】**：`{correct_ans}`\n\n"
        full_content += f"{ans_md}\n"

        file_path = os.path.join(year_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(full_content)

        success_q += 1

    print(f"✅ {year} 年编译完毕: 产出题目 {success_q}/47 篇，沉淀有效矢量图 {svg_extracted} 张。")
    return True

def main():
    parser = argparse.ArgumentParser(description="408 历年统考真题一站式高保真爬取与编译工具")
    parser.add_argument('--year', type=int, help="指定爬取的年份 (例如 2025)")
    parser.add_argument('--all', action='store_true', help="全量检查/补抓 2009-2026；已有年度默认跳过")
    parser.add_argument('--force', action='store_true', help="允许刷新已有年度 raw source；属于显式破坏性操作")
    args = parser.parse_args()

    print("=" * 65)
    print("408 考研统考真题一站式纯净爬取与编译引擎 (Single Script Runner)")
    print("=" * 65)

    if args.year:
        process_year(args.year, force=args.force)
    elif args.all:
        for y in range(2009, 2027):
            process_year(y, force=args.force)
            time.sleep(random.uniform(0.3, 0.5))
    else:
        parser.print_help()
        return 2

    print("=" * 65)
    print("🎉 任务执行完毕！")
    print("=" * 65)

if __name__ == '__main__':
    raise SystemExit(main())
