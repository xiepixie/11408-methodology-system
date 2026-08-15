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

### completion 不等于 running

设备完成通常只使等待条件成立并让 task 变为 runnable；何时获得 CPU 仍由调度决定。

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
