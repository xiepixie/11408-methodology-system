# 主存与存储硬件：地址怎样落到物理介质

状态：Canonical LaTeX 已完成本轮结构、术语与题库攻击重审；Published PDF 已同步本轮正文。

## Hook

主存不是抽象数组，而是用有限引脚、阵列端口和有物理代价的介质兑现地址访问。本册按“地址/粒度 → 芯片/Bank/行列定位 → 物理操作/事务 → Latency/Cycle/Throughput/Bandwidth”组织，分别回答地址落到哪里、一次怎样服务、下一请求何时可来以及稳态能服务多快。

## Scope / Stop Boundary

本册 Owns 编址单位、存储字/总线粒度、SRAM/DRAM/Flash/HDD 组织、行列译码、芯片扩展、交叉编址、访问时序和介质成本。

Cache line/tag/replacement 归 CO-06；VA/TLB 归 CO-07；总线事务细节归 CO-08；磁盘调度、文件映射和 OS Page Cache 归 OS。

## Owns / Uses

- Uses CO-03 存储接口和 CO-08 传输控制；
- 向 CO-06/07 输出存储访问粒度、延迟和带宽接口；
- LBA 只作为主机线性抽象，不推出真实物理连续。

## 训练导航

- [主存组织与访问成本](主存组织与访问成本.md)：训练芯片扩展、DRAM 行列/刷新、交叉编址、连续对象跨体、突发事务、Latency/Access Time/Cycle/Throughput/Bandwidth、磁盘与 RAID；稳定机制仍回本册 Canonical。
- [Flash 与 SSD 介质特性](Flash与SSD介质特性.md)：训练非易失性、NAND page/erase-block 粒度、读写不对称、垃圾回收/磨损均衡与“SSD 很快但通常不是主存”的层次边界。
- [存储系统真题训练总索引](../90_做题规则/存储系统真题训练总索引.md)：按 2009—2026 真题把 CO-05 与 Cache/TLB/OS VM 的训练接口接起来。

## Read Next

- [CO-06 Cache 与存储层次](../60_Cache与存储层次/README.md)
- [CO-08 总线与 I/O 硬件](../80_总线与IO硬件/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-05_主存与存储硬件_方法论手册.tex)
- [Published PDF](../../../90_publish/408/CO-05_主存与存储硬件_方法论手册.pdf)

## 当前状态

正文已改为单一因果路径，不再用“前半册概述 + 后半册补充细节”重复解释同一机制；容量/地址、介质状态、芯片扩展、Bank/交叉、时间与速率、HDD/SSD 边界均已统一术语。Cache、页表、文件系统与 OS 策略继续保持 Owner 边界。
