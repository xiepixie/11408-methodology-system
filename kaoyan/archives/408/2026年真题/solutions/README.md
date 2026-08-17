# 2026 年 408｜心智模型题解

本目录是 **Derived Solution Layer**，不拥有题面事实，也不重新定义 Handbook 机制。

- 原题唯一来源：`../2026 年全国硕士研究生招生考试.md` 及其嵌入的综合题正式题面。
- 通用题解合同：`../../../../00_system/exam_solution_authoring_spec.md`。
- Agent 执行协议：`../../../../00_system/exam_solution_agent_prompt.md`。
- [题解质量保证与学生学习合同](../../../../00_system/exam_solution_quality_assurance.md)。
- Q1～Q40 固定按 `Model Anchor -> 解题链 -> 选项判断 -> Verification -> Compression -> 易错边界` 组织。
- Q41～Q47 固定按 `Model Anchor -> Problem Representation -> Decision Points -> Solution Chain -> Verification -> Compression -> 易错边界` 组织；算法题额外包含正确性与复杂度合同。
- 旧 `../qNN_*.md` 的答案与解析仅作为 legacy derived reference；冲突时以 Canonical Source + 独立推导为准。

## 当前状态

2026 已完成 Q1～Q47 的 model-grounded solution，并通过统一结构复核：

```text
Q1～Q11   数据结构
Q12～Q22  计算机组成原理
Q23～Q32  操作系统
Q33～Q40  计算机网络
Q41～Q47  综合应用题深度 Gate
```

年度 Source 疑点、legacy correction 与 Candidate Rule Evidence 统一记录在 `solution_review.md`，不污染题解正文；若题解独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则直接 Stable Write 修正唯一 Owner，并回归受影响题解。