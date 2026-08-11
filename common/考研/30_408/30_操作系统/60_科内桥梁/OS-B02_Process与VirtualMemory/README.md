# OS-B02｜Process × Virtual Memory

状态：目录已建立，正文未建。

## Owners
OS01 Process/Control ↔ OS03 Virtual Memory。

## Mother Interface
`Process Identity -> Address Space Association -> fork/share relation -> COW divergence -> Process-visible memory state`

## Owns
process 与 address space 怎样关联，fork 后哪些映射共享、什么时候因写入发生 COW 分化。

## Boundary
页表、缺页、frame/replacement 由 VM Topic Own；process 生命周期与调度由 OS01 Own。CPU 硬件翻译进入 X-B02。
