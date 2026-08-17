# 计组科内桥梁与综合：从 C 语句到一次精确提交

状态：legacy-unregistered Source；不再作为 Canonical Bridge / Integration Owner。

> 新的唯一 Owner 已拆分为 `85_科内桥梁/CO-B01`、`85_科内桥梁/CO-B02` 与 `86_综合专题/CO-I01`。本文件保留旧工作稿内容供 Source Diff，不再继续在这里新增稳定定义。

## 1. 这份旧稿原来试图解决什么

八个 Topic 分别拥有稳定机制，本册只拥有它们之间的接口：

1. **C × ISA × CPU Bridge**：同一个程序动作在语言、指令契约和数据通路上分别是什么；
2. **一条指令的一生 Integration**：从取指到提交，串起流水线、翻译、Cache、主存和异常；
3. **设备读取接口**：只串到硬件完成通知，不复制 OS 的阻塞/唤醒策略。

统一主线：

```text
Meaning
-> ISA State Delta
-> Values and Addresses
-> Hardware Route
-> Resource Schedule
-> Precise Commit
```

## 2. Bridge：C、ISA 与 CPU 是三种不同描述

| 层 | 关注对象 | 典型问题 | 不应越界 |
|---|---|---|---|
| C / language | 类型、对象、表达式、控制流 | 程序想得到什么？ | 不承诺具体指令序列 |
| ABI/compiler | 参数、栈帧、寄存器分配 | 怎样表示成某 ISA 程序？ | 不承诺内部硬件 |
| ISA | 架构状态和指令语义 | 每条指令必须改变什么？ | 不规定流水级与 Cache |
| microarchitecture | 路径、端口、时序、预测 | 怎样实现 ISA？ | 不得改变可见语义 |

一条高级语句可以映射成多条指令，一条复杂指令也可以包含多个内部微操作。两个“多步”不是同一层。

## 3. C 表达式如何生成机器活动

以：

```c
y = a[i] + b;
```

为母例。若元素类型大小为 $w$ B：

$$
EA_a=base(a)+i\times w
$$

可能的机器级语义链：

```text
scale i
-> add base to form VA
-> load element
-> add b
-> place result in y's assigned location
```

这里至少有四种独立决定：

- C 类型决定元素大小、扩展和溢出语义的一部分；
- 编译器决定是否把变量保存在寄存器、是否合并地址计算；
- ISA 决定可用指令与可见结果；
- CPU 决定每条指令的路径和时序。

因此看到汇编题，先问这是语言必然、ABI 约定、ISA 事实还是当前实现选择。

## 4. 一条指令的生命周期状态机

```text
Fetch
-> Decode / Operand Read
-> Execute / Address Generation
-> Translate
-> Cache / Memory
-> Writeback Candidate
-> Commit
```

并非每条指令都经过全部阶段，阶段也不等于固定一个周期。这个状态机描述逻辑职责：

- Fetch 根据 PC 取得指令编码；
- Decode 产生 ISA 操作和控制需求；
- Operand Read 取得架构源值或旁路值；
- Execute 产生算术结果、条件或 VA；
- Translate/Memory 为访存指令提供授权后的数据；
- Commit 才改变软件可见状态。

## 5. 母指令一：ADD

### 语义

$$
R[rd]\leftarrow R[rs1]+R[rs2]\pmod{2^n}
$$

### 接口链

1. ISA 指定源、目标和位宽解释；
2. register file 或 forwarding 提供操作数；
3. ALU 执行模 $2^n$ 加法并产生必要状态；
4. 流水线检查 RAW 和功能部件冲突；
5. 无异常时结果写回/提交。

### 核验

- carry 与 signed overflow 按不同解释判断；
- ALU produced 不等于 committed；
- forwarding 可早于 register-file write。

## 6. 母指令二：LOAD

### 语义

$$
\begin{aligned}
VA&\leftarrow R[base]+\operatorname{sign\_extend}(immediate),\\
R[rd]&\leftarrow \operatorname{extend}(M[VA,width]).
\end{aligned}
$$

### 完整路径

```text
PC -> instruction fetch
-> decode/load operands
-> ALU forms VA
-> TLB hit or page walk
-> permission check and PA
-> cache hit or line fill
-> byte select and extension
-> rd commit
```

### 三个独立等待点

- operand producer 尚未给出 base：pipeline RAW；
- translation cache 没有 VPN：TLB miss/page walk；
- data cache 没有 block：Cache miss/fill。

三者可能叠加，但处理对象和恢复路径不同。

### 精确性

若翻译或权限异常，`rd` 不能写入部分/猜测值；较年轻指令的副作用必须被阻止。OS 修复后可以重试，但架构上 load 只成功提交一次。

## 7. 母指令三：STORE

### 语义

$$
\begin{aligned}
VA&\leftarrow R[base]+\operatorname{sign\_extend}(immediate),\\
M[VA,width]&\leftarrow \operatorname{low\_width\_bits}(R[data]).
\end{aligned}
$$

### 与 LOAD 的关键差异

- 同时依赖地址源和写数据源；
- 最终提交对象是内存状态，不是通用寄存器；
- Cache write policy 决定副本和下一级何时更新；
- 发生异常时不能留下部分可见写入。

在更复杂实现中，store 可以先进入内部 buffer，再在安全边界成为全局可见；本册只保留“执行准备”与“架构/内存可见提交”必须区分的不变量。

## 8. 母指令四：BRANCH

### 语义

$$
\begin{aligned}
condition&\leftarrow \operatorname{compare}(operands),\\
next\_PC&\leftarrow
\begin{cases}
target,&condition=true,\\
sequential\_PC,&condition=false.
\end{cases}
\end{aligned}
$$

### 接口链

