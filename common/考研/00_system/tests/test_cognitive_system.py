import importlib.util
import sys
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


class ContextRoutingTests(unittest.TestCase):
    def test_linear_algebra_context_uses_canonical_atlas_and_subject_rules(self):
        context = MODULE.SUBJECTS["linear-algebra"]["context"]
        expected_atlas = Path(
            "10_数学一/20_线性代数/线性代数 Subject Atlas：空间、映射、表示与不变量.md"
        )
        expected_rules = Path("10_数学一/90_学科做题规则/线性代数.md")
        self.assertIn(expected_atlas, context)
        self.assertIn(expected_rules, context)
        self.assertTrue((MODULE.PROJECT_ROOT / expected_atlas).exists())
        self.assertTrue((MODULE.PROJECT_ROOT / expected_rules).exists())


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
        self.assertTrue(any("30_408/README.md" in message for message in messages))


class PublishPreflightTests(unittest.TestCase):
    def test_old_course_atlas_tex_is_rejected_as_second_truth(self):
        target = MODULE.PROJECT_ROOT / "30_408" / "408_Course_Atlas.tex"
        codes = {finding.code for finding in MODULE.publish_preflight(target)}
        self.assertIn("P-ATLAS-VIEW", codes)

    def test_atlas_visual_must_live_under_assets(self):
        target = MODULE.PROJECT_ROOT / "30_408" / "408_Course_Atlas.tex"
        codes = {finding.code for finding in MODULE.publish_view_preflight(target)}
        self.assertIn("PV-LOCATION", codes)

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
        target = MODULE.PROJECT_ROOT / "00_system" / "考研考试控制_从能力到分数的方法论手册_v1.tex"
        codes = {finding.code for finding in MODULE.publish_preflight(target)}
        self.assertIn("P-NO-README", codes)

    def test_publish_env_exposes_project_root_to_texinputs(self):
        env = MODULE.project_compile_env()
        texinputs = env.get("TEXINPUTS", "")
        self.assertTrue(texinputs.startswith(f"{MODULE.PROJECT_ROOT}:"))

    def test_system_handbook_template_is_not_a_missing_landing_page_debt(self):
        template = MODULE.PROJECT_ROOT / "00_system" / "handbook_template.tex"
        messages = {finding.message for finding in MODULE.audit_tex_without_readme()}
        self.assertFalse(any(str(template.relative_to(MODULE.PROJECT_ROOT)) in message for message in messages))


if __name__ == "__main__":
    unittest.main()
