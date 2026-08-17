---
title: 二分图判定
source: https://www.codebrick.tech/algo-blog/posts/graph/bipartite.html
---

# 二分图判定

## 场景引入

二分图是指图的节点可以分成两组，使得每条边都连接不同组的节点。判断一个图是否是二分图，本质上是一个**图着色问题**：能否用两种颜色给节点染色，使得相邻节点颜色不同？

## 二分图示例

每条边都连接不同组的节点 -- 这就是二分图。

## 染色判定流程

## 核心思路：BFS/DFS 染色

从任意节点开始，染颜色 0。所有邻居染颜色 1。邻居的邻居染颜色 0...如果发现某个邻居已经被染了**相同颜色**，则不是二分图。

## LC 785. 判断二分图

### BFS 解法
javascript

```
function isBipartite(graph) {
  const n = graph.length;
  const color = new Array(n).fill(-1); // -1 = 未染色

  for (let i = 0; i < n; i++) {
    if (color[i] !== -1) continue;
    // BFS 染色
    const queue = [i];
    color[i] = 0;
    while (queue.length) {
      const node = queue.shift();
      for (const neighbor of graph[node]) {
        if (color[neighbor] === -1) {
          color[neighbor] = 1 - color[node]; // 染相反颜色
          queue.push(neighbor);
        } else if (color[neighbor] === color[node]) {
          return false; // 同色相邻，不是二分图
        }
      }
    }
  }
  return true;
}
```

### DFS 解法
javascript

```
function isBipartite(graph) {
  const n = graph.length;
  const color = new Array(n).fill(-1);

  function dfs(node, c) {
    color[node] = c;
    for (const neighbor of graph[node]) {
      if (color[neighbor] === -1) {
        if (!dfs(neighbor, 1 - c)) return false;
      } else if (color[neighbor] === c) {
        return false;
      }
    }
    return true;
  }

  for (let i = 0; i < n; i++) {
    if (color[i] === -1 && !dfs(i, 0)) return false;
  }
  return true;
}
```

## LC 886. 可能的二分法

将 n 个人分成两组，给定"不喜欢"关系，能否分成两组使得不喜欢的人不在同一组？

本质就是建图 + 二分图判定：javascript

```
function possibleBipartition(n, dislikes) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [a, b] of dislikes) {
    graph[a].push(b);
    graph[b].push(a);
  }
  // 复用上面的二分图判定代码
  const color = new Array(n + 1).fill(-1);
  for (let i = 1; i <= n; i++) {
    if (color[i] === -1 && !dfs(graph, color, i, 0)) return false;
  }
  return true;
}
```

## 复杂度

时间 O(V + E)，空间 O(V)。

## LeetCode 练习

- LC 785. 判断二分图
- LC 886. 可能的二分法