# 真题题解：心智模型驱动写作规范

> 本规范拥有“如何把 Canonical Exam Source 写成高质量 Derived Solution”的稳定合同。408、数学一以及后续其他考试共用同一套方法；学科差异由 Subject Atlas / Topic / Bridge / Integration / Rules 负责，不复制第二套题解规则。
>
> 题解的学生学习责任、跨年度风格一致性、质量 Gate 与模型反馈闭环由 [`exam_solution_quality_assurance.md`](exam_solution_quality_assurance.md) 统一拥有；本文件不复制第二套 QA 规则。

## 1. 题解的身份

真题题面与题解必须分层：

```text
Canonical Exam Source = 原题事实 Owner
Handbook / Bridge / Integration = 机制与边界 Owner
Subject Rules = 题面触发、第一动作与检查 Owner
Exam Solution = Derived：把某一道题沿上述模型完整跑一遍
```

题解**不得成为新的知识 Owner**。如果题解推理暴露 Handbook 缺口，只记录 Challenge / Evidence，另走稳定写入流程；不能在题解里悄悄重定义机制。

## 2. Source-of-Truth 顺序

每道题固定按以下顺序读取：

1. 对应年度 `*_正式版.md` 中的 Canonical Question；
2. 408 Course / Subject Atlas；
3. 该题真正调用的 Topic Canonical `.tex`；
4. 必要时读取 Bridge / Integration Canonical `.tex`；
5. 对应 Subject Rules；
6. 旧 `qNN_*.md` 的答案与解析只作为 Derived Reference，用于发现遗漏、比较答案，不作为题面事实或机制 Owner。

若旧题解与 Canonical Source 冲突，以正式版题面为准；若旧题解与 Handbook 冲突，先检查 Handbook 适用边界，不能为了迁就旧答案修改模型。

## 3. 通用解题骨架

所有题解都以通用解题内核为底座：

```text
目标
-> 对象
-> 约束
-> 结构
-> 输出形态
-> 候选路径
-> 风险点
-> 校验
-> 表达
```

408 再切换为对应 Subject Adapter：

```text
数据结构：关系 -> 任务负载 -> 表示 -> 不变量 -> 操作 -> 代价
计组：状态 -> 位置 -> 路径 -> 资源 -> 时序 -> 提交 -> 代价
操作系统：对象 / 关系 / 队列 -> 事件 -> 机制 -> 策略 -> 新状态 -> 安全性 / 活性 / 代价
计算机网络：作用域 -> 名称 / 对象 -> 状态拥有者 -> 事件 -> 转移 -> 反馈 -> 代价
```

不要求把这些词机械写成九个小标题；题解必须让读者看得出这些决策实际发生了。

## 4. 每道题的最低交付结构

### 4.1 单项选择题

固定结构：

```markdown
# <考试ID>-YYYY-QNN

> 原题：[[年度正式卷#N]]

## 模型锚点
- Topic / Bridge：...
- 题目信号：...
- 第一动作：...

## 解题链
...

## 选项判断
A. ...
B. ...
...

## 校验
...

## 压缩
看到“...” -> 先“...” -> 再“...”

## 易错边界
...
```

**批量归档题解禁止省略或合并这些一级结构。** 即使题目很简单，也必须保留 `选项判断`、`校验`、`压缩`、`易错边界` 四个标题；内容可以短，但结构不能漂移。这样年度批量阅读时，读者能够在固定位置找到同一种信息。

### 4.2 填空题

固定结构：

```markdown
# <考试ID>-YYYY-QNN

> 原题：[[年度正式卷#N]]

## 模型锚点
- Topic / Bridge：...
- 题目信号：...
- 第一动作：...

## 解题链
...

## 校验
...

## 压缩
看到“...” -> 先“...” -> 再“...”

## 易错边界
...
```

填空题不设置虚假的“选项判断”。数值、表达式、区间或矩阵结果必须在 `解题链` 中明确给出最终填写内容；若答案可机器比较，可在 Frontmatter 中保存 `answer` 作为 Derived 索引，但正文推理仍是学生学习责任的唯一可读依据。

### 4.3 解答题 / 综合应用题 / 算法题

固定结构：

```markdown
# <考试ID>-YYYY-QNN

> 原题：[[年度正式卷#NN（本题 X 分）]]

## 模型锚点
...

## 问题表征
把题面对象、状态、约束和输出重新表示成当前学科的语言。

## 关键决策
说明为什么走这条路径，而不是竞争路径。

## 求解链
### (1) ...
### (2) ...
...

## 校验
至少给一个尽量独立于原计算路线的检查。

## 压缩
题目信号 -> 第一动作 -> 关键转折 -> 停止条件。

## 易错边界
列出这题最容易混淆的 1~3 个概念边界。
```

算法设计题额外必须包含：

