---
title: 堆排序
source: https://www.codebrick.tech/algo-blog/posts/sorting/heap-sort.html
---

# 堆排序

## 场景引入

堆排序是一个"看起来完美"的算法：时间复杂度稳定 O(n log n)，空间复杂度 O(1)，不像快速排序有最坏退化的风险，不像归并排序需要额外空间。但现实中，堆排序几乎不被用作通用排序算法。这是为什么？

理解堆排序不仅是掌握一种排序方式，更是深入理解**堆（优先队列）**这一核心数据结构的基础。

## 核心思路

堆排序分两个阶段：

### 阶段一：建堆（Build Max Heap）

将无序数组原地构建为一个**最大堆**。最大堆的性质：每个节点的值都大于等于其子节点的值。

用数组表示完全二叉树时：

- 节点 `i` 的左子节点：`2i + 1`
- 节点 `i` 的右子节点：`2i + 2`
- 节点 `i` 的父节点：`Math.floor((i - 1) / 2)`

从最后一个非叶子节点（`Math.floor(n/2) - 1`）开始，自底向上对每个节点执行 `heapify`（下沉）操作。建堆的时间复杂度是 **O(n)**，不是 O(n log n)——这是一个常见的误区。

### 阶段二：排序（Extract Max）

- 堆顶（`arr[0]`）是最大值，将它与数组最后一个元素交换
- 堆的有效大小减一（最后一个位置已放好最大值）
- 对新的堆顶执行 `heapify`，恢复堆性质
- 重复直到堆大小为 1

### heapify（下沉）操作

`heapify(arr, size, root)` 将 `root` 节点下沉到正确位置：

- 比较 `root`、`left`、`right` 三者，找到最大的
- 如果最大的不是 `root`，交换并继续下沉
- 直到 `root` 比两个子节点都大，或到达叶子节点

## 算法流程图

## 可视化演示
加载可视化中...

## 代码实现
javascript

```
function heapSort(arr) {
  const n = arr.length;

  // 阶段一：建堆（从最后一个非叶子节点开始）
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }

  // 阶段二：逐个提取最大值
  for (let i = n - 1; i > 0; i--) {
    [arr[0], arr[i]] = [arr[i], arr[0]]; // 最大值放到末尾
    heapify(arr, i, 0);                  // 恢复堆性质
  }

  return arr;
}

function heapify(arr, size, root) {
  let largest = root;
  const left = 2 * root + 1;
  const right = 2 * root + 2;

  if (left < size && arr[left] > arr[largest]) {
    largest = left;
  }
  if (right < size && arr[right] > arr[largest]) {
    largest = right;
  }

  if (largest !== root) {
    [arr[root], arr[largest]] = [arr[largest], arr[root]];
    heapify(arr, size, largest); // 继续下沉
  }
}
```

## 为什么堆排序实践中比快速排序慢？

堆排序的理论复杂度优于快速排序（没有 O(n²) 最坏情况），但实际运行速度通常慢 2-3 倍。原因在于：

-

**缓存不友好**：堆的访问模式是跳跃式的（父节点到子节点的下标关系是 `2i+1`），导致 CPU 缓存命中率低。快速排序的分区操作是顺序扫描，缓存友好。
-

**比较次数更多**：堆排序平均比较次数约 2n log n，而快速排序约 1.39n log n。
-

**不可预测的分支**：heapify 中的比较方向依赖数据，CPU 分支预测命中率低。

这就是为什么 C++ `std::sort` 使用 IntroSort（快排 + 堆排 + 插入排序的混合），只在快排递归深度过深时才切换到堆排序作为保底。

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 最好 | O(n log n) | O(1) |
| 平均 | O(n log n) | O(1) |
| 最坏 | O(n log n) | O(1) |

**稳定性**：**不稳定**。堆顶与末尾交换时，相等元素的相对顺序可能改变。

**建堆时间**：O(n)，不是 O(n log n)。这是因为大部分节点在底层，下沉距离短。数学证明：∑h=0⌊log⁡n⌋⌈n/2h+1⌉⋅O(h)=O(n)

## 深入理解

- `heapify`（下沉操作）是堆的核心，理解它就能理解建堆和排序的全过程
- 建堆为什么是 O(n) 而不是 O(n log n)？因为大部分节点在底层，下沉距离短
- 堆排序的最大价值不在排序本身，而在**优先队列**（堆）这一数据结构
- 堆的常见应用：Top K 问题、中位数维护、任务调度

## LeetCode 练习

- [LC 912. 排序数组](https://leetcode.cn/problems/sort-an-array/) — 堆排序标准实现
- [LC 215. 数组中的第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) — 用最小堆维护 Top K
- [LC 347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) — 堆的经典应用
- [LC 295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/) — 对顶堆
- [LC 23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/) — 最小堆辅助合并