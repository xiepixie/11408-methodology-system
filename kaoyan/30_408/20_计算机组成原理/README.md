# 计算机组成原理 Subject Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Subject Atlas。52 份个人旧笔记已完成全科 Source Routing；CO-01 至 CO-08 均已建立并发布 Canonical LaTeX 候选正文，待统一真题攻击与人工确认。

## 学科母问题

计算机组成原理研究：怎样用有限数量、有限速度和有限带宽的硬件，正确而高效地实现 ISA 对软件承诺的程序语义。

把软件可见的体系结构状态记为 $S_{\mathrm{arch}}$。对一条已定义语义的指令 $I$，ISA 规定它在合法前提下应产生怎样的下一架构状态，可抽象为

$$
S'_{\mathrm{arch}}=\operatorname{Spec}_I(S_{\mathrm{arch}}).
$$

一个具体硬件实现可以在内部采用不同的数据通路、缓存、流水或其他微架构机制。记正常完成一次执行后得到的软件可见状态为

$$
S_{\mathrm{visible}}
:=
\operatorname{VisibleState}\!\left(\operatorname{Execute}_{\mathrm{impl}}(I,S_{\mathrm{arch}})\right).
$$

实现正确性要求

$$
S_{\mathrm{visible}}
=
\operatorname{Spec}_I(S_{\mathrm{arch}}).
$$

若发生异常，则下一可见状态必须服从 ISA 对异常入口与可见状态的规定，而不是任意留下部分更新。因此“有限硬件怎样实现既定程序语义”才是后续通路、时序、存储层次与 I/O 机制的共同约束。

\textbf{考纲总览入口：}传统的存储程序思想把指令和数据都放入可寻址存储器，由 PC 驱动“取指—解释—执行—更新状态”的循环；高级语言程序则经编译、汇编、链接和装入，才成为这条循环可以消费的机器级映像。这个历史模型只规定可观察的程序存储与执行入口，不规定某一台机器必须采用单一总线或固定节拍。

性能题也先统一对象再换算单位：响应时间是一次任务完成所需的时间，吞吐率是单位时间完成的任务量；CPU 执行时间由 $IC\times CPI\times T_{clk}$ 生成，MIPS/MFLOPS/ZFLOPS 只是以不同“每秒完成多少条指令/浮点操作”的速率表示，不能跨指令集、程序或精度口径直接比较。任何指标都必须回到同一程序、同一结果正确性和完整成本路径。

## 计组统一六格坐标

本 Atlas 用六个坐标观察同一次硬件执行：

$$
\mathcal M_{\mathrm{CO}}
:=
(\text{ISA State},\text{Data Location},\text{Datapath/Control},\text{Timing},\text{Architectural Visibility},\text{Cost}).
$$

它们是同时约束一次实现的观察维度，不是六个依次发生的物理阶段。这里的 `Architectural Visibility` 沿用项目中的 `Commit` 简称，指结果何时成为软件可见的架构状态；它不假设所有处理器都存在某个名为 commit 的独立流水级。

| 坐标 | 首要问题 | 当前 Owner |
|---|---|---|
| `ISA State` | 指令前后哪些状态对软件可见？同一串 bit 按什么语义解释？ | CO-01、CO-02 |
| `Data Location` | 指令和操作数现在在寄存器、Cache、主存、设备还是翻译结构中？ | CO-05、CO-06、CO-07、CO-08 |
| `Datapath / Control` | 值经过哪些 ALU、MUX、寄存器、总线和控制信号？ | CO-03、CO-B01 |
| `Timing` | 值何时产生、何时 ready、何时被 consumer need，哪里需要重叠或等待？ | CO-04 |
| `Commit` | 哪个时钟/顺序边界后结果才成为架构状态？异常如何保持精确？ | CO-03、CO-04、CO-I01 |
| `Cost` | 关键路径、周期、CPI、stall、miss penalty、带宽和总时间从哪里来？ | `90_做题规则`，各 Topic 提供局部参数 |

