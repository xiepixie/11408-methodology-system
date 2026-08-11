# 总线与 I/O 硬件：同步处理器怎样与异步设备合作

状态：Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建。

> **迁移提示**：以下长篇内容是此前误写在 README 中的 working source。它可用于后续 Source Diff，但不再视为 Handbook 正文。正式手册必须迁入同目录 `.tex`；迁移完成后本 README 将压缩为引子、范围、边界和阅读链接。

## 1. 母问题

多个速度不同、完成时间不确定的部件，怎样共享有限通信线路并完成可确认的请求与数据传输？

```text
request intent
-> controller state
-> arbitration
-> address/control/data phases
-> completion evidence
-> interrupt or polling observation
```

总线解决共享通信，控制器把设备细节转换为寄存器和事务，PIO/中断/DMA 决定谁搬数据、谁等待完成。

## 2. 总线不是一捆静态导线，而是协议

总线事务至少包含：请求、仲裁、寻址、命令、数据与完成/释放。共享性要求任一时刻只有合法主设备驱动对应线路；分时性把低硬件成本换成等待与仲裁。

| 角色 | 责任 |
|---|---|
| master / initiator | 获得使用权并发起事务 |
| slave / target | 解码地址、响应命令 |
| arbiter | 在竞争者中授予共享资源 |
| interconnect | 传输地址、数据、控制与响应 |

“CPU、内存、设备”不是固定主从：DMA 控制器获得总线后可成为 master，内存成为 target。

## 3. 地址、数据、控制三类信息

- 地址标识目标和位置；地址线可能分时复用，位数不能直接套作单周期可传数据量；
- 数据线宽度给出每个 beat 的最大原始数据位数；
- 控制/响应表达 read/write、byte enable、ready、error、interrupt、request/grant 等协议状态。

理论峰值带宽：

$$
BW_{peak}=bytes/beat\times beats/cycle\times frequency
$$

有效带宽还要乘协议效率和利用率。地址阶段、等待状态、仲裁、编码与方向切换都可能消耗周期。

## 4. 同步、异步与分离事务

### 同步

双方按共同 clock 的规定周期采样。控制简单、吞吐高，但慢设备需 wait state 或适配。

### 异步握手

请求/应答边沿建立完成关系，可适配不同速度。可靠性来自握手，而非“没有时钟所以更慢”的定义。

### 分离事务

请求发出后释放通道，响应稍后作为独立阶段返回；可在长延迟期间服务其他请求，但需要事务 ID、缓冲和匹配逻辑。

同步/异步描述定时协议，串行/并行描述物理传输方式，两组概念不能互相替代。

## 5. 仲裁：共享资源的选择策略

集中式链式查询、计数器轮询、独立请求，或分布式仲裁，本质都在权衡：

- 优先级与响应延迟；
- 公平性与饥饿；
- 仲裁速度；
- 请求/授权线路成本；
- 故障影响范围。

固定优先级可降低关键设备延迟，却可能使低优先级长期饥饿；轮转改善公平性，但最坏响应时间和状态复杂度增加。

## 6. I/O 接口：把设备变成寄存器状态机

典型控制器暴露：

- data register / FIFO；
- status register：ready、busy、done、error；
- control/command register；
- 可选地址、计数、描述符和中断屏蔽寄存器。

### 编址

- memory-mapped I/O：普通地址空间和 load/store 访问控制器寄存器；
- isolated I/O：独立端口空间和专用指令。

区别在软件可见寻址契约，不意味着设备本身更快。MMIO 还需遵守设备访问顺序和不可随意缓存等体系结构规则。

## 7. 三种控制方式：谁等待，谁搬数据

| 方式 | CPU 等待方式 | 数据路径 | 完成发现 | 适合 |
|---|---|---|---|---|
| polling / PIO | 循环读状态 | device <-> CPU reg <-> memory | 主动查询 | 简单、短且快事件 |
| interrupt-driven | 可先做别的工作 | 通常仍由 CPU 指令搬运 | 设备异步通知 | 低/中速、事件型 |
| DMA | CPU 只配置和收尾 | device <-> memory | 块完成/错误中断 | 大块、高速传输 |

中断减少 busy waiting，不消除 ISR 和数据搬运成本；DMA 减少传输阶段的 CPU 指令，不代表完全不需 CPU，也不代表不占总线。

