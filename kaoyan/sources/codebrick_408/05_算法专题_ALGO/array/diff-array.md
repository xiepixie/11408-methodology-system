---
title: 差分数组：高效处理区间修改
source: https://www.codebrick.tech/algo-blog/posts/array/diff-array.html
---

# 差分数组：高效处理区间修改

## 场景引入

假设你有一个数组，需要对它进行**多次区间修改**操作：把下标 [i, j] 之间的所有元素都加上一个值 val。暴力做法每次修改需要遍历区间 O(n)，如果有 m 次修改就是 O(m*n)。

差分数组可以把每次区间修改降到 O(1)，最后一次性还原结果。这个技巧和前缀和恰好是**互逆操作**：前缀和解决区间查询，差分数组解决区间修改。

想象一个场景：公交车沿途有 n 个站，每组乘客在站 i 上车、站 j 下车。你需要求每一站车上有多少人。差分数组就是解决这类问题的利器。

## 核心思路

### 差分数组的定义

对于原数组 `nums`，其差分数组 `diff` 定义为：

```
diff[0] = nums[0]
diff[i] = nums[i] - nums[i-1]  (i >= 1)
```

差分数组有一个关键性质：**对差分数组求前缀和就能还原原数组**。

### 区间修改的 O(1) 操作

要对区间 `[left, right]` 的所有元素加上 `val`，只需要：javascript

```
diff[left] += val;
if (right + 1 < diff.length) {
  diff[right + 1] -= val;
}
```

为什么这样就行？因为差分数组还原时做前缀和：

- `diff[left] += val` 使得从 left 开始，后面所有元素都会被加上 val
- `diff[right+1] -= val` 使得从 right+1 开始，抵消掉之前加的 val
- 最终效果就是只有 `[left, right]` 区间被加了 valjavascript

```
// 差分数组工具类
class DiffArray {
  constructor(nums) {
    this.diff = new Array(nums.length).fill(0);
    this.diff[0] = nums[0];
    for (let i = 1; i < nums.length; i++) {
      this.diff[i] = nums[i] - nums[i - 1];
    }
  }

  // 对区间 [left, right] 加 val，O(1)
  increment(left, right, val) {
    this.diff[left] += val;
    if (right + 1 < this.diff.length) {
      this.diff[right + 1] -= val;
    }
  }

  // 还原原数组，O(n)
  restore() {
    let res = new Array(this.diff.length);
    res[0] = this.diff[0];
    for (let i = 1; i < this.diff.length; i++) {
      res[i] = res[i - 1] + this.diff[i];
    }
    return res;
  }
}
```

## 可视化演示

### 差分数组构建与区间修改
加载可视化中...

## 代码实现

### LC 370. 区间加法

给定长度为 n 的全零数组，执行多次区间加法操作 `[startIndex, endIndex, inc]`，返回最终数组。javascript

```
function getModifiedArray(length, updates) {
  let diff = new Array(length).fill(0);

  for (let [start, end, inc] of updates) {
    diff[start] += inc;
    if (end + 1 < length) {
      diff[end + 1] -= inc;
    }
  }

  // 前缀和还原
  for (let i = 1; i < length; i++) {
    diff[i] += diff[i - 1];
  }

  return diff;
}
```

注意：初始数组全零时，差分数组也全零，所以可以直接在差分数组上操作。

### LC 1094. 拼车
javascript

```
function carPooling(trips, capacity) {
  // 站点范围 0~1000
  let diff = new Array(1001).fill(0);

  for (let [numPassengers, from, to] of trips) {
    diff[from] += numPassengers;  // from 站上车
    diff[to] -= numPassengers;    // to 站下车（注意：到站就下车）
  }

  // 前缀和还原，检查每站是否超载
  let current = 0;
  for (let i = 0; i < diff.length; i++) {
    current += diff[i];
    if (current > capacity) {
      return false;
    }
  }

  return true;
}
```

注意这题 `to` 处直接减，而不是 `to + 1`。因为题意是乘客在 `to` 站下车，到 `to` 站时已经不在车上了。

### LC 1109. 航班预订统计
javascript

```
function corpFlightBookings(bookings, n) {
  let diff = new Array(n).fill(0);

  for (let [first, last, seats] of bookings) {
    diff[first - 1] += seats;      // 1-indexed 转 0-indexed
    if (last < n) {
      diff[last] -= seats;
    }
  }

  // 前缀和还原
  for (let i = 1; i < n; i++) {
    diff[i] += diff[i - 1];
  }

  return diff;
}
```

## 前缀和与差分数组的对偶关系

|  | 前缀和 | 差分数组 |
| --- | --- | --- |
| 擅长 | 区间查询 O(1) | 区间修改 O(1) |
| 构建 | 累加求和 | 相邻做差 |
| 还原 | 相邻做差 → 原数组 | 累加求和 → 原数组 |
| 关系 | 差分数组的前缀和 = 原数组 | 前缀和数组的差分 = 原数组 |

## 复杂度分析

| 操作 | 时间复杂度 |
| --- | --- |
| 构建差分数组 | O(n) |
| 单次区间修改 | O(1) |
| 还原原数组 | O(n) |
| m 次修改 + 还原 | O(m + n) |

对比暴力的 O(m * n)，当修改次数 m 很大时优势明显。

## LeetCode 练习

按难度递进：

- LC 370. 区间加法（中等）
- LC 1109. 航班预订统计（中等）
- LC 1094. 拼车（中等）
- LC 253. 会议室 II（中等）— 差分思想的变体
- LC 732. 我的日程安排表 III（困难）