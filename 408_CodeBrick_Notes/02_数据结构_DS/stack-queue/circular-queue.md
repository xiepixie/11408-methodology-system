---
title: 循环队列
source: https://www.codebrick.tech/ds-full/posts/stack-queue/circular-queue.html
---

# 循环队列

## 大纲定位

本篇对应 2026 大纲 **三、栈、队列和数组 →（二）栈和队列的顺序存储结构**， 是这一条目里**队列**那一半的全部内容，也是本章密度最高的一节。

分工边界：

- 同属三（二）的《[顺序栈](./sequential-stack.html)》《[共享栈](./shared-stack.html)》讲**栈**的顺序存储；
- 队列的**链式**实现在《[链式队列](./queue.html)》里，属于大纲三（三）；
- 队列的**逻辑定义与 FIFO 性质**在《[栈和队列的基本概念](./concepts.html)》里。

本篇要交付的能力有三件：**说清假溢出为什么会发生**、**说清 `% MaxSize` 为什么必要**、 **把队空队满的三种判别方案连同代码差异一次讲透**。第三件是这一章最容易只背结论的地方。

## 知识框架

## 从假溢出说起

队列用一组连续单元存放，另设两个整型量 `front`、`rear`。最朴素的约定（严蔚敏教材口径）是：

初始化时 `front = rear = 0`；每插入一个队尾元素 `rear` 加 1，每删除一个队头元素 `front` 加 1。 于是非空队列中 `front` 始终指向队头元素，`rear` 始终指向**队尾元素的下一个位置**。

问题出在"只增不减"上。设 `MaxSize = 6`，依次做：入队 6 个、出队 3 个、再入队 1 个。

| 时刻 | front | rear | 数组占用 | 说明 |
| --- | --- | --- | --- | --- |
| 初始 | 0 | 0 | `[_ _ _ _ _ _]` | 空 |
| 入队 6 个 | 0 | 6 | `[a b c d e f]` | `rear` 已越过数组末端 |
| 出队 3 个 | 3 | 6 | `[_ _ _ d e f]` | **前 3 格空出来了** |
| 再入队 1 个 | 3 | 7？ | — | `data[6]` 根本不存在 |

明明还有 3 个空单元，却已经写不进去了——这就是**假溢出**（false overflow）： **不是空间不够，而是空间在数组的另一头、指针够不着**。

**区分真假溢出**：真溢出是元素个数确实达到了容量；假溢出是元素个数没到容量， 但 `rear` 已经撞上数组边界。假溢出是**顺序存储 + 单向移动指针**这一组合的必然产物， 与队列本身无关（栈不会有这个问题，因为栈的两个操作都在同一端，指针会来回移动）。

## 循环：`% MaxSize` 为什么必要

解决办法是把数组**首尾相接**看成一个环：下标 `MaxSize-1` 的下一个是 `0`。 指针移动因此改写成front=(front+1)modMaxSize,rear=(rear+1)modMaxSize

**`% MaxSize` 做了两件事，缺一不可：**

- **保证下标合法**。不取模时 `rear` 是一个无界增长的整数，`data[rear]` 迟早越界。 取模把 `rear` 的取值域压缩到 {0,1,…,MaxSize−1}， 而这**恰好就是数组的合法下标集合**。
- **实现"绕回"**。`(MaxSize-1 + 1) % MaxSize = 0`，指针从末端自动跳回开头， 把出队腾出的前段空间重新利用起来。

**取模能不能换成 `if`？** 能，完全等价： `rear++; if (rear == MaxSize) rear = 0;`。取模只是把这个判断写成一个算术表达式。 理解这一点很重要——它说明 `%` 在这里**不是数学技巧，只是"走到头就回到 0"的紧凑写法**。 反过来也提醒你：如果某一步的指针移动跨度大于 1（比如 `rear = rear + 2`）， 用 `if` 就漏判了，必须用取模。

**指针后退时的取模写法**：双端队列或某些变体里需要 `rear` 后退一格， 必须写成 `rear = (rear - 1 + MaxSize) % MaxSize`。加 `MaxSize` 不是多此一举—— C 语言里负数取模的结果**不是正数**（`-1 % 8` 得到 `-1`），直接 `(rear-1) % MaxSize` 会得到 −1 这个非法下标。**凡是可能出现负数的取模，都要先加一个 `MaxSize`。**

