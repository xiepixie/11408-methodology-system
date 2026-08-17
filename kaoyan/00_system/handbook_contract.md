# Handbook 与 Rule 契约

本契约规定稳定资产需要说清什么，但不规定固定章节数、篇幅、YAML 或表单。自然中文能说清，就不增加结构。

> 写作原则与验收标准见 [handbook_writing_spec.md](handbook_writing_spec.md)。本文件只定义最低完成清单。

## 1. 所有 Handbook 的共同要求

### 1.1 逻辑契约

读者和 AI 应当能够快速找到：

1. **Position**：它位于哪个学科和母问题下；
2. **Boundary**：负责什么，不负责什么；
3. **Mother Model**：用什么核心模型组织内容；
4. **Owns**：本文件独立定义什么；
5. **Uses**：依赖哪些其他 Owner；
6. **Failure / Boundary Cases**：模型在哪里失效或需要分层；
7. **Compression**：怎样用一张图或一组问题复原主干。

这些信息可以自然写在前言和正文里，不要求机械填字段。

### 1.2 物理文件契约：Atlas 与深度 Handbook 分开

四种 Handbook 的解释责任不同，因此不强迫使用同一种物理格式。

#### Atlas

Atlas 的正文就是地图与导航本身，因此使用 Markdown 作为 Canonical Source：

```text
<Atlas Directory>/
├── README.md              # Canonical Atlas Source + Navigation Hub
└── assets/
    └── <Atlas>_Poster.tex # 可选：由 Atlas 派生的视觉海报
```

Atlas `README.md` 可以并且应该直接拥有：Mother Question、Scope、Foundation、Topic / Bridge / Integration 地图、依赖关系、Stop Boundary、推荐路由和当前建设状态。它不需要再建立一份同义 `.tex` 正文。

可选的 `assets/<Atlas>_Poster.tex` 只负责把 README 已经拥有的地图转换成 TikZ/排版视图。它**不能拥有 README 中不存在的定义、边界或新结论**；否则会形成第二份知识真相。

#### Topic / Bridge / Integration

需要长解释、推导、机制和例题的 Handbook 继续使用：

```text
<Handbook Directory>/
├── README.md          # Landing Page
├── <Handbook>.tex     # Canonical deep body
└── assets/            # 可选
```

编译后的阅读版统一进入 `90_publish/`。

Topic / Bridge / Integration 的 README 推荐按学生阅读顺序组织：

1. **Hook**：为什么值得打开；
2. **Mother Question**：本册解决什么；
3. **Scope / Stop Boundary**：负责什么、停在哪里；
4. **Owns / Uses**：真正需要的 Owner 关系；
5. **Read Next**：前置与相邻资产；
6. **Manual**：Canonical `.tex` 与 Published PDF；
7. **Status**：当前正文成熟度。

它们的 README 不得承载完整定义链、长推导、完整机制正文、整套例题或复制 `.tex`。

### 1.3 状态必须与物理文件事实一致

状态词义统一由 [`terminology.md`](terminology.md) §10 定义。本契约只规定状态与文件之间必须满足的关系：

- Atlas 必须显式声明 `类型：Atlas`；其 Canonical Source 就是当前 `README.md`，因此 `Atlas 工作稿 / 待人工确认 / 已采用` 不要求同目录存在 `.tex`；
- Topic / Bridge / Integration 声称 `LaTeX 工作稿 / 待人工确认 / 已采用` 时，当前目录必须能确定唯一 Canonical `.tex`；
- 声称 `已发布` 时，必须存在与对应发布源同步的 `90_publish/*.pdf`；
- Topic / Bridge / Integration 的正文仍只存在于 Markdown/README 时，只能标为 `README 旧工作稿待迁移` 或 Source。

因此：**Atlas README 可以成为稳定知识 Owner；Topic / Bridge / Integration README 不可以。** 两者不能再用同一条“README 只做 Landing”的规则处理。

自动检查规则不在本文件重复定义。唯一规则见 [`repository_integrity.md`](repository_integrity.md)：`check` 只拦截机器可以确定的错误，`audit` 只报告允许暂存的维护债务。

## 2. Atlas

Atlas 是 **Map & Navigation Hub**。它不是“缩短版 Topic”，也不是等待 LaTeX 正文补齐的空壳。

Canonical Atlas README 至少说清：

