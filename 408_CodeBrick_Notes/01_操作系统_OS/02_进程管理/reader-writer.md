---
title: 读者-写者问题 ​
source: https://www.codebrick.tech/os-blog/posts/process/reader-writer.html
---

# 读者-写者问题

2026 大纲 **二（三）6 经典同步问题**的读者-写者部分（生产者-消费者见《[[01_操作系统_OS/02_进程管理/producer-consumer.md|生产者-消费者问题]]》）。

## 速查

| **问题定义** | 保证**一个 Writer 进程必须与其他进程互斥地访问共享对象**；教材说它常被用来测试新的同步原语 |
| --- | --- |
| **半互斥三行** | 读-读**不互斥**（都不改数据）；读-写互斥（会读到只写了一半的数据）；写-写互斥（修改互相覆盖） |
| 🔴 **一个普通信号量表达不了半互斥** | `mutex = 1` 会把读者之间也互斥掉，`mutex = N` 又挡不住写者。破局思路：**不让单个读者去争锁，而让"读者这一整群"作为整体去和写者争锁** ⇒ 需要计数器 `readcount` |
| **基准方案两个信号量** | `rw_mutex = 1`（读者群与写者之间、写者与写者之间）、`mutex = 1`（保护 `readcount`） |
| 🔴 **第一个读者 P、最后一个读者 V** | `rw_mutex` 锁的是"**一群**"而非单个读者：第一个进场时替全群挡住写者，后来者发现已有人读就直接进。若每个读者都 `P(rw_mutex)`，读者之间就互斥了。判据：**看这个信号量代表的是"一个进程"还是"一群进程"的进入权** |
| 🔴 **"改计数 + 判断"必须整体在 mutex 里** | 拆开会出两种错：两人都读到旧值 0 都以为自己是第一个（各 P 一次 → **读者之间被互斥**）；或两人都在对方 `++` 之后读值都以为自己不是第一个（**写者能在有人读时进场**） |
| 🔴 **读操作在 mutex 之外** | `V(mutex)` 在读操作**之前**就执行——`mutex` 只保护 `readcount` 这个变量，不保护读操作本身，**这正是多读者能并行的原因**。圈进去方案就退化成普通互斥 |
| **教材写法与本文等价** | 教材作 `wait(rmutex); if (readcount==0) wait(wmutex); readcount++; signal(rmutex);`——先判断是否为 0 再自增，与"先自增再判断是否为 1"是同一件事。**只要"判断 + 修改"整体在 rmutex 里，先后无所谓** |
| 🔴 **三种方案共享同一套骨架** | `readcount` + "第一个 P、最后一个 V"一字未改，差别**只在有没有闸门、闸门何时关**：读者优先**不挡**→ 写者饥饿；写者优先加 `readTry`，**写者一到就关**→ 读者饥饿；读写公平加 `w`，**谁先到谁先过**→ 都不饿 |
| 🔴 **公平方案里两个 `V(w)` 位置相反** | **读者提前 `V(w)`**（读者本就该并行，读完才放会让读者在 `w` 上串行）；**写者写完才 `V(w)`**（写者本就独占，提前放开只会让下一个请求空转排队，排队意义没了）。判据：**问这个角色本身是否允许并行** |
| **同构模式用了两次** | 写者优先里 `writecount` + `mutexW` + `readTry` 与读者那边 `readcount` + `mutexR` + `rw_mutex` 完全同构——**"第一个进的人替整群关门，最后一个出的人替整群开门"**。记住这条，两段代码都不用背 |

## 交互可视化
加载可视化中...

## 一、读者优先方案

```
semaphore rw_mutex = 1;   // 读者群与写者之间、写者与写者之间的互斥
semaphore mutex    = 1;   // 保护 readcount 这个共享变量
int readcount = 0;        // 当前正在读的进程数

// 写者进程
writer() {
    do {
        P(rw_mutex);      // 申请独占权
        perform write operation;
        V(rw_mutex);
    } while (TRUE);
}

// 读者进程
reader() {
    do {
        P(mutex);             // 保护 readcount
        readcount++;
        if (readcount == 1)   // 我是第一个读者
            P(rw_mutex);      //   替整群读者把写者挡在门外
        V(mutex);

        perform read operation;   // 多个读者可以同时读

        P(mutex);
        readcount--;
        if (readcount == 0)   // 我是最后一个读者
            V(rw_mutex);      //   放行写者
        V(mutex);
    } while (TRUE);
}
```

