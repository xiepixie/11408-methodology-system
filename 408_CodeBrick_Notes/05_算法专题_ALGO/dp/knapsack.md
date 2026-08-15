---
title: 背包问题：DP 的模板题
source: https://www.codebrick.tech/algo-blog/posts/dp/knapsack.html
---

# 背包问题：DP 的模板题

## 场景引入

背包问题是动态规划中最基础、最重要的模型之一。很多看似不相关的问题（分割等和子集、目标和、零钱兑换）本质上都是背包问题的变体。

## 0-1 背包

有 N 件物品和容量为 W 的背包。第 i 件物品重量 wt[i]，价值 val[i]。每件物品只能选一次，求最大价值。

### 0-1 背包决策流程

### 二维 DP
javascript

```
function knapsack(W, wt, val) {
  const n = wt.length;
  // dp[i][w] = 前 i 件物品、容量为 w 时的最大价值
  const dp = Array.from({ length: n + 1 }, () => new Array(W + 1).fill(0));

  for (let i = 1; i <= n; i++) {
    for (let w = 1; w <= W; w++) {
      if (wt[i - 1] > w) {
        dp[i][w] = dp[i - 1][w]; // 装不下
      } else {
        dp[i][w] = Math.max(
          dp[i - 1][w],                        // 不选第 i 件
          dp[i - 1][w - wt[i - 1]] + val[i - 1] // 选第 i 件
        );
      }
    }
  }
  return dp[n][W];
}
```

### 一维优化（滚动数组）
javascript

```
function knapsack(W, wt, val) {
  const dp = new Array(W + 1).fill(0);
  for (let i = 0; i < wt.length; i++) {
    for (let w = W; w >= wt[i]; w--) { // 倒序遍历！
      dp[w] = Math.max(dp[w], dp[w - wt[i]] + val[i]);
    }
  }
  return dp[W];
}
```

关键：内层循环**倒序**，保证每件物品只用一次。

## 完全背包

每件物品可以无限次使用。

唯一区别：内层循环改为**正序**。javascript

```
for (let w = wt[i]; w <= W; w++) { // 正序！
  dp[w] = Math.max(dp[w], dp[w - wt[i]] + val[i]);
}
```

### LC 518. 零钱兑换 II

给定硬币面额和目标金额，求凑出目标金额的组合数。javascript

```
function change(amount, coins) {
  const dp = new Array(amount + 1).fill(0);
  dp[0] = 1; // base case：金额 0 有 1 种方式（不选）

  for (const coin of coins) {
    for (let j = coin; j <= amount; j++) {
      dp[j] += dp[j - coin];
    }
  }
  return dp[amount];
}
```

## 子集背包

### LC 416. 分割等和子集

判断数组能否分成两个子集，使得两个子集的元素和相等。

转化：能否从数组中选出一些数，使其和恰好等于 sum/2？→ 0-1 背包问题。javascript

```
function canPartition(nums) {
  const sum = nums.reduce((a, b) => a + b, 0);
  if (sum % 2 !== 0) return false;
  const target = sum / 2;

  const dp = new Array(target + 1).fill(false);
  dp[0] = true;

  for (const num of nums) {
    for (let j = target; j >= num; j--) {
      dp[j] = dp[j] || dp[j - num];
    }
  }
  return dp[target];
}
```

## 如何识别背包问题

| 特征 | 对应 |
| --- | --- |
| 从一组物品中选择 | 物品 |
| 有一个限制（容量/目标值） | 背包容量 |
| 每个物品只能选一次 | 0-1 背包 |
| 每个物品可以选多次 | 完全背包 |
| 求最大/最小/方案数 | DP 目标 |

## 复杂度

- 时间：O(N × W)
- 空间：O(W)（一维优化后）

## LeetCode 练习

- LC 416. 分割等和子集 ⭐（0-1 背包）
- LC 494. 目标和（0-1 背包变体）
- LC 518. 零钱兑换 II（完全背包）
- LC 322. 零钱兑换（完全背包求最小值）