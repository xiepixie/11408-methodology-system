# Cache 与存储层次：怎样维护一个正确的高速副本

状态：LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布。

## Hook

Cache 不是“小型主存”，而是带身份、有效性、修改状态和替换策略的副本系统。本册追踪“局部性 → 块搬运 → 放置 → tag/valid → offset → 替换/写状态 → AMAT”。

## Scope / Stop Boundary

本册 Owns block/line、tag/index/offset、映射、hit/miss、3C、替换、write-through/write-back、write-allocate/no-write-allocate、容量位数和 AMAT。

不拥有主存阵列/介质组织、TLB/page walk、OS Page Cache 或文件系统缓存。

## Owns / Uses

- Uses CO-05 的存储粒度、带宽和下一级延迟；
- Uses CO-07 的 VA/PA 翻译接口；
- Uses CO-04 的 miss stall/重叠边界；
- 向 CO-B02、CO-I01 输出 hit/miss 与重试条件。

## Read Next

- [CO-05 主存与存储硬件](../50_主存与存储硬件/README.md)
- [CO-07 地址翻译与虚拟存储硬件](../70_地址翻译与虚拟存储硬件/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-06_Cache与存储层次_方法论手册.tex)
- [Published PDF](../../../90_publish/CO-06_Cache与存储层次_方法论手册.pdf)

## 当前状态

正文已核销《Cache》《存储器层次》Source：地址三分、候选身份、状态机、3C、替换、写策略和 AMAT 进入 Canonical；固定命中周期、精确替换位数和“所有 miss 阻塞整机”等特例保持题设边界。
