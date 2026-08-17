---
title: 二叉堆：从数组到优先队列
source: https://www.codebrick.tech/algo-blog/posts/heap/basics.html
---

# 二叉堆：从数组到优先队列

## 场景引入

操作系统的任务调度需要快速取出优先级最高的任务，搜索引擎需要快速获取相关性最高的结果。这些场景都需要一种数据结构：**优先队列**。而优先队列的底层实现就是二叉堆。

## 核心原理

二叉堆是一棵**完全二叉树**，用**数组**存储（不需要指针）：

- 节点 `i` 的父节点：`Math.floor((i - 1) / 2)`
- 节点 `i` 的左子节点：`2 * i + 1`
- 节点 `i` 的右子节点：`2 * i + 2`

**最小堆**：父节点 ≤ 子节点（堆顶是最小值） **最大堆**：父节点 ≥ 子节点（堆顶是最大值）

## 两个核心操作

### 上浮（swim）—— 插入时使用

新元素放到数组末尾，然后不断与父节点比较、交换，直到满足堆性质。

### 下沉（sink）—— 删除堆顶时使用

堆顶移除后，把末尾元素放到堆顶，然后不断与较小的子节点比较、交换。

## 完整实现
javascript

```
class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() { return this.heap.length; }
  peek() { return this.heap[0]; }

  push(val) {
    this.heap.push(val);
    this._swim(this.heap.length - 1);
  }

  pop() {
    const top = this.heap[0];
    const last = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = last;
      this._sink(0);
    }
    return top;
  }

  _swim(i) {
    while (i > 0) {
      const parent = Math.floor((i - 1) / 2);
      if (this.heap[i] >= this.heap[parent]) break;
      [this.heap[i], this.heap[parent]] = [this.heap[parent], this.heap[i]];
      i = parent;
    }
  }

  _sink(i) {
    const n = this.heap.length;
    while (2 * i + 1 < n) {
      let child = 2 * i + 1;
      if (child + 1 < n && this.heap[child + 1] < this.heap[child]) child++;
      if (this.heap[i] <= this.heap[child]) break;
      [this.heap[i], this.heap[child]] = [this.heap[child], this.heap[i]];
      i = child;
    }
  }
}
```

## 建堆：O(n) 而非 O(n log n)

从最后一个非叶子节点开始，依次下沉：javascript

```
function buildHeap(arr) {
  const n = arr.length;
  // 从最后一个非叶子节点开始下沉
  for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
    sink(arr, i, n);
  }
}
```

为什么是 O(n)？因为大部分节点在底层，下沉距离短。数学证明：总操作次数 ≈ 2n。

## 复杂度分析

| 操作 | 时间 |
| --- | --- |
| 插入（push） | O(log n) |
| 删除堆顶（pop） | O(log n) |
| 查看堆顶（peek） | O(1) |
| 建堆 | O(n) |

空间复杂度：O(n)

## 面试要点

- 能手写 MinHeap/MaxHeap（push、pop、swim、sink）
- 理解堆是完全二叉树，用数组存储
- 知道建堆是 O(n) 而非 O(n log n)
- JavaScript 没有内置堆，面试时需要手写