# 人机协作与系统更新工作流

本文件回答四个问题：我们怎样开始一次协作、不同学习场景怎样使用 AI、结束时更新哪些文件、怎样知道系统进展到哪里。

## 1. 一次协作的最小闭环

每次交互不要求填表，但应尽量提供真实输入：

```text
目的
+ 当前材料
+ 自己已经做过的判断或过程
+ 希望 AI 扮演的角色（可省略）
-> AI 显化差异、断点或边界
-> 人重新判断
-> 决定 No Update / Inbox / Rules / Handbook
-> 必要时更新状态和生成进度
```

AI 开始复杂任务时应说明主要角色。默认角色按场景选择：新知识用 Mapper/Socratic Tutor，错题用 Debugger，规则验证用 Adversary，稳定更新用 Editor，训练设计用 Coach。

## 2. 三个循环

### 学习快循环：分钟到天

```text
学习或做题
-> 暴露自己的理解和过程
-> Model Diff / First Divergence
-> No Update 或 Candidate
```

快循环允许频繁对话，但默认不重构 Handbook。

### 认知慢循环：周或专题

```text
Inbox + 待验证 Rules + 新题表现
-> 找重复模式
-> 反例与竞争解释
-> 人工决定
-> 更新 Canonical Handbook / Rules
```

### 训练文档内部循环：语义先行，视觉后置

专题训练 Markdown 不要求“写一段就同步画一张图”。最佳节奏是：

```text
先写清问题表示 / 母题 / 局部规则 / 反例
-> 发现图能显著压缩推理时，立即留下规范“待补图”或“候选配图”占位
-> 继续完成本轮语义审阅与 Source Diff
-> 整个专题集中图审：去重、复用、决定是否真的值得画
-> 批量建立图源并生成 SVG
-> 视觉验收后替换占位
-> 必要图清零后再进入“已采用”
```

这里强调的是“**图意图早记录，图资产晚生成**”，而不是“把图永远拖到以后”。具体占位语法、TikZ→SVG 管线和成熟门槛见 [`topic_practice_writing_spec.md`](topic_practice_writing_spec.md)。

### 发布循环：阶段

Topic / Bridge / Integration：

```text
Canonical .tex 内容已采用
-> 检查 Owner 与依赖
-> 用项目脚本编译
-> PDF 自动进入 90_publish/
-> 更新 README Landing Page 与状态
```

Atlas 的 Canonical 内容直接在 README 更新；只有确实需要全景视觉海报时才生成派生视图。Publication 只同步已经确认的内容，不参与日常探索。

## 3. 进度从哪里看

打开项目根目录的 `PROGRESS.md`：

- “当前焦点”来自人工维护的 `CURRENT.md`；
- “资产明细”来自各 Atlas/Topic/Bridge/Integration 入口顶部的 `状态：...`；
- `PROGRESS.md` 由脚本生成，不手工修改。

Handbook 状态词义统一见 [`terminology.md`](terminology.md) §10；本工作流不再维护第二份状态词典。

这里只规定什么时候改状态：**只有物理资产或人工决定真实变化时才改。** 新建目录、写长 README、生成 PDF、做完一道题，都不能单独作为“已采用”的理由；发布同步与内容采用是两个不同事实。

## 4. 使用场景与更新动作

### 场景 A：刚学完课程、教材或视频

**怎么用系统**

1. 先打开对应 Atlas/Topic，确认已有母模型；
2. 使用者先复述自己的理解；
3. AI 做 Model Diff，只找主干、层次混淆、缺失接口和边界；
4. AI 用反例或边界问题攻击；
5. 使用者重新解释。

**结束时更新**

- 理解没有稳定新增：No Update；
- 有疑问或候选连接：对应学科 `inbox.md`，若学科没有独立 Inbox 则写入全局/408 Inbox；
- 发现 Handbook 事实错误：进入“场景 F：修改稳定模型”；
- 不因为刚看完就修改正式手册。

### 场景 A2：已有心智模型，但题目不会

用户明确要求时，AI 可以直接解答，但应使用 Model-Grounded Solver，而不是输出脱离项目语言的标准答案。

```text
读取 Atlas / Topic / Subject Rules
-> 指出 Model Anchor
-> 把题面翻译成模型对象
-> 解释路径选择
-> 给出解题链和 Verification
-> 让用户复原起手或关键转折
```

解出一道题默认 No Update。只有解题过程暴露出 Handbook 缺口、可复现的调用障碍或新的候选规则时，才进入 Inbox、Rules 或稳定更新流程。

