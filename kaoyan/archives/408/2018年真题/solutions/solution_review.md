# 2018 408｜题解审阅记录

> 本文件记录 Derived Solution 阶段发现的 Source/Legacy 差异、模型澄清和 Candidate Rules Evidence。正式题解保持干净；单题技巧不直接晋升 Rules。若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

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

### Q11｜学科路由仍受 legacy 文件名污染

- Q11 是“自底向上建大根堆”，按 408 Profile 属于**数据结构**。
- Legacy 文件仍名为 `q11_计算机组成原理.md`，旧年度索引也把它放在计组区；本轮已把年度索引恢复为 Q1～Q11 数据结构、Q12～Q22 计组。
- 新题解 frontmatter 的 `subject` 以 Profile 为准，legacy 文件名只保留链接兼容。

### Q41｜Legacy 代码存在数组越界

- Legacy prose 已正确指出只应记录 `1..n`，但代码却只判断 `num > 0` 后执行 `vis[num-1]=1`。
- 当输入中存在 `num>n` 时会越界，和其文字推理自身冲突。
- 新题解把候选域证明放在第一步，并明确使用 `1 <= A[i] <= n`。
- 这是“先锁 Representation/State Domain，再写数组索引”的典型证据。

### Q42｜MST 不唯一 + TTL 必须跨模型重置 Cost Owner

- 题图的两个最经济方案均为 7 条边、总费用 16。
- 两棵 MST 的差别来自权值同为 3 的连接边：方案 1 采用 `WH-QD`，方案 2 采用 `BJ-TL`。
- 第 (3) 问不能继续把边权当作“距离”；TTL 的 Owner 是路由器转发次数。
- 因此方案 1 的 `TL->JN->QD->WH->XA->BJ` 在 TTL=5 时会在 XA 转发处归零，H2 不能收到；方案 2 中 TL 与 BJ 直接相连，H2 可以收到。
- Legacy 正文在答案段落处被截断，本轮依据 Canonical 图与 `q42_fig2.svg` 的两棵方案独立恢复。

### Q43｜三种 I/O 方式必须统一到 arrival/service rate

- 查询 I/O、中断 I/O、DMA 的表面公式不同，但真正统一模型是：设备数据到达速率 vs CPU/控制器服务速率。
- A：4 B / 2 MBps = 2 μs 一份数据；每次查询至少 80 ns，因此最低 CPU 占用 4%。
- B：4 B / 40 MBps = 0.1 μs，而一次中断至少 0.8 μs；单缓冲模型下中断服务跟不上数据到达。
- DMA：CPU 成本从“每 4 B”变成“每 1000 B 块”，最终 CPU 占用仍为 4%，但机制已完全不同。

### Q44｜`VA -> PA -> Cache` 层次得到再次验证

- 本题同时出现 TLB、页表、物理页号与 Cache，最危险错误是直接拿 VA 高位去解释 Cache Tag。
- 正确链为：`VA -> VPN/offset -> TLB/PageTable -> PPN -> PA -> Cache Tag/set/offset`。
- 第二个地址只问 set，而 `set+block offset=8 bit < page offset=12 bit`，因此可利用“页内偏移翻译前后不变”直接从 VA 低位得到组号 3。
- 这与 2020/2023 等年份出现的 Page/Block/Set 分层证据形成跨年重复。

### Q45｜PDBR 的变化由 Address-Space Owner 决定

- “发生上下文切换”并不是判断 PDBR 是否变化的充分条件。
- 进程切换通常改变地址空间 Owner，所以需装载新页目录物理基址；同一进程线程切换共享同一地址空间，因此 PDBR 不变。
- 这比死记“进程切换变、线程切换不变”更具迁移性：真正的问题是 translation root 的 Owner 是否改变。

### Q46｜文件系统容量题是多资源瓶颈问题

- 最大文件长度由 inode 索引 fan-out 决定：`8 + 1024 + 1024^2 + 1024^3` 个数据簇。
- 5600 B 小文件本身只需 2 个 direct 数据簇，不消耗间接索引块；数据区可支持 256M 个，但 inode 只有 64M 个，所以 inode 是瓶颈。
- F1/F2 最后一簇号定位时间不同，原因不是“文件越大越慢”这一模糊趋势，而是跨过了 `8 direct blocks = 32 KB` 的索引层级边界。

### Q47｜Legacy 题面文字错误，但 Canonical 已正确

- Legacy 旧题解中曾出现“路由器通过 F1 转发时进行了**分配**”；Canonical Source 当前已经是正确的“进行了**分片**”。
- 本轮不对 Canonical 做无意义修正，只在 Derived Review 记录 legacy 差异。
- 分片计算严格按 `payload -> MTU-header -> 8B alignment -> offset`：最大数据 776 B，2 片，offset 为 0、97。

## Candidate Rule Evidence

### DS

- **数组索引前先压缩候选域**：若问题只关心有限值域，先证明 State Domain，再把值映射为直接寻址标记；这能同时解释正确性与越界边界。
- **图综合题每次换问法要重置 Cost Owner**：MST 阶段 cost=边权；TTL 阶段 cost=路由器转发次数。共享一张图不代表共享同一个度量。
- **构造型堆题先分清 build-heap 与 repeated insert**：两者状态演化不同，不能只看最终堆。

### CO

- **I/O 方式统一成 Arrival Rate vs Service Rate**：查询、中断、DMA 的机制差异可以通过“CPU 每处理单位数据需要介入几次”生成，而不是背三套孤立百分比公式。
- **TLB/Page Table 与 Cache 分层**：先完成 translation，再做 cache projection；若 cache index 完全位于 page offset 内，才允许用 VA 低位直接求 set。
- **标志位先定数值语义**：CF 看无符号借位/进位，OF 看有符号可表示性，不能共用一个直觉。

### OS

- **状态迁移先问缺什么条件**：只缺 CPU 是 Ready；缺资源/I/O 条件是 Blocked。
- **地址空间寄存器的更新由 Owner 变化触发**：PDBR/translation-root 属于进程地址空间，不属于线程私有执行流。
- **文件系统综合题要同时找 metadata capacity 与 data capacity**：最大文件数由资源瓶颈 `min(...)` 决定；访问时间则由索引路径层数决定。

### NET

- **跨路由器题固定重画当前链路 Scope**：IP endpoint 与 MAC next-hop 分属不同生命周期，路由器处必须重新封装二层头。
- **CIDR 聚合先验证边界对齐**：公共前缀不仅决定长度，还必须确认候选网络连续且以聚合块边界起始。
- **IPv4 分片固定链**：`original payload -> max aligned payload -> number of fragments -> offset/8 -> payload conservation`。

以上仍保持 Candidate Evidence；后续继续用 2017 及更早年份检查其跨题稳定性，再决定是否通过 Evidence Promotion 更新 Subject Rules。