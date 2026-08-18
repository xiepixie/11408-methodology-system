# CodeBrick OS 全量 Source Diff

日期：2026-08-15  
场景：`import`  
角色：Mapper + Editor  
状态：已完成 76 篇逐篇语义 Diff、Canonical 回写与双向完成审计

## 1. 目标与边界

本记录服务于一个明确目标：吸收 `../../../../sources/codebrick_408/01_操作系统_OS/` 的全部有效细节，以现有操作系统 Subject Atlas 与六册 Canonical Topic 正文为骨架，渐进扩充 OS Handbook。

本记录只拥有 Source Diff 证据，不拥有任何操作系统定义、机制或做题规则。稳定知识必须回写唯一 Canonical `.tex`；题面触发、第一动作、检查和退出条件进入 OS Rules；模拟器使用说明只作为学习工具证据，不因篇幅较长自动进入 Handbook。

## 2. 输入快照

- Source 根目录：`../../../../sources/codebrick_408/01_操作系统_OS/`（从 `kaoyan/` 回到资源目录后进入 CodeBrick Source）。
- 原子笔记：76 篇，不含 `00_操作系统知识全景总览.md`。
- 总行数：13,288 行。
- 聚合 SHA-256：`08aab2a94e0b1c75a2e5c77848111beb155eec9f6b392b57acaaa4eb6f4f3b5c`。
- 分组：概述 9 篇 / 1,244 行；进程管理 29 篇 / 5,756 行；内存管理 15 篇 / 2,640 行；文件管理 12 篇 / 1,976 行；I/O 管理 11 篇 / 1,672 行。

聚合哈希按相对路径排序；每个文件把 `UTF-8 relative-path + NUL + lowercase ASCII hex sha256(file-content) + NUL` 依次输入外层 SHA-256。Source 内容变化时，必须重新打开受影响行，不能沿用本记录的旧结论。

## 3. 唯一 Owner 路由

| CodeBrick 分组 | Canonical Owner | 路由原则 |
|---|---|---|
| 操作系统概述 | OS-00；控制权细节只在 OS-01/02 使用 | OS-00 Own 运行环境、结构、引导、虚拟机和权限入口；不重讲进程生命周期 |
| 进程/线程/调度/IPC | OS-01/02 | Own 执行实体、控制权、生命周期、队列、调度和 IPC 引用关系 |
| 同步/锁/PV/管程/死锁 | OS-03 | Own 并发轨迹、等待条件、互斥、同步、不变量、安全性和死锁 |
| 内存管理 | OS-04 | Own VA/VMA/PTE/frame/backing object、驻留、置换、页生命周期和 mmap |
| 文件管理 | OS-06/07 | Own name/object/open-reference/block/persistence 五层映射与文件操作 |
| I/O 管理 | OS-05 | Own request/driver/controller/transfer/completion/wakeup、buffer、设备分配和介质成本 |
| 软硬件交接 | X-B01/X-B02/X-B03 或 OS Internal Bridge | Topic 只保留最小接口；稳定 handoff 由 Bridge Own |
| 题面动作与公式口径 | OS Rules | 机制正文解释为什么；Rules 解释何时触发、如何检查和何时停止 |

## 4. 76 篇逐项路由台账

状态词：`Routed` 表示唯一 Owner 已确定、尚未完成逐篇语义核销；`Diffed` 表示已逐篇核对并形成 Covered/Update/Extension/Reject 结论；`Written` 表示需要的知识已回写 Canonical Owner。不得把 `Routed` 误读为已经吸收。

### 4.1 操作系统概述（9）

