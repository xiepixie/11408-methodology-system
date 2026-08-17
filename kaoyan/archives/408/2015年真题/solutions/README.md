# 2015 年 408｜Derived Solution Layer

> 状态：Q1～Q47 已完成 `model-grounded-v1`。本目录只拥有题解，不拥有题面或 Handbook 机制；题面事实唯一来自 `../2015 年全国硕士研究生招生考试.md`。

- Canonical Source：[[../2015 年全国硕士研究生招生考试|2015 正式卷]]
- 年度审阅：[[solution_review|solution_review]]
- 质量合同：`../../../00_system/exam_solution_quality_assurance.md`

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

## 学科导航

### 数据结构

[[q01]] · [[q02]] · [[q03]] · [[q04]] · [[q05]] · [[q06]] · [[q07]] · [[q08]] · [[q09]] · [[q10]] · [[q11]] · [[q41]] · [[q42]]

### 计算机组成原理

[[q12]] · [[q13]] · [[q14]] · [[q15]] · [[q16]] · [[q17]] · [[q18]] · [[q19]] · [[q20]] · [[q21]] · [[q22]] · [[q43]] · [[q44]]

### 操作系统

[[q23]] · [[q24]] · [[q25]] · [[q26]] · [[q27]] · [[q28]] · [[q29]] · [[q30]] · [[q31]] · [[q32]] · [[q45]] · [[q46]]

### 计算机网络

[[q33]] · [[q34]] · [[q35]] · [[q36]] · [[q37]] · [[q38]] · [[q39]] · [[q40]] · [[q47]]

## 本年度特别注意

- Q11 的 legacy 文件名仍为 `q11_计算机组成原理.md`，但按共享 408 Exam Profile 属于**数据结构**；旧文件名只保留兼容链接。
- Q18 说明“同 bank”只是冲突必要条件，还要检查请求间距。
- Q23/Q24 再次强化“硬件异常入口 vs OS 软件保存”和“普通指令也可能通过 fault 进入内核”的层次边界。
- Q41 利用有限值域把链表去重从 $O(m^2)$ 压缩到 $O(m)$。
- Q42 把邻接矩阵幂统一解释成定长 walk 计数。
- Q45 在题目抽象层只需 `full/empty` 四个计数信号量；额外 mutex 属底层容器实现条件，不机械加入同步模型。
- Q47 继续使用 `Scope -> next hop -> ARP/DHCP state`，区分端到端 IP 与当前链路 MAC。

## 使用方式

推荐学生先闭卷完成题目；若卡住，只揭示 `Model Anchor`，综合题再揭示 `Problem Representation`。完成后用 `Verification` 找自己的 First Divergence，最后遮住正文，仅凭 `Compression` 复原第一动作与关键不变量。

Source Gap、legacy correction 与 Candidate Rules Evidence 统一进入 `solution_review.md`；题解正文不承担审计日志职责。