# 计算机组成原理学科总图：ISA 语义如何成为硬件时序

状态：Source；Atlas Deep Map 工作稿，待与根目录 Canonical Subject Atlas README 做 Source Diff。

> **迁移提示**：以下内容保留为计组 Atlas 的旧 Deep Map Source，用来检查根 Atlas 是否漏掉重要母模型、边界或路由。当前正式 Subject Atlas 已由 `../README.md` 直接拥有，不再把这份旧稿迁成第二份 Atlas `.tex`。

> Position：本文件是 [Computer Organization Subject Atlas](../README.md) 的 **Atlas Deep Map Supplement**。根 `README.md` 是唯一 Subject Atlas 导航 Owner；本文件保留更展开的学科母模型、边界与调用协议工作稿。

## 1. 学科母问题

计算机组成原理不只是罗列部件，而是在回答一个约束实现问题：

> 怎样用有限位宽、有限端口、有限带宽和有限速度的硬件，实现 ISA 承诺的程序语义，并让各种加速对软件保持透明？

统一生成链是：

```text
ISA Semantic
-> Data Movement
-> Hardware Path
-> Timing / Arbitration
-> Architectural State Commit
```

每道题都可以投影到六问：

```text
State -> Location -> Path -> Resource -> Timing -> Commit
```

- **State**：指令开始前，软件可见状态是什么？
- **Location**：源数据和目标数据此刻在哪里？
- **Path**：数据要经过哪些组合逻辑、寄存器和接口？
- **Resource**：哪些端口、总线、功能部件被共享？
- **Timing**：值何时产生、何时可被后继使用？
- **Commit**：何时才真正改变寄存器、内存或 PC？

## 2. 为什么部件清单不是模型

朴素学习会把 ALU、Cache、TLB、总线和 DMA 分章记忆。它在综合题中失效，因为同一个名字可能处在不同层：

- ISA 规定 `LOAD` 的可见效果，却不规定它用单周期、多周期还是流水线实现；
- Cache miss 和 TLB miss 都会“没找到”，但缺的是数据副本还是地址翻译；
- 数据已经算出，不等于已经提交；DMA 已经搬完，也不等于等待者已经被 OS 唤醒。

真正稳定的对象不是部件名，而是三类契约：

| 契约 | 约束谁 | 核心问题 |
|---|---|---|
| 表示契约 | 位串与解释 | 同一位串按什么类型、位宽和舍入规则解释？ |
| ISA 契约 | 软件与处理器 | 指令必须产生什么可见状态变化？ |
| 微架构契约 | 硬件内部 | 用什么路径、资源和时序实现该变化？ |

## 3. 对象、表示与状态

一串比特本身既不是整数，也不是地址或指令。它的意义来自解释上下文。

```text
bits + width + interpretation + operation
-> value / address / instruction / control field
```

因此解题时必须分开：

- **对象**：数值、指令、地址、缓存块、页表项、总线事务；
- **表示**：补码、IEEE 754、指令字段、tag/index/offset、VPN/offset；
- **载体**：寄存器、Cache line、DRAM row、控制器寄存器；
- **状态变化**：寄存器写回、PC 重定向、Cache line 置脏、PTE 检查、中断入口。

## 4. 三条主线

### 4.1 指令主线

```text
C operation
-> ISA instruction sequence
-> fetch / decode
-> operand read
-> execute / memory
-> commit
```

它连接 [ISA 与机器级程序](../20_ISA与机器级程序/README.md)、[CPU 数据通路与控制](../30_CPU数据通路与控制/README.md)和[流水线](../40_流水线与指令级并行/README.md)。

### 4.2 存储主线

```text
virtual address
-> translation
-> physical address
-> cache lookup
-> memory transaction
-> DRAM / storage medium
```

地址翻译回答“对象在哪里”，Cache 回答“高速副本是否在这里”，主存硬件回答“物理地址怎样落到芯片和阵列”。三者不能用一个“访存”黑箱代替。

### 4.3 外设主线

```text
CPU programs controller
-> device progresses asynchronously
-> PIO / interrupt / DMA transfers or reports
-> precise architectural entry
```

计组拥有寄存器、事务、仲裁、中断入口和 DMA 搬运；进程阻塞、驱动策略与唤醒属于 OS 或跨学科 Bridge。

## 5. 五个全局不变量

