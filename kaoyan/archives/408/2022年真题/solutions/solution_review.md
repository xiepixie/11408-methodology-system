# 2022 408｜题解审阅记录

> 本文件只记录 Derived Solution 审阅中发现的 Source / Legacy Difference 与模型证据；正式题解保持干净。单题技巧不能直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

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

## Source / Legacy Review

### Q11｜学科路由元数据

- Q11 比较直接插入排序与快速排序，按 408 Profile 属于**数据结构**。
- Legacy 文件仍名为 `q11_计算机组成原理.md`，旧年度索引也曾把 Q11 放入计组；本轮年度索引已按 Profile 修正，新题解路由到数据结构 Owner。
- 不改 legacy 文件名本身，避免破坏已有引用；文件名不作为学科真值。

### Q17｜DRAM 地址位与物理引脚不能混写

- `8192×8192` 的行、列各需要 13 bit 地址信息，但 DRAM 通过 RAS/CAS 分时复用同一组地址引脚。
- 因而“逻辑行列地址合计 26 bit”不能推出“芯片有 26 根地址引脚”；错误项为 C。
- 这是 CO 中“逻辑地址字段 ≠ 物理接口资源”的典型 Evidence。

### Q19｜扩展操作码必须逐层扣预算

- 二地址格式 4-bit OP 共 16 个前缀，12 个已占用，剩 4 个扩展到一地址层；
- 一地址层容量 `4×64=256`，使用 254 后剩 2 个前缀；
- 零地址层容量因此为 `2×64=128`。
- 不能把所有“剩余位”一次性当独立操作码空间计算。

### Q21｜中断 I/O 的速率关系

- Legacy 结论 C 正确，但容易被一句“中断适合低速设备”掩盖真正机制。
- 本轮把判断压回 producer/consumer 稳定性：设备产生下一数据的间隔若短于 CPU 完成一次中断处理所需时间，服务速度跟不上到达速度。

### Q30｜缺页事件与缺页处理代价分层

- 页面置换算法、工作集和并发进程数量会改变驻留状态/内存压力，从而影响缺页率。
- 页缓冲队列在本题教材模型中主要降低换出/重新调入的处理代价，不改变“访问时页面是否属于当前驻留集”的事件判定。
- 题解明确把 `fault occurrence` 与 `fault handling cost` 分开。

### Q41｜BST 判定的空结点终止顺序

- Legacy 解法使用中序递增不变量，核心方向正确。
- 但 legacy 代码先递归左右索引，再判断当前数组项是否为 `-1`；本轮改成“索引越界或当前结点不存在立即返回”，使 `-1 = 空子树终止` 成为显式结构不变量。
- 复杂度保持 `O(ElemNum)`，递归空间 `O(h)`。

### Q42｜Top-10 从全排序升级为阈值 Owner

- 任务只要求最小 10 个数，不需要建立全部元素的全序。
- 本轮采用固定 10 元素大根堆：堆顶拥有“当前赢家中的最大值”这一淘汰阈值，每个新元素先做一次阈值比较，只有真正进入 Top-10 时才下滤。
- 平均/最坏渐近时间均为 `O(n)`，固定辅助空间 `O(1)`。
- Legacy 的长度 10 有序数组也能达到线性渐近量级，但 Heap 更直接表达 workload 对 Representation 的要求。

### Q43｜单总线题统一从 State Delta 推控制

- `SF=F15`；加法 OF 为“同号输入、异号输出”，减法 OF 为“异号输入、输出符号偏离 A”。
- Y/Z 的 Owner 不是“提高 ALU 速度”，而是解决单总线下两个输入与结果不能同时占有总线的问题。
- `rd` 是写寄存器编号，应接地址译码器；`rs` 控制读选择。
- 取指路径固定为 `PC -> MAR -> Memory -> MDR -> IR`；题设把从 Read 到数据进入 MDR 的完整过程定义为 5 周期，因此总计最少 7 周期。

