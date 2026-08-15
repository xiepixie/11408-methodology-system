---
title: 链式队列
source: https://www.codebrick.tech/ds-full/posts/stack-queue/queue.html
---

# 链式队列

## 大纲定位

本篇对应 2026 大纲 **三、栈、队列和数组 →（三）栈和队列的链式存储结构**。

这一条目由两篇分担：《[链栈](./linked-stack.html)》负责**栈**的链式实现， **本篇负责队列的链式实现**。

与其他相关篇的边界：

- 队列的**顺序存储**（假溢出、循环队列、队空队满三方案）在《[循环队列](./circular-queue.html)》里， 属大纲三（二），本篇只在对比表里引用其结论；
- 队列的**逻辑定义与 FIFO 性质**在《[栈和队列的基本概念](./concepts.html)》里，属三（一）。

本篇要交付的核心能力：**说清链队为什么需要两个指针，以及"删到最后一个元素"这个边界为什么必须特判**。

## 知识框架

## 核心思想

链式队列的三条核心特点：

- **FIFO**：只能从队尾（`rear`）插入、从队头（`front`）删除；
- **必须两个指针**：`front` 指向队头（或头结点），`rear` 指向队尾结点。 只留一个指针不行——单链表无法回退，光有 `front` 找队尾要 O(n)， 光有 `rear` 找队头同样要 O(n)；
- **通常带头结点**：让空队列与非空队列的入队、出队走同一条代码路径。

**对照链栈记**：链栈只在表头一端操作，**一个 `top` 就够**，而且**不需要头结点**； 链队在两端操作，**必须两个指针**，而且**带头结点更划算**。 差异的唯一根源是"操作发生在几端"。

结点与队列的定义：c

```
// 链式队列结点
typedef struct LinkNode {
    int data;
    struct LinkNode *next;
} LinkNode;

// 链式队列（带头结点）
typedef struct {
    LinkNode *front;  // 队头指针，始终指向头结点
    LinkNode *rear;   // 队尾指针，指向最后一个数据结点
} LinkQueue;
```

队列状态示意：text

```
空队列:   front → [头结点] ← rear
                   next = NULL

非空队列: front → [头结点] → [a₁] → [a₂] → [a₃] ← rear
                                              next = NULL
```

**判空条件**：`Q.front == Q.rear`（两者都指向头结点）。 注意这个条件与《[循环队列](./circular-queue.html)》方案一的判空**长得一样但含义完全不同**： 那里比较的是两个数组下标，这里比较的是两个地址；而且链队**不存在"满"**， 所以 `front == rear` 没有二义性，不需要牺牲单元、不需要 `tag`。

## 初始化与判空
c

```
bool InitQueue(LinkQueue *Q) {
    Q->front = Q->rear = (LinkNode *)malloc(sizeof(LinkNode));  // 建头结点
    if (Q->front == NULL) return false;
    Q->front->next = NULL;
    return true;
}

bool QueueEmpty(LinkQueue Q) {
    return Q.front == Q.rear;
}
```

初始化里**两个指针都指向头结点**，这一步和判空条件是配套的，改一个必须改另一个。

## 交互可视化

通过下方的交互动画，你可以逐步观察链式队列的执行过程：加载可视化中...

## 操作详解

### 入队操作

在队尾插入新元素，需要修改 `rear` 指针。c

```
// 入队（带头结点）
bool EnQueue(LinkQueue *Q, int x) {
    LinkNode *s = (LinkNode *)malloc(sizeof(LinkNode));
    if (s == NULL) return false;   // 内存分配失败——链队唯一的失败来源
    s->data = x;
    s->next = NULL;                // 新结点将成为队尾，next 必须置空
    Q->rear->next = s;             // 挂到当前队尾之后
    Q->rear = s;                   // 队尾指针后移
    return true;
}
```

**`s->next = NULL` 不能省**：`malloc` 出来的内存内容是未定义的，如果不显式置空， `rear->next` 会是一个随机值，后续遍历或出队判断（`p->next`）就会踩到野指针。

