# OS Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 按当前 Owner 边界逐册重构。

- [OS-B01｜Wait / Block / Wakeup](OS-B01_WaitBlockWakeup/README.md)
- [OS-B02｜Process × Virtual Memory](OS-B02_Process与VirtualMemory/README.md)
- [OS-B03｜Process × File Reference](OS-B03_Process与FileReference/README.md)
- [OS-B04｜VM × File × I/O](OS-B04_VMFileIO/README.md)

这些 Bridge 只拥有 OS Topic 之间的 handoff，不拥有 CPU privilege、MMU、DMA 等跨科硬件接口；后者统一上移到 `30_408/50_桥梁专题/`。

旧 `OS_科内桥梁与跨科接口_方法论手册.tex` 不再是 Owner；其中 Priority Inversion、MMIO、Process × File 与 VM × File 等内容仍需逐项核对当前 Topic / Bridge 的承接情况，因此旧 `.tex` / PDF 暂时保留为 Source。

## Review v1

OS-B01--B04 已完成首轮升级并发布；统一审阅重点是 task state、address-space association、reference lifetime 和 file/page/I/O handoff。下一轮以同步、fork/COW、fd 引用和 mmap 回写题验证。
