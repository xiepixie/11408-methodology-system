# 统一术语

本文件只解决一个问题：让使用者和不同 AI 对关键词采用同一种理解。它不是要求日常记录填写的字段表。

## 1. 三类长期资产

### Handbooks

相对稳定的认知模型，包括 Atlas、Topic、Bridge 和 Integration。它们回答“世界怎样运转”，更新应当较慢。

物理格式按解释责任分开：Atlas 的 Canonical Source 是 `README.md`；Topic / Bridge / Integration 的 Canonical Source 是 `.tex`，同目录 README 只做 Landing Page。PDF 始终只是发布视图。

### Rules

做题和考试中的可执行动作。它们回答“什么时候做什么、怎样检查、什么时候退出”，可以包含“待验证”区域。

### Inbox

未经整理的真实输入，包括学习感受、错题过程、疑问、候选想法和 AI 对话摘要。Inbox 可以自由、重复、矛盾，也可以被删除。

### 稳定资产

允许后续学习和 Agent **直接当作当前基线调用**的内容：Canonical Handbooks 与“已采用”Rules。Inbox、Candidate、Source、旧 PDF 和临时工作模型都不是稳定资产。

“稳定”只表示修改门槛更高、必须改唯一 Owner；不表示内容永远正确。

## 2. 三个 Plane

| Plane | 含义 |
|---|---|
| Knowledge | 形成和维护世界模型 |
| Control | 形成和维护行动规则 |
| Learning | 用体验、反例和新题检验前两者 |

Publication 是前三者的发布视图，不是第四份知识。对 Topic / Bridge / Integration，通常指由 Canonical `.tex` 编译得到的 PDF；对 Atlas，可选的 PDF/海报只是 Canonical README 的视觉投影。任何发布视图都不拥有新知识。

## 3. Handbook 物理术语

### Landing Page

Topic / Bridge / Integration 目录中的 `README.md`。负责引子、Mother Question、Scope、Owns/Uses/Stop Boundary、状态、`.tex`/PDF 链接和阅读导航。它不是简化版正文。

Atlas 是例外：Atlas 的 README 同时承担导航与 Canonical 地图正文，因此不称为“只做 Landing Page”。

### Canonical Atlas Source

显式声明 `类型：Atlas` 的 `README.md`。它拥有 Mother Question、Foundation、Topic/Bridge/Integration 地图、关系和 Routing，但不展开长机制正文。

### Canonical Deep Handbook Source

Topic / Bridge / Integration 目录中的 `.tex` 文件。完整定义、机制、推导、边界、例题和压缩结构只在这里维护。

### Published View

`90_publish/` 中的阅读或视觉输出。Topic / Bridge / Integration 由 Canonical `.tex` 通过安全发布入口生成；Atlas 的可选海报只可重复 README 已有的地图语义。PDF 不得手工修改，也不得反向成为 Owner。

### Source

尚未进入当前 Canonical Owner 的输入材料。旧笔记、教材、旧 Markdown、旧 LaTeX、PDF、AI 草稿都可以是 Source。**Source 可以很有价值，但它没有修改项目定义的权力。**

### Canonical

“当前项目认定的唯一维护位置”。它不表示永远正确，只表示：如果要修改这条稳定定义，应当改这里，而不是另建第二份正文。

### Mother Question

一本 Atlas / Topic / Bridge / Integration 最核心、能约束内容取舍的问题。任何正文段落都应该能回答“它怎样帮助解决这个问题？”；答不上来时，通常说明内容越界或只是背景材料。

### Scope / Stop Boundary

- **Scope**：本册明确负责解释的范围；
- **Stop Boundary**：解释到哪里必须停止，并把后续责任交给另一个 Owner。

这两个词一起防止“为了完整”把相邻 Topic 整章复制进来。

### Foundation

由 Atlas 拥有的共用基础语言，例如全科反复使用的对象分类、表示语言或成本度量。Foundation 不是第五种 Handbook，也不与 Topic 平级。

### Handbook Diff

把一个 Source 与当前 Owner 对照，逐项判断：哪些重复、哪些真正新增、哪些冲突、哪些越界、哪些其实属于 Rules 或 Evidence。它不是重新总结 Source。

### 纳管