**带头结点的好处正体现在这里**：即使队列是空的（`front == rear ==` 头结点）， `Q->rear->next = s` 也是合法的——它把新结点挂在头结点后面，逻辑上就是队头。 **不需要 `if (队空)` 的特判**，空队列与非空队列走完全相同的代码。

### 出队操作

删除队头元素（头结点之后的第一个结点）。**关键边界：如果删掉的正是最后一个元素， `rear` 会指向一块被释放的内存，必须把它拉回头结点。**c

```
// 出队（带头结点）
bool DeQueue(LinkQueue *Q, int *x) {
    if (Q->front == Q->rear) return false;  // 队空
    LinkNode *p = Q->front->next;           // p 指向队头元素
    *x = p->data;
    Q->front->next = p->next;               // 头结点跳过 p
    if (Q->rear == p)                       // ◆ 原队列只有一个数据结点
        Q->rear = Q->front;                 //   rear 指回头结点，恢复"空队列"形态
    free(p);
    return true;
}
```

**为什么必须有 ◆ 这一句**——给一个具体反例：

设队列中只有一个元素 `a₁`，此时 `front` 指头结点 `H`，`rear` 指 `a₁`，`H->next = a₁`。

| 步骤 | 若**漏写** ◆ 的状态 |
| --- | --- |
| `p = front->next` | `p = a₁` |
| `front->next = p->next` | `H->next = NULL`，链表已空 |
| `free(p)` | `a₁` 所在内存被归还 |
| 结果 | `front == H`、`rear` **仍指向已释放的 `a₁`**，且 `front != rear`，**判空返回"非空"** |
| 下一次 `EnQueue` | 执行 `Q->rear->next = s`，即**向已释放内存写入**——未定义行为 |
| 下一次 `DeQueue` | `front != rear` 通过判空，`p = front->next = NULL`，随后 `*x = p->data` **空指针解引用** |

补上 ◆ 之后：`rear = front = H`，判空恢复为真，队列回到与 `InitQueue` 之后完全相同的形态。

这个边界在**顺序存储的循环队列里不存在**——那里 `front`、`rear` 是下标， 出队只是 `front` 前进一格，不会有"指向已释放内存"的问题。 **链式结构的边界风险来自 `free`**，这是它与顺序结构最本质的差异之一。

### 取队头元素
c

```
bool GetHead(LinkQueue Q, int *x) {
    if (Q.front == Q.rear) return false;
    *x = Q.front->next->data;    // 头结点的下一个才是队头元素
    return true;
}
```

**是 `front->next->data` 而不是 `front->data`**——头结点不存数据，这是带头结点写法最常见的笔误。

### 不带头结点的写法（对照）

不设头结点时，`front` 直接指向队头元素，空队列用 `front == NULL` 表示。 代价是**入队和出队各多一个特判**：c

```
bool InitQueue_NH(LinkQueue *Q) { Q->front = Q->rear = NULL; return true; }

bool QueueEmpty_NH(LinkQueue Q) { return Q.front == NULL; }

bool EnQueue_NH(LinkQueue *Q, int x) {
    LinkNode *s = (LinkNode *)malloc(sizeof(LinkNode));
    if (s == NULL) return false;
    s->data = x; s->next = NULL;
    if (Q->front == NULL)          // ◆ 空队列：新结点既是队头也是队尾
        Q->front = Q->rear = s;
    else {
        Q->rear->next = s;
        Q->rear = s;
    }
    return true;
}

bool DeQueue_NH(LinkQueue *Q, int *x) {
    if (Q->front == NULL) return false;      // 队空
    LinkNode *p = Q->front;
    *x = p->data;
    Q->front = p->next;
    if (Q->rear == p)              // ◆ 删的是最后一个元素
        Q->rear = NULL;            //   两个指针一起归零
    free(p);
    return true;
}
```

对比两种写法，**头结点买到的是"入队不用特判空队列"**（少一个 `if`）， **没能买到的是"出队不用特判删最后一个"**——那个 `if` 两种写法都躲不掉， 只是重置的目标不同（带头结点是 `rear = front`，不带是 `rear = NULL`）。

