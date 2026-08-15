---
title: 单链表判环：从哈希表到快慢指针
source: https://www.codebrick.tech/ds-full/posts/exams/ext-linked-list-cycle.html
---

# 单链表判环：从哈希表到快慢指针

本文属于[「408 算法拓展训练」](./extensions.html)——考纲内、真题代码题尚未考过的经典题。链表判环是「链表」这一考点里最常被单独拎出来考的操作之一，快慢指针的用法和 2009·42（倒数第 k 个结点）、2019·41（链表重排）系出同源。**它是经典训练题，不是真题，也不押题。**

## 题目

给定一个单链表的头指针 head，判断链表中是否存在环（即某个结点的 next 最终指回链表中已经出现过的结点，导致遍历永远走不到 NULL）。要求分析时间复杂度和空间复杂度。

链表结点定义如下：c

```
typedef struct node {
    int val;
    struct node *next;
} NODE;
```

判环没有强制要求时间上多快，但对空间复杂度的期望很明确——最优解应当是 O(1) 空间。下面先写一个直觉上最容易想到的解法。

## 第一步：把暴力解写对——哈希集合记录已访问结点

最直接的想法：遍历链表，每经过一个结点就把它的地址记下来；如果某一步将要访问的结点已经在记录里出现过，说明这条路走回了老地方，链表有环。如果一路走到 NULL 都没有重复，说明无环。c

```
#include <stdbool.h>

// 用一个简单的开放地址哈希集合存放已访问结点的地址
#define TABLE_SIZE 10007

typedef struct {
    NODE *slots[TABLE_SIZE];
    bool used[TABLE_SIZE];
} AddrSet;

void setInit(AddrSet *set) {
    for (int i = 0; i < TABLE_SIZE; i++) set->used[i] = false;
}

bool setContainsOrAdd(AddrSet *set, NODE *p) {
    unsigned long h = ((unsigned long)p / sizeof(NODE)) % TABLE_SIZE;
    while (set->used[h]) {
        if (set->slots[h] == p) return true;   // 已存在，命中
        h = (h + 1) % TABLE_SIZE;               // 线性探测
    }
    set->slots[h] = p;
    set->used[h] = true;
    return false;                               // 新加入
}

bool hasCycle(NODE *head) {
    AddrSet visited;
    setInit(&visited);
    NODE *p = head;
    while (p != NULL) {
        if (setContainsOrAdd(&visited, p)) return true;   // 再次遇到，有环
        p = p->next;
    }
    return false;                               // 走到 NULL，无环
}
```

拿一条尾部指回中间结点的链表走一遍：从 head 出发逐个把结点地址塞进集合，一旦发现某个结点已经在集合里，立刻返回有环；如果正常走到 NULL 则返回无环。

**复杂度**：每个结点最多访问一次，做一次常数期望时间的哈希查找/插入，时间 O(n)；集合最坏要存下全部 n 个结点的地址，空间 O(n)。

## 它值多少分

拓展题按真题同样的两维度看（详见[真题专题总纲](./brute-to-optimal.html)）：

- **正确性**：哈希集合能可靠判断任何结点是否被重复访问过，逻辑直接对应「环」的定义，结果正确、复杂度分析与实现一致。正确性维度的分拿得到。
- **最优性**：判环这道题的最优解是 O(1) 空间。哈希集合解的 O(n) 空间达不到这个期望，最优性这一档拿不到。

一份写对的哈希集合解拿正确性分、丢最优性分。链表判环恰好是「用一点点结构性质换掉整个辅助空间」的典型例子。

## 暴力解的浪费在哪

用[总纲](./brute-to-optimal.html)的「找浪费三问」审这份哈希集合解：

**有没有放着性质不用？——有。** 哈希集合解把每一个走过的结点地址都存了下来，为的是回答一个问题：「我现在走到的这个结点，之前是不是走过？」但仔细想想，判断「链表有没有环」根本不需要精确知道**是哪个**结点被重复访问，只需要知道**存不存在**重复访问这件事。

**性质在哪：如果链表有环，那么在环里绕圈的任意两个不同速度的指针，迟早会相遇。** 这是纯粹的相对运动关系——环上两个指针的速度差不为零，快指针每一步比慢指针多走一步，在有限的环长内，快指针迟早会追上慢指针，从相对静止的角度看它们最终会在同一个结点相遇。而如果没有环，快指针只会正常地先到达 NULL，不会有相遇这回事。

**浪费的本质：哈希集合存下了每个结点的身份，去回答「有没有重复」；而重复的存在性，两个不同速度的指针单靠相对运动就能测出来，完全不需要记住任何一个结点。**

## 智慧化改造：快慢指针 Floyd 判圈

对策是总纲里的第三类手段——**利用已知的结构性质**。这里的性质就是环上的相对运动：设慢指针 slow 每次走一步，快指针 fast 每次走两步，两者同时从 head 出发。

