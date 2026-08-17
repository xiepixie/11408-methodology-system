# OS-B02｜Process × Virtual Memory

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS-01/02 Process/Control ↔ OS-04 Virtual Memory。

## Mother Interface
`Process Identity -> Address-Space Association -> fork Mapping Relation -> private write -> COW Decision -> Mapping Divergence if needed -> Retry`

## Owns
process 与 address space 怎样关联，fork 后哪些映射共享、什么时候因写入发生 COW 分化。

## Boundary
页表、缺页、frame/replacement 由 OS-04 Own；process 生命周期与调度由 OS-01/02 Own。CPU 硬件翻译进入 X-B02。

## Manual
- [Canonical 正文](OS-B02_Process与VirtualMemory_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/OS-B02_Process与VirtualMemory_桥梁手册.pdf)

## Review v2
已把 `task_struct/mm_struct/CR3/COW bit/4KB` 从定义降为实现实例，并显式拆开 Execution Switch 与 Address-Space Switch。COW 只服务 private divergence semantics，不覆盖显式共享 mapping。下一轮用 fork/write/exec 组合题验证共享对象与分化时机。
