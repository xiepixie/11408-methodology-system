# 真题题解质量保证与学生学习合同

> **身份：Control / QA Owner。**
>
> 本文件只拥有“高质量真题题解怎样被学生学习、怎样保持跨年度风格一致、怎样反向校验心智模型、怎样验收”的质量合同。
> 题解的知识机制仍由 Handbook / Bridge / Integration 拥有；具体写作语义仍服从 [`exam_solution_authoring_spec.md`](exam_solution_authoring_spec.md)；Agent 执行入口仍服从 [`exam_solution_agent_prompt.md`](exam_solution_agent_prompt.md)。

## 1. 题解不是答案库，而是一次可复原的模型运行

学生学真题真正需要得到的不是“这题答案是什么”，而是以下闭环：

```text
我为什么应该想到这个模型？
-> 题面怎样翻译成模型对象？
-> 为什么走这条路而不是另一条？
-> 关键状态/不变量怎样推进？
-> 我怎样在考场及时发现自己错了？
-> 下次看到什么信号能重新调用？
```

因此一份合格题解至少承担六种学习责任：

1. **定位（Locate）**：知道本题调用哪个 Model Owner，以及题面触发信号；
2. **表征（Represent）**：把自然语言题面变成对象、状态、关系、约束、路径或成本；
3. **决策（Decide）**：知道为什么选择当前方法，并能排除最危险的竞争路径；
4. **生成（Generate）**：结论能从机制、不变量和状态演化推出，而不是从答案反推解释；
5. **校验（Verify）**：拥有独立于主推导的错误检测动作；
6. **迁移（Transfer）**：把这题压缩成下次可调用的 Signal -> Action -> Invariant -> Check。

如果学生只能“看懂答案”，但遮住答案后不能复原第一动作和关键转折，这份题解仍未完成它的学习责任。

## 2. 学生使用真题的推荐节奏

题解结构要支持**渐进揭示**，而不是一上来把全部答案灌给学生。

推荐四遍使用法：

```text
第 1 遍：闭卷独立作答
第 2 遍：只看模型锚点 / 问题表征，再重新尝试
第 3 遍：查看关键决策 / 求解链，对照自己的第一次分叉
第 4 遍：遮住正文，只凭压缩 + 校验复原
```

对于已经做错的题，再追加一问：

> 我的首次分叉点是模型不存在、信号没触发、路径选错、状态更新错、检查缺失，还是表达没有形成得分链？

因此题解正文不承担个人错因诊断，但必须提供足够清楚的模型节点，使错题系统能定位首次分叉点。

## 3. 固定结构：同类信息永远出现在同一位置

### 3.1 单项选择题

题号范围由 Exam Profile / 年度 `exam.json` 决定。一级标题固定且顺序固定：

```text
模型锚点
-> 解题链
-> 选项判断
-> 校验
-> 压缩
-> 易错边界
```

不得把 `选项判断` 改成“逐项判断”“其他选项为什么不对”等平行一级标题；需要展开时放在 `选项判断` 内部。

### 3.2 填空题

题号范围由 Exam Profile / 年度 `exam.json` 决定。一级标题固定且顺序固定：

```text
模型锚点
-> 解题链
-> 校验
-> 压缩
-> 易错边界
```

填空题必须明确最终填写内容；不增加虚假的 `选项判断`，也不机械复制综合题的 `问题表征 / 关键决策`。高推理风险填空题可以在 `解题链` 内用更低层级展开。

### 3.3 解答题 / 综合应用题

题号范围由 Exam Profile / 年度 `exam.json` 决定。一级标题固定且顺序固定：

```text
模型锚点
-> 问题表征
-> 关键决策
-> 求解链
-> 校验
-> 压缩
-> 易错边界
```

算法题的 `操作契约 / 状态与不变量 / 算法 / 正确性说明 / 复杂度` 使用三级标题或 `求解链` 内部小节表达，**不再增加平行 H2**。

### 3.3 Frontmatter

