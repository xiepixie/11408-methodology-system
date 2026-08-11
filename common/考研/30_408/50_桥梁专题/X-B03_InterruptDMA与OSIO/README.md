# X-B03｜Interrupt / DMA × OS I/O

状态：目录已建立，正文未建。

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