### Q44｜Legacy 解析缺失 DMA 小问

- Legacy 文件只保留了 CHS 与平均访问时间，未完整保留第 (3) 问 DMA 解析。
- 本轮独立恢复：512 B / 8 B = **64 次总线请求**；周期挪用方式下 CPU 与 DMA 同时请求主存时，DMA 可优先取得总线，CPU 暂缓一个周期。
- 该题再次验证“机械延迟 / 总线事务 / DMA 完成”必须分层计数。

### Q45｜目录名边与 inode 身份

- `doc` 与 `course1` 的目录项都指向 inode 10，因此是两个名字引用同一文件对象，块号 x 必与 course1 相同，为 30。
- 目录 `course` 已在内存只消除了目录块 I/O；inode 10 未声明缓存，仍需读取 inode-table block，再读数据块，共 2 块。
- 6 MB 文件需要 1536 个数据块，`10 direct + 1024 single < 1536`，因此需要一级和二级间接地址项，不需三级。

### Q46｜同步题先删掉程序顺序已覆盖的边

- 完整偏序为 `A->C, B->C, C->D, C->E, E->F`。
- T1 自带 `A->E->F`，T2 自带 `B->C->D`，真正跨线程且未被程序顺序覆盖的只剩 `A->C` 和 `C->E`。
- 因此两个初值为 0 的事件信号量足够，且不会错误地把 D/E 串行化。

### Q47｜四个 Scope 必须重置模型

- 设备类型：`same broadcast + different collision -> switch`；`same collision -> hub`。
- CSMA/CD：最小帧 64 B 在 100 Mbps 下发送 5.12 μs，往返预算扣除 Hub 双向额外延迟后得到 H2-H3 最远 **210 m**。
- DHCP：首报文为 `DHCPDISCOVER`，二层广播目的 MAC 为 `FF-FF-FF-FF-FF-FF`；E0 在同一广播域上可以收到，但不会因此把二层广播继续路由。
- 802.11 AP 下行：`Addr1=H5(E1), Addr2=AP/BSSID(C1), Addr3=H4(D1)`。

## Candidate Rule Evidence

### DS

- **依赖外层变量的嵌套循环先写求和**，不要按嵌套层数机械相乘。
- **B 树删除候选题用“是否存在合法修复路径”判断**，不要把某一种实现的唯一结果升级为定义。
- **固定 Top-K 先找 threshold owner**：最小 k 个数对应 size-k max heap。

### CO

- **逻辑编码位与物理接口资源分层**：DRAM 行列地址位不等于地址引脚数。
- **扩展操作码按剩余前缀逐层展开**。
- **单总线数据通路固定 `State Delta -> bus owner -> temporary state -> control signals`**。
- **I/O 性能题继续区分 mechanical latency / bus transaction / DMA arbitration**。

### OS

- **调度题固定 `Event -> Candidate -> Decision -> Queue mutation`**，调度次数从决策点计而不是从进程数猜。
- **Page Fault 与 Replacement 分开**：有空闲页框时 fault 不需要 victim。
- **文件题继续使用 `name -> inode -> index path -> block`，硬链接由 inode identity 判定。**
- **同步图先消去线程内 program order 已覆盖的边，再为剩余跨线程边配同步原语。**

### NET

- **先定 Scope** 已跨 2022/2023 重复出现：一跳流控、广播域、冲突域、端到端关闭必须各用自己的 Owner。
- **CSMA/CD 距离题先建立 round-trip timing budget**，设备延迟也进入同一预算。
- **协议字段题先判断方向/状态**：802.11 三地址角色必须由 `ToDS/FromDS` 决定。
- **TCP 时间题继续使用 event timeline**：timeout、FIN/TIME_WAIT、HTTP persistent connection 都不能只背 RTT 数。

以上仍保持 Candidate Evidence；已经开始出现跨 2022～2026 的重复模式，但是否晋升 Rules 应在更早年份继续验证后统一处理。