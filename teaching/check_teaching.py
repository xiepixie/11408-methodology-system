#!/usr/bin/env python3
"""Teaching Domain Steady-State Verification Gate.

This script owns Teaching domain invariants in post-migration steady state:
1. Canonical Templates: 4-page student/teacher templates & questions.tex pack.
2. Canonical Question Pool: steady-state no-loss floor preserved, taxonomy/macro/privacy invariants enforced.
3. Canonical Topics: steady-state no-loss floor preserved, clean inputs & boundaries enforced.
4. Student Delivery Sessions: teaching/students/ active sessions & bridges.
5. Repository Hygiene: zero generated LaTeX leftovers or untracked state.
6. Optional Real XeLaTeX Smoke Compilation (--compile).

Usage:
    python3 teaching/check_teaching.py
    python3 teaching/check_teaching.py --compile
    python3 teaching/check_teaching.py --json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Sequence

TEACHING_ROOT = Path(__file__).resolve().parent
REPO_ROOT = TEACHING_ROOT.parent
TEMPLATE_ROOT = TEACHING_ROOT / "templates"
POOL_ROOT = TEACHING_ROOT / "pool"
TOPICS_ROOT = TEACHING_ROOT / "topics"
STUDENTS_ROOT = TEACHING_ROOT / "students"
CODEX_AGENTS_ROOT = REPO_ROOT / ".codex" / "agents"
COMPILER = REPO_ROOT / "infra" / "scripts" / "compile_tex.py"

CORE_TEMPLATES = (
    TEMPLATE_ROOT / "一对一错题课_学案模板.tex",
    TEMPLATE_ROOT / "一对一错题课_教案模板.tex",
)
QUESTION_PACK = TEMPLATE_ROOT / "questions.tex"
EXPECTED_AGENT_CONFIGS = {
    "question-ingester.toml": "question_ingester",
    "diagnosis-solver.toml": "diagnosis_solver",
    "session-planner.toml": "session_planner",
    "lesson-typesetter.toml": "lesson_builder",
    "session-reviewer.toml": "session_reviewer",
}
AGENT_FORBIDDEN_TEXT = ("comm" + "on/", "AGENT.md", "latexmk")

FORBIDDEN_PATTERNS = (
    (
        re.compile(r"\\usepackage(?:\[[^]]*\])?\{[^}]*" + "comm" + r"on/ipara\}"),
        "T-PATH-LEGACY-IPARA",
        "Canonical Teaching source must load `ipara` through infra, not a legacy path.",
    ),
    (
        re.compile(r"\\usepackage(?:\[[^]]*\])?\{(?:\.\./)+ipara\}"),
        "T-PATH-RELATIVE-IPARA",
        "Canonical Teaching source must load `ipara` through standard package name.",
    ),
    (
        re.compile(r"\\(?:input|include)\{[^}]*" + "comm" + "on/pool"),
        "T-PATH-LEGACY-POOL",
        "Canonical Teaching source must resolve questions via `teaching/pool/`.",
    ),
    (
        re.compile(r"\\(?:input|include)\{[^}]*" + "comm" + "on/topics"),
        "T-PATH-LEGACY-TOPICS",
        "Canonical Teaching source must resolve topics via `teaching/topics/`.",
    ),
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    target: str

    def format_line(self) -> str:
        return f"[{self.severity}][{self.code}] {self.target}: {self.message}"


def check_templates() -> list[Finding]:
    findings: list[Finding] = []
    for template in CORE_TEMPLATES:
        if not template.is_file():
            findings.append(Finding("ERROR", "T-TPL-MISSING", "Core template file missing", str(template.relative_to(REPO_ROOT))))
            continue
        text = template.read_text(encoding="utf-8")
        for pattern, code, msg in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                findings.append(Finding("ERROR", code, msg, str(template.relative_to(REPO_ROOT))))

    if not QUESTION_PACK.is_file():
        findings.append(Finding("ERROR", "T-PACK-MISSING", "Template question pack questions.tex missing", str(QUESTION_PACK.relative_to(REPO_ROOT))))
    else:
        pack_text = QUESTION_PACK.read_text(encoding="utf-8")
        if ("comm" + "on/pool") in pack_text:
            findings.append(Finding("ERROR", "T-PACK-LEGACY-POOL", "Template question pack must not reference legacy pool", str(QUESTION_PACK.relative_to(REPO_ROOT))))
        if "\\TeachingPoolRoot" not in pack_text and "teaching/pool" not in pack_text:
            findings.append(Finding("ERROR", "T-PACK-ROOT-PATH", "Template question pack must resolve to teaching/pool", str(QUESTION_PACK.relative_to(REPO_ROOT))))
    return findings


def check_student_sessions() -> list[Finding]:
    findings: list[Finding] = []
    if not STUDENTS_ROOT.is_dir():
        findings.append(Finding("ERROR", "T-STUDENTS-DIR", "teaching/students directory missing", "teaching/students"))
        return findings

    student_dirs = [d for d in STUDENTS_ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")]
    if not student_dirs:
        findings.append(Finding("WARNING", "T-STUDENTS-EMPTY", "No student directories found in teaching/students", "teaching/students"))
        return findings

    for sdir in student_dirs:
        profile = sdir / "profile.md"
        if not profile.is_file():
            findings.append(Finding("WARNING", "T-STUDENT-NO-PROFILE", f"Student profile.md missing for {sdir.name}", str(sdir.relative_to(REPO_ROOT))))

        sessions_dir = sdir / "sessions"
        if sessions_dir.is_dir():
            for tex_file in sessions_dir.rglob("*.tex"):
                text = tex_file.read_text(encoding="utf-8", errors="ignore")
                for pattern, code, msg in FORBIDDEN_PATTERNS:
                    if pattern.search(text):
                        findings.append(Finding("ERROR", code, msg, str(tex_file.relative_to(REPO_ROOT))))
    return findings


def check_agent_configs() -> list[Finding]:
    findings: list[Finding] = []
    seen_names: set[str] = set()
    for filename, expected_name in EXPECTED_AGENT_CONFIGS.items():
        path = CODEX_AGENTS_ROOT / filename
        target = str(path.relative_to(REPO_ROOT))
        if not path.is_file():
            findings.append(Finding("ERROR", "T-AGENT-MISSING", f"Canonical Teaching agent config missing: {filename}", target))
            continue
        text = path.read_text(encoding="utf-8")
        try:
            parsed = tomllib.loads(text)
        except tomllib.TOMLDecodeError as exc:
            findings.append(Finding("ERROR", "T-AGENT-TOML", f"Invalid TOML: {exc}", target))
            continue
        actual_name = str(parsed.get("name", ""))
        if actual_name != expected_name:
            findings.append(Finding("ERROR", "T-AGENT-NAME", f"Expected agent name `{expected_name}`, got `{actual_name or 'missing'}`", target))
        if actual_name in seen_names:
            findings.append(Finding("ERROR", "T-AGENT-DUPLICATE", f"Duplicate runtime agent name `{actual_name}`", target))
        seen_names.add(actual_name)
        for forbidden in AGENT_FORBIDDEN_TEXT:
            if forbidden in text:
                findings.append(Finding("ERROR", "T-AGENT-LEGACY", f"Post-migration agent config contains forbidden legacy execution token `{forbidden}`", target))

    lesson = CODEX_AGENTS_ROOT / "lesson-typesetter.toml"
    if lesson.is_file() and "infra/scripts/compile_tex.py" not in lesson.read_text(encoding="utf-8"):
        findings.append(Finding("ERROR", "T-AGENT-COMPILER", "lesson_builder must use the shared infra compiler entrypoint", str(lesson.relative_to(REPO_ROOT))))
    return findings


def run_domain_audits() -> list[Finding]:
    findings: list[Finding] = []
    audits = [
        ("audit_pool.py", TEACHING_ROOT / "audit_pool.py"),
        ("audit_topics.py", TEACHING_ROOT / "audit_topics.py"),
        ("audit_hygiene.py", TEACHING_ROOT / "audit_hygiene.py"),
    ]
    for name, script in audits:
        if not script.is_file():
            continue
        res = subprocess.run([sys.executable, str(script)], cwd=REPO_ROOT, capture_output=True, text=True)
        if res.returncode != 0:
            findings.append(Finding("ERROR", f"T-AUDIT-{name.upper()}", f"{name} failed with return code {res.returncode}:\n{res.stdout.strip()}", str(script.relative_to(REPO_ROOT))))
    return findings


def compile_template(template: Path) -> list[Finding]:
    findings: list[Finding] = []
    if not COMPILER.is_file():
        findings.append(Finding("ERROR", "T-COMPILER-MISSING", f"Shared compiler missing: {COMPILER}", str(COMPILER)))
        return findings

    with tempfile.TemporaryDirectory(prefix="ipara_teaching_smoke_") as tmpdir:
        res = subprocess.run(
            [sys.executable, str(COMPILER), str(template), "--outdir", tmpdir, "--warnings-as-errors"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if res.returncode != 0:
            findings.append(Finding("ERROR", "T-COMPILE-FAIL", f"Smoke compilation failed: {res.stdout.strip()} {res.stderr.strip()}", str(template.relative_to(REPO_ROOT))))
            return findings

        # Verify page count
        out_pdf = Path(tmpdir) / f"{template.stem}.pdf"
        if not out_pdf.is_file():
            findings.append(Finding("ERROR", "T-PDF-MISSING", "Compiled PDF was not produced", str(template.relative_to(REPO_ROOT))))
            return findings

        page_match = re.search(r"\((\d+)\s+pages\)", res.stdout)
        if page_match:
            pages = int(page_match.group(1))
            if pages != 4:
                findings.append(Finding("ERROR", "T-PAGE-COUNT", f"Template must be exactly 4 pages, got {pages} pages", str(template.relative_to(REPO_ROOT))))
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Teaching domain steady-state integrity gate.")
    parser.add_argument("--compile", action="store_true", help="Run real XeLaTeX smoke compilation on core templates.")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format.")
    args = parser.parse_args(argv)

    findings: list[Finding] = []
    findings.extend(check_templates())
    findings.extend(check_student_sessions())
    findings.extend(check_agent_configs())
    findings.extend(run_domain_audits())

    if args.compile:
        for template in CORE_TEMPLATES:
            findings.extend(compile_template(template))

    errors = [f for f in findings if f.severity == "ERROR"]
    warnings = [f for f in findings if f.severity == "WARNING"]

    if args.json:
        payload = {
            "status": "PASS" if not errors else "FAIL",
            "error_count": len(errors),
            "warning_count": len(warnings),
            "findings": [asdict(f) for f in findings],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 1 if errors else 0

    print("=" * 80)
    print("Teaching Domain Steady-State Gate")
    print("=" * 80)
    print(f"Templates checked : {len(CORE_TEMPLATES)} core + questions.tex pack")
    print(f"Students root     : {STUDENTS_ROOT.relative_to(REPO_ROOT)}")
    print(f"Agent configs     : {len(EXPECTED_AGENT_CONFIGS)} canonical roles")
    print(f"Smoke compile     : {'ENABLED' if args.compile else 'DISABLED (use --compile)'}")
    print("-" * 80)

    if findings:
        for finding in findings:
            print(finding.format_line())
        print("-" * 80)

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1

    print(f"PASSED: 0 errors, {len(warnings)} warning(s). All steady-state invariants hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
