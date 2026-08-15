# 并发、同步与死锁

状态：待人工确认；已发布。历史 PV/死锁笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管。

> 不可预测交错下怎样保持共享状态正确，并让系统持续推进？

## Scope

本册从 execution trace 与 shared-state invariant 出发，生成 atomicity、mutex、semaphore、condition variable、monitor、经典 PV 模式与 deadlock 控制。

## Owns / Uses / Stop Boundary

- **Owns**：互斥与同步边界、P/V 许可模型、条件变量谓词模型、并发模式、等待依赖、安全性与死锁处理。
- **Uses**：进程 Topic 的 task/block/wakeup；I/O Topic 的 Spooling 作为破坏独占条件的例子。
- **Stop Boundary**：不拥有 scheduler 的运行队列策略，不把设备/文件/页面的局部机制复制进并发正文。

## Read Next

若题目重点转为 task 何时重新获得 CPU，回到[进程、线程、调度与控制权](../10_进程线程调度与控制权/README.md)。

## Manual

- [Canonical LaTeX](OS-03_并发锁与PV_方法论手册.tex)
- [Published PDF](../../../90_publish/OS-03_并发锁与PV_方法论手册.pdf)
