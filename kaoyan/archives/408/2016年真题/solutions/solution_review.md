# 2016 年 408｜题解与模型反馈审阅

> 本文件只记录 Derived Solution 阶段发现的 Source/Profile/Legacy 差异与模型证据；正式题解保持学生可读。单题技巧不直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并重新验证受影响题解。

## 1. 年度结论

2016 Q1～Q47 已完成 `model-grounded-v1`：

```text
47/47 Coverage
+ Q1-Q40 Answer Consistency
+ Historical Routing Override Applied
+ Fixed QA Structure
+ Independent Verification
+ Model Feedback Review
```

2016 是 408 历史路由的重要异常年：

```text
Q41      计算机网络
Q42-Q43  数据结构
Q44-Q45  计算机组成原理
Q46-Q47  操作系统
```

题解 frontmatter 与年度 README 均以 Exam Profile 为准，不再受 legacy 文件名误导。

## 2. Source / Profile / Legacy Review

### Q11｜legacy 学科文件名错误

Q11 是外部排序，按长期稳定客观题路由属于**数据结构**；legacy 文件仍名为 `q11_计算机组成原理.md`。

处理：

```text
Canonical solution subject = 数据结构
legacy_reference            = 保留旧文件名兼容
```

不改写题面。

### Q41｜历史综合题路由 + 速率单位修正

legacy 文件名把 Q41 放在数据结构，但题目完整讨论 TCP 握手、`rwnd/cwnd`、RTT 与连接释放，Profile 正确路由为**计算机网络**。

更重要的是，legacy 解析在第 (3) 问写出：

```text
20 KB/s = 20.48 kbps
```

这是 bit/byte 单位换算错误。五轮发送量：

$$1+2+4+8+5=20\text{ KB},$$

5 个 RTT = 1 s，因此：

$$20\text{ KB/s}=20\times1024\times8\text{ bit/s}=163.84\text{ kb/s}.$$

新题解保留 `20 KB/s` 作为主答案，并明确换算为 `163.84 kb/s`。这是 **Legacy Difference / Derived Solution Correction**，不需要改 Handbook。

### Q43｜历史路由 + Quickselect 复杂度边界

legacy 文件名将 Q43 标为计组，实际是数据结构算法设计题。

旧解析只写“时间 $O(n)$、空间 $O(1)$”。新题解收紧为：

```text
普通 partition quickselect
-> expected O(n)
-> worst O(n^2)
-> iterative extra space O(1)
```

并把“先锁 cardinality -> 最大化 sum gap -> 只求 rank boundary”作为真正生成算法的模型链。没有把考试常用简写冒充成最坏界证明。

### Q45｜历史路由

legacy 文件名为操作系统，但本题问 TLB、物理地址字段、Cache 映射、Cache miss/page fault 成本与写策略，Profile 路由为**计算机组成原理**。

新题解固定：

```text
VA -> VPN|offset
-> TLB
-> PA -> PFN|offset
-> Cache tag|set|block offset
```

避免 OS/CO 因“page”一词发生 Owner 混淆。

### Q47｜历史路由 + legacy 正文残损

legacy 文件名为计算机网络，实际是 FAT/目录/文件簇访问，Profile 路由为**操作系统**。

legacy 解析正文在现存文件中严重残损，新题解从 Canonical Source + Semantic SVG 独立恢复：

```text
dir  -> dir1:48
dir1 -> file1:100, file2:200
file1 chain = 100 -> 106 -> 108
file2 chain = 200 -> 201 -> 202
```

并独立推出：

```text
FAT max = 128 KB
max file = 256 MB
FAT[100] = 106
FAT[106] = 108
read byte 5000 -> disk clusters 48, 106
```

## 3. 代表性质量改进

### DS｜从局部模拟升级为不变量/上下界

