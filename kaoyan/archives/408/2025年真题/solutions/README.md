# 2025 年 408｜Derived Solution Layer

> 状态：Q1～Q47 已完成 `model-grounded-v1`。本目录只拥有题解，不拥有题面或知识机制；题面事实唯一来自 `../2025 年全国硕士研究生招生考试.md`，机制唯一 Owner 仍是对应 Handbook / Bridge / Integration。

## 阅读入口

- [[../2025 年全国硕士研究生招生考试|Canonical Exam Source]]
- [[solution_review|年度题解审阅与模型反馈]]
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

算法题的 `Operation Contract / State-Invariant / Why Correct / Complexity` 只作为 `Solution Chain` 内部小节，不新增平行 H2。

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

- Legacy `qNN_*.md` 只作旧解析参考，不能反向覆盖 Canonical Source、Handbook 或本目录独立推理。
- 同类信息固定放在同一 H2；审计、Source Gap、Legacy Difference 与 Candidate Evidence 统一进入 `solution_review.md`。
- 一道题暴露出的做题技巧先作为 Candidate Rule Evidence；若独立确认 Canonical Handbook 存在事实、机制或适用边界硬错误，则按 Stable Write 修正唯一 Owner，并重新验证受影响题解。
- 学习时推荐先独立作答，再逐层揭示 `Model Anchor -> Representation/Decision -> Solution -> Verification/Compression`，避免“看懂答案 = 会做”的错觉。