机器最低字段固定为：

```yaml
---
type: exam-solution
exam_id: <exam>-YYYY
question_id: <exam>-YYYY-QNN
question_number: NN
subject: ...
status: model-grounded-v1
source_exam: ../YYYY 年全国硕士研究生招生考试.md
legacy_reference: ../qNN_*.md
answer: A   # 仅在题型具有可稳定机器比较的答案时按 Profile / 年度合同要求
---
```

`model_anchors` 可作为索引优化字段存在，但不是唯一真相，也不是完成质量门；**正文 `模型锚点` 才是学生与 Agent 可读的模型锚点**。这样避免 Frontmatter 与正文长期漂移。

正文顶部的 `> 原题：...` 是推荐导航，不作为硬质量门；Canonical 来源关系由 `source_exam` 保证。若写该链接，必须指向正式卷而不是 legacy q 文件。

## 4. 每个部分究竟应该告诉学生什么

### 4.1 模型锚点：回答“为什么想到它”

至少显式包含：

```text
Model Owner / Topic / Bridge / Rules
题目信号
第一动作
```

合格的第一动作必须是可执行动作，例如：

```text
Cache + 页大小
-> 先做 offset / index 位预算
```

而不是：

```text
这是 Cache 题，套 Cache 公式。
```

如果一道题跨多个 Owner，只列真正参与推理的 2～4 个，不列百科目录。

### 4.2 解题链 / 求解链：回答“模型怎样跑起来”

必须从对象、约束、状态或不变量开始，让公式和结论自然长出来。

优先结构：

```text
Direct / Naive Interpretation
-> Constraint / Failure
-> Mechanism / Invariant
-> State Transition
-> Result
```

数值题至少保留决定答案的关键中间量；状态机题保留状态表/时间线；地址题保留字段预算；算法题保留不变量与复杂度。

禁止：

- 只有最终公式，没有公式为何出现；
- 从标准答案倒推一段看似合理的说明；
- 把 8～10 个状态变化揉进一个长段落；
- 用“显然”“易知”跳过真正的决策步骤。

### 4.3 选项判断：回答“为什么不是那些看起来也对的答案”

选择题必须给出最终选项。

若错误选项共享同一个计算链，可以一句统一排除；若属于高混淆概念题，应指出错误选项具体偷换了：

```text
Object / Scope / State / Timing / Owner / Boundary / Unit
```

不要求为了格式机械写四段百科解释。目标是让学生识别**最危险的错误路径**。

### 4.4 问题表征：回答“题面现在变成了什么对象”

综合题在计算前必须把题面重新表达为当前学科语言：

- DS：Relation / Workload / Representation / Invariant / Cost；
- CO：State / Location / Path / Width / Resource / Timing；
- OS：Objects / Relations / Queues / Event / Mechanism / Policy；
- NET：Scope / Endpoint / State Owner / Event / Transition / Feedback。

这一节不是复述题面。它只保留会改变推理的状态和约束。

### 4.5 关键决策：回答“为什么选这条路”

至少写出一个真正影响解法的决策，例如：

```text
为什么先做地址位预算而不是先查 Cache；
为什么维护后缀极值而不是枚举所有 j；
为什么用 counting semaphore 而不是一个粗粒度 mutex；
为什么 ACK 必须按字节空间而不是按报文个数解释。
```

如果存在一个极易混淆的竞争路径，必须明确排除。

### 4.6 校验：回答“怎样尽早发现错了”

校验必须尽量独立于主推导，不是把原式再算一遍。

推荐：

- DS：结构不变量、计数守恒、极端样例、复杂度量级；
- CO：位宽、范围、单位、地址字段、结果可表示性；
- OS：Safety/Liveness、资源守恒、队列资格、状态迁移权限；
- NET：Scope、bit/byte、窗口上界、序号守恒、payload/fragment 守恒、时延数量级。

一条很短但有区分力的检查，比一段重复推导更好。

### 4.7 压缩：回答“下次如何重新调用”

