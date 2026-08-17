---
title: 区间调度问题：贪心算法的经典应用
source: https://www.codebrick.tech/algo-blog/posts/greedy/interval.html
---

# 区间调度问题：贪心算法的经典应用

## 场景引入

贪心算法的核心：**每一步都做局部最优选择，期望达到全局最优**。但并非所有问题都能用贪心，区间调度问题是贪心算法的"安全区"——可以证明局部最优 = 全局最优。

### 区间调度贪心策略

## LC 435. 无重叠区间

给定区间集合，求最少需要移除多少个区间，使得剩余区间互不重叠。

**贪心策略**：按右端点排序，每次选择右端点最小的区间（给后面留更多空间）。javascript

```
function eraseOverlapIntervals(intervals) {
  intervals.sort((a, b) => a[1] - b[1]); // 按右端点排序
  let count = 0;
  let end = -Infinity;

  for (const [start, finish] of intervals) {
    if (start >= end) {
      end = finish; // 不重叠，选择这个区间
    } else {
      count++; // 重叠，移除
    }
  }
  return count;
}
```

## LC 452. 用最少数量的箭引爆气球

和 LC 435 本质相同——求最多有多少个不重叠区间（每个不重叠区间需要一支箭）。javascript

```
function findMinArrowShots(points) {
  points.sort((a, b) => a[1] - b[1]);
  let arrows = 1;
  let end = points[0][1];

  for (let i = 1; i < points.length; i++) {
    if (points[i][0] > end) {
      arrows++;
      end = points[i][1];
    }
  }
  return arrows;
}
```

## LC 56. 合并区间

**策略**：按左端点排序，依次合并有重叠的区间。javascript

```
function merge(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);
  const result = [intervals[0]];

  for (let i = 1; i < intervals.length; i++) {
    const last = result[result.length - 1];
    if (intervals[i][0] <= last[1]) {
      last[1] = Math.max(last[1], intervals[i][1]); // 合并
    } else {
      result.push(intervals[i]); // 不重叠
    }
  }
  return result;
}
```

## 区间问题套路

| 题目 | 排序方式 | 核心操作 |
| --- | --- | --- |
| 无重叠区间 | 按右端点 | 贪心选右端点最小的 |
| 合并区间 | 按左端点 | 依次合并重叠区间 |
| 引爆气球 | 按右端点 | 等同于无重叠区间 |

## 复杂度

时间 O(n log n)（排序），空间 O(1) 或 O(n)。

## LeetCode 练习

- LC 435. 无重叠区间 ⭐
- LC 452. 用最少数量的箭引爆气球
- LC 56. 合并区间 ⭐
- LC 986. 区间列表的交集
- LC 1024. 视频拼接