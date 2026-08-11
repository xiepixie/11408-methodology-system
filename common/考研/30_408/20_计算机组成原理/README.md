# 计算机组成原理 Subject Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Subject Atlas，八个 Topic 的Markdown 工作稿仍是 Source，深度正文按册迁入 Canonical LaTeX。

## 学科母问题

计算机组成原理研究：怎样用有限数量、有限速度和有限带宽的硬件，正确而高效地实现 ISA 对软件承诺的程序语义。

$$
\text{ISA Semantic}
\to \text{Data Movement}
\to \text{Hardware Path}
\to \text{Timing}
\to \text{Architectural State Commit}
$$

硬件内部可以重叠、缓存和推测，但对软件可见的程序语义必须保持。

## 旧 Deep Map / Source

[计组学科总图旧稿](00_学科总图/README.md)保留 State、Location、Path、Resource、Timing 与 Commit 的详细展开，可用于 Source Diff；当前唯一 Subject Atlas Owner 是本 README。

## 八个核心 Topic

| Topic | 唯一母问题 | Stop Boundary |
|---|---|---|
| [数据表示与运算](10_数据表示与运算/README.md) | 同一串比特怎样在给定位宽和解释下表示、参与运算？ | 不展开完整 CPU 数据通路 |
| [ISA 与机器级程序](20_ISA与机器级程序/README.md) | 高级语言意图怎样编码成软件可见的机器语义？ | 不展开微架构时序 |
| [CPU 数据通路与控制](30_CPU数据通路与控制/README.md) | 一条指令怎样变成真实数据移动和控制信号？ | 不展开多指令重叠 |
| [流水线与指令级并行](40_流水线与指令级并行/README.md) | 多条指令怎样时间重叠而不破坏语义？ | 不重讲单指令所有微操作 |
| [主存与存储硬件](50_主存与存储硬件/README.md) | 一个地址怎样落到芯片、Bank、Row、Column 和介质？ | 不拥有 Cache 副本协议 |
| [Cache 与存储层次](60_Cache与存储层次/Cache%20与存储层次：怎样维护一个正确的高速副本.md) | 怎样维护一个正确的高速副本？ | 不拥有 OS Page Cache |
| [地址翻译与虚拟存储硬件](70_地址翻译与虚拟存储硬件/README.md) | VA 怎样经 TLB/页表形成 PA 并继续访问 Cache/Memory？ | 不拥有 frame 分配、换页、COW 和 fault policy |
| [总线与 I/O 硬件](80_总线与IO硬件/README.md) | 同步 CPU 怎样通过共享事务与异步设备合作？ | 不拥有 OS block/wakeup 和驱动策略 |

专题正文已按 `10_` 到 `80_` 落地为工作稿，当前状态不代表稳定采用。

## Canonical Ownership

### 数据表示与运算 Owns

位宽、unsigned/signed、定长运算、补码、ALU 标志、移位、乘除基本电路、IEEE 754 与舍入。

### ISA 与机器级程序 Owns

ISA contract、指令格式、寻址、endian/alignment、RISC/CISC trade-off，以及 C 的表达式、数组、控制流和函数调用怎样映射到机器级语义。

### CPU 数据通路与控制 Owns

PC、寄存器堆、ALU、MUX、总线、存储接口、微操作、单/多周期、硬布线与微程序控制；母指令为 ADD、LOAD、STORE、BRANCH。

### 流水线 Owns

stage timing、latency/throughput、structural/data/control hazard、forwarding、stall、flush、CPI，以及 408 范围内的并行性扩展。

### 主存硬件 Owns

SRAM/DRAM/Flash、芯片扩展、地址线、交叉编址、多模块存储和设备介质的硬件组织与访问成本。

### Cache Owns

locality、line、mapping、tag/index/offset、replacement、write policy、hit/miss 和 AMAT。

### 地址翻译硬件 Owns

VPN/offset、PTE 硬件可见格式、TLB、page walk、VA/PA 位划分以及 TLB 与 Cache 的组合路径。

### 总线与 I/O 硬件 Owns

bus transaction、arbitration、timing、controller registers、port addressing、polling、中断硬件路径和 DMA controller/transfer。

## Internal Bridge 与 Integration

新的 Canonical 入口：

- [CO-B01｜ISA Semantic × Datapath](85_科内桥梁/CO-B01_ISA语义与数据通路/README.md)：指令承诺的状态变化怎样翻译成微操作、通路与控制；
- [CO-B02｜Address Translation × Cache Access](85_科内桥梁/CO-B02_地址翻译与Cache访问/README.md)：VA/PA 位怎样进入 TLB/Page Table 与 Cache 的组合访问路径；
- [CO-I01｜一条指令的一生](86_综合专题/CO-I01_一条指令的一生/README.md)：优先以 LOAD 追踪 ISA -> CPU -> Pipeline -> Translation -> Cache/Memory -> Commit。

`C -> ISA` 的机器级映射仍由 ISA Topic Own，不再把 `C × ISA × CPU` 建成跨科 Bridge。原 `85_科内桥梁与综合/` 旧稿保留为 Source/legacy work draft，不再拥有新的 Bridge/Integration 定义。

Cross-Subject Bridge 统一上移到 [408 Cross-Subject Bridge Atlas](../50_桥梁专题/README.md)：Privilege/Exception × OS、Hardware Address Translation × OS VM、Interrupt/DMA × OS I/O。

## 性能的归属

性能不是第九个硬件子系统。IC、CPI、IPC、clock、critical path、latency、throughput、bandwidth、AMAT 与 speedup 进入[计组做题规则](90_做题规则/README.md)中的性能工具箱，各 Topic 只使用与自身机制直接相关的指标。

## Question Control Adapter

$$
\text{State}
\to \text{Location}
\to \text{Path}
\to \text{Resource}
\to \text{Timing}
\to \text{Commit}
$$

1. 当前软件可见状态是什么？
2. 数据现在在哪里？
3. 它将经过哪条硬件路径？
4. 需要哪些共享资源，是否冲突？
5. 数据何时可用，在哪个周期边界锁存？
6. 最终何时改变体系结构状态？

## 建议审查顺序

```text
Atlas
-> CPU 数据通路与控制
-> ISA 与机器级程序
-> 流水线
-> Cache / 地址翻译
-> 数据表示 / 主存 / I/O
-> 一条指令的一生
```

审查时优先攻击《CPU 数据通路与控制》的“状态差 -> 路径 -> 微操作”以及《一条指令的一生》的跨层慢路径；它们决定其余 Topic 是否能被统一调用。