| Source | Owner | 当前状态 | 重点核对 |
|---|---|---|---|
| `01_操作系统概述/cpu-mode.md` | OS-00 + X-B01 | Written (OS-00) | 特权/敏感指令与保护闭环已进入 OS-00 第五章；具体入口/返回状态仍待 X-B01 联动核对 |
| `01_操作系统概述/interrupt-exception.md` | OS-01/02 + X-B01 | Diffed (Covered) | OS-01/02 第十六章已有硬件/软件入口、断点/现场、向量、嵌套、屏蔽字、时钟抢占与进程切换边界；X-B01 保留最小跨科接口，无需重复拥有 |
| `01_操作系统概述/link-load.md` | OS-00 | Diffed (Covered) | OS-00 第四章已有 symbol resolution、relocation、三种链接与三种装入方式及地址绑定边界 |
| `01_操作系统概述/memory-image.md` | OS-00 + OS-04 Use | Written | OS-00 第四章已补文件占用、来源、权限、增长方式矩阵；页表与驻留细节保持转交 OS-04 |
| `01_操作系统概述/os-boot.md` | OS-00 | Written | OS-00 第七章已补 BIOS/MBR/PBR/UEFI、446+64+2 推导、阶段化引导与首个用户态系统边界 |
| `01_操作系统概述/os-concept.md` | OS-00 | Written | OS-00 第二、三章已补时分/空分复用、异步可再现性底线及多道运行的中断/独立 I/O 闭环 |
| `01_操作系统概述/os-structure.md` | OS-00 | Written | OS-00 第六章已补微内核教学路径计数、机制/策略边界、外核正交轴、LibOS 收益与四类代价 |
| `01_操作系统概述/system-call.md` | OS-00 + X-B01 | Written (OS-00) | OS-00 第五章已补服务分类、库函数边界、四类参数传递与 user-pointer 校验；入口/返回硬件接口待 X-B01 核对 |
| `01_操作系统概述/virtual-machine.md` | OS-00 | Written | OS-00 第九章已补 CPU 四类路径、GVA→GPA→HPA、shadow/EPT、三类 I/O 虚拟化、IOMMU 与 Type 1/2 判据 |

### 4.2 进程、线程、调度、同步与死锁（29）