**它的代价是写者饥饿**：只要新读者源源不断到达，`readcount` 就始终不为 0，`V(rw_mutex)` 永远不执行。判据是——写者能不能进场取决于 `readcount` 会不会归零，而**没有任何机制阻止新读者加入**，所以只要读者到达率足够高，写者饥饿必然发生。要补救就必须找地方**挡住后来的读者**，三种方案的差别全在"挡在哪里"。

## 二、写者优先方案

思路：**写者一到，就先把"读者入口"关上**，已经在读的读者读完即可，新读者一律拦在门外。

```
semaphore rw_mutex = 1;   // 读写互斥（同上）
semaphore mutexR   = 1;   // 保护 readcount
semaphore mutexW   = 1;   // 保护 writecount
semaphore readTry  = 1;   // 读者入口闸门：有写者在就关上
int readcount = 0, writecount = 0;

writer() {
    do {
        P(mutexW);
        writecount++;
        if (writecount == 1)  P(readTry);   // 第一个写者关闭读者闸门
        V(mutexW);

        P(rw_mutex);
        perform write operation;
        V(rw_mutex);

        P(mutexW);
        writecount--;
        if (writecount == 0)  V(readTry);   // 最后一个写者打开读者闸门
        V(mutexW);
    } while (TRUE);
}

reader() {
    do {
        P(readTry);           // 闸门关着就进不来
        P(mutexR);
        readcount++;
        if (readcount == 1)  P(rw_mutex);
        V(mutexR);
        V(readTry);           // 立即放开闸门，不阻塞后面的读者

        perform read operation;

        P(mutexR);
        readcount--;
        if (readcount == 0)  V(rw_mutex);
        V(mutexR);
    } while (TRUE);
}
```

写者一到就把 `readTry` 拿走，此后新读者全部卡在 `P(readTry)`，`readcount` 因此能归零、写者随即拿到 `rw_mutex`；而只要还有写者排队（`writecount > 0`），闸门就一直关着。代价是轮到**读者饥饿**。穷举检验（2 个读者 + 2 个写者的完整交错）：可达状态 4056，死锁态 **0**，"写者与读者同时在临界区"或"两个写者同时在临界区"的状态 **0**。

## 三、读写公平方案

思路取中：**读者和写者都在同一个信号量 `w` 上排队，先到先得**。

```
semaphore rw_mutex = 1;
semaphore mutex    = 1;
semaphore w        = 1;   // 公共排队闸门
int readcount = 0;

writer() {
    P(w);
    P(rw_mutex);
    perform write operation;
    V(rw_mutex);
    V(w);
}

reader() {
    P(w);                 // 和写者在同一条队上排
    P(mutex);
    readcount++;
    if (readcount == 1)  P(rw_mutex);
    V(mutex);
    V(w);                 // 立即释放，不挡住已在读的同伴

    perform read operation;

    P(mutex);
    readcount--;
    if (readcount == 0)  V(rw_mutex);
    V(mutex);
}
```

写者一旦在 `w` 上排上队，后到的读者就被挡在 `P(w)` 前、接不上 `readcount`；当前这批读者读完后 `readcount` 归零，写者获得机会。

## 四、三种方案的完整矩阵

