# OS Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 按当前 Owner 边界逐册重构。

- [OS-B01｜Wait / Block / Wakeup](OS-B01_WaitBlockWakeup/README.md)
- [OS-B02｜Process × Virtual Memory](OS-B02_Process与VirtualMemory/README.md)
- [OS-B03｜Process × File Reference](OS-B03_Process与FileReference/README.md)
- [OS-B04｜VM × File × I/O](OS-B04_VMFileIO/README.md)

这些 Bridge 只拥有 OS Topic 之间的 handoff，不拥有 CPU privilege、MMU、DMA 等跨科硬件接口；后者统一上移到 `30_408/50_桥梁专题/`。

旧 `OS_科内桥梁与跨科接口_方法论手册.tex` 不再是 Owner，逐项路由已经完成：Priority Inversion / inheritance / ceiling → OS-03（OS-01/02 只保留调度接口）；MMIO / Port I/O → CO-08 与跨科 X-B01/X-B03，OS-05 只 Use 设备寄存器接口；Process × File → OS-B03；VM × File/Page Cache → OS-B04。旧 `.tex` / PDF 仅因 Source 保留策略暂存，不能作为第二份定义来源。

## Review v1

OS-B01--B04 已完成第二轮语义收敛：把 Linux 结构体/固定字段从“定义”降为工程实例，稳定接口统一为 wait relation、address-space association/COW divergence、fd binding→OFD→file object、file range↔resident page↔I/O completion。下一轮以同步、fork/COW、fd 引用和 mmap 回写题验证这些接口是否能无提示复原。