```text
操作契约
-> 状态 / 不变量
-> 算法
-> 正确性说明
-> 适用边界
-> 复杂度
```

不能只有代码。

## 5. 模型锚点必须具体

禁止写：

- “考数据结构基础”；
- “考 Cache”；
- “考 TCP”；
- “套公式即可”。

必须写到可调用的 Owner / 机制，例如：

```text
DS09：分块查找的两级查找成本
CO-B02：VA -> page offset / VPN -> PA -> Cache index
OS03：Allocation / Need / Available 的安全状态推进
NET-B04：effective send window = min(rwnd, cwnd)
```

若一道题确实跨 Owner，最多列出真正参与推理的 2~4 个 Anchor，并说明接口；不要为了显得全面罗列整门学科。

## 6. “题目信号 -> 第一动作”是题解核心

每题必须回答：为什么一个人在考场看到这个题面时，应该想到当前模型？

合格写法：

```text
“均匀分块 + 块间顺序 + 块内顺序”
-> 把每块元素数设为 b
-> 总比较次数写成 n/b + b
-> 再优化 b
```

不合格写法：

```text
这是分块查找题，所以用分块查找公式。
```

第一动作必须可执行、可复原。

## 7. 机制必须能从模型生成

题解优先采用：

```text
Problem
-> Naive / direct interpretation
-> Constraint or failure
-> Mechanism
-> Result
```

不要把最终公式作为起点。可以压缩推导，但至少保留“为什么这个式子出现”。

## 8. 校验不是重算一遍

优先独立检查：

- DS：结构不变量、操作次数、边界数量级；
- CO：位宽/单位、状态差、地址字段、结果可表示范围；
- OS：对象引用、队列资格、Safety/Liveness、资源守恒；
- Network：Scope/Owner、bit-byte 单位、地址合法性、窗口/时延上界、字段作用域。

选择题也应给出一个快速 sanity check；综合题至少一个小问应有独立校验。

## 9. 压缩必须能用于下一题

每道题最后压成一条可复原路径：

```text
题目信号 -> 第一动作 -> 关键不变量 / 方程 -> 停止条件 / 检查
```

压缩不能变成无条件口诀。必须保留适用前提，例如：

```text
固定分配 + 局部置换 + 页面序列
-> 只在该进程页框内维护 LRU
```

而不是“页面题就画 LRU”。

## 10. 选项题必须解释错误选项为什么错

对高混淆题，错误选项往往比正确答案更有学习价值。至少说明：

- 它偷换了哪个对象/范围/状态；
- 它少了哪个前提；
- 它把哪两个相邻机制混成了一个。

纯数值选项若由同一计算链排除，可合并说明，不必人为写四段重复话。

## 11. 不得复制不可靠题面

题解文件不再维护第二份完整题面。正文只放 Canonical Source 链接和必要的“题面压缩表示”。

原因：历史抓取 `qNN_*.md` 中存在 OCR、公式、图形、变量和选项错误。Derived Solution 若复制整题，未来会再次形成双 Source。

旧 `qNN_*.md` 可以保留作为抓取/旧解析参考，新高质量题解进入年度：

```text
solutions/qNN.md
```

## 12. 元数据合同

题解 Frontmatter 最低包含：

```yaml
---
type: exam-solution
exam_id: 408-2025
question_id: 408-2025-Q01
question_number: 1
subject: 数据结构
status: model-grounded-v1
source_exam: ../2025 年全国硕士研究生招生考试.md
legacy_reference: ../q01_数据结构.md
answer: B   # 仅客观题
model_anchors:
  - DS-Atlas-Foundation
---
```

`answer`、难度、Topic、错题状态属于 Derived 层，可以存在于题解，但不能写回 Canonical Exam Source。`answer` 是否必填由 Exam Profile 的题型与该题是否具有可稳定机器比较的唯一答案决定，不能再用固定题号区间替代题型判断。

`model_anchors` 是可选的索引优化字段，不作为完成质量门；正文 `模型锚点` 才是学生与 Agent 的可读锚点。正文顶部 `> 原题：...` 也是推荐导航而非硬门槛，Canonical 来源关系由必填 `source_exam` 保证。这样避免迁移年份之间因冗余元数据产生无意义格式分叉。

## 13. 题解质量门

### 13.1 内容质量门

一题只有同时通过以下质量门才算完成：

1. **源题正确**：题面事实只来自 Canonical Exam Source；
2. **模型定位**：明确读取对应 Atlas / Topic / Rules；
3. **机制生成**：核心结论不是无解释口诀；
4. **边界处理**：至少处理本题真正存在的高风险混淆；
5. **校验**：有可执行检查；
6. **压缩**：下一题可以从信号复原路径；
7. **答案正确**：最终答案 / 数值 / 代码正确且表达满足题目要求；
8. **所有权不泄漏**：题解没有悄悄成为新的机制定义 Owner。

