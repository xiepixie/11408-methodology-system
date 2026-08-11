# 操作系统学科总图

状态：目录已建立，正文未建。

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

## Owns

- Resource、Abstraction、Virtualization、Protection 与 Control 的学科母问题；
- Object / Relation / Queue / Event / Mechanism / Policy / Invariant / Cost 统一语言；
- OS-00、五个机制 Topic、科内 Bridge 和 Integration 的导航关系。

其中 OS-00 是基础 Canonical Owner：负责把裸硬件、程序运行环境、OS 结构/引导/VMM 与后续机制 Topic 接起来；Atlas 只压缩其母模型，不在这里复制正文。

## 必须保持的区分

- mechanism 不等于 policy；
- task state 不等于 CPU privilege state；
- address translation 不等于 page residency；
- file name 不等于 file object，不等于 open instance；
- I/O completion 不等于 process 已经重新运行。

## Stop Boundary

不完整定义调度算法、PV、页表、换页、DMA、OFD 或 journaling；也不完整推演 `read()`。
