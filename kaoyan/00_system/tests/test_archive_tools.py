from __future__ import annotations

import ast
import unittest
from pathlib import Path


SYSTEM_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = SYSTEM_ROOT / "tools"


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
