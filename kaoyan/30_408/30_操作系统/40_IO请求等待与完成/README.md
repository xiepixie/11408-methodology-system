# I/O 请求、等待与完成

状态：已发布；11 份 外部 I/O 笔记已完成语义核销，Canonical LaTeX 已按请求、等待、搬运、完成与设备成本链条增量扩充。

> 进程怎样向异步设备提交请求、等待，并在完成后安全继续？

## Scope

本册以 `submit -> wait/return -> device progress -> completion -> wake/notify` 为生命周期，分开控制路径、数据路径与 task 状态路径。

## Owns / Uses / Stop Boundary

- **Owns**：OS request、driver 侧、submit/wait/complete、设备独立层、buffering、device allocation/queue、HDD cost 与调度。
- **Uses**：进程 Topic 的 block/wakeup；VM 的页驻留；文件系统的 block mapping；计组的 interrupt/DMA hardware。
- **Stop Boundary**：DMA 总线与中断控制器硬件属于计组；pathname、inode、OFD 和 journaling 属于文件系统。

## 训练导航

- [I/O 请求与完成](IO请求与完成.md)：把程序查询、中断、DMA、缓冲、SPOOLing、磁盘调度与阻塞 I/O 统一放进控制线、数据线和任务状态线；承接旧 Canonical 的十三问检查表与题型路由。

## Read Next

完整 blocking `read()` 进入 [OS-I01](../70_综合专题/OS-I01_BlockingRead/README.md)；DMA 的软硬件交接进入 Cross-Subject X-B03。

## Manual

- [Canonical LaTeX](OS-05_IO系统_方法论手册.tex)
- [Published PDF](../../../90_publish/408/OS-05_IO系统_方法论手册.pdf)
