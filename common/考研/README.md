# 考研个人认知与考场决策系统

> **系统真正保存的，不是“我看过什么”，而是经过学习与题目证据反复检验以后，属于自己的、可执行、可更新的认知模型。**

本项目不追求制作一套百科全书式 11408 讲义。它要帮助使用者完成四件事：

$$
\text{Understand} \to \text{Solve} \to \text{Perform} \to \text{Learn}
$$

- **Understand**：形成正确、有边界、有解释力的学科模型；
- **Solve**：面对新题，知道怎样识别、起手、推进和检查；
- **Perform**：在时间、风险和注意力约束下把能力换成分数；
- **Learn**：让真实体验经过反例和新题检验后改进系统。

## 1. 只长期维护三类资产

| 资产 | 回答的问题 | 更新速度 |
|---|---|---|
| **Handbooks** | 世界到底怎样运转？ | 慢 |
| **Rules** | 做题和考试时具体怎样行动？ | 快 |
| **Inbox** | 最近真实发生了什么，哪些想法还不确定？ | 随时 |

Handbooks 包括 Atlas、Topic、Bridge 和 Integration，但物理格式按职责分开：**Atlas 的 Canonical Source 是 Markdown README**，因为它的正文就是地图、关系和导航；Topic / Bridge / Integration 的 Canonical Source 是 LaTeX (`.tex`)，同目录 README 只做 Landing Page。Rules 与 Inbox 继续使用 Markdown。

目录可以比这三类更细，但不得把目录结构变成日常录入负担。

## 2. Plane 是职责，不是额外存储

$$
\boxed{\text{Knowledge Plane}+\text{Control Plane}+\text{Learning Plane}}
\longrightarrow
\boxed{\text{Publication View}}
$$

- **Knowledge Plane** 由 Handbooks 承担，保存相对稳定的世界模型；
- **Control Plane** 由 Rules 承担，保存题目和考试中的行动规则；
- **Learning Plane** 由 Inbox 和真实练习承担，负责暴露、攻击和验证候选想法；
- **Publication View** 不是第四个 Plane，而是发布投影；Topic / Bridge / Integration 的 PDF 来自 Canonical `.tex`，Atlas 可选的 PDF/海报只视觉化 Canonical README，任何 PDF 都不是另一份知识源。

## 3. AI 的位置

AI 不替使用者建立模型。它负责缩短模型迭代周期：

$$
\text{体验} \to \text{AI 帮助说清发生了什么} \to \text{提出可证伪假设}
\to \text{寻找反例} \to \text{新题检验} \to \text{人工决定是否更新唯一 Owner}
$$

AI 可以扮演：

- **Mapper**：把新知识挂到已有母模型；
- **Socratic Tutor**：通过追问检验理解；
- **Debugger**：定位思维第一次偏离的位置；
- **Adversary**：寻找边界和最小反例；
- **Editor**：验证后更新正确 Owner，避免重复；
- **Coach**：生成少量、针对断点的诊断题。

最终决定“这条规律我是否真的相信”的只能是使用者。

## 4. 每天怎样使用

### 刚学完一个机制

1. 使用者先用自己的话解释，不先让 AI 总结；
2. AI 对照现有手册做 **Model Diff**，只指出正确主干、层次混淆和缺失连接；
3. AI 用边界情形和反例攻击这个解释；
4. 能解释旧知识、多个问题并经得住攻击的新机制，才考虑进入 Handbook；
5. 其余内容不改手册，继续做题。

### 做完一道题

1. 保留题目、自己的过程和答案；
2. AI 不先重做，而是定位思维第一次偏离正确路径的位置；
3. 判断属于模型、识别、路径、执行/检查/表达，还是考试决策问题；
4. 偶发且没有稳定机制的错误：**No Update**；
5. 可能复现的规律先写入 Inbox 或 Rules 的“待验证”区域；
6. 用少量陌生题攻击和检验，再决定保留、修改或放弃。

### 晚间或每周复盘

把真正有价值的几条记录交给 AI，检查：

1. 哪些只是一次性事件；
2. 哪些错误机制重复出现；
3. 哪些候选规则值得继续测试；
4. 哪些结果说明 Handbook 本身有误；
5. 哪些 Inbox 可以直接删除。

一天可以不修改任何 Handbook。少更新但更新得有根据，比每天产生很多规则更健康。

## 5. 发现以后改哪里

| 发现 | 去向 |
|---|---|
| 概念或机制理解错 | Topic Handbook |
| 两个专题的接口理解错 | Bridge / Integration |
| 看不出题型或结构 | Subject Rules |
| 不知道怎样起手 | Subject Rules |
| 执行、检查或表达容易失控 | Subject Rules |
| 时间分配、退出或返回策略错误 | Exam Control |
| 偶发随机错误 | No Update |
| 还不知道是不是规律 | Inbox / 待验证 |

## 6. 快慢双循环

快循环以小时或天为单位：

$$
\text{Learn} \to \text{Practice} \to \text{Problem}
\to \text{AI Diagnosis} \to \text{Candidate}
$$