固定压缩为：

```text
Signal -> First Action -> Key Invariant / Equation -> Stop / Check
```

必须保留适用条件。不能写成“页面题就画 LRU”“TCP 题就算 RTT”这种无条件口诀。

推荐在复杂题最后追加一个**复原问题**，但不新增一级标题，例如：

> 复原检查：如果把页大小改成 2 KB，哪一步必须重新判断？

这让题解从“看懂”转为“能取回”。

### 4.8 易错边界：回答“哪两个相邻概念不能再混”

只保留真正影响本题的 1～3 个边界，例如：

```text
TLB miss != page fault
Blocked -> Ready != Ready -> Running
min(rwnd,cwnd) 是在途上限，不是新增可发送量
完全二叉树 != 满二叉树
```

禁止把这一节写成额外知识百科。

## 5. 不同题型的深度预算

“统一格式”不等于“统一字数”。答案深度由**推理风险**决定，而不是题号决定。

### A. 直接概念题

目标：1 个决定性边界 + 1 个反例/校验即可。

### B. 单链计算题

目标：保留关键中间量、单位和一个独立 sanity check。

### C. 多状态 / 多层级题

必须显式画状态链、时间线、地址字段或 Scope；不能只写自然语言长段落。

### D. 算法与综合题

必须达到：

```text
操作契约
-> 状态 / 不变量
-> 候选 / 决策
-> 算法 / 状态演化
-> 正确性说明
-> 复杂度 / 代价
-> 独立校验
```

如果学生看完仍不知道“为什么这个算法不会漏情况”，则题解不合格。

## 6. 心智模型反馈闭环：题解必须能反向修系统

题解发现“题目条件可疑、现有模型解释不自然、或模型修改后需要回测”时，先调用 [`problem_model_validation.md`](problem_model_validation.md) 判断问题位于 Question、Practice、Bridge 还是 Canonical。本文件只继续负责题解 QA，不复制那套双向验证协议。

每道题完成后必须内部分类：

```text
No Update
Source Correction
Candidate Rule Evidence
Handbook Challenge
Bridge Evidence
Canonical Model Update
```

关键区别：**“单题不能随便晋升规则”不等于“已经证实的模型错误要等很多年才修”。**

### 6.1 什么时候立即修 Handbook

若真题独立推导已经证明 Canonical Handbook 存在以下硬缺陷：

- 事实错误；
- 机制方向错误；
- 适用边界写错；
- 缺失一个会导致标准真题无法生成正确答案的必要状态/接口；

则本轮不能只写 `Handbook Challenge` 后继续传播错误。应执行稳定写入：

```text
确认 Canonical Question
-> 排除 legacy / Source 错误
-> 找唯一 Handbook Owner
-> 用独立机制或第二证据确认冲突
-> 更新 Canonical Handbook
-> 检查受影响 Rules / Bridge / Integration
-> 重新验证当前题与可能受影响的已写题解
-> 必要时重新发布阅读版
```

这属于 **Canonical Model Update**。

### 6.2 什么时候只登记 Candidate

以下情况不要急着改 Handbook：

- 模型本身正确，只是学生没想到调用它；
- 某个“第一动作”可能提高做题稳定性，但尚无迁移证据；
- 单题暴露了一个方便技巧，但还不知道边界；
- 题面存在多个合理解释，证据不足。

这些先按作用域进入对应 Topic Practice、Subject Rules 的待验证证据或年度 `solution_review.md`；单一问题族的第一动作不因为来自真题就自动上移 Subject Rules。

### 6.3 Source 错误与模型错误严格分开

如果题解算不通，优先排查：

```text
Canonical Source fidelity
-> Exam Profile / routing
-> Handbook boundary
-> Derived Solution
```

不能为了让旧答案成立而修改模型，也不能为了维护模型而偷偷改题面。

## 7. 六道质量门

### 质量门 A｜源题与答案正确性

