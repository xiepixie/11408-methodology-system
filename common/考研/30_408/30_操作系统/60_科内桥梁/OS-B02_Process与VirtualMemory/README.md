# OS-B02｜Process × Virtual Memory

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS01 Process/Control ↔ OS04 Virtual Memory。

## Mother Interface
`Process Identity -> Address Space Association -> fork/share relation -> COW divergence -> Process-visible memory state`

## Owns
process 与 address space 怎样关联，fork 后哪些映射共享、什么时候因写入发生 COW 分化。

## Boundary
页表、缺页、frame/replacement 由 VM Topic Own；process 生命周期与调度由 OS01 Own。CPU 硬件翻译进入 X-B02。

## Manual
- [Canonical 正文](OS-B02_Process与VirtualMemory_桥梁手册.tex)
- [Published PDF](../../../../90_publish/OS-B02_Process与VirtualMemory_桥梁手册.pdf)

## Review v1
已核对 fork 共享、写时复制、fault/retry 与 context switch 的分层；下一轮用 fork/read/write 组合题验证共享对象与分化时机。