- 如果链表无环，fast 会正常地先到达 NULL（或 fast->next 为 NULL），循环结束，返回无环；
- 如果链表有环，fast 会先于 slow 进入环，并在环内不断绕圈；由于 fast 每一步比 slow 多走一步，两者在环内的相对位置每步缩小 1，有限步内必然相遇——一旦 `slow == fast`，就确认有环。c

```
#include <stdbool.h>

bool hasCycle(NODE *head) {
    NODE *slow = head;
    NODE *fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;              // 慢指针走一步
        fast = fast->next->next;        // 快指针走两步
        if (slow == fast) return true;  // 相遇，说明有环
    }
    return false;                       // fast 提前到达 NULL，说明无环
}
```

从哈希集合解升级过来，几处最容易翻车：

- **循环条件必须同时检查 `fast != NULL` 和 `fast->next != NULL`**。fast 一次走两步，如果只判断 `fast != NULL` 就去访问 `fast->next->next`，在无环链表的最后一两步会造成空指针解引用。
- **先移动指针，再比较是否相遇**。如果在移动前比较 `slow == fast`（此时两者都还在 head），会立即误判为有环；必须让两个指针至少各走一步之后再判断。
- **不需要额外变量记录任何结点**。相比哈希集合解要开辟整块存储，这里全程只有 slow、fast 两个指针，改造的核心就是「用两个指针的相对速度替代整个哈希表」。
- **不要求找到环的入口，只判断是否有环**。若题目进一步要求返回环的起始结点，需要在相遇后让一个指针从 head 重新出发、两者都改为每次走一步，再次相遇处即为环入口——这是判环之后的经典追加问法，不在本题范围内。

**复杂度**：无环时 fast 最多走 n/2 步到达 NULL，时间 O(n)；有环时 fast 最多在进入环后额外绕一圈追上 slow，总步数仍是 O(n) 量级。全程只用了 slow、fast 两个指针变量，空间 O(1)——这就是把哈希集合的 O(n) 空间彻底消除后的结果。

## 两版对照跑一遍

同一条链表 `1 → 2 → 3 → 4 → 5`，把尾结点的 next 指回结点 2，构造出一个环。先看哈希集合解（演示为 JavaScript 版本，用 `Set` 等价代替哈希表）：加载可视化中...

再看 Floyd 快慢指针——全程只有两个指针在移动，没有任何辅助容器：加载可视化中...

演示为 JavaScript 版本，逻辑与上文 C 代码一一对应。

## 等价方法与升级空间

- **标记位法**：如果结点结构允许改动（比如加一个 `visited` 布尔字段），可以不开辅助集合，直接把访问过的结点标记在结点自己身上。这份解同样是 O(n) 时间，空间开销从「独立哈希表」变成「侵入式字段」，但依然不是 O(1) 额外空间，且改动了原始数据结构，通常不如快慢指针干净。
- **找环入口是判环的自然延伸**：相遇后让一个指针回到 head、两者都改为一次走一步，再次相遇的结点就是环的入口。这一步用到的仍然是快慢指针，理解了判环的相对运动就理解了找入口的原理。
- **为什么不用更复杂的方案**：判环问题在数学上有更精细的分析（比如环长、相遇点到入口的距离关系），但 408 大纲只要求判断「有没有环」，Floyd 判圈已经是最简洁的 O(1) 空间最优解，没有必要引入更复杂的工具。

## 下一步

- 在 OJ 上把代码提交跑一遍：[单链表判环](https://www.codebrick.tech/oj/problems/ds-drill-singly-linked-list-107-detect-cycle)
- 回到方法论源头：[「暴力解到最优解」真题专题总纲](./brute-to-optimal.html)
- 同属「链表」的拓展题：[判断链表回文](./ext-palindrome-linked-list.html) 用的也是快慢指针找中点，是这道题手段上的近亲

### 相关真题（8题）
[2024Q12分](https://www.codebrick.tech/practice/q/ds-2024-01?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2019Q4113分](https://www.codebrick.tech/practice/q/ds-2019-41?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2017Q112分](https://www.codebrick.tech/practice/q/ds-2017-11?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2016Q12分](https://www.codebrick.tech/practice/q/ds-2016-01?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2015Q4115分](https://www.codebrick.tech/practice/q/ds-2015-41?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2013Q12分](https://www.codebrick.tech/practice/q/ds-2013-01?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2012Q4212分](https://www.codebrick.tech/practice/q/ds-2012-42?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)[2009Q4215分](https://www.codebrick.tech/practice/q/ds-2009-42?ctx=ds-2024-01,ds-2019-41,ds-2017-11,ds-2016-01,ds-2015-41,ds-2013-01,ds-2012-42,ds-2009-42)