**常见误解**：以为"带头结点就不用管边界了"。实际上带头结点消除的是**空队列入队**这一个边界， **队列变空**那个边界依然存在。

### 用带尾指针的循环链表表示队列

还有一种常见变体：**只用一个 `rear` 指针**，把链表做成**带头结点的循环单链表**， `rear` 指向队尾结点，`rear->next` 就是头结点，`rear->next->next` 就是队头元素。text

```
        ┌──────────────────────────────┐
        ↓                              │
      [头结点] → [a₁] → [a₂] → [a₃] ───┘
                                 ↑ rear
```

- 入队：在 `rear` 之后插入，再 `rear = s`，O(1)；
- 出队：`p = rear->next->next`（队头元素），改 `rear->next->next = p->next`， 若删的是最后一个则 `rear = rear->next`（指回头结点），O(1)。

**好处**：只需保存一个指针，两端操作仍都是 O(1)。原因是循环结构让"从队尾一步走到队头" 成为可能，抵消了单链表不能回退的限制。c

```
// 带头结点的循环单链表表示队列，只保存 rear
typedef LinkNode *CQueue;    // rear 指针本身就是整个队列

bool InitCQueue(CQueue *rear) {
    LinkNode *h = (LinkNode *)malloc(sizeof(LinkNode));   // 头结点
    if (h == NULL) return false;
    h->next = h;             // 自己指向自己：空队列
    *rear = h;               // 队空时 rear 指向头结点
    return true;
}

bool CQueueEmpty(CQueue rear) {
    return rear->next == rear;      // 只有头结点
}

bool EnCQueue(CQueue *rear, int x) {
    LinkNode *s = (LinkNode *)malloc(sizeof(LinkNode));
    if (s == NULL) return false;
    s->data = x;
    s->next = (*rear)->next;        // 新结点接到头结点前（即环回去）
    (*rear)->next = s;              // 挂到当前队尾之后
    *rear = s;                      // 队尾后移
    return true;
}

bool DeCQueue(CQueue *rear, int *x) {
    if ((*rear)->next == *rear) return false;   // 队空
    LinkNode *h = (*rear)->next;                // 头结点
    LinkNode *p = h->next;                      // 队头元素
    *x = p->data;
    h->next = p->next;                          // 头结点跳过 p
    if (*rear == p)                             // ◆ 删的是最后一个数据结点
        *rear = h;                              //   rear 指回头结点
    free(p);
    return true;
}
```

**注意 `EnCQueue` 里 `s->next = (*rear)->next;` 这一句**：`(*rear)->next` 永远是头结点， 所以新结点自动"环回去"，环不会断。**这一句写反（先 `(*rear)->next = s`）同样会造成自环**， 与《[链栈](./linked-stack.html)》里头插法的坑一模一样。

**出队里的 ◆ 依然躲不掉**——删掉最后一个数据结点后 `rear` 会悬空， 必须指回头结点。**换成循环链表并没有消除这个边界，只是省掉了一个指针。**

## 复杂度分析

| 操作 | 时间复杂度 | 来历 |
| --- | --- | --- |
| 入队 | O(1) | 一次 `malloc` + 两次指针赋值，与队列长度 n 无关（**因为保存了 `rear`**） |
| 出队 | O(1) | 一次判空 + 常数次指针操作 + 一次 `free` |
| 取队头 | O(1) | 直接访问 `front->next->data` |
| 判空 | O(1) | 一次指针比较 |
| 求队长 | O(n) | 需从队头遍历到 `NULL`，除非额外维护计数器 |

**如果不保存 `rear`**，入队就要从 `front` 走到表尾，变成 O(n)—— 这正是"链队必须两个指针"的量化理由。

**空间复杂度**：n 个元素占 n 个结点（带头结点则是 n+1 个）， 每个结点比顺序存储多一个指针域。设 `int` 与指针各占 4 字节， **存储密度 =4/8=1/2**；顺序存储的存储密度是 1。 单次操作的辅助空间 O(1)。

## 链式队列 vs 循环队列

