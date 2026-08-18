# 考研考试控制与认知系统

> 类型：System Control
> 状态：已采用；本目录持有认知系统调度内核、自动化校验工具、真题转换规范与考试控制方法论手册。

## 1. 核心手稿与规范索引

- **考试控制方法论手册**：[`考研考试控制_从能力到分数的方法论手册_v1.tex`](考研考试控制_从能力到分数的方法论手册_v1.tex)
  - 核心架构：考试时间分配与节奏控制、得分期望最大化策略、卡点脱困与应急决策、考场心智状态调控。
- **场景与协作**：
  - [场景路由与最小上下文协议](agent_context_protocol.md)
  - [人机协作与系统更新工作流](collaboration_workflow.md)
  - [场景启动速查](interaction_playbook.md)
- **Handbook 与规则**：
  - [Handbook 与 Rule 契约](handbook_contract.md)
  - [学科心智模型手册通用写作规范](handbook_writing_spec.md)
  - [专题训练写作规范](topic_practice_writing_spec.md)
  - [Inbox 与规则验证协议](evidence_promotion.md)
  - [Canonical Ownership Matrix](ownership_matrix.md)
- **真题源重建**：
  - [真题源重建执行提示词](exam_source_agent_prompt.md)
  - [真题与试卷 Source 转译规范](exam_source_conversion_spec.md)
  - [考试 Profile](exam_profiles/README.md)
- **真题题解**：
  - [真题题解执行提示词](exam_solution_agent_prompt.md)
  - [心智模型驱动题解写作规范](exam_solution_authoring_spec.md)
  - [真题题解质量保证与学生学习合同](exam_solution_quality_assurance.md)
- **仓库与排版**：
  - [仓库完整性与维护审计](repository_integrity.md)
  - [LaTeX Design System 路由](latex_design_system.md)
  - [LaTeX 视觉与布局规范](latex_layout_spec.md)

同一规则只允许一个 Owner。执行提示词负责“怎么执行”，规范负责“规则是什么”，速查页只负责入口，不复制正文。

## 2. 自动化工具与状态

- 认知系统主脚本：`python3 00_system/cognitive_system.py {check,audit,progress,publish}`
- 工具库：`00_system/tools/`
- 考试 Profile：`00_system/exam_profiles/`
- 当前项目焦点：[CURRENT.md](../CURRENT.md)
- 资产生成进度：[PROGRESS.md](../PROGRESS.md)
