# 408 Course Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Course Atlas，四个 Subject 与下游 Handbook 按当前拓扑继续建设。

> 一道 408 综合题真正困难的地方，往往不是“它属于哪一章”，而是你能不能看清：数据现在是什么结构、程序要求什么语义、硬件怎样执行、OS 在什么时候接管、网络状态又由谁维护。
>
> 这套体系不把四科压成一种语言，而是给四科各自建立世界模型，再只在真正需要交接的位置建 Bridge。

## 这册解决什么

408 Course Atlas 回答三个问题：

1. 数据结构、计组、操作系统、计算机网络分别研究什么；
2. 四科 Topic / Bridge / Integration 怎样组织，哪些关系不能混；
3. 面对综合题时，应该先切换到哪一种观察语言。

本 README 本身就是 408 的 Canonical Atlas。旧 `408_Course_Atlas.tex` / PDF 不再作为导航入口或地图 Owner，但在逐项 Source Diff 完成前继续保留；后续若需要视觉海报，只从本 README 已确认的关系派生。

仓库为什么这样切，见[408 Canonical Topology 设计依据](00_统一总图/README.md)。后者是架构设计文档，不是学生 Atlas。

## 四个 Subject Atlas

| 学科 | 核心问题 | 入口 |
|---|---|---|
| 数据结构 | 怎样按 Workload 组织关系，使关键操作以可接受成本完成？ | [Data Structure](10_数据结构/README.md) |
| 计算机组成原理 | 怎样用有限硬件正确、高效地实现 ISA 对软件承诺的语义？ | [Computer Organization](20_计算机组成原理/README.md) |
| 操作系统 | 怎样在并发、有限资源和异步硬件事件下提供受保护的执行环境？ | [Operating System](30_操作系统/README.md) |
| 计算机网络 | 没有共享内存与全局即时状态时，独立机器怎样完成通信？ | [Computer Network](40_计算机网络/README.md) |

## 跨科层

只有真正通过 Bridge 两道 Gate 的接口才独立建册：

- [Cross-Subject Bridge Atlas](50_桥梁专题/README.md)
- [Cross-Subject Integration Layer](60_综合专题/README.md)

当前核心跨科 Bridge：

- X-B01 Privilege / Exception / System Call × OS Control；
- X-B02 Hardware Address Translation × OS Virtual Memory；
- X-B03 Interrupt / DMA × OS I/O；
- X-B04 Process / Socket × Transport Endpoint 仍为 Candidate Core。

当前核心跨科 Integration：

- X-I01 一次 LOAD / Memory Access 的完整慢路径；
- X-I02 一次 Blocking File `read()` 的完整生命周期。

## 做题时怎么用

四科共享的只是控制语言，不共享一个万能世界模型：

```text
Data Structure -> Relation / Representation / Operation / Invariant / Cost
CO             -> State / Location / Path / Resource / Timing / Commit
OS             -> Object / Queue / Event / Mechanism / Policy / New State
Network        -> Scope / Name / State Owner / Event / Feedback / Cost
```

规则入口：[408 通用做题规则](90_408做题规则/README.md)。

## 共同观察镜头

跨科时可以共享少量观察问题，但回答必须切回当前 Subject 的语言：

1. **Object / Goal**：当前追踪什么对象，题目最终要求什么？
2. **Representation / State**：系统保存了哪些信息，它们在哪里？
3. **Operation / Event**：什么操作或事件使状态有资格改变？
4. **Invariant / Boundary**：什么必须保持，哪些相似概念不能混？
5. **Cost / Workload**：时间、空间、带宽、I/O 或等待代价从哪里来？

箭头的语义由上下文决定：`A -> B` 可能表示推理顺序、依赖或转换；只有写成状态转换时，才必须同时指出触发事件。共同镜头只负责切换学科，不覆盖四个 Subject Atlas 的母模型。

## 跨科重复出现的关系

这些是 Course Atlas 拥有的关系地图，不是额外 Topic：

| 关系 | 典型落点 | 使用边界 |
|---|---|---|
| Representation / Indirection | Hash bucket、VA -> PTE -> frame、Name -> IP | 多一层映射换定位、共享或隔离；具体机制回各 Topic |
| State / Invariant | Heap 偏序、ISA 提交、PV 条件、TCP 窗口 | 用来解释动作资格与校验，不把四科压成同一种状态机 |
| Scarcity / Sharing | ALU/总线冲突、ready queue、共享链路 queue | 需求超过瞬时供给时出现等待、排队或仲裁 |
| Locality / Caching | Cache、TLB、Page Cache、DNS cache | 必须区分副本 Owner、miss 处理者与一致性边界 |
| Fast / Slow Path | Hash 冲突、Cache miss、Page Fault、timeout | 先判断本次走哪条路径，再计算代价 |
| Trade-off / Workload | 索引维护、流水线 hazard、调度切换、窗口状态 | “更好”必须绑定工作负载与成本口径 |

四个高价值接口继续由 Bridge Own：渐近成本与机器成本默认是 DS 对机器成本模型的 Use；Privilege/MMU/Interrupt/DMA 与 OS 的稳定交接进入 X-B01--X-B03；socket 与 transport endpoint 是否升为 Core 由 X-B04 的证据决定。

## 阅读建议

第一次进入 408，不要先背“跨科大图”。先进入正在学习的 Subject Atlas，把本学科自己的对象和机制建立起来；当两个 Owner 真正发生数据、状态或控制权交接时，再打开 Bridge；只有需要追踪一个完整真实过程时才进入 Integration。

README 到这里停止。课程级地图由本 README 维护；学科深度进入四个 Subject，接口进入 Bridge，完整过程进入 Integration，做题动作进入 Rules。
