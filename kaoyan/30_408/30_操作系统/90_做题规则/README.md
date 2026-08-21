# 操作系统做题规则

状态：工作稿。475–695 操作系统练习题库已完成一轮回归攻击；这些证据可支持训练规则继续保留，但**不能替代真题 + 陌生题验证**，因此尚不直接升级为“已采用”。

## 已采用

暂无。既有出版物中的检查表仍需在真题和陌生题中完成最终验证。

题库回归证据索引：[475–695 题库回归矩阵](题库回归矩阵.md)。

## 题库回归已支持｜475–695

本轮 221 道题反复支持了以下操作规则，后续验证应优先用真题/陌生题攻击其边界，而不是重新从零发明另一套流程：

- **状态题**：`Blocked / Ready / Running / Suspended` 必须落到“缺 CPU、缺事件还是缺重新激活资格”；wakeup 只先承诺 Ready。
- **线程题**：先数内核真正可见的调度实体，再判断 ULT/KLT/M:N 的时间片、阻塞传播和物理并行度。
- **调度题**：先固定 Candidate / Key / Decision Point / Tie / Preemption；RR 中主动阻塞会提前释放 CPU，动态优先级必须服从题设更新策略。
- **PV/Mutex**：先确定 semaphore 内部记法；经典负值模型才可用 `|S|=等待者数`；`Blocked != Unlock`，锁所有权与 CPU 所有权分开追踪。
- **死锁**：单类资源公式必须先过假设门；`Deadlocked ⊂ Unsafe`，多类资源立即切回 Need/Available/Safety。
- **经典内存管理**：先分地址绑定时机、物理放置粒度、逻辑分段结构和碎片类型；动态分区必须维护地址有序区间而非只记块大小。
- **分页/虚存**：translation / residency / fault / replacement 分层；多级页表先锁 offset，再拆 VPN；置换前先锁 frame quota 与 victim scope。
- **文件系统**：pathname 与 fd 两个入口分开；先追 `fd -> open state -> object`；I/O 次数题先写缓存假设；bitmap 先统一 0/1-based 编号。
- **I/O**：控制线、数据线、task 状态线分开；Interrupt / DMA / Blocking 互不等价；缓冲先画时间线；磁盘调度先声明 endpoint convention，再生成服务顺序。
- **设备成本模型**：HDD 的 seek/rotation/transfer 与 SSD 的 FTL/GC/wear leveling 不混用；CHS 只在题设固定几何模型下线性化。

## 待验证

### OS 首次定位链

```text
Model Contract
-> Resource / Abstraction
-> Objects / Relations / Queues
-> Event
-> Boundary / Owner
-> Mechanism
-> Policy
-> Invariant
-> Wait / Fault / Recovery
-> Cost
```

第一步先锁定**决定答案的模型契约**：单/多处理器、调度域、信号量内部表示、地址/块编号方式、经典实现口径、是否忽略某类缓存/缺页/写回/端点成本。只有这些前提不改变答案时，才允许省略不写。随后再区分底层资源与上层抽象，按事件推进状态；只有存在多个合法候选时才引入 Policy。正常路径已经唯一且题目不问失败/性能时，在 `Invariant` 检查通过后停止，不机械展开慢路径与成本。

### 不同维度不能互相推出

遇到选项把两个概念直接画等号时，先检查它们是否属于不同轴：

- `Blocked ≠ Unlock`：CPU 使用权变化，不自动改变锁/资源所有权；
- `Wakeup ≠ Running`：等待条件满足，不自动完成调度；
- `Mapping ≠ Residency`：存在虚拟映射，不保证页面已在 RAM；
- `Interrupt ≠ DMA`：一个描述完成通知，一个描述主要数据搬运者；
- `fd ≠ OFD ≠ file object`：句柄、打开实例、持久对象属于不同层；
- `Available enough ≠ Safe`：当前能分配，不代表试分配后仍存在安全序列。

这类“跨轴偷换”是 475–695 中最稳定的错误来源之一。
### 先列对象、关系和队列

综合题开始模拟前，先列出 task、address space、fd/OFD、page/frame、request 等对象，以及当前引用和所在队列。

### 事件、机制和策略分开写

先写发生了什么，再写系统用什么机制处理，最后才写策略选择哪个合法结果。

### 状态题把“状态标签”落到 Queue / Wait Relation

看到 Ready / Running / Blocked 不先背箭头，先问当前实体是否有 CPU、是否具备运行条件、正在等待哪个事件，以及它应属于哪个 runnable/wait 集合。Wakeup 只解除等待并恢复调度资格；没有 scheduler/dispatch 不能直接从 Blocked 跳到 Running。

### 调度计算先写 Candidate / Key / Decision / Tie / Preemption

画甘特图前先固定五件事：当前候选集是谁、比较键是什么、在哪些决策点重算、同键怎样破平局、运行中键变化/新到达是否允许抢占。题目未说明同刻到达与时间片耗尽的先后时，要显式声明约定并全程一致，不能把某个模拟器默认顺序当算法定义。

