# Agent 场景路由与 Context Pack 协议

本协议解决一个问题：用户不需要每次重新介绍项目，也不需要先选择 AI 角色。Agent 根据请求识别场景，读取最少但足够的项目上下文，再沿现有心智模型工作。

## 1. 自动路由原则

用户只需自然说明正在发生什么，例如：

- “我还没有形成这个专题的模型，想和你讨论”；
- “这题不会，请按我们的模型讲”；
- “这是我的错题和过程，找第一次偏离”；
- “我怀疑这条规则有用，帮我攻击”；
- “把这本旧手册纳入系统”。

Agent 必须自动判断场景和角色。只有学科、题目或原始过程确实缺失到无法继续时，才追问最少信息。

## 2. 四层最小 Context Pack

Agent 不应为了显得全面而通读整个仓库。每次只读取与任务有关的四层：

### L0：系统契约

默认由 `AGENTS.md` 提供。需要术语或更新判断时再读：

- `00_system/terminology.md`；
- `00_system/collaboration_workflow.md`；
- `00_system/handbook_contract.md`；
- `00_system/evidence_promotion.md`。

### L1：当前项目状态

- `CURRENT.md`：当前焦点与待人工决定；
- `PROGRESS.md`：资产状态和可用 Handbook。

纯解一道题时可以只读 CURRENT；涉及更新、导入或复盘时必须读两者。

### L2：学科基线

读取对应学科复习总览与导航、Atlas 和 Subject Rules。它们告诉 Agent：

- 这门学科用什么母模型；
- 当前有哪些 Topic；
- 哪些模型只是规划，哪些已经存在；
- 做题时采用什么 Adapter；
- 当前有哪些待验证或已采用规则。

### L3：当前任务

- 最接近的 Topic Handbook；
- 必要的 Bridge/Integration；
- 用户提供的题目、原始过程和答案；
- 与本场景有关的 Inbox 或候选 Rule。

如果 Topic 只有“目录已建立，正文未建”，Agent 必须明确说明当前没有成熟 Canonical 模型。此时可以基于 Atlas、教材和讨论建立工作假设，但不能假装在调用已有 Handbook。

## 3. 场景路由表

> 场景结束时的文件更新矩阵见 [collaboration_workflow.md](collaboration_workflow.md) §5。本协议只管 Context 读取，不管写入。

| 场景 | 典型表达 | 主要角色 | 必读 Context | 默认结果 |
|---|---|---|---|---|
| `explore` | 还没有模型、想深入讨论 | Mapper + Socratic Tutor | 学科复习总览与导航、Atlas、相邻 Topic | provisional model + 反例 + 用户复述 |
| `model-diff` | 刚学完，这是我的理解 | Socratic Tutor + Mapper | Atlas、Topic | 主干/混淆/缺口/边界 |
| `solve` | 这题不会，按现有模型讲 | Model-Grounded Solver | Atlas、Topic、Subject Rules | 模型锚点 + 解题链 + 校验 + 复原问题 |
| `wrong` | 这是错题和原过程 | Debugger | Topic、Rules、Evidence 协议 | First Divergence + 诊断假设 + 最小复测 |
| `adversary` | 攻击这条理解/规则 | Adversary | Topic 或 Rules、已有表现 | 反例、失效条件、成本与下一次测试 |
| `practice` | 针对这个断点出题 | Coach | Topic、Rules、已确认断点 | 少量诊断题 + 每题观察目标 |
| `import` | 导入新手册/旧稿 | Mapper + Editor | Handbook Contract、Ownership、复习总览与导航 | Handbook Diff + 人工决策点 |
| `review` | 周复盘/专题复盘 | Adversary + Editor + Coach | Inbox、Rules、CURRENT、PROGRESS | 删除/继续/采用/更新建议 |
| `publish` | 同步 LaTeX/PDF | Editor | Canonical Owner、依赖、发布源 | 发布同步与验证 |

## 4. 三个核心学习场景

### 4.1 尚未形成心智模型：`explore`

Agent 不应直接交付一篇完整讲义。推荐顺序：

