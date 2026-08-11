# OS Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 按当前 Owner 边界逐册重构。

- [OS-B01｜Wait / Block / Wakeup](OS-B01_WaitBlockWakeup/README.md)
- [OS-B02｜Process × Virtual Memory](OS-B02_Process与VirtualMemory/README.md)
- [OS-B03｜Process × File Reference](OS-B03_Process与FileReference/README.md)
- [OS-B04｜VM × File × I/O](OS-B04_VMFileIO/README.md)

这些 Bridge 只拥有 OS Topic 之间的 handoff，不拥有 CPU privilege、MMU、DMA 等跨科硬件接口；后者统一上移到 `30_408/50_桥梁专题/`。
