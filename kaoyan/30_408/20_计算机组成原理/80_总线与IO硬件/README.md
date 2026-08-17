# 总线与 I/O 硬件

> 类型：Topic
> 状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## 引子

同步处理器怎样通过有限共享通道，与速度不同、完成时间不确定的设备可靠合作？

```text
Request
-> Interface State
-> Arbitration
-> Transaction
-> Transfer
-> Completion Signal
```

## Scope

本 Topic 拥有总线角色与事务、仲裁、同步/异步握手、控制器寄存器、I/O 编址、polling、中断硬件入口和 DMA 控制器/传输。

它使用 ISA 的异常/中断契约、主存访问成本与 Cache 接口，但不拥有驱动策略、请求队列、进程阻塞/唤醒、DMA 映射生命周期或设备调度。

## Stop Boundary

- 硬件可以置 pending、判优、交付向量并进入 ISA 规定的入口；保存完整软件上下文、服务设备和唤醒任务归 OS。
- DMA 可以搬运数据并报告完成；buffer policy、mapping/unmapping、completion callback 归 OS 与 X-B03。
- 总线仲裁只决定共享事务发起权，不等于 OS 设备分配。

## 阅读

- [Canonical 深度正文](CO-08_总线与IO硬件_方法论手册.tex)
- [发布 PDF](../../../90_publish/408/CO-08_总线与IO硬件_方法论手册.pdf)
- [计组 Subject Atlas](../README.md)
- [计组做题规则](../90_做题规则/README.md)
- [Interrupt/DMA 与 OS I/O Bridge](../../50_桥梁专题/X-B03_InterruptDMA与OSIO/README.md)

## 来源状态

旧总线、I/O 接口、控制方式、中断与 DMA 笔记只作为 Source；Source Diff 见 `80_evidence/review_log/`。本 README 只负责入口、边界与导航。
