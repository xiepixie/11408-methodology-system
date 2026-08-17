---
title: 最短路径：Dijkstra 算法
source: https://www.codebrick.tech/algo-blog/posts/graph/dijkstra.html
---

# 最短路径：Dijkstra 算法

## 场景引入

地图导航软件是如何计算最快路线的？从起点到终点有无数条路径，怎样高效找到最短的那条？

Dijkstra 算法就是解决**单源最短路径**问题的经典方法——从一个起点出发，找到到所有其他节点的最短距离。

## 最短路径示例

从 A 出发的最短距离：A=0, B=2, C=5（经B）, D=3（经B）

## 核心思路

Dijkstra 本质是 **BFS + 贪心**：每次从未确定的节点中选择距离最小的，确定它的最短距离，然后更新它的邻居。用优先队列（最小堆）加速选择过程。

## 模板代码
javascript

```
function dijkstra(graph, start) {
  const n = graph.length;
  const dist = new Array(n).fill(Infinity);
  dist[start] = 0;

  // 最小堆：[距离, 节点]
  const heap = new MinHeap();
  heap.push([0, start]);

  while (heap.size() > 0) {
    const [d, node] = heap.pop();

    // 已经有更短的路径了，跳过
    if (d > dist[node]) continue;

    for (const [next, weight] of graph[node]) {
      const newDist = dist[node] + weight;
      if (newDist < dist[next]) {
        dist[next] = newDist;
        heap.push([newDist, next]);
      }
    }
  }

  return dist;
}
```

## LC 743. 网络延迟时间

有 n 个节点和有向加权边，从节点 k 发送信号，返回所有节点收到信号的最短时间。如果不能到达所有节点，返回 -1。javascript

```
function networkDelayTime(times, n, k) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [u, v, w] of times) {
    graph[u].push([v, w]);
  }

  const dist = dijkstra(graph, k, n);

  let maxDist = 0;
  for (let i = 1; i <= n; i++) {
    if (dist[i] === Infinity) return -1;
    maxDist = Math.max(maxDist, dist[i]);
  }
  return maxDist;
}

function dijkstra(graph, start, n) {
  const dist = new Array(n + 1).fill(Infinity);
  dist[start] = 0;
  // 简化：用数组模拟堆
  const pq = [[0, start]];

  while (pq.length) {
    pq.sort((a, b) => a[0] - b[0]);
    const [d, node] = pq.shift();
    if (d > dist[node]) continue;
    for (const [next, weight] of graph[node]) {
      if (dist[node] + weight < dist[next]) {
        dist[next] = dist[node] + weight;
        pq.push([dist[next], next]);
      }
    }
  }
  return dist;
}
```

注：面试时可用数组排序模拟堆。生产环境应使用真正的 MinHeap。

## Dijkstra 的限制

- **不能处理负权边**。负权边可能导致已确定的最短距离被更新，破坏贪心策略。
- 负权边需要用 Bellman-Ford 算法。

## 复杂度

| 实现 | 时间 |
| --- | --- |
| 朴素（遍历找最小） | O(V²) |
| 优先队列优化 | O(E log V) |

空间 O(V + E)。

## LeetCode 练习

- LC 743. 网络延迟时间 ⭐
- LC 1514. 概率最大的路径
- LC 1631. 最小体力消耗路径
- LC 787. K 站中转内最便宜的航班