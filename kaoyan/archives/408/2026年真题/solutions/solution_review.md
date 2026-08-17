# 2026 408｜题解审阅记录

> 本文件只记录 Derived Solution 审阅中发现的 Source Gap、Legacy Difference 与模型证据；不把诊断文字塞进正式题解正文。单题技巧不能直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

## 本轮格式 Gate

Q1～Q40 统一使用：

```text
Model Anchor
-> 解题链
-> 选项判断
-> Verification
-> Compression
-> 易错边界
```

Q41～Q47 统一使用：

```text
Model Anchor
-> Problem Representation
-> Decision Points
-> Solution Chain
-> Verification
-> Compression
-> 易错边界
```

算法题 Q41 额外显式包含 `Operation Contract / State-Invariant / Why Correct / Complexity`。

## Source / Legacy Review

### Q11｜学科路由元数据

- 题目是外部排序，按 408 Profile 应属于**数据结构**。
- 旧抓取文件仍名为 `q11_计算机组成原理.md`，且旧全景索引也把 Q11 放在计组；新题解已按数据结构 Owner 路由。
- 这是 legacy metadata 问题，不影响 Canonical 题面。

### Q28｜PTE 大小为隐含条件

- 当前 Canonical 题面给出三级索引 `9/9/9` 与 12 位页内偏移，但没有单独写 PTE 大小。
- 选择 C=256K 需要采用 64 位系统常用的 `8 B/PTE`，从而 `512 × 8 B = 4 KB`，每张三级页表占一个页框。
- 新题解显式写出这个隐含条件，不伪装成题面已明说。

### Q37｜路由表缺失与答案纠正

- 当前 Canonical 图形只保留了网络拓扑，原题同时给出的 $R_1$ 初始路由表未完整进入 SVG；本轮已把路由表作为可编辑 Markdown 表补回正式卷。
- 旧抓取/旧索引把答案记为 C=5；该结果只完成了链路故障后的路由重算，没有继续执行题目明确要求的“充分路由聚合”。
- 重算后 `199.10.20.0/27` 与 `199.10.20.32/27` 共享转发出口，并可合法聚合为 `199.10.20.0/26`，因此最终条目数为 **4，答案 B**。
- 已同步更新 `solutions/q37.md`、legacy q37 答案字段与年度全景索引，避免 Derived 层出现答案分叉。

### Q43｜指令格式恢复与 legacy 数值错误

- 本轮审阅发现 Canonical Q43 表格曾与同目录 `q43_fig1.svg` / legacy 题面不一致。
- 已把正式卷中的格式恢复为：

```text
R: 0000 | rt | rs/num | OP1
I: OP2  | rt | imm8
M: OP3  | offset(12)
```

并恢复 M 型隐含 `R0/R15` 的语义。
- Legacy 解析先算出 `ABCDH + F001H = 19BCEH`，随后却写成 `R2=98CEH`；正确 16 位结果为 **9BCEH**。

### Q44｜EXTOP

- 正确最低位数为 **1 bit**：只需要区分 zero extension / sign extension 两种控制状态。
- 左移 `num` 使用零扩展，M 型带符号 `offset` 使用符号扩展，所以两者 EXTOP 不能相同。
- Legacy 题面标题写“满分 15 分”，而年度 Canonical / `exam.json` 记录 Q44 为 13 分；旧分题中四小问分值又只合计 9 分。该**分值元数据仍值得用高清原卷最终核对**，但不影响现有机制答案。

### Q45｜调度时间轴

- 采用题面字面规则直接事件模拟：P4 从 20 ms 开始运行，50 ms 时间片在 70 ms 用完，优先级 5→4；P2 因更早进入同优先级就绪队列，70～80 ms 先运行，随后 P4 80～90 ms 完成。
- 得到：22 次时钟中断、7 次 CPU 调度；首次调度 `P1=90, P2=10, P3=140, P4=20 ms`；全部进程在 225 ms 完成。
- 部分外部 legacy/grading 页面存在“P4 20～90 ms 连续运行”及“P1 剩 45 ms 却在 220 ms 完成”的内部矛盾；新题解不采纳这些与题面时间片规则冲突的二次解析。

### Q47｜初始拥塞窗口

- 当前 Canonical 给出 `ssthresh=8 MSS`，但没有显式写初始 `cwnd`。
- Q47(2)(4) 的标准数值链采用经典考试口径 `cwnd0=1 MSS`；该 Source 条件缺口统一保留在本年度 review，正式题解只在 Decision Points 中引用这一受控假设，不再新增平行 H2。
- SEQ/ACK 采用 TCP 字节序号语义：SYN/FIN 各消耗 1 个序号，纯 ACK 不消耗序号。

## Candidate Rule Evidence

- **DS**：代码选择题稳定受益于“先检查非法解引用，再检查循环推进/停止条件”。
- **CO**：指令/数据通路综合题应固定采用 `Format -> Read/Write Set -> State Delta -> Control Path`。
- **OS**：调度综合题必须先钉死 `Event -> Decision Point -> Queue mutation -> Tie break`，再画甘特图。
- **NET**：TCP 综合题使用三账本：`SEQ/ACK`、`cwnd/rwnd/FlightSize`、`RTT timeline`。

以上仅记为 Candidate Evidence；跨年份重复后再考虑晋升 Rules。