- 题面事实只来自 Canonical Exam Source；
- 客观题或其他可稳定机器比较的题型，其 `answer` 与年度答案索引一致；
- 综合题小问、单位、代码合同完整；
- Legacy 只用于交叉检查。

### 质量门 B｜模型落地

- 模型锚点可定位；
- 题目信号具体；
- 第一动作可执行；
- 公式/操作来自机制，而非记忆答案。

### 质量门 C｜教学可复原性

学生遮住答案后，能否回答：

1. 这题最先要表示什么？
2. 最关键的决策是什么？
3. 哪一步最容易错？
4. 怎样知道答案大概率对？

若不能，题解应补问题表征 / 关键决策 / 校验，而不是单纯加字数。

### 质量门 D｜迁移与提取

- 压缩能迁移到表面不同的新题；
- 易错边界不是本题专属废话；
- 必要时有一个复原问题。

### 质量门 E｜格式一致性

- 固定 H2 完整且顺序一致；
- 不出现自由发挥的平行 H2；
- Frontmatter、答案、链接不断裂；
- **整年完成态**必须存在年度 README 与 `solution_review.md`；partial 阶段不提前创建完成标记；
- **格式迁移也必须做语义回归**：新增 / 移动标题时，摘要必须从当前 `解题链 / 求解链` 重新提炼，不能按题号、知识点名或记忆生成占位文字；格式修完后再核一次答案与正文机制是否一致。

### 质量门 F｜模型反馈闭环

- Source/Legacy 差异有去向；
- 规则证据不越权晋升；
- 已证实 Handbook 缺陷不能只留在 review；
- 更新模型后重新检查受影响题解。

## 8. 自动检查与人工审阅的边界

机器可以硬检查：

- partial 阶段已有题解的题级格式/路由/链接事实；
- 整年完成态由 Exam Profile / 年度 `exam.json` 定义的完整 Coverage；
- Frontmatter 必填字段；
- Profile / 年度合同要求的可机器比较答案；
- H2 完整、唯一、顺序一致；
- `Model Owner / Topic / Bridge / Rules` 至少有一个显式锚点，且 `题目信号 / 第一动作` 存在；
- `source_exam / legacy_reference` 目标存在；
- 整年完成态的年度 `README.md / solution_review.md` 存在。

机器**不能**可靠判断：

- 推理是否真的正确；
- 模型锚点是否选对 Owner；
- 校验是否独立；
- 一条 Rule 是否已经有足够证据；
- Handbook 是否需要改。

这些必须由年度内容审阅与跨年模型审阅完成。

## 9. 跨年度一致性审阅

每完成一个年度，不只检查这一年，还要问：

```text
同一机制在不同年份是否使用同一术语？
同一题型是否出现两套第一动作？
某个旧题解是否因为新模型修正而过期？
Candidate Rule 是否已经跨年重复到值得 Promotion Review？
```

每完成 3～5 个年份，至少做一次横向抽样：每科各抽“概念题 / 数值题 / 综合题”检查模型语言是否漂移。

## 10. 交付标准

一个年度只有同时满足下面条件才可写“完成”：

```text
Profile-defined Full Coverage
+ Answer Consistency
+ Fixed Format
+ Model-Grounded
+ Independently Verified
+ Student-Reconstructable
+ Model Feedback Closed
```

其中前三项可机器质量门；后四项必须有人 / Agent 阅读。

### 11. 栏目语言合同

题解的**格式栏目统一使用中文**。不得再出现一半中文、一半英文的 H2/H3 标题。

固定映射为：

```text
模型锚点
问题表征
关键决策
解题链 / 求解链
校验
压缩
易错边界
操作契约
状态与不变量
正确性说明
复杂度
```

英文只保留在以下场景：协议/标准名（如 TCP、OSPF、IEEE 754）、代码标识符、模型编号（如 CO-03）、原题术语或确实没有自然中文替代的技术名。**不得再把英文用作题解栏目标题或流程标签。**

**最终目标不是让题解越来越长，而是让学生越来越少依赖题解。**