| 对比项 | 循环队列（顺序） | 链式队列 |
| --- | --- | --- |
| 容量 | 预分配 `MaxSize`，固定 | 按需分配，无固定上限 |
| 队满 | **会发生**（三种判别方案见对应篇） | **不会**，只可能 `malloc` 失败 |
| 假溢出 | 靠取模绕回解决 | 天然不存在 |
| 判空 | 方案一 `front == rear`（下标比较） | `front == rear`（地址比较）或 `front == NULL` |
| 是否需要牺牲单元 | 方案一需要，容量 `MaxSize-1` | 不需要 |
| 指针个数 | 2 个下标 | 2 个指针（或 1 个 `rear` + 循环链表） |
| 存储密度 | 1 | <1 |
| 求队长 | O(1) | O(n)（除非另设计数器） |
| 缓存性能 | 好（连续存储） | 差（结点分散） |
| 适用场景 | 容量可预估（如调度队列、缓冲区） | 容量波动大或完全不可预估 |

严蔚敏教材对选择标准的表述是："如果用户的应用程序中设有循环队列，则必须为它设定一个最大队列长度； 若用户无法预估所用队列的最大长度，则宜采用链队。"

## 易混淆知识点

| 对比项 | 情况 A | 情况 B | 判别依据 |
| --- | --- | --- | --- |
| 判空条件 | 带头结点：`front == rear` | 不带头结点：`front == NULL` | 看 `front` 指的是头结点还是队头元素 |
| 取队头元素 | 带头结点：`front->next->data` | 不带头结点：`front->data` | 头结点不存数据，必须多跳一步 |
| 入队是否特判空队列 | 带头结点：**不需要** | 不带头结点：**需要**（`front`、`rear` 同时置为新结点） | 空队列时 `rear` 是否是一个可安全解引用的结点 |
| 出队是否特判"删最后一个" | **两种写法都需要** | — | 删完 `rear` 会悬空，带头结点重置为 `front`，不带则重置为 `NULL` |
| 链队 `front == rear` vs 循环队列 `front == rear` | 链队：**只可能是空**，无二义 | 循环队列方案一：也是空，但那是**牺牲一格换来的** | 链队根本没有"满"，所以不存在二义性 |
| 链队 vs 链栈的指针数 | 链队：2 个（或 1 个 `rear` + 循环链表） | 链栈：1 个 `top` | 操作发生在几端 |
| 链队 vs 链栈的头结点 | 链队：**通常带**（省掉入队特判） | 链栈：**通常不带**（没有可省的特判） | 头结点能否真正消除某个边界分支 |
| 求队长复杂度 | 循环队列 O(1) | 链队 O(n) | 有没有能直接算出个数的量 |
| `s->next = NULL` | 入队时必须写 | 漏写 → `rear->next` 是随机值 | `malloc` 不清零 |

## 本节小结

学完本篇，你应该能够：

- 解释链队**为什么必须两个指针**，并给出量化理由：只保留 `front` 时入队要遍历到表尾， 退化为 O(n)；
- 写出带头结点的 `InitQueue` / `QueueEmpty` / `EnQueue` / `DeQueue` / `GetHead`， 五个函数的口径互相一致；
- **说清"删掉最后一个元素后必须 `rear = front`"的后果**：漏写会让 `rear` 指向已释放内存， 下一次入队向野指针写、下一次出队空指针解引用——能把这条反例完整讲一遍；
- 写出不带头结点的对照版本，并准确指出头结点消除的是**入队时的空队列特判**， 而**队列变空的特判两种写法都躲不掉**；
- 描述"带尾指针的循环单链表表示队列"的结构，并说明它为什么能用一个指针做到两端 O(1)；
- 从容量、队满、假溢出、存储密度、求队长五个维度对比链队与循环队列，并给出选型标准。

三个最关键的结论：

- **两个指针是链队的结构性要求**，不是实现偏好；
- **`if (rear == p) rear = front;` 是链队出队的必答项**，它修的是一个会导致未定义行为的悬空指针；
- **链队没有"满"**，所以 `front == rear` 不存在循环队列那种二义性。

## 教材出处

