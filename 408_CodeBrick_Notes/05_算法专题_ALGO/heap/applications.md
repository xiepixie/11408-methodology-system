---
title: 堆的经典应用：Top-K 与中位数
source: https://www.codebrick.tech/algo-blog/posts/heap/applications.html
---

# 堆的经典应用：Top-K 与中位数

## 场景引入

搜索引擎要实时显示 Top 10 热搜关键词，数据流源源不断——你不可能每次都排序一遍。堆是解决这类「动态维护极值」问题的利器。

## Top-K 问题解题思路

## LC 215. 数组中的第 K 个最大元素

### 方法一：最小堆（维护大小为 K 的堆）
javascript

```
function findKthLargest(nums, k) {
  const heap = new MinHeap();
  for (const num of nums) {
    heap.push(num);
    if (heap.size() > k) heap.pop(); // 弹出最小的
  }
  return heap.peek(); // 堆顶就是第 K 大
}
```

**思路**：维护一个大小为 K 的最小堆，遍历完后堆顶就是第 K 大元素。

时间 O(n log k)，空间 O(k)。

### 方法二：快速选择（平均 O(n)）
javascript

```
function findKthLargest(nums, k) {
  const target = nums.length - k;

  function quickSelect(lo, hi) {
    const pivot = nums[hi];
    let i = lo;
    for (let j = lo; j < hi; j++) {
      if (nums[j] <= pivot) {
        [nums[i], nums[j]] = [nums[j], nums[i]];
        i++;
      }
    }
    [nums[i], nums[hi]] = [nums[hi], nums[i]];

    if (i === target) return nums[i];
    if (i < target) return quickSelect(i + 1, hi);
    return quickSelect(lo, i - 1);
  }

  return quickSelect(0, nums.length - 1);
}
```

## LC 347. 前 K 个高频元素
javascript

```
function topKFrequent(nums, k) {
  const freq = new Map();
  for (const n of nums) freq.set(n, (freq.get(n) || 0) + 1);

  // 用最小堆维护 top K 高频元素
  const heap = new MinHeap(); // 按频率比较
  for (const [num, count] of freq) {
    heap.push({ num, count });
    if (heap.size() > k) heap.pop();
  }

  return heap.heap.map(item => item.num);
}
```

## LC 295. 数据流的中位数

**核心思路**：用两个堆——一个最大堆存较小的一半，一个最小堆存较大的一半。javascript

```
class MedianFinder {
  constructor() {
    this.maxHeap = new MaxHeap(); // 左半部分（较小值）
    this.minHeap = new MinHeap(); // 右半部分（较大值）
  }

  addNum(num) {
    // 先加入左半部分
    this.maxHeap.push(num);
    // 左半部分最大值移到右半部分
    this.minHeap.push(this.maxHeap.pop());
    // 保持平衡：左半部分可以多一个
    if (this.minHeap.size() > this.maxHeap.size()) {
      this.maxHeap.push(this.minHeap.pop());
    }
  }

  findMedian() {
    if (this.maxHeap.size() > this.minHeap.size()) {
      return this.maxHeap.peek();
    }
    return (this.maxHeap.peek() + this.minHeap.peek()) / 2;
  }
}
```

**关键洞察**：

- maxHeap 的堆顶 ≤ minHeap 的堆顶
- 两个堆的大小差不超过 1
- 中位数要么是 maxHeap 堆顶，要么是两个堆顶的平均值

## 堆的应用模式

| 模式 | 说明 | 例题 |
| --- | --- | --- |
| 维护 Top-K | 用大小为 K 的堆，遍历时维护 | LC 215, 347 |
| 合并 K 个有序序列 | 用堆维护 K 个指针 | LC 23 |
| 动态中位数 | 对顶堆（一大一小） | LC 295 |
| 贪心选择 | 每次取最优（最大/最小） | 各种贪心题 |

## 复杂度分析

| 题目 | 时间 | 空间 |
| --- | --- | --- |
| LC 215（堆） | O(n log k) | O(k) |
| LC 347 | O(n log k) | O(n) |
| LC 295 addNum | O(log n) | O(n) |
| LC 295 findMedian | O(1) | — |

## LeetCode 练习

- LC 215. 数组中的第 K 个最大元素 ⭐
- LC 347. 前 K 个高频元素 ⭐
- LC 295. 数据流的中位数 ⭐
- LC 23. 合并 K 个升序链表 ⭐
- LC 703. 数据流中的第 K 大元素