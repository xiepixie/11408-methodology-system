---
title: 拓扑排序：如何确定编译依赖顺序
source: https://www.codebrick.tech/algo-blog/posts/graph/topo-sort.html
---

# 拓扑排序：如何确定编译依赖顺序

## 场景引入

编译 C++ 项目时，源文件之间有 include 依赖。编译器需要确定一个编译顺序，使得每个文件在被依赖的文件之后编译。如果依赖关系形成了环，则无法编译。

这就是**拓扑排序**要解决的问题。

## 拓扑排序示例

以课程依赖为例：修课程 1 前必须先修课程 0，修课程 3 前必须先修课程 1 和 2。

Kahn 算法（BFS）执行过程：

## LC 207. 课程表（环检测）

你需要修 n 门课，部分课程有先修要求。判断是否能完成所有课程。

### BFS 解法（Kahn 算法）
javascript

```
function canFinish(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const inDegree = new Array(numCourses).fill(0);

  for (const [course, pre] of prerequisites) {
    graph[pre].push(course);
    inDegree[course]++;
  }

  // 入度为 0 的节点入队
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }

  let count = 0;
  while (queue.length) {
    const node = queue.shift();
    count++;
    for (const next of graph[node]) {
      inDegree[next]--;
      if (inDegree[next] === 0) queue.push(next);
    }
  }

  return count === numCourses; // 能处理所有节点 = 无环
}
```

### DFS 解法
javascript

```
function canFinish(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  for (const [course, pre] of prerequisites) {
    graph[pre].push(course);
  }

  // 0=未访问, 1=访问中, 2=已完成
  const state = new Array(numCourses).fill(0);

  function hasCycle(node) {
    if (state[node] === 1) return true;  // 发现环
    if (state[node] === 2) return false; // 已处理
    state[node] = 1;
    for (const next of graph[node]) {
      if (hasCycle(next)) return true;
    }
    state[node] = 2;
    return false;
  }

  for (let i = 0; i < numCourses; i++) {
    if (hasCycle(i)) return false;
  }
  return true;
}
```

## LC 210. 课程表 II（拓扑排序序列）

在 LC 207 的基础上，输出一个合法的课程学习顺序。javascript

```
function findOrder(numCourses, prerequisites) {
  const graph = Array.from({ length: numCourses }, () => []);
  const inDegree = new Array(numCourses).fill(0);

  for (const [course, pre] of prerequisites) {
    graph[pre].push(course);
    inDegree[course]++;
  }

  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }

  const order = [];
  while (queue.length) {
    const node = queue.shift();
    order.push(node);
    for (const next of graph[node]) {
      inDegree[next]--;
      if (inDegree[next] === 0) queue.push(next);
    }
  }

  return order.length === numCourses ? order : [];
}
```

## BFS vs DFS 对比

|  | BFS（Kahn） | DFS |
| --- | --- | --- |
| 思路 | 不断删除入度为 0 的节点 | 深搜标记状态，检测回边 |
| 输出拓扑序 | 入队顺序即拓扑序 | 后序逆序为拓扑序 |
| 推荐 | 更直观，面试首选 | 代码更短 |

## 复杂度

时间 O(V + E)，空间 O(V + E)。

## LeetCode 练习

- LC 207. 课程表 ⭐
- LC 210. 课程表 II ⭐
- LC 269. 火星词典