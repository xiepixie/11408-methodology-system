#!/usr/bin/env python3
r"""I.P.A.R.A shared LaTeX build engine.

This module owns only domain-agnostic compilation mechanics:
- multi-pass XeLaTeX execution;
- shared TeX search-path setup;
- diagnostic parsing;
- optional explicit output handoff;
- auxiliary-file cleanup.

Domain policy (for example "a Kaoyan Handbook must publish into 90_publish/")
belongs to the caller and is expressed via ``--publish-dir``. The compiler does
not infer a business domain from the source path.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

AUX_EXTENSIONS = {
    ".aux", ".log", ".out", ".toc", ".synctex", ".synctex.gz", ".xdv",
    ".fls", ".fdb_latexmk", ".nav", ".snm", ".vrb", ".bbl", ".blg",
}

REPO_ROOT = Path(__file__).resolve().parents[2]
LATEX_ROOT = REPO_ROOT / "infra" / "latex"


def clean_aux_files(directory: Path, verbose: bool = True) -> int:
    """Remove generated LaTeX helper files below ``directory``."""
    count = 0
    for root, _, files in os.walk(directory):
        for filename in files:
            path = Path(root) / filename
            if path.suffix in AUX_EXTENSIONS or "synctex" in path.name:
                try:
                    path.unlink()
                    count += 1
                    if verbose:
                        print(f"  [clean] {path.relative_to(directory)}")
                except OSError as exc:
                    print(f"  [warn] cannot remove {path}: {exc}")
    return count


def inspect_log_output(output: str) -> dict[str, object]:
    """Extract fatal diagnostics, warnings and page count from XeLaTeX output."""
    warnings: list[str] = []
    errors: list[str] = []
    page_count: int | None = None

    for line in output.splitlines():
        stripped = line.strip()
        if line.startswith("!") or "Error" in line:
            errors.append(stripped)
        elif "Warning:" in line or "undefined" in line.lower() or "Rerun" in line:
            warnings.append(stripped)

        match = re.search(r"Output written on .*?\((\d+)\s+pages?", line)
        if match:
            page_count = int(match.group(1))

    # Long Unicode paths can make XeLaTeX wrap the "Output written on ..."
    # record across lines.  Keep the cheap per-line parse above, then fall back
    # to a whole-output match so page-count policy gates remain trustworthy.
    if page_count is None:
        match = re.search(r"Output written on[\s\S]*?\((\d+)\s+pages?", output)
        if match:
            page_count = int(match.group(1))

    return {"page_count": page_count, "errors": errors, "warnings": warnings}


def build_environment(target_dir: Path) -> dict[str, str]:
    """Build a domain-neutral TEXINPUTS search path.

    ``infra/latex`` is the global design-system owner. ``REPO_ROOT`` allows
    canonical sources to address repository-relative assets. ``kaoyan`` is
    included for handbook compatibility layer resolution. Any caller-provided
    TEXINPUTS is preserved.
    """
    env = os.environ.copy()
    existing = env.get("TEXINPUTS", "")
    roots = [target_dir, LATEX_ROOT, REPO_ROOT / "kaoyan", REPO_ROOT]
    env["TEXINPUTS"] = ".:" + ":".join(str(path) for path in roots) + f":{existing}:"
    return env


def compile_single_tex(
    tex_path: Path,
    *,
    keep_aux: bool = False,
    publish_dir: Path | None = None,
    warnings_as_errors: bool = False,
) -> bool:
    """Compile one TeX source and optionally hand the PDF to an explicit directory."""
    tex_path = tex_path.resolve()
    if not tex_path.is_file() or tex_path.suffix != ".tex":
        print(f"[error] not a TeX file: {tex_path}")
        return False

    target_dir = tex_path.parent
    local_pdf = target_dir / f"{tex_path.stem}.pdf"
    env = build_environment(target_dir)

    print("\n==========================================")
    print(f"[compile] {tex_path}")
    print("==========================================")

    # Compile into an isolated build directory.  A validation/publish run must
    # never delete or overwrite a repository PDF merely because --publish-dir
    # was supplied.  Relative \input/\includegraphics resolution still uses the
    # source directory as cwd; only generated TeX state is redirected.
    with tempfile.TemporaryDirectory(prefix="ipara-xelatex-", delete=not keep_aux) as build_tmp:
        build_dir = Path(build_tmp)
        generated_pdf = build_dir / f"{tex_path.stem}.pdf"
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            f"-output-directory={build_dir}",
            tex_path.name,
        ]

        final_info: dict[str, object] | None = None
        for pass_no in (1, 2, 3):
            if pass_no == 3 and final_info is not None:
                warnings = final_info["warnings"]
                assert isinstance(warnings, list)
                if not any("Rerun" in warning or "undefined" in warning.lower() for warning in warnings):
                    break

            print(f"[pass {pass_no}/3] xelatex")
            result = subprocess.run(
                command,
                cwd=target_dir,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            final_info = inspect_log_output(result.stdout)
            errors = final_info["errors"]
            assert isinstance(errors, list)
            if result.returncode != 0 or errors:
                print(f"[error] XeLaTeX pass {pass_no} failed")
                for error in errors[:10]:
                    print(f"  {error}")
                return False

        assert final_info is not None
        if not generated_pdf.is_file():
            print(f"[error] compiler returned success but PDF is missing: {generated_pdf}")
            return False

        page_count = final_info["page_count"]
        page_text = f"{page_count} pages" if page_count is not None else "page count unknown"
        print(f"[ok] compiled: {tex_path} ({page_text})")

        warnings = final_info["warnings"]
        assert isinstance(warnings, list)
        if warnings_as_errors and warnings:
            print("[error] final-pass LaTeX warnings are forbidden in strict mode")
            for warning in warnings[:12]:
                print(f"  {warning}")
            return False

        if publish_dir is not None:
            publish_dir = publish_dir.resolve()
            publish_dir.mkdir(parents=True, exist_ok=True)
            target_pdf = publish_dir / generated_pdf.name
            if target_pdf.exists():
                target_pdf.unlink()
            shutil.copy2(generated_pdf, target_pdf)
            print(f"[handoff] {target_pdf}")
        else:
            shutil.copy2(generated_pdf, local_pdf)
            print(f"[output] {local_pdf}")

        if warnings:
            print("[warnings]")
            for warning in warnings[:8]:
                print(f"  {warning}")

    if keep_aux:
        print(f"[keep-aux] isolated build state retained at {build_dir}")
    else:
        print("[clean] isolated build state removed; source directory untouched")

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="I.P.A.R.A shared XeLaTeX build engine")
    parser.add_argument("paths", nargs="*", help="TeX files or directories containing TeX files")
    parser.add_argument("--clean-all", action="store_true", help="clean LaTeX auxiliary files below repository root")
    parser.add_argument("--keep-aux", action="store_true", help="keep auxiliary files after compilation")
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="fail before PDF handoff if the final XeLaTeX pass still reports warnings",
    )
    parser.add_argument(
        "--publish-dir",
        "--outdir",
        type=Path,
        dest="publish_dir",
        help="explicit PDF handoff directory; domain policy must be supplied by the caller",
    )
    args = parser.parse_args()

    if args.clean_all:
        print(f"[clean-all] {REPO_ROOT}")
        print(f"[ok] removed {clean_aux_files(REPO_ROOT)} auxiliary files")
        return 0

    if not args.paths:
        parser.print_help()
        return 1

    all_success = True
    for raw_path in args.paths:
        path = Path(raw_path).resolve()
        if path.is_dir():
            tex_files = sorted(path.glob("**/*.tex"))
            print(f"[scan] {path}: {len(tex_files)} TeX files")
            for tex_file in tex_files:
                all_success &= compile_single_tex(
                    tex_file,
                    keep_aux=args.keep_aux,
                    publish_dir=args.publish_dir,
                    warnings_as_errors=args.warnings_as_errors,
                )
        else:
            all_success &= compile_single_tex(
                path,
                keep_aux=args.keep_aux,
                publish_dir=args.publish_dir,
                warnings_as_errors=args.warnings_as_errors,
            )

    return 0 if all_success else 1


if __name__ == "__main__":
    sys.exit(main())
