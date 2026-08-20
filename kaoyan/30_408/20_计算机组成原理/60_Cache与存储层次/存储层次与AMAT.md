# 存储层次与 AMAT：到底在平均什么

> 训练定位：本文件负责把“存储层次、hit/miss、访问时间、miss penalty、AMAT/EAT”这些性能语言定义清楚，并给出跨层组合方法。  
> 模型归属：[CO-06 Cache 与存储层次方法论手册](CO-06_Cache与存储层次_方法论手册.tex)。Cache 的副本机制与 AMAT 由 CO-06 Own；DRAM/介质 latency 与 bandwidth 调用 CO-05；TLB/page walk 调用 CO-07；Page Fault 修复调用 OS-04 / X-B02。

## 一、母问题：一个访存请求到底可能走多远，平均要等多久

> [!question] 根本问题
> CPU 发出一次访存请求后，目标信息可能已经在很近的快速层，也可能必须一路走到更慢的层。怎样用一个统一模型表示“走到哪一层”和“为这条路径付多少时间”？

AMAT 的本质不是某个 Cache 公式，而是**路径成本的期望值**：

$$
\boxed{E[T]=\sum_i P(\text{path}_i)\,T(\text{path}_i)}
$$

最小的两路径图是：

```text
Original memory reference
├─ hit   [probability = HR] → path time = T_hit
└─ miss  [probability = MR] → path time = T_miss,total
```

这里的分支表示**互斥完成路径**，不是说硬件一定按这张图逐级串行执行。真实实现可以并行查 tag/data、并行查 TLB/Cache，或隐藏部分 miss 等待；只要最终路径概率和路径时间定义清楚，期望模型仍成立。

因此，AMAT（Average Memory Access Time，平均存储器访问时间）回答的是：

> **在明确的一组访问请求、层次结构和时间口径下，一次“原始访存请求”从该接口看来平均需要多少时间。**

它是统计期望，不是说每一次访问真的都耗时 AMAT。

## 二、先区分三条容易被画成一条的层次

一次 `load/store` 可能同时涉及地址翻译和数据访问，但它们不是同一个 Cache。

### 1. 地址翻译层次：找“这个 VA 指向谁”

```text
VA
→ TLB
→ Page Table / Page Walk
→ PFN + permission
→ PA
```

- TLB 缓存的是**地址翻译与权限元数据**，不是程序数据；
- TLB hit：所需翻译副本可直接使用；
- TLB miss：需要 page walk，不等于 Page Fault；
- PTE 显示页面不驻留或权限不允许时，才进入 fault 分支。

### 2. 硬件数据层次：找“这个 PA 对应的数据副本在哪里”

典型抽象是：

```text
L1 Cache
→ L2 Cache
→ LLC / L3 Cache
→ DRAM
```

- Cache 保存数据块副本；
- 上层更小、更快，下层更大、更慢；
- Cache miss 才向更低一级请求数据块；
- 多级 Cache 的 AMAT 是这一条链上的条件期望。

### 3. 虚存后备层次：页面不在 RAM 时怎样恢复

```text
Page currently usable / resident?
├─ yes → 正常完成地址翻译并访问数据
└─ no / other fault → Page Fault → OS classify
                         ├─ file / swap backed → I/O → update mapping → retry
                         ├─ demand-zero / COW   → memory repair → update mapping → retry
                         └─ illegal access      → reject / terminate
```

这里的对象是**页、映射与驻留状态**。主存对虚拟内存而言承担“当前驻留工作集”的角色，但 Page Fault 的处理者、传输单位和时间尺度与 CPU Cache miss 完全不同。只有 file/swap-backed 等路径真正需要后备存储 I/O；demand-zero、COW 等 fault 可以在内存中修复。

> [!idea] 不要画成 `TLB → L1 → L2 → DRAM → Disk` 一条无条件流水线
> TLB 属于**翻译路径**；L1/L2/L3 属于**数据副本路径**；Disk/SSD 只在页面不驻留等 OS 慢路径中进入。一次 load 会组合这些机制，但它们的 hit/miss 不是同一种事件。

