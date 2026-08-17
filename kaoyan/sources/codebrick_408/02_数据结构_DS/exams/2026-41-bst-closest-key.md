---
title: 2026·41 BST 最近邻：从中序遍历全树到沿路径下降
source: https://www.codebrick.tech/ds-full/posts/exams/2026-41-bst-closest-key.html
---

# 2026·41 BST 最近邻：从中序遍历全树到沿路径下降

本文属于[「从暴力解到最优解」专题](./brute-to-optimal.html)的**第二组**，也是一个反例。这道题的题干里连"比较次数"这种委婉说法都没有，从头到尾没出现任何要求效率的字眼。但它给定的存储结构是**二叉搜索树**，不是普通二叉树，也不是有序数组——**存储结构本身就是一种措辞**，它在无声地告诉你：这棵树的有序性是拿来用的，不用上就等于没读懂题。这比 [2022·42](./2022-42-top-k-min.html) 里那句藏着的「比较次数尽可能少」还要隐蔽。

## 题目

假定二叉搜索树使用二叉链表存储，存储结构如下：c

```
typedef struct BSTNode {
    int data;
    struct BSTNode *left, *right;
} BSTNode;
```

给一棵二叉搜索树 T 和整数 K，查找树中关键字与 K 之差的绝对值最小的所有结点，并输出该绝对值与结点中的关键字。

(1) 给出算法的基本设计思想。（4 分） (2) 使用 C/C++ 描述算法。（9 分）

总分 13 分。通读一遍题干会发现，它只字未提"高效""复杂度""比较次数"——如果只用"有没有出现尽可能高效"这条规则来判断要不要优化，这道题会被直接归为"不用优化"。但判分口径里明明白白写着 O(h) 才能拿满分。**优化要求这次藏在一个名词上：BSTNode。** 题面给的是二叉搜索树，这个存储结构本身就在暗示"用上它的有序性"。

## 第一步：把暴力解写对

先不管 BST 这个身份，把它当成一棵普通二叉树来看：要找与 K 之差绝对值最小的关键字，最直接的想法是把树上所有结点都看一遍，边看边和当前最优比较：c

```
// 中序遍历整棵树，记录与 K 最接近的所有关键字（可能并列两个）
void inorderClosest(BSTNode *node, int K, int *best, int keys[], int *cnt) {
    if (node == NULL) return;
    inorderClosest(node->left, K, best, keys, cnt);

    int diff = node->data > K ? node->data - K : K - node->data;
    if (diff < *best) {
        *best = diff;
        keys[0] = node->data;
        *cnt = 1;
    } else if (diff == *best) {
        keys[(*cnt)++] = node->data;      // 并列，追加（中序遍历天然升序，无需排序）
    }

    inorderClosest(node->right, K, best, keys, cnt);
}

void closestKeyBruteForce(BSTNode *T, int K) {
    int best = 2147483647;                // 足够大的初值
    int keys[2];                          // 最近邻最多两个
    int cnt = 0;

    inorderClosest(T, K, &best, keys, &cnt);

    printf("%d\n", best);
    for (int i = 0; i < cnt; i++) {
        printf("%d%c", keys[i], i == cnt - 1 ? '\n' : ' ');
    }
}
```

中序遍历天然按升序访问所有关键字，所以并列时先遇到的一定是较小的那个（floor），后遇到的是较大的那个（ceil），`keys` 数组不需要额外排序就已经是升序。

**复杂度**：中序遍历访问每个结点一次，时间 O(n)；递归栈深度等于树高，空间 O(h)。

## 它值多少分

按正确性/最优性两个维度（详见[总纲](./brute-to-optimal.html)），这道题的判分口径写得非常干净，直接把两个维度分开标注：

- **正确性**：只要抓住"要找的是与 K 之差绝对值最小的关键字"这个核心，并且想到"最近邻可能有两个（K 两侧等距并列）"要全部输出，用任何方法都给分——中序遍历整棵树完全符合这两条。(1) 问 4 分里的 3 分能拿到；(2) 问 9 分里，代码正确求出结果、正确处理命中/单侧/并列三种边界的 6 分也能拿到。
- **最优性**：题目给的是 BST，判分口径专门留了分数给"是否用上有序性做到只沿一条路径就找到答案"——(1) 问剩下的 1 分、(2) 问剩下的 3 分（时间 O(h) 2 分 + 空间 O(1) 迭代 1 分）都要求你不能只用"能遍历"这一件事，中序遍历整棵树是 O(n)，够不着。

**暴力解拿正确性分、丢最优性分**——这道 13 分的题，暴力解稳稳拿到 9 分，剩下 4 分全部挂在"有没有用 BST 的有序性把 O(n) 降到 O(h)"上。

## 暴力解的差距在哪

用总纲的三个问题审一遍：

**有没有放着性质不用？——这是本题唯一的浪费来源，但分量很重。**中序遍历把树上每一个结点都看了一遍，可这棵树是 BST：任意结点的左子树全部更小、右子树全部更大。暴力解完全没利用这条性质——它对待 BST 的方式和对待一棵随便长的二叉树没有任何区别。

**关键洞察**：一旦确定了 floor（≤K 的最大关键字）和 ceil（≥K 的最小关键字），比这两个邻居离 K 更远的结点全部可以不看。而 BST 的结构恰好保证：从根出发的一条路径，就能把 floor 和 ceil 同时找出来——不在这条路径上的结点，不可能比路径上的更接近 K。

## 智慧化改造：沿一条路径同时锁定 floor 和 ceil

从根开始迭代下降，每一步只看当前结点和 K 的大小关系：

- `cur->data == K`：命中，距离为 0，直接结束；
- `cur->data < K`：cur 比 K 小，是当前最优的 floor 候选，但右子树里可能还有更大、仍然 ≤ K 的——**向右走**；
- `cur->data > K`：对称，cur 是当前最优的 ceil 候选，**向左走**。

