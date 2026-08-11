# OS Integration Layer

状态：框架已采用，正文待重构。

当前只建立两个核心 Canonical Process：

- [OS-I01｜一次 Blocking `read()`](OS-I01_BlockingRead/README.md)
- [OS-I02｜`fork()` + COW + Resource Reference](OS-I02_ForkCOW与资源引用/README.md)

`mmap()` + file-backed page、lock contention 等先作为 Topic/Bridge 的 worked example；只有出现独立 Composition 价值时再晋升新的 Integration。