| Source | Owner | 当前状态 | 重点核对 |
|---|---|---|---|
| `02_进程管理/banker.md` | OS-03 | Written | 已补 Available/Total 自检、Need/Allocation 归还不变量、Work 单调贪心证明、末态核对、$O(n^2m)$ 与 Max/动态进程适用边界 |
| `02_进程管理/condition-variable.md` | OS-03 | Written | 已补入口/条件/紧急三类队列及 wait/signal 交权；Hoare/Mesa/Hansen 语义、lost wakeup 与 while 边界既有并完成核销 |
| `02_进程管理/context-switch-simulator.md` | Evidence/Extension；机制回 OS-01/02 | Diffed (Extension + Corrected) | 保留 A→B 动态轨迹、模式/线程/进程切换对照与 $q/(q+\delta)$ 实验变量；UI 指南留 Evidence；拒绝“模式切换只改 PSW、寄存器绝不会移动”“每次复制整个 PCB”等过度简化 |
| `02_进程管理/context-switch.md` | OS-01/02 | Written | 三层上下文已映射到四维 Switch；补硬件入口/软件保存边界、内核栈 SP 交接、保存/恢复动作与切换事件计数、直接/间接成本 |
| `02_进程管理/deadlock-concept.md` | OS-03 | Written | 既有定义、资源分类、Coffman、四策略、预防代价与单类资源公式完成；本批补四策略选择的边界与资源全序/锁序接口 |
| `02_进程管理/deadlock-detection.md` | OS-03 | Written | 既有 RAG/化简/矩阵 Request 算法与 Banker 分界完成；补贪心不变量、检测触发时机、逐个终止复检、检查点回滚与恢复饥饿 |
| `02_进程管理/dining-philosophers.md` | OS-03 | Written | 既有等待环、限制人数/全序/原子资格方案完成；补 AND、mutex 包两次 P 与四类方案破坏中间状态/无饥饿边界 |
| `02_进程管理/fair-scheduling.md` | OS-01/02 | Written | 已补 Actual/Entitled 比率、权重份额与统计窗口；Process/User/Thread 主体及多开进程份额漏洞由既有模型覆盖 |
| `02_进程管理/fcfs.md` | OS-01/02 | Written | 已补统一比较键、非抢占决策点、有限队列无新来者饥饿证明、护航效应导致 CPU/I/O 成团空闲 |
| `02_进程管理/hrrn.md` | OS-01/02 | Written | 已补响应比的假想带权周转含义、FCFS/SJF 两端倾向、仅决策点重算与无饥饿所需进度假设 |
| `02_进程管理/ipc.md` | OS-01/02 | Written | 已补低/高级通信入口、消息边界/寻址/方向/容量/三类阻塞组合、匿名/命名 pipe、EOF、signal 递送边界与定性选择矩阵 |
| `02_进程管理/lock.md` | OS-03 | Written | 已补四准则入口、spin/sleep 成本不等式、单 CPU/多 CPU、TTAS 缓存写失效、锁粒度和锁序；priority 协议承接三方入口 |
| `02_进程管理/mlfq.md` | OS-01/02 | Written | 已补五条生成规则、量子耗尽/提前让出、累计 allotment 防 gaming、boost/aging 与层数/量子/周期参数权衡；同刻规则保持题设参数 |
| `02_进程管理/multi-level-queue.md` | OS-01/02 | Written | 已补队列分类/队列间/队列内三次决策、固定优先级 vs CPU share、前台 RR/后台 FCFS 的 workload 匹配及 MLQ 固定成员边界 |
| `02_进程管理/multiprocessor.md` | OS-01/02 | Written | 已补 SMP/AMP 与 UMA/NUMA 正交轴、四类经典组织、soft/hard affinity、push/pull、迁移收益不等式及持锁抢占耦合 |
| `02_进程管理/priority.md` | OS-01/02 + OS-03 Use | Written (OS-01/02) | 已补静态/动态 × 抢占/非抢占两轴、数值方向依题设、Aging 活性假设与三任务优先级反转接口；inheritance/ceiling 待 OS-03 唯一 Owner 核销 |
| `02_进程管理/process-concept.md` | OS-01/02 | Diffed (Covered + Corrected) | 既有 Program/Process Image/Process Instance/Thread、共享私有三权与 PCB≠进程已覆盖；Source 将共享库笼统称“一个进程含多个程序”被规范为 executable/shared-object mappings，不升级含混定义 |
| `02_进程管理/process-control.md` | OS-01/02 | Written | 既有线性/链接/索引与原子状态事务已覆盖；补 Free PCB/Ready/$W_E$ 的操作成本生成、创建/终止触发分类及父子关系的系统边界 |
| `02_进程管理/process-state.md` | OS-01/02 | Written | 五态/七态、禁边与队列关系既有覆盖；补四类 Suspend 发起者、进程/线程组作用域及“线程不机械套独立七态”边界 |
| `02_进程管理/producer-consumer.md` | OS-03 | Written | 既有容量不变量、P 顺序死锁、V 顺序边界与多类变式完成；补单槽可省 mutex 与多类产品定位不变量 |
| `02_进程管理/reader-writer.md` | OS-03 | Written | 既有读者优先/写者优先完成；补公共到达闸门公平方案、FIFO 公平假设与读者并发上限/信号量集接口 |
| `02_进程管理/rr.md` | OS-01/02 | Written | 已补 RR 队列事务、$q/(q+\delta)$ 假设、约 $(n-1)(q+\delta)$ 重访时间、固定 workload 退化 FCFS 与同刻入队显式约定 |
| `02_进程管理/scheduling-concept.md` | OS-01/02 | Written | 三级调度、指标、scheduler/dispatcher 与安全点既有覆盖；补 Candidate/Key/Decision/Tie/Preemption 统一控制器和 idle task 接口 |
| `02_进程管理/scheduling-simulator.md` | Evidence/Extension；机制回 OS-01/02 | Diffed (Extension + Corrected) | UI/默认甘特图留 Evidence；吸收跨算法参数实验与 tie/arrival/switch-cost 显式约定；拒绝把默认 workload 下“FCFS 最大、SJF 最小”等观察升级为无条件定理 |
| `02_进程管理/semaphore.md` | OS-03 | Written | 已补整型 busy-wait→记录型 block/wakeup、负值编码边界、AND 原子多资源取得、信号量集 $t/d$ 与 $d=0$ 测试语义 |
| `02_进程管理/sjf.md` | OS-01/02 | Written | 已补已到达候选集、SJF/SRTF 决策点、相邻交换论证与假设边界、EWMA 及 $\alpha$ 两端、阶段变化滞后与长任务饥饿 |
| `02_进程管理/sync-impl.md` | OS-03 | Written | 已补单标志→双标志先/后检查→Peterson 失败修补链、内存序实现边界及硬件原子/让权分界 |
| `02_进程管理/sync-mutex-concept.md` | OS-03 | Written | 已补 Entry/Critical/Exit/Remainder 四段、四准则 Safety/Progress/Efficiency 分层与陌生方案反例控制器 |
| `02_进程管理/thread.md` | OS-01/02 | Written | ULT/KLT、M:1/1:1/M:N、两级队列与阻塞传播既有覆盖；补 Runtime System、Jacketing、LWP、PTDA、现场表示边界和进程级终止/挂起作用域 |