图源：殷人昆《数据结构——用面向对象方法与 C++ 描述》（第 2 版）图3.20 循环队列的插入与删除，p116

这张图最值得看的是**最后一格**：`rear` 绕回到 0、`front` 停在 1，两个指针相邻， 数组里有 7 个元素、1 个空位——这正是下面"方案一"要保留的那个空位。

## `front == rear` 的二义性

绕回带来一个新麻烦。看两个场景（`MaxSize = 8`）：

- **队空**：入队 4 个再出队 4 个，`front = rear = 4`；
- **队满**：从空开始连续入队 8 个，`rear` 走了一圈回到 0……而 `front` 也是 0，`front = rear = 0`。

**同一个条件 `front == rear`，既可能是空，也可能是满。** 仅靠这两个指针无法区分， 必须额外引入信息。教材的原话是：

"对于循环队列不能以头、尾指针的值是否相同来判别队列空间是'满'还是'空'。"

引入信息的方式有三种，下面逐一给出**判空条件、判满条件、最多能存几个元素、代码差异**。

## 方案一：牺牲一个存储单元

**做法**：约定队列中**永远保留一个空位不存数据**。这样"满"的时候 `rear` 停在 `front` 的 前一格，`front == rear` 就只可能是空。

| 项 | 表达式 |
| --- | --- |
| 判空 | `front == rear` |
| 判满 | `(rear + 1) % MaxSize == front` |
| 最多元素数 | **`MaxSize - 1`** |
| 元素个数 | `(rear - front + MaxSize) % MaxSize` |
| 额外空间 | 无（只用 `front`、`rear`） |

**为什么判满是 `(rear+1) % MaxSize == front`**：`rear` 指向下一个入队位置， 如果这个位置**正是队头**，说明再入一个就会覆盖队头元素——此时空闲的只剩 `rear` 这一格， 按约定它不许使用，所以判为满。c

```
#define MaxSize 10

typedef struct {
    int data[MaxSize];
    int front, rear;   // rear 指向"下一个入队位置"
} SqQueue;

void InitQueue(SqQueue *Q) { Q->front = Q->rear = 0; }

bool QueueEmpty(SqQueue Q) { return Q.front == Q.rear; }

bool QueueFull(SqQueue Q)  { return (Q.rear + 1) % MaxSize == Q.front; }

bool EnQueue(SqQueue *Q, int x) {
    if ((Q->rear + 1) % MaxSize == Q->front)
        return false;                        // 队满，留下的那一格不许用
    Q->data[Q->rear] = x;                    // 先写入 rear 指的空位
    Q->rear = (Q->rear + 1) % MaxSize;       // 再让 rear 前进
    return true;
}

bool DeQueue(SqQueue *Q, int *x) {
    if (Q->front == Q->rear)
        return false;                        // 队空
    *x = Q->data[Q->front];                  // 先取队头元素
    Q->front = (Q->front + 1) % MaxSize;     // 再让 front 前进
    return true;
}

int QueueLength(SqQueue Q) {
    return (Q.rear - Q.front + MaxSize) % MaxSize;
}
```

**代价**：牺牲了 1 个单元，容量从 `MaxSize` 变成 `MaxSize - 1`。 **收益**：不需要任何额外变量，判空判满都是一句比较，是三种方案里**最省事的**， 也是各类教材与考题的默认口径。

## 方案二：增设 `size` 计数器

**做法**：额外维护一个 `size` 记录当前元素个数，入队 `size++`、出队 `size--`。 有了确切个数，`front == rear` 的二义性自然消失。

| 项 | 表达式 |
| --- | --- |
| 判空 | `size == 0` |
| 判满 | `size == MaxSize` |
| 最多元素数 | **`MaxSize`**（用满） |
| 元素个数 | `size`（直接读，O(1) 且无需取模） |
| 额外空间 | 1 个 `int` |

c

```
typedef struct {
    int data[MaxSize];
    int front, rear;   // rear 仍指向"下一个入队位置"
    int size;          // 当前元素个数
} SqQueue2;

void InitQueue2(SqQueue2 *Q) { Q->front = Q->rear = 0; Q->size = 0; }

bool QueueEmpty2(SqQueue2 Q) { return Q.size == 0; }
bool QueueFull2 (SqQueue2 Q) { return Q.size == MaxSize; }

bool EnQueue2(SqQueue2 *Q, int x) {
    if (Q->size == MaxSize) return false;    // 判满改看 size，与指针无关
    Q->data[Q->rear] = x;
    Q->rear = (Q->rear + 1) % MaxSize;
    Q->size++;                               // ← 与方案一的唯一代码差异
    return true;
}

bool DeQueue2(SqQueue2 *Q, int *x) {
    if (Q->size == 0) return false;          // 判空改看 size
    *x = Q->data[Q->front];
    Q->front = (Q->front + 1) % MaxSize;
    Q->size--;                               // ← 与方案一的唯一代码差异
    return true;
}
```

