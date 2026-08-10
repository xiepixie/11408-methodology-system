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

### 发布循环：阶段

```text
Canonical .tex 内容已采用
-> 检查 Owner 与依赖
-> 用项目脚本编译
-> PDF 自动进入 90_publish/
-> 更新 README Landing Page 与状态
```

Publication 只同步已经确认的内容，不参与日常探索。

## 3. 进度从哪里看

打开项目根目录的 `PROGRESS.md`：

- “当前焦点”来自人工维护的 `CURRENT.md`；
- “资产明细”来自各 Atlas/Topic/Bridge/Integration 入口顶部的 `状态：...`；
- `PROGRESS.md` 由脚本生成，不手工修改。

状态采用少量自然语言：

| 状态 | 含义 |
|---|---|
| 规划 | 只有母问题和位置 |
| 目录已建立，正文未建 | 已有入口和边界，没有正文 |
| 工作稿 | 正在形成模型，尚未人工采用 |
| 待人工确认 | AI 或旧材料已整理，需要使用者判断 |
| 已采用 | 当前被使用者接受为工作态 Canonical 内容 |
| 旧发布物待纳管 | 有 LaTeX/PDF，但没有完成当前 Owner、边界和事实审查 |
| 已发布 | 已采用内容存在对应发布视图 |
| 需修订 | 发现事实、边界或依赖问题，尚未处理完 |

“已发布”不是认知成熟度的替代品。“已采用”和“发布状态”必要时可以在一句状态中并列说明。

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
| 已形成可执行动作 | Subject Rules 的“待验证” |
| 明确是世界模型错误 | 先记录冲突，再进入场景 F |
| 时间、退出、返回和风险错误 | Exam Control |

原题标准解答可以保存为题目资产，但不能替代错误诊断。

### 场景 D：验证一条候选规则

1. 打开 Subject Rules 的“待验证”；
2. AI 生成最小反例、表面不同的新题和竞争规则；
3. 记录实际收益、失效条件和时间成本；
4. 人决定已采用、收窄后继续验证、局部保留、已否定或 No Update。

只修改对应 Rules。若规则实际上揭示了机制错误，再单独启动 Handbook 更新，不把机制定义塞进 Rules。

### 场景 E：新增或导入一本手册

“导入”不自动等于“成为 Canonical”。外部讲义、旧 LaTeX 和 AI 生成稿首先都是输入材料。

1. **定位**：先判断 Atlas、Topic、Bridge、Integration 还是 Rules；若只是指出真实但超纲的连接或阻断伪连接，再标记为 Extension / Anti-Bridge 关系，不新建第五、第六类 Handbook；
2. **找 Owner**：检查学科复习总览与导航和 `ownership_matrix.md`；
3. **Handbook Diff**：与当前 Owner 比较重复、新增、冲突和越界；
4. **拆分**：Knowledge、Control、Evidence、Publication 内容分别去正确位置；
5. **人工决定**：接受哪些模型、保留哪些候选、拒绝哪些说法；
6. **纳管**：Handbook 内容进入对应 Canonical `.tex`；README 只建立/更新 Landing Page。若旧正文来自 Markdown，先作为 Source 做 Diff，再迁入 `.tex`；
7. **状态**：更新该资产入口顶部的状态；
8. **依赖**：只有产品拓扑或 Owner 改变时，才更新复习总览与导航/Ownership；
9. **发布**：旧 LaTeX/PDF 先标为 legacy；新 Handbook 以 `.tex` 为正文 Owner，PDF 仅由脚本生成，不反向拥有知识；
10. **检查**：运行 `progress --write` 和 `check`。

### 场景 F：修改稳定 Handbook

只有三类理由足够：事实/边界错误、重要机制补全、原结构已造成重复或妨碍解释。

必须更新：

1. Canonical Handbook；
2. Handbook 入口状态；
3. 受影响的 Use/Bridge/Integration。

条件更新：

- Owner 或依赖改变：`ownership_matrix.md`；
- 专题地图改变：学科复习总览与导航；
- 做题动作改变：Subject Rules；
- 发布稿因此过时：标记待同步，之后进入发布循环。

### 场景 G：形成跨专题理解

先过 **Bridge Validity**，再过 **Standalone Promotion**，不能把“真连接”和“值得独立建册”混成同一个判断。

**Gate 1｜Bridge Validity**

1. 去掉具体题目后，两个独立 Owner 之间是否仍有稳定、可复用的 `A output -> translation/shared structure -> B input`？
2. 如果只是 B 调用 A 的既有机制，没有新的交接责任，记为 `Use`；
3. 如果只是多个成熟模块为了完成一个完整问题而按顺序协作，归 Integration；
4. 如果只是名称、公式或直觉相似而不能互推，标 Anti-Bridge。

**Gate 2｜Standalone Promotion**

真接口只有同时出现明显 Ownership Pressure、重复调用、当前范围相关性和新的可调用推理价值时，才独立建立 Bridge。否则保留为 Bridge Note / Candidate / Extension。

因此：