- **Why**：当前范围为什么值得单独研究，母问题是什么；
- **Where**：Topic / Bridge / Integration 分别位于什么位置；
- **Relationship**：它们依赖谁、向谁输出、哪些连接必须阻断；
- **Routing**：学生和 Agent 从当前问题应该进入哪个 Owner；
- **Foundation**：全范围反复使用、但不值得拆成独立 Topic 的共同语言；
- **Status**：哪些 Owner 已有正文，哪些仍是 Source / Candidate / 待建设。

Atlas 可以有层级：Course / Exam Atlas 负责多个 Subject Atlas 之间的地图、共享控制语言和跨学科接口；Subject Atlas 负责本学科自己的世界模型。上层 Atlas 不为了“统一”而抹平下层学科差异。

Atlas 可以使用 Markdown 表格、文本树、公式和 Mermaid。内容必须保持“地图粒度”：允许给一个足以解释路由的最小例子或边界，但不展开长证明、完整机制推导、整套题型或复杂计算。需要这些内容时，直接链接 Topic / Bridge / Integration Owner。

Atlas 的可选 LaTeX 海报只服务全景视觉，不影响 Canonical 状态。海报缺失不表示 Atlas 未完成。

## 3. Topic

Topic 应围绕一个机制回答：

- 为什么需要它；
- 有哪些对象、状态和关系；
- 什么事件触发什么变化；
- 必须保持什么不变量；
- 对象或关系的一生；
- 成本、边界和反例；
- 它向外提供什么接口。

Topic 不负责“考试三分钟没思路怎么办”。做题动作放入 Rules。

## 4. Bridge

Bridge 只需要说清：

- 接口两侧分别由谁拥有；
- 两边真正共享的数学或机制结构是什么；
- A 输出什么，经过什么翻译，B 怎样接收；
- 接口必须保持什么不变量或合法性条件；
- 一个足以验证接口的最小例子；
- 什么时候应该调用这座 Bridge；
- 哪些只是表面相似，必须停止类比。

Bridge 可以给两侧最小摘要，但必须链接 Owner，不重新讲完整 Topic，也不写成综合题集。

建立 Bridge 必须经过两道 Gate：

1. **Bridge Validity｜先判断它是不是真接口**：删掉具体题目后，是否仍存在稳定、可重复使用的 `A 输出 -> 翻译/共享结构 -> B 输入`？如果只是 B 调用 A 的既有机制，记为 `Use`；如果只是多个模块为了完成一个具体过程而依次协作，归 `Integration`。
2. **Standalone Promotion｜再判断它值不值得独立建册**：依次检查四件事：
   - **责任压力（Ownership Pressure）**：不单独建立接口 Owner 时，两侧是否会反复重复解释，或长期说不清交接责任？
   - **重复调用（Reuse）**：这条接口是否会被多个不同问题反复调用，而不是只服务一个漂亮例子？
   - **当前范围相关性**：它是否直接服务当前学习/考试主干，而不是远期扩展知识？
   - **新推理价值（New Inference）**：单独说明接口以后，是否真的能得到新的判断或起手，而不只是多一个类比？

通过第一道 Gate、未通过第二道 Gate 的内容，不建立独立 Handbook；按实际情况留作 `Use / Bridge Note / Candidate / Extension`。这些词的含义见 [`terminology.md`](terminology.md)。

## 5. Integration

Integration 应选择一个真实过程或 Canonical Problem，并说清：

- 初始问题与最终目标；
- 需要识别并调用哪些成熟 Topic / Bridge；
- 这些模块按什么顺序组合；
- 每一步由哪个 Owner 负责；
- 执行过程中有哪些分支、失败点或替代路径；
- 怎样用独立信息验证组合结果。

Integration 的主线是：

$$
\boxed{\text{Problem}\to\text{Module Recognition}\to\text{Module Composition}\to\text{Execution}\to\text{Verification}}
$$

Integration 拥有协作轨迹，不拥有参与机制本身。若删掉具体问题后没有剩下一条新的可复用接口理论，就不应把它升级成 Bridge。

## 6. Extension 与 Anti-Bridge

它们不是新的 Handbook 类型，而是稳定知识中的关系角色。

- **Extension**：真实但超出当前核心范围的结构连接。正文只保留足够指向未来的最小解释，不让高级理论挤占当前主干。
- **Anti-Bridge**：必须主动阻断的伪连接。至少说清“为什么容易混淆、真正判据是什么、哪些结论禁止互推”。