**与方案一的代码差异只有三处**：判满/判空的条件换成 `size`，入队末尾多一句 `size++`， 出队末尾多一句 `size--`。指针的移动方式**一个字都没变**。

**代价**：多一个变量，且每次入队出队多一次自增自减（常数开销，不改变 O(1)）。 **收益**：容量用满 `MaxSize`；求队列长度不用取模，直接读 `size`。

## 方案三：增设 `tag` 标志位

**做法**：用一位 `tag` 记录**最近一次成功操作是入队还是出队**：入队后置 `tag = 1`， 出队后置 `tag = 0`。

推理依据：**只有入队才可能把队列填满，只有出队才可能把队列清空**。 所以当 `front == rear` 时，看最后一步是什么就能定性。

| 项 | 表达式 |
| --- | --- |
| 判空 | `front == rear && tag == 0` |
| 判满 | `front == rear && tag == 1` |
| 最多元素数 | **`MaxSize`**（用满） |
| 元素个数 | `front != rear` 时用 `(rear-front+MaxSize) % MaxSize`；`front == rear` 时由 `tag` 决定是 `0` 还是 `MaxSize` |
| 额外空间 | 1 位（实现上通常还是 1 个 `int`） |

c

```
typedef struct {
    int data[MaxSize];
    int front, rear;
    int tag;           // 0 = 最近一次是出队，1 = 最近一次是入队
} SqQueue3;

void InitQueue3(SqQueue3 *Q) {
    Q->front = Q->rear = 0;
    Q->tag = 0;        // 初始视作"刚出过队"，于是初始状态被判为空
}

bool QueueEmpty3(SqQueue3 Q) { return Q.front == Q.rear && Q.tag == 0; }
bool QueueFull3 (SqQueue3 Q) { return Q.front == Q.rear && Q.tag == 1; }

bool EnQueue3(SqQueue3 *Q, int x) {
    if (Q->front == Q->rear && Q->tag == 1) return false;   // 队满
    Q->data[Q->rear] = x;
    Q->rear = (Q->rear + 1) % MaxSize;
    Q->tag = 1;                                             // ← 关键：入队置 1
    return true;
}

bool DeQueue3(SqQueue3 *Q, int *x) {
    if (Q->front == Q->rear && Q->tag == 0) return false;   // 队空
    *x = Q->data[Q->front];
    Q->front = (Q->front + 1) % MaxSize;
    Q->tag = 0;                                             // ← 关键：出队置 0
    return true;
}

int QueueLength3(SqQueue3 Q) {
    if (Q.front != Q.rear)
        return (Q.rear - Q.front + MaxSize) % MaxSize;
    return Q.tag == 1 ? MaxSize : 0;                        // 指针相等时靠 tag 定性
}
```

**`tag` 必须在每次成功操作后都更新，不能只在 `front == rear` 时更新**—— 因为判断发生在下一次操作之前，那时你无法回溯"上一步是什么"。这是本方案代码题里最常见的漏写。

**初值 `tag = 0` 的理由**：初始队列是空的，而判空要求 `tag == 0`，所以初值只能取 0。 如果初始化成 1，`InitQueue` 之后队列会被误判成"满"，第一次入队就直接失败—— 这是一个可以立刻自查的边界。

## 元素个数公式的来历

以 `rear` 指向"下一个入队位置"为前提，队列实际占用的下标是front, front+1, …, rear−1(modMaxSize)

个数就是 rear−front，但这个差在**绕回之后是负数**（比如 `MaxSize=8`、 `front=6`、`rear=2`，差为 −4，实际有 4 个元素）。在环上，"负 4"和"正 4"表示的是同一件事， 只要模 `MaxSize` 归一化即可：Length=(rear−front+MaxSize)modMaxSize

代入验证：(2−6+8)mod8=4 ✓。

