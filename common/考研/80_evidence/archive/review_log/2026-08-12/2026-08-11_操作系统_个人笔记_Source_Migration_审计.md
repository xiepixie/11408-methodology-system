# 操作系统个人笔记 Source Migration 审计

> 日期：2026-08-11
>
> 性质：Evidence 层 Source Diff / Owner Diff 记录，不是新的知识 Owner。
>
> 来源一：`学习领域/卡片盒笔记主题索引卡/` 中全部 `OS-*.md` 主题卡。
>
> 来源二：`学习领域/归档/408/操作系统/` 中 20 个 Markdown 文件；其中 10 个为空壳，10 个包含约 2,850 行正文。

## 1. 审计口径

本轮不以逐句搬运为完成标准，而按以下 Gate 判断：

1. 可复用机制必须进入唯一 Topic Owner；
2. 跨 Topic 交接只保留接口，不在两侧复制完整路径；
3. 题面信号、第一动作、验证和退出条件进入 OS Rules 的“待验证”；
4. 已被 Canonical 更准确覆盖的内容记为 Duplicate，不重复扩写；
5. 超出 408 主干但真实的内容保留为 Extension / Source；
6. 含事实错误、绝对化工程结论或无法成立公式的段落明确 Reject。

## 2. 卡片盒主题卡路由

### 2.1 Foundation 与程序运行环境

| Source | Owner | Diff 结论 |
|---|---|---|
| `OS-程序内存映像.md` | OS-00 | Duplicate；代码/数据/BSS/heap/stack 已在“程序运行环境”中分层，未重复扩写 |
| `OS-虚拟机类型对比.md` | OS-00 | Duplicate；Type 1/2 已按部署结构而非优劣口诀解释 |
| `OS-宏内核与微内核对比.md` | OS-00 | Duplicate；现有正文已有特权核心大小、隔离、IPC/切换成本比较轴 |
| `OS-系统结构与引导.md`、`OS-系统引导链.md` | OS-00 | Duplicate；Firmware -> Bootloader -> Kernel -> User Space 生命周期已存在 |
| `OS-用户态与内核态.md` | OS-00 / OS-01/02 Use | Duplicate；权限边界与控制权入口已存在 |

### 2.2 进程、线程、调度与控制权

| Source | Owner | Diff 结论 |
|---|---|---|
| `OS-程序-进程-线程对比.md` | OS-01/02 | Duplicate/Refinement；资源容器与执行路径的对象边界已进入 Canonical |
| `OS-进程间通信IPC.md` | OS-01/02 | Duplicate；按共享状态、数据流/消息、事件通知分类，不搬运 IPC 名词目录 |
| `OS-系统调用.md` | OS-01/02 | Duplicate；系统调用五阶段与 mode switch/context switch 边界已存在 |
| `OS-中断机制.md`、`OS-中断处理过程.md` | OS-01/02；Cross-Subject X-B01 Use | Duplicate；硬件入口与软件 handler 已分责 |
| `OS-中断与异常核心区别.md`、`OS-中断-陷阱-异常对比.md` | OS-00 / OS-01/02 | Duplicate；保留“是否与当前指令同步相关”的稳定判据，不采用混乱的“软件中断”口径 |
| `OS-网络设备接口Socket.md` | OS-01/02 IPC Use；Network Owner | Extension；只保留本地 IPC/进程端点接口，运输层语义不上移到 OS Topic |

### 2.3 并发、同步与死锁

| Source | Owner | Diff 结论 |
|---|---|---|
| `OS-管程wait-锁释放机制.md` | OS-03；Rules | Canonical Update + Candidate Rule；补强 atomic release-and-block、返回前重新加锁与谓词重检 |
| `OS-管程signal-信号量V-本质区别.md` | OS-03；Rules | Canonical Update + Candidate Rule；补入许可是否保存、共享谓词 Owner、Mesa/Hoare 边界 |
| `OS-最小资源数.md` | OS-03；Rules | Canonical Update + Candidate Rule；保留标量公式，但增加单资源、最大需求、完成后释放等适用条件 |
| `OS-死锁条件-临界区要求-概念边界.md` | OS-03 | Duplicate；Coffman 条件与临界区正确性要求已按不同问题分层 |
| `OS-死锁.md` | OS-03 | Duplicate；等待图、安全/不安全/死锁、预防/规避/检测/恢复已完整覆盖 |

