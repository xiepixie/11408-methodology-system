# 系统架构定义 (architecture.md)

> **核心原理**：
> “学科心智模型”是在描述**世界是什么**；
> “做题控制、考试决策”是在描述**人怎样操作这个模型**；
> “个人经验演化”是在描述**前两者怎样被更新**。
>
> 三者并非平行堆叠的静态知识，而是由 **Knowledge Plane + Control Plane + Learning Plane** 构成的认知闭环系统；**Publication Plane** 则是前三者的稳定发布视图。

---

## 一、 系统四平面架构图 (Architecture Overview)

$$
\boxed{
\begin{aligned}
\text{\textbf{Knowledge Plane (理解世界)}} &: \text{Subject / Atlas} \to \text{Topic} \to \text{Bridge} \to \text{Integration}\\[4pt]
\text{\textbf{Control Plane (操作模型)}} &: \text{Question Micro-Control (通用九问)} + \text{Exam Macro-Control}\\[4pt]
\text{\textbf{Learning Plane (进化闭环)}} &: \text{Observation} \to \text{Diagnosis} \to \text{Hypothesis} \to \text{Candidate} \to \text{Test} \to \text{Promote}\\[4pt]
\text{\textbf{Publication Plane (发布视图)}} &: \text{Working Knowledge (.md)} \longrightarrow \text{Published Manuals (.tex / .pdf)}
\end{aligned}
}
$$

---

## 二、 知识产品分类 (Knowledge Product Types)

正式区分以下 6 种知识产品，不得把所有内容都混同命名为“方法论手册”：

| 类型 | 核心问题 | 典型稳定性 |
|---|---|---|
| **Atlas (学科总图)** | 这门学科的世界长什么样？ | 很稳定 |
| **Topic Manual (专题手册)** | 单一机制为什么存在、怎样运转？ | 稳定 |
| **Bridge (桥梁手册)** | 两个专题在哪里交接、谁负责什么？ | 稳定 |
| **Integration (综合手册)** | 多个机制怎样共同完成一个过程？ | 稳定 |
| **Practice System (训练系统)** | 做题和考试时怎样判断与行动？ | 持续生长 |
| **Evidence Base (证据库)** | 哪些观察支持或反驳某条规则？ | 持续增长 |

---

## 三、 认知成熟度标记 (Rule Maturity Tags)

内容成熟度与知识粒度是两条独立坐标：
- `O (Observation)`：原始观察
- `H (Hypothesis)`：诊断后的假设
- `C (Candidate)`：待测试候选规则
- `V (Validated)`：多场景验证有效
- `K (Canonical Core)`：标准宿主定本
- `P (Published)`：已发布视图状态
- `X (Rejected)`：否定废弃记录

---

## 四、 知识归属原则 (Canonical Ownership)

为了防止系统在扩展过程中篇幅暴涨、自我重复：

1. **唯一宿主原则 (One Concept $\to$ One Canonical Owner)**：
   - 每个元概念或公式机制只能在一本 Topic/Bridge 手册中被“拥有”（Owns）；
   - 下游手册（Bridge/Integration）或其他学科只能对其进行引用（`Use / Reference`），严禁重复全文解释。

2. **写作前置检查 5 问**：
   - 这是 Knowledge、Control、Learning/Evidence 还是 Publication 内容？
   - 它的粒度是 Subject、Topic、Bridge、Integration，还是 Rule/Case？
   - 当前 Canonical Owner 是谁？
   - 本文件是在 Own、Use、Bridge 还是 Integrate？
   - 修改是否会影响依赖它的其他文档？

3. **台账管理**：
   - 所有权以 `00_system/ownership_matrix.md` 为唯一台账。

---

## 五、 渐进式纳管原则 (Progressive Adoption)

- **Markdown (`.md`) = Working Knowledge (工作态知识)**：
  - 承载总图、规则、错题诊断、接口定义、候选修改等日常演化内容。
- **LaTeX (`.tex` $\to$ `.pdf`) = Published Handbook (发布态手册)**：
  - 只保存已经成熟、准备发布的定本手册。
  - 既有成果在 Bootstrap 阶段不得为了目录整齐而批量盲目搬迁；只在有真实内容修改时迁移。PDF 只能由对应的 Canonical LaTeX 源生成。
