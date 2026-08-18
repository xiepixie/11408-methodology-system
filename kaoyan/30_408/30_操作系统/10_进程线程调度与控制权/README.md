# 进程、线程、调度与控制权

状态：待人工确认；已发布。历史长笔记与主题卡的 Source Diff 已完成；2026-08-15 外部笔记全量审计中的进程/线程/调度/IPC 18 篇也已逐篇核销，Canonical LaTeX 已增量发布为 50 页。

> 一个静态程序怎样成为可命名、受保护、可等待、可回收的进程实例？其中的执行流又怎样获得有限 CPU 的执行机会，并在阻塞、唤醒与调度中安全转移控制权？

## Scope

本册围绕 task、context 与 queue 追踪程序、进程、线程、PCB/TCB、生命周期、调度、上下文切换、系统调用/中断入口，以及 IPC 的进程侧语义。

## Owns / Uses / Stop Boundary

- **Owns**：task identity、执行上下文、run/wait queue、状态迁移、调度策略、block/wakeup、IPC 分类与进程侧状态。
- **Uses**：OS-00 的运行环境入口；OS-03 的同步协议；OS-04 的 address-space 机制；OS-05 的 I/O 完成；OS-06/07 的文件引用。
- **Stop Boundary**：不重讲 PV/管程、页表与 COW、fd/OFD/inode、DMA 搬运或运输层 socket 语义。

## 训练导航

- [进程线程状态与控制权](进程线程状态与控制权.md)：承接旧 Canonical 的线程九问、进程状态、系统调用/中断、PCB/TCB 与 IPC 控制清单；只训练状态推演与 Owner 路由。
- [调度计算](调度计算.md)：训练决策事件点、ready set、Gantt 时间线、HRRN/RR/MLFQ 与指标反推；调度机制与策略定义仍由 Canonical 拥有。

## Read Next

同步与共享状态进入[并发、同步与死锁](../20_并发同步与死锁/README.md)；阻塞 I/O 的设备侧进入[I/O 请求、等待与完成](../40_IO请求等待与完成/README.md)。

## Manual

- [Canonical LaTeX](OS-01_OS-02_进程线程调度与控制权_方法论手册.tex)
- [Published PDF](../../../90_publish/408/OS-01_OS-02_进程线程调度与控制权_方法论手册.pdf)
