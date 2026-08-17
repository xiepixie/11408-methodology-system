# 2021 408｜题解审阅记录

> 本文件记录 Derived Solution 审阅中发现的 Source / Legacy Difference 与模型证据；正式题解保持干净。单题技巧不能直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

## 本轮格式 Gate

Q1～Q40：

```text
Model Anchor
-> 解题链
-> 选项判断
-> Verification
-> Compression
-> 易错边界
```

Q41～Q47：

```text
Model Anchor
-> Problem Representation
-> Decision Points
-> Solution Chain
-> Verification
-> Compression
-> 易错边界
```

## Progress Review

本轮中途复查确认：题解推进方式符合预期，没有退化为 legacy 解析改写。Q1～Q47 均从 Canonical Source 独立推理，并执行 Answer Consistency、Heading Order、Model Anchor 三要素、Source/Legacy Link、SVG Reference 与综合题分值检查。

同时修正了本轮自身一个术语问题：Q02 的结构是“一端只能入、另一端可入可出”，即**输出受限双端队列**（两端可入、仅一端可出），不是输入受限双端队列。术语已在正式题解中更正。

## Source / Legacy Review

### Q11｜学科路由仍以 408 Profile 为准

- Q11 是大根堆插入，属于数据结构。
- Legacy 文件名仍为 `q11_计算机组成原理.md`，旧年度索引也曾把 Q11 放入计组。
- 本轮 Derived Solution 路由为数据结构，并修正年度索引的科目计数；不把 legacy 文件名当成学科真值。

### Q30｜“删除文件”与链接生命周期

- Legacy 把释放 inode / 数据块写成无条件动作，语义略宽。
- 更严谨的模型是：删除 pathname 首先删除目录项并减少链接引用；只有最后一个硬链接且不存在延迟释放条件时，才释放文件对象和数据块。
- 本题选项仍然明确指向 A，因为删除原文件不要求遍历并删除独立的符号链接/快捷方式。

### Q34｜差分曼彻斯特首位边界

- 图中第一码元缺少前一码元末电平参照，因此单靠局部波形无法独立判断首位。
- 第 2～8 位可由“码元起始是否跳变”确定为 `0111001`，结合选项唯一得到 A=`10111001`。
- 题解明确保留这一边界，不伪造第一位的独立推导。

### Q41｜Legacy 算法存在矩阵维度错误

- Legacy 示例代码内层循环写成 `e < numEdges`，这不是邻接矩阵的合法列边界。
- 邻接矩阵维度是 `numVertices × numVertices`，正确算法必须扫描 `j < G.numVertices`。
- 题干已经保证图连通，所以不需要额外 DFS/BFS；只需统计奇度顶点是否为 0 或 2。

### Q42｜稳定性必须给重复元素加身份

- 输出值 `{-10,10,11,19,25,25}` 本身无法说明稳定性，因为两个 25 数值相同。
- 用 `25a,25b` 标记原顺序后可见：原代码在相等时增加前一个元素的排名，使 `25a` 排到 `25b` 后面，因此不稳定。
- 把 `<` 改成 `<=` 后，相等时增加后一个元素的排名，恢复稳定性。

### Q43｜宽度 Owner 与 Legacy 理由修正

- `word size=16`、`address bus=20`、`data bus=8` 分别约束 ALU/一般运算宽度、MAR 与 MDR，不应机械等同。
- `01B3H` 的低 16 位结果 `8290H` 是截断机器数；溢出判断必须检查真实带符号乘积是否超出 16 位补码范围。
- Legacy 对符号扩展的解释引用“跳转可能向前/向后”，但第 (4) 问明确说的是 I 型访存偏移量；正确理由是 `imm` 被定义为带符号地址偏移，必须符号扩展以保持数值。

### Q44｜TLB 的 LRU 是组内状态

- VPN 访问序列映射到 set 4 的局部序列为 `12 -> 4 -> 12 -> 20`。
- 第二次访问 12 是命中，并刷新最近使用状态，所以 20 到来时淘汰的是 4，而不是 12。
- 这是“Cache/TLB 组相联题先切 set，再维护局部 replacement state”的强证据。

### Q45｜Safety 与 Progress 必须同时验证

- 方法 1 虽然把 `check/update` 包在关中断区中，却在 `S<=0` 时持续关中断忙等，阻断让 `signal()` 推进的路径，因此 liveness 失败。
- 方法 2 在等待时暂时开中断、重新检查前再关中断，在题设单处理机模型下同时满足 atomicity 与 progress。
- 该结论不能无条件推广到多处理器；关本 CPU 中断不等于跨核互斥。

### Q47｜Legacy 的“CSMA/CD 帧”术语不准确

- DNS 报文的封装应写作 `DNS -> UDP -> IP -> Ethernet frame`。
- CSMA/CD 是经典共享以太网的介质访问控制机制，不是一个独立的“帧封装格式”。
- 本题事件链恢复为：ARP DNS -> DNS -> ARP gateway -> TCP handshake -> HTTP；交换机在 t1 前学习 `cc@4, bb@1, aa@2`，H2 至少只收到两次 ARP 广播。

## Candidate Rule Evidence

### DS

- **表示参数先恢复，再做地址/结构计算**：Q03 先恢复列数；Q09 先把关键字数转成孩子数。
- **图算法问中间状态时维护算法自己的 frontier/state**：Q07 看 zero-indegree frontier，Q08 看 settled/unsettled 与 dist。
- **算法稳定性必须使用带身份的重复元素验证**：只看最终数值序列不够。

### CO

- **同一题出现多个“位宽”时先找 Owner**：word/address/data/instruction/register fields 各自受不同契约约束。
- **机器码先切字段，再解释语义；溢出看数学真值，不看截断位模式是否“合法”**。
- **组相联翻译缓存先 `VPN -> set`，replacement state 只在组内更新**。

### OS

- **事件、对象生命周期、策略分层**：创建进程不等于立即 Running；unlink pathname 不等于无条件立即释放全部文件资源。
- **同步正确性至少同时检查 Safety + Progress**，不能只证明互斥。
- **特权级与中断允许状态是两个独立维度**，不能把 kernel mode 等价为 interrupts disabled。

### NET

- **先定 PDU / Layer Scope 再算开销或功能 Owner**。
- **交换机题按每个帧事件维护 `source MAC -> ingress port` 状态**，并区分 broadcast flood 与 known unicast。
- **远端 IP 通信的 ARP Owner 是下一跳网关，不是远端终点**。

以上均保持 Candidate Evidence；继续用 2020 及更早年份验证跨题迁移后，再考虑 Evidence Promotion。