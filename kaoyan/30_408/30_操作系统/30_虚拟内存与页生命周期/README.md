# 虚拟内存与页生命周期

状态：Canonical LaTeX 已完成本轮术语与版面重审；15 份外部内存管理笔记已完成语义核销。现有 Published PDF 仍是上一版派生稿，待发布流程同步。

> 每个进程怎样获得受保护、可扩展、按需兑现的地址空间？

## Scope

本册用 `Region -> Mapping -> Residency -> Translation -> Fault -> Reclaim` 追踪虚拟页的一生，并区分地址意义、页表状态、物理驻留和置换策略。

## Owns / Uses / Stop Boundary

- **Owns**：OS mapping、page fault、frame allocation、replacement、working set/PFF、COW、mmap 的 VM 侧与物理页分配边界。
- **Uses**：计组的硬件地址翻译；文件系统的 file object/block mapping；I/O 的 page-in/writeback request。
- **Stop Boundary**：不重新拥有 TLB/MMU 硬件路径、pathname/fd/OFD 或设备 DMA 完成机制。

## 训练导航

- [地址翻译与缺页](地址翻译与缺页.md)：训练 VA/VPN/offset、多级页表、TLB/PTE、Page Fault 原因分类、COW 与跨计组翻译链；408 经典“缺页”保持为页面当前不驻留这一分支，不再把 TLB miss、Cache miss 或所有 Page Fault 混称“缺页”。
- [页面驻留与置换](页面驻留与置换.md)：训练 resident set、FIFO/LRU/CLOCK、dirty/writeback、local/global、Belady、working set/PFF 与 thrashing；承接旧训练阶梯。

## Read Next

file-backed page 的跨册接口见 [VM × File × I/O](../60_科内桥梁/OS-B04_VMFileIO/README.md)。

## Manual

- [Canonical LaTeX](OS-04_虚拟内存与地址翻译_方法论手册.tex)
- [Published PDF](../../../90_publish/408/OS-04_虚拟内存与地址翻译_方法论手册.pdf)
