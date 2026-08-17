---
title: 子序列问题：LIS 与 LCS
source: https://www.codebrick.tech/algo-blog/posts/dp/subsequence.html
---

# 子序列问题：LIS 与 LCS

## 最长递增子序列（LIS）

### LC 300. 最长递增子序列

给定数组 nums，找到最长严格递增子序列的长度。

#### DP 解法 O(n²)

`dp[i]` = 以 `nums[i]` 结尾的最长递增子序列长度。javascript

```
function lengthOfLIS(nums) {
  const n = nums.length;
  const dp = new Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[j] < nums[i]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }
  return Math.max(...dp);
}
```

#### 贪心 + 二分 O(n log n)

维护一个 `tails` 数组，`tails[i]` 表示长度为 `i+1` 的递增子序列的最小末尾元素。javascript

```
function lengthOfLIS(nums) {
  const tails = [];
  for (const num of nums) {
    let lo = 0, hi = tails.length;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (tails[mid] < num) lo = mid + 1;
      else hi = mid;
    }
    tails[lo] = num;
  }
  return tails.length;
}
```

### LIS 状态转移图

## 最长公共子序列（LCS）

### LC 1143. 最长公共子序列

给定两个字符串 text1 和 text2，返回它们的最长公共子序列的长度。

`dp[i][j]` = `text1[0..i-1]` 和 `text2[0..j-1]` 的 LCS 长度。javascript

```
function longestCommonSubsequence(text1, text2) {
  const m = text1.length, n = text2.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (text1[i - 1] === text2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[m][n];
}
```

**状态转移**：

- 字符相同：`dp[i][j] = dp[i-1][j-1] + 1`
- 字符不同：`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

### LCS 状态转移图

## LCS 的变体

### LC 583. 两个字符串的删除操作

最少删除次数 = `m + n - 2 * LCS(s1, s2)`

### LC 712. 两个字符串的最小 ASCII 删除和

把 LCS 中的"长度"换成"ASCII 值之和"即可。

## 复杂度

| 题目 | 时间 | 空间 |
| --- | --- | --- |
| LIS（DP） | O(n²) | O(n) |
| LIS（贪心+二分） | O(n log n) | O(n) |
| LCS | O(mn) | O(mn)，可优化为 O(n) |

## LeetCode 练习

- LC 300. 最长递增子序列 ⭐
- LC 354. 俄罗斯套娃信封问题
- LC 1143. 最长公共子序列 ⭐
- LC 583. 两个字符串的删除操作
- LC 712. 两个字符串的最小 ASCII 删除和