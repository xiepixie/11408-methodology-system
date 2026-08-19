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

官方考查基准与考纲原件见：[408 官方考试大纲完整版](408_考试大纲_官方原件完整版.md)。

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

四科共享的只是控制语言，不共享一个万能世界模型。进入不同 Subject 后，应切换到各自的检查坐标：

- **Data Structure**：Relation、Operation Contract、Workload、Representation、Invariant / Boundary、Cost；
- **CO**：ISA State、Location、Path / Resource、Timing、Architectural Visibility、Cost；
- **OS**：Object / Relation、Resource Metadata / Queue、Event、Mechanism / Policy、New State、Safety / Liveness；
- **Network**：Scope、Name / Object、State Owner、Event / Transition、Feedback、Cost。

这些是检查职责，不是四条学科本体的因果链。

规则入口：[408 通用做题规则](90_408做题规则/README.md)。

## 共同观察镜头

跨科时可以共享少量观察问题，但回答必须切回当前 Subject 的语言：

1. **Object / Goal**：当前追踪什么对象，题目最终要求什么？
2. **Representation / State**：系统保存了哪些信息，它们在哪里？
3. **Operation / Event**：什么操作或事件使状态有资格改变？
4. **Invariant / Boundary**：什么必须保持，哪些相似概念不能混？
5. **Cost / Workload**：时间、空间、带宽、I/O 或等待代价从哪里来？

共同镜头只负责切换学科，不覆盖四个 Subject Atlas 的母模型。全项目不再让无标签箭头依靠上下文猜关系：逻辑推导使用 $\Rightarrow$；元素映射使用 $\mapsto$；状态迁移写明事件；接口/信息流必须加标签；推荐检查顺序直接使用编号列表。

## 跨科重复出现的关系

这些关系首先由课程总图负责列出和导航；默认不因“跨科重复出现”就额外建册。只有当某一关系通过“跨科母模型”的晋升条件——存在稳定母问题、可迁移生成模型、明确禁止错误类比，并且不会抢走局部机制归属——才允许单独展开成长文专题：

| 关系 | 典型落点 | 使用边界 |
|---|---|---|
| 表示与间接层 | Hash 桶定位；虚拟地址经页表项形成物理页框；域名经解析得到地址记录 | 多一层映射换定位、共享或隔离；每个映射的输入、输出和负责人必须单独说明，具体机制回各专题 |
| 状态与不变量 | Heap 偏序、指令提交、PV 条件、TCP 窗口 | 用来解释动作资格与校验，不把四科压成同一种状态机 |
| 稀缺与共享 | ALU/总线冲突、就绪队列、共享链路队列 | 需求超过瞬时供给时出现等待、排队或仲裁 |
| [**缓冲与有限中间态**](00_统一总图/跨科母模型_缓冲与有限中间态.md) | 循环队列、流水寄存器/硬件 FIFO、操作系统缓冲池、可靠传输/TCP 接收缓冲、路由器队列 | 用有限空间把不能同时、等速、同粒度或按序推进的两端解耦；已通过母模型晋升条件，但具体机制仍回各专题 |
| 局部性与缓存 | Cache、TLB、页缓存、DNS 缓存 | 必须区分副本负责人、未命中处理者与一致性边界；缓存与缓冲可以共用物理区域，但概念目的不同 |
| 快路径与慢路径 | Hash 冲突、Cache miss、Page Fault、timeout | 先判断本次走哪条路径，再计算代价 |
| 权衡与工作负载 | 索引维护、流水线 hazard、调度切换、窗口状态 | “更好”必须绑定工作负载与成本口径 |

### 缓冲与有限中间态：第一份 Atlas-owned 跨科母模型补充

“缓冲”不是一种数据结构，也不是一种特殊内存材料。它反复出现，是因为两个阶段经常无法在同一时刻、以同一速率、同一粒度、同一顺序或同一资源占有条件直接完成交接。系统于是用**有限中间态**换取时间解耦，再由空/满、所有权、反馈和调度决定边界行为。

这一关系已经单独展开为[跨科母模型：缓冲与有限中间态](00_统一总图/跨科母模型_缓冲与有限中间态.md)。这份 Course Atlas 补充文档统一解释单缓冲、双缓冲、循环缓冲、缓冲池、队列、缓存、窗口、直接存储器访问、流水寄存器、动态随机存取存储器行缓冲、假脱机、外部排序缓冲、可靠传输接收缓冲、TCP 接收缓冲和路由器队列，并明确哪些只是相似、不能硬套同一状态机。它不是第五种 Handbook，不改变局部机制的唯一 Owner。

Course Atlas 只保留三条压缩结论：

1. **缓冲容量不等于服务能力**：有限 Buffer 能吸收 burst、允许重叠，但长期到达率持续超过服务率时最终仍会触及满边界；
2. **Buffer ≠ Queue ≠ Cache ≠ Window**：分别回答暂存解耦、服务次序、未来复用和逻辑许可；它们可以组合，不是同义词；
3. **看到陌生缓冲先问四件事**：谁生产、谁消费、为什么不能直接交接、满了怎么办；随后立即切回具体 Subject Topic。

这组关系不晋升为跨科 Bridge：它没有稳定的“学科 A 输出经翻译后成为学科 B 输入”单一接口，而是多个独立 Owner 反复采用的设计模式。

四个高价值接口继续由 Bridge Own：渐近成本与机器成本默认是 DS 对机器成本模型的 Use；Privilege/MMU/Interrupt/DMA 与 OS 的稳定交接进入 X-B01--X-B03；socket 与 transport endpoint 是否升为 Core 由 X-B04 的证据决定。

## 阅读建议

第一次进入 408，不要先背“跨科大图”。先进入正在学习的 Subject Atlas，把本学科自己的对象和机制建立起来；当两个 Owner 真正发生数据、状态或控制权交接时，再打开 Bridge；只有需要追踪一个完整真实过程时才进入 Integration。

README 到这里停止。课程级地图由本 README 维护；学科深度进入四个 Subject，接口进入 Bridge，完整过程进入 Integration，做题动作进入 Rules。
