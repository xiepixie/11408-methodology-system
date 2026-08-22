#!/usr/bin/env python3
"""Repository-wide steady-state gate orchestrator.

This file owns no domain rule. It only runs each Canonical Domain gate so a
maintainer can prove the repository is structurally healthy with one command.
The actual invariants remain owned by infra/, teaching/, and kaoyan/.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse


REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Gate:
    name: str
    command: tuple[str, ...]


REQUIRED_ROOT_PATHS = (
    REPO_ROOT / "AGENTS.md",
    REPO_ROOT / "README.md",
    REPO_ROOT / "infra" / "README.md",
    REPO_ROOT / "teaching" / "README.md",
    REPO_ROOT / "teaching" / "AGENTS.md",
    REPO_ROOT / "kaoyan" / "README.md",
    REPO_ROOT / "kaoyan" / "AGENTS.md",
)
RETIRED_ROOTS = (
    REPO_ROOT / "common",
    REPO_ROOT / "408_Exam_Archive",
    REPO_ROOT / "Math1_Exam_Archive",
    REPO_ROOT / "408_CodeBrick_Notes",
)
ROUTER_DOCS = (
    REPO_ROOT / "README.md",
    REPO_ROOT / "infra" / "README.md",
    REPO_ROOT / "11408 Methodology System.md",
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


HARD_GATES = (
    Gate("Infra", (sys.executable, "infra/check_infra.py")),
    Gate("Teaching", (sys.executable, "teaching/check_teaching.py", "--compile")),
    Gate(
        "Kaoyan unit tests",
        (sys.executable, "-m", "unittest", "discover", "-s", "kaoyan/00_system/tests", "-p", "test_*.py"),
    ),
    Gate("Kaoyan hard check", (sys.executable, "kaoyan/00_system/cognitive_system.py", "check")),
    Gate("Kaoyan Handbook template", (sys.executable, "kaoyan/00_system/check_handbook_template.py")),
    Gate(
        "408 Archive",
        (sys.executable, "kaoyan/00_system/tools/validate_exam_archive_spec.py", "--exam", "408", "--quiet"),
    ),
    Gate(
        "Math1 Archive",
        (sys.executable, "kaoyan/00_system/tools/validate_exam_archive_spec.py", "--exam", "math1", "--quiet"),
    ),
    Gate("Math1 Canonical Source", (sys.executable, "kaoyan/00_system/tools/check_math1_exam_source.py", "--quiet")),
    Gate(
        "English Daily Reading",
        (
            sys.executable,
            "kaoyan/20_英语一/10_阅读/daily_reading/00_system/tools/check_daily_reading.py",
            "--smoke",
        ),
    ),
)


def check_root_wiring() -> bool:
    print("\n" + "=" * 88, flush=True)
    print("[REPO GATE] Root wiring", flush=True)
    print("=" * 88, flush=True)
    errors: list[str] = []

    for path in REQUIRED_ROOT_PATHS:
        if not path.exists():
            errors.append(f"Missing root/domain router: {path.relative_to(REPO_ROOT)}")

    for retired in RETIRED_ROOTS:
        if retired.is_dir() and any(path.is_file() for path in retired.rglob("*")):
            errors.append(f"Retired root contains active files: {retired.relative_to(REPO_ROOT)}/")

    for doc in ROUTER_DOCS:
        if not doc.is_file():
            continue
        text = doc.read_text(encoding="utf-8")
        for raw_link in MARKDOWN_LINK_RE.findall(text):
            parsed = urlparse(raw_link)
            if parsed.scheme or raw_link.startswith("#"):
                continue
            target_text = unquote(parsed.path)
            if not target_text:
                continue
            target = (doc.parent / target_text).resolve()
            if not target.exists():
                errors.append(f"Broken router link: {doc.relative_to(REPO_ROOT)} -> {raw_link}")

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")
        print("[FAIL] Root wiring")
        return False
    print("[PASS] Root wiring")
    return True


def run_gate(gate: Gate) -> bool:
    print("\n" + "=" * 88, flush=True)
    print(f"[REPO GATE] {gate.name}", flush=True)
    print("=" * 88, flush=True)
    result = subprocess.run(gate.command, cwd=REPO_ROOT)
    if result.returncode == 0:
        print(f"[PASS] {gate.name}")
        return True
    print(f"[FAIL] {gate.name} (exit {result.returncode})")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all Canonical repository hard gates.")
    parser.add_argument(
        "--audit",
        action="store_true",
        help="after hard gates, also print the non-blocking Kaoyan maintenance audit",
    )
    args = parser.parse_args()

    failures: list[str] = []
    if not check_root_wiring():
        failures.append("Root wiring")

    for gate in HARD_GATES:
        if not run_gate(gate):
            failures.append(gate.name)

    if args.audit:
        print("\n" + "=" * 88, flush=True)
        print("[NON-BLOCKING AUDIT] Kaoyan maintenance debt", flush=True)
        print("=" * 88, flush=True)
        subprocess.run(
            [sys.executable, "kaoyan/00_system/cognitive_system.py", "audit"],
            cwd=REPO_ROOT,
            check=False,
        )

    print("\n" + "=" * 88)
    if failures:
        print("REPOSITORY GATE: FAILED")
        print("Failed domains: " + ", ".join(failures))
        return 1
    print("REPOSITORY GATE: PASSED")
    print(f"{len(HARD_GATES) + 1} canonical hard gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
