# OS-00 操作系统基础与程序运行环境

状态：Canonical LaTeX 已建立并有 Published PDF；外部操作系统概述笔记 9 篇已完成语义核销，其中 8 篇增量写入本册，interrupt/exception 由 OS-01/02 机制正文与 X-B01 接口覆盖。

- [Canonical LaTeX](OS-00_操作系统基础与程序运行环境_方法论手册.tex)
- [Published PDF](../../../90_publish/408/OS-00_操作系统基础与程序运行环境_方法论手册.pdf)
- [基础概念与 Owner 定位](基础概念与Owner定位.md)：承接旧 Canonical 的七问控制器与概念路由；只训练定位和转交，不复制 OS-00 机制正文。

## Position

本文件是 **OS Subject Atlas-owned Foundation Supplement**，不是与五个机制 Topic 平级的独立 Topic 类型。它回答：

> 为什么程序不能直接把裸硬件当作自己的机器？操作系统怎样把有限、共享、异步且会失败的物理资源，组织成程序可使用的受保护运行环境？

本 Foundation Supplement 不重新拥有后续 Topic 的内部机制，而是把所有 OS Topic 共同使用的入口模型、基础术语和程序运行环境集中在 Atlas 责任范围内。未来若内容进一步压缩，可并入 OS Subject Atlas；物理拆文件不改变 Ownership。

## Mother Model

$$
\boxed{
\text{Finite Physical Resources}
\xrightarrow[\text{Protection + Policy}]{\text{Abstraction + Virtualization}}
\text{Program-visible Managed Environment}
}
$$

OSTEP 的三条主线作为基础观察镜头：

$$
\boxed{\text{Virtualization} + \text{Concurrency} + \text{Persistence}}
$$

其中 Protection / Isolation、Abstraction、Performance 与 Reliability 是贯穿三条主线的横向约束，而不是第四个并列专题。

## Owns

- OS 为什么存在：abstraction、virtualization、resource management、protection/isolation 的基础关系；
- OSTEP `Virtualization / Concurrency / Persistence` 与 408 基础概念的映射；
- 操作系统四个基本特征：并发、共享、虚拟、异步，以及它们的因果关系和边界；
- 时分/空分复用的教材分析轴，以及异步对结果可再现性提出的正确性底线；
- OS 基本功能/服务与后续 Topic 的导航；
- 操作系统发展逻辑：人工操作 / 单道批处理 / 多道批处理 / 分时 / 实时；
- 程序从静态文件到运行映像的入口语义：编译后目标文件、链接、可执行文件、装入、进程映像；
- `Program ≠ Executable ≠ Process Image ≠ Process`；
- 静态链接、装入时动态链接、运行时动态链接的基础语义；
- OS 结构的比较轴：分层、宏内核/模块化、微内核、外核；
- 微内核的边界成本、外核与微内核的正交关系，以及 Exokernel / LibOS 的能力与代价；
- 系统引导的概念链：Firmware → Boot Manager/Bootloader → Kernel → User Space；
- Legacy BIOS/MBR/PBR 与 UEFI 的两类查找协议；
- 机器级虚拟化：CPU、memory、I/O 三条虚拟化路径，VMM/Hypervisor 与 OS 资源虚拟化的区别。

## Stop Boundary

- trap / syscall / interrupt、进程状态、调度、PCB/TCB → OS-01/02；
- 同步互斥、PV、管程、死锁 → OS-03；
- 重定位后的 VA→PA 翻译、页表、缺页、换页、COW/mmap → OS-04；
- 驱动、DMA、I/O request、buffering、设备调度 → OS-05；
- pathname、fd/OFD、inode、文件分配、journaling → OS-06/07；
- CPU 特权级、MMU、IRQ 控制器的软硬件接口 → CPU × OS Bridge。

程序链接与装入在本册只追到“静态文件怎样形成运行映像”。一旦题目开始追问地址翻译、驻留、页框和缺页，立即切到 OS-04。

## Source Backbone

- Remzi H. Arpaci-Dusseau, Andrea C. Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*：Introduction、Virtual Machine Monitors；
- System V ELF gABI：Program Loading and Dynamic Linking；
- GNU Binutils `ld` Documentation：linker 的对象合并、symbol resolution 与 relocation；
- UEFI Specification：Boot Manager；
- Linux Kernel Documentation：Linux/x86 Boot Protocol；
- seL4 Documentation：microkernel 的 minimal privileged core 与 user-space services；
- MIT Exokernel papers：separate protection from management。