- 真接口 + 值得独立维护：Bridge；
- 真连接但只是单向调用：Use；
- 追踪一个真实过程怎样组合：Integration；
- 真实但超纲或当前不值得独立维护：Extension / Candidate；
- 表面相似但结构不同：Anti-Bridge；
- 仍只是新发现：Inbox；
- 不在两个 Topic 中各复制一份完整解释。

例如 Page Cache 的共享关系进入 VM x File Bridge，一次 `read()` 的完整轨迹进入 OS Integration。

### 场景 H：专题/每周复盘

1. 汇总 Inbox 和待验证 Rules；
2. 删除一次性、重复和无法复原的记录；
3. 找重复机制和模型冲突；
4. 对候选规则做反例与成本检查；
5. 人工决定晋升、修改、否定或继续观察；
6. 更新 `CURRENT.md` 的当前焦点与下一步；
7. 重新生成 `PROGRESS.md` 并运行检查。

### 场景 I：模考与考场决策

输入应包含题序、用时、进入/退出/返回行为和最终得分。AI 先分析 Expected Score under Time Constraint，不把所有失分归为知识问题。

- 单题操作问题进入 Subject Rules；
- 时间、风险、注意力和返回策略进入 Exam Control；
- 只有明确机制误解才挑战 Handbook。

### 场景 J：编译与发布 Handbook

1. 确认目标 `.tex` 就是该 Handbook 的 Canonical Source；
2. 确认 Owner、状态和依赖已经同步；
3. README 只检查导航、引子、Scope 和 `.tex`/PDF 链接，不把正文复制进去；
4. 从 `common/考研/` 使用 `python3 ../scripts/compile_tex.py "<目标.tex>"`；
5. 确认编译成功，专题目录无同名 PDF，最终 PDF 位于 `90_publish/` 根目录；
6. 检查交叉引用、页面、图表和发布链接；
7. 只有真实达到对应成熟度才更新状态；
8. 生成进度并运行系统检查。

## 5. 文件更新矩阵

| 动作 | 必须更新 | 条件更新 | 不应更新 |
|---|---|---|---|
| 学完新内容 | 通常无 | Inbox | PDF、Ownership |
| 做题/错题 | Inbox 或 No Update | Rules、Exam Control | Handbook（未经验证） |
| 规则验证 | Subject Rules | Inbox 清理 | Topic 机制定义 |
| 导入旧手册 | README Landing + Canonical `.tex` 工作稿 | 复习总览与导航、Ownership、Rules | 把旧 Markdown/PDF 继续当正文 Owner |
| 修改 Topic | Canonical `.tex`、README 状态/链接 | Uses/Bridge/Integration、重新编译 PDF | 把完整正文写回 README |
| 新建 Bridge | README Landing + Bridge `.tex` | Ownership、两侧链接、Anti-Bridge 边界 | 重讲两侧 Topic |
| 新建 Integration | README Landing + Integration `.tex` | 复习总览与导航、参与 Owner 链接 | 重新拥有局部机制 |
| 增加 Extension / Anti-Bridge | 对应 Handbook `.tex` 的关系段落 | README 仅在导航必要时提示 | 为它们新建平行 Handbook 树 |
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

## 7. 系统自动防线与简单命令

`python3 00_system/cognitive_system.py check` 是项目资产一致性与规则防越权的自动化防线，硬性校验以下 5 项：

1. **Handbook 包结构与状态一致性**：未建立 Canonical `<Handbook>.tex` 的 Topic/Bridge/Integration，其 `状态：...` 禁止虚报为 `已采用` / `Canonical` / `已发布`（必须标为 `legacy working draft` / `provisional model`）；
2. **README 篇幅与越权检测**：非 legacy 的 Handbook `README.md` 篇幅不得超过 200 行上限，防范 README 沦为第二份简版正文；
3. **Ownership Matrix 与唯一 Owner 冲突检查**：校验 `ownership_matrix.md` 中的文件引用真实存在；检测非 legacy 文件中是否存在相同的 H1 标题（防止对同一机制重复建立 Canonical Owner）；
4. **悬空引用与做题规则/Bridge/Integration 链接完整性**：扫描所有 Markdown（包含 `Subject Rules`、Bridge、Integration）的相对链接，确保无断链或悬空引用；
5. **`CURRENT.md` 存在性与更新状态**：确保 `CURRENT.md` 存在且包含 `# 当前焦点` 节点，防止其沦为无人维护的摆设。

常用脚本命令：

```bash
python3 00_system/cognitive_system.py start <scenario> --subject <subject> --topic <topic>
python3 00_system/cognitive_system.py progress --write
python3 00_system/cognitive_system.py check
python3 00_system/cognitive_system.py prompt model-diff
python3 00_system/cognitive_system.py prompt first-divergence
python3 00_system/cognitive_system.py prompt adversary
python3 00_system/cognitive_system.py prompt import-handbook
python3 00_system/cognitive_system.py prompt weekly-review
python3 00_system/cognitive_system.py prompt publish
```

脚本不依赖第三方包，不读取私人仓库外材料，也不自动修改 Canonical 内容。
