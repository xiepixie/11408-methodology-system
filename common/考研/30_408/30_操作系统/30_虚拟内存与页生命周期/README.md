# 虚拟内存与页生命周期

状态：待人工确认；已发布。历史内存/页框笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管。

> 每个进程怎样获得受保护、可扩展、按需兑现的地址空间？

## Scope

本册用 `Region -> Mapping -> Residency -> Translation -> Fault -> Reclaim` 追踪虚拟页的一生，并区分地址意义、页表状态、物理驻留和置换策略。

## Owns / Uses / Stop Boundary

- **Owns**：OS mapping、page fault、frame allocation、replacement、working set/PFF、COW、mmap 的 VM 侧与物理页分配边界。
- **Uses**：计组的硬件地址翻译；文件系统的 file object/block mapping；I/O 的 page-in/writeback request。
- **Stop Boundary**：不重新拥有 TLB/MMU 硬件路径、pathname/fd/OFD 或设备 DMA 完成机制。

## Read Next

file-backed page 的跨册接口见 [VM × File × I/O](../60_科内桥梁/OS-B04_VMFileIO/README.md)。

## Manual

- [Canonical LaTeX](OS-04_虚拟内存与地址翻译_方法论手册.tex)
- [Published PDF](../../../90_publish/OS-04_虚拟内存与地址翻译_方法论手册.pdf)
