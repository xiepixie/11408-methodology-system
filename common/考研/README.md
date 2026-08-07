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

Handbooks 包括学科总图、专题、桥梁和综合手册。Rules 包括学科做题规则和考场决策。Inbox 可以是几句话，不要求字段、标签或固定格式。

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
- **Publication Plane** 只是前三者的发布视图，不是另一份知识源。

## 3. AI 的位置

AI 不替使用者建立模型。它负责缩短模型迭代周期：

$$
\text{体验} \to \text{AI 帮助显化} \to \text{提出假设}
\to \text{寻找反例} \to \text{新题检验} \to \text{正式沉淀}
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

## 7. 契约文件各自负责什么

| 文件 | 唯一职责 |
|---|---|
| `architecture.md` | 拥有系统边界、三类资产和快慢循环的结构决策 |
| `terminology.md` | 拥有核心术语定义 |
| `handbook_writing_spec.md` | 拥有所有心智模型手册与专题手册的认知结构、写作原则与验收标准 |
| `handbook_contract.md` | 拥有 Handbooks 与 Rules 的最低完成标准 |
| `evidence_promotion.md` | 拥有 Inbox、诊断和候选规则验证流程 |
| `ownership_matrix.md` | 登记稳定概念和规则的归属 |
| `collaboration_workflow.md` | 拥有具体使用场景、文件更新矩阵和协作结束条件 |
| `AGENTS.md` | 拥有人与 AI 的协作行为规则 |

其他文件只引用或简述这些规则，不另建一套定义。

## 8. 项目入口

- [快速开始一次学习协作](QUICK_START.md)
- [架构与日常更新路径](00_system/architecture.md)
- [统一术语](00_system/terminology.md)
- [手册写作规范（认知结构与验收标准）](00_system/handbook_writing_spec.md)
- [Handbook 与 Rule 契约](00_system/handbook_contract.md)
- [Canonical Ownership 台账](00_system/ownership_matrix.md)
- [Inbox 与规则验证协议](00_system/evidence_promotion.md)
- [具体协作与更新工作流](00_system/collaboration_workflow.md)
- [Agent 场景路由与 Context Pack](00_system/agent_context_protocol.md)
- [可重复交互入口](00_system/interaction_playbook.md)
- [通用解题控制内核](01_control/problem_solving_kernel.md)
- [人机协作规则](AGENTS.md)
- [当前项目进度](PROGRESS.md)

学科驾驶舱：

- [数学一](10_数学一/README.md)
- [英语一](20_英语一/README.md)
- [408](30_408/408%20计算机综合驾驶舱.md)

## 9. 当前阶段

408 框架、协作场景、Rules/Inbox 入口和进度脚本已经建立。当前仍未完成的是：选择一个真实专题或错题，跑通第一次“输入 -> 诊断/攻击 -> 人工决定 -> Canonical Update / No Update”的完整闭环。

日常首先打开 [项目进度](PROGRESS.md)，再按当前场景进入 Handbook、Rules 或 Inbox。
