# 2022 年 408｜Derived Solution Layer

> 状态：Q1～Q47 已完成 `model-grounded-v1`。本目录只拥有题解，不拥有题面；题面事实唯一来自 `../2022 年全国硕士研究生招生考试.md`。

## 阅读入口

- [[../2022 年全国硕士研究生招生考试|Canonical Exam Source]]
- [[solution_review|年度题解审阅记录]]
- [题解质量保证与学生学习合同](../../../../00_system/exam_solution_quality_assurance.md)

## 固定格式

选择题 Q1～Q40：

```text
Model Anchor
-> 解题链
-> 选项判断
-> Verification
-> Compression
-> 易错边界
```

综合题 Q41～Q47：

```text
Model Anchor
-> Problem Representation
-> Decision Points
-> Solution Chain
-> Verification
-> Compression
-> 易错边界
```

## 逐题导航

### 数据结构

[[q01]] · [[q02]] · [[q03]] · [[q04]] · [[q05]] · [[q06]] · [[q07]] · [[q08]] · [[q09]] · [[q10]] · [[q11]] · [[q41]] · [[q42]]

### 计算机组成原理

[[q12]] · [[q13]] · [[q14]] · [[q15]] · [[q16]] · [[q17]] · [[q18]] · [[q19]] · [[q20]] · [[q21]] · [[q22]] · [[q43]] · [[q44]]

### 操作系统

[[q23]] · [[q24]] · [[q25]] · [[q26]] · [[q27]] · [[q28]] · [[q29]] · [[q30]] · [[q31]] · [[q32]] · [[q45]] · [[q46]]

### 计算机网络

[[q33]] · [[q34]] · [[q35]] · [[q36]] · [[q37]] · [[q38]] · [[q39]] · [[q40]] · [[q47]]

## 使用边界

- Legacy `qNN_*.md` 只作为旧解析参考，不能反向覆盖 Canonical 题面或本目录独立推理。
- 单题暴露出的做题动作先写入 `solution_review.md` 作为 Candidate Rule Evidence，跨题稳定后再走 Evidence Promotion；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则直接 Stable Write 修正唯一 Owner，并回归受影响题解。
- 发现 Source 与题目逻辑/答案发生硬冲突时，先修 Source，再写/修题解；不得为了迁就旧答案在题解里制造第二套题面。