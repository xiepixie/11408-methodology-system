import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "cognitive_system.py"
SPEC = importlib.util.spec_from_file_location("cognitive_system_under_test", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class StatusSemanticsTests(unittest.TestCase):
    def test_rules_status_does_not_claim_handbook_body(self):
        status = "工作稿，待验证规则已建立，尚无已采用规则"
        self.assertFalse(MODULE.status_claims_handbook_body(status))

    def test_pending_latex_creation_does_not_claim_body(self):
        status = "Subject Landing Page 已建立；Canonical LaTeX 正文待逐册建立"
        self.assertFalse(MODULE.status_claims_handbook_body(status))

    def test_latex_working_draft_claims_body(self):
        self.assertTrue(MODULE.status_claims_handbook_body("LaTeX 工作稿；待继续校验"))

    def test_pending_human_confirmation_claims_body(self):
        self.assertTrue(MODULE.status_claims_handbook_body("工作稿，待人工确认"))

    def test_source_marker_overrides_pending_confirmation(self):
        status = "Source；README 工作稿待迁入 Canonical LaTeX 后再人工确认"
        self.assertFalse(MODULE.status_claims_handbook_body(status))

    def test_published_pdf_phrase_claims_published(self):
        status = "Canonical LaTeX 第一版正文已建立并已有 Published PDF"
        self.assertTrue(MODULE.status_claims_published(status))

    def test_published_pdf_phrase_also_claims_handbook_body(self):
        self.assertTrue(MODULE.status_claims_handbook_body("已有 Published PDF"))

    def test_legacy_publish_debt_does_not_claim_current_publish(self):
        self.assertFalse(MODULE.status_claims_published("旧发布物待纳管"))

    def test_source_working_draft_uses_source_bucket(self):
        status = "Source；Atlas Foundation 工作稿，待迁入 Canonical LaTeX"
        self.assertEqual(MODULE.status_bucket(status), "Handbook Source 待迁移")

    def test_source_diff_phrase_does_not_change_status_bucket(self):
        status = "**工作稿｜已完成第一轮 Source Diff 与重构，待人工确认。**"
        self.assertEqual(MODULE.status_bucket(status), "待人工确认")

    def test_source_diff_phrase_is_not_a_source_status(self):
        status = "工作稿｜已完成第一轮 Source Diff 与重构，待人工确认"
        self.assertFalse(MODULE.status_is_source_only(status))
        self.assertTrue(MODULE.status_claims_handbook_body(status))

    def test_narrative_working_draft_phrase_does_not_set_working_bucket(self):
        status = "Subject Landing Page 已建立；八个 Topic 的旧 README 工作稿已降为 Source 待迁移"
        self.assertEqual(MODULE.status_bucket(status), "框架/目录已建立")

    def test_explicit_latex_working_draft_beats_architecture_note(self):
        status = "LaTeX 工作稿，架构已采用，待逐科正文继续校验"
        self.assertEqual(MODULE.status_bucket(status), "工作稿")

    def test_atlas_working_draft_uses_working_bucket(self):
        self.assertEqual(MODULE.status_bucket("Atlas 工作稿；地图仍在形成"), "工作稿")

    def test_architecture_adopted_without_body_is_framework_bucket(self):
        status = "架构已采用，正文待逐册建立"
        self.assertEqual(MODULE.status_bucket(status), "框架/目录已建立")

    def test_published_pdf_phrase_uses_published_bucket(self):
        status = "Canonical LaTeX 第一版正文已建立并已有 Published PDF"
        self.assertEqual(MODULE.status_bucket(status), "已发布")

    def test_candidate_core_uses_candidate_bucket(self):
        status = "Candidate Core；接口结构已确认，独立 Core 优先级待真题证据"
        self.assertEqual(MODULE.status_bucket(status), "Candidate")

    def test_rule_pending_validation_uses_pending_bucket(self):
        status = "待验证；由旧 Source 中的做题经验重新路由形成"
        self.assertEqual(MODULE.status_bucket(status), "待验证")

    def test_deprecated_navigation_uses_deprecated_bucket(self):
        status = "废弃入口，仅保留导航指针"
        self.assertEqual(MODULE.status_bucket(status), "废弃/Source 导航")

    def test_legacy_unregistered_uses_legacy_bucket(self):
        status = "legacy-unregistered Source；不再作为 Canonical Owner"
        self.assertEqual(MODULE.status_bucket(status), "旧发布物待纳管")

    def test_rules_directory_is_not_handbook_area(self):
        path = Path("30_408/10_数据结构/90_做题规则/README.md")
        self.assertFalse(MODULE.is_handbook_area(path))


class TrainingFigureLifecycleTests(unittest.TestCase):
    def setUp(self):
        self._old_project_root = MODULE.PROJECT_ROOT
        self._tmp = tempfile.TemporaryDirectory()
        MODULE.PROJECT_ROOT = Path(self._tmp.name).resolve()

    def tearDown(self):
        MODULE.PROJECT_ROOT = self._old_project_root
        self._tmp.cleanup()

    def _write_training_package(self, status: str, placeholder: str) -> None:
        topic = MODULE.PROJECT_ROOT / "10_数学一" / "10_高等数学" / "01_测试专题"
        topic.mkdir(parents=True, exist_ok=True)
        (topic / "README.md").write_text(
            "# 测试专题\n\n"
            f"> 状态：{status}\n\n"
            "## 训练导航\n\n"
            "- [反函数](反函数.md)\n",
            encoding="utf-8",
        )
        (topic / "反函数.md").write_text(
            "# 反函数\n\n"
            "> 训练定位：测试图意图生命周期。  \n"
            "> 模型归属：[《测试正文》](测试正文.tex)。\n\n"
            f"{placeholder}\n",
            encoding="utf-8",
        )

    def test_required_figure_is_audit_only_while_pending_confirmation(self):
        self._write_training_package(
            "待人工确认；Canonical LaTeX 工作稿已建立",
            "> **待补图｜反函数_单射判别**：用水平线展示一个输出是否对应多个输入。",
        )
        hard_codes = {finding.code for finding in MODULE.training_markdown_findings()}
        self.assertNotIn("E-TRAINING-FIGURE-TODO", hard_codes)
        audit_codes = {finding.code for finding in MODULE.audit_training_figure_todos()}
        self.assertIn("A-TRAINING-FIGURE-TODO", audit_codes)

    def test_required_figure_blocks_adopted_topic(self):
        self._write_training_package(
            "已采用；Canonical LaTeX 正文已建立",
            "> **待补图｜反函数_单射判别**：用水平线展示一个输出是否对应多个输入。",
        )
        hard_codes = {finding.code for finding in MODULE.training_markdown_findings()}
        self.assertIn("E-TRAINING-FIGURE-TODO", hard_codes)

    def test_candidate_figure_neither_blocks_nor_enters_required_audit(self):
        self._write_training_package(
            "已采用；Canonical LaTeX 正文已建立",
            "> **候选配图｜反函数_图像补充**：若文字不够直观，再补图。",
        )
        hard_codes = {finding.code for finding in MODULE.training_markdown_findings()}
        self.assertNotIn("E-TRAINING-FIGURE-TODO", hard_codes)
        audit_codes = {finding.code for finding in MODULE.audit_training_figure_todos()}
        self.assertNotIn("A-TRAINING-FIGURE-TODO", audit_codes)


class PostMigrationContractTests(unittest.TestCase):
    def test_repo_root_is_parent_of_kaoyan_domain(self):
        self.assertEqual(MODULE.REPO_ROOT, MODULE.PROJECT_ROOT.parent)

    def test_shared_compiler_is_owned_by_infra(self):
        expected = MODULE.REPO_ROOT / "infra" / "scripts" / "compile_tex.py"
        self.assertEqual(MODULE.SHARED_COMPILE_SCRIPT, expected)
        self.assertTrue(expected.is_file())

    def test_active_kaoyan_assets_have_no_legacy_routes(self):
        self.assertEqual(MODULE.legacy_route_findings(), [])


class ContextRoutingTests(unittest.TestCase):
    def test_linear_algebra_context_uses_canonical_atlas_and_subject_rules(self):
        context = MODULE.SUBJECTS["linear-algebra"]["context"]
        expected_atlas = Path("10_数学一/20_线性代数/README.md")
        expected_rules = Path("10_数学一/90_学科做题规则/线性代数.md")
        self.assertIn(expected_atlas, context)
        self.assertIn(expected_rules, context)
        self.assertTrue((MODULE.PROJECT_ROOT / expected_atlas).exists())
        self.assertTrue((MODULE.PROJECT_ROOT / expected_rules).exists())


class ExamSolutionIntegrityTests(unittest.TestCase):
    def test_2019_comprehensive_routing_override_is_applied(self):
        profile = __import__("json").loads(MODULE.EXAM_PROFILE_408.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.expected_408_subject(profile, 2019, 43), "操作系统")
        self.assertEqual(MODULE.expected_408_subject(profile, 2019, 45), "计算机组成原理")

    def test_2016_comprehensive_routing_override_is_applied(self):
        profile = __import__("json").loads(MODULE.EXAM_PROFILE_408.read_text(encoding="utf-8"))
        self.assertEqual(MODULE.expected_408_subject(profile, 2016, 41), "计算机网络")
        self.assertEqual(MODULE.expected_408_subject(profile, 2016, 42), "数据结构")
        self.assertEqual(MODULE.expected_408_subject(profile, 2016, 46), "操作系统")

    def test_solution_year_lifecycle_distinguishes_partial_from_complete(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            solutions_dir = Path(tmpdir)
            self.assertFalse(MODULE.solution_year_declared_complete(solutions_dir, [1, 2, 3]))
            (solutions_dir / "README.md").write_text("# partial marker test\n", encoding="utf-8")
            self.assertTrue(MODULE.solution_year_declared_complete(solutions_dir, [1, 2, 3]))
        with tempfile.TemporaryDirectory() as tmpdir:
            self.assertTrue(MODULE.solution_year_declared_complete(Path(tmpdir), list(range(1, 48))))

    def test_completed_exam_solution_years_pass_machine_gate(self):
        self.assertEqual(MODULE.exam_solution_findings(), [])

    def test_model_anchor_requires_explicit_owner_marker(self):
        self.assertIsNotNone(MODULE.EXAM_SOLUTION_ANCHOR_OWNER_RE.search("- 主题：DS07｜DFS\n"))
        self.assertIsNotNone(MODULE.EXAM_SOLUTION_ANCHOR_OWNER_RE.search("- 模型归属：CO-03 数据通路\n"))
        self.assertIsNotNone(MODULE.EXAM_SOLUTION_ANCHOR_OWNER_RE.search("- 规则：先定作用域\n"))
        self.assertIsNotNone(MODULE.EXAM_SOLUTION_ANCHOR_OWNER_RE.search("- Topic：DS07｜DFS\n"))
        self.assertIsNone(MODULE.EXAM_SOLUTION_ANCHOR_OWNER_RE.search("- 题目信号：出现 Cache\n"))

    def test_exam_solution_preferred_headings_are_chinese(self):
        self.assertEqual(MODULE.EXAM_SOLUTION_OBJECTIVE_HEADINGS[0], "模型锚点")
        self.assertEqual(MODULE.EXAM_SOLUTION_OBJECTIVE_HEADINGS[3], "校验")
        self.assertEqual(MODULE.EXAM_SOLUTION_COMPREHENSIVE_HEADINGS[1], "问题表征")
        self.assertEqual(MODULE.EXAM_SOLUTION_COMPREHENSIVE_HEADINGS[2], "关键决策")
        self.assertEqual(MODULE.EXAM_SOLUTION_COMPREHENSIVE_HEADINGS[3], "求解链")

    def test_2014_partial_solutions_use_chinese_headings(self):
        solutions_dir = MODULE.EXAM_SOLUTION_ROOT / "2014年真题" / "solutions"
        for path in sorted(solutions_dir.glob("q[0-9][0-9].md")):
            text = path.read_text(encoding="utf-8")
            headings = tuple(MODULE.EXAM_SOLUTION_H2_RE.findall(text))
            self.assertEqual(headings, MODULE.EXAM_SOLUTION_OBJECTIVE_HEADINGS)


class AtlasFormatTests(unittest.TestCase):
    def test_course_atlas_is_declared_markdown_canonical(self):
        readme = MODULE.PROJECT_ROOT / "30_408" / "README.md"
        self.assertTrue(MODULE.is_atlas_readme(readme))
        self.assertEqual(MODULE.declared_handbook_type(readme), "Atlas")

    def test_atlas_is_not_missing_tex_debt(self):
        target = "30_408/10_数据结构/README.md"
        messages = {finding.message for finding in MODULE.audit_missing_tex()}
        self.assertFalse(any(target in message for message in messages))

    def test_source_only_deep_map_is_not_missing_tex_debt(self):
        target = "30_408/10_数据结构/00_学科总图/README.md"
        messages = {finding.message for finding in MODULE.audit_missing_tex()}
        self.assertFalse(any(target in message for message in messages))

    def test_root_level_atlas_tex_is_audit_debt(self):
        messages = {finding.message for finding in MODULE.audit_atlas_duplicate_tex()}
        self.assertTrue(any("10_数学一/00_学科总图/README.md" in message for message in messages))


class PublishPreflightTests(unittest.TestCase):
    def test_old_course_atlas_tex_is_rejected_as_second_truth(self):
        target = (
            MODULE.PROJECT_ROOT
            / "10_数学一"
            / "00_学科总图"
            / "数学一_高等数学_心智模型手册_v2.tex"
        )
        codes = {finding.code for finding in MODULE.publish_preflight(target)}
        self.assertIn("P-ATLAS-VIEW", codes)

    def test_atlas_visual_must_live_under_assets(self):
        target = MODULE.PROJECT_ROOT / "30_408" / "assets" / "408_Course_Atlas_Poster.tex"
        codes = {finding.code for finding in MODULE.publish_view_preflight(target)}
        self.assertNotIn("PV-LOCATION", codes)

    def test_current_topic_tex_passes_publish_preflight(self):
        target = (
            MODULE.PROJECT_ROOT
            / "10_数学一"
            / "20_线性代数"
            / "01_向量空间_生成基与坐标"
            / "向量空间_生成基与坐标.tex"
        )
        self.assertEqual(MODULE.publish_preflight(target), [])

    def test_current_os_topic_tex_passes_publish_preflight(self):
        target = (
            MODULE.PROJECT_ROOT
            / "30_408"
            / "30_操作系统"
            / "10_进程线程调度与控制权"
            / "OS-01_OS-02_进程线程调度与控制权_方法论手册.tex"
        )
        self.assertEqual(MODULE.publish_preflight(target), [])

    def test_noncanonical_math_methodology_tex_is_rejected(self):
        target = (
            MODULE.PROJECT_ROOT
            / "10_数学一"
            / "90_学科做题规则"
            / "研究生数学_做题与研究的方法论手册.tex"
        )
        codes = {finding.code for finding in MODULE.publish_preflight(target)}
        self.assertIn("P-NOT-CANONICAL", codes)

    def test_tex_without_landing_page_is_rejected(self):
        dummy_dir = MODULE.PROJECT_ROOT / "00_system" / "tests" / "tmp_test_dir"
        dummy_dir.mkdir(parents=True, exist_ok=True)
        dummy_tex = dummy_dir / "test_no_readme.tex"
        dummy_tex.write_text("% dummy", encoding="utf-8")
        try:
            codes = {finding.code for finding in MODULE.publish_preflight(dummy_tex)}
            self.assertIn("P-NO-README", codes)
        finally:
            if dummy_tex.exists():
                dummy_tex.unlink()
            if dummy_dir.exists():
                dummy_dir.rmdir()

    def test_publish_env_exposes_project_root_to_texinputs(self):
        env = MODULE.project_compile_env()
        texinputs = env.get("TEXINPUTS", "")
        self.assertTrue(texinputs.startswith(f"{MODULE.PROJECT_ROOT}:"))

    def test_math1_handbook_publishes_into_math1_category(self):
        target = (
            MODULE.PROJECT_ROOT
            / "10_数学一"
            / "10_高等数学"
            / "02_极限与连续_邻域尺度与存在性"
            / "极限与连续_邻域尺度与存在性.tex"
        )
        self.assertEqual(MODULE.publish_target_dir(target), MODULE.PUBLISH_DIR / "math1")

    def test_system_handbook_template_is_not_a_missing_landing_page_debt(self):
        template = MODULE.PROJECT_ROOT / "00_system" / "handbook_template.tex"
        messages = {finding.message for finding in MODULE.audit_tex_without_readme()}
        self.assertFalse(any(str(template.relative_to(MODULE.PROJECT_ROOT)) in message for message in messages))


if __name__ == "__main__":
    unittest.main()