例如“概率独立 ≠ 线性无关”“正交 ≠ 概率独立”适合作为 Anti-Bridge，而不是再新建一个 Topic。

## 7. Rules

规则不是知识摘要。它必须能改变下一道题中的行为。

一条规则至少要自然说清：

- 看到什么信号时使用；
- 起手或下一步具体做什么；
- 怎样检查是否有效；
- 什么时候不适用或应该退出。

例如：

```markdown
### 分部积分前先预测复杂度

看到乘积且考虑分部积分时，正式计算前先比较两种拆法：
哪一种会让剩余积分的结构变简单？

如果两种都没有降低复杂度，先停止计算并寻找换元、恒等变形或递推结构。
```

Rules 可以只有三个区域：

```markdown
## 已采用
## 待验证
## 已否定
```

不要求为每条规则填写编号、证据数量或固定字段。复杂或有争议的规则可以附几道代表题和反例。

## 8. 什么内容不进入稳定资产

以下内容通常留在 Inbox 或直接删除：

- 刚看完课程后的复述；
- 一次偶发计算错误；
- 还没有形成具体动作的感想；
- 只对一道旧题有效的答案记忆；
- 无法说明边界的聪明口诀；
- 与现有内容重复但没有新增解释力的段落。

## 9. AI-readable，而不是 machine-schema

Handbook 既给人看，也为 AI 提供长期对齐上下文。为此应当：

- 固定核心术语；
- 明确母模型；
- 区分 Owns 与 Uses；
- 区分教材模型、考试模型和工程现实；
- 把长解释拆成清晰推理链；
- 在跨专题处提供可追踪链接。

不需要把正常中文改写成 JSON。可读、稳定、边界明确比字段齐全更重要。

## 10. 更新节奏

| 资产 | 建议节奏 |
|---|---|
| Inbox | 随时写，随时删 |
| 待验证 Rules | 做题后或晚间加入 |
| 已采用 Rules | 每周或获得新证据后更新 |
| Handbooks | 专题或阶段性更新 |
| PDF | Handbook 稳定修订后发布 |

## 11. 发布

- Atlas 的稳定地图直接写入 Canonical README；它不要求 LaTeX/PDF 才算完成；
- Topic / Bridge / Integration 的稳定深度正文写入 Canonical `.tex`，README 只做 Landing Page；
- `90_publish/` 根目录集中展示需要发布的 PDF；
- 深度 Handbook 在 `kaoyan/` 根目录运行 `python3 00_system/cognitive_system.py publish "<target.tex>"`，由安全入口检查项目范围、Landing Page、Canonical 状态、唯一 `.tex` 与发布 stem；
- Atlas 若制作视觉海报，必须由 Canonical README 派生；海报源放在 `assets/`，使用 `python3 00_system/cognitive_system.py publish-view "<Atlas>/assets/<Atlas>_Poster.tex"`，并且不得新增 README 没有的定义或边界；
- 世界模型修改必须发生在对应 Canonical Owner：Atlas 改 README，Topic / Bridge / Integration 改 `.tex`；不得只改 PDF；
- 既有 LaTeX/PDF 在完成 Ownership 梳理前标记为 `legacy-unregistered`；
- 旧长 README 只有在承载 Topic / Bridge / Integration 深度正文时才需要迁入 `.tex`。真正属于 Atlas 的地图内容保留在 Markdown；
- 新建 Canonical Topic / Bridge / Integration `.tex` 使用 `infra/latex/ipara-handbook.cls` 的正式 Handbook Family，默认 `profile=standard`；既有正文可继续使用 `kaoyan/ipara-handbook.sty` Compatibility Surface 以保障稳定编译。Family/Profile/依赖/Semantic API 与 KOMA/CTeX 技术底座统一由全局 [`infra/latex/README.md`](../../infra/latex/README.md) 拥有，本仓库仅通过 [`latex_design_system.md`](latex_design_system.md) 路由；具体字体、表格、代码、TikZ 与版心参数见 [`latex_layout_spec.md`](latex_layout_spec.md)。已有 Canonical `.tex` 不为追求视觉一致而批量重排，只在发生真实正文修订或排版/可移植性问题时切换到正式 Family API。

发布前检查 Owner、引用、编译和关键排版即可。本项目的长期认知手册没有默认四页限制。
