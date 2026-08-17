---
title: 用两个栈实现队列：两个栈的分工
source: https://www.codebrick.tech/ds-full/posts/exams/ext-queue-via-stacks.html
---

# 用两个栈实现队列：两个栈的分工

本文属于[「408 算法拓展训练」](./extensions.html)——考纲内、真题代码题尚未考过的经典题。这道题和 2019·42「用循环单链表实现队列」是同一类型——**数据结构设计题**，没有暴力解可以优化，考的是给定约束（只能用栈）反推出可行方案的设计判断力。**它是经典训练题，不是真题，也不押题。**

## 题目

仅使用两个栈（只能进行 `push`、`pop`、判空这类栈的标准操作，不能直接访问栈中间的元素），实现一个队列，支持 `enqueue(x)`（入队）和 `dequeue()`（出队并返回队头元素）两个操作。要求分析摊还时间复杂度。

这道题没有「尽可能高效」这类字样，但它对时间复杂度仍有隐含要求——用两个栈模拟队列的操作次数不能退化到每次都很慢，答案要能给出摊还复杂度的分析，这正是设计题里「隐含约束」的典型样子。

## 关键设计洞察：倒两次等于翻转两次

栈是后进先出（LIFO），队列要的是先进先出（FIFO）——两者顺序正好相反。**只用一个栈做不到**：不管怎么组合 `push`/`pop`，单个栈没法把「最先进的元素」放到能被优先取出的位置。

关键洞察是：**把一个栈的全部内容依次弹出、再依次压入另一个栈，等于把这段元素的顺序整体翻转了一次**。翻转一次的结果，原来栈底（最早进的）元素变成了新栈的栈顶（最先能弹出的）——顺序从 LIFO 变成了 FIFO。

于是分工自然浮现：一个栈（`in`）专门负责承接入队的新元素，顺序和入队顺序一致（后进的在顶）；需要出队时，把 `in` 的全部内容"倒"进另一个栈（`out`），这一倒就把顺序翻转成了「最早入队的在 `out` 的栈顶」，直接弹出即可。

## 做法与关键细节

**数据结构**：两个栈 `in` 和 `out`。

**入队 enqueue(x)**：直接压入 `in` 栈，O(1)。不管 `out` 栈的状态，入队永远只操作 `in`。

**出队 dequeue()**：

- 检查 `out` 栈是否为空；
- 若 `out` 为空，把 `in` 栈的元素全部弹出、依次压入 `out`（这一步是唯一的「翻转」时机）；
- 若 `out` 非空（或刚搬运完），直接弹出 `out` 的栈顶，就是当前队头。c

```
#define MAXSIZE 100

typedef struct {
    int data[MAXSIZE];
    int top;
} Stack;

void initStack(Stack *s) { s->top = -1; }
int stackEmpty(Stack *s) { return s->top == -1; }
void push(Stack *s, int x) { s->data[++s->top] = x; }
int pop(Stack *s) { return s->data[s->top--]; }

typedef struct {
    Stack in;
    Stack out;
} MyQueue;

void initQueue(MyQueue *q) {
    initStack(&q->in);
    initStack(&q->out);
}

void enqueue(MyQueue *q, int x) {
    push(&q->in, x);
}

int dequeue(MyQueue *q) {
    if (stackEmpty(&q->out)) {              // 只有 out 空了才搬运
        while (!stackEmpty(&q->in)) {
            push(&q->out, pop(&q->in));
        }
    }
    return pop(&q->out);
}

int queueEmpty(MyQueue *q) {
    return stackEmpty(&q->in) && stackEmpty(&q->out);
}
```

**摊还分析是这道题的得分关键**。单看某一次 `dequeue`，如果恰好触发了搬运，那一次要花 O(n)（n 为 `in` 里当时的元素数）；但把整个操作序列（若干次 enqueue、dequeue 混合调用）放在一起看：**每个元素从入队到出队，一生只会被压入 `in` 一次、从 `in` 弹出一次、压入 `out` 一次、从 `out` 弹出一次，一共 4 次栈操作**。n 次操作的总代价不超过 O(n)，均摊到每次操作就是**摊还 O(1)**。这和顺序表扩容的摊还分析是同一个道理——单次操作可能贵，但代价均摊到足够多次操作上就被稀释了。

## 两个栈分工，看一遍

下面演示先连续入队 1、2、3，出队一次触发搬运（此时输出 1），接着入队 4，再连续出队三次（依次输出 2、3、4）——注意第二次出队没有再次搬运,因为 `out` 里还有元素：加载可视化中...

演示为 JavaScript 版本，逻辑与上文 C 代码一一对应。

## 常见错点

- **每次出队都无条件搬运一次**。不检查 `out` 是否为空、每次 `dequeue` 都把 `in` 倒进 `out`，会把 `out` 里还没消费完的正确顺序打乱（多倒一次又翻转回去了），而且失去了摊还 O(1) 的优势，退化成每次都可能 O(n)。
- **搬运时机反了：`in` 空了才倒**。应该是 `out` 空了才倒——`in` 只负责接收新元素，它空不空跟能不能出队没有关系，出队能不能进行看的是 `out` 有没有货。
- **判断队空只查一个栈**。队列为空的条件是 `in` 和 `out` 都为空，只查其中一个会漏判——元素可能还没被倒进 `out`，此时 `in` 非空但 `out` 空，不能误判为队空。
- **倒的时候只倒一部分**。翻转顺序必须把 `in` 的元素**一次性全部**弹出压入 `out`，倒到一半就停会让剩下的元素顺序和已经倒过去的元素顺序不一致，破坏 FIFO。

## 下一步

- 在 OJ 上把代码提交跑一遍：[用两个栈实现队列](https://www.codebrick.tech/oj/problems/ds-drill-queue-application-101-queue-via-stacks)
- 同属「栈的应用」的拓展题：括号匹配、逆波兰表达式求值、中缀表达式转后缀
- 同类型的数据结构设计题：[2019·42 用循环单链表实现队列](./2019-42-circular-queue.html)
- 回到方法论源头：[「暴力解到最优解」真题专题总纲](./brute-to-optimal.html)

### 相关真题（12题）
[2026Q4210分](https://www.codebrick.tech/practice/q/ds-2026-42?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2025Q22分](https://www.codebrick.tech/practice/q/ds-2025-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2024Q22分](https://www.codebrick.tech/practice/q/ds-2024-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2020Q22分](https://www.codebrick.tech/practice/q/ds-2020-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2018Q12分](https://www.codebrick.tech/practice/q/ds-2018-01?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2017Q22分](https://www.codebrick.tech/practice/q/ds-2017-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2015Q12分](https://www.codebrick.tech/practice/q/ds-2015-01?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2014Q22分](https://www.codebrick.tech/practice/q/ds-2014-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2013Q22分](https://www.codebrick.tech/practice/q/ds-2013-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2012Q22分](https://www.codebrick.tech/practice/q/ds-2012-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2010Q12分](https://www.codebrick.tech/practice/q/ds-2010-01?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)[2009Q22分](https://www.codebrick.tech/practice/q/ds-2009-02?ctx=ds-2026-42,ds-2025-02,ds-2024-02,ds-2020-02,ds-2018-01,ds-2017-02,ds-2015-01,ds-2014-02,ds-2013-02,ds-2012-02,ds-2010-01,ds-2009-02)