把旧材料从“只可参考的 Source”接入当前系统的维护链。至少要完成：找到唯一 Owner、决定内容进入 Canonical Atlas README 还是 Topic / Bridge / Integration `.tex`、更新入口与状态、确认旧发布物如何追溯。**移动文件或已有 PDF 不等于完成纳管。**

### Core / Candidate / Bridge Note

- **Core**：当前学习/考试范围内，已经决定长期保留在主干上的资产或接口角色。Core 表示优先级和范围，不自动表示“已采用”或“已发布”；
- **Candidate Core**：结构上可能值得进入 Core，但仍缺少足够的范围/真题/重复调用证据；在升级前仍按 Candidate 对待；
- **Candidate**：值得继续验证、但还没有达到稳定资产条件的候选。Candidate 不是 Canonical Owner，也不能被后续 Agent 当成已采用结论；
- **Bridge Note**：已经确认存在连接，但当前没有必要建立独立 Bridge Handbook 时，留在相关 Owner 中的一小段接口说明。

### Provisional Model

当仓库还没有成熟 Canonical Handbook 时，为了继续讨论而临时建立的**工作模型**。必须明确标成 provisional / 临时，之后仍要经过 Source Diff、反例和人工确认，不能因为 AI 写得完整就自动升级。

### Canonical Problem

一个 Integration 反复用来检验模块组合能力的代表性完整问题。它的作用是固定“哪些模块怎样协作”的主线，不表示所有题都长得一样，也不拥有参与模块的机制定义。

### Boot Core / Context Pack

- **Boot Core**：Agent 进入仓库后固定读取的最小启动文件；
- **Context Pack**：针对当前任务继续加载的最少一组相关文件。

具体读取顺序由 [`agent_context_protocol.md`](agent_context_protocol.md) 定义。

## 4. Handbook 类型

- **Atlas**：某一范围内的对象、母问题、专题关系和学习地图；可分为 Course / Exam Atlas 与 Subject Atlas，上层 Atlas 不强迫下层学科共享同一世界模型；
- **Topic**：一个机制或紧密机制簇的对象、规则、生命周期和边界；
- **Bridge**：两个专题之间稳定、可复用的共享机制、翻译规则和责任分界；
- **Integration**：多个成熟机制参与同一完整问题时的协作轨迹。

Topic 拥有机制，Bridge 拥有接口，Integration 拥有协作过程。后两者不得为了完整而重写 Topic。

### Extension

真实存在、但超出当前核心学习范围的深层连接。它不是独立 Handbook 类型，默认作为相关 Atlas / Topic / Bridge 的扩展段落存在。

### Anti-Bridge

表面名称、公式或直觉相似，但对象、关系或可推导结论不同的伪连接。它不是独立 Handbook 类型，默认记录在相关 Atlas / Bridge 的边界段落，用来阻止错误迁移。

## 5. 学习与诊断术语

### Model Diff

把使用者先说出的理解与现有 Handbook 对照，只找正确主干、层次混淆、缺失连接和边界错误。它不是重新总结整章。

### First Divergence

原始思路第一次偏离有效路径的位置。它通常早于最终算错或写错的位置。

### Candidate Rule

根据体验提出、尚待陌生题检验的行动规则。可以直接放在 Inbox，或放在 Rules 的“待验证”区域。

### Evidence

真实学习和做题结果对某个模型或规则的支持或反驳。Evidence 不等于文件数量，也不要求单独建档。

### Independent Test

能够减少“记住旧题答案”影响的新题或新场景。即时重做原题只能检查是否看懂，不能单独证明规则可迁移。

### No Update

经过判断后决定不修改 Handbooks 或 Rules。偶发错误、原因不明或没有可执行改进时，No Update 是正常且正式的结果。

### Batch Consolidation

按周或专题集中查看 Inbox，识别重复模式、攻击候选规则，并决定删除、继续观察或更新稳定资产。

## 6. 五类问题

| 类型 | 含义 | 通常去向 |
|---|---|---|
| 模型问题 | 对概念、机制或边界理解错误；稳定更新时再区分 Topic mechanism / Bridge interface / Integration composition | Handbook |
| 识别问题 | 知识存在，但没有识别题目结构 | Subject Rules |
| 路径问题 | 识别正确，但起手或路径选择不合理 | Subject Rules |
| 执行/检查/表达问题 | 方向合理，但状态维护、计算、校验或得分链失控 | Subject Rules |
| 考试决策问题 | 时间、退出、返回、风险或注意力策略错误 | Exam Control |

