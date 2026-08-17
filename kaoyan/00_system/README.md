# 考研考试控制与认知系统

> 类型：System Control
> 状态：已采用；本目录持有认知系统调度内核、自动化校验工具、真题转换规范与考试控制方法论手册。

## 1. 核心手稿与规范索引

- **考试控制方法论手册**：[`考研考试控制_从能力到分数的方法论手册_v1.tex`](考研考试控制_从能力到分数的方法论手册_v1.tex)
  - 核心架构：考试时间分配与节奏控制、得分期望最大化策略、卡点脱困与应急决策、考场心智状态调控。
- **系统核心规范**：
  - [仓库完整性与维护审计](repository_integrity.md) (`repository_integrity.md`)
  - [真题源转换规范](exam_source_conversion_spec.md) (`exam_source_conversion_spec.md`)
  - [题解质量保证规范](exam_solution_quality_assurance.md) (`exam_solution_quality_assurance.md`)
  - [Ownership 矩阵台账](ownership_matrix.md) (`ownership_matrix.md`)

## 2. 自动化工具与状态

- 认知系统主脚本：`python3 00_system/cognitive_system.py {check,audit,progress,publish}`
- 工具库：`00_system/tools/`
- 考试 Profile：`00_system/exam_profiles/`
- 当前项目焦点：[CURRENT.md](../CURRENT.md)
- 资产生成进度：[PROGRESS.md](../PROGRESS.md)
