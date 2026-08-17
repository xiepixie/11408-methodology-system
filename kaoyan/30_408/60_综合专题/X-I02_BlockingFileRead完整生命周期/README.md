# X-I02｜一次 Blocking File `read()` 的完整生命周期

状态：目录已建立，正文未建。

## Canonical Problem
用户进程对文件发起 blocking `read()`，需要真实设备 I/O 时，从用户态到设备再回到用户态，哪些 Subject/Bridge 依次接力？

## Composition
`User Process -> System Call -> File Objects -> Page Cache/I-O Request -> Block -> Controller/DMA -> Interrupt -> Kernel Completion -> Wakeup -> Schedule -> Return`

## Uses
OS-I01、OS-B01、OS-B03、OS-B04、CO08、X-B01、X-B03。

## Owns
跨 OS × CO 的完整 read 生命周期与 handoff 顺序，不重新定义 file、DMA、interrupt、scheduler 或 wakeup 的局部机制。

## Verification
分别追踪：data location、task state、request state、device state、control owner；任一时刻都要能回答“谁持有数据、谁在等待、谁能推动下一次状态变化”。