**加 `MaxSize` 在 C 语言里是必需的**，理由前面说过：C 的 `%` 对负数不返回正余数， `(2-6) % 8` 得到 −4 而不是 4。

**这个公式在方案二/三下会失效**：当队列存满 `MaxSize` 个元素时 `rear == front`， 公式算出 0，与事实相反。方案二用 `size` 绕开，方案三用 `tag` 特判。 方案一因为容量只有 `MaxSize - 1`，`rear == front` 只能是空，公式**永远正确**—— 这是方案一被广泛采用的又一个理由。

### 由 `front`、`rear` 反推队列状态

循环队列 `data[0..49]`（`MaxSize = 50`），采用"牺牲一个单元"方案， `rear` 指向下一个入队位置。已知某时刻 `front = 45`、`rear = 8`，问： ① 队中有多少元素？② 还能再入队几个？③ 队头元素、队尾元素分别在哪个下标？

**① 元素个数**：(8−45+50)mod50=13mod50=13 个。

**验证**：占用的下标是 `45, 46, 47, 48, 49, 0, 1, ..., 7`，即 5 个 + 8 个 =13 个 ✓。

**② 还能入队几个**：容量为 MaxSize−1=49，已有 13 个，还能入 49−13=36 个。

**验证**：入满后 `rear` 应停在 `front` 的前一格，即 `rear = 44`； 从 8 走到 44 共走 44−8=36 步，每步入一个 ✓。

**③ 队头在 `data[45]`**（`front` 直接指向队头元素）； **队尾元素在 `data[7]`**——不是 `data[8]`！`rear = 8` 指的是**下一个空位**， 最后一个有效元素在 (8−1+50)mod50=7。

**③ 是这类题最常错的一问**。判据永远是先问一句"`rear` 指的是元素还是空位"， 再决定要不要退一格。

## 另一种指针约定：`rear` 指向队尾元素本身

上面所有公式的前提是"`rear` 指向下一个入队位置"。有的题目会改成 "**`front` 指向队头元素，`rear` 指向队尾元素**"，此时结论全部要重推。

推法只有一句：**先写出"队列占用了哪些下标"，再数格子。** 在新约定下，队列占用 front∼rear（含两端），共 (rear−front+1+MaxSize)modMaxSize 个。于是：

| 项 | `rear` 指向下一个空位（本篇默认） | `rear` 指向队尾元素 |
| --- | --- | --- |
| 初始化 | `front = rear = 0` | `front = 0, rear = MaxSize - 1` |
| 入队 | 先 `data[rear] = x`，再 `rear = (rear+1)%MaxSize` | 先 `rear = (rear+1)%MaxSize`，再 `data[rear] = x` |
| 出队 | 先 `x = data[front]`，再 `front` 前进 | 同左 |
| 判空（牺牲一单元） | `front == rear` | `(rear + 1) % MaxSize == front` |
| 判满（牺牲一单元） | `(rear + 1) % MaxSize == front` | `(rear + 2) % MaxSize == front` |
| 元素个数 | `(rear - front + MaxSize) % MaxSize` | `(rear - front + 1 + MaxSize) % MaxSize` |

注意右列的入队是**先移指针再写入**，与左列相反——道理和《[顺序栈](./sequential-stack.html)》 里"`top` 指元素就先移后写"完全一样：**指针指向有效元素时，写入前必须先腾一格**。

**考场做法**：不要背右边这一列。看到题面改了约定，就在草稿纸上画一个 `MaxSize = 5` 的小环， 手动入队两三个、出队一个，把"占用哪些下标"标出来，公式自然浮现。 现场推一遍不到一分钟，比记四套公式可靠得多。

## 交互可视化

通过下方的交互动画，你可以逐步观察循环队列的执行过程：加载可视化中...

## 复杂度分析

| 操作 | 时间复杂度 | 来历 |
| --- | --- | --- |
| 入队 | O(1) | 一次判满比较 + 一次写内存 + 一次取模，操作数与元素个数 n 无关 |
| 出队 | O(1) | 一次判空比较 + 一次读内存 + 一次取模 |
| 取队头 | O(1) | `data[front]` 一次随机存取 |
| 判空 / 判满 | O(1) | 一到两次整数比较 |
| 求队长 | O(1) | 方案一/三是一次减法加一次取模；方案二直接读 `size` |

