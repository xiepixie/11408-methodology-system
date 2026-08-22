#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_math1_svgs.py
======================
显式重生成仍由 legacy direct-SVG 管线拥有的数学一 Semantic SVG 资产（暗色+亮色双主题）。
已经建立 assets/src/*.tex 的 TikZ-backed 图不属于本脚本 Owner。
严格执行：kaoyan/00_system/exam_source_conversion_spec.md (Section 10)
"""

import argparse
import os
import re
import json

KAOYAN_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ARCHIVE_ROOT = os.path.join(KAOYAN_ROOT, "archives/math1")

DARK_THEME = {
    "bg": "#2e362c",
    "fg": "#edf4e8",
    "node": "#3b4337",
    "soft": "#394136",
    "muted": "#596452",
    "accent": "#98c379",
    "shade": "rgba(237, 244, 232, 0.15)",
    "plane1": "rgba(152, 195, 121, 0.25)",
    "plane2": "rgba(97, 175, 239, 0.25)",
    "plane3": "rgba(229, 192, 123, 0.25)"
}

LIGHT_THEME = {
    "bg": "#faf8f5",
    "fg": "#111111",
    "node": "#ffffff",
    "soft": "#f7f6f1",
    "muted": "#eceee8",
    "accent": "#2e7d32",
    "shade": "rgba(0, 0, 0, 0.08)",
    "plane1": "rgba(46, 125, 50, 0.20)",
    "plane2": "rgba(25, 118, 210, 0.20)",
    "plane3": "rgba(230, 81, 0, 0.20)"
}

def make_svg(width, height, content, theme):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <style>
    .bg {{ fill: {theme["bg"]}; }}
    .fg {{ stroke: {theme["fg"]}; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }}
    .axis {{ stroke: {theme["fg"]}; stroke-width: 1.8; fill: none; }}
    .grid {{ stroke: {theme["muted"]}; stroke-width: 1; stroke-dasharray: 4,4; fill: none; }}
    .curve {{ stroke: {theme["fg"]}; stroke-width: 2.4; fill: none; }}
    .curve-accent {{ stroke: {theme["accent"]}; stroke-width: 2.4; fill: none; }}
    .curve-dashed {{ stroke: {theme["fg"]}; stroke-width: 2; stroke-dasharray: 5,5; fill: none; }}
    .shade {{ fill: {theme["shade"]}; stroke: {theme["fg"]}; stroke-width: 1.5; }}
    .plane1 {{ fill: {theme["plane1"]}; stroke: {theme["fg"]}; stroke-width: 1.5; }}
    .plane2 {{ fill: {theme["plane2"]}; stroke: {theme["fg"]}; stroke-width: 1.5; }}
    .plane3 {{ fill: {theme["plane3"]}; stroke: {theme["fg"]}; stroke-width: 1.5; }}
    .text {{ fill: {theme["fg"]}; font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', Arial, sans-serif; font-size: 15px; text-anchor: middle; }}
    .text-sm {{ fill: {theme["fg"]}; font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', Arial, sans-serif; font-size: 13px; text-anchor: middle; }}
    .text-xs {{ fill: {theme["fg"]}; font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', Arial, sans-serif; font-size: 11px; text-anchor: middle; }}
    .point {{ fill: {theme["fg"]}; }}
  </style>
  <rect width="100%" height="100%" class="bg"/>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="{theme["fg"]}"/>
    </marker>
    <marker id="arrow-sm" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 7 5 L 0 8 z" fill="{theme["fg"]}"/>
    </marker>
  </defs>
  {content}
</svg>"""

# 1990
def gen_1990_q01(theme):
    # 笛卡尔坐标严格换算：原点 O(60, 320), 比例 scale=60px
    # A(1, 2) -> (120, 200)
    # B(3, 4) -> (240, 80)
    # 圆心 M(2, 3) -> (180, 140), 半径 R = sqrt(2)*60 ≈ 84.85
    # 下半圆过最低点 (3, 2) -> (240, 200)
    content = """
  <!-- 坐标轴 -->
  <line x1="30" y1="320" x2="360" y2="320" class="axis" marker-end="url(#arrow)"/>
  <line x1="60" y1="350" x2="60" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="355" y="345" class="text">x</text>
  <text x="40" y="40" class="text">y</text>
  <text x="45" y="340" class="text">O</text>

  <!-- 弦 AB 虚线 -->
  <line x1="120" y1="200" x2="240" y2="80" class="curve-dashed"/>

  <!-- 下半圆弧线（严格以 AB 为直径，下凸过 (3,2)，半径 84.85） -->
  <path d="M 120 200 A 84.85 84.85 0 0 0 240 80" class="curve" stroke-width="2.8"/>

  <!-- 轨迹流动箭头（沿下半圆从 A 指向 B） -->
  <polygon points="180,225 192,220 188,233" fill="{theme['fg']}"/>

  <!-- 原点到动点 P 的虚线向量 -->
  <line x1="60" y1="320" x2="240" y2="200" class="fg" stroke-dasharray="3,3"/>

  <!-- 动点 P 处的受力向量 F -->
  <line x1="240" y1="200" x2="185" y2="125" class="curve-accent" stroke-width="2.5" marker-end="url(#arrow)"/>

  <!-- 关键点标记 -->
  <circle cx="120" cy="200" r="4.5" class="point"/>
  <circle cx="240" cy="80" r="4.5" class="point"/>
  <circle cx="240" cy="200" r="4" class="point"/>

  <!-- 文字与坐标标注 -->
  <text x="90" y="225" class="text-sm">A(1,2)</text>
  <text x="265" y="75" class="text-sm">B(3,4)</text>
  <text x="255" y="220" class="text-sm">P</text>
  <text x="175" y="120" class="text-sm">F</text>
""".replace("{theme['fg']}", theme["fg"])
    return make_svg(400, 360, content, theme)

def gen_1990_q02(theme):
    content = """
  <line x1="30" y1="150" x2="330" y2="150" class="axis" marker-end="url(#arrow)"/>
  <line x1="60" y1="270" x2="60" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="325" y="175" class="text">x</text>
  <text x="45" y="40" class="text">y</text>
  <text x="48" y="168" class="text">O</text>
  <polygon points="60,150 240,60 240,240" class="shade"/>
  <line x1="60" y1="150" x2="270" y2="45" class="curve"/>
  <line x1="60" y1="150" x2="270" y2="255" class="curve"/>
  <line x1="240" y1="40" x2="240" y2="260" class="curve-dashed"/>
  <text x="240" y="170" class="text-sm">1</text>
  <text x="280" y="55" class="text-sm">y = x</text>
  <text x="280" y="250" class="text-sm">y = -x</text>
  <text x="160" y="155" class="text">D</text>
"""
    return make_svg(360, 300, content, theme)

# 1991
def gen_1991_q01(theme):
    content = """
  <line x1="30" y1="150" x2="330" y2="150" class="axis" marker-end="url(#arrow)"/>
  <line x1="180" y1="270" x2="180" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="325" y="175" class="text">x</text>
  <text x="165" y="40" class="text">y</text>
  <text x="168" y="168" class="text">O</text>
  <polygon points="80,250 80,50 280,50" class="shade"/>
  <polygon points="180,150 180,50 280,50" class="plane1"/>
  <line x1="80" y1="250" x2="80" y2="50" class="curve"/>
  <line x1="80" y1="50" x2="280" y2="50" class="curve"/>
  <line x1="80" y1="250" x2="280" y2="50" class="curve"/>
  <circle cx="80" cy="250" r="3.5" class="point"/>
  <circle cx="80" cy="50" r="3.5" class="point"/>
  <circle cx="280" cy="50" r="3.5" class="point"/>
  <text x="55" y="260" class="text-xs">(-1,-1)</text>
  <text x="55" y="45" class="text-xs">(-1,1)</text>
  <text x="295" y="45" class="text-xs">(1,1)</text>
  <text x="215" y="95" class="text">D₁</text>
  <text x="130" y="110" class="text">D</text>
"""
    return make_svg(360, 300, content, theme)

# 2001
def gen_2001_q01_stem(theme):
    content = """
  <line x1="30" y1="150" x2="330" y2="150" class="axis" marker-end="url(#arrow)"/>
  <line x1="180" y1="270" x2="180" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="325" y="175" class="text">x</text>
  <text x="165" y="40" class="text">y</text>
  <text x="168" y="168" class="text">O</text>
  <path d="M 50 250 C 120 230, 160 190, 180 150 C 200 110, 240 70, 310 50" class="curve"/>
  <text x="290" y="80" class="text-sm">y = f(x)</text>
"""
    return make_svg(360, 300, content, theme)

def gen_2001_q01_opt_a(theme):
    content = """
  <line x1="20" y1="150" x2="220" y2="150" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="120" y1="190" x2="120" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="170" class="text-sm">x</text>
  <text x="105" y="30" class="text-sm">y</text>
  <path d="M 30 145 C 80 140, 100 50, 120 50 C 140 50, 160 140, 210 145" class="curve"/>
"""
    return make_svg(240, 200, content, theme)

def gen_2001_q01_opt_b(theme):
    content = """
  <line x1="20" y1="150" x2="220" y2="150" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="120" y1="190" x2="120" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="170" class="text-sm">x</text>
  <text x="105" y="30" class="text-sm">y</text>
  <path d="M 30 50 C 80 130, 100 140, 120 140 C 140 140, 160 130, 210 50" class="curve"/>
"""
    return make_svg(240, 200, content, theme)

def gen_2001_q01_opt_c(theme):
    content = """
  <line x1="20" y1="150" x2="220" y2="150" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="120" y1="190" x2="120" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="170" class="text-sm">x</text>
  <text x="105" y="30" class="text-sm">y</text>
  <path d="M 30 170 C 80 160, 100 150, 120 150 C 140 150, 160 60, 210 40" class="curve"/>
"""
    return make_svg(240, 200, content, theme)

def gen_2001_q01_opt_d(theme):
    content = """
  <line x1="20" y1="150" x2="220" y2="150" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="120" y1="190" x2="120" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="170" class="text-sm">x</text>
  <text x="105" y="30" class="text-sm">y</text>
  <path d="M 30 40 C 80 60, 100 150, 120 150 C 140 150, 160 160, 210 170" class="curve"/>
"""
    return make_svg(240, 200, content, theme)

# 2002
def gen_2002_q04_opt_a(theme):
    content = """
  <polygon points="30,140 150,140 190,90 70,90" class="plane1"/>
  <polygon points="30,140 70,90 110,30 70,80" class="plane2"/>
  <polygon points="150,140 190,90 150,30 110,80" class="plane3"/>
  <text x="110" y="175" class="text-sm">A (三棱柱两两相交)</text>
"""
    return make_svg(220, 190, content, theme)

def gen_2002_q04_opt_b(theme):
    content = """
  <polygon points="30,60 150,60 190,30 70,30" class="plane1"/>
  <polygon points="30,130 150,130 190,100 70,100" class="plane1"/>
  <polygon points="60,150 140,150 180,20 100,20" class="plane2"/>
  <text x="110" y="175" class="text-sm">B (两平行一相交)</text>
"""
    return make_svg(220, 190, content, theme)

def gen_2002_q04_opt_c(theme):
    content = """
  <line x1="110" y1="20" x2="110" y2="150" class="curve" stroke-width="2.5"/>
  <polygon points="30,50 110,20 110,150 30,180" class="plane1"/>
  <polygon points="50,85 110,20 110,150 170,85" class="plane2"/>
  <polygon points="190,50 110,20 110,150 190,180" class="plane3"/>
  <text x="110" y="175" class="text-sm">C (共线相交)</text>
"""
    return make_svg(220, 190, content, theme)

def gen_2002_q04_opt_d(theme):
    content = """
  <polygon points="30,50 150,50 190,20 70,20" class="plane1"/>
  <polygon points="30,95 150,95 190,65 70,65" class="plane2"/>
  <polygon points="30,140 150,140 190,110 70,110" class="plane3"/>
  <text x="110" y="175" class="text-sm">D (三平面平行)</text>
"""
    return make_svg(220, 190, content, theme)

# 2003
def gen_2003_q01(theme):
    content = """
  <line x1="40" y1="140" x2="380" y2="140" class="axis" marker-end="url(#arrow)"/>
  <line x1="160" y1="240" x2="160" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="375" y="165" class="text">x</text>
  <text x="145" y="40" class="text">y</text>
  <text x="145" y="158" class="text">O</text>
  <path d="M 60 40 C 90 90, 110 140, 120 140 C 130 140, 140 180, 160 140 C 180 100, 200 90, 220 90 C 240 90, 260 140, 280 140 C 300 140, 330 180, 360 180" class="curve"/>
  <circle cx="120" cy="140" r="3.5" class="point"/>
  <circle cx="160" cy="140" r="3.5" class="point"/>
  <circle cx="280" cy="140" r="3.5" class="point"/>
  <text x="115" y="160" class="text-sm">x₁</text>
  <text x="280" y="160" class="text-sm">x₂</text>
  <text x="340" y="90" class="text">y = f'(x)</text>
"""
    return make_svg(420, 260, content, theme)

# 2005
def gen_2005_q17(theme):
    content = """
  <line x1="30" y1="260" x2="350" y2="260" class="axis" marker-end="url(#arrow)"/>
  <line x1="60" y1="290" x2="60" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="345" y="285" class="text">x</text>
  <text x="45" y="40" class="text">y</text>
  <text x="48" y="278" class="text">O</text>
  <line x1="60" y1="260" x2="210" y2="10" class="curve-dashed"/>
  <line x1="160" y1="20" x2="270" y2="220" class="curve-dashed"/>
  <path d="M 60 260 C 100 180, 140 70, 180 85 C 210 95, 230 130, 240 160 C 255 200, 280 230, 310 240" class="curve"/>
  <circle cx="60" cy="260" r="3.5" class="point"/>
  <circle cx="180" cy="60" r="4" class="point"/>
  <circle cx="240" cy="160" r="4" class="point"/>
  <text x="180" y="45" class="text-sm">(2,4)</text>
  <text x="265" y="160" class="text-sm">(3,2)</text>
  <text x="130" y="100" class="text-sm">l₁</text>
  <text x="245" y="70" class="text-sm">l₂</text>
  <text x="290" y="220" class="text">C</text>
"""
    return make_svg(380, 320, content, theme)

# 2007
def gen_2007_q03(theme):
    content = """
  <line x1="30" y1="140" x2="430" y2="140" class="axis" marker-end="url(#arrow)"/>
  <line x1="230" y1="240" x2="230" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="425" y="165" class="text">t</text>
  <text x="215" y="40" class="text">y</text>
  <text x="218" y="158" class="text">O</text>
  <path d="M 50 140 A 30 30 0 0 1 110 140" class="curve"/>
  <path d="M 110 140 A 60 60 0 0 0 230 140" class="curve"/>
  <path d="M 230 140 A 60 60 0 0 1 350 140" class="curve"/>
  <path d="M 350 140 A 30 30 0 0 0 410 140" class="curve"/>
  <text x="50" y="160" class="text-sm">-3</text>
  <text x="110" y="160" class="text-sm">-2</text>
  <text x="350" y="160" class="text-sm">2</text>
  <text x="410" y="160" class="text-sm">3</text>
  <text x="380" y="70" class="text">y = f(t)</text>
"""
    return make_svg(460, 260, content, theme)

# 2008
def gen_2008_q07(theme):
    content = """
  <line x1="180" y1="160" x2="180" y2="20" class="axis" marker-end="url(#arrow)"/>
  <line x1="180" y1="160" x2="330" y2="160" class="axis" marker-end="url(#arrow)"/>
  <line x1="180" y1="160" x2="70" y2="250" class="axis" marker-end="url(#arrow)"/>
  <text x="195" y="30" class="text">z</text>
  <text x="325" y="185" class="text">y</text>
  <text x="60" y="260" class="text">x</text>
  <text x="168" y="175" class="text">O</text>
  <path d="M 120 40 C 140 100, 160 110, 180 110 C 200 110, 220 100, 240 40" class="curve"/>
  <ellipse cx="180" cy="40" rx="60" ry="15" class="curve-dashed"/>
  <path d="M 120 280 C 140 220, 160 210, 180 210 C 200 210, 220 220, 240 280" class="curve"/>
  <ellipse cx="180" cy="280" rx="60" ry="15" class="curve-dashed"/>
"""
    return make_svg(360, 320, content, theme)

# 2009
def gen_2009_q03_stem(theme):
    content = """
  <line x1="30" y1="160" x2="330" y2="160" class="axis" marker-end="url(#arrow)"/>
  <line x1="100" y1="260" x2="100" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="325" y="185" class="text">x</text>
  <text x="85" y="40" class="text">y</text>
  <text x="88" y="178" class="text">O</text>
  <line x1="50" y1="210" x2="100" y2="160" class="curve"/>
  <line x1="100" y1="110" x2="150" y2="110" class="curve"/>
  <line x1="150" y1="110" x2="250" y2="210" class="curve"/>
  <circle cx="50" cy="210" r="3.5" class="point"/>
  <circle cx="100" cy="110" r="3.5" class="point"/>
  <circle cx="150" cy="110" r="3.5" class="point"/>
  <circle cx="250" cy="210" r="3.5" class="point"/>
  <text x="50" y="150" class="text-sm">-1</text>
  <text x="150" y="180" class="text-sm">1</text>
  <text x="200" y="180" class="text-sm">2</text>
  <text x="250" y="180" class="text-sm">3</text>
  <text x="270" y="120" class="text">y = f(x)</text>
"""
    return make_svg(360, 290, content, theme)

def gen_2009_q03_opt_a(theme):
    content = """
  <line x1="20" y1="120" x2="220" y2="120" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="70" y1="180" x2="70" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="138" class="text-sm">x</text>
  <text x="55" y="30" class="text-sm">y</text>
  <path d="M 30 150 Q 50 120 70 120 L 110 80 Q 150 50 190 100" class="curve"/>
"""
    return make_svg(240, 190, content, theme)

def gen_2009_q03_opt_b(theme):
    content = """
  <line x1="20" y1="120" x2="220" y2="120" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="70" y1="180" x2="70" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="138" class="text-sm">x</text>
  <text x="55" y="30" class="text-sm">y</text>
  <path d="M 30 150 Q 50 130 70 120 L 110 70 Q 150 40 190 70" class="curve"/>
"""
    return make_svg(240, 190, content, theme)

def gen_2009_q03_opt_c(theme):
    content = """
  <line x1="20" y1="120" x2="220" y2="120" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="70" y1="180" x2="70" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="138" class="text-sm">x</text>
  <text x="55" y="30" class="text-sm">y</text>
  <path d="M 30 100 Q 50 120 70 120 L 110 80 Q 150 60 190 130" class="curve"/>
"""
    return make_svg(240, 190, content, theme)

def gen_2009_q03_opt_d(theme):
    content = """
  <line x1="20" y1="120" x2="220" y2="120" class="axis" marker-end="url(#arrow-sm)"/>
  <line x1="70" y1="180" x2="70" y2="20" class="axis" marker-end="url(#arrow-sm)"/>
  <text x="215" y="138" class="text-sm">x</text>
  <text x="55" y="30" class="text-sm">y</text>
  <path d="M 30 100 Q 50 110 70 120 L 110 70 Q 150 40 190 100" class="curve"/>
"""
    return make_svg(240, 190, content, theme)

# 2015
def gen_2015_q01(theme):
    content = """
  <line x1="40" y1="140" x2="380" y2="140" class="axis" marker-end="url(#arrow)"/>
  <line x1="210" y1="240" x2="210" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="375" y="165" class="text">x</text>
  <text x="195" y="40" class="text">y</text>
  <text x="198" y="158" class="text">O</text>
  <path d="M 60 210 C 90 140, 110 90, 130 140 C 150 190, 180 190, 210 140 C 240 90, 270 90, 290 140 C 310 190, 330 140, 360 70" class="curve"/>
  <circle cx="130" cy="140" r="3.5" class="point"/>
  <circle cx="210" cy="140" r="3.5" class="point"/>
  <circle cx="290" cy="140" r="3.5" class="point"/>
  <text x="125" y="160" class="text-sm">-1</text>
  <text x="290" y="160" class="text-sm">1</text>
  <text x="340" y="55" class="text">y = f''(x)</text>
"""
    return make_svg(420, 260, content, theme)

# 2017
def gen_2017_q03(theme):
    content = """
  <line x1="40" y1="200" x2="400" y2="200" class="axis" marker-end="url(#arrow)"/>
  <line x1="60" y1="220" x2="60" y2="30" class="axis" marker-end="url(#arrow)"/>
  <text x="395" y="225" class="text">t</text>
  <text x="45" y="40" class="text">v</text>
  <text x="48" y="215" class="text">O</text>
  <path d="M 60 160 C 100 130, 130 110, 150 110 C 130 130, 100 170, 60 200 Z" class="shade"/>
  <text x="110" y="150" class="text-sm">S₁=10</text>
  <text x="210" y="125" class="text-sm">S₂=20</text>
  <text x="310" y="95" class="text-sm">S₃=3</text>
  <path d="M 60 160 C 120 110, 200 90, 360 80" class="curve"/>
  <path d="M 60 200 C 140 180, 220 70, 360 95" class="curve-dashed"/>
  <text x="380" y="75" class="text-sm">v₁(t)</text>
  <text x="380" y="110" class="text-sm">v₂(t)</text>
"""
    return make_svg(440, 260, content, theme)

# 2024
def deploy_svg(year, filename, generator):
    ydir = os.path.join(ARCHIVE_ROOT, f"{year}年真题")
    assets_dir = os.path.join(ydir, "assets")
    light_dir = os.path.join(assets_dir, "light")
    os.makedirs(assets_dir, exist_ok=True)
    os.makedirs(light_dir, exist_ok=True)
    
    dark_svg = generator(DARK_THEME)
    with open(os.path.join(assets_dir, filename), "w", encoding="utf-8") as f:
        f.write(dark_svg)
        
    light_svg = generator(LIGHT_THEME)
    with open(os.path.join(light_dir, filename), "w", encoding="utf-8") as f:
        f.write(light_svg)

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="显式重生成 Math1 legacy direct-SVG 资产；TikZ-backed Canonical Asset 不在此范围。"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="确认重生成全部 legacy direct-SVG 暗/亮双主题资产",
    )
    args = parser.parse_args(argv)
    if not args.all:
        parser.error("这是写操作；请显式传入 --all。查看说明可使用 --help。")

    print("=" * 60)
    print(" 生成 Math1 legacy direct-SVG 资产 (暗色 + 亮色)")
    print("=" * 60)

    deploy_svg(1990, "q01_force_semicircle.svg", gen_1990_q01)
    deploy_svg(1990, "q02_random_var_triangle.svg", gen_1990_q02)
    deploy_svg(1991, "q01_triangle_integral.svg", gen_1991_q01)
    deploy_svg(2001, "q01_f_graph.svg", gen_2001_q01_stem)
    deploy_svg(2001, "q01_opt_a.svg", gen_2001_q01_opt_a)
    deploy_svg(2001, "q01_opt_b.svg", gen_2001_q01_opt_b)
    deploy_svg(2001, "q01_opt_c.svg", gen_2001_q01_opt_c)
    deploy_svg(2001, "q01_opt_d.svg", gen_2001_q01_opt_d)
    deploy_svg(2002, "q04_opt_a.svg", gen_2002_q04_opt_a)
    deploy_svg(2002, "q04_opt_b.svg", gen_2002_q04_opt_b)
    deploy_svg(2002, "q04_opt_c.svg", gen_2002_q04_opt_c)
    deploy_svg(2002, "q04_opt_d.svg", gen_2002_q04_opt_d)
    deploy_svg(2003, "q01_df_graph.svg", gen_2003_q01)
    deploy_svg(2005, "q01_inflection_tangents.svg", gen_2005_q17)
    deploy_svg(2007, "q01_semicircle_integral.svg", gen_2007_q03)
    deploy_svg(2008, "q01_two_sheet_hyperboloid.svg", gen_2008_q07)
    deploy_svg(2009, "q01_f_graph.svg", gen_2009_q03_stem)
    deploy_svg(2009, "q02_opt_a.svg", gen_2009_q03_opt_a)
    deploy_svg(2009, "q03_opt_b.svg", gen_2009_q03_opt_b)
    deploy_svg(2009, "q04_opt_c.svg", gen_2009_q03_opt_c)
    deploy_svg(2009, "q05_opt_d.svg", gen_2009_q03_opt_d)
    deploy_svg(2015, "q01_d2f_inflection.svg", gen_2015_q01)
    deploy_svg(2017, "q01_speed_curves.svg", gen_2017_q03)

    # 2024 Q5 已迁移为 TikZ-backed Canonical Asset：
    # assets/src/q05_three_planes_pencil.tex -> infra/scripts/compile_tikz_to_svg.py
    # 这里不得再生成第二份 q01/q05 SVG Owner，更不得覆盖 Canonical q05 资产。

    print(" 23 组 legacy direct-SVG 资产 (共 46 文件) 全部生成完毕。")

if __name__ == "__main__":
    main()
