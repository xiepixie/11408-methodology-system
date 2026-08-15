---
title: 最小生成树：Kruskal 与 Prim
source: https://www.codebrick.tech/algo-blog/posts/graph/mst.html
---

# 最小生成树：Kruskal 与 Prim

## 场景引入

要在 n 个城市之间修建公路使所有城市连通，每条路有不同的成本。如何选择 n-1 条路使得总成本最小？这就是最小生成树（MST）问题。

## MST 示例

最小生成树选择的边（总权重 = 2+1+3 = 6）：

## Kruskal vs Prim 选择

## Kruskal 算法

**思路**：贪心。按边权从小到大排序，依次加入不形成环的边。用并查集判断是否成环。javascript

```
function kruskal(n, edges) {
  edges.sort((a, b) => a[2] - b[2]); // 按权重排序
  const uf = new UnionFind(n);
  let totalCost = 0;
  let edgeCount = 0;

  for (const [u, v, weight] of edges) {
    if (uf.connected(u, v)) continue; // 会形成环，跳过
    uf.union(u, v);
    totalCost += weight;
    edgeCount++;
    if (edgeCount === n - 1) break; // n-1 条边就够了
  }

  return edgeCount === n - 1 ? totalCost : -1;
}
```

时间 O(E log E)，瓶颈在排序。

## Prim 算法

**思路**：从任意节点开始，每次选择连接已选节点和未选节点的最小边。用优先队列（堆）优化。javascript

```
function prim(n, edges) {
  // 建邻接表
  const graph = Array.from({ length: n }, () => []);
  for (const [u, v, w] of edges) {
    graph[u].push([v, w]);
    graph[v].push([u, w]);
  }

  const visited = new Set();
  const heap = new MinHeap(); // [weight, node]
  heap.push([0, 0]); // 从节点 0 开始
  let totalCost = 0;

  while (heap.size() > 0 && visited.size < n) {
    const [weight, node] = heap.pop();
    if (visited.has(node)) continue;
    visited.add(node);
    totalCost += weight;

    for (const [next, w] of graph[node]) {
      if (!visited.has(next)) {
        heap.push([w, next]);
      }
    }
  }

  return visited.size === n ? totalCost : -1;
}
```

时间 O(E log V)。

## Kruskal vs Prim

|  | Kruskal | Prim |
| --- | --- | --- |
| 核心数据结构 | 并查集 | 优先队列 |
| 时间复杂度 | O(E log E) | O(E log V) |
| 适合场景 | 稀疏图（边少） | 稠密图（边多） |
| 实现难度 | 简单（排序+并查集） | 中等（需要堆） |

## LC 1584. 连接所有点的最小费用
javascript

```
function minCostConnectPoints(points) {
  const n = points.length;
  const edges = [];
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const dist = Math.abs(points[i][0] - points[j][0])
                 + Math.abs(points[i][1] - points[j][1]);
      edges.push([i, j, dist]);
    }
  }
  return kruskal(n, edges);
}
```

## LeetCode 练习

- LC 1135. 最低成本联通所有城市
- LC 1584. 连接所有点的最小费用
- LC 1319. 连通网络的操作次数