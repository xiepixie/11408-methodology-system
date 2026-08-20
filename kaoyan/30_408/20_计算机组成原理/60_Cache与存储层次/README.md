# Cache 与存储层次：怎样维护一个正确的高速副本

状态：Canonical LaTeX 已完成本轮结构、术语与图示重审；现有 Published PDF 仍是上一版派生稿，待发布流程同步。

## Hook

Cache 不是“小型主存”，而是需要证明副本身份并维护状态的有限高速层。本册按“Locality → Block Transfer → Placement → Identity/State → Hit/Miss → Replacement/Write → Hierarchy Cost”组织：先保证取对数据，再由真实状态轨迹生成命中率与 AMAT。地址翻译层次和虚存 fault 路径只通过接口组合，不并入同一个 Cache 状态机。

## Scope / Stop Boundary

本册 Owns block/line、tag/index/offset、映射、hit/miss、3C、替换、write-through/write-back、write-allocate/no-write-allocate、容量位数，以及存储层次性能语言：hit time、miss penalty、miss total time、local/global miss rate 与 AMAT。翻译 EAT 和 Page-Fault EAT 只在接口处定义区别，机制仍分别归 CO-07 与 OS-04。

不拥有主存阵列/介质组织、TLB/page walk、OS Page Cache 或文件系统缓存。

## Owns / Uses

- Uses CO-05 的存储粒度、带宽和下一级延迟；
- Uses CO-07 的 VA/PA 翻译接口；
- Uses CO-04 的 miss stall/重叠边界；
- 向 CO-B02、CO-I01 输出 hit/miss 与重试条件。

## 训练导航

- [存储层次与 AMAT](存储层次与AMAT.md)：先定义不同存储/翻译层次分别缓存什么，再统一 hit/miss、hit time、miss penalty、miss total time、local/global miss rate、AMAT/EAT 与多级期望模型。
- [Cache 访问流与命中率](Cache访问流与命中率.md)：训练程序 → reference stream → address/block/set stream → Cache state → hit/miss count → cost；包含 stride、alignment/footprint、完整 miss 与写策略。性能计算默认先调用《存储层次与 AMAT》的时间口径。
- [存储系统真题训练总索引](../90_做题规则/存储系统真题训练总索引.md)：按 2009—2026 真题路由到 CO-05/06/07、CO-B02 与 OS VM。

## Read Next

- [CO-05 主存与存储硬件](../50_主存与存储硬件/README.md)
- [CO-07 地址翻译与虚拟存储硬件](../70_地址翻译与虚拟存储硬件/README.md)
- [计组做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](CO-06_Cache与存储层次_方法论手册.tex)
- [Published PDF](../../../90_publish/408/CO-06_Cache与存储层次_方法论手册.pdf)

## 当前状态

正文已合并为单一因果路径，去掉原来的重复“补充细节”层；地址字段/line 状态、三种映射、完整 miss 生命周期、写策略、3C、替换、AMAT、多级 local/global miss rate 与翻译接口已按 Owner 重新排序。固定命中周期、精确替换位数和“所有 miss 阻塞整机”等仍保持题设边界。