- Q3：不是手工试轨道，而是“每条 FIFO 必须形成递增子序列”；`8>4>2>1` 给出 4 轨下界，再给 4 轨构造闭合最优性。
- Q24 虽属 OS，但同样使用“资源 lane + 下界/构造”而不是只画一个偶然甘特图。
- Q42：用 `E=km=n-1` 同时生成叶数与高度极值结构。
- Q43：先证明最优集合结构，再用 rank boundary 生成 quickselect。

### CO｜成本/地址 Owner 分层

- Q18：PC 最小位数与 IR 指令长度分账；对齐只减少合法指令位置编码预算。
- Q44：墙钟任务时间与 CPU 占用周期分账，第 15 条 ISR 指令作为设备重启事件点。
- Q45：虚拟页、物理页框、Cache set/tag 三层地址字段不混算。

### OS｜先问谁拥有状态变化

- Q25：死锁最少进程数转成最短 wait-for cycle。
- Q30：先确认 same object，再画 R/W conflict，不把同名变量或 R-R 当互斥。
- Q46：`waitTime` 是 anti-starvation feedback owner，且必须根据“priority 数值越小越优先”决定符号方向。
- Q47：目录只拥有 name→first cluster，FAT 拥有后继链，文件偏移再决定目标数据簇。

### NET｜Scope + State + Timeline

- Q35：前一帧的 MAC learning 会改变确认帧的转发范围。
- Q37：只推进“一次 RIP 更新”的 transient state，不拿最终收敛状态覆盖当前时刻。
- Q39：Same-Subnet Gate 先于 default gateway。
- Q41：`SEQ/ACK`、`rwnd/cwnd`、RTT 三账本分离，并额外用单位守恒抓出 legacy 速率错误。

## 4. Candidate Rule Evidence

以下只登记可迁移动作，不因单年样本自动晋升：

### DS

- **最小资源数题使用“不可突破下界 + 同值构造”闭合最优性**：Q3 很典型。
- **算法设计先从目标函数推出最优结构，再决定需要多少有序信息**：Q43 证明“只需 order-statistic boundary，不需 full sort”。

### CO

- **时间题固定分 `wall-clock critical path` 与 `CPU/resource occupancy`**：Q44 与其他年份的 DMA/流水线/Cache 成本分账同构。
- **跨 TLB/Cache 题先按 Address Owner 分层再切位**：Q45 再次验证。

### OS

- **并发题先做 same-object test，再做 conflict test**：Q30 对 R-R、R-W/W-W 边界非常清楚。
- **动态调度反馈先确定比较键方向，再决定 aging 项符号**：Q46 可迁移到所有数值型优先级题。

### NET

- **协议综合题固定三账本/多账本**：Q41 再次证明序号、窗口、时间不能揉成一个公式。
- **分布式路由必须按 advertisement event 推 transient state**：Q37 与后续年份的 DV/OSPF/BGP 时间轴规则同向。

## 5. Handbook Challenge

本年度没有发现一个“Canonical Handbook 已被 2016 真题独立证明为事实、机制或适用边界错误，却仍需要立即修正文”的硬冲突。

本年发现的主要问题属于：

```text
Legacy routing errors
+ Legacy solution unit error
+ Legacy truncation
+ Complexity-boundary clarification
```

当前 Handbook / Rules 已能够生成修正后的答案，因此不为了制造更新量而重复改写知识 Owner。

若后续更早年份证明某个模型本身有硬错误，则不需要等待“跨年 Rule Promotion”，直接进入 Canonical Model Update。

## 6. 年度学习验收

2016 题解现在支持学生按渐进揭示使用：

```text
独立做题
-> 看 Model Anchor 恢复起手
-> 综合题只看 Representation / Decision 再做
-> 对照 Solution Chain 找 First Divergence
-> 用 Verification 独立查错
-> 用 Compression 在下一题重新调用
```

尤其推荐把 Q3、Q24、Q30、Q41、Q44、Q45、Q47 作为“模型运行”代表题：它们分别训练最优性闭合、资源时间线、冲突 Owner、TCP 多账本、成本分账、地址分层与文件对象链。
