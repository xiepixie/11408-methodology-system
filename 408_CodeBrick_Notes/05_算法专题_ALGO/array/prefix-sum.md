---
title: 前缀和：O(1) 区间查询的秘诀
source: https://www.codebrick.tech/algo-blog/posts/array/prefix-sum.html
---

# 前缀和：O(1) 区间查询的秘诀

## 场景引入

假设你有一个数组，需要频繁查询**任意区间 [i, j] 内元素的和**。如果每次都暴力遍历区间求和，每次查询是 O(n)。当查询次数很多时，总时间代价就很大。

前缀和的思路很简单：**提前把前 i 个元素的累加和算好存起来**，这样任意区间的和就可以通过两个前缀和相减得到，查询时间 O(1)。

这就像看银行账户余额一样 -- 你不需要把每笔交易重新加一遍，只需要用"截至今天的余额"减去"截至上月的余额"就知道这个月花了多少钱。

## 核心思路

### 一维前缀和
javascript

```
// 构建前缀和数组：prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
function buildPrefix(nums) {
  let prefix = new Array(nums.length + 1).fill(0);
  for (let i = 0; i < nums.length; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
  }
  return prefix;
}

// 查询区间 [left, right] 的和
function rangeSum(prefix, left, right) {
  return prefix[right + 1] - prefix[left];
}
```

关键点：

- `prefix` 数组长度比原数组多 1，`prefix[0] = 0` 作为哨兵
- `prefix[i]` 表示 `nums[0..i-1]` 的累加和
- 区间 `[left, right]` 的和 = `prefix[right + 1] - prefix[left]`

### 为什么用 n+1 长度？

让 `prefix[0] = 0` 可以统一公式，避免对 `left === 0` 做特殊处理。

## 可视化演示

### 一维前缀和构建与查询
加载可视化中...

## 代码实现

### LC 303. 区域和检索 - 数组不可变
javascript

```
class NumArray {
  constructor(nums) {
    this.prefix = new Array(nums.length + 1).fill(0);
    for (let i = 0; i < nums.length; i++) {
      this.prefix[i + 1] = this.prefix[i] + nums[i];
    }
  }

  sumRange(left, right) {
    return this.prefix[right + 1] - this.prefix[left];
  }
}
```

构建前缀和 O(n)，之后每次查询 O(1)。

### LC 304. 二维区域和检索 - 矩阵不可变

二维前缀和是一维的扩展。`prefix[i][j]` 表示从 `(0,0)` 到 `(i-1,j-1)` 矩形区域内所有元素的和。javascript

```
class NumMatrix {
  constructor(matrix) {
    let m = matrix.length, n = matrix[0].length;
    // prefix[i][j] = sum of matrix[0..i-1][0..j-1]
    this.prefix = Array.from({ length: m + 1 },
      () => new Array(n + 1).fill(0)
    );

    for (let i = 1; i <= m; i++) {
      for (let j = 1; j <= n; j++) {
        this.prefix[i][j] = matrix[i-1][j-1]
          + this.prefix[i-1][j]
          + this.prefix[i][j-1]
          - this.prefix[i-1][j-1];
      }
    }
  }

  sumRegion(row1, col1, row2, col2) {
    return this.prefix[row2+1][col2+1]
      - this.prefix[row1][col2+1]
      - this.prefix[row2+1][col1]
      + this.prefix[row1][col1];
  }
}
```

二维前缀和的构建用到**容斥原理**：

```
prefix[i][j] = matrix[i-1][j-1]
             + prefix[i-1][j]    (上方)
             + prefix[i][j-1]    (左方)
             - prefix[i-1][j-1]  (左上角被加了两次，减掉)
```

查询区域和同样用容斥原理：

```
sum(row1, col1, row2, col2)
  = prefix[row2+1][col2+1]
  - prefix[row1][col2+1]       (上方多余部分)
  - prefix[row2+1][col1]       (左方多余部分)
  + prefix[row1][col1]         (左上角被减了两次，加回来)
```

### LC 560. 和为 K 的子数组

前缀和的另一个经典应用：结合哈希表。javascript

```
function subarraySum(nums, k) {
  let count = 0;
  let prefixSum = 0;
  let map = new Map();
  map.set(0, 1); // 前缀和为 0 出现 1 次

  for (let num of nums) {
    prefixSum += num;
    // 如果之前有前缀和等于 prefixSum - k
    // 说明中间那段子数组的和就是 k
    if (map.has(prefixSum - k)) {
      count += map.get(prefixSum - k);
    }
    map.set(prefixSum, (map.get(prefixSum) || 0) + 1);
  }

  return count;
}
```

思路：`prefix[j] - prefix[i] = k` 等价于 `prefix[i] = prefix[j] - k`。遍历时用哈希表记录每个前缀和出现的次数。

## 复杂度分析

| 操作 | 一维前缀和 | 二维前缀和 |
| --- | --- | --- |
| 构建 | O(n) | O(m * n) |
| 查询 | O(1) | O(1) |
| 空间 | O(n) | O(m * n) |

## LeetCode 练习

按难度递进：

- LC 303. 区域和检索 - 数组不可变（简单）
- LC 304. 二维区域和检索 - 矩阵不可变（中等）
- LC 560. 和为 K 的子数组（中等）
- LC 525. 连续数组（中等）
- LC 238. 除自身以外数组的乘积（中等）— 前缀积变体
- LC 1314. 矩阵区域和（中等）