|  | 读者优先 | 写者优先 | 读写公平 |
| --- | --- | --- | --- |
| 新增信号量 | 无（基准方案） | `mutexW`、`readTry` + 变量 `writecount` | `w` |
| 挡住后来读者的地方 | **不挡** | 有写者时挡在 `P(readTry)` | 有人排队时挡在 `P(w)` |
| 写者到达后要等多久 | 可能**无限期**（`readcount` 不归零） | 当前这批读者读完即可 | 排在它前面的那些请求完成即可 |
| 谁会饥饿 | **写者** | **读者** | 都不会 |
| 读的吞吐量 | 最高 | 最低 | 居中 |
| 判据：什么时候选它 | 读远多于写，且写可以推迟（如缓存统计） | 写的时效性关键，数据必须尽快更新（如配置下发） | 两类请求都不能长期饿着（通用场景） |

变形：最多允许 RN 个读者同时读，用信号量集怎么写（想看"测试而不占用"这一能力怎么用时展开）

实际系统常给并发读数设一个上限（避免读者太多把写者拖垮）。教材用[[01_操作系统_OS/02_进程管理/semaphore.md|信号量集]]给出这个变形：引入信号量 `L`，初值为 `RN`，读者进入前执行 `Swait(L, 1, 1)` 使 `L` 减 1；当 `RN` 个读者进入后 `L` 减为 0，第 `RN+1` 个读者会因 `Swait(L, 1, 1)` 失败而阻塞。

```
int RN;                          // 允许的最大并发读者数
semaphore L = RN, mx = 1;

void reader() {
    do {
        Swait(L, 1, 1);          // 占一个读名额
        Swait(mx, 1, 0);         // 只测试 mx >= 1，不占用它（d = 0）
        perform read operation;
        Ssignal(L, 1);           // 归还名额
    } while (TRUE);
}

void writer() {
    do {
        Swait(mx, 1, 1; L, RN, 0);   // 要求 mx>=1 且占用它；同时要求 L 达到满额 RN 但不占用
        perform write operation;
        Ssignal(mx, 1);
    } while (TRUE);
}
```

两处用到了信号量集的特殊形态：

| 写法 | 含义 | 起什么作用 |
| --- | --- | --- |
| `Swait(mx, 1, 0)`（读者） | 只测试 `mx ≥ 1`，**不占用**（d=0） | 就是那个"**可控开关**"：没有写者时（`mx = 1`）允许多个读者通过；写者占走 `mx` 后（`mx = 0`）后续读者全被挡住 |
| `Swait(mx, 1, 1; L, RN, 0)`（写者） | 占用 `mx`；同时要求 `L` 恢复到满额 `RN` 但不占用它 | `L = RN` 等价于"当前一个读者也没有"，写者靠这一条确认读者全部退场 |

这个变形把"**测试而不占用**"这一能力用到了极致——普通记录型信号量做不到"多个进程同时通过同一个初值为 1 的信号量"。

## 本节小结

- 半互斥（读-读不互斥、读-写与写-写互斥）**一个普通信号量表达不了**，破局思路是让"读者整群"作为整体去和写者争锁，因此引入 `readcount`：**第一个读者 `P(rw_mutex)`、最后一个读者 `V(rw_mutex)`**。
- 两处最容易写错：**"改计数 + 判断"必须整体放在 mutex 里**（否则两人都以为自己是第一个、或都以为自己不是第一个），而**读操作必须在 mutex 之外**（这是多读者能并行的前提）。
- 三种方案共享同一套骨架，差别只在**有没有闸门、闸门何时关**：不挡 → 写者饥饿；`readTry` 写者一到就关 → 读者饥饿；`w` 先到先得 → 都不饥饿。公平方案里读者提前 `V(w)`、写者写完才 `V(w)`，判据是这个角色本身是否允许并行。教材出处

- **问题定义与记录型信号量解法**：汤小丹《计算机操作系统》2.5.3 节，印刷 p65——"允许多个进程同时读一个共享对象……但不允许一个 Writer 进程和其他 Reader 进程或 Writer 进程同时访问共享对象"；"读者-写者问题常被用来测试新同步原语"。代码为 `semaphore rmutex=1, wmutex=1; int readcount=0;`，读者段写作 `wait(rmutex); if(readcount==0) wait(wmutex); readcount++; signal(rmutex);`。
- **带 RN 上限的信号量集解法**：同书印刷 p66——"增加了一个限制，即最多只允许 RN 个读者同时读。为此，又引入了一个信号量 L，并赋予其初值为 RN"，代码为读者 `Swait(L,1,1); Swait(mx,1,0);`、写者 `Swait(mx,1,1; L,RN,0);`。
- **`Swait(S,1,0)` 是可控开关**：同书 2.4.3 节，印刷 p55。

