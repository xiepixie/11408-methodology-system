# 408 跨学科 Integration

状态：目录已建立，正文未建。

本目录只拥有跨学科的完整协作轨迹，不拥有任何局部机制。

## 学科内部 Integration

- 数据结构：《从问题需求到数据结构选择》；
- 计组：《一条指令的一生》；
- OS：《一次内核跨子系统过程》；
- 网络：《一个网络请求的一生》。

这些内容留在各自学科目录。

## 全局规划母题

### 程序读取网络数据的一生

```text
Remote Application
-> Network Protocols
-> NIC / DMA
-> Interrupt or Poll
-> Kernel Network Stack
-> Socket Buffer
-> Wake Process
-> CPU executes copy/return path
-> User Program observes bytes
```

需要同时追踪：

- 网络：packet、scope、protocol state 和 feedback；
- 计组：DMA、interrupt、Cache/TLB/Memory 和 instruction timing；
- OS：request、buffer、task state、wait/wakeup 和 scheduling；
- 数据结构：queue、buffer、lookup table 等提供的操作能力。

## 完成条件

全局 Integration 只有在相关 Topic 和 Bridge 已有稳定 Owner 后才开始正文。否则所谓“综合”只会复制未稳定的局部知识。
