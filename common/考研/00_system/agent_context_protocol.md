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

Agent 不应为了显得全面而通读整个仓库。上下文加载分为 **Boot Core + Task Context**。

### L0：Boot Core

每次新的仓库任务固定建立三项启动上下文：

1. `AGENTS.md`：压缩后的项目架构、Ownership、协作与读取规则；
2. `CURRENT.md`：当前焦点、正在推进的资产和待人工决定；
3. 本文件 `00_system/agent_context_protocol.md`：场景路由与最小 Context Pack。

`AGENTS.md` 是启动清单，不要求 Agent 每次全文读取整个 `00_system/`。

只有任务触发时再升级读取权威契约：

- 稳定资产写入、导入、状态/拓扑变化：`collaboration_workflow.md`；
- Handbook/Rules 新建或重构：`handbook_contract.md`；
- 大规模 Handbook 正文打磨：`handbook_writing_spec.md`；
- Owner、重复定义和依赖：`ownership_matrix.md`；
- 错题、规则晋升、周复盘：`evidence_promotion.md`；
- 系统架构变化：`architecture.md`；
- 术语冲突：`terminology.md`；
- 脚本、`check / audit / publish` 或仓库一致性：`repository_integrity.md`。

`PROGRESS.md` 是生成型资产状态快照：涉及更新、导入、复盘、规划时读取；纯局部解题或讲解可不读。

### L1：当前项目状态

Boot Core 已经包含 `CURRENT.md`。如果本任务需要判断全局成熟度、可用资产或状态变化，再补读 `PROGRESS.md`。

### L2：学科基线

先读取对应 Course / Subject Atlas `README.md` 和 Subject Rules。显式声明 `类型：Atlas` 的 README 本身就是 Canonical Atlas Source，Agent 应直接从这里取得：

- 学科 Mother Question；
- Topic / Bridge / Integration 地图；
- Foundation 与关键关系；
- 当前 Routing 与 Stop Boundary；
- 哪些深度 Handbook 仍是规划或 Source；
- 当前有哪些待验证或已采用规则。

**不要为了调用 Atlas 再寻找一份同义 `.tex`。** Atlas 的可选海报/PDF只是视觉视图，不增加知识。只有进入 Topic / Bridge / Integration 时，才继续寻找其 Canonical `.tex`。

### L3：当前任务

若当前资产是 Atlas，直接读取其 Canonical README；若当前资产是 Topic / Bridge / Integration，则按顺序读取：

1. 当前目录的 `README.md` Landing Page；
2. 同目录或 Landing Page 指向的 Canonical `.tex`；
3. 用户提供的题目、原始过程和答案；
4. 与本场景有关的 Rules / Inbox / Source。

Topic / Bridge / Integration 如果没有 Canonical `.tex`，或者状态明确为“README 旧工作稿待迁移 / 正文未建”，Agent 必须说明当前没有成熟深度 Handbook。旧长 README 只能当 Source 使用，不能假装在调用仓库现有模型。

## 3. 场景路由表

> 场景结束时的文件更新矩阵见 [collaboration_workflow.md](collaboration_workflow.md) §5。本协议只管 Context 读取，不管写入。

| 场景 | 典型表达 | 主要角色 | 必读 Context | 默认结果 |
|---|---|---|---|---|
| `explore` | 还没有模型、想深入讨论 | Mapper + Socratic Tutor | 学科复习总览与导航、Atlas、相邻 Topic | 临时工作模型（provisional model）+ 反例 + 用户复述 |
| `model-diff` | 刚学完，这是我的理解 | Socratic Tutor + Mapper | Atlas、Topic | 主干/混淆/缺口/边界 |
| `solve` | 这题不会，按现有模型讲 | Model-Grounded Solver | Atlas、Topic、Subject Rules | 模型锚点 + 解题链 + 校验 + 复原问题 |
| `wrong` | 这是错题和原过程 | Debugger | Topic、Rules、Evidence 协议 | First Divergence + 诊断假设 + 最小复测 |
| `adversary` | 攻击这条理解/规则 | Adversary | Topic 或 Rules、已有表现 | 反例、失效条件、成本与下一次测试 |
| `practice` | 针对这个断点出题 | Coach | Topic、Rules、已确认断点 | 少量诊断题 + 每题观察目标 |
| `import` | 导入新手册/旧稿 | Mapper + Editor | Handbook Contract、Ownership、复习总览与导航 | Handbook Diff + 人工决策点 |
| `review` | 周复盘/专题复盘 | Adversary + Editor + Coach | Inbox、Rules、CURRENT、PROGRESS | 删除/继续/采用/更新建议 |
| `publish` | 编译并发布 Topic / Bridge / Integration | Editor | Canonical `.tex`、Owner、依赖、Landing Page | PDF 编译验证 + 发布链接 |

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

408 区分 Course Atlas 与四个 Subject Atlas。Agent 应按任务范围读取最小上下文：

- Course / Cross-Subject：`30_408/README.md` + `30_408/50_桥梁专题/README.md` + `30_408/60_综合专题/README.md`；
- 数据结构：`30_408/README.md` + `30_408/10_数据结构/README.md` + 数据结构 Rules；
- 计组：`30_408/README.md` + `30_408/20_计算机组成原理/README.md` + 计组 Rules；
- OS：`30_408/README.md` + `30_408/30_操作系统/README.md` + OS Rules；
- 网络：`30_408/README.md` + `30_408/40_计算机网络/README.md` + 网络 Rules。

Cross-Subject Bridge / Integration 问题只在需要时读取四科相关 Owner，不无差别加载所有 Topic。旧 408 综合复习总览入口已清退，统一由 `30_408/README.md` 路由。

### 数学一

数学一现在区分 Course Atlas 与三个 Subject Atlas。Agent 应按任务范围读取最小上下文：

- Course / Cross-Subject：`10_数学一/README.md` + `10_数学一/50_桥梁专题/README.md` + `10_数学一/60_综合专题/README.md`；
- 高等数学：`10_数学一/README.md` + `10_数学一/10_高等数学/README.md` + 数学 Rules；
- 线性代数：`10_数学一/README.md` + `10_数学一/20_线性代数/线性代数 Subject Atlas：空间、映射、表示与不变量.md` + `10_数学一/90_学科做题规则/README.md` + `10_数学一/90_学科做题规则/线性代数.md`；
- 概率论与数理统计：`10_数学一/README.md` + `10_数学一/30_概率论/README.md` + `10_数学一/90_学科做题规则/概率统计.md`。

自动路由 Subject：`math / calculus / linear-algebra / probability`。Cross-Subject Bridge 或 Integration 问题使用 `math`；单科问题优先使用对应 Subject，避免无差别加载三科世界模型。

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

## 7. Agent 的首轮反馈要求

第一次回复先给**能直接改变下一步动作的信息**，不先做长篇项目介绍：

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