慢循环以周或阶段为单位：

$$
\text{Candidate} \to \text{More Evidence} \to \text{AI Challenge}
\to \text{Human Judgment} \to \text{Canonical Update}
$$

不得把两个循环合并。每错一道题就修改正式手册，会让稳定模型不断抖动。

## 7. Handbook 的物理结构

### Atlas：Markdown 就是地图本体

```text
<Atlas Directory>/
├── README.md              # Canonical Atlas Source + Navigation Hub
└── assets/
    └── <Atlas>_Poster.tex # 可选视觉海报；不得拥有新结论
```

Atlas 要频繁改 Topic 状态、Owner 关系和路由，而且学生/Agent 需要直接点击进入下游资产，因此不再为同一地图维护第二份 `.tex` 正文。

### Topic / Bridge / Integration：LaTeX 承担深度正文

```text
<Handbook Directory>/
├── README.md          # Landing Page
├── <Handbook>.tex     # Canonical deep body
└── assets/            # 可选

90_publish/
└── <Handbook>.pdf
```

从 `common/考研/` 发布深度 Handbook：

```bash
python3 00_system/cognitive_system.py publish "<target.tex>"
```

该入口确认项目范围、Canonical 状态、唯一 Source 和发布冲突。Atlas 的可选视觉海报放在 `assets/`，使用 `python3 00_system/cognitive_system.py publish-view "<Atlas>/assets/<Atlas>_Poster.tex"`；它是派生视图，不参与知识 Ownership。

## 8. 契约文件各自负责什么

| 文件 | 唯一职责 |
|---|---|
| `architecture.md` | 拥有系统边界、三类资产和快慢循环的结构决策 |
| `terminology.md` | 拥有核心术语定义 |
| `handbook_writing_spec.md` | 拥有所有心智模型手册与专题手册的认知结构、写作原则与验收标准 |
| `latex_design_system.md` | 考研子项目的 LaTeX 路由 Stub；全局 Family/Profile/Variant、依赖与 Semantic API Owner 位于 `../latex/README.md` |
| `latex_layout_spec.md` | 拥有 LaTeX 的具体字体、版心、表格、代码、图示与视觉迁移参数 |
| `handbook_contract.md` | 拥有 Handbooks 与 Rules 的最低完成标准 |
| `evidence_promotion.md` | 拥有 Inbox、诊断和候选规则验证流程 |
| `ownership_matrix.md` | 登记稳定概念和规则的归属 |
| `agent_context_protocol.md` | 拥有 Agent 自动场景路由、Boot Core 与最小 Context Pack |
| `collaboration_workflow.md` | 拥有具体使用场景、文件更新矩阵和协作结束条件 |
| `repository_integrity.md` | 拥有 `check / audit / publish` 的机器可判定边界与仓库完整性规则 |
| `AGENTS.md` | Agent 进入仓库后的 Boot Manifest；只保留启动顺序、契约路由和必须执行的安全入口 |

其他文件只引用或简述这些规则，不另建一套定义。

## 9. 项目入口

- [快速开始一次学习协作](QUICK_START.md)
- [架构与日常更新路径](00_system/architecture.md)
- [统一术语](00_system/terminology.md)
- [手册写作规范（认知结构与验收标准）](00_system/handbook_writing_spec.md)
- [I.P.A.R.A LaTeX Design System（全局 Canonical Owner）](../latex/README.md)
- [LaTeX 开源项目 Source Reference Pool（全局 Research Log）](../latex/reference_pool.md)
- [考研 LaTeX 路由 Stub](00_system/latex_design_system.md)
- [LaTeX 视觉与布局规范](00_system/latex_layout_spec.md)
- [Handbook 与 Rule 契约](00_system/handbook_contract.md)
- [Canonical Ownership 台账](00_system/ownership_matrix.md)
- [Inbox 与规则验证协议](00_system/evidence_promotion.md)
- [具体协作与更新工作流](00_system/collaboration_workflow.md)
- [Agent 场景路由与 Context Pack](00_system/agent_context_protocol.md)
- [可重复交互入口](00_system/interaction_playbook.md)
- [通用解题控制内核](01_control/problem_solving_kernel.md)
- [Agent 启动协议与人机协作规则](AGENTS.md)
- [当前项目进度](PROGRESS.md)

Course / Subject Atlas 入口：

- [数学一](10_数学一/README.md)
- [英语一](20_英语一/README.md)
- [408](30_408/README.md)

## 10. 当前阶段

数学一与 408 均已建立 Course / Subject Atlas、Topic/Bridge/Integration 与 Rules 入口。当前物理契约是：**Atlas = Canonical Markdown Map；Topic / Bridge / Integration = README Landing + Canonical LaTeX**。历史长 README 只有在承担深度机制正文时才需要迁入 LaTeX；真正属于 Atlas 的地图内容保留在 Markdown，不再为了格式统一重复制作 `.tex`。

日常首先打开 [项目进度](PROGRESS.md)，再按当前场景进入 Handbook、Rules 或 Inbox。
