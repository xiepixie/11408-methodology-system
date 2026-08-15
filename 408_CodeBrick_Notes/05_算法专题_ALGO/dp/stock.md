---
title: 股票买卖系列：状态机 DP
source: https://www.codebrick.tech/algo-blog/posts/dp/stock.html
---

# 股票买卖系列：状态机 DP

## 场景引入

LeetCode 有 6 道股票买卖问题（121/122/123/188/309/714），看似各不相同，实际上可以用**一个状态机框架**全部解决。

## 统一框架

定义状态：`dp[i][k][s]`

- `i`：第 i 天
- `k`：最多还能交易 k 次
- `s`：0 = 不持有股票，1 = 持有股票

状态转移：

```
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
              // 今天不操作       // 今天卖出

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
              // 今天不操作       // 今天买入（消耗一次交易）
```

### 股票买卖状态机

## LC 121. 买卖股票的最佳时机（k=1）
javascript

```
function maxProfit(prices) {
  let minPrice = Infinity;
  let maxProfit = 0;
  for (const price of prices) {
    minPrice = Math.min(minPrice, price);
    maxProfit = Math.max(maxProfit, price - minPrice);
  }
  return maxProfit;
}
```

## LC 122. 买卖股票的最佳时机 II（k=∞）
javascript

```
function maxProfit(prices) {
  let dp_i_0 = 0, dp_i_1 = -Infinity;
  for (const price of prices) {
    const temp = dp_i_0;
    dp_i_0 = Math.max(dp_i_0, dp_i_1 + price);
    dp_i_1 = Math.max(dp_i_1, temp - price);
  }
  return dp_i_0;
}
```

## LC 309. 含冷冻期（k=∞，卖出后等一天）
javascript

```
function maxProfit(prices) {
  let dp_i_0 = 0, dp_i_1 = -Infinity, dp_prev_0 = 0;
  for (const price of prices) {
    const temp = dp_i_0;
    dp_i_0 = Math.max(dp_i_0, dp_i_1 + price);
    dp_i_1 = Math.max(dp_i_1, dp_prev_0 - price); // 用前天的状态
    dp_prev_0 = temp;
  }
  return dp_i_0;
}
```

## LC 714. 含手续费（k=∞，每次交易扣费）
javascript

```
function maxProfit(prices, fee) {
  let dp_i_0 = 0, dp_i_1 = -Infinity;
  for (const price of prices) {
    const temp = dp_i_0;
    dp_i_0 = Math.max(dp_i_0, dp_i_1 + price);
    dp_i_1 = Math.max(dp_i_1, temp - price - fee); // 买入时扣手续费
  }
  return dp_i_0;
}
```

## LC 123. 最多两次交易（k=2）
javascript

```
function maxProfit(prices) {
  let dp_10 = 0, dp_11 = -Infinity;
  let dp_20 = 0, dp_21 = -Infinity;
  for (const price of prices) {
    dp_20 = Math.max(dp_20, dp_21 + price);
    dp_21 = Math.max(dp_21, dp_10 - price);
    dp_10 = Math.max(dp_10, dp_11 + price);
    dp_11 = Math.max(dp_11, -price);
  }
  return dp_20;
}
```

## LC 188. 最多 k 次交易
javascript

```
function maxProfit(k, prices) {
  const n = prices.length;
  if (k >= n / 2) {
    // k 足够大，等同于无限次交易
    let profit = 0;
    for (let i = 1; i < n; i++) {
      if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
    }
    return profit;
  }

  const dp = Array.from({ length: k + 1 }, () => [0, -Infinity]);
  for (const price of prices) {
    for (let j = k; j >= 1; j--) {
      dp[j][0] = Math.max(dp[j][0], dp[j][1] + price);
      dp[j][1] = Math.max(dp[j][1], dp[j - 1][0] - price);
    }
  }
  return dp[k][0];
}
```

## 总结

| 题目 | k | 特殊条件 |
| --- | --- | --- |
| LC 121 | 1 | 无 |
| LC 122 | ∞ | 无 |
| LC 123 | 2 | 无 |
| LC 188 | 任意 k | 无 |
| LC 309 | ∞ | 冷冻期 |
| LC 714 | ∞ | 手续费 |

**一个框架，六道题。** 状态机 DP 的威力。

## LeetCode 练习

- LC 121/122/123/188/309/714 全部做一遍 ⭐