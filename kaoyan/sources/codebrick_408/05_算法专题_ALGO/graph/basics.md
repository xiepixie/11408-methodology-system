---
title: 图的基础：存储与遍历
source: https://www.codebrick.tech/algo-blog/posts/graph/basics.html
---

# 图的基础：存储与遍历

## 场景引入

社交网络中的好友关系、地图中的道路连接、代码中的模块依赖——这些都是图。图是最通用的数据结构，树和链表都是图的特例。

## 示例图

上图的两种存储方式：

| 邻接表 | 邻接矩阵 |
| --- | --- |
| 0 → [1, 2] | [0,1,1,0] |
| 1 → [0, 3] | [1,0,0,1] |
| 2 → [0] | [1,0,0,0] |
| 3 → [1] | [0,1,0,0] |

## DFS vs BFS 遍历流程

## 图的存储

### 邻接表（推荐）
javascript

```
// 用 Map<number, number[]> 表示
const graph = new Map();
graph.set(0, [1, 2]);
graph.set(1, [0, 3]);
graph.set(2, [0]);
graph.set(3, [1]);

// 或直接用数组
const graph2 = [[1,2], [0,3], [0], [1]];
```

空间 O(V + E)，适合稀疏图。LeetCode 大多数图题用邻接表。

### 邻接矩阵
javascript

```
// matrix[i][j] = 1 表示 i 到 j 有边
const matrix = [
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,0],
  [0,1,0,0]
];
```

空间 O(V²)，适合稠密图，查询边是否存在为 O(1)。

## DFS 遍历
javascript

```
function dfs(graph, start) {
  const visited = new Set();

  function traverse(node) {
    if (visited.has(node)) return;
    visited.add(node);
    console.log(node); // 处理节点
    for (const neighbor of graph[node]) {
      traverse(neighbor);
    }
  }

  traverse(start);
}
```

## BFS 遍历
javascript

```
function bfs(graph, start) {
  const visited = new Set([start]);
  const queue = [start];

  while (queue.length) {
    const node = queue.shift();
    console.log(node); // 处理节点
    for (const neighbor of graph[node]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }
}
```

## 图 vs 树的遍历区别

图可能有环，所以必须用 `visited` 集合防止死循环。树没有环，不需要 visited。

## LC 797. 所有可能的路径

给定有向无环图（DAG），找出从 0 到 n-1 的所有路径。javascript

```
function allPathsSourceTarget(graph) {
  const result = [];
  const target = graph.length - 1;

  function dfs(node, path) {
    if (node === target) {
      result.push([...path]);
      return;
    }
    for (const next of graph[node]) {
      path.push(next);
      dfs(next, path);
      path.pop();
    }
  }

  dfs(0, [0]);
  return result;
}
```

## 复杂度

| 算法 | 时间 | 空间 |
| --- | --- | --- |
| DFS | O(V + E) | O(V) |
| BFS | O(V + E) | O(V) |

## LeetCode 练习

- LC 797. 所有可能的路径
- LC 200. 岛屿数量（网格图 DFS）
- LC 133. 克隆图