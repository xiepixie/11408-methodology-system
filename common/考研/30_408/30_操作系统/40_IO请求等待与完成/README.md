# I/O 请求、等待与完成

状态：待人工确认；已发布。历史磁盘/I-O 笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管。

> 进程怎样向异步设备提交请求、等待，并在完成后安全继续？

## Scope

本册以 `submit -> wait/return -> device progress -> completion -> wake/notify` 为生命周期，分开控制路径、数据路径与 task 状态路径。

## Owns / Uses / Stop Boundary

- **Owns**：OS request、driver 侧、submit/wait/complete、设备独立层、buffering、device allocation/queue、HDD cost 与调度。
- **Uses**：进程 Topic 的 block/wakeup；VM 的页驻留；文件系统的 block mapping；计组的 interrupt/DMA hardware。
- **Stop Boundary**：DMA 总线与中断控制器硬件属于计组；pathname、inode、OFD 和 journaling 属于文件系统。

## Read Next

完整 blocking `read()` 进入 [OS-I01](../70_综合专题/OS-I01_BlockingRead/README.md)；DMA 的软硬件交接进入 Cross-Subject X-B03。

## Manual

- [Canonical LaTeX](OS-05_IO系统_方法论手册.tex)
- [Published PDF](../../../90_publish/OS-05_IO系统_方法论手册.pdf)