### 2.4 虚拟内存与页生命周期

| Source | Owner | Diff 结论 |
|---|---|---|
| `OS-页框分配.md`、`OS-页框分配策略.md` | OS-04；Rules | Canonical Update + Candidate Rules；补入正确性底线 vs 有效驻留、Working Set vs PFF、allocation vs replacement scope |
| `OS-内存连续分配.md` | OS-04 | Duplicate；连续分区、碎片、分配/回收与 Buddy 边界已存在 |
| `OS-内存不连续分配.md` | OS-04 | Duplicate；分页、分段、段页式和多级页表生成链已存在 |

明确拒绝：来源中的“某固定 ISA 示例必需若干页框”若未给完整指令/跨页/fault-restart 语义，不进入稳定结论；“工作集总和超过内存 iff 已颠簸”不成立。

### 2.5 I/O 请求、等待与完成

| Source | Owner | Diff 结论 |
|---|---|---|
| `OS-DMA与页面锁定.md` | OS-05；Cross-Subject X-B03 Use；Rules | Canonical Update + Candidate Rule；保留 DMA-visible mapping 生命周期、pin/unpin 对称、scatter-gather/bounce buffer |
| `OS-IO系统三层并发模型.md`、`OS-IO软件四层架构.md` | OS-05；Rules | Refinement；收敛为数据、控制/完成、task 状态三条线，软件层次继续由 OS-05 Own |
| `OS-中断驱动IO.md`、`OS-阻塞IO模型.md`、`OS-非阻塞IO模型.md` | OS-05 | Duplicate；完成发现、搬运者、调用者行为继续保持正交 |
| `OS-设备独立性.md` | OS-05 | Duplicate；统一接口与设备特定知识归 Driver 的边界已存在 |
| `OS-主从设备号.md` | OS-05；Rules | Canonical Update + Candidate Rule；补入 logical name -> major/minor -> driver -> instance，并阻断 bus master/slave 类比 |
| `OS-字符设备接口.md`、`OS-块设备接口.md` | OS-05 | Duplicate；按工作负载与接口语义区分，不按具体设备死背 |
| `OS-设备管理数据结构.md`、`OS-设备分配策略.md` | OS-05 | Duplicate；SDT/DCT/COCT/CHCT 与静态/动态分配已存在 |
| `OS-缓冲与缓存的区别.md`、`OS-双缓冲技术.md` | OS-05 | Duplicate；速率/粒度匹配与复用副本已经分开 |
| `OS-缓冲池.md` | OS-05；Rules | Canonical Update + Candidate Rule；把三类队列改写为 buffer Owner/内容有效性/状态迁移模型 |
| `OS-Spooling时空解耦.md`、`OS-SPOOLing技术.md` | OS-05 | Duplicate；保留中转存储、队列、后台服务与物理吞吐边界 |
| `OS-磁盘访问时间模型.md`、`OS-磁盘调度算法.md` | OS-05 | Duplicate；成本分解、数轴模拟、方向与端点边界已存在 |
| `OS-LBA逻辑块地址抽象.md` | OS-05；Rules | Canonical Update + Candidate Rule；补入 LBN/LBA/physical placement 三层与“逻辑连续不推出物理连续” |

明确拒绝：来源中的“DMA 只懂裸物理地址”“pin 必然是 PTE 固定位”“普通 `kmalloc` 内存可被换出”“DMA 永远优于 PIO”均不能成为稳定工程结论。

### 2.6 文件系统与跨 Topic 接口