走到空指针时，floor、ceil 至少有一个已经确定；比较 `K − floor` 和 `ceil − K`，哪个小输出哪个，相等则两个都输出。整条路径长度不超过树高 h，一次下降就把答案锁定。c

```
void closestKey(BSTNode *T, int K) {
    int hasFloor = 0, hasCeil = 0;
    int floorV = 0, ceilV = 0;
    BSTNode *cur = T;

    while (cur != NULL) {
        if (cur->data == K) {                 /* 命中 */
            printf("0\n%d\n", K);
            return;
        } else if (cur->data < K) {
            if (!hasFloor || cur->data > floorV) {
                hasFloor = 1;
                floorV = cur->data;
            }
            cur = cur->right;
        } else {
            if (!hasCeil || cur->data < ceilV) {
                hasCeil = 1;
                ceilV = cur->data;
            }
            cur = cur->left;
        }
    }

    if (!hasFloor) {                                          /* 整树都 > K */
        printf("%d\n%d\n", ceilV - K, ceilV);
    } else if (!hasCeil) {                                    /* 整树都 < K */
        printf("%d\n%d\n", K - floorV, floorV);
    } else {
        int df = K - floorV, dc = ceilV - K;
        if (df < dc)      printf("%d\n%d\n", df, floorV);
        else if (dc < df) printf("%d\n%d\n", dc, ceilV);
        else              printf("%d\n%d %d\n", df, floorV, ceilV);  /* 并列升序 */
    }
}
```

从暴力解升级过来，几个细节决定这道题能拿多满：

- **方向别记反**：`cur->data < K` 是 floor 候选、向右走；`cur->data > K` 是 ceil 候选、向左走。方向记反会漏掉真正的候选，直接导致结果错误，不只是"不够优"。
- **floor/ceil 只需各更新一次判断，不需要回溯**：走到底时 floor 一定是路径上 ≤ K 的最大者、ceil 一定是路径上 ≥ K 的最小者，BST 性质保证不在路径上的结点不会比它们更近。
- **迭代而非递归**：用 while 循环只需要几个标量，空间 O(1)；写成递归下降虽然思路一样，但要额外算上 O(h) 的调用栈，最优性那 1 分要求的是迭代版本。
- **并列升序天然成立**：floorV < K < ceilV，`floorV ceilV` 的顺序写出来就是升序，不需要额外排序。

**复杂度**：时间 O(h)，沿单条路径下降，平衡树 O(log⁡n)、最坏退化 O(n)；空间 O(1)，只用了 4 个标量加一个游标指针。两个维度全部拿满，这就是标准答案。

## 两版对照跑一遍

建一棵 BST（依次插入 50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 65, 75），取 K = 55——特意选一个落在 50 和 60 正中间的 K，用来验证并列双解。先看中序遍历整树版，注意它把每一个结点都访问了一遍：加载可视化中...

再看沿路径下降版——注意它只走了一条从根到底的路径，没碰过路径以外的任何结点，两版最终得到的差值与关键字完全一致：加载可视化中...

演示用了内置的 `TreeNode`（字段名是 `val`），和上文 C 代码里题面给定的 `data` 字段是同一个东西，换了个名字而已。两版在 K = 55（50、60 正中间）的并列用例上给出完全相同的结果：差值 5，关键字 50 和 60。

## 等价方法与升级空间

- **递归中序遍历 vs 迭代路径下降**：这不是唯一的分歧点。就算都用"沿路径找 floor/ceil"这个正确思路，写成递归也能拿到 (2) 问的最优性时间分（O(h) 依然成立），但递归自带的调用栈是 O(h) 空间，够不上"空间 O(1)"这最后 1 分——**迭代版本才是把这道题拿满分的写法**。
- **中序遍历但提前剪枝**：有人会想到"中序遍历时如果当前差值已经开始变大就提前退出"，这个直觉是对的（BST 中序序列本身有序，差值确实是先减后增的单峰形状），但实现起来要在遍历过程中额外维护"是否已经过了最优点"的状态，比直接利用 BST 结构沿路径下降复杂得多，也更容易在边界条件上出错——本题的判分口径认的是"沿一条路径"这个更直接的做法。
- **哈希/排序等无关方法**：这道题的输入就是一棵 BST，题目也没给"关键字集合"以外的接口，把树先转成数组再二分之类的做法要先付出一遍 O(n) 遍历的代价，等价于中序遍历版本，同样够不上最优性。

## 下一步

- 在 OJ 上把两版代码都提交跑一遍：[ds-2026-41 BST 最近邻](https://www.codebrick.tech/oj/problems/ds-2026-41-bst-closest-key)
- 回到题库看这道题的完整解析与错因：[真题库 · 数据结构](https://www.codebrick.tech/practice/browse/ds)

### 相关真题（8题）
[2026Q4113分](https://www.codebrick.tech/practice/q/ds-2026-41?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2024Q72分](https://www.codebrick.tech/practice/q/ds-2024-07?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2022Q4113分](https://www.codebrick.tech/practice/q/ds-2022-41?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2020Q52分](https://www.codebrick.tech/practice/q/ds-2020-05?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2018Q62分](https://www.codebrick.tech/practice/q/ds-2018-06?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2013Q62分](https://www.codebrick.tech/practice/q/ds-2013-06?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2013Q4210分](https://www.codebrick.tech/practice/q/ds-2013-42?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)[2011Q72分](https://www.codebrick.tech/practice/q/ds-2011-07?ctx=ds-2026-41,ds-2024-07,ds-2022-41,ds-2020-05,ds-2018-06,ds-2013-06,ds-2013-42,ds-2011-07)