性能是跨 Topic 的成本坐标，不是第九个硬件子系统；任何性能结论都必须回到同一程序、同一 IC、完整 CPI 与时钟周期。

## 四个学习轴

- **Semantic State**：数据表示、ISA、异常/中断语义决定“允许改变什么”；
- **Data Location**：寄存器、主存、Cache、TLB、I/O 决定“现在在哪里”；
- **Datapath / Control / Timing**：通路、控制与时钟决定“怎样走、什么时候能用”；
- **Resource / Cost**：ALU、端口、总线和存储系统有限，冲突和缺失决定“哪里等待、付出什么代价”。

学习某一册时，先指出它主要占据哪个轴，再列出它向相邻 Owner 输出的状态包；不要把局部机制重新写成整门学科模型。

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
| [Cache 与存储层次](60_Cache与存储层次/README.md) | 怎样维护一个正确的高速副本？ | 不拥有 OS Page Cache |
| [地址翻译与虚拟存储硬件](70_地址翻译与虚拟存储硬件/README.md) | VA 怎样经 TLB/页表形成 PA 并继续访问 Cache/Memory？ | 不拥有 frame 分配、换页、COW 和 fault policy |
| [总线与 I/O 硬件](80_总线与IO硬件/README.md) | 同步 CPU 怎样通过共享事务与异步设备合作？ | 不拥有 OS block/wakeup 和驱动策略 |

专题 Source 已按 `10_` 到 `80_` 路由。CO-01 至 CO-08 已形成待人工确认的 Canonical LaTeX 候选正文；新知识进入各 Topic 唯一 Owner，README 不再承载深层机制。

## 贯穿母例：`LOAD rd, disp(rs)`

| 六格 | LOAD 中要追踪的事实 | 交接 |
|---|---|---|
| `ISA State` | `Reg[rd] <- M[Reg[rs] + sign-extended disp]`，并按 ISA 推进 `PC` | CO-01/02 |
| `Data Location` | 指令先在 I-Cache/Memory，`rs` 在寄存器，数据可能在 Cache、主存或设备 | CO-05/06/08 |
| `Datapath / Control` | 读寄存器、扩展立即数、ALU 生成 EA、选择访存端口和写回通路 | CO-03/B01 |
| `Timing` | EA、翻译、Cache 数据何时 ready；后继指令何时 need；是否 forwarding/stall | CO-04 |
| `Commit` | 无权限/翻译/访存异常后，只有合法路径才写 `rd` 并提交 `NextPC` | CO-07/B02/I01 |
| `Cost` | TLB/Cache hit-miss、memory/bus wait、hazard、CPI 与周期时间如何组合 | Rules/I01 |

这张表只负责导航；翻译、Cache、通路、流水线和总线的具体机制仍由各自 Canonical `.tex` 拥有。

## 计组核心边界

| 不能混用 | 判据 | 典型错误 |
|---|---|---|
| ISA 与 Microarchitecture | 指令/寄存器/寻址语义看 ISA；流水级、预测、内部端口看实现 | 把某 CPU 的实现细节当成所有同 ISA 机器都必须如此 |
| CPI 与程序总时间 | `CPU time = IC x CPI x clock period` | 只看 CPI 或 GHz 宣称更快 |
| Pipeline throughput 与 instruction latency | 填满后每周期完成几条 vs 某条指令从进入到完成多久 | 把五级流水说成每条指令只需一个周期 |
| Address field 与 full address | 字段可能是寄存器号、立即数、偏移，需 EA 生成 | 直接把字段当绝对地址 |
| TLB miss、Page Fault、Cache miss | 翻译副本、映射/权限、数据副本是三个处理者不同的状态机 | 一看到 miss 就默认磁盘 I/O |
| Interrupt 与 DMA | Interrupt 解决通知，DMA 解决批量搬运 | 认为 DMA 完全不需要 CPU 或中断 |

## 计组做题六步入口

