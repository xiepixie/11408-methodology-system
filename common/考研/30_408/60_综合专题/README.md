# 408 Cross-Subject Integration Layer

状态：框架已采用；2 个核心 Integration 已建立骨架，综合发布物待按新 Ownership 纳管。

本目录只拥有跨 Subject 的完整协作轨迹，不拥有局部机制。

## X-I01｜一次 LOAD / Memory Access 的完整慢路径

[入口](X-I01_LOAD与MemoryAccess慢路径/README.md)

```text
Instruction
-> Effective Address / VA
-> TLB / Page Table
-> PA
-> Cache
-> Memory

slow path:
Page Fault
-> Kernel Repair
-> PTE Update
-> Retry
-> Commit
```

重点检验：TLB miss、Cache miss、Page Fault 的层级和责任差异。

## X-I02｜一次 Blocking File `read()` 的完整生命周期

[入口](X-I02_BlockingFileRead完整生命周期/README.md)

```text
User Process
-> System Call
-> fd/OFD/inode
-> Page Cache / I-O Request
-> Controller / DMA
-> Interrupt / Completion
-> Wakeup / Schedule
-> Return
```

重点检验：OS 科内 read 轨迹怎样跨 X-B01/X-B03 接上硬件。

## Extension

`NIC -> kernel network stack -> socket -> process` 的完整网络接收路径暂不建立第三个 Core Integration；等 X-B04 的 Core 优先级和相关 Topic 通过真题/Coverage evidence 后再决定。

## Legacy Source

既有 `408四科统一方法论手册.tex`、`OS-I1_OS综合状态机_方法论手册.tex` 等发布物是 Source/legacy publication，不因已发布而拥有新的 Canonical 轨迹。
