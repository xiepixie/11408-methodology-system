# 2016 年 408｜Derived Solution Layer

> 状态：Q1～Q47 已完成 `model-grounded-v1`。本目录只拥有题解，不拥有题面或知识机制；题面事实唯一来自 `../2016 年全国硕士研究生招生考试.md`，机制唯一 Owner 仍是对应 Atlas / Topic / Bridge / Integration。

## 阅读入口

- [[../2016 年全国硕士研究生招生考试|Canonical Exam Source]]
- [[solution_review|年度题解审阅与模型反馈]]
- [题解写作规范](../../../../00_system/exam_solution_authoring_spec.md)
- [题解质量保证与学生学习合同](../../../../00_system/exam_solution_quality_assurance.md)

## 2016 历史路由例外

2016 综合应用题不能套其他年份的默认题号分科。以 `00_system/exam_profiles/408.json` 为唯一机器路由：

```text
Q41      计算机网络
Q42-Q43  数据结构
Q44-Q45  计算机组成原理
Q46-Q47  操作系统
```

因此部分 legacy 文件名与真实学科不一致：

```text
q41_数据结构.md       -> Q41 实际为网络
q43_计算机组成原理.md -> Q43 实际为数据结构
q45_操作系统.md       -> Q45 实际为计组
q47_计算机网络.md     -> Q47 实际为操作系统
```

另外 Q11 legacy 文件名仍写作 `q11_计算机组成原理.md`，但客观题 Profile 的 Q1～Q11 属于数据结构。legacy 文件名只为兼容旧链接，不能反向拥有路由。

## 固定格式

Q1～Q40：

```text
Model Anchor
-> 解题链
-> 选项判断
-> Verification
-> Compression
-> 易错边界
```

Q41～Q47：

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

[[q01]] · [[q02]] · [[q03]] · [[q04]] · [[q05]] · [[q06]] · [[q07]] · [[q08]] · [[q09]] · [[q10]] · [[q11]] · [[q42]] · [[q43]]

### 计算机组成原理

[[q12]] · [[q13]] · [[q14]] · [[q15]] · [[q16]] · [[q17]] · [[q18]] · [[q19]] · [[q20]] · [[q21]] · [[q22]] · [[q44]] · [[q45]]

### 操作系统

[[q23]] · [[q24]] · [[q25]] · [[q26]] · [[q27]] · [[q28]] · [[q29]] · [[q30]] · [[q31]] · [[q32]] · [[q46]] · [[q47]]

### 计算机网络

[[q33]] · [[q34]] · [[q35]] · [[q36]] · [[q37]] · [[q38]] · [[q39]] · [[q40]] · [[q41]]

## 使用边界

- Legacy `qNN_*.md` 只作旧解析/答案参考；遇到冲突时以 Canonical Source + Exam Profile + Handbook + 独立推导为准。
- 2016 Q41 的平均传输速率按单位守恒写为 `20 KB/s = 163.84 kb/s`；legacy 中把它写成 `20.48 kbps` 属于 Derived Solution 单位错误，详见 `solution_review.md`。
- Q43 普通 partition quickselect 的 `O(n)` 应理解为期望时间；最坏枢轴序列仍可退化到 `O(n^2)`，不得用考试常用简写抹掉边界。
- 单题暴露出的做题动作先进入 Candidate Rule Evidence；若独立确认 Canonical Handbook 存在事实、机制或适用边界硬错误，则直接 Stable Write 修正唯一 Owner，并回归受影响题解。
- 学习时先独立作答，再逐层揭示 `Model Anchor -> Representation/Decision -> Solution -> Verification/Compression`；看懂完整解析不等于已经能独立调用模型。