### 场景 B：做完一道题，答案正确

正确不等于无需诊断。重点检查路径是否稳定、成本是否异常、是否依赖偶然猜中。

- 正确且路径稳定：No Update；
- 正确但慢、靠猜或无法解释：AI 定位路径/检查断点，写 Inbox 或待验证 Rule；
- 出现可迁移的新解释：先作为 Hypothesis，用陌生题攻击，不直接改 Handbook。

### 场景 C：错题或考试失分

**怎么用系统**

1. 提供题目、原始过程、答案、用时和仍记得的想法；
2. AI 不先重做，定位 First Divergence；
3. 区分事实、主要假设和竞争解释；
4. 判断模型、识别、路径、执行/检查/表达或考试决策；
5. 设计能够区分解释的最小复测。

**结束时更新**

| 结论 | 更新位置 |
|---|---|
| 偶发、不可解释、无具体改进 | No Update |
| 还不确定是否重复 | Inbox |
| 已形成可执行动作 | 若只属于一个问题族，进入对应训练 Markdown；真正跨多个训练专题时才进入 Subject Rules |
| 明确是世界模型错误 | 先记录冲突，再进入场景 F |
| 时间、退出、返回和风险错误 | Exam Control |

原题标准解答可以保存为题目资产，但不能替代错误诊断。

### 场景 D：验证一条候选规则

1. 先判断规则作用范围：局部规则打开对应训练 Markdown；跨多个训练专题的规则才打开 Subject Rules；
2. AI 生成最小反例、表面不同的新题和竞争规则；
3. 记录实际收益、失效条件和时间成本；
4. 人决定已采用、收窄后继续验证、局部保留、已否定或 No Update。

只修改对应训练文档或 Subject Rules。若验证过程中发现它其实只是某个问题族的局部技巧，就保留在对应训练 Markdown；若规则实际上揭示了机制错误，再单独启动 Handbook 更新，不把机制定义塞进训练文档或 Rules。

### 场景 E0：转译真题 / PDF / 扫描试卷

真题 Source 重建先执行 [`exam_source_agent_prompt.md`](exam_source_agent_prompt.md)，再执行 [`exam_source_conversion_spec.md`](exam_source_conversion_spec.md) 与对应 Exam Profile，不按 Handbook 导入处理。**408、数学一共用同一条 Source 重建流水线；学科差异由 Profile 和题面表达，不复制第二套规则。**

目标是得到**简单、正确、可编辑的 Canonical Exam Source**：Markdown / LaTeX / code block / Semantic SVG。工作中可以比较 PDF、高清截图和外部题库，但最终题面不保留 OCR 日志、来源争议、诊断 callout、答案或解析。成熟 Source 进入对应 Exam Archive，不再以 `80_evidence/inbox/` 作为长期 Owner。

默认顺序：

```text
确定 Exam Profile + 建立 exam.json
-> 确定目标 Exam Archive / Canonical Owner
-> Preflight 与题号 Coverage
-> 题目结构恢复
-> 原生格式转换
-> SVG 语义重建
-> Question-Driven Logic Review
-> 逐题 Fidelity Pass
-> dark/light 确定性渲染
-> 自动 Validation
-> 清理中间产物
```

完成条件固定为 `Complete + Correct + Editable + Readable + Validated`。完成后的真题以对应 Exam Archive 为唯一可修改正文 Owner；后续 Evidence、错题、Handbook / Rules 从这里引用，不反向污染题面。迁移旧位置时只保留 redirect / legacy pointer，禁止出现两份 Canonical 正文。

### 场景 E1：用心智模型批量重写真题题解

题解属于 Derived Solution Layer，不反向拥有题面或机制。执行 [`exam_solution_agent_prompt.md`](exam_solution_agent_prompt.md) + [`exam_solution_authoring_spec.md`](exam_solution_authoring_spec.md) + [`exam_solution_quality_assurance.md`](exam_solution_quality_assurance.md)，并以 `01_control/problem_solving_kernel.md` 为通用控制底座。

固定链路：

```text
Canonical Exam Question
-> Subject / Topic / Bridge 定位
-> 读取 Canonical Handbook + Subject Rules
-> legacy qNN 仅作旧解析参考
-> 独立求解
-> Model Anchor / Problem Representation / Decision / Solution / Verification / Compression
-> 写入 <year>/solutions/qNN.md
-> 年度 Validation
-> No Update / Rule Evidence / Handbook Challenge / Bridge Evidence
```

