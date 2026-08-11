# OS-I01｜一次 Blocking `read()`

状态：目录已建立，正文未建。

## Canonical Problem
进程对文件发起 blocking `read()`，数据不在可立即返回的位置时，OS 内部各机制怎样协作直到系统调用返回？

## Composition
`Task -> syscall -> fd/OFD/inode -> Page Cache -> I/O request -> block -> completion -> wake -> runnable -> return`

## Uses
OS01、OS04、OS05、OS-B01、OS-B03、OS-B04。

## Owns
OS 科内完整 read 协作轨迹；涉及 DMA/interrupt 的硬件交接调用 Cross-Subject X-B03，不在本册重讲硬件机制。