### 4.3 内存管理（15）

| Source | Owner | 当前状态 | 重点核对 |
|---|---|---|---|
| `03_内存管理/clock-replace.md` | OS-04 | Written | A/M 位生命周期、简单/改进 CLOCK、扫描轮次与 Belady 边界 |
| `03_内存管理/contiguous-allocation.md` | OS-04 | Written | 三种连续分配、空闲结构、四策略、四种回收邻接、紧凑前提 |
| `03_内存管理/demand-paging.md` | OS-04 + X-B02/X-B03 Use | Written | fault/block/I/O/wakeup/retry、EAT 路径、P/A/M 位、TLB 失效 |
| `03_内存管理/fifo-replace.md` | OS-04 | Written | 命中不更新、Belady 异常与 stack property 边界 |
| `03_内存管理/lru-replace.md` | OS-04 | Written | 精确/近似实现、开销、与 FIFO 的非支配关系 |
| `03_内存管理/memory-concept.md` | OS-04 | Written | 重定位、保护、分配、共享、覆盖/交换、内外碎片 |
| `03_内存管理/memory-mapped-file.md` | OS-04 + OS-B04 | Written | file-backed 私有/共享映射、脏页写回、页缓存与请求分页边界 |
| `03_内存管理/opt-replace.md` | OS-04 | Written | 规则、交换论证、最优但不可在线实现 |
| `03_内存管理/page-allocation.md` | OS-04 | Written | 最小页框、fixed/variable × local/global、调页来源、工作集/PBA、回收资格 |
| `03_内存管理/page-replace-simulator.md` | Evidence/Extension；机制回 OS-04 | Diffed | 保留实验变量、引用串和算法对比；不迁移 UI 指南 |
| `03_内存管理/paging.md` | OS-04 + X-B02 | Written | 页大小权衡、PTE 字段、TLB、多级页表、EAT |
| `03_内存管理/seg-paging.md` | OS-04 + CO-07 Use | Written | 位划分、两阶段合法性检查、三种方式对比 |
| `03_内存管理/segmentation.md` | OS-04 + CO-07 Use | Written | 逻辑结构、段表、共享/保护、分页边界 |
| `03_内存管理/virtual-memory-concept.md` | OS-04 | Written | 局部性反例、定义、硬件支持、请求分段、基本分页边界 |
| `03_内存管理/virtual-memory-perf.md` | OS-04 + OS Rules | Written | 缺页率因素、thrashing 正反馈、工作集/PFF/负载控制 |

### 4.4 文件管理（12）