三条路径的组合关系更接近：

```text
CPU memory reference with VA
│
├─ Translation track: VA → TLB / page walk → permission → PA
│                                  └─ cannot continue → page-fault exception → OS repair/reject → retry or terminate
│
└─ Data track after a legal address is available:
   Cache hierarchy → main memory
```

这张图的箭头表示**语义依赖与控制转移**：不是所有箭头都对应一个固定时钟阶段，也不是每次访问都会走到最右端。

## 三、不同层次到底缓存什么

| 层次 / 机制 | 保存的对象 | 典型管理者 | 传输 / 管理粒度 | “命中”真正表示什么 | miss / failure 后去哪 |
|---|---|---|---|---|---|
| Register | ISA 可见或内部寄存器值 | ISA / CPU / 编译器协同 | register / word | 通常不使用 Cache hit 语义 | 由指令和数据通路决定 |
| L1/L2/L3 Cache | 数据或指令的 block 副本 | hardware | cache line / block | valid + identity 匹配，目标 block 在本层 | 下一 Cache 层或 DRAM |
| TLB | VPN→PFN + permission 等翻译副本 | MMU / hardware | translation entry | 所需地址翻译副本在 TLB | page walk |
| DRAM 主存 | 当前物理内存内容；同时承载 resident pages | memory controller + OS 管理物理页 | burst / cache line 服务；VM 以 page 管理 | 直接 DRAM 访问通常不称“Cache hit”；VM 语境可问 page 是否 resident | Cache refill，或 VM fault 分支 |
| VM backing store | file/swap-backed 页面不驻留时的后备内容 | OS + storage stack | page / storage block | 通常不以 CPU Cache hit 表述 | page-in / I/O / retry |
| OS Page Cache | 文件内容的内存副本 | OS | page / folio 等 OS 对象 | 文件所需内容已在内存缓存 | 文件系统 / 块设备 |

> [!warning] 相同的“cache”一词不代表同一个状态机
> CPU Cache、TLB、OS Page Cache 都利用局部性保存副本，但对象、身份字段、填充/失效事件、管理者和 miss 成本不同。训练时只共享“有限快速副本”的直觉，不共享具体 tag/PTE/文件状态机。

## 四、AMAT 前必须先把时间术语定义清楚

### 1. Latency 与 Access Time：都谈等待，但不要无条件当同义词

**Latency（延迟）**是更一般的“请求到结果可用”的等待时间；**Access Time（访问时间）**通常指某个存储器件或接口完成一次规定访问所需的时间。教材中二者常近似互换，但严谨做题时必须写清起点和终点。

例如：

- Cache hit latency：发起 Cache lookup 到命中数据可供消费者使用；
- DRAM read latency：控制器发出读请求到首个所需数据可用；
- 磁盘 access time：可能把 seek、rotation、controller、transfer 等阶段按题设合并。

因此“主存访问时间 50ns”不能自动解释成“每隔 50ns 才能接收下一请求”，后者属于 cycle / initiation interval 问题。

### 2. Cycle Time：同一资源多久可以接受下一次独立操作

**存储周期（memory cycle time）**强调资源再次可被启动的最小间隔，不等于本次数据第一次变得可用的 latency。

所以：

$$
\boxed{\text{Access Time} \neq \text{Cycle Time}}
$$

多体交叉、流水 DRAM 可以在首个请求尚未完全“消失”前启动别的 Bank，从而提高吞吐，而不必等比例降低一次随机访问的 latency。

### 3. Throughput 与 Bandwidth：一个数请求，一个数数据量

**吞吐量（throughput）**关注单位时间完成多少请求/事务：

$$
Throughput=\frac{\text{completed requests or transactions}}{\text{time}}.
$$

**带宽（bandwidth）**关注单位时间真正传输多少有效数据：

$$
Bandwidth=\frac{\text{effective bytes transferred}}{\text{time}}.
$$

