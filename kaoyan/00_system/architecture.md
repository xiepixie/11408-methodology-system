# 系统架构与日常更新路径

## 1. 设计约束

这是一个个人长期学习系统，不是多人软件平台。架构首先服从以下约束：

1. 每天记录必须足够自然，不能要求为每道题填表；
2. AI 可以加速比较、诊断和反例生成，但不能代替个人判断；
3. 稳定模型更新要慢，候选想法流动可以快；
4. 同一知识不能在 Markdown、LaTeX 和多篇手册中成为多份真相；
5. 只有确实出现维护困难时，才增加字段、模板或自动化。

因此，本项目不建设数据库，也不要求复杂 schema。

## 2. 三个 Plane、三个资产与一个发布投影

Plane 是思考职责，资产是实际维护对象：

| Plane | 逻辑资产 | 默认物理载体 | 负责什么 |
|---|---|---|---|
| Knowledge | Handbooks | **Atlas: Markdown README**；**Topic/Bridge/Integration: `.tex` + README Landing** | 保存稳定的世界模型 |
| Control | 局部训练规则 + Subject Rules | Markdown | 保存可执行的做题和考场动作；局部规则优先进入对应训练专题 |
| Learning | 专题训练 + Inbox + 真实练习 | Markdown | 用母题、变式和代表题压缩题目空间，并积累真实检验 |

**Publication View 不是第四个 Plane，也不是第四类资产。** 它只是把前三者中已经确认需要发布的内容投影成阅读视图；对 Handbook 来说，就是 `90_publish/<category>/*.pdf`（按 `math1/`, `english1/`, `408/`, `system/` 分类组织）。

这里必须区分“逻辑资产”和“文件格式”。`Atlas / Topic / Bridge / Integration` 是认知职责，不要求共用一种载体：Atlas 的责任就是地图、关系和 Routing，因此 Canonical Source 直接使用 Markdown README；Topic / Bridge / Integration 需要长机制正文，Canonical Source 使用 LaTeX，README 只做入口。

Learning Plane 不是独立知识库。Case、测试记录和反例都可以只作为 Inbox、母题与训练或待验证规则的一部分存在；只有复杂问题才单独成文。

这里固定一条重要原则：**知识与训练分文件，训练内部不再人为拆散。** 一个 Topic / Bridge / Integration 目录中，Canonical `.tex` 只拥有数学机制；同目录可以有若干按内容命名的训练 Markdown，例如 `反函数.md`、`周期性.md`、`单调性.md`。训练文档可以把母题、变式、局部技巧、起手规则、检查动作与代表题放在一起，因为这些内容在复习时本来就共同服务同一个问题族。README 负责导航，不再要求固定的 `母题与训练.md` 或 `做题规则.md`。除 README 外，专题目录中长期保留的普通 Markdown 默认视为训练文档；历史 Source / Review 应显式标注并尽量移出正式训练入口。训练 Markdown 的头部契约、规则三元组、拆分/合并信号和配图工作流由 [`topic_practice_writing_spec.md`](topic_practice_writing_spec.md) 唯一维护。

## 3. Knowledge Plane

Knowledge 回答：“世界怎样运转？”

它包括：

$$
\text{Atlas} \to \text{Topic} \to \text{Bridge} \to \text{Integration}
$$

- **Atlas**：对象、母问题和专题地图；
- **Topic**：一个机制为什么存在、怎样运转；
- **Bridge**：两个专题在哪里交接、为什么能够连接；
- **Integration**：多个成熟机制怎样共同完成一个真实过程。

Atlas 允许按范围分层。一个考试科目或课程可以有 **Course / Exam Atlas**，下面再连接多个 **Subject Atlas**。上层 Atlas 只负责地图、共享控制语言和跨学科接口，不强迫不同 Subject 共享一个“万能世界模型”。

这个层级表示观察范围，不表示内容重复。Topic 拥有机制，Bridge 只拥有接口，Integration 只拥有协作轨迹。

### Bridge 与 Integration 的判别

架构层只固定责任边界：

$$
\boxed{\text{Bridge}=\text{为什么能接}}
\qquad
\boxed{\text{Integration}=\text{怎样一起工作}}
$$

是否构成 Bridge、以及真接口是否值得独立建册，不在本文件重复定义。统一执行 [`handbook_contract.md`](handbook_contract.md) §4 的 **Bridge Validity / Standalone Promotion** 两道 Gate。

因此架构上的最小约束只有两条：

- 仅仅“B 使用 A”时保持 `Use`，不要为了连接感另建 Bridge；
- 追踪一个具体问题如何调用多个成熟模块时归 Integration，不把协作轨迹伪装成新接口。

### Extension 与 Anti-Bridge

`Extension` 和 `Anti-Bridge` 只是关系角色，不增加第五、第六种 Handbook，也不建立平行资产树。具体词义统一见 [`terminology.md`](terminology.md)；写入哪本 Handbook 由 Ownership 决定。

因此稳定 Knowledge 资产仍只有 Atlas、Topic、Bridge、Integration 四类 Handbook。

### Handbook 属于慢循环

架构层只规定：**一次学习、一道题或一条新想法不会自动改 Handbook。** 是否已有足够理由修改稳定 Owner，交给 [`collaboration_workflow.md`](collaboration_workflow.md) 的稳定写入流程和 [`evidence_promotion.md`](evidence_promotion.md) 的证据判断；本文件不维护另一套更新门槛。

## 4. Control Plane

Control 回答：“面对题目和试卷时怎样行动？”

它分为：