| Source | Owner | 当前状态 | 重点核对 |
|---|---|---|---|
| `04_文件管理/directory.md` | OS-06/07 | Written | 命名映射、结构演进、操作、线性/散列实现 |
| `04_文件管理/file-concept.md` | OS-06/07 | Written | 文件身份、属性、分类、操作集合 |
| `04_文件管理/file-logical-structure.md` | OS-06/07 | Written | 流式/记录式、顺序/索引/索引顺序/散列逻辑结构 |
| `04_文件管理/file-operation.md` | OS-06/07 | Written | create/delete/open/close/read/write/seek/truncate 状态变化 |
| `04_文件管理/file-physical-structure.md` | OS-06/07 | Written | 连续/链接/FAT/索引/混合索引、随机访问与扩展成本 |
| `04_文件管理/file-protection.md` | OS-06/07 | Written | access matrix、ACL/capability、Unix rwx、目录权限、口令/加密 |
| `04_文件管理/free-space.md` | OS-06/07 | Written | 空闲表/链/位图/成组链接及比较 |
| `04_文件管理/fs-mount.md` | OS-06/07 | Written | mount/unmount、mount table、路径跨越、自举根文件系统 |
| `04_文件管理/fs-structure.md` | OS-06/07 | Written | 软件层次、磁盘结构、内存结构 |
| `04_文件管理/hard-soft-link.md` | OS-06/07 | Written | 身份/路径语义、跨 FS、删除悬空、引用计数 |
| `04_文件管理/inode.md` | OS-06/07 | Written | FCB/inode、磁盘/内存 inode、文件名边界、inode 定位 |
| `04_文件管理/vfs.md` | OS-06/07 | Written | 函数指针接口、superblock/inode/dentry/file、调用流程 |

### 4.5 I/O 管理（11）

| Source | Owner | 当前状态 | 重点核对 |
|---|---|---|---|
| `05_IO管理/buffer.md` | OS-05 | Written | 四目标、单/双/循环缓冲、一般耗时模型、缓冲池、磁盘缓存边界 |
| `05_IO管理/device-allocation.md` | OS-05 | Written | DCT/COCT/CHCT/SDT、分配约束、步骤、回收、LUT、SPOOLing 后的虚拟分配 |
| `05_IO管理/device-concept.md` | OS-05 + CO-08 Use | Written | 设备/控制器/端口/接口、端口编址边界 |
| `05_IO管理/disk.md` | OS-05 | Written | 物理结构、访问时间、调度、提速、格式化/分区/文件系统、坏块 |
| `05_IO管理/driver-interface.md` | OS-05 | Written | 统一接口、驱动流程、控制方式耦合、中断配合 |
| `05_IO管理/hdd-simulator.md` | Evidence/Extension；机制回 OS-05 | Diffed | 吸收六算法算例、访问时间和地址变量；不迁移 3D/UI 指南 |
| `05_IO管理/io-api.md` | OS-05 | Written | 字符/块/网络 API、系统调用、blocking/nonblocking/async 边界 |
| `05_IO管理/io-control.md` | OS-05 + X-B03 | Written | polling/interrupt/DMA/channel 的搬运者、完成者与粒度 |
| `05_IO管理/io-software-layer.md` | OS-05 | Written | 分层目标、各层职责、一次读盘责任链 |
| `05_IO管理/spooling.md` | OS-05 | Written | 脱机到假脱机、输入/输出井、守护进程、虚拟设备 |
| `05_IO管理/ssd.md` | OS-05 | Written | FTL、写放大、GC、磨损均衡、闪存类型、OS 策略变化 |

## 5. 分批写入顺序

1. OS-00：9 篇概述，先核对 MBR/PBR/UEFI、系统调用参数传递、虚拟化方式和中断向量/嵌套细节。
2. OS-01/02 + OS-03：29 篇按 Owner 拆分；先完成调度算法与同步/死锁矩阵，再吸收模拟器中真正生成性算例。
3. OS-04：15 篇已完成；补足连续分配回收、P/A/M 位与 EAT、PBA、替换算法实现/边界，并发布 25 页手册。
4. OS-06/07：12 篇已完成；补足逻辑文件结构、Unix 目录权限、成组链接、VFS 对象和 inode 定位，并发布 24 页手册。
5. OS-05：11 篇已完成；补足一般缓冲时间模型、设备分配表链、磁盘管理/坏块和 SSD 细节，并发布 31 页手册。
6. Bridge/Integration/Rules：只处理 Topic 扩充真实改变的接口或题面动作，不复制机制。

