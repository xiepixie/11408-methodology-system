---
title: 结构体、指针与链式结点
source: https://www.codebrick.tech/ds-full/posts/c-exam/structs-pointers.html
---

# 结构体、指针与链式结点

很多考生不是不会链表算法，而是看到 `LNode *p`、`p->next` 就无法落笔。408 所需的指针范围其实很窄：**让指针指向结点、沿链接移动、比较地址、修改链接。**

不需要先学复杂指针运算。

## 先读懂题目给出的结构体
c

```
typedef struct LNode {
    int data;
    struct LNode *next;
} LNode, *LinkList;
```

这段定义产生两个别名：c

```
LNode node;       /* 一个结点本体 */
LNode *p;         /* 指向结点的指针 */
LinkList L;       /* 同样是 LNode * */
```

`LinkList` 只是指针类型的别名，不代表一整条链表被复制进变量。

## `.` 和 `->` 取决于左边是不是指针
c

```
LNode node;
LNode *p = &node;

node.data = 10;   /* node 是结构体本体，用 . */
p->data = 10;     /* p 是结构体指针，用 -> */
```

`p->next` 等价于 `(*p).next`。卷面直接使用箭头最清楚。

图结构体经常按值传入：c

```
int solve(MGraph G) {
    return G.Edge[0][1];   /* G 不是指针，所以用 . */
}
```

树根和链表头通常是指针：c

```
int solve(TreeNode *root) {
    return root->data;
}
```

## `NULL` 表示“不指向结点”

链式遍历的标准骨架：c

```
LNode *p = L->next;        /* 带头结点，跳过头结点 */
while (p != NULL) {
    /* 处理 p->data */
    p = p->next;
}
```

访问 `p->data` 前必须确定 `p != NULL`。下面的顺序会崩：c

```
while (p->data != target && p != NULL)   /* 错：先解引用，后判空 */
```

应写成：c

```
while (p != NULL && p->data != target)
```

C 的 `&&` 从左向右短路；若 `p == NULL`，右侧不会执行。

## 带头结点：第一个数据结点通常是 `head->next`

2009·42、2012·42、2015·41、2019·41 都涉及带头结点。头结点本身通常不保存有效数据：text

```
head -> 第一个数据结点 -> 第二个数据结点 -> NULL
```

因此遍历从 `head->next` 开始。把 `head` 当作第一个数据结点，是代码题最常见的整体错位。

### 改错：遍历起点错了一格

下面这段想数出数据结点个数。链表有 5 个数据结点，它却输出 `6`——因为把头结点也数了进去。改对遍历起点让它输出 `5`。

## 比较地址，不等于比较数据

2012·42 的“共享后缀”指两条链从某处开始使用同一批结点。判定同一个结点要写：c

```
if (p == q)       /* 地址相同：就是同一个结点 */
```

而不是：c

```
if (p->data == q->data)   /* 只能说明值相同 */
```

这是指针题的重要阅读规则：题目说“相同结点、共享结点、相交”，通常比较地址；说“关键字相同、值相等”，才比较数据域。

## 用前驱删除单链表结点

若 `pre->next` 是待删结点：c

```
LNode *temp = pre->next;
pre->next = temp->next;
free(temp);
```

顺序不能换。先 `free(temp)` 再读取 `temp->next` 属于释放后访问。

连续删除时，删除后 `pre` 不前进：c

```
while (pre->next != NULL) {
    if (shouldDelete(pre->next)) {
        LNode *temp = pre->next;
        pre->next = temp->next;
        free(temp);
    } else {
        pre = pre->next;
    }
}
```

## 修改指针变量，还是修改调用者的头指针
c

```
void move(Node *p) {
    p = p->next;
}
```

这里只改变局部变量 `p`，调用者的指针不变。若题目要求函数修改调用者持有的根指针或头指针，通常需要二级指针：c

```
void insert(Node **head, int value) {
    /* 通过 *head 修改调用者的头指针 */
}
```

不过历年大题多数已给定结构并要求遍历或原地重连，不要看到链表就主动上二级指针。以题目原型为准。

## 链表逆置的三行核心
c

```
LNode *pre = NULL;
LNode *cur = first;

while (cur != NULL) {
    LNode *next = cur->next;  /* 先保存后继 */
    cur->next = pre;          /* 再反转链接 */
    pre = cur;
    cur = next;
}
```

顺序口诀不是为了背语法，而是防止丢链：**存后继、改链接、两指针前进。**

## 立即写：倒数第 k 个结点

只补完 `findKthFromTail`。链表有头结点，默认数据为 `10 20 30 40 50`，`k=2`，正确输出为 `40`。

完成后测试 `k=1`、`k=5`、`k=6`。这些边界比普通样例更能检验指针距离是否正确。

## 立即写：BST 单路径下降

2026·41 的骨架：指针从根一路下降，边走边更新“目前最接近 K 的候选”。补完 `closestKey`，默认查 `K=58`，正确输出为 `60`。

关键是候选要在每一步都更新——答案不一定在最后落脚的那个结点上，途中经过的结点可能才是最近的。

## 对应真题练习

- [2009·42 倒数第 k 个结点](https://www.codebrick.tech/oj/problems/ds-2009-42-find-kth-from-tail)
- [2012·42 两链表共同后缀](https://www.codebrick.tech/oj/problems/ds-2012-42-list-common-suffix)
- [2015·41 链表按绝对值去重](https://www.codebrick.tech/oj/problems/ds-2015-41-list-dedup-by-abs)
- [2019·41 链表重排练习](https://www.codebrick.tech/oj/problems/p2313-reorder-list)
- [2026·41 BST 最近关键字](https://www.codebrick.tech/oj/problems/ds-2026-41-bst-closest-key)

## 本篇卷面检查

- 左边是结构体本体还是指针，应该用 `.` 还是 `->`？
- 带头结点时是否从 `head->next` 开始？
- 解引用前是否已经判空？
- 题目要求比较的是地址还是数据域？
- 改链接前是否保存了仍需访问的后继？
- 删除后前驱指针该不该前进？

下一篇：[递归与状态传递](./recursion-state.html)。