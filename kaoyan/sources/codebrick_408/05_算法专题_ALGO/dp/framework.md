---
title: 动态规划核心框架
source: https://www.codebrick.tech/algo-blog/posts/dp/framework.html
---

# 动态规划核心框架

## 场景引入

给你若干面额的硬币和一个目标金额，问你**最少**需要几枚硬币凑出这个金额？

这就是经典的**零钱兑换**问题（LC 322），也是理解动态规划的最佳入门题。

## 动态规划 = 穷举 + 备忘录

动态规划的本质是**穷举**——把所有可能的选择都试一遍，找到最优解。但暴力穷举效率太低，所以用**备忘录**（或 dp 数组）来记录已算过的子问题，避免重复计算。

### 三步走框架

写出动态规划解法，只需要思考三个问题：

- **状态**：什么在变化？→ 目标金额在减少
- **选择**：每一步有哪些选择？→ 选择用哪种面额的硬币
- **base case**：最小子问题的答案？→ 金额为 0 时需要 0 枚硬币

写出状态转移方程：

```
dp[amount] = min(dp[amount - coin] + 1)  对所有 coin in coins
```

### DP 三步演进流程

### 状态转移思考框架

## 从暴力递归到动态规划

### 第一步：暴力递归
javascript

```
function coinChange(coins, amount) {
  // base case
  if (amount === 0) return 0;
  if (amount < 0) return -1;

  let res = Infinity;
  for (const coin of coins) {
    const sub = coinChange(coins, amount - coin);
    if (sub === -1) continue;
    res = Math.min(res, sub + 1);
  }
  return res === Infinity ? -1 : res;
}
```

问题：存在大量重复计算。`coinChange(coins, 11)` 会多次计算 `coinChange(coins, 9)`。

### 第二步：加备忘录
javascript

```
function coinChange(coins, amount) {
  const memo = new Array(amount + 1).fill(-2); // -2 表示未计算

  function dp(n) {
    if (n === 0) return 0;
    if (n < 0) return -1;
    if (memo[n] !== -2) return memo[n]; // 查备忘录

    let res = Infinity;
    for (const coin of coins) {
      const sub = dp(n - coin);
      if (sub === -1) continue;
      res = Math.min(res, sub + 1);
    }
    memo[n] = res === Infinity ? -1 : res; // 存备忘录
    return memo[n];
  }

  return dp(amount);
}
```

### 第三步：自底向上 dp 数组
javascript

```
function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0; // base case

  for (let i = 1; i <= amount; i++) {
    for (const coin of coins) {
      if (i - coin < 0) continue;
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  return dp[amount] > amount ? -1 : dp[amount];
}

coinChange([1, 2, 5], 11); // 输出 3（5+5+1）
```

## 可视化演示
加载可视化中...

## 如何推导状态转移方程

遇到 DP 题目，按这个顺序思考：

- **确定状态**：哪些变量描述了当前子问题？
- **确定选择**：每个状态下可以做什么决策？
- **确定 dp 数组含义**：`dp[i]` 代表什么？
- **写出转移方程**：`dp[i]` 和 `dp[i-1]`（或其他状态）的关系
- **确定 base case**：最小子问题的答案

## 复杂度分析

以零钱兑换为例：

- **时间复杂度**：O(amount × n)，n 为硬币种类数
- **空间复杂度**：O(amount)

## LeetCode 练习

入门级 DP（掌握框架）：

- LC 509. 斐波那契数
- LC 322. 零钱兑换 ⭐
- LC 70. 爬楼梯

进阶（更复杂的状态定义）：

- LC 300. 最长递增子序列 ⭐
- LC 72. 编辑距离 ⭐
- LC 121. 买卖股票的最佳时机 ⭐