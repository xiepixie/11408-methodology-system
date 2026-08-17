---
title: 二分查找左右边界：从线性扫到二分收敛
source: https://www.codebrick.tech/ds-full/posts/exams/ext-binary-search-bound.html
---

# 二分查找左右边界：从线性扫到二分收敛

本文属于[「408 算法拓展训练」](./extensions.html)——考纲内、真题代码题尚未考过的经典题。折半查找是「查找」这一章的核心算法，考纲要求掌握判定树、ASL 计算，「在有重复值的有序数组里找边界」是折半查找最常见的变体，也是练「收缩条件怎么写」的好材料。**它是经典训练题，不是真题，也不押题。**

## 题目

给定一个升序排列的数组 a（长度 n），其中的元素可能重复，给定目标值 target。设计一个时间上尽可能高效的算法，返回 target 在数组中第一次出现和最后一次出现的下标；如果 target 不存在，两个下标都返回 −1。

题面出现了「尽可能高效」，按[拓展训练导语](./extensions.html)的分类，这道题属于「暴力→最优」型。

## 第一步：把暴力解写对——线性扫一遍

最直接的想法：从头到尾扫一遍数组，第一次遇到等于 target 的位置记为 first，之后每遇到一次都更新 last，扫完整个数组就得到了首尾位置。c

```
void searchRangeBrute(int a[], int n, int target, int *first, int *last) {
    *first = -1;
    *last = -1;
    for (int i = 0; i < n; i++) {
        if (a[i] == target) {
            if (*first == -1) *first = i;   // 第一次遇到，记下起点
            *last = i;                       // 每次遇到都更新终点
        }
    }
}
```

拿 a = `[1,2,2,2,3,4,5,5,6]`、target = 2 走一遍：i=1 第一次遇到 2，first=1、last=1；i=2、i=3 继续遇到 2，last 更新到 3；后面不再遇到 2，扫完返回 first=1、last=3。

**复杂度**：不管目标值存不存在，都要扫完整个数组，时间 O(n)；只用了几个变量，空间 O(1)。

## 它值多少分

用[总纲](./brute-to-optimal.html)的两维度看：

- **正确性**：线性扫描一定能找全所有等于 target 的位置，first/last 的更新逻辑正确，复杂度分析 O(n) 与实现一致。正确性维度的分拿得到。
- **最优性**：题面要求「尽可能高效」，数组本身有序这条性质暴力解完全没有用上，期望复杂度是 O(log⁡n)。这一档拿不到。

## 暴力解的浪费在哪

用[总纲](./brute-to-optimal.html)的「找浪费三问」审一遍：

**有没有放着性质不用？——有。** 数组是升序的，这意味着所有等于 target 的元素在数组里是**连续的一段**，而且这一段的左边全比 target 小、右边全比 target 大。暴力解对着这样一个有序数组，仍然一格一格地扫过去，完全没有利用「有序」这个前提——它对无序数组也会这么扫，多花的时间全部来自「没用上有序性」这一件事。

**浪费的本质：数组的有序性能让我们一次跳过一大段肯定不含答案的区间，暴力解却坚持一格一格挪，把这条捷径浪费掉了。**

## 智慧化改造：二分收缩，命中也不停

对策是总纲里的第三类手段——**利用已知的结构性质**，这里的性质就是「有序」。二分查找每一步都能把搜索范围砍掉一半，关键的改造在于：**普通二分查找一旦命中就直接返回，但找边界需要在命中之后继续收缩**——找左边界时，命中了也不能停，要继续往左收（`right = mid - 1`），因为左边可能还有相同的值；找右边界同理，命中了继续往右收（`left = mid + 1`）。每次命中都先把当前位置记到答案里，再继续收缩，直到区间收完，最后记下的就是边界。c

