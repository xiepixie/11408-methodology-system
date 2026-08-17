---
title: BFS 框架：最短路径的通用解法
source: https://www.codebrick.tech/algo-blog/posts/bfs/framework.html
---

# BFS 框架：最短路径的通用解法

## 场景引入

想象你站在一个迷宫的入口，要找到到出口的**最短路线**。你有两种策略：

- **DFS**（深度优先）：一条路走到黑，碰壁再回头。能找到出口，但不保证最短。
- **BFS**（广度优先）：从起点开始，先探索所有距离为 1 的位置，再探索距离为 2 的位置……**第一次到达出口时，走的一定是最短路**。

BFS 的核心价值就是：**在无权图中，BFS 天然能找到最短路径**。

## 核心思路

### BFS 模板
javascript

```
function bfs(start, target) {
  const queue = [start];
  const visited = new Set();
  visited.add(start);
  let step = 0;

  while (queue.length > 0) {
    const size = queue.length;
    // 遍历当前层的所有节点
    for (let i = 0; i < size; i++) {
      const cur = queue.shift();
      // 判断是否到达终点
      if (cur === target) return step;
      // 将相邻节点加入队列
      for (const next of getNeighbors(cur)) {
        if (!visited.has(next)) {
          visited.add(next);
          queue.push(next);
        }
      }
    }
    step++; // 层数 +1
  }
  return -1; // 无法到达
}
```

### BFS 逐层扩散流程

### BFS vs DFS 选择指南

### 模板要点

- **队列**：先进先出，保证逐层扩散
- **visited 集合**：防止走回头路，避免死循环
- **按层遍历**：内层 `for` 循环处理当前层的所有节点，`step` 记录层数
- **第一次到达即最短**：因为是逐层扩散，第一次碰到目标一定是最短路径

### BFS vs DFS 选择指南

| 场景 | 选 BFS | 选 DFS |
| --- | --- | --- |
| 求最短路径/最少步数 | 首选 | 不适合 |
| 求所有路径/方案 | 不适合 | 首选 |
| 图中存在环 | 都可以（需 visited） | 都可以（需 visited） |
| 树的层序遍历 | 首选 | 不适合 |
| 空间受限 | 占用大（存整层） | 占用小（递归栈） |

## 可视化演示

以二叉树最小深度为例，观察 BFS 逐层扩散的过程：加载可视化中...

## 代码实现

### LC 111. 二叉树的最小深度
javascript

```
function minDepth(root) {
  if (!root) return 0;
  const queue = [root];
  let depth = 1;
  while (queue.length > 0) {
    const size = queue.length;
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      // 叶子节点 → 第一次到达即最小深度
      if (!node.left && !node.right) return depth;
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    depth++;
  }
  return depth;
}
```

为什么 BFS 能求最小深度？因为它逐层遍历，第一个碰到的叶子节点一定在最浅的那一层。DFS 则需要遍历所有路径才能确定最小值。

### LC 752. 打开转盘锁

**问题**：4 位密码锁，每次可以将一个拨轮转动一格（0-9 循环），给定死锁组合 deadends，求从 "0000" 到 target 的最少步数。javascript

```
function openLock(deadends, target) {
  const dead = new Set(deadends);
  if (dead.has('0000')) return -1;

  const queue = ['0000'];
  const visited = new Set(['0000']);
  let step = 0;

  while (queue.length > 0) {
    const size = queue.length;
    for (let i = 0; i < size; i++) {
      const cur = queue.shift();
      if (cur === target) return step;

      // 每个拨轮可以向上或向下转
      for (let j = 0; j < 4; j++) {
        const up = plusOne(cur, j);
        const down = minusOne(cur, j);
        if (!visited.has(up) && !dead.has(up)) {
          visited.add(up);
          queue.push(up);
        }
        if (!visited.has(down) && !dead.has(down)) {
          visited.add(down);
          queue.push(down);
        }
      }
    }
    step++;
  }
  return -1;
}

function plusOne(s, i) {
  const arr = s.split('');
  arr[i] = arr[i] === '9' ? '0' : String(+arr[i] + 1);
  return arr.join('');
}

function minusOne(s, i) {
  const arr = s.split('');
  arr[i] = arr[i] === '0' ? '9' : String(+arr[i] - 1);
  return arr.join('');
}
```

这道题的精髓在于把**密码状态抽象为图的节点**，每次拨动就是一条边。求最少步数就是求无权图最短路径，天然适合 BFS。

### LC 200. 岛屿数量（BFS 版）

DFS 是更常见的解法（详见[[05_算法专题_ALGO/dfs/islands.md|岛屿问题系列]]），BFS 同样可以解：发现 `'1'` 时用 BFS 逐层扩散，把整个连通区域标记为 `'0'`。每次触发 BFS 就是一个新岛屿。

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 二叉树最小深度 | O(n) | O(n) 队列最大一层 |
| 转盘锁 | O(10^4 * 8) | O(10^4) visited |
| 岛屿数量 BFS | O(m * n) | O(min(m, n)) 队列 |

BFS 的空间复杂度通常高于 DFS，因为需要存储整层节点。但这是用空间换取"最短路径保证"的代价。

## 双向 BFS 优化

对于起点和终点都已知的问题（如转盘锁），可以从两端同时 BFS，在中间相遇。时间复杂度从 O(b^d) 降低到 O(b^(d/2))，其中 b 是分支因子，d 是深度。

核心思想：每次选择**节点数更少**的那一端扩展，两端交替进行。

## LeetCode 练习

- [LC 111. 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)（BFS 入门）
- [LC 102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)（BFS 基础）
- [LC 752. 打开转盘锁](https://leetcode.cn/problems/open-the-lock/)（抽象图 BFS）
- [LC 200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)（网格 BFS/DFS）
- [LC 127. 单词接龙](https://leetcode.cn/problems/word-ladder/)（双向 BFS 经典题）
- [LC 773. 滑动谜题](https://leetcode.cn/problems/sliding-puzzle/)（状态图 BFS）