下面是**检查顺序**，不是硬件事件的唯一时间顺序：

1. 抄出题目给定的 PC、寄存器、PTE、Cache 行、队列和目标架构状态；
2. 标记指令与操作数当前在哪里，miss 后下一层是谁；
3. 画当前题真正经过的最小数据通路；
4. 检查 ALU、端口、总线、存储器和写口的资源冲突；
5. 对每个值标 `produced / ready / consumer need`，再计算 stall、miss penalty 或带宽；
6. 最后确认异常/提交边界，统一 `IC x CPI x clock period` 的成本口径。

若题目是“TLB miss、PTE 有效、Cache hit”的虚拟地址访问，先走 page walk/refill 得到 PA，再访问 Cache；不要把 TLB miss 改写成 Page Fault。

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
- [CO-I01｜一条指令的一生](86_综合专题/CO-I01_一条指令的一生/README.md)：优先以 LOAD 为贯穿对象，按执行过程追踪 ISA 语义、CPU 通路、流水时序、地址翻译、Cache/Memory 与最终架构可见状态；具体事件顺序由该 Integration 明确标注。

CO-B01、CO-B02 与 CO-I01 的 Canonical 候选正文均已建立并发布；它们只拥有跨 Owner handoff 或组合过程，不复制八个 Topic 的局部机制。

C 语言语义到 ISA 机器级语义的映射仍由 ISA Topic Own，不再把 `C × ISA × CPU` 建成跨科 Bridge。原 `85_科内桥梁与综合/` 旧稿保留为 Source/legacy work draft，不再拥有新的 Bridge/Integration 定义。

Cross-Subject Bridge 统一上移到 [408 Cross-Subject Bridge Atlas](../50_桥梁专题/README.md)：Privilege/Exception × OS、Hardware Address Translation × OS VM、Interrupt/DMA × OS I/O。

跨科母模型入口：[缓冲与有限中间态](../00_统一总图/跨科母模型_缓冲与有限中间态.md)。MDR/MBR、流水寄存器、I/O FIFO、写缓冲和 DRAM 行缓冲都可借它建立“有限中间态”直觉，但各自的时序、状态与性能公式仍由 CO-03/04/05/06/08 拥有。

## 性能的归属

性能不是第九个硬件子系统。IC、CPI、IPC、clock、critical path、latency、throughput、bandwidth、AMAT 与 speedup 进入[计组做题规则](90_做题规则/README.md)中的性能工具箱，各 Topic 只使用与自身机制直接相关的指标。

## 真题训练层

稳定机制仍由八个 Topic、Bridge 与 Integration 拥有；真题训练只负责把题面转换成可调用的 Owner、状态轨迹和成本输入，不建立第二套理论。存储系统跨 CO-05 / CO-06 / CO-07 / CO-B02 / OS-04 的统一训练入口见 [存储系统真题训练总索引](90_做题规则/存储系统真题训练总索引.md)。其中六类传统题型仅作检索标签，统一按 `Request → Granularity → Stream → Owner → State → Count → Cost → Verify` 推进。

## Question Control Adapter

下面七问是推荐检查顺序：

1. 当前软件可见状态是什么？
2. 数据现在在哪里？
3. 它将经过哪条硬件路径？
4. 需要哪些共享资源，是否冲突？
5. 数据何时可用，在哪个周期边界锁存？
6. 最终何时改变体系结构状态？
7. 这条完整路径的等待、带宽、CPI 或总时间代价是什么？

## 建议审查顺序

建议依次审查 Atlas、CPU 数据通路与控制、ISA 与机器级程序、流水线、Cache / 地址翻译、数据表示 / 主存 / I/O，最后用《一条指令的一生》做组合验收。这个顺序服务审查效率，不表示这些 Topic 构成单向因果链。

审查时优先攻击《CPU 数据通路与控制》的“架构状态差、数据依赖、合法通路与微操作”以及《一条指令的一生》的跨层慢路径；它们决定其余 Topic 是否能被统一调用。
