# 408 跨学科 Bridge

状态：框架已采用，具体 Bridge 正文待建，旧发布物待纳管。

本目录只放跨越两个或更多学科 Owner 的接口。单一学科内部的 Bridge 留在对应学科目录。

## 规划 Bridge

| Bridge                   | 两侧 Owner                           | 只负责什么                                                  | 当前状态              |
| --------------- | --------------- | -------------------- | ---------- |
| C x ISA x CPU            | 程序语义 / 计组 ISA 与 CPU Topic          | C 结构怎样形成指令、寄存器、地址计算和控制流                                | 规划，优先留在计组科内       |
| Cache x VM x OS          | 计组地址翻译与 Cache / OS VM              | VA、TLB、PTE、PA、Cache、Page Fault 的交接与重试                  | 规划                |
| Interrupt / DMA x OS     | 计组 I/O 硬件 / OS I/O 与 Process       | request、DMA transfer、interrupt、completion、wakeup 的责任边界 | 既有旧发布物待拆清         |
| OS x Network             | OS Process/I/O / Network Transport | socket、kernel stack、NIC、buffer、wakeup 怎样连接进程与 packet   | 规划，Engineering 扩展 |
| Data Structure x Systems | 数据结构 Topic / 计组、OS、网络 Topic        | Heap、Queue、Tree、Hash 等怎样为系统机制提供操作能力                    | 规划，按真实依赖建设        |

## 边界原则

Bridge 必须列出：

1. 两侧 Canonical Owner；
2. 交接的对象、状态、数据或控制权；
3. 输入与输出；
4. 接口不变量；
5. fast/slow/error path 的分界；
6. 哪些内容只引用、不重新定义。

## 既有材料

`OS_计组桥梁专题_CPU与内核软硬件协作边界_v1` 当前覆盖范围较宽。正式纳管时，应判断它是保留为总 Bridge Atlas，还是拆成 `Cache x VM x OS` 与 `Interrupt / DMA x OS` 两条具体接口；在此之前不复制其正文。
