from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
SYSTEM_DIR = TESTS_DIR.parent
KAOYAN_DIR = SYSTEM_DIR.parent
DAILY_READING_DIR = KAOYAN_DIR / "20_英语一" / "10_阅读" / "daily_reading"
TOOLS_DIR = DAILY_READING_DIR / "00_system" / "tools"
CHECK_SCRIPT = TOOLS_DIR / "check_daily_reading.py"


def load_check_module():
    spec = importlib.util.spec_from_file_location("check_daily_reading", CHECK_SCRIPT)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {CHECK_SCRIPT}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class DailyReadingIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.checker = load_check_module()

    def test_current_repo_passes_all_static_checks(self):
        self.assertEqual(self.checker.check_build_cleanliness(), [])
        self.assertEqual(self.checker.check_templates(), [])
        self.assertEqual(self.checker.check_all_articles(), [])

    def test_cornell_linkage_detects_missing_noteitem(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            adir = Path(tmpdir) / "2026-08-20_sample_test"
            adir.mkdir()
            (adir / "article.md").write_text("# Test Article\n\nSome raw english text.", encoding="utf-8")
            (adir / "reading_view.pdf").write_bytes(b"%PDF-fake")

            # TeX has \kw{word}{kw01} but no \noteitem{kw01}
            tex_content = r"""
\documentclass{ctexart}
\usepackage{ipara-reading}
\begin{document}
\kw{word}{kw01}
\end{document}
"""
            (adir / "reading_view.tex").write_text(tex_content, encoding="utf-8")

            errors = self.checker.check_article_dir(adir)
            self.assertTrue(any("without matching \\noteitem" in e for e in errors), f"Expected missing noteitem error, got: {errors}")

    def test_cornell_linkage_detects_duplicate_noteitem(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            adir = Path(tmpdir) / "2026-08-20_sample_test"
            adir.mkdir()
            (adir / "article.md").write_text("# Test Article\n\nSome raw english text.", encoding="utf-8")
            (adir / "reading_view.pdf").write_bytes(b"%PDF-fake")

            tex_content = r"""
\documentclass{ctexart}
\usepackage{ipara-reading}
\begin{document}
\kw{word1}{kw01}
\noteitem{kw01}{explanation 1}
\noteitem{kw01}{explanation 2}
\end{document}
"""
            (adir / "reading_view.tex").write_text(tex_content, encoding="utf-8")

            errors = self.checker.check_article_dir(adir)
            self.assertTrue(any("duplicate \\noteitem" in e for e in errors), f"Expected duplicate noteitem error, got: {errors}")

    def test_article_md_detects_spoilers(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            adir = Path(tmpdir) / "2026-08-20_sample_test"
            adir.mkdir()
            (adir / "article.md").write_text("# Test Article\n\n## 单词讲解\n\nSpoiling vocabulary.", encoding="utf-8")
            (adir / "reading_view.pdf").write_bytes(b"%PDF-fake")
            (adir / "reading_view.tex").write_text(r"\documentclass{ctexart}\usepackage{ipara-reading}\begin{document}\end{document}", encoding="utf-8")

            errors = self.checker.check_article_dir(adir)
            self.assertTrue(any("forbidden preview spoiler" in e for e in errors), f"Expected spoiler error, got: {errors}")
