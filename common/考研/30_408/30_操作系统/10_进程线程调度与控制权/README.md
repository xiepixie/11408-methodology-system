# 进程、线程、调度与控制权

状态：待人工确认；已发布。历史长笔记、主题卡与 `codebrick_os_blog` 标准 408 Coverage Source Diff 已完成，Canonical LaTeX 候选正文已纳管。

> 一个静态程序怎样成为可命名、受保护、可等待、可回收的进程实例？其中的执行流又怎样获得有限 CPU 的执行机会，并在阻塞、唤醒与调度中安全转移控制权？

## Scope

本册围绕 task、context 与 queue 追踪程序、进程、线程、PCB/TCB、生命周期、调度、上下文切换、系统调用/中断入口，以及 IPC 的进程侧语义。

## Owns / Uses / Stop Boundary

- **Owns**：task identity、执行上下文、run/wait queue、状态迁移、调度策略、block/wakeup、IPC 分类与进程侧状态。
- **Uses**：OS-00 的运行环境入口；OS-03 的同步协议；OS-04 的 address-space 机制；OS-05 的 I/O 完成；OS-06/07 的文件引用。
- **Stop Boundary**：不重讲 PV/管程、页表与 COW、fd/OFD/inode、DMA 搬运或运输层 socket 语义。

## Read Next

同步与共享状态进入[并发、同步与死锁](../20_并发同步与死锁/README.md)；阻塞 I/O 的设备侧进入[I/O 请求、等待与完成](../40_IO请求等待与完成/README.md)。

## Manual

- [Canonical LaTeX](OS-01_OS-02_进程线程调度与控制权_方法论手册.tex)
- [Published PDF](../../../90_publish/OS-01_OS-02_进程线程调度与控制权_方法论手册.pdf)
