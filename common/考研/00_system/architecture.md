# 系统架构定义 (architecture.md)

> **核心原理**：
> “学科心智模型”是在描述**世界是什么**；
> “做题控制、考试决策”是在描述**人怎样操作这个模型**；
> “个人经验演化”是在描述**前两者怎样被更新**。
>
> 三者并非平行堆叠的静态知识，而是由 **Knowledge Plane + Control Plane + Learning Plane** 构成的认知闭环系统；**Publication Plane** 则是前三者的稳定发布视图。

---

## 一、 系统四平面架构图 (Architecture Overview)

\[
\boxed{
\begin{aligned}
\text{\textbf{Knowledge Plane (理解世界)}} &: \text{Subject} \to \text{Topic} \to \text{Bridge} \to \text{Integration}\\[4pt]
\text{\textbf{Control Plane (操作模型)}} &: \text{Question Micro-Control} + \text{Exam Macro-Control}\\[4pt]
\text{\textbf{Learning Plane (进化闭环)}} &: \text{Observation} \to \text{Diagnosis} \to \text{Hypothesis} \to \text{Candidate} \to \text{Test} \to \text{Promote}\\[4pt]
\text{\textbf{Publication Plane (发布视图)}} &: \text{Working Knowledge (.md)} \longrightarrow \text{Published Manuals (.tex / .pdf)}
\end{aligned}
}
\]

---

## 二、 核心解耦原则：二维坐标定位法

系统中的任何一项知识或规则，都可以用**【横轴：知识粒度】$\times$【纵轴：认知成熟度】**进行唯一定位，彻底消除“四层目录机械混用”的问题。

### 1. 横轴：知识粒度 (Granularity Axis)
- **Subject（学科总图）**：定义学科元概念、全景图与底座模型（如 408 的 `Data -> Program -> Machine -> OS -> Network`）。
- **Topic（专题）**：深入分析单一步骤或局部机制（如 VM 的 `VA -> PTE -> PA`）。
- **Bridge（桥梁）**：专门研究两个专题交接处的接口（如 `mmap: VM <-> File`）。
- **Integration（综合）**：追踪多个机制在同一逻辑过程中的状态流转（如 `read()` 系统调用的跨子系统事件流）。

### 2. 纵轴：认知成熟度 (Maturity Axis)
- `O (Observation)`：原始现象与错题感知（存放在 `80_evidence/inbox/`）。
- `H (Hypothesis)`：归因诊断后提出的可证伪假设。
- `C (Candidate Rule)`：待验证的候选操作规则。
- `V (Validated)`：经多场景测试验证有效的操作规则。
- `K (Canonical Core)`：已正式吸收进 Knowledge/Control Plane 的标准定本。
- `Published`：已编译导出为 `.pdf` 发布视图的稳定状态。

---

## 三、 知识归属原则：Canonical Ownership

为了防止系统在扩展过程中篇幅暴涨、自我重复：

1. **唯一宿主原则 (One Concept $\to$ One Canonical Owner)**：
   - 每个元概念或公式机制只能在一本 Topic/Bridge 手册中被“拥有”（Owns）；
   - 下游手册（Bridge/Integration）或其他学科只能对其进行引用（`Use / Reference`），严禁重复全文解释。

2. **所有权矩阵维护**：
   - 每次新增概念或重构文档时，必须首先查阅并更新 `00_system/ownership_matrix.md`。

---

## 四、 存储载体分离原则 (Working Knowledge vs Published View)

- **Markdown (`.md`) = Working Knowledge (工作态知识)**：
  - 优点：文本易检索、AI 易增删、支持 git 细粒度 diff 与版本追溯、原生 Markdown 链接。
  - 职责：承载总图、规则、错题诊断、接口定义、候选修改等日常演化内容。

- **LaTeX (`.tex` $\to$ `.pdf`) = Published Handbook (发布态手册)**：
  - 优点：4 页精排一界一页、TikZ 出版级图形、完美黑白打印与公式排版。
  - 职责：只保存**已经成熟、准备发布的定本手册**。不随每日临时感悟直接修改 `.tex`，而是通过`inbox` $\to$ `validate` $\to$ `canonical md` $\to$ `tex/pdf` 的发布流水线进行周期性版本修订。