## 8. 中断硬件路径与精确入口

外部设备通过控制器提出异步请求。CPU 在体系结构允许的边界检查待处理中断，结合 enable/mask/priority 决定是否接受，并保存 ISA 规定的最小返回状态、切换到处理入口。

```text
device event
-> pending request
-> arbitration / priority / mask
-> precise boundary
-> save architectural return state
-> vector/entry
```

具体是否自动关中断、保存哪些寄存器、向量表怎样寻址都依 ISA。通用寄存器的完整保存、驱动服务、进程唤醒和调度通常属于软件。

### 异常与中断

- exception 与当前指令同步相关；
- external interrupt 与当前指令异步；
- trap/fault 等术语的精确定义以 ISA 为准。

二者可共享入口框架，但不能仅因都“跳到处理程序”就混为一个因果类型。

## 9. DMA：把搬运循环下沉到硬件

CPU 预先配置 source/destination、length、direction/control；DMAC 在设备与内存之间发起事务，更新地址与计数，完成或错误后通知 CPU。

```text
CPU setup
-> device/DMA request
-> bus arbitration
-> transfer beats
-> address/count update
-> completion interrupt
```

### 三种共享方式

- burst：一次授权后连续传一块，吞吐高，但 CPU 可能长时间失去总线；
- cycle stealing：每次占用一个或少量周期，在带宽和 CPU 干扰间折中；
- transparent/interleaved：利用 CPU 不使用总线的时隙或固定分时，依具体硬件时序。

“DMA 优先级高于所有中断”“每字必发一次 DREQ”“CPU 在 burst 中完全不能工作”都不是跨系统不变量，应以题设总线和控制器模型为准。

## 10. 硬件与 OS 的 Stop Boundary

| 阶段 | 计组 Hardware Owns | OS / Bridge Owns |
|---|---|---|
| 请求 | 控制器寄存器、命令事务 | syscall、驱动策略、请求队列 |
| 等待 | busy/done/IRQ 状态 | block、schedule |
| 传输 | PIO 数据寄存器或 DMA 事务 | buffer policy、映射准备 |
| 完成 | interrupt entry、status | ISR 业务、wake up、错误恢复 |

本 Topic 可说“硬件产生中断并进入处理入口”，不把“唤醒哪个进程”写成硬件动作。

## 11. 母例：DMA 读取一个块

1. CPU/驱动准备可供设备使用的内存地址与长度；
2. 写 DMAC/设备控制寄存器启动请求；
3. DMAC 与 CPU 或其他 master 竞争互连；
4. 获授权后在设备与主存之间传输若干 beat，并更新计数；
5. 若总线或内存冲突，延迟体现在共享资源等待；
6. 完成时控制器置状态并产生中断；
7. CPU 在精确边界进入处理入口；
8. 后续确认、解除映射、唤醒与返回由软件完成。

## 12. 做题调用协议

1. 标 initiator、target、数据方向和完成条件；
2. 把事务拆成 arbitration/address/data/response；
3. 标每阶段占用的总线或端口；
4. 计算峰值后再扣除 wait、控制和空闲；
5. I/O 方式题明确“谁搬数据、CPU 何时参与、完成怎样发现”；
6. 中断题分硬件最小入口与软件保存/服务；
7. DMA 题分 setup、transfer、completion，避免把总线暂停当上下文切换。

## 13. 最小反例

- DMA 传输不经过 CPU 寄存器，但仍占用内存与互连带宽。
- 中断方式让 CPU 与设备工作重叠，却可能因事件太密使入口开销超过轮询。
- 数据总线 64 位、1 GHz 不自动等于 8 GB/s 有效带宽；每周期 beat 数和协议效率未知。
- CPU 暂停一次总线访问不等于保存现场进入 ISR。

## 14. 压缩信号

> 总线题追踪“谁在何时拥有线路”；I/O 题追踪“谁搬数据、谁证明完成”。

## 15. 来源处理

归档《总线结构》《IO 控制方式》《中断处理》《DMA》《磁盘》用于题型覆盖。原笔记中的驱动、阻塞、唤醒、缓冲和磁盘调度只作为跨 OS 接口，不在本 Topic 建第二份稳定定义；空白的《总线计算》《IO 接口》未被当作已有模型。
