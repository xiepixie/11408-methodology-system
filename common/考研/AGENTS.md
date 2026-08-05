# AGENTS: 考研个人认知与方法论系统维护协议

> **系统定位**：本目录（`common/考研/`）并非单纯的 PDF 讲义堆砌库，而是**一个可持续吸收学习、做题和考试反馈，并将其沉淀为稳定心智模型、解题控制规则与考场决策规则的个人认知系统（Personal Cognitive & Methodology System）**。
>
> **核心工作流**：
> $$
> \boxed{\text{Knowledge Plane}} \leftrightarrow \boxed{\text{Control Plane}} \quad \xleftarrow{\text{Feedback}} \quad \boxed{\text{Learning / Evidence Plane}} \quad \xrightarrow{\text{Publish}} \quad \boxed{\text{Publication Plane}}
> $$

---

## 一、 认知系统维护八大铁律 (Mandatory Rules)

1. **禁止直接将 Raw Observation 写入 Stable Core**
   - 任何做题感受或一次性失误（如“我觉得这题简单所以算错了”）只能作为原始数据存入 `80_evidence/inbox/`。
   - 未经诊断（Diagnosis）、假设（Hypothesis）与测试（Test）的观察，严禁直接改写 `00_system/`、`01_control/` 或各学科正式主干文档。

2. **新知识/新规则必须指定唯一 Canonical Owner**
   - 遵从 **One Concept/Rule $\rightarrow$ One Canonical Owner** 原则。
   - 新增内容前必须查阅 `00_system/ownership_matrix.md`；若概念已有 Owner，其他文档只能进行引用（`Use / Reference`），严禁重复全文解释。

3. **跨专题与综合层只研究接口与状态流转**
   - 专题册（Topic）负责将单一机制彻底推演穿透；
   - 桥梁册（Bridge）只研究两个专题之间的接口（Interface）；
   - 综合册（Integration）只追踪多个机制在同一状态机中的事件与状态流转，不重复定义底层数据结构与公式。

4. **新模块/讲义必须声明声明边界三元组**
   - 所有 Markdown/LaTeX 知识单元必须在文件头部标明：
     - `Scope`: 适用学科与边界范围；
     - `Owns`: 本单元唯一拥有的核心概念；
     - `Uses / Bridges`: 本单元引用的外部概念或跨界接口。

5. **做题心得与做题规则必须附带 Evidence 证据链**
   - 规则的晋升必须遵守 `00_system/evidence_promotion.md` 流程。
   - 任何晋升为 `Validated` 或 `Canonical` 的规则，必须包含 `evidence`（验证题号/样本数）与 `counterexamples`（反例记录）。

6. **修改母模型必须同步演化依赖文档**
   - 一旦更新某学科的母模型（Mother Model）或基础定义，必须检索并同步审查 `ownership_matrix.md` 中所有引用该模型的下游 Bridge 与 Integration 手册。

7. **PDF/LaTeX 是发布产物，不是经验 Inbox**
   - 每日做题反馈、微调思路与候选规则统一在 Markdown 层（`Working Knowledge`）完成迭代；
   - `.tex` 与 `.pdf` 仅作为阶段性成熟成果的发布视图（`Publication Plane`），严禁把 `.tex` 当作临时草稿本。

8. **发现冲突必须优先更新 Ownership Matrix**
   - 当不同学科或不同专题出现概念归属冲突或重复定义时，首先更新 `00_system/ownership_matrix.md` 确定唯一归属，再执行文本重构。

---

## 二、 三大 Plane 与发布视图分工

| 架构 Plane | 对应能力 | 存储形式 | 核心职责 |
|---|---|---|---|
| **Knowledge Plane** | **Understand** | `10_数学一/`, `20_英语一/`, `30_408/` | 构建正确而有生成力的世界模型（Atlas $\to$ Topic $\to$ Bridge $\to$ Integration） |
| **Control Plane** | **Solve & Perform** | `01_control/` & 各学科 `90_学科做题规则/` | 提供微观解题控制（Question Control）与宏观考场决策（Exam Control） |
| **Learning Plane** | **Learn** | `80_evidence/` | 记录原始错题观察（Observation），执行规则晋升流水线 |
| **Publication Plane** | **Publish View** | `90_publish/` (`tex/`, `pdf/`) | 将稳定成熟的 Working Knowledge 导出为精排 PDF 手册 |

---

## 三、 规则成熟度状态标记 (Rule Maturity Tags)

在 `80_evidence/` 与各学科规则库中，所有规则必须标注成熟度状态：

- `status: O` (Observation) —— 原始做题感受/错题记录（未翻译）
- `status: H` (Hypothesis) —— 已翻译为行为归因的可证伪假设
- `status: C` (Candidate) —— 已提炼为可操作的候选规则
- `status: V` (Validated) —— 经过至少 3 次不同场景验证有效
- `status: K` (Canonical) —— 已写入学科主干/控制内核的标准规则
- `status: X` (Rejected) —— 经过验证被废弃或证明无效的规则

---

## 四、 协同交互指南 (AI & User Pairing)

- **AI 在阅读本仓库时**：应首先读取 `README.md` 与 `00_system/architecture.md` 获取全局视角，遵守 `ownership_matrix.md` 避免重复写入。
- **AI 在处理错题反馈时**：应严格按照 `evidence_promotion.md` 协助用户将错题感受翻译为诊断与候选规则，写入 `80_evidence/inbox/`。
- **AI 在编写 PDF 时**：应确保 LaTeX 正文符合 `handbook_contract.md` 规范，并调用 `common/scripts/compile_tex.py` 编译与清理。
