---
title: FloodFill 与岛屿问题系列
source: https://www.codebrick.tech/algo-blog/posts/dfs/islands.html
---

# FloodFill 与岛屿问题系列

## 场景引入

打开 Windows 画图工具，选择油漆桶，点击一个区域，颜色就会"蔓延"到整个连通区域。这就是 **FloodFill** 算法——从一个起点出发，向四个方向扩散，直到碰到边界或不同颜色的格子。

LeetCode 上的岛屿系列问题，本质上都是 FloodFill 的变体。掌握一个 DFS 框架，就能解决整个系列。

## 核心思路

### 网格 DFS 框架

把二维网格想象成一个图：每个格子是节点，上下左右相邻的格子之间有边。网格 DFS 就是图的 DFS：javascript

```
function dfs(grid, i, j) {
  const m = grid.length, n = grid[0].length;
  // 越界检查（相当于图遍历的 null 判断）
  if (i < 0 || j < 0 || i >= m || j >= n) return;
  // 已访问或不是目标（相当于 visited 检查）
  if (grid[i][j] === 0) return;

  grid[i][j] = 0; // 标记已访问（原地修改代替 visited 数组）

  // 向四个方向扩散
  dfs(grid, i - 1, j); // 上
  dfs(grid, i + 1, j); // 下
  dfs(grid, i, j - 1); // 左
  dfs(grid, i, j + 1); // 右
}
```

这个框架有三个关键点：

- **越界检查**代替了树遍历中的 `if (node === null) return`
- **原地标记**代替了 `visited` 集合，将访问过的 `1` 改为 `0`
- **四方向递归**代替了树的 `left/right` 递归

### FloodFill DFS 流程图

### 岛屿系列的通用套路

所有岛屿题的外层逻辑都一样：javascript

```
for (let i = 0; i < m; i++) {
  for (let j = 0; j < n; j++) {
    if (grid[i][j] === 1) {
      // 发现一个新岛屿，用 DFS 淹没整个岛
      dfs(grid, i, j);
    }
  }
}
```

不同题目只是在 DFS 过程中**收集不同的信息**。

## 可视化演示
加载可视化中...

## 代码实现

### LC 200. 岛屿数量

**问题**：计算网格中岛屿的数量。`1` 表示陆地，`0` 表示水。javascript

```
function numIslands(grid) {
  let count = 0;
  const m = grid.length, n = grid[0].length;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        count++;           // 发现新岛屿
        dfs(grid, i, j);   // 淹没整个岛
      }
    }
  }
  return count;
}

function dfs(grid, i, j) {
  const m = grid.length, n = grid[0].length;
  if (i < 0 || j < 0 || i >= m || j >= n) return;
  if (grid[i][j] === 0) return;
  grid[i][j] = 0; // 淹没
  dfs(grid, i - 1, j);
  dfs(grid, i + 1, j);
  dfs(grid, i, j - 1);
  dfs(grid, i, j + 1);
}
```

每次发现一个 `1`，就触发 DFS 把整个连通的陆地全部淹没（变成 `0`）。触发了几次 DFS，就有几个岛屿。

### LC 695. 岛屿的最大面积

**变化**：DFS 过程中累加面积。javascript

```
function maxAreaOfIsland(grid) {
  let maxArea = 0;
  const m = grid.length, n = grid[0].length;
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (grid[i][j] === 1) {
        maxArea = Math.max(maxArea, dfs(grid, i, j));
      }
    }
  }
  return maxArea;
}

function dfs(grid, i, j) {
  const m = grid.length, n = grid[0].length;
  if (i < 0 || j < 0 || i >= m || j >= n) return 0;
  if (grid[i][j] === 0) return 0;
  grid[i][j] = 0;
  return 1 + dfs(grid, i-1, j) + dfs(grid, i+1, j)
           + dfs(grid, i, j-1) + dfs(grid, i, j+1);
}
```

唯一的改动：DFS 函数返回淹没的格子数量，每个格子贡献 1。

### LC 1254. 统计封闭岛屿的数目

**变化**：靠边的岛屿不算封闭。技巧是**先用 DFS 淹没所有靠边的陆地**，再正常计数。遍历四条边，对边上的陆地调用 `dfs` 淹没，剩下的就是封闭岛屿。

### LC 1905. 统计子岛屿

**变化**：grid2 的岛屿如果所有格子在 grid1 中也是陆地，才是子岛。技巧同上：**先排除不满足条件的岛**。遍历 grid2，凡是 `grid2[i][j] === 1 && grid1[i][j] === 0` 的位置，用 DFS 淹掉。剩下的 grid2 岛屿都是子岛。

### LC 694. 不同岛屿的数量

**变化**：形状相同只算一个。技巧：用 DFS 的**遍历方向序列**编码形状（上=1/下=2/左=3/右=4，回溯用负数标记）。相同形状的岛屿 DFS 路径序列一定相同，用 `Set` 去重。

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 岛屿数量 | O(m * n) | O(m * n) 递归栈 |
| 最大面积 | O(m * n) | O(m * n) |
| 封闭岛屿 | O(m * n) | O(m * n) |
| 子岛屿 | O(m * n) | O(m * n) |
| 不同岛屿 | O(m * n) | O(m * n) |

所有题目的复杂度都是 O(m * n)，因为每个格子最多被访问一次。

## 总结：五题一框架

| 题目 | 核心变化 |
| --- | --- |
| LC 200 岛屿数量 | 基础模板，DFS 计数 |
| LC 695 最大面积 | DFS 返回面积，取最大值 |
| LC 1254 封闭岛屿 | 先淹边界，再计数 |
| LC 1905 子岛屿 | 先排除非子岛，再计数 |
| LC 694 不同岛屿 | 用 DFS 路径编码形状 |

所有变体的核心 DFS 函数几乎一模一样，区别只在外层逻辑。

## LeetCode 练习

- [LC 200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)（入门必做）
- [LC 695. 岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/)（DFS 返回值）
- [LC 1254. 统计封闭岛屿的数目](https://leetcode.cn/problems/number-of-closed-islands/)（边界处理）
- [LC 1905. 统计子岛屿](https://leetcode.cn/problems/count-sub-islands/)（双网格对比）
- [LC 694. 不同岛屿的数量](https://leetcode.cn/problems/number-of-distinct-islands/)（形状编码，会员题）
- [LC 733. 图像渲染](https://leetcode.cn/problems/flood-fill/)（原始 FloodFill）