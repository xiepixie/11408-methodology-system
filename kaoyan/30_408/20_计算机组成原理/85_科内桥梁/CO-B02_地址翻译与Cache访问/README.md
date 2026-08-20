# CO-B02｜Address Translation × Cache Access

> 类型：Bridge
> 状态：Canonical Bridge LaTeX 已完成本轮术语与接口重审；现有发布 PDF 仍是上一版派生稿，待发布流程同步。

## Hook

翻译硬件输出 PA、权限与访问属性，Cache 需要合法地址身份以及 tag/index/offset。若接口不明确，就会把 TLB miss、translation fault 与 Cache miss 混成同一种“未命中”，或在 VIPT 题中凭容量口诀猜并行条件。

## Mother Interface

```text
VA Access Request
-> Translation Result Packet
-> Cache Address/Attribute Packet
-> Hit/Miss Path
```

## Owners / Boundary

- Left Owner：[CO-07 地址翻译与虚拟存储硬件](../../70_地址翻译与虚拟存储硬件/README.md)；
- Right Owner：[CO-06 Cache 与存储层次](../../60_Cache与存储层次/README.md)；
- 本 Bridge 只 Own 地址位、权限/属性与串并行时序的交接；
- PTE/page walk 留在 CO-07，mapping/tag/replacement 留在 CO-06，Page Fault 修复留给 OS/X-B02。

## 训练导航

- [地址翻译与 Cache 综合训练](地址翻译与Cache综合训练.md)：训练 Page Offset 不变量、VA/PA 位交接、PIPT/VIPT/VIVT、TLB miss / translation fault / Cache miss 分流、命中组合、fault retry 与跨层 event count；局部机制仍回 CO-06/07。
- [存储系统真题训练总索引](../../90_做题规则/存储系统真题训练总索引.md)：查看 2009—2026 真题证据与六类题型的 Owner 路由。

## 阅读

- [Canonical Bridge 正文](CO-B02_地址翻译与Cache访问_桥梁手册.tex)
- [发布 PDF](../../../../90_publish/408/CO-B02_地址翻译与Cache访问_桥梁手册.pdf)
- [一条指令的一生](../../86_综合专题/CO-I01_一条指令的一生/README.md)

## 当前状态

CO-06/07 两侧 Owner 已存在，接口通过 Bridge Validity 与 Standalone Promotion 两道 Gate。正文仍待人工确认，不代表规则已通过真题验证。

## Review v1
已核对 VA/PA、权限/属性、PIPT/VIPT/VIVT 和 TLB miss/Page Fault/Cache miss 分流；保持 OS 修复归 X-B02。下一轮用页大小、组数、相联度变化题验证位预算。