## 相关知识

[[01_操作系统_OS/02_进程管理/producer-consumer.md|生产者-消费者问题]]｜[[01_操作系统_OS/02_进程管理/dining-philosophers.md|哲学家进餐问题]]｜[[01_操作系统_OS/02_进程管理/semaphore.md|信号量]]

## 真题练习

### 相关真题（3题）
[2019Q438分](https://www.codebrick.tech/practice/q/os-2019-43?ctx=os-2019-43,os-2014-47,os-2009-45)[2014Q478分](https://www.codebrick.tech/practice/q/os-2014-47?ctx=os-2019-43,os-2014-47,os-2009-45)[2009Q457分](https://www.codebrick.tech/practice/q/os-2009-45?ctx=os-2019-43,os-2014-47,os-2009-45)[[01_操作系统_OS/02_进程管理/producer-consumer.md|上一篇生产者-消费者问题]][[01_操作系统_OS/02_进程管理/dining-philosophers.md|下一篇哲学家进餐问题]]

### 相关文章

- [[01_操作系统_OS/02_进程管理/process-concept.md|进程基本概念]]
- [[01_操作系统_OS/02_进程管理/process-state.md|进程状态与转换]]
- [[01_操作系统_OS/02_进程管理/thread.md|线程（内核级与用户级）]]
- [[01_操作系统_OS/02_进程管理/process-control.md|进程的组织与控制]]
- [[01_操作系统_OS/02_进程管理/ipc.md|进程间通信]]
- [[01_操作系统_OS/02_进程管理/scheduling-concept.md|调度的基本概念与目标]]
- [[01_操作系统_OS/02_进程管理/fcfs.md|FCFS 先来先服务调度]]
- [[01_操作系统_OS/02_进程管理/sjf.md|SJF 短作业优先调度]]
- [[01_操作系统_OS/02_进程管理/rr.md|时间片轮转调度]]
- [[01_操作系统_OS/02_进程管理/priority.md|优先级调度]]
- [[01_操作系统_OS/02_进程管理/hrrn.md|高响应比优先调度]]
- [[01_操作系统_OS/02_进程管理/multi-level-queue.md|多级队列调度]]
- [[01_操作系统_OS/02_进程管理/mlfq.md|多级反馈队列调度]]
- [[01_操作系统_OS/02_进程管理/fair-scheduling.md|公平调度算法]]
- [[01_操作系统_OS/02_进程管理/scheduling-simulator.md|调度算法对比模拟器]]
- [[03_计算机组成原理_CO/cpu/multiprocessor.md|多处理机调度]]
- [[01_操作系统_OS/02_进程管理/context-switch.md|上下文切换机制]]
- [[01_操作系统_OS/02_进程管理/context-switch-simulator.md|上下文切换模拟器]]
- [[01_操作系统_OS/02_进程管理/sync-mutex-concept.md|同步与互斥基本概念]]
- [[01_操作系统_OS/02_进程管理/sync-impl.md|同步互斥实现方法]]
- [[01_操作系统_OS/02_进程管理/lock.md|锁]]
- [[01_操作系统_OS/02_进程管理/semaphore.md|信号量]]
- [[01_操作系统_OS/02_进程管理/condition-variable.md|条件变量]]
- [[01_操作系统_OS/02_进程管理/producer-consumer.md|生产者-消费者问题]]
- [[01_操作系统_OS/02_进程管理/dining-philosophers.md|哲学家进餐问题]]
- [[01_操作系统_OS/02_进程管理/deadlock-concept.md|死锁的概念与预防]]
- [[01_操作系统_OS/02_进程管理/banker.md|银行家算法]]
- [[01_操作系统_OS/02_进程管理/deadlock-detection.md|死锁检测与解除]]