```text
确认母问题
-> 暴露用户已有直觉
-> 给出最小对象/关系/过程
-> 用一个生成性例子运行模型
-> 改变条件攻击模型
-> 用户重新解释
-> 暂存为工作假设或 No Update
```

输出必须区分：仓库已有模型、Agent 提出的工作假设、用户已经确认的理解。

### 4.2 已有模型但题目不会：`solve`

用户明确要求解答时，Agent 可以给完整解法，但必须沿模型组织：

1. **Model Anchor**：这题调用哪个 Atlas/Topic/Rule；
2. **Problem Representation**：把题面翻译成该模型中的对象、状态、关系或约束；
3. **Decision Point**：为什么选择当前路径；
4. **Solution Chain**：逐步完成解答，每一步标出调用的机制；
5. **Verification**：怎样提前发现错误；
6. **Compression**：下次看到什么信号，可以复原这条路径；
7. **Retrieval Check**：让用户不用看答案重新说出起手和关键转折。

如果已有 Handbook 与通用教材模型不同，优先使用 Handbook，并明确指出差异。若 Handbook 不完整或可疑，先声明证据边界。

### 4.3 错题诊断：`wrong`

Agent 先保护原始过程，不用标准解答覆盖它：

```text
Observable Facts
-> First Divergence
-> Related Mental Model
-> Missing / Misused / Unavailable?
-> Competing Explanation
-> Minimal Retest
-> No Update / Inbox / Candidate Rule / Handbook Challenge
```

“没掌握某个模型”不是默认结论。还要区分：

- 模型不存在或内容错误；
- 模型存在但题面信号没有触发；
- 模型被触发但路径选择错误；
- 路径正确但执行、检查或表达失控；
- 考场决策阻止了模型发挥。

## 5. 学科 Context 入口

### 408

- 总复习总览：`30_408/408 计算机综合复习总览.md`；
- 数据结构：`30_408/10_数据结构/README.md`；
- 计组：`30_408/20_计算机组成原理/README.md`；
- OS：`30_408/30_操作系统/操作系统复习总览.md`；
- 网络：`30_408/40_计算机网络/README.md`。

### 数学一

- 复习总览与导航：`10_数学一/README.md`；
- 已有概率统计 Atlas：`10_数学一/30_概率论/README.md`；
- 概率统计 Rules：`10_数学一/90_学科做题规则/概率统计.md`。

### 英语一

- 复习总览与导航：`20_英语一/README.md`；
- 当前 Topic 与 Rules 尚未形成时，Agent 必须说明这一事实。

## 6. 用户最少需要提供什么

| 场景 | 最少输入 |
|---|---|
| explore | 学科/专题 + 目前的直觉或最困惑的问题 |
| model-diff | 自己的解释 |
| solve | 题目 + 卡在哪里；已有尝试可选 |
| wrong | 题目 + 原始过程 + 自己答案；用时可选 |
| adversary | 候选理解/规则 + 已知成功或失败场景 |
| practice | 已确认断点 + 希望训练的难度/时间 |
| import | 来源文件 + 认为可能属于哪个专题 |
| review | Inbox + 待验证 Rules + 真实表现 |

用户不需要提供角色名、Owner、Plane、成熟度或更新文件列表。这些由 Agent 根据项目协议判断。

## 7. Agent 的反馈速度要求

第一次回复优先给高价值反馈，不先做长篇项目介绍：

- `solve`：先给 Model Anchor 和起手；
- `wrong`：先给 First Divergence；
- `explore`：先给母问题和第一个区分；
- `adversary`：先给最小反例；
- `import`：先给产品类型和可能 Owner。

背景说明只在它能改变判断时补充。复杂任务可以继续深入，但首屏必须让用户知道下一步做什么。

## 8. 场景结束时

Agent 必须报告：

- 这次调用了哪些现有模型；
- 哪些是仓库事实，哪些是临时假设；
- 用户是否已经确认；
- No Update、Inbox、Candidate Rule 还是 Canonical Update；
- 下一次最小检验是什么。

没有得到用户确认时，不把对话中临时形成的模型写成“已采用”。