旧 `qNN_*.md` 不再被视为高质量题解 Owner，且不得复制其中可能存在 OCR 错误的题面。若真题暴露的只是候选调用规则或证据不足的模型疑点，先登记 Challenge / Candidate 并继续验证；若已经独立确认 Canonical Handbook 存在事实、机制或适用边界硬错误，则在同一维护闭环中进入 Stable Write，修正唯一 Handbook Owner 后重新验证受影响题解。Rule Promotion 与 Handbook Error Fix 不使用同一证据门槛。

### 场景 E：新增或导入一本手册

“导入”不自动等于“成为 Canonical”。外部讲义、旧 LaTeX 和 AI 生成稿首先都是输入材料。

1. **定位**：先判断 Atlas、Topic、Bridge、Integration 还是 Rules；若只是指出真实但超纲的连接或阻断伪连接，再标记为 Extension / Anti-Bridge 关系，不新建第五、第六类 Handbook；
2. **找 Owner**：检查对应 Course / Subject Atlas 和 `ownership_matrix.md`；
3. **Handbook Diff**：与当前 Owner 比较重复、新增、冲突和越界；
4. **Source 纠错**：若输入材料是用户自有、当前可编辑的原笔记，并且已独立确认存在事实、机制、适用边界或计算硬错误，则在继续迁移前直接回修原 Source；review log 同时记录“原错法 → 修正 → 受影响 Owner”。不得只在 Canonical 里写对、却让原笔记继续保留已知错误。外部不可编辑材料只记录勘误，不改原件；
5. **拆分**：Knowledge 内容进入 Handbook Owner；可复用的问题表示、变式轴、代表题、局部技巧和局部规则进入最相关专题中按内容命名的训练 Markdown；只有跨多个训练专题的 Control 才进入 Subject Rules；Evidence 留在学习证据。若 Source 自带旧 PDF/排版稿，只把它登记为发布/Source 线索，不把 Publication View 当成新的知识 Owner；
6. **人工决定**：接受哪些模型、保留哪些候选、拒绝哪些说法；
7. **纳管**：先看类型。Atlas 的稳定地图内容进入 Canonical README；Topic / Bridge / Integration 的深度正文进入 Canonical `.tex`，README 只建立/更新 Landing Page。旧 Markdown 先作为 Source 做 Diff，不机械搬运；
8. **状态**：更新该资产入口顶部的状态；
9. **依赖**：只有产品拓扑或 Owner 改变时，才更新对应 Course / Subject Atlas 与 Ownership；
10. **发布**：旧 LaTeX/PDF 先标为 legacy；Topic / Bridge / Integration 以 `.tex` 为正文 Owner，Atlas 以 README 为地图 Owner；PDF 仅是派生阅读/视觉视图，不反向拥有知识；
11. **检查**：运行 `progress --write` 和 `check`。

### 场景 F：修改稳定 Handbook

只有三类理由足够：事实/边界错误、重要机制补全、原结构已造成重复或妨碍解释。

必须更新：

1. Canonical Handbook；
2. Handbook 入口状态；
3. 受影响的 Use/Bridge/Integration。

条件更新：

- Owner 或依赖改变：`ownership_matrix.md`；
- 专题地图改变：对应 Course / Subject Atlas；
- 做题动作、题目族表示、变式轴或局部技巧改变：优先更新对应训练 Markdown；
- 真正跨多个训练专题的控制动作改变：更新 Subject Rules；
- 发布稿因此过时：标记待同步，之后进入发布循环。

### 场景 G：形成跨专题理解

本场景不重新定义 Bridge 判据。先读取 [`handbook_contract.md`](handbook_contract.md) §4，按其中 **Bridge Validity → Standalone Promotion** 两道 Gate 判断，再执行写入动作。

结果只允许落到以下位置：

- 通过两道 Gate：建立或更新 Bridge；
- 只有单向调用：记录 `Use`；
- 具体过程组合多个模块：进入 Integration；
- 真连接但当前不值得独立维护：记录 Candidate / Extension；
- 只能形成表面类比：记录 Anti-Bridge；
- 证据还不足：留在 Inbox。

无论结果是哪一种，都不在两个 Topic 中复制同一套完整解释。

### 场景 H：专题/每周复盘

1. 汇总 Inbox、当前专题训练 Markdown 中待复核的局部控制，以及 Subject Rules 的待验证候选；
2. 删除一次性、重复和无法复原的记录；
3. 找重复机制和模型冲突，并先判断规则作用域；
4. 对候选规则做反例与成本检查；
5. 人工决定局部保留、跨专题晋升、修改、否定或继续观察；
6. 更新 `CURRENT.md` 的当前焦点与下一步；
7. 重新生成 `PROGRESS.md` 并运行检查。

