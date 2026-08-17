# X-B03｜Interrupt / DMA × OS I/O

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
CO08 总线与 I/O 硬件 ↔ OS04 I/O，并连接 OS01 Process/Control。

## Mother Interface
`OS Submit -> Controller/DMA Transfer -> Device Completion -> Interrupt Delivery -> Kernel Completion -> Wakeup`

## Owns
硬件异步完成怎样被 OS 观察并转换成 request completion 与 task state 变化。

## Responsibility Split
- 计组：controller register、bus transaction、DMA transfer、interrupt delivery/arbitration；
- OS：driver/request、submit/wait、completion、buffering、wakeup。

## Boundary
Wait/Block/Wakeup 的 OS 科内统一接口由 OS-B01 Own；本 Bridge 只拥有软硬件完成 handoff。

## Manual
- [Canonical 正文](X-B03_InterruptDMA与OSIO_桥梁手册.tex)
- [Published PDF](../../../90_publish/408/X-B03_InterruptDMA与OSIO_桥梁手册.pdf)

## Review v1
已核对 buffer ownership、DMA address、completion evidence、interrupt/polling 分支和 wake 边界；下一轮用阻塞 read 与异步设备完成题验证。