1. ISA 规定比较和 target 形成；
2. 数据通路读取操作数并计算条件/目标；
3. 流水线在结果未知时预测或等待；
4. 若预测错误，错误路径指令被 flush；
5. 正确 next PC 成为后续取指依据。

验证点：错误路径可以被取指甚至执行，但不得留下架构副作用。

## 9. Function Call：控制流与存储的联合接口

函数调用可拆成：

```text
argument placement
-> save return address / transfer PC
-> stack-frame and callee-save actions
-> body instructions
-> restore agreed state / return
```

栈是普通内存区域，因此 push/pop 或 load/store 会经过翻译与 Cache；返回地址是控制流状态；哪些寄存器由谁保存是 ABI 契约。把三者分开才能解释递归、叶函数优化和栈访问性能。

## 10. 设备读取：只连接硬件半程

```text
CPU writes controller command
-> controller/device works asynchronously
-> PIO or DMA moves data
-> status becomes done / IRQ pending
-> CPU takes precise interrupt entry
```

若使用 DMA：DMAC 成为互连 master，与 CPU 竞争内存带宽；Cache coherence 或 buffer 可见性取决于具体平台。硬件完成中断之后的驱动处理、阻塞进程唤醒和用户态返回，进入全局 `Interrupt / DMA x OS` Bridge，而不在这里复述。

## 11. 统一慢路径表

| 事件 | 检测者 | 缺失/冲突对象 | 处理者 | 恢复点 | 提交约束 |
|---|---|---|---|---|---|
| RAW hazard | pipeline control | 尚不可用的值 | forwarding/stall hardware | 依赖满足后推进 | 消费者不可读旧值 |
| structural hazard | scheduler/control | 共享硬件资源 | stall/arbitrate | 资源可用后推进 | 不得同时非法占用 |
| branch mispredict | branch unit | 正确控制路径 | flush/redirection hardware | 正确 target fetch | 错路不提交 |
| TLB miss | translation unit | 翻译副本 | HW walk 或 SW，依 ISA | refill/retry | 权限通过前不提交访问 |
| Cache miss | cache controller | 数据块副本 | memory hierarchy | fill/retry | 返回正确 block |
| page/access fault | MMU | 映射/权限 | precise exception + OS | ISA 指定位置重试/终止 | faulting 副作用不提交 |
| external interrupt | interrupt logic | 异步事件待处理 | HW entry + software ISR | return PC | 保存可恢复边界 |

## 12. 性能怎样穿过各层

总执行时间不是把所有局部“速度”口号相加，而是建立事件频率与事件成本：

$$
T=IC\times CPI_{base}\times T_{clk}+\sum_j count_j\times penalty_j
$$

其中某些 penalty 已包含在 CPI，某些能与其他工作重叠。综合题必须先声明成本模型，防止流水 stall、Cache miss penalty 和内存时间重复计算。

一条 LOAD 的平均成本可分层递归，但不应把所有路径都当串行：VIPT 可并行 TLB 与 set lookup，乱序核可隐藏部分 miss，DMA 可与 CPU 计算重叠。题设未说明时，只采用题设的简化模型并明确假设。

## 13. 跨层不变量

1. **表示一致**：load 的字节选择、扩展与 ISA 类型一致；
2. **地址合法**：翻译与权限通过后，数据才可被指令使用；
3. **身份正确**：Cache 必须 valid+tag 命中，不能只靠 index；
4. **资源合法**：同拍端口和总线占用满足硬件约束；
5. **时间合法**：消费者不早于 value available；
6. **提交精确**：异常、误预测和中断边界不留下错误副作用。

## 14. 综合题调用协议

1. 写语言/ISA 层的目标状态，不先进入 Cache 公式；
2. 把每条指令分类为 ALU、LOAD、STORE、BRANCH 或 control/system；
3. 对每条指令填六列：State、Location、Path、Resource、Timing、Commit；
4. 对访存地址依次做 EA、translation、Cache、memory；
5. 对每个“未找到/未就绪”查统一慢路径表；
6. 建流水时间图和共享资源占用图；
7. 用跨层不变量做最终核验；
8. 将局部事件数代入已声明的性能模型。

## 15. 最小反例

- 编译器生成了 load，不代表每次循环都访问主存；Cache hit 可在上层满足。
- Cache 中已有目标物理块，不代表虚拟访问有权限读取它。
- DMA 已写入内存，不自动推出 CPU Cache 立即看到新值；是否一致依平台机制。
- 分支结果已算出，不代表此前取入的错误路径指令可以提交。

## 16. 压缩页：一条 LOAD 的六问

| 问题 | LOAD 的回答 |
|---|---|
| State | base、PC、目标寄存器旧值 |
| Location | 指令在 I-cache，base 在寄存器，数据在某级存储 |
| Path | decode -> ALU -> TLB -> D-cache/memory -> writeback |
| Resource | reg ports、ALU、TLB、cache port、memory bus |
| Timing | base ready、translation ready、data ready |
| Commit | 无异常且数据正确时更新 rd |

## 17. Stop Boundary

- C 语言完整语义和编译优化不在本册拥有；
- Cache coherence、多核内存模型不在当前 408 主干展开；
- Page Fault 修复、frame replacement、block/wakeup 属于 OS；
- 磁盘调度和文件系统路径不进入“一条指令的一生”。

## 18. 来源与校验

- 归档 23 份计组笔记提供题型和旧解释；7 个空文件只记为材料缺口，没有被伪装成已有模型。
- [RISC-V RV32I](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)提供 ADD/LOAD/STORE/BRANCH 的公开 ISA 锚点。
- [RISC-V Supervisor ISA](https://docs.riscv.org/reference/isa/v20260120/priv/supervisor.html)提供地址翻译与精确异常接口锚点。
- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/)提供浮点格式和运算边界锚点。
