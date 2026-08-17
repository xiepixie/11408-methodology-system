# 操作系统学科总图

> 类型：Atlas
> 状态：Derived Deep Map Supplement；不是第二个 Canonical Atlas Owner。当前地图已与 `../README.md` 的 Subject Atlas 拓扑同步。

规划标题：《操作系统统一总图：资源、抽象、状态与控制权》。

## Position

本文件是 [Operating System Subject Atlas](../README.md) 的 **Atlas Deep Map Supplement**，不是第二个独立 Atlas Owner。`../README.md` 拥有正式 Foundation / Topic / Bridge / Integration 导航；本文件保留更展开的 OS 对象、状态与控制权总图，不重写局部机制。

## Mother Model

$$
\text{Resource}
\xrightarrow{Abstraction/Virtualization/Protection}
\text{Managed Object}
$$

$$
(Objects,Relations,Queues)
\xrightarrow{Event+Mechanism+Policy}
(Objects',Relations',Queues')
$$

## Mirrors / Expands

本页只把 Subject Atlas 已采用的关系展开成便于浏览的深层地图，不新增可独立修改的知识 Owner：

- Resource、Abstraction、Virtualization、Protection 与 Control 的学科母问题仍由 `../README.md` 的 Subject Atlas Own；
- Object / Relation / Queue / Event / Mechanism / Policy / Invariant / Cost 统一语言仍由 Subject Atlas 定义；
- OS-00、五个机制 Topic、科内 Bridge 和 Integration 的正式导航仍以 `../README.md` 为准。

其中 OS-00 是 Foundation 的 Canonical 深度 Owner：负责把裸硬件、程序运行环境、OS 结构/引导/VMM 与后续机制 Topic 接起来；本页只压缩其位置，不复制正文。

## 必须保持的区分

- mechanism 不等于 policy；
- task state 不等于 CPU privilege state；
- address translation 不等于 page residency；
- file name 不等于 file object，不等于 open instance；
- I/O completion 不等于 process 已经重新运行。

## Stop Boundary

不完整定义调度算法、PV、页表、换页、DMA、OFD 或 journaling；也不完整推演 `read()`。
