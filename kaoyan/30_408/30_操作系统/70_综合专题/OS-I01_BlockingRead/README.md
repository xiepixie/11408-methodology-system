# OS-I01｜一次 Blocking `read()`

状态：LaTeX 工作稿待人工确认；Canonical Integration 正文已建立并发布。

## Canonical Problem
进程对文件发起 blocking `read()`，数据不在可立即返回的位置时，OS 内部各机制怎样协作直到系统调用返回？

## Composition
`Task -> syscall -> fd/OFD/inode -> Page Cache -> I/O request -> block -> completion -> wake -> runnable -> return`

## Uses
OS-01/02、OS-05、OS-06/07、OS-B01、OS-B03、OS-B04；若继续追问 interrupt/DMA 的硬件交接，再调用 X-B03。

## Owns
OS 科内完整 read 协作轨迹、快/慢路径分支、失败定位与跨 Owner 验证；涉及 DMA/interrupt 的硬件交接调用 Cross-Subject X-B03，不在本册重讲局部机制。

## Manual
- [Canonical 正文](OS-I01_BlockingRead_综合手册.tex)
- [Published PDF](../../../../90_publish/408/OS-I01_BlockingRead_综合手册.pdf)