- 链队的存储结构（`QNode` + `LinkQueue`，含 `front` / `rear` 两个指针）与 "给链队添加一个头结点，并令头指针始终指向头结点"的口径： 严蔚敏《数据结构（C 语言版）》（第 2 版）**p73**「3.5.3 链队——队列的链式表示和实现」
- "若用户无法预估所用队列的最大长度，则宜采用链队"：同书 **p73**
- 入队算法 3.17（分配结点 → 置数据域 → 插入队尾 → 修改队尾指针）：同书 **p74**
- 出队算法 3.18 与其第 ④ 步"判断出队元素是否为最后一个元素，若是，则将队尾指针重新赋值， 指向头结点"，以及正文"在链队出队操作时还要考虑当队列中最后一个元素被删后， 队列尾指针也丢失了"：同书 **p75**
- 取队头算法 3.19：同书 **p75**

## 相关知识

- [循环队列](./circular-queue.html)：队列的顺序存储实现，通过取模解决假溢出；两篇是同一逻辑结构的两种落地
- [链栈](./linked-stack.html)：同属大纲三（三），对比可看清"操作端数"如何决定指针个数与头结点取舍
- [栈和队列的基本概念](./concepts.html)：队列的 ADT 与"出队序列唯一"的性质
- [单链表](./../linear/singly-linked-list.html)：链队的入队/出队就是单链表的尾插与删首结点
- [广度优先搜索](./../graph/bfs.html)：队列的典型使用者，每一层结点依次入队出队驱动逐层遍历
- [二叉树的层次遍历](./../tree/level-order-traversal.html)：同样由队列驱动，是本篇最直接的应用

### 相关文章

- [[02_数据结构_DS/stack-queue/concepts.md|栈和队列基本概念]]
- [[02_数据结构_DS/stack-queue/sequential-stack.md|顺序栈]]
- [[02_数据结构_DS/stack-queue/shared-stack.md|共享栈]]
- [[02_数据结构_DS/stack-queue/linked-stack.md|链栈]]
- [[02_数据结构_DS/stack-queue/circular-queue.md|循环队列]]
- [[02_数据结构_DS/stack-queue/deque.md|双端队列]]
- [[02_数据结构_DS/stack-queue/bracket-matching.md|应用：括号匹配]]
- [[02_数据结构_DS/stack-queue/expression-eval.md|应用：表达式求值]]
- [[02_数据结构_DS/stack-queue/recursion.md|应用：栈在递归中的应用]]
- [[02_数据结构_DS/stack-queue/array-storage.md|多维数组的存储]]
- [[02_数据结构_DS/stack-queue/special-matrix.md|特殊矩阵的压缩存储]]

### 交互体验
[ 前往完整可视化页面 → ](https://codebrick.tech/ds-visual/visual/stack-queue/queue)

## 真题练习

### 相关真题（6题）
[2019Q4210分](https://www.codebrick.tech/practice/q/ds-2019-42?ctx=ds-2019-42,ds-2018-02,ds-2016-03,ds-2014-03,ds-2011-03,ds-2009-01)[2018Q22分](https://www.codebrick.tech/practice/q/ds-2018-02?ctx=ds-2019-42,ds-2018-02,ds-2016-03,ds-2014-03,ds-2011-03,ds-2009-01)[2016Q32分](https://www.codebrick.tech/practice/q/ds-2016-03?ctx=ds-2019-42,ds-2018-02,ds-2016-03,ds-2014-03,ds-2011-03,ds-2009-01)[2014Q32分](https://www.codebrick.tech/practice/q/ds-2014-03?ctx=ds-2019-42,ds-2018-02,ds-2016-03,ds-2014-03,ds-2011-03,ds-2009-01)[2011Q32分](https://www.codebrick.tech/practice/q/ds-2011-03?ctx=ds-2019-42,ds-2018-02,ds-2016-03,ds-2014-03,ds-2011-03,ds-2009-01)[2009Q12分](https://www.codebrick.tech/practice/q/ds-2009-01?ctx=ds-2019-42,ds-2018-02,ds-2016-03,ds-2014-03,ds-2011-03,ds-2009-01)