# 基础概念与 Owner 定位

> 训练定位：面对操作系统基础、程序运行环境、OS 结构、引导与机器虚拟化等概念题时，训练先判断当前对象和层次，再把进入局部机制的问题送到正确 Canonical Owner。  
> 模型归属：[OS-00 操作系统基础与程序运行环境方法论手册](OS-00_操作系统基础与程序运行环境_方法论手册.tex)。abstraction、virtualization、protection、程序运行映像、OS 结构与 boot 的机制由 Canonical 正文拥有；本文件只负责概念辨析与路由。

## 七个定位问题

1. 当前谈的是物理资源、OS 抽象，还是程序可见对象？
2. 题面主要在问 abstraction、virtualization、protection 还是 policy？
3. 并发、共享、虚拟、异步中，真正描述的是哪一种性质？
4. 当前对象是 program、object file、executable、process image 还是 process？
5. 正在追踪数据/符号绑定，还是 CPU 控制权？
6. 比较 OS 结构时，privilege boundary 画在哪里？
7. 若已经进入进程、同步、页表、I/O、文件内部机制，应转交哪个 Owner？

## 局部规则：概念题先锁对象再判断性质

**触发信号**：选项用“程序/进程”“装入/驻留”“中断/切换”等相近词替换。

**第一动作**：先给题目中的名词标对象层：静态描述、运行映像、动态实例、CPU 模式、任务状态或资源抽象。

**检查与退出**：如果两个选项说的根本不是同一层对象，不要继续比较表面措辞；先回到 Canonical 的对象定义。

## 局部规则：地址题固定做“地址四问”

**触发信号**：题面同时出现目标文件、链接、重定位、逻辑地址/虚拟地址、装入地址、物理地址、页表或页框等词。

**第一动作**：不要先算数值，先给当前地址补全四个限定词：

1. **属于哪个地址空间/表示？** 文件偏移、节内偏移、程序级虚拟地址、进程 VA，还是 PA？
2. **相对谁解释？** 相对本 section、本模块、PC、某个装入基址，还是页表映射？
3. **谁拥有足够信息决定它？** 汇编器、链接器、Loader/OS，还是 MMU + 当前页表？
4. **什么时候才确定？** 汇编时、链接时、装入时，还是每次真正访问时？

**检查与退出**：只要两步地址变换的“地址空间、Owner 或确定时机”不同，就不能把它们合并成一个“地址换算”。一旦进入 VA→PA、页表、驻留/缺页，停止在 OS-00，转交 OS-04 / CO-07。

## 常用边界

| 对象 A | ≠ | 对象 B | 第一判据 |
| ------------- | ------- | ------------------ | -------------------------------- |
| Abstraction | ≠ | Virtualization | 接口简化 vs 逻辑化/复用物理资源 |
| Concurrency | ≠ | Parallelism | 一段时间内共同推进 vs 同一时刻物理同时执行 |
| Mechanism | ≠ | Policy | 如何做到 vs 选择谁/选择什么 |
| Program | ≠ | Process | 静态描述 vs 某次动态执行实例 |
| Executable | ≠ | Process Image | 文件表示 vs 某次执行形成的运行时表示 |
| Section | ≠ | Program Segment | 链接/静态组织单位 vs 装入映射单位 |
| Link-time Relocation | ≠ | Run-time Address Translation | 修补目标/映像中的地址相关引用 vs 每次访问时 VA→PA |
| Loading | ≠ | All Pages Resident | 建立运行映像/映射 vs 所有内容已兑现到 RAM |
| Task State | ≠ | CPU Mode | Ready/Blocked/Running vs User/Kernel privilege |
| Monolithic | ≠ | Non-modular | 特权边界位置 vs 软件内部组织方式 |
| Firmware | ≠ | Bootloader | 早期平台环境 vs 选择/装载内核的后续阶段 |
| OS Virtualization | ≠ | Machine Virtualization | 给应用受管抽象 vs 给 Guest OS 一台虚拟机器 |

## Owner 路由

- trap / syscall / interrupt、process/thread、PCB/TCB、调度、状态迁移 → OS-01/02；
- 同步互斥、PV、管程、死锁 → OS-03；
- VA/PA、页表、缺页、COW、页面置换 → OS-04；
- driver、DMA、request/completion、buffering、设备调度 → OS-05；
- pathname、inode、fd/OFD、文件索引、journaling → OS-06/07；
- CPU privilege、MMU、IRQ 控制器等软硬件接口 → 对应跨科 Bridge。

## 最短压缩

OS-00 训练只做两件事：**先问“这是什么层的对象”，再问“这个局部机制真正属于谁”。** 一旦 Owner 已经确定，就停止在基础册继续展开。
