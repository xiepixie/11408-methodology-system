#!/usr/bin/env python3
r"""
LaTeX 自动化编译与清理工具 (compile_tex.py)

功能：
1. 自动进行多遍编译（Double/Triple Pass），确保 \zpageref{LastPage}、目录与交叉引用页码 100% 准确。
2. 捕获并解析 xelatex 日志中的 Warning、Error 与 Undefined References，防止静默吞掉报错。
3. 编译成功后自动清理该目录下所有临时辅助文件（.aux, .log, .out, .toc, .synctex 等）。
4. 支持全局清理模式 (--clean-all)。

用法示例：
  - 编译指定文件：
      python3 common/scripts/compile_tex.py "common/templates/一对一错题课_教案模板.tex"
  - 全局清理编译临时文件：
      python3 common/scripts/compile_tex.py --clean-all
"""

import sys
import os
import argparse
import subprocess
import re
from pathlib import Path

# LaTeX 辅助临时文件后缀
AUX_EXTENSIONS = {
    ".aux", ".log", ".out", ".toc", ".synctex", ".synctex.gz",
    ".fls", ".fdb_latexmk", ".nav", ".snm", ".vrb", ".bbl", ".blg"
}

def clean_aux_files(directory: Path, verbose: bool = True) -> int:
    """递归清理指定目录下的所有 LaTeX 辅助临时文件"""
    count = 0
    for root, _, files in os.walk(directory):
        for f in files:
            p = Path(root) / f
            if p.suffix in AUX_EXTENSIONS or "synctex" in p.name:
                try:
                    p.unlink()
                    count += 1
                    if verbose:
                        print(f"  [清理临时文件] {p.relative_to(directory)}")
                except Exception as e:
                    print(f"  ⚠️ 无法删除 {p}: {e}")
    return count

def inspect_log_output(output: str) -> dict:
    """解析 xelatex 输出，提取页码、错误与警告信息"""
    lines = output.splitlines()
    warnings = []
    errors = []
    page_count = None

    for line in lines:
        if line.startswith("!") or "Error" in line:
            errors.append(line.strip())
        elif "Warning:" in line or "undefined" in line.lower() or "Rerun" in line:
            warnings.append(line.strip())
        
        m = re.search(r"Output written on .*?\((\d+)\s+pages?", line)
        if m:
            page_count = int(m.group(1))

    return {
        "page_count": page_count,
        "errors": errors,
        "warnings": warnings
    }

def compile_single_tex(tex_path: Path, keep_aux: bool = False) -> bool:
    """编译单文件：自动多遍 xelatex 编译，确保页码与引用正确"""
    if not tex_path.is_file() or tex_path.suffix != ".tex":
        print(f"❌ 错误: 文件不存在或不是 .tex 文件 -> {tex_path}")
        return False

    target_dir = tex_path.parent
    file_name = tex_path.name
    pdf_name = tex_path.stem + ".pdf"
    pdf_path = target_dir / pdf_name

    print(f"\n==========================================")
    print(f"📄 开始编译: {tex_path}")
    print(f"==========================================")

    cmd = [
        "xelatex",
        "-interaction=nonstopmode",
        file_name
    ]

    # 第 1 次编译
    print("⏳ [Pass 1/3] 正在进行第 1 次 xelatex 编译...")
    res1 = subprocess.run(cmd, cwd=target_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    info1 = inspect_log_output(res1.stdout)

    if res1.returncode != 0 or info1["errors"]:
        print(f"❌ 第 1 次编译失败！错误信息：")
        for err in info1["errors"][:10]:
            print(f"   {err}")
        return False

    # 第 2 次编译
    print("⏳ [Pass 2/3] 正在进行第 2 次 xelatex 编译（写入交叉引用与总页数）...")
    res2 = subprocess.run(cmd, cwd=target_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    info2 = inspect_log_output(res2.stdout)

    # 检查是否仍有未决引用，必要时执行 Pass 3
    need_pass3 = any("Rerun" in w or "undefined" in w.lower() for w in info2["warnings"])
    if need_pass3:
        print("⏳ [Pass 3/3] 检测到未决引用，正在执行第 3 次 xelatex 编译...")
        res3 = subprocess.run(cmd, cwd=target_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        info2 = inspect_log_output(res3.stdout)

    # 检查最终编译状态
    if info2["errors"]:
        print(f"❌ 编译失败！关键错误：")
        for err in info2["errors"][:10]:
            print(f"   {err}")
        return False

    pages_str = f"{info2['page_count']} 页" if info2['page_count'] else "未知"
    print(f"✅ 编译成功！输出文件: {pdf_path} (共 {pages_str})")

    if info2["warnings"]:
        print("⚠️ 编译提示信息：")
        for w in info2["warnings"][:5]:
            print(f"   • {w}")

    # 清理当前目录下的临时文件
    if not keep_aux:
        print("🧹 自动清理临时辅助文件...")
        cleaned = clean_aux_files(target_dir, verbose=False)
        print(f"✨ 已清理 {cleaned} 个临时文件 (保持目录干净)")

    return True

def main():
    parser = argparse.ArgumentParser(description="LaTeX 自动化多遍编译与清理工具")
    parser.add_argument("paths", nargs="*", help="要编译的 .tex 文件或包含 .tex 的目录路径")
    parser.add_argument("--clean-all", action="store_true", help="递归清理整个项目工作区的所有辅助临时文件")
    parser.add_argument("--keep-aux", action="store_true", help="保留编译产生的辅助文件（不自动清理）")
    
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent.parent

    if args.clean_all:
        print(f"🧹 开始全项目递归清理 LaTeX 临时辅助文件 ({project_root})...")
        count = clean_aux_files(project_root, verbose=True)
        print(f"🎉 全局清理完成，共移除 {count} 个临时文件！")
        return

    if not args.paths:
        parser.print_help()
        sys.exit(1)

    all_success = True
    for p_str in args.paths:
        p = Path(p_str).resolve()
        if p.is_dir():
            tex_files = sorted(p.glob("**/*.tex"))
            print(f"🔍 在目录 {p} 中找到 {len(tex_files)} 个 .tex 文件")
            for tf in tex_files:
                success = compile_single_tex(tf, keep_aux=args.keep_aux)
                if not success:
                    all_success = False
        else:
            success = compile_single_tex(p, keep_aux=args.keep_aux)
            if not success:
                all_success = False

    if not all_success:
        sys.exit(1)

if __name__ == "__main__":
    main()