**空间复杂度**：数组固定占 O(MaxSize)，与实际元素个数无关； 单次操作的辅助空间 O(1)。方案二/三比方案一多一个 O(1) 的变量。

**注意"能存多少"与"占多少空间"是两回事**：三种方案占的数组空间都是 `MaxSize`， 区别只在**可用容量**（方案一 `MaxSize-1`，方案二/三 `MaxSize`）。 所以"方案一更省空间"是错的——它更省的是**变量**，付出的是**容量**。

## 易混淆知识点

### 队空队满判别的三种方案（本章最该掌握的一张表）

| 对比项 | 方案一 牺牲一个单元 | 方案二 增设 `size` | 方案三 增设 `tag` | 判别依据 |
| --- | --- | --- | --- | --- |
| 额外空间 | 无 | 1 个 `int` | 1 位标志 | 看结构体里除 `front`/`rear` 外还有没有别的字段 |
| **判空条件** | `front == rear` | `size == 0` | `front == rear && tag == 0` | 空的判据从"指针相等"变成"计数为 0"或"指针相等且上一步是出队" |
| **判满条件** | `(rear+1) % MaxSize == front` | `size == MaxSize` | `front == rear && tag == 1` | 满的判据同上 |
| **最多存几个** | `MaxSize - 1` | `MaxSize` | `MaxSize` | 只有方案一留了一个不用的空位 |
| `front == rear` 时 | **只可能是空** | 可能空也可能满，由 `size` 定 | 可能空也可能满，由 `tag` 定 | 方案一消除了二义性，另两种是"保留二义性 + 额外信息裁决" |
| 元素个数公式 | `(rear-front+MaxSize) % MaxSize`，**恒成立** | `size`，直接读 | 指针不等时用公式；相等时看 `tag` 取 `0` 或 `MaxSize` | 满队时 `rear == front`，通用公式会算成 0 |
| 入队代码差异 | 判满用取模比较 | 判满看 `size`，末尾 `size++` | 判满看 `front==rear && tag==1`，末尾 `tag = 1` | 三者的指针移动语句**完全相同**，只差判定条件与收尾一句 |
| 出队代码差异 | 判空 `front == rear` | 判空 `size == 0`，末尾 `size--` | 判空 `front==rear && tag==0`，末尾 `tag = 0` | 同上 |
| 适用场合 | 默认口径；不想加字段 | 需要频繁查询队长，或必须用满容量 | 强调"最后一次操作"语义、只肯多用 1 位 | 题面若提到"不允许浪费存储单元"，排除方案一 |

### 其他易混点

| 对比项 | 情况 A | 情况 B | 判别依据 |
| --- | --- | --- | --- |
| 真溢出 vs 假溢出 | 真溢出：元素数确已达容量 | 假溢出：容量没用完，但 `rear` 撞到数组末端 | 数一下当前元素个数是否等于容量 |
| 循环队列 vs 循环链表 | 循环队列：**逻辑上**把数组首尾相接，靠取模实现 | 循环链表：**物理上**最后一个结点指回第一个结点 | 有没有真实存在的指针把尾接回头 |
| `(rear+1)%MaxSize` vs `rear+1` | 前者绕回后仍是合法下标 | 后者在 `rear == MaxSize-1` 时越界 | 取模保证结果落在 `0..MaxSize-1` |
| `(rear-front+MaxSize)%MaxSize` vs `(rear-front)%MaxSize` | 前者对绕回情形正确 | 后者在 C 中可能得到负数 | C 的 `%` 对负被除数返回负余数 |
| 循环队列判满 vs 共享栈判满 | 循环队列方案一必须牺牲一格 | [共享栈](./shared-stack.html) `top1+1==top2`，**不牺牲** | 共享栈有两个从两端相向移动的指针，不会出现"相等"歧义；循环队列只有一对同向绕圈的指针 |
| `tag` 更新时机 | 每次**成功**的入队/出队后都更新 | 只在 `front == rear` 时更新 | 判定发生在下一次操作之前，无法回溯上一步 |

## 本节小结

学完本篇，你应该能够：