只有当每个事务的有效数据量近似固定、且统计口径一致时，才可写成近似关系：

$$
Bandwidth\approx Throughput\times\text{bytes per completed transaction}.
$$

因此：

$$
\boxed{Latency\neq Throughput\neq Bandwidth}
$$

Burst、bank interleaving 常主要提高可重叠程度、吞吐量和带宽，并不保证首个数据的 latency 同比例下降。

### 4. Hit Time：本层命中时需要付出的时间

$T_{hit}$ 是请求在当前缓存层命中时，从该层接口看到的服务时间。它通常包含完成本层定位、身份检查和取出目标数据所需的时间；具体是否并行读取 tag/data、是否分流水级，服从题设或实现。

### 5. Miss Rate / Hit Rate：是事件比例，不是时间

若当前层收到 $N$ 次访问，其中 $M$ 次 miss：

$$
MR=\frac{M}{N},\qquad HR=1-MR.
$$

必须先说明分母 $N$ 是谁收到的访问。L2 的分母通常不是 CPU 原始 reference 数，而是实际到达 L2 的请求数。

### 6. Miss Penalty：miss 比 hit 多付出的额外代价

本文件采用最清晰的定义：

> [!def] Miss Penalty
> 若一次 miss 的**总路径时间**为 $T_{miss,total}$，当前层 hit time 为 $T_{hit}$，且 miss 一定先支付当前层 lookup，则
> $$
> MP=T_{miss,total}-T_{hit}.
> $$
> 因此 $MP$ 是相对 hit 路径的**额外时间**。

典型 Cache read miss 的额外路径可能包含：victim 选择、dirty write-back、下一级 lookup、主存/总线服务、block refill、状态更新和 retry。哪些部分已经包含在题目给出的“缺失损失”中，必须由题面口径确认。

可把时间关系画成：

```text
hit path : | current-level lookup + hit data delivery |
miss path: | current-level lookup | lower-level service | refill / state update | retry or critical-word return |
            <---------------------- T_miss,total ------------------------------>
            <--- T_hit ---><---------------------- MP ------------------------->
```

这张图只表示**记账边界**，不声称所有阶段都严格串行。若题设允许 write-back、refill、critical-word-first 或其他阶段重叠，要先画真实事件时间线再定价。

### 7. Miss Total Time：一次真正 miss 从头到尾花多久

$$
T_{miss,total}=T_{hit}+MP
$$

只在上面的“MP 是额外成本”定义成立时可这样写。如果题目直接把“200 cycles”定义为 miss path 的完整总时间，就不能再额外加一次 $T_{hit}$。

## 五、单级 AMAT：从条件期望推出，不背两个互相打架的公式

设当前层：

- hit rate 为 $HR$；
- miss rate 为 $MR=1-HR$；
- hit path 总时间为 $T_{hit}$；
- miss path 总时间为 $T_{miss,total}$。

从期望定义直接得到：

$$
AMAT=HR\cdot T_{hit}+MR\cdot T_{miss,total}.
$$

若再定义 miss penalty 为额外成本：

$$
T_{miss,total}=T_{hit}+MP,
$$

则：

$$
\begin{aligned}
AMAT
&=(1-MR)T_{hit}+MR(T_{hit}+MP)\\
&=T_{hit}+MR\cdot MP.
\end{aligned}
$$

所以：

$$
\boxed{AMAT=T_{hit}+MR\cdot MP}
$$

不是另一条独立公式，而是**条件期望公式在“MP=额外成本”定义下的化简**。

> [!idea] AMAT 第一动作
> 永远先问：**题目给我的 miss 时间，是“额外 penalty”还是“miss 总路径时间”？** 先确定定义，再选公式。

### 母例：命中 2 cycles，miss 额外再损失 200 cycles

若 $MR=3\%$，并且题目明确“miss penalty 200 cycles”是额外成本：

$$
AMAT=2+0.03\times200=8\text{ cycles}.
$$