```
int lowerBound(int a[], int n, int target) {
    int left = 0, right = n - 1, ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] == target) {
            ans = mid;
            right = mid - 1;        // 命中也向左收，找更靠左的相同值
        } else if (a[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}

int upperBound(int a[], int n, int target) {
    int left = 0, right = n - 1, ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] == target) {
            ans = mid;
            left = mid + 1;         // 命中也向右收，找更靠右的相同值
        } else if (a[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return ans;
}
```

从暴力解升级过来，几处最容易翻车：

- **`left <= right` 而不是 `left < right`。** 二分查找的循环条件决定了区间能不能收窄到只剩一个元素还继续判断，写成 `<` 会在只剩一个候选元素时提前退出，漏判这个元素本身是不是答案。
- **命中后要不要继续收缩，是左边界和右边界唯一的区别。** 两个函数其余部分完全一样，`a[mid] == target` 分支里 `right = mid - 1` 还是 `left = mid + 1`，是两者的全部差异——写反了会导致 lowerBound 实际上找到的是右边界。
- **`mid` 用 `left + (right - left) / 2` 而不是 `(left + right) / 2`。** 两者数学上等价，但后者在 left、right 都很大时可能整数溢出，408 考场对这个细节不严格要求，但工程上是标准写法，值得养成习惯。
- **`ans` 记录的是「最近一次命中的位置」，不是「最后一次进入循环的位置」。** 二分收缩到最后可能 `left > right` 却压根没命中过（target 不存在），这时 ans 始终是初始值 −1，不能返回 mid 或 left。

**复杂度**：每一步区间减半，时间 O(log⁡n)；只用了常数个变量，空间 O(1)。相比暴力解的 O(n)，是数量级的提升。

## 两版对照跑一遍

同一组输入 a = `[1,2,2,2,3,4,5,5,6]`、target = 2（答案：first=1、last=3）。先看线性扫描——一格一格挪过去：加载可视化中...

再看二分收缩——命中后继续向对应方向收，逐步逼近边界：加载可视化中...

演示为 JavaScript 版本，逻辑与上文 C 代码一一对应。

## 等价方法与升级空间

- **也可以用标准库风格的 lower_bound/upper_bound 语义实现**：lower_bound 返回第一个 ≥ target 的位置，upper_bound 返回第一个 > target 的位置，通过 `upper_bound(target) - 1` 得到最后一次出现的位置。这和本文「命中后继续收缩」的写法是同一个思路的两种表达，理解了其中一种就理解了另一种。
- **为什么不需要更复杂的做法**：这道题的搜索空间就是数组下标本身，二分查找已经把复杂度压到了对数级，要确认答案在哪个位置，读入信息本身就至少需要 O(log⁡n) 次比较（判定树高度下界），408 大纲内没有更快的等价算法。

## 下一步

- 在 OJ 上把代码提交跑一遍：[二分查找左右边界](https://www.codebrick.tech/oj/problems/ds-drill-binary-search-103-search-bound)
- 看二分查找判定树与 ASL 的交互演示：[折半查找可视化](https://codebrick.tech/ds-visual/visual/search/binary-search)
- 回到方法论源头：[「暴力解到最优解」真题专题总纲](./brute-to-optimal.html)

### 相关真题（7题）
[2024Q52分](https://www.codebrick.tech/practice/q/ds-2024-05?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)[2023Q82分](https://www.codebrick.tech/practice/q/ds-2023-08?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)[2017Q82分](https://www.codebrick.tech/practice/q/ds-2017-08?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)[2016Q92分](https://www.codebrick.tech/practice/q/ds-2016-09?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)[2015Q72分](https://www.codebrick.tech/practice/q/ds-2015-07?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)[2011Q4215分](https://www.codebrick.tech/practice/q/ds-2011-42?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)[2010Q92分](https://www.codebrick.tech/practice/q/ds-2010-09?ctx=ds-2024-05,ds-2023-08,ds-2017-08,ds-2016-09,ds-2015-07,ds-2011-42,ds-2010-09)