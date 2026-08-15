# 主存与存储硬件：地址怎样落到物理介质

状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## Hook

主存不是抽象数组，而是用有限引脚、阵列端口和有物理代价的介质实现地址访问。本册追踪“地址/粒度 → 模块/芯片 → 行/列 → 感测/编程 → 传输 → 延迟/带宽”。

## Scope / Stop Boundary

本册 Owns 编址单位、存储字/总线粒度、SRAM/DRAM/Flash/HDD 组织、行列译码、芯片扩展、交叉编址、访问时序和介质成本。

Cache line/tag/replacement 归 CO-06；VA/TLB 归 CO-07；总线事务细节归 CO-08；磁盘调度、文件映射和 OS Page Cache 归 OS。

## Owns / Uses

- Uses CO-03 存储接口和 CO-08 传输控制；
- 向 CO-06/07 输出存储访问粒度、延迟和带宽接口；
- LBA 只作为主机线性抽象，不推出真实物理连续。

## Read Next

- [CO-06 Cache 与存储层次](../60_Cache与存储层次/README.md)
- [CO-08 总线与 I/O 硬件](../80_总线与IO硬件/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-05_主存与存储硬件_方法论手册.tex)
- [Published PDF](../../../90_publish/CO-05_主存与存储硬件_方法论手册.pdf)

## 当前状态

正文已核销《主存储器》《存储器层次》《磁盘》Source：阵列/扩展/刷新、存储层次、介质访问成本进入 Canonical；Cache、页表、文件系统与 OS 策略保持边界。