## 6. 完成门槛

- 76 行全部从 `Routed` 进入 `Diffed`，每行有明确 `Covered / Update / Extension / Reject` 结论与 Owner 位置；
- 所有 `Update` 都已进入唯一 Canonical `.tex`，且原有模型、推导、边界和例子无删除；
- 模拟器/UI 指南只吸收其生成性算例与观察变量，不复制产品使用说明；
- Topic 改动影响的 Bridge/Integration/Rules 已反向核对；
- 六册通过 `cognitive_system.py publish`，随后 `progress --write`、`check`、`audit`；
- 最后按源目录和 Canonical 目录双向抽查，不能以关键词命中替代语义覆盖证明。

## 7. 当前决策

- 结果类型：`Canonical Update / Source Diff complete`。
- 当前没有因为 Source 数量改变 OS Subject 拓扑或 Owner。
- 当前没有把外部笔记中的题目链接、教材出处或 UI 描述提升为 Canonical 事实。
- OS 概述 9 篇已全部完成语义核销：8 篇形成 OS-00 增量，`interrupt-exception.md` 由既有 OS-01/02 机制正文覆盖，X-B01 只保留接口边界。
- OS-00 23 页 Published View 已通过全页渲染、空白页和左右安全区检查；OS-01/02 50 页也已完成同样的全页渲染与边缘检查。
- OS-01/02 所属 18 篇已全部语义核销：Canonical 从 40 页增量到 50 页；两个 simulator 只吸收生成性观察变量并纠正过度简化，UI 留 Evidence。
- OS-03 的同步、锁、PV、管程与死锁 11 篇已全部核销，Canonical 从 30 页增量到 36 页并通过发布编译；`priority.md` 的 inheritance/ceiling 接口也已回写 OS-03。
- OS-04 内存 15 篇已全部核销，Canonical 发布为 25 页；连续分区、翻译/EAT、缺页生命周期、页框分配、置换与 mmap 边界已补齐并通过全页检查。
- OS-06/07 文件 12 篇已全部核销，Canonical 发布为 24 页；逻辑/物理结构、目录/链接、VFS/mount、空闲空间和文件操作状态链已补齐并通过全页检查。
- OS-05 I/O 11 篇已全部核销，Canonical 发布为 31 页；缓冲时间模型、DMA/设备表链、SPOOLing、HDD/SSD 成本模型已补齐；第 10 页原有 DMA 生命周期单行越界已修复，全页检查无空白页和左右越界。
- 当前 76 篇已全部完成语义核销；下一动作是做双向完成审计并确认 Bridge/Integration 接口无需重复机制。

## 8. 完成审计（2026-08-15）

- Source 侧：目录共有 77 个 Markdown；排除只负责导航且自述“共 76 篇”的 `00_操作系统知识全景总览.md` 后，恰有 76 个原子文件、13,288 行。按上节可复算算法得到聚合 SHA-256 `08aab2a94e0b1c75a2e5c77848111beb155eec9f6b392b57acaaa4eb6f4f3b5c`。
- Ledger 侧：76 个 Source 相对路径与台账 76 行集合完全相等，无缺项、无额外项、无 `Routed`；状态均为 `Written` 或 `Diffed` 及其带 Owner/边界的细分形式。
- Canonical 侧：六册唯一 Owner 均保留原文并完成增量回写；模拟器只吸收算法变量、引用串和生成性对比，不迁移 3D/UI/产品使用说明。
- Bridge/Integration 反查：OS-B04 已拥有 file-backed page、mmap、page cache、I/O completion 的 handoff；OS-I01 已把 DMA/interrupt 硬件交接路由到 X-B03。新增 Topic 细节没有产生新的可复用接口，因此结论为 `No Update`，避免在 Bridge 重复机制。
- Published View：OS-00/OS-01/02/OS-03/OS-04/OS-05/OS-06/07 分别为 23/50/36/25/31/24 页；均经发布脚本编译。OS-05 本轮全页渲染无空白页和左右越界，并修复第 10 页 DMA 生命周期公式的旧版越界。