它表示大量访问平均下来，每个原始访问从 Cache 接口看来约花 8 cycles；并不表示每一次访问真的花 8 cycles。

## 六、多级 Cache：下一级 AMAT 会变成上一级 miss path 的一部分

假设：

- L1 hit time 为 $t_1$，local miss rate 为 $m_1$；
- 只有 L1 miss 才访问 L2；
- L2 一旦被访问，hit time 为 $t_2$，local miss rate 为 $m_2$；
- L2 miss 后访问 DRAM，服务时间为 $t_M$；
- 暂不考虑 write-back、refill 额外总线时间和重叠。

则：

$$
AMAT_{L1}
=t_1+m_1\left(t_2+m_2t_M\right).
$$

展开：

$$
AMAT_{L1}=t_1+m_1t_2+m_1m_2t_M.
$$

这说明一层 AMAT 不是“每一级平均时间直接相加”，而是：

> **只有走到某一级，才支付该级的时间。**

### Local Miss Rate 与 Global Miss Rate

L2 的 local miss rate：

$$
m_2=\frac{\text{L2 misses}}{\text{L2 accesses}}.
$$

L2 的 global miss rate：

$$
g_2=\frac{\text{L2 misses}}{\text{CPU original references}}.
$$

在“每个 L1 miss 恰好访问一次 L2、无 bypass/prefetch 等额外请求”的简单串行模型中：

$$
g_2=m_1m_2.
$$

所以多级题必须先确认题目给的是 local 还是 global miss rate。

> [!warning] 真实实现可能有 overlap、prefetch、write buffer、non-blocking Cache
> 一旦题设允许并行或隐藏部分等待，不能机械把所有 latency 相加。先画事件时间线，再决定某些成本是相加、取最大、还是不进入 CPU stall。

## 七、地址翻译的“平均访问时间”不是 Cache AMAT 的同义词

教材常用 **EAT（Effective Access Time，有效访问时间）** 表示 TLB、页表、Page Fault 等路径组合后的有效平均成本。这里“有效”不是另一种数学运算；在这类题里，EAT 仍然是按路径概率得到的期望时间，只是平均的对象通常不是单纯 Cache reference。

例如，忽略 Cache，假设：

- TLB lookup 时间为 $t_T$；
- 一次主存访问为 $t_M$；
- 单级页表；
- TLB hit rate 为 $h$；
- TLB miss 后必须先访问一次主存页表，再访问目标数据；
- 不发生 Page Fault；
- 各步骤串行。

则：

$$
EAT=h(t_T+t_M)+(1-h)(t_T+2t_M).
$$

这算的是**地址翻译 + 数据主存访问**的平均路径，不是 CPU Cache 的 AMAT。

若再存在 Page Fault，最稳妥的写法仍然是：

$$
EAT=(1-p)T_{normal}+pT_{fault,total},
$$

其中 $p$ 是 page-fault probability，$T_{fault,total}$ 必须说明是否包含 trap、OS handler、I/O、页表更新和 retry。若 $P_{fault}$ 被明确定义为相对 normal path 的额外 penalty，则也可写成：

$$
EAT=T_{normal}+pP_{fault}.
$$

Page Fault 的概率往往极小，但一次 fault 的代价可能极大，所以它仍可能显著影响平均值。

## 八、一次 LOAD 到底怎样组合这些层次

从**语义依赖**而非固定时钟顺序观察：

```text
LOAD(virtual address)
→ 得到合法 PA
   ├─ TLB hit → 直接得到翻译
   └─ TLB miss → page walk
        ├─ PTE valid/resident/allowed → refill TLB → 得到 PA
        └─ fault → OS repair / reject → 若可修复则 retry LOAD
→ 用 PA / 合法的 Cache 地址接口访问数据层次
   ├─ L1 hit → 返回数据
   └─ L1 miss → L2 / LLC
        ├─ lower-cache hit → refill upper cache → retry/complete
        └─ lower-cache miss → DRAM → refill → complete
→ 指令获得数据
```

