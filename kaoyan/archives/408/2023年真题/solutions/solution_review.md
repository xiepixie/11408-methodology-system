# 2023 408｜题解审阅记录

> 本文件只记录 Derived Solution 审阅中发现的 Source Correction、Legacy Difference 与模型证据；正式题解保持干净。单题技巧不能直接晋升 Rules；若独立确认 Canonical Handbook 存在事实、机制或边界硬错误，则按 Stable Write 修正唯一 Owner，并回归受影响题解。

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

- Q11 是快速排序划分，按 408 Profile 属于**数据结构**。
- Legacy 文件仍名为 `q11_计算机组成原理.md`，旧索引也曾把它列入计组；本轮已修正年度索引，并在新题解按数据结构 Owner 路由。
- Raw/legacy 文件名不作为学科真值，权威路由仍为 Exam Profile。

### Q21｜Canonical 题面发生语义级错误

- 本轮发现 Canonical Q21 的 D 项曾写成“外部设备通过中断控制器向 CPU 发**中断请求信号**”。
- 若保持这句话，D 本身是正确命题，与本题“错误的是”及唯一答案 D 发生硬冲突。
- Legacy 原题保存的是“发**中断结束信号**”，这一表述才构成错误项：设备通过中断控制器向 CPU 提交的是中断请求，而不是所谓中断结束信号。
- 已在 Canonical Source 中恢复为“中断结束信号”，再生成 Q21 题解。此项说明题解阶段仍必须做 Question-Logic Review，不能假定 Source Freeze 后绝无字符级语义错误。

### Q42｜置换—选择 run 边界恢复

- Legacy 解析把三个初始归并段粘连为一串文本，肉眼难以判断 run 边界。
- 本轮按 Replacement Selection 状态机独立模拟，得到：

```text
Run1: 37, 51, 63, 92, 94, 99
Run2: 14, 15, 23, 31, 48, 56, 60, 90, 166
Run3: 8, 17, 43, 100
```

- 三段长度 6+9+4=19，与输入记录总数守恒。

### Q43｜列优先访问并不降低本题 Cache 命中率

- 不能只凭“调换循环后空间局部性变差”直接判断命中率下降。
- 固定 j 时行间 stride=256 B=8 blocks；64 组 Cache 中每 8 个 set 循环一次，24 行只让每个相关 set 同时容纳 3 个数组 cache line。
- Cache 为 4-way，因此数组自身不会产生冲突替换；每个 32 B block 仍是 1 miss + 7 hit，两个循环次序的命中率都为 87.5%。
- 这是对“趋势口诀必须回到实际 associativity/capacity”规则的强证据。

### Q44｜三层语义不能混算

- `jmp/jge` 的 relative displacement 以 **Next PC** 为基准；
- 第 19 条 `mov [EA],0Ah` 的源操作数是立即数，复合表达式属于目的地址；
- `00 20 42 00` / `0A 00 00 00` 的低有效字节先出现，锁定 little-endian；
- 数组页第一次访问会缺页，不代表已经执行过多条指令的代码页在第 19 条取指时仍缺页。

### Q45｜普通函数交换不能替代原子 swap

- Legacy 结论正确，但本轮把安全性原因压回不变量：只有原子 `FALSE -> TRUE` ownership transfer 才能允许线程进入临界区。
- `newSwap()` 的三条普通读写可被另一线程插入；函数封装不产生原子性。
- 正确修复为 `if -> while`、退出 `lock=TRUE -> lock=FALSE`。

### Q46｜Wakeup 不等于 Running

- 正确事件链：`② Block -> ⑥ input -> ④ interrupt -> ③ driver data move -> ① Ready -> scheduler -> ⑤ syscall return`。
- ① 只恢复 P 的调度资格，不能把“插入就绪队列”写成“P 立即执行”。
- 这与 OS-B01 的 Wait/Block/Wakeup 边界高度一致。

### Q47｜TCP 三账本闭合

- FTP 控制连接持久、数据连接按传输建立/关闭。
- SYN 占 1 个序号，所以首数据字节为 101；18000 B 数据占 101～18100，FIN=18101，第二次挥手 ACK=18102。
- `cwnd`: 1→2→4(ssthresh) 后进入拥塞避免；ACK=2101 时为 3 MSS，ACK=7101 时为 5 MSS。
- 从请求建数据连接到文件全部确认：1 RTT 建连 + 5 RTT 数据批次 = 6 RTT=60 ms；应用层平均速率 2.4 Mb/s。

## Candidate Rule Evidence

### DS

- **矩阵题先锁行/列语义**：有向邻接矩阵中“行=出、列=入”应作为第一动作，随后再写算法。
- **开放定址删除必须区分 EMPTY / DELETED**：失败查找停止条件是首个真正 EMPTY，而不是删除标记。
- **Replacement Selection 用 active/frozen 状态机**：run 边界由 active 集合清空触发，不由固定 m 条记录触发。

### CO

- **绝对先分层再算地址**：Page / Block / Set 是三个不同投影；综合题应先写统一 VA 生成式再分别取字段。
- **局部性趋势必须经过实际 Cache Geometry Gate**：stride 大不自动推出冲突；必须计算 set occupancy 与 associativity。
- **机器码题固定 `Instruction Boundary -> Next PC -> Operand Role -> Endian -> Residency`**。

### OS

- **状态迁移题优先问等待条件是否仍成立**：`Blocked -> Ready` 是解除等待；只有 dispatch 才进入 Running。
- **原子互斥先写 owner invariant**：不能用“代码看起来交换了变量”代替 atomicity 证明。

### NET

- **多跳等速传输用“首包 + 流水间隔”**，不要把每个包的所有 hop 时延串行相加。
- **窗口协议先从序号空间推合法窗口上界**，再比较吞吐/利用率。
- **TCP 综合题继续验证三账本**：`SEQ/ACK`、`cwnd/phase`、`RTT timeline`。

以上均保持 Candidate Evidence；等 2022 及更早年份出现独立重复样本后，再考虑更新 Subject Rules。
