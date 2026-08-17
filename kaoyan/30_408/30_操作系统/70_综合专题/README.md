# OS Integration Layer

> 类型：Atlas
> 状态：已采用；README 是 Canonical Integration Map。OS-I01 / OS-I02 的深度正文与 Published PDF 分别由各自子目录拥有，仍待人工确认与陌生题验证。

当前只保留两个具有稳定 Composition 价值的 Canonical Process：

- [OS-I01｜一次 Blocking `read()`](OS-I01_BlockingRead/README.md)
- [OS-I02｜`fork()` + COW + Resource Reference](OS-I02_ForkCOW与资源引用/README.md)

`mmap()` + file-backed page、lock contention 等继续作为 Topic/Bridge 的 worked example；只有删掉具体题面后仍存在新的、可重复调用的 Composition 责任时，才晋升新的 Integration，避免把综合题数量等同于 Integration 数量。