| Source | Owner | Diff 结论 |
|---|---|---|
| `OS-文件系统.md`、`OS-文件系统全景解析.md` | OS-06/07 | Duplicate；Name -> Object -> Open State -> Data Mapping -> Persistence 主干已覆盖 |
| `OS-文件系统深度解析.md` | OS-06/07 | Duplicate/Refinement；create、open/read/write、link/unlink、VFS、block mapping 与 crash consistency 已存在 |
| `OS-VFS三级表结构解耦进程与文件.md` | OS-06/07；OS-B03 Use | Duplicate；fd -> OFD -> inode/object 与独立 open/fork/dup 的 offset 关系已存在 |
| `OS-PageCache.md` | OS-B04 VM × File × I/O；OS-04/05/06 Use | Bridge Note / existing interface；不在三个 Topic 中再造完整 Page Cache Owner |

## 3. 归档长笔记路由

| Source | Owner | Diff 结论 |
|---|---|---|
| `操作系统概述.md`、`内存管理基础.md`、`内存连续分配.md`、`内存非连续分配.md`、`死锁.md`、`IO设备,分配与回收.md`、`IO软件与控制.md`、`文件系统基础.md`、`目录与空闲空间管理.md`、`文件物理结构.md` | 对应 OS-00/03/04/05/06/07 | Empty Source；文件为 0 行，不产生知识更新 |
| `处理机调度.md` | OS-01/02 | Duplicate；批处理/分时/实时的目标函数与经典算法比较已覆盖 |
| `进程管理.md` | OS-01/02 | Duplicate；程序/进程/线程、实现模型、生命周期与调度均已覆盖 |
| `进程通信.md` | OS-01/02 | Duplicate/Extension；IPC 主干已覆盖，RPC/网络 socket 深层语义留作 Source |
| `中断与系统调用.md` | OS-01/02；X-B01 Use | Duplicate/Extension；入口/handler 分责已覆盖，中断控制器优先级与屏蔽细节留给计组 Owner |
| `进程同步.md` | OS-03 | Duplicate；生产者消费者、读者写者、理发师、哲学家、吸烟者、前驱图均已在模式库中 |
| `虚拟内存管理.md` | OS-04 | Canonical Update 的辅助 Source；与页框主题卡合并审查，不重复导入 |
| `页框分配.md` | OS-04；Rules | Canonical Update + Reject mix；双层页框需求、PFF 与二维轴进入 Owner，错误“定理”和绝对化公式被拒绝 |
| `磁盘.md` | OS-05；Rules | Refinement；I/O 三线、LBA 边界与题型信号进入现有 Owner，其余重复 |
| `OS-公式总结.md` | OS-04/05；Rules | Source only；公式必须回到题设假设验证，不把速查表设为第二 Owner |
| `OS-术语汇总.md` | OS-04 / OS-01/02 | Source only；术语解释由对应机制 Owner 维护，不建立平行词典 |

## 4. Owner 结果

- OS-00：个人笔记与当前程序运行环境、系统结构、引导和虚拟机正文一致，无需重复扩写。
- OS-01/02：进程/线程/调度/IPC/控制权正文已经覆盖来源主干，无新增机制 Owner。
- OS-03：新增条件变量与信号量的状态 Owner 边界，以及单类资源最小量公式的严格适用域。
- OS-04：新增页框正确性底线/性能目标、Working Set/PFF 和配额/置换作用域的正交结构。
- OS-05：新增 DMA mapping 生命周期、major/minor 标识层、经典缓冲池状态机与 LBA 边界。
- OS-06/07：来源中的文件系统主干已由现有 Canonical 更准确覆盖，无需复制。
- OS Rules：新增可执行候选动作，并记录两个已否定的绝对化规则；旧笔记不构成“已采用”证据。

## 5. 结论与下一步

本次迁移属于 **Canonical Update + Candidate Rules + Explicit Rejects**。高价值内容已经进入唯一 Topic Owner，题面动作进入待验证 Rules，重复内容未建立第二正文，错误与超纲实现细节未被包装成稳定结论。

下一步应使用真题/陌生题攻击新增 Rules，重点验证：管程 `signal/V` 边界、single-resource 最小量公式 Gate、Working Set/PFF 分流、DMA mapping 生命周期、LBN/LBA/physical placement 三层。未获得真实做题证据前，不把这些规则移入“已采用”。