### 场景 I：模考与考场决策

输入应包含题序、用时、进入/退出/返回行为和最终得分。AI 先分析 Expected Score under Time Constraint，不把所有失分归为知识问题。

- 单一问题族的识别、路径、执行与检查问题进入对应 Topic / Bridge / Integration 的训练 Markdown；
- 只有同一控制跨多个训练专题反复出现并有证据支撑时，才进入 Subject Rules；
- 时间、风险、注意力和返回策略进入 Exam Control；
- 只有明确机制误解才挑战 Handbook。

### 场景 J：编译与发布 Handbook

先区分类型：Atlas 不需要 PDF 才算完成；Topic / Bridge / Integration 才进入常规正文发布链。

Topic / Bridge / Integration：

1. 确认目标 `.tex` 就是该 Handbook 的 Canonical Source；
2. 确认 Owner、状态和依赖已经同步；
3. README 只检查导航、引子、Scope 和 `.tex`/PDF 链接，不把正文复制进去；
4. 在 `kaoyan/` 根目录使用 `python3 00_system/cognitive_system.py publish "<目标.tex>"`；不要绕过 Kaoyan preflight 直接把共享编译器当作发布入口；
5. 确认编译成功，专题目录无同名 PDF，最终 PDF 位于 `90_publish/`；
6. 检查交叉引用、页面、图表和发布链接；
7. 只有真实达到对应成熟度才更新状态；
8. 生成进度并运行系统检查。

Atlas 如果制作视觉海报，海报必须完全派生自 Canonical README；海报缺失或暂未同步不降低 Atlas 的知识成熟度。

## 5. 文件更新矩阵

| 动作 | 必须更新 | 条件更新 | 不应更新 |
|---|---|---|---|
| 学完新内容 | 通常无 | Inbox | PDF、Ownership |
| 做题/错题 | Inbox 或 No Update | Rules、Exam Control | Handbook（未经验证） |
| 真题/PDF 转译 | Exam Archive 中的 Canonical Markdown + `exam.json` + 必要 Semantic SVG + Logic Review | 简短 README、复核清单 | Handbook、Rules、答案/解析、第二份 Canonical 正文 |
| 规则验证 | Subject Rules | Inbox 清理 | Topic 机制定义 |
| 导入旧 Atlas | Canonical Atlas README | Ownership、Rules | 为同一地图再造一份 `.tex` 真相 |
| 导入旧 Topic/Bridge/Integration | README Landing + Canonical `.tex` 工作稿 | Course / Subject Atlas、Ownership、Rules | 把旧 Markdown/PDF 继续当正文 Owner |
| 修改 Topic | Canonical `.tex`、README 状态/链接 | Uses/Bridge/Integration、重新编译 PDF | 把完整正文写回 README |
| 新建 Bridge | README Landing + Bridge `.tex` | Ownership、两侧链接、Anti-Bridge 边界 | 重讲两侧 Topic |
| 新建 Integration | README Landing + Integration `.tex` | Course / Subject Atlas、参与 Owner 链接 | 重新拥有局部机制 |
| 增加 Extension / Anti-Bridge | Atlas 写入 Canonical README；Topic/Bridge 写入 Canonical `.tex` | 入口导航 | 为它们新建平行 Handbook 树 |
| 发布 | `90_publish/*.pdf`、README 发布链接、状态 | 依赖链接 | Inbox、手工编辑 PDF |
| 周复盘 | CURRENT、Inbox/Rules 决策 | Handbook | 为了显得有进度而更新 |

## 6. 每次协作的结束报告

AI 结束时简要回答：

1. 这次使用了什么输入和角色；
2. 发现了什么事实、假设和反例；
3. 最终是 No Update、Candidate 还是 Canonical Update；
4. 修改了哪些文件，为什么是这些 Owner；
5. 哪些决定仍由使用者确认；
6. 下一次最小验证动作是什么。

## 7. 简单命令

```bash
python3 00_system/cognitive_system.py start <scenario> --subject <subject> --topic <topic>
python3 00_system/cognitive_system.py progress --write
python3 00_system/cognitive_system.py check
python3 00_system/cognitive_system.py publish "<Topic-or-Bridge-or-Integration.tex>"
python3 00_system/cognitive_system.py publish-view "<Atlas>/assets/<Atlas>_Poster.tex"
```

脚本不依赖第三方包，不读取私人仓库外材料，也不自动修改 Canonical 内容。