- 用一组具体数字复现**假溢出**的发生过程，并说明它是"顺序存储 + 单向指针"的必然产物；
- 解释 `% MaxSize` 的两个作用（保证下标合法、实现绕回），并说明它等价于 `if (rear == MaxSize) rear = 0`；能指出指针后退时为什么必须写 `(x - 1 + MaxSize) % MaxSize`；
- 说清 `front == rear` 的二义性从何而来，并**默写出三种方案各自的判空条件、判满条件、 最大元素数**；
- 写出三种方案的完整入队/出队代码，并准确指出它们之间**只差判定条件和收尾一句**；
- 推导元素个数公式 `(rear-front+MaxSize)%MaxSize`，说明它在方案二/三满队时为什么失效；
- 遇到"`rear` 指向队尾元素"这类改约定的题目，能用"先写出占用了哪些下标，再数格子"的方法 现场把四个公式重推出来。

三个最关键的结论：

- **方案一牺牲一格换来"`front == rear` 只可能是空"**，代价是容量少 1，收益是不加任何字段 且长度公式恒成立；
- **三种方案的指针移动语句完全一致**，差别只在判定条件与收尾的 `size++` / `tag = 1`；
- **公式全部可推**，`% MaxSize` 与 `+MaxSize` 各自解决"越界"和"负数"，不是记忆项。

## 教材出处

- 队列的顺序存储表示与 `front = rear = 0` 的约定（非空队列中头指针指向队头元素、 尾指针指向队尾元素的下一个位置）：严蔚敏《数据结构（C 语言版）》（第 2 版）**p70** 「3.5.2 循环队列——队列的顺序表示和实现」
- 假溢出与"不能以头、尾指针是否相同判别队满队空"，以及两种处理方法 （**少用一个元素空间**、**另设标志位**）与队空 `Q.front == Q.rear`、 队满 `(Q.rear + 1) % MAXQSIZE == Q.front`：同书 **p71**
- 求循环队列长度算法 3.12 `(Q.rear - Q.front + MAXQSIZE) % MAXQSIZE`、 入队算法 3.13、出队算法 3.14：同书 **p72**
- 若无法预估队列最大长度则宜采用链队：同书 **p73**
- 图源：殷人昆《数据结构——用面向对象方法与 C++ 描述》（第 2 版）图3.20 循环队列的插入与删除，**p116**

教材正文只给出**两种**处理方法（少用一个元素空间、另设标志位）， 本篇的"增设 `size` 计数器"是同一思路（补充额外信息以消歧）下的第三种常见做法， 在各类题目中同样出现，故并列讲解，但不挂在教材页码之下。

## 相关知识

- [栈和队列的基本概念](./concepts.html)：队列的 ADT 与"出队序列唯一"的性质
- [链式队列](./queue.html)：队列的链式实现，天然没有假溢出，代价是每个结点多一个指针域； 容量不可预估时用它
- [共享栈](./shared-stack.html)：同样是"顺序存储怎么判满"，但因为两个指针相向移动， 不需要牺牲单元——两篇对读能看清歧义的来源
- [双端队列](./deque.html)：两端都能进出的推广，指针后退时的 `(x-1+MaxSize)%MaxSize` 就来自本篇
- [循环链表](./../linear/circular-linked-list.html)："首尾相连"的另一种实现方式， 区别在于它是靠真实指针接回去的
- [广度优先搜索](./../graph/bfs.html)：队列最主要的使用者，逐层扩展依赖 FIFO

### 相关文章

- [[02_数据结构_DS/stack-queue/concepts.md|栈和队列基本概念]]
- [[02_数据结构_DS/stack-queue/sequential-stack.md|顺序栈]]
- [[02_数据结构_DS/stack-queue/shared-stack.md|共享栈]]
- [[02_数据结构_DS/stack-queue/linked-stack.md|链栈]]
- [[02_数据结构_DS/stack-queue/queue.md|链式队列]]
- [[02_数据结构_DS/stack-queue/deque.md|双端队列]]
- [[02_数据结构_DS/stack-queue/bracket-matching.md|应用：括号匹配]]
- [[02_数据结构_DS/stack-queue/expression-eval.md|应用：表达式求值]]
- [[02_数据结构_DS/stack-queue/recursion.md|应用：栈在递归中的应用]]
- [[02_数据结构_DS/stack-queue/array-storage.md|多维数组的存储]]
- [[02_数据结构_DS/stack-queue/special-matrix.md|特殊矩阵的压缩存储]]

### 交互体验
[ 前往完整可视化页面 → ](https://codebrick.tech/ds-visual/visual/stack-queue/circular-queue)

## 真题练习

### 相关真题（1题）
[2011Q32分](https://www.codebrick.tech/practice/q/ds-2011-03)