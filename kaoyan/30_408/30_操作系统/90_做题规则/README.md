# 操作系统做题规则

状态：工作稿，待验证规则已建立，尚无已采用规则。

## 已采用

暂无。既有出版物中的检查表需要在真题和陌生题中重新验证。

## 待验证

### OS 首次定位链

```text
Resource / Abstraction
-> Objects / Relations / Queues
-> Event
-> Boundary
-> Mechanism
-> Policy
-> Invariant
-> Wait / Fault / Recovery
-> Cost
```

先区分底层资源与上层抽象，再按事件推进状态；只有存在多个合法候选时才引入 Policy。正常路径已经唯一且题目不问失败/性能时，在 `Invariant` 检查通过后停止，不机械展开慢路径与成本。

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
