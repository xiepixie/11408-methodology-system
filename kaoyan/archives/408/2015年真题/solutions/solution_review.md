# 2015 年 408｜题解与模型审阅记录

> 本文件记录 Derived Solution 阶段发现的 Legacy Difference、模型澄清与 Candidate Rules Evidence。正式题解保持干净；Canonical Source、Handbook 和 Rules 仍由各自唯一 Owner 维护。

## 1. 年度结论

- Q1～Q47 已建立 `model-grounded-v1`。
- Q1～Q40 均符合固定选择题结构；Q41～Q47 均符合综合题深度 Gate。
- 选择题 `answer` 与年度索引/legacy answer 一致。
- 2015 使用共享 408 默认综合题路由，无年度 override。
- Canonical Source 本轮未发现需要改写题意的明确硬冲突；主要问题集中在 legacy 学科标注、解析精度和综合题实现质量。

## 2. Routing / Asset Corrections

### Q11｜Legacy 学科文件名错误

Q11 是希尔排序，按 Exam Profile 属于数据结构 Q1～Q11。

旧文件名仍是：

```text
q11_计算机组成原理.md
```

只作为历史兼容引用保留。新题解 `subject`、年度导航与后续统计均按**数据结构**处理。

### 年度索引

年度快速答案保持不变；Derived Solution 导航应指向 `solutions/qNN.md`，旧 `qNN_*.md` 只作为 Legacy Reference。

## 3. Legacy Solution Corrections / Clarifications

### Q18｜同一 bank 不足以推出冲突

Legacy 只强调多体交叉映射，容易形成：

```text
same bank -> conflict
```

的过强规则。

正式题解补足时间维度：

```text
bank = address mod 4
+ request spacing / bank busy state
-> conflict or no conflict
```

`8008` 与 `8004` 虽同 bank0，但相隔完整轮转；真正危险的是尾部连续 `8004 -> 8000`。

### Q22｜异常返回语义不能一概而论

Legacy 使用“内中断不能被屏蔽，一旦出现应立即处理”一类宽泛表述，并用个别例子解释 D。

正式题解改为更稳定的：

```text
fault / trap / abort
-> different restart contract
```

因此 D 的问题是把所有内部异常都绝对化成“处理后回到原指令”。

### Q23｜Hardware Entry 与 Software Context Save 分层

正式题解明确：

```text
hardware -> minimum return state (PC/PSW...)
OS/ISR   -> GPR context as needed
```

避免“所有现场都由 OS 保存”或“所有现场都由硬件保存”的两种过度简化。

### Q31｜位图题必须分 `bit index -> bitmap block -> byte`

Legacy 结论正确，但公式表述有压平风险。

正式题解固定两级投影：

```text
409612
-> bitmap bit index
-> bitmap block offset = 50
-> actual block = 32 + 50 = 82
-> bit offset = 12
-> byte offset = 1
```

### Q41｜Legacy 代码存在字段与索引不一致

Legacy 题解中：

- 文字一度出现按 `q[data]` 记录；
- 代码使用 `abs(data)`；
- 结点字段在 `link / next` 之间混用；
- 未完整给出结点定义与复杂度闭环。

正式题解统一成：

```text
key = abs(data) ∈ [0,n]
seen[key]
pre / p linked-list invariant
```

并给出可运行的 $O(m)$ / $O(n)$ 实现。

### Q42｜Legacy Derived 内容不完整

Legacy 文件中的矩阵正文发生明显扁平/截断，难以直接学习。

本轮从 Canonical 图恢复邻接矩阵，并独立计算：

$$
A^2=
\begin{bmatrix}
3&1&0&3&1\\
1&3&2&1&2\\
0&2&2&0&2\\
3&1&0&3&1\\
1&2&2&1&3
\end{bmatrix}.
$$

同时把核心机制恢复为：

```text
(A^m)ij = number of length-m walks from i to j
```

而不是只保留矩阵结果。

### Q45｜Legacy 同步方案存在过度同步

Legacy 使用：

```text
A_full / A_empty / A_mutex
B_full / B_empty / B_mutex
```

六个信号量。

在题面把“取一个邮件/放一个邮件”视为原子抽象操作、且每个信箱只有一个 producer 与一个 consumer 的语义层，本题真正的同步条件只有容量 permit：

