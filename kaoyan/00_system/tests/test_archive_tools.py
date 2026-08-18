from __future__ import annotations

import ast
import importlib.util
import json
import re
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = SYSTEM_ROOT / "tools"
MATH1_ARCHIVE_ROOT = SYSTEM_ROOT.parent / "archives" / "math1"


def top_level_string_constant(path: Path, name: str) -> str | None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            continue
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return node.value.value
    return None


class ScraperUpstreamRouteTests(unittest.TestCase):
    def test_math1_scraper_has_current_base_url(self):
        path = TOOLS_ROOT / "scrape_math1_exam_archive.py"
        self.assertEqual(
            top_level_string_constant(path, "BASE_URL"),
            "https://www.csgraduates.com/study_methods/math/math1",
        )

    def test_408_scraper_has_current_base_url(self):
        path = TOOLS_ROOT / "scrape_408_exam_archive.py"
        self.assertEqual(
            top_level_string_constant(path, "BASE_URL"),
            "https://www.csgraduates.com/study_methods/408quiz",
        )


class Math1MetadataRoundTripTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scraper_path = TOOLS_ROOT / "scrape_math1_exam_archive.py"
        spec = importlib.util.spec_from_file_location("math1_scraper_for_test", scraper_path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot load scraper module: {scraper_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        cls.get_math1_metadata = staticmethod(module.get_math1_metadata)

    def test_scraper_metadata_matches_all_canonical_exam_sources(self):
        year_dirs = sorted(
            (
                (int(match.group(1)), path)
                for path in MATH1_ARCHIVE_ROOT.glob("*年真题")
                if (match := re.fullmatch(r"(\d{4})年真题", path.name))
            ),
            key=lambda item: item[0],
        )
        self.assertTrue(year_dirs, "Math1 archive has no year directories")

        years = [year for year, _ in year_dirs]
        self.assertEqual(years, list(range(years[0], years[-1] + 1)), "Math1 archive years must be contiguous")

        for year, year_dir in year_dirs:
            with self.subTest(year=year):
                exam = json.loads((year_dir / "exam.json").read_text(encoding="utf-8"))
                self.assertEqual(sum(exam["question_scores"].values()), exam["total_score"])
                self.assertEqual(len(exam["question_scores"]), exam["question_count"])

                for q_num in range(1, exam["question_count"] + 1):
                    question_files = list(year_dir.glob(f"q{q_num:02d}_*.md"))
                    self.assertEqual(len(question_files), 1, f"{year} Q{q_num:02d} must have exactly one source file")

                    text = question_files[0].read_text(encoding="utf-8")
                    parts = text.split("---", 2)
                    self.assertEqual(len(parts), 3, f"invalid frontmatter: {question_files[0]}")
                    frontmatter = parts[1]

                    subject_match = re.search(r"^subject:\s*(.+)$", frontmatter, re.MULTILINE)
                    type_match = re.search(r"^type:\s*(.+)$", frontmatter, re.MULTILINE)
                    score_match = re.search(r"^score:\s*(\d+)$", frontmatter, re.MULTILINE)
                    self.assertIsNotNone(subject_match)
                    self.assertIsNotNone(type_match)
                    self.assertIsNotNone(score_match)

                    actual = {
                        "subject": subject_match.group(1).strip(),
                        "type": type_match.group(1).strip(),
                        "score": int(score_match.group(1)),
                    }
                    expected = self.get_math1_metadata(year, q_num)
                    self.assertEqual(expected, actual, f"{year} Q{q_num:02d} scraper metadata drift")
                    self.assertEqual(actual["score"], exam["question_scores"][str(q_num)])


class Math1SvgOwnershipTests(unittest.TestCase):
    def test_archive_builder_delegates_svg_generation(self):
        path = TOOLS_ROOT / "build_math1_archive.py"
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        function_names = {
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        assigned_names = {
            target.id
            for node in tree.body
            if isinstance(node, ast.Assign)
            for target in node.targets
            if isinstance(target, ast.Name)
        }
        self.assertNotIn("make_svg", function_names)
        self.assertNotIn("DARK_THEME", assigned_names)
        self.assertNotIn("LIGHT_THEME", assigned_names)
        self.assertIn("import generate_math1_svgs", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
