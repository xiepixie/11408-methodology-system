# 2024 年 408｜心智模型题解

本目录是 **Derived Solution Layer**：题面事实只引用 `../2024 年全国硕士研究生招生考试.md`，机制由 `kaoyan/30_408/` 的 Atlas / Topic / Rules 提供。

执行合同：

- [题解写作规范](../../../../00_system/exam_solution_authoring_spec.md)
- [题解质量保证与学生学习合同](../../../../00_system/exam_solution_quality_assurance.md)

统一格式：

```text
选择题：Model Anchor -> 解题链 -> 选项判断 -> Verification -> Compression -> 易错边界
综合题：Model Anchor -> Problem Representation -> Decision Points -> Solution Chain -> Verification -> Compression -> 易错边界
```

旧 `qNN_*.md` 仅作 legacy reference，不作为题面或机制真值。

## 当前状态

2024 年 Q1～Q47 已完成 **model-grounded v1**：

```text
Q1～Q11   数据结构选择题
Q12～Q22  计算机组成原理选择题
Q23～Q32  操作系统选择题
Q33～Q40  计算机网络选择题
Q41～Q47  综合应用题深度 Gate
```

本轮同时对 Canonical Source 做了逐题一致性审阅：明显错题/错选项已恢复，综合题分值与 `exam.json` 已重新对齐。年度 Source / Legacy 差异及 Candidate Rule Evidence 统一记录在 `solution_review.md`；若题解独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则直接 Stable Write 修正唯一 Owner，并回归受影响题解。