- **Question Control**：识别、路径、执行、检查和表达；
- **Exam Control**：进入、退出、返回、时间、风险和注意力分配。

Rule 必须足够具体，至少让人知道：

- 什么时候使用；
- 具体做什么；
- 怎样判断有效；
- 什么时候不适用或应该退出。

Rule 可以先放在“待验证”区域，不需要立即证明自己是长期规律。

规则按作用范围就近归属：

- 只服务一个具体问题族的规则，直接写进对应训练 Markdown，与母题和变式放在一起；
- 真正跨多个训练专题、多个 Topic 反复使用的规则，才进入 Subject Rules；
- 跨学科、跨考试的通用控制继续由 `01_control/problem_solving_kernel.md` 与 Exam Control 拥有。

因此 Subject Rules 不再承担“收集本学科所有局部技巧”的职责，它主要负责跨专题控制与训练专题导航。

## 5. Learning Plane

Learning 同时回答两个问题：“题目空间怎样被压缩？”以及“这次体验是否值得修改系统？”

专题训练文档负责保存稳定的问题表示、母题、变式轴、局部技巧、局部做题规则与代表题。它不是第二本 Handbook：不重新证明数学机制；其核心职责是把大量具体题压缩为少量可生成的问题族，并让“怎么识别、怎么起手、怎么检查”紧贴对应母题。文件按内容命名，不按资产类型命名。训练图形采用“图意图早记录、图资产晚生成”：正文语义成形时先声明必要视觉责任，专题集中图审后再生成派生 SVG；图形生产不成为日常写作的前置阻塞，但必要图必须在专题成熟采用前闭环。

主路径只有：

```text
体验
-> 写入 Inbox 或直接与 AI 对话
-> AI 帮助显化第一个偏离点
-> 形成可攻击的假设
-> 用反例和陌生题检验
-> 人决定 No Update / 修改 Rule / 修改 Handbook
```

Inbox 是自由区。几句话、原始草稿或一段对话摘要都可以，不要求 ID、标签、YAML 或完整分类。

Learning Plane 只负责把一次体验变成**可检验的候选**，不直接决定稳定资产怎么改。诊断术语与 No Update 的含义见 [`terminology.md`](terminology.md)；错题、证据强度和规则晋升见 [`evidence_promotion.md`](evidence_promotion.md)。

架构只坚持两条：

1. **允许 No Update。** 一次错误或一次新理解不必产生新节点；
2. **快慢循环分离。** 观察、假设、复测可以快，修改 Handbook / 已采用 Rules 必须进入稳定写入流程。

具体场景怎样读取 Context 由 [`agent_context_protocol.md`](agent_context_protocol.md) 路由；场景结束后更新哪些文件由 [`collaboration_workflow.md`](collaboration_workflow.md) 决定。

## 6. Canonical Ownership 何时启用

Ownership 是慢循环的维护规则，不是每天记录 Inbox 的前置条件。

当准备修改 Handbook 或正式 Rules 时，才需要确认：

1. 谁拥有这个概念或规则；
2. 当前文件是在 Own、Use、Bridge、Integrate，还是只记录 Extension / Anti-Bridge 关系；
3. 修改会影响哪些下游内容；
4. 发布视图是否需要稍后同步。

Inbox 中可以有重复、模糊和矛盾。Canonical 层不可以。

## 7. Handbook 与 Publication 的架构关系

具体目录、状态和发布命令统一由 [`handbook_contract.md`](handbook_contract.md) 与 [`repository_integrity.md`](repository_integrity.md) 约束。架构层只固定 Source-of-Truth：

```text
Atlas:
README.md = Canonical map + navigation
optional poster/PDF = derived visual view

Topic / Bridge / Integration:
README.md       = Landing Page + training navigation
.tex            = Canonical deep body
<训练主题>.md   = optional training topic; names follow content, not asset type
PDF             = compiled reading view
```

因此 Publication 不创造新结论，也不拥有知识。Atlas 海报只能视觉化 README 已有关系；深度 Handbook PDF 只能展示 `.tex`。这样不会因为“Markdown 好改、PDF 好看”而演化成多份可修改真相。

发布节奏应慢于 Rule，Rule 应慢于 Inbox：

```text
Inbox: 随时
Rules: 几天或每周整合
Atlas README: 拓扑/Owner/路由真实变化时更新
Topic/Bridge/Integration .tex: 专题或阶段性更新
PDF / Poster: 稳定修订后按需生成
```

PDF 不能因为排版完成就获得更高可信度。

## 8. 已接受的取舍

### 自由 Inbox，而不是结构化数据库

- **获得**：低摩擦，真实记录更容易发生；
- **放弃**：自动统计和严格查询能力；
- **重新评估条件**：只有当记录量真实造成检索困难时，再增加最少字段。

### AI 承担复杂分析，不要求用户填写复杂结构

- **获得**：保留诊断深度，同时降低日常负担；
- **风险**：不同 AI 的分析可能不一致；
- **缓解**：用 Handbooks、固定术语和协作协议作为 AI Alignment Context。

### 快慢循环分离

- **获得**：候选想法可以快速出现，稳定模型不会频繁抖动；
- **代价**：Inbox 中会暂时存在未解决问题；
- **接受理由**：延迟判断比过早沉淀更安全。

## 9. 非目标

本项目不追求：

- 为每道题建档；
- 自动维护所有标签和状态；
- 用题量或文档数量代表学习效果；
- 让 AI 直接生成“我的理解”；
- 把所有经验都保留下来；
- 开发一个独立的 AI 学习产品。

技术基础保持简单：Markdown、LaTeX/PDF、Git 和按需使用的 AI 已经足够。