```text
A_full=x
A_empty=M-x
B_full=y
B_empty=N-y
```

四个计数信号量即可表达 `nonempty / nonfull`。

若具体 mailbox 底层实现有多个共享指针/索引需要原子更新，mutex 可以作为更低实现层补充；但不应把实现锁无条件提升为题目机制本体。

### Q47｜Legacy MAC 文本有明显拼写污染

Legacy 出现：

```text
ff-ff-ff-f-ff-ff
```

正式题解恢复为标准广播 MAC：

```text
FF-FF-FF-FF-FF-FF
```

并明确两层地址生命周期：

```text
IP destination = end-to-end endpoint
Ethernet destination = current-hop next hop
```

## 4. Candidate Rules Evidence

### 数据结构

- **有限值域是 Representation Signal**：一旦给出 `key ∈ [0,n]`，先检查 direct addressing / bitmap 是否能把重复查询从扫描降成 $O(1)$。
- **矩阵幂题先恢复关系语义**：`Aij` 是一步关系，矩阵乘法是在枚举中间状态；由此自然生成 walk-count 解释。
- **排序题先命名 Cost Owner**：比较次数、移动次数、稳定性、总时间不是同一成本坐标。

### 计算机组成原理

- **同一硬件资源是否冲突 = identity + timing**：Q18 再次证明只看 bank/set/port 身份不够，还要看占用生命周期是否重叠。
- **异常题固定分 `Detection -> Hardware Response -> Software Handler -> Return Contract`**：Q22/Q23 连续提供证据。
- **多层存储题先做 Geometry/Owner 预算**：Q15/Q16 分别验证 metadata capacity 与 TLB/Cache/write-policy 分层。

### 操作系统

- **Running -> ? 先问还缺不缺 CPU 以外条件**：Q25 与后续多年 `Blocked -> Ready != Running` 模型一致。
- **同步原语数量由真实等待条件/冲突边决定**：Q45 支持“先画 permit/conflict graph，再决定 semaphore/mutex”，而不是每个共享名词都配一把锁。
- **文件/位图题优先做对象投影**：file offset -> index level；disk block -> bitmap bit -> bitmap storage location。

### 计算机网络

- **窗口题先做 in-flight budget，再做 sequence-space safety**：Q35 与 2016/2017/后续 GBN 证据一致。
- **Layer Scope 决定地址 Owner**：Q37/Q38/Q47 重复出现 collision/broadcast/prefix/next-hop 边界。
- **TCP 同时维护 congestion 与 receiver capacity**：Q39 再次证明 `send window = min(cwnd,rwnd)`，不能只追一条窗口曲线。

以上先作为跨年 Evidence。已有同义稳定 Rules 的不重复造新规则；真正新增动作必须继续通过 Evidence Promotion。

## 5. Handbook Challenge

本年度未发现一个已被独立真题事实证明为 Canonical Handbook **硬错误**的条目。

本轮更接近“表达/边界增强”的项目有：

1. CO：存储体/Cache 等资源冲突是否都应统一显式写成 `Identity + Occupancy Interval`；
2. OS：同步题是否应在 Rules 中进一步强化“semantic permit vs implementation mutex”；
3. DS：邻接矩阵幂的 walk-count Bridge 是否已经足够显式；
4. NET：窗口题的 `in-flight budget -> sequence-space invariant` 是否已跨年稳定到可升级为统一 Rule。

这些先进入跨年 Promotion 审阅，不因 2015 单年再次出现就机械重复写 Handbook。

## 6. 学习质量观察

2015 的题型很好地说明为什么题解不能只是“正确答案 + 知识点”：

- Q18 若只记答案 D，会学成错误规则“同 bank 就冲突”；
- Q22/Q23 若只背术语，会把 fault/trap 和硬件/软件保存混在一起；
- Q41/Q42 的真正价值是把题面压缩成可迁移 Representation；
- Q45 的价值在于学会**最小同步状态**，而不是复制一份能运行但过度加锁的代码；
- Q47 要能从 Scope 重新生成 DHCP/ARP/网关行为，而不是背几个地址。

因此本年度继续符合 QA Owner 的目标：题解应让学生能定位自己的 First Divergence，并在下一道陌生题上重新生成第一动作。