import contextlib
import importlib.util
import io
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "exam_profiles" / "math1.json"
BUILD_TOOL_PATH = ROOT / "tools" / "build_math1_archive.py"
SVG_TOOL_PATH = ROOT / "tools" / "generate_math1_svgs.py"


def era_for_year(profile: dict, year: int) -> dict:
    matches = []
    for era in profile["eras"]:
        years = era["years"]
        if years["from"] <= year <= years["to"]:
            matches.append(era)
    if len(matches) != 1:
        raise AssertionError(f"year {year} resolved to {len(matches)} eras")
    return matches[0]


def subject_for_question(era: dict, question: int) -> str | None:
    for route in era.get("subject_routing", []):
        if question in route.get("questions", []):
            return route["subject"]
    return None


class Math1ExamProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
        spec = importlib.util.spec_from_file_location("build_math1_archive", BUILD_TOOL_PATH)
        assert spec is not None and spec.loader is not None
        cls.build_tool = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.build_tool)

        svg_spec = importlib.util.spec_from_file_location("generate_math1_svgs", SVG_TOOL_PATH)
        assert svg_spec is not None and svg_spec.loader is not None
        cls.svg_tool = importlib.util.module_from_spec(svg_spec)
        svg_spec.loader.exec_module(cls.svg_tool)

    def test_every_archive_year_resolves_to_exactly_one_era(self):
        for year in range(1987, 2027):
            with self.subTest(year=year):
                era_for_year(self.profile, year)

    def test_2007_is_its_own_24_question_era(self):
        era = era_for_year(self.profile, 2007)
        self.assertEqual(era["era_id"], "era_2007")
        self.assertEqual(era["question_count"], 24)
        self.assertEqual(era["sections"][0]["questions"], {"from": 1, "to": 10})
        self.assertEqual(era["sections"][1]["questions"], {"from": 11, "to": 16})
        self.assertEqual(era["sections"][2]["questions"], {"from": 17, "to": 24})
        self.assertEqual(subject_for_question(era, 7), "线性代数")
        self.assertEqual(subject_for_question(era, 9), "概率论与数理统计")

    def test_current_era_routes_q7_to_linear_algebra(self):
        era = era_for_year(self.profile, 2026)
        self.assertEqual(era["era_id"], "era_2021_present")
        self.assertEqual(subject_for_question(era, 7), "线性代数")
        self.assertEqual(subject_for_question(era, 8), "概率论与数理统计")

    def test_2024_figure_route_uses_canonical_q05_asset(self):
        self.assertEqual(
            self.build_tool.YEAR_SVG_MAP[2024],
            [("q05", "assets/q05_three_planes_pencil.svg")],
        )

        generator_source = SVG_TOOL_PATH.read_text(encoding="utf-8")
        self.assertNotIn("q01_three_planes.svg", generator_source)
        self.assertNotIn("gen_2024_q05", generator_source)

    def test_direct_svg_generator_requires_explicit_all(self):
        calls = []
        original_deploy = self.svg_tool.deploy_svg
        self.svg_tool.deploy_svg = lambda *args, **kwargs: calls.append((args, kwargs))
        try:
            with contextlib.redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit):
                    self.svg_tool.main([])
            self.assertEqual(calls, [])

            with contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as help_exit:
                    self.svg_tool.main(["--help"])
            self.assertEqual(help_exit.exception.code, 0)
            self.assertEqual(calls, [])
        finally:
            self.svg_tool.deploy_svg = original_deploy


if __name__ == "__main__":
    unittest.main()