1. **位宽守恒**：截断、扩展、移位和舍入必须显式说明目标位宽。
2. **单一驱动**：共享总线同一时刻至多一个发送者，多个接收者可以同时锁存。
3. **资源排他**：单端口存储器、ALU、总线等资源同一拍不能服务互斥请求。
4. **顺序语义**：内部可重叠和推测，已提交状态必须等价于 ISA 顺序执行。
5. **慢路径闭环**：miss、fault、interrupt 都必须写出检测者、处理者、恢复点与是否重试。

## 6. 优化从哪里生成

每种优化都由同一个问题生成：关键路径或共享资源成为瓶颈。

| 瓶颈 | 机制 | 获得 | 付出 |
|---|---|---|---|
| 组合路径过长 | 流水寄存器切段 | 更高吞吐 | hazard、寄存器开销、单条延迟未必下降 |
| 远端存储过慢 | Cache / TLB | 平均延迟下降 | 副本、替换、一致性与 miss 慢路径 |
| 总线等待设备 | 中断 / DMA | CPU 与设备重叠 | 入口开销、仲裁、完成同步 |
| 控制信号复杂 | 微程序控制 | 规则化、可扩展 | 控制存储与译码时延 |
| 物理阵列端口不足 | 多模块交叉编址 | 带宽提升 | 地址分布、冲突和控制复杂度 |

不能只写“更快”。任何优化都要同时回答正确性不变量和新增成本。

## 7. Topic Ownership

| Topic | Owns | Uses | Stop Boundary |
|---|---|---|---|
| 数据表示与运算 | 位宽、补码、标志、IEEE 754 | ISA 运算语义 | 不展开完整数据通路 |
| ISA 与机器级程序 | 指令可见语义、寻址、C 映射 | 表示规则 | 不拥有实现时序 |
| CPU 数据通路与控制 | 单条指令的部件、微操作和控制 | ISA | 不展开多指令重叠 |
| 流水线 | 重叠执行、hazard、stall/forward/flush | 单指令路径 | 不重写 ISA |
| 主存与存储硬件 | 芯片、阵列、扩展、DRAM、介质 | 物理地址 | 不拥有 Cache 协议 |
| Cache 与存储层次 | 高速副本的定位、命中、替换和写策略 | 局部性、主存 | 不拥有 OS Page Cache |
| 地址翻译硬件 | VA 到 PA、PTE、TLB、page walk | ISA 访存、Cache | 不拥有换页策略 |
| 总线与 I/O 硬件 | 事务、仲裁、控制器、中断、DMA | CPU/存储接口 | 不拥有进程阻塞与唤醒 |

## 8. 母例：一条 LOAD

以 `LOAD rd, imm(rs1)` 为压缩全景：

1. ISA 定义 $EA=R[rs1]+\operatorname{sign\_extend}(imm)$，成功时 $R[rd]\leftarrow M[EA]$；
2. 数据通路读取 `rs1`，ALU 形成地址；
3. 若启用虚拟存储，VA 经 TLB 或 page walk 形成 PA，并检查权限；
4. PA 被拆成 Cache 的 tag/index/offset；
5. hit 时选出目标字节并扩展，miss 时访问下一级并填充；
6. 流水线保证依赖者只在值可用后消费；
7. 无异常时才写 `rd`，有精确异常时该指令及之后的副作用不得提交。

这个例子揭示两个常见混淆：地址形成不等于地址翻译，数据返回不等于体系结构提交。

## 9. 题目调用协议

面对陌生题，按以下顺序：

1. 抄出 ISA 级初态和目标状态，不先画电路；
2. 给每个值标注位置、位宽与解释；
3. 画最短数据路径，列出必经寄存器和组合部件；
4. 建资源占用表，寻找同拍冲突；
5. 建时间轴，区分 produced、available、latched、committed；
6. 单独展开 miss/fault/interrupt 慢路径；
7. 用不变量核验：位宽、权限、旧值保存、提交顺序是否成立。

## 10. 压缩信号

> 计组题不是问“这个部件是什么”，而是问：一个有类型、有位宽的状态变化，经过哪些有限资源，在什么时刻被正确提交。

## 11. 校验依据

- [RISC-V Unprivileged ISA, RV32I](https://docs.riscv.org/reference/isa/v20260120/unpriv/rv32.html)：用于校验基础整数、分支与访存的 ISA 可见语义。
- [RISC-V Privileged ISA, Supervisor](https://docs.riscv.org/reference/isa/v20260120/priv/supervisor.html)：用于校验异常入口、PTE 与地址翻译的硬件/软件边界。
- [IEEE 754-2019](https://standards.ieee.org/ieee/754/6210/)：用于校验浮点格式、运算、舍入与异常条件的范围。