“粗心”“基础差”“状态不好”不是这里的正式类型。需要继续追问发生在哪一步，以及是否存在可复现机制。

## 7. Ownership 角色

- **Canonical Owner**：某一稳定概念或规则唯一允许修改其定义的位置；
- **Own**：定义语义和边界；
- **Use / Reference**：使用或给出最小摘要并链接 Owner；
- **Bridge**：只定义 Owner 之间的接口；
- **Integrate**：只追踪多个 Owner 的协作；
- **Extension**：只指出真实但超出当前核心范围的结构连接，不因此扩张主干；
- **Anti-Bridge**：只记录必须主动阻断的伪连接和禁推关系。

Ownership 只约束稳定 Handbooks 和正式 Rules，不约束自由 Inbox。Extension / Anti-Bridge 是关系角色，不新增长期资产类型。

## 8. 规则的日常状态

日常维护只需要三个自然语言状态：

- **待验证**：听起来合理，但还没有经过足够的新题攻击；
- **已采用**：使用者根据实际表现决定把它作为当前行动规则；
- **已否定**：无效、成本过高或存在更好的规则，保留简短原因即可。

如需做阶段性审计，可以使用 O/H/C/V/K/X：

- O：原始观察；
- H：可证伪假设；
- C：候选规则；
- V：已有迁移证据；
- K：已进入 Canonical Owner；
- X：已否定。

这套字母是可选分析语言，不是每条 Inbox 或每个 Handbook 的必填元数据。`published` 是独立发布状态，不属于这条序列。

## 9. AI 角色

- **Mapper**：寻找知识归属和母模型位置；
- **Socratic Tutor**：用问题迫使使用者调用自己的模型；
- **Model-Grounded Solver**：在用户明确要求解答时，沿已有心智模型完成题目并把步骤映射回模型；
- **Debugger**：找 First Divergence；
- **Adversary**：攻击假设和规则；
- **Editor**：把已确认内容放进正确 Owner；
- **Coach**：设计少量、针对断点的训练。

AI 可以切换角色，但应先说明当前角色，避免一边诊断一边突然代替使用者完成整题。

## 10. Handbook 状态用语

以下词只描述当前资产事实，不评价“学会了多少”。先看 Handbook 类型，再解释状态。

### Atlas

- **规划**：Atlas 的范围或母问题已决定，但 Canonical README 地图还没有建立；
- **Atlas 工作稿**：已存在 `类型：Atlas` 的 Canonical README，地图仍在形成；
- **待人工确认**：候选 Atlas 地图已经写入 Canonical README，等待使用者决定是否采用；
- **已采用**：使用者接受当前 Canonical README 作为现阶段地图与导航基线；
- **需修订**：Atlas 的范围、关系、Owner 或 Routing 已发现问题。

Atlas 不要求 `.tex`。可选海报/PDF 是否同步是独立发布事实，不改变 Atlas 的知识状态。

### Topic / Bridge / Integration

- **规划**：已经决定归属或 Mother Question，但还没有正式 package；
- **目录已建立，正文未建**：README Landing Page 已存在，但当前目录没有 Canonical `.tex`；
- **README 旧工作稿待迁移**：历史正文仍在 Markdown/README 中，只作为 Source；
- **LaTeX 工作稿**：唯一 Canonical `.tex` 已建立，正文仍在形成；
- **待人工确认**：需要确认的候选正文已经写入 Canonical `.tex`；
- **已采用**：使用者接受当前 Canonical `.tex` 作为现阶段工作模型；
- **需修订**：已发现事实、边界、Owner 或依赖问题。

### 发布与 legacy

- **已发布**：当前发布源已经生成同步的 `90_publish/*.pdf`；它只描述发布同步，不证明知识已经被采用；
- **legacy-unregistered / 旧发布物待纳管**：旧 Markdown/LaTeX/PDF 尚未完成当前 Ownership 与 Source-of-Truth 梳理，只作为 Source 或旧阅读版。

`已采用` 与 `已发布` 回答不同问题，必要时可以同时出现。

**不使用 `已打穿` 作为正式状态。** 它无法由仓库事实或稳定学习证据客观验收。