### 13.2 格式 / 可读性质量门（批量任务硬门槛）

批量题解除了“算对”，还必须保证**同类信息永远出现在同一位置**。不得因为题目简单、赶进度或由不同批次生成而自由发挥标题结构。

#### 单项选择题固定顺序

题号范围由 Exam Profile / 年度 `exam.json` 决定，不在本合同硬编码。

```text
头部元数据
# QID
> 原题链接
模型锚点
解题链
选项判断
校验
压缩
易错边界
```

其中 `模型锚点` 固定至少出现：

```text
Topic / Bridge
题目信号
第一动作
```

#### 填空题固定顺序

题号范围同样由 Exam Profile / 年度 `exam.json` 决定。

```text
头部元数据
# QID
> 原题链接
模型锚点
解题链
校验
压缩
易错边界
```

填空题不增加 `选项判断`，也不为了追求统一强行增加 `问题表征 / 关键决策`；若题目本身推理层级高，可在 `解题链` 内用 H3 拆分，但 H2 结构保持稳定。

#### 解答题 / 综合应用题固定顺序

```text
头部元数据
# QID
> 原题链接
模型锚点
问题表征
关键决策
求解链
校验
压缩
易错边界
```

算法题在上述骨架内额外显式出现：

```text
操作契约
状态 / 不变量
算法
正确性说明
复杂度
```

这些内容必须放在 `求解链` 内部，用 H3 或更低层级组织；不得为了算法题新增平行 H2，从而破坏整卷扫描结构。

#### 可读性约束

- 一段只承担一个推理动作；连续 4～6 行仍未换段时，优先检查是否混入第二个逻辑层次；
- 数值/状态题优先使用小表格、状态链或对齐公式，不把 6～10 个中间量塞进一段话；
- `校验` 必须独立成段，不得藏在 `解题链` 末句；
- `压缩` 必须是一条可扫描的路径，优先使用 `题目信号 -> 第一动作 -> 不变量 -> 检查`；
- `易错边界` 控制在真正影响本题判断的 1～3 个边界，不堆百科知识；
- 不使用 Emoji 作为稳定层级标记；结构依靠 Markdown 标题，而不是视觉装饰；
- 同一年度不得同时维护 `qNN.md`、`<考试ID>-YYYY-QNN.md` 等两份正文 Owner；旧别名只能是 redirect。

### 13.3 年度格式验收

批量完成后必须进行一次**整年结构检查**，至少验证：

1. `solutions/qNN.md` 覆盖 Exam Profile / 年度 `exam.json` 定义的目标题号，无漏题、无重复正文；
2. Frontmatter 必填字段完整；客观题或其他可稳定机器比较的题型按 Profile / 年度合同检查 `answer`；
3. 同题型必需标题全部存在且顺序一致；
4. 每题 `模型锚点` 都有“题目信号 / 第一动作”；
5. 原题链接、`source_exam`、`legacy_reference` 不断链；
6. 年度答案索引与 `solutions/qNN.md` 不分叉；
7. `solution_review.md` 承接 Source Gap / Legacy Difference，不把审计日志塞进每道题正文。

**只完成 47 个文件但未通过年度格式验收，不得宣称“整卷题解完成”。**

## 14. 批量工作流

```text
年度正式卷
-> 按 Exam Profile 路由 Subject
-> QNN 定位 Topic / Bridge / Integration
-> 读取 Canonical Handbook + Rules
-> 读取 legacy answer 作为参考
-> 独立求解
-> 对比旧答案
-> 生成心智模型驱动题解
-> 单题校验
-> 年度答案一致性 / 链接 / 头部元数据验证
-> 记录 Handbook Challenge / Rule Evidence
```

批量时不因为某一题有疑点停止整年：可疑题写入年度 `solution_review.md`，其余题继续。只有会污染大量后续题的系统性错误才暂停批量。

## 15. 题解反向验证 Handbook

真题题解同时是 Handbook / Rules 的 Evidence。每题完成后内部判断：

```text
No Update
Source Correction
Candidate Rule Evidence
Handbook Challenge
Bridge Evidence
Canonical Model Update
```

单题技巧不能直接晋升规则。只有重复题面信号、稳定第一动作、明确边界和真实收益形成证据后，才进入 Evidence Promotion。

但“规则需要迁移证据”不能被误读成“已经证实的 Handbook 错误也要等多年”。如果 Canonical Question 的独立推导证明 Handbook 存在事实、机制或适用边界硬错误，应先排除 Source/legacy 问题，再按 Stable Write 修改唯一 Canonical Owner，并重新验证受影响题解。证据仍不充分时才保留 `Handbook Challenge`。完整闭环由 [`exam_solution_quality_assurance.md`](exam_solution_quality_assurance.md) §6 拥有。
