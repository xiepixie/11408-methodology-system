# 计算机组成原理 Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas。CO-B01 与 CO-B02 的 Canonical 候选正文均已建立并发布，待真题攻击与人工确认。

- [CO-B01｜ISA Semantic × Datapath](CO-B01_ISA语义与数据通路/README.md)：架构状态差怎样成为数据依赖、通路与控制输入；
- [CO-B02｜Address Translation × Cache Access](CO-B02_地址翻译与Cache访问/README.md)：翻译结果怎样成为 Cache 地址身份与访问属性输入。

Bridge 只解释计组 Topic 之间的 handoff。OS 参与的 privilege/fault/DMA 接口统一上移到 `30_408/50_桥梁专题/`。

## Review v1

CO-B01--B02 已完成首轮审阅；保留 ISA/数据通路的状态差包与翻译契约，以及 VA/PA/权限到 Cache 的分流。下一轮用 store、异常、位预算和 TLB/Cache 并行性题验证。