### 切换计数先问“到底在数什么”

出现“切换次数/开销”时先区分：调度决策次数、真正换执行实体的 context-switch event、保存/恢复动作、用户/内核模式转换、地址空间切换。系统调用或中断可以只有 mode entry/return；scheduler 也可能再次选中原实体，不能把这些量机械画等号。

### IPC 先定对象、容量和等待语义

先判断传的是共享状态、字节流/消息还是事件通知，再标通信对象在哪里、是否有容量、send/read/write/receive 在什么条件下阻塞、数据/通知是否会被消费或保留。不要用“共享内存最快”“管道自动同步”“signal 会排队”一类绝对口诀替代接口条件。

### completion 不等于 running

设备完成通常只使等待条件成立并让 task 变为 runnable；何时获得 CPU 仍由调度决定。

### `fork()` 综合题逐对象标 Copy / Share / Reference / Rebuild

不要写一句“子进程复制父进程”。至少分别检查 process identity、execution context、private/shared mapping、fd binding、OFD/open instance 与 file object；随后对 write/close/read/exec 逐项指出哪一层真正发生分化。相同 fd 数字不能推出共享 offset，真正判据是是否引用同一 OFD。

### Blocking `read()` 同时画 Control / File / Data / Completion 四条线

先用 `fd -> OFD -> file range` 定位本次读什么，再问内容是否已 resident/cached；只有确实需要 I/O 且 blocking 语义要求等待时，task 才进入 wait relation。I/O completion 先更新 request/data 状态并使 waiter Ready，之后 scheduler 才决定何时恢复 syscall 并返回。

### translation、fault、replacement 三分

虚拟内存题先判断地址翻译是否命中、页面是否驻留、是否需要选择 victim，不能看到页号就直接执行置换算法。

### 页框题先拆“配额”和“victim 范围”

看到 fixed/variable、local/global 时先画两条轴：每个进程有多少页框，以及 victim 能从谁的驻留页中选择。只改变其中一条时，不连带假设另一条也改变。

### 工作集与 PFF 分别看“集合”和“反馈”

给引用窗口时统计窗口内不同页面；给缺页率上下界时按反馈方向调节页框。若题目只给某一时刻的工作集总和，不直接断言系统已经颠簸，还要看是否持续、是否真的产生高频换入换出。

### 管程题先写共享谓词，再写 wait/signal

先写受 mutex 保护的条件谓词；等待方用 `while (!predicate) wait(cv, m)`，并检查 wait 是否原子释放锁且返回前重新获得锁。修改方先改变共享状态，再通知等待者。

### `signal(cv)` 与 `V(S)` 不按“都会唤醒”互换

先问同步状态由谁拥有：信号量的 V 会增加许可并可保存；条件变量 signal 只通知等待队列，条件本身仍由共享变量拥有。用队列为空的场景检查两者是否被误当成同义操作。

### 单类资源最小量公式先过假设门

只有一类同质可重用资源、每个进程给出最大需求、获得全部后完成并释放时，才考虑 `sum(max_i - 1) + 1`。出现多类资源或 Allocation/Need 矩阵，立即切回 Banker 安全序列。

### DMA 题追踪 mapping 生命周期

按 `prepare -> map/pin -> submit -> complete/sync -> unmap/unpin` 检查。题目出现虚拟连续但物理离散时，再判断 scatter-gather 或 bounce buffer；不要默认 DMA address 就是 CPU 物理地址。

### I/O 综合题同时画三条线

分别追踪数据路径、控制/完成路径和 task 状态路径。中断驱动描述完成发现方式，DMA 描述搬运者，blocking/non-blocking 描述调用线程行为，三者不能互相推出。

### 设备题先分“名字、驱动类别、具体实例”

出现 major/minor 时，先写 major 选择驱动/类别、minor 由驱动解释具体实例；不要与总线 master/slave 的发起者/响应者关系混淆。

### 缓冲池题按 buffer 状态迁移模拟

不要只背空闲、输入、输出队列名称。每一步写清 buffer 当前 Owner、内容是否有效、进入哪个队列、谁因此阻塞或被唤醒。

### 磁盘地址题保持三层编号

分别标出文件内 LBN、设备 LBA 和题设物理位置。只有题目明确给出固定映射时才做 CHS 换算；不能由 LBA 连续直接推出真实介质物理连续。

### 文件题先判断入口是 pathname 还是 fd

pathname 先走目录/命名解析；fd 先走 `fd -> OFD -> object`。涉及 I/O 次数时先写缓存假设，再计算目录、索引块和数据块访问，不能把内存 dentry 与磁盘目录项混为一项。

## 已否定

### “工作集总和超过物理内存，当且仅当系统已经颠簸”

已否定。它只能提示持续负载下的高风险；是否已经颠簸还取决于实际驻留、访问轨迹、调度与缺页行为。

### “DMA pinning 就是在所有 PTE 中设置固定 Pinned 位”

已否定。稳定要求是 DMA-visible mapping 在传输生命周期内有效且不可被错误回收；具体 pin/accounting 位置属于实现细节。
