---
title: 路径问题：二维 DP 入门
source: https://www.codebrick.tech/algo-blog/posts/dp/path.html
---

# 路径问题：二维 DP 入门

## 场景引入

一个机器人在 m×n 的网格左上角，每次只能向右或向下移动一步，到达右下角有多少种不同路径？如果网格上有权值，怎么找权值之和最小的路径？

### 网格路径 DP 方向

## LC 62. 不同路径

`dp[i][j]` = 到达 (i,j) 的路径数。javascript

```
function uniquePaths(m, n) {
  const dp = Array.from({ length: m }, () => new Array(n).fill(1));

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
  }
  return dp[m - 1][n - 1];
}
```

空间优化为一维：javascript

```
function uniquePaths(m, n) {
  const dp = new Array(n).fill(1);
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[j] += dp[j - 1];
    }
  }
  return dp[n - 1];
}
```

## LC 64. 最小路径和

`dp[i][j]` = 到达 (i,j) 的最小路径和。javascript

```
function minPathSum(grid) {
  const m = grid.length, n = grid[0].length;
  const dp = Array.from({ length: m }, () => new Array(n).fill(0));

  dp[0][0] = grid[0][0];
  for (let i = 1; i < m; i++) dp[i][0] = dp[i - 1][0] + grid[i][0];
  for (let j = 1; j < n; j++) dp[0][j] = dp[0][j - 1] + grid[0][j];

  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
    }
  }
  return dp[m - 1][n - 1];
}
```

## LC 174. 地下城游戏（反向 DP）

骑士从左上角到右下角，每个格子有正/负的生命值变化。求骑士初始最少需要多少生命值才能到达终点（全程 ≥ 1）。

**关键**：从终点向起点反向推导。javascript

```
function calculateMinimumHP(dungeon) {
  const m = dungeon.length, n = dungeon[0].length;
  // dp[i][j] = 从 (i,j) 出发到终点所需的最少生命值
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(Infinity));
  dp[m][n - 1] = dp[m - 1][n] = 1;

  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      const minNext = Math.min(dp[i + 1][j], dp[i][j + 1]);
      dp[i][j] = Math.max(minNext - dungeon[i][j], 1);
    }
  }
  return dp[0][0];
}
```

**为什么不能正向 DP？** 因为正向时，最小生命值和最大剩余生命值无法同时用一个 DP 状态表示。

## 二维 DP 模式

| 题目 | 方向 | 转移 |
| --- | --- | --- |
| LC 62 | 正向 | dp[i][j] = 上 + 左 |
| LC 64 | 正向 | dp[i][j] = min(上, 左) + grid |
| LC 174 | 反向 | dp[i][j] = max(min(下, 右) - grid, 1) |

## 复杂度

时间 O(m×n)，空间 O(m×n)，均可优化为 O(n)。

## LeetCode 练习

- LC 62. 不同路径
- LC 63. 不同路径 II（有障碍物）
- LC 64. 最小路径和 ⭐
- LC 174. 地下城游戏
- LC 931. 下降路径最小和