VIPT 等实现可能把某些 TLB/Cache 工作并行化，但**语义上**仍必须先证明合法地址身份，才能把最终 Cache hit 当成有效访问结果。

### 为什么 Page Fault 不应该塞进普通 Cache miss penalty

Cache miss 的下一级通常仍在硬件存储层次内完成；Page Fault 会发生异常控制转移，进入 OS，甚至访问 SSD/HDD，修复映射后重新执行原访问。二者的处理者、状态变化、时间尺度和 retry 边界都不同。

所以只有题目明确要求构造“整个系统从 CPU reference 到最终完成”的全路径平均时间时，才把它们放进同一个总期望模型；即使如此，也应保留路径分层，而不是造一个巨大“miss penalty”。

## 九、为什么不同存储层次采用不同策略

Cache—主存和“需要后备内容的虚存页换入/换出路径”都利用局部性，但代价尺度不同，因此设计选择不同。这里“主存”在 408 常由 DRAM 实现，但不应把 DRAM 这个介质名直接当作层次名；也不能把所有 Page Fault 都描述成主存↔后备存储传输。

| 维度 | CPU Cache ↔ 主存 | Virtual Memory：典型主存 ↔ Backing Store 路径 |
|---|---|---|
| 主要对象 | cache block / line | page |
| 典型管理者 | hardware | hardware detect + OS manage/repair |
| 访问失败名称 | Cache miss | nonresident page 可触发 Page Fault；其他 Page Fault 不一定涉及后备存储 |
| 下一级代价 | 相对较低的 Cache/主存访问与传输成本 | 可能涉及 SSD/HDD I/O，通常远高于主存访问 |
| 映射倾向 | 直接 / 组相联 / 全相联的硬件折中 | page→frame 灵活映射，由页表描述 |
| 替换 | hardware policy | OS / hardware-assisted policy |
| 写回 | write-through 或 write-back 均可能 | 对慢速后备存储通常倾向延迟写回 dirty page |
| 核心性能语言 | hit time、miss rate、miss penalty、AMAT | residency、fault rate、fault service time、EAT |

这张表不是说虚存“就是一个大 Cache”，而是说明两者共享“用较快有限层保存未来可能重用的信息”这一生成性动机；具体状态机仍由各自 Owner 解释。

## 十、四个“平均时间”不能混

| 名称 | 平均的对象 | 典型分母 / 输入 | 常见用途 |
|---|---|---|---|
| Cache AMAT | CPU 发给该 Cache 层次的原始 data/instruction references | hit/miss 路径概率 | 比较 Cache 参数与层次性能 |
| TLB / translation EAT | 需要虚实地址翻译的 references | TLB hit/miss、page-walk 路径 | 分析地址翻译成本 |
| Page-fault EAT | 程序内存 references | normal / fault 路径概率 | 分析虚存慢路径的平均影响 |
| Program CPU time / memory stall | 整个程序或指令流 | reference count、stall overlap、CPI 等 | 最终程序性能 |

因此：

$$
\boxed{AMAT\neq CPU\ Time}
$$

即使 AMAT 已知，也不能在不知道每条指令产生多少访存、哪些等待能重叠、base CPI 是否已含 hit time 的情况下直接得到程序执行时间。

## 十一、概念边界

| 概念边界 | 为什么容易混淆 | 真正判据 | 题目信号 | 混淆后的错误 |
|---|---|---|---|---|
| TLB hit ≠ Cache hit | 都叫高速缓存命中 | 前者命中翻译，后者命中数据块 | VPN/PFN 与 tag/index 同现 | 把 TLB miss 当数据 miss |
| Page resident ≠ TLB hit | TLB 常缓存 resident page 的翻译 | 页在 RAM 不保证翻译副本在 TLB | 页表 present 但 TLB miss | 把 page walk 当缺页 |
| Cache miss ≠ Page Fault | 都会进入慢路径 | 数据块副本缺失 vs 页面无法正常完成翻译/驻留 | Cache / PTE 同现 | 误加磁盘访问 |
| Hit Time ≠ Access Time of lower memory | 都用 ns/cycle | 当前层命中路径 vs 下一级设备 latency | AMAT | 把 DRAM latency 当 Cache hit time |
| Miss Penalty ≠ Miss Total Time | 常都被口语叫“缺失时间” | penalty 是额外成本；total 包含当前层 lookup | “缺失损失 200 cycles” | 多加或少加一次 hit time |
| Local MR ≠ Global MR | 都写 miss rate | 分母是本级 accesses 还是 CPU original refs | 多级 Cache | 多乘或少乘上层 MR |
| Latency ≠ Throughput | 都描述“快慢” | 单请求等待 vs 单位时间完成请求数 | bank/pipeline | 用请求率反推单次延迟 |
| Throughput ≠ Bandwidth | 都描述稳态能力 | 请求/事务数每秒 vs 有效数据量每秒 | burst/总线宽度 | 把 transactions/s 直接当 B/s |
| Latency ≠ Bandwidth | 都描述性能 | 单请求等待 vs 稳态数据率 | burst/interleaving | 用带宽推出随机访问延迟 |
| AMAT ≠ CPU Time | 都用 cycle/ns | 每 reference 的期望 vs 整个程序时间 | CPI / instruction count | 把 AMAT 直接当程序时间 |

## 十二、真题怎样调用这套定义

- **2009 Q21**：先定义 hit rate / miss rate 的分母；
- **2010 Q17**：TLB、Page、Cache 的 hit/miss 是不同事件；
- **2012 Q43**：Cache miss event rate 继续生成 DRAM bandwidth、Page Fault 与 DMA event rate；
- **2013 Q43**：先由 burst + 多体主存算一次 Cache miss 的服务成本，再进入 CPU 总时间；
- **2015 Q16**：write-through 使 Cache hit 写也可能继续产生主存写流量；
- **2016 OS Q45**：Cache miss 与 Page Fault 的成本尺度、写策略不同；
- **2018 Q44**：TLB 命中和 Cache 命中必须分别判断；
- **2024 Q16**：Cache—主存和主存—外存层次的管理者、传输单位、映射/写回不同；
- **2025 Q43**：必须先辨认“缺失损失 200 cycles”究竟是 penalty 还是 miss total time；
- **2026 OS Q29**：TLB、工作集等机制都可能影响平均访存时间，但作用节点不同。

## 十三、做题控制协议

```text
1. 当前平均的“原始请求”是什么？CPU reference、TLB lookup、Cache access，还是 page access？
2. 当前有哪些互斥路径？hit / miss / fault 各自概率是多少？
3. 每条路径从什么时刻开始，到什么时刻结束？
4. hit time、miss penalty、miss total time 分别怎么定义？
5. miss rate 是 local 还是 global？
6. 下一级时间是一个固定 latency，还是另一个 AMAT？
7. write-back、refill、bus、page walk、fault I/O 是否已经包含？
8. 哪些阶段串行相加，哪些允许 overlap？
9. 用 $E[T]=\sum P_iT_i$ 重新构造公式。
10. 最后检查单位、概率和极端情况。
```

### 两个独立检查

- 若 $MR=0$，AMAT 必须退化为 $T_{hit}$；
- 若 $MR=1$，AMAT 必须退化为 $T_{miss,total}$。

多级公式还可以令某一级 $m_i=0$，检查更低层成本是否自动消失。这个极端值检查比重新抄一遍计算更可靠。

## 十四、最短压缩

> [!summary] 一句话
> **AMAT 是“从某个访存接口看，一次原始请求沿不同命中/缺失路径完成所需时间”的期望；先定义路径和时间口径，再算概率，最后才化简成 $T_{hit}+MR\cdot MP$。**

> [!summary] 三条层次
> **翻译层次回答“地址是谁”，Cache 层次回答“数据副本在哪”，虚存后备层次回答“页面不在 RAM 时怎样恢复”。** 三者可以在一次 LOAD 中组合，但不能共享同一个 hit/miss 定义。
