---
title: 并查集：一种优雅的连通性数据结构
source: https://www.codebrick.tech/algo-blog/posts/graph/union-find.html
---

# 并查集：一种优雅的连通性数据结构

## 场景引入

社交网络中，如何快速判断两个人是否属于同一个朋友圈？如何快速合并两个朋友圈？并查集就是为这类**动态连通性**问题而生的数据结构。

## 核心 API

- `find(x)`：找到 x 所属集合的代表元素（根节点）
- `union(x, y)`：合并 x 和 y 所在的集合
- `connected(x, y)`：判断 x 和 y 是否在同一个集合

## 并查集操作流程

## 实现

### 基础版
javascript

```
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.count = n; // 连通分量数
  }

  find(x) {
    while (this.parent[x] !== x) {
      x = this.parent[x];
    }
    return x;
  }

  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);
    if (rootX === rootY) return;
    this.parent[rootX] = rootY;
    this.count--;
  }

  connected(x, y) {
    return this.find(x) === this.find(y);
  }
}
```

### 优化版（路径压缩 + 按秩合并）
javascript

```
class UnionFind {
  constructor(n) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = new Array(n).fill(0);
    this.count = n;
  }

  find(x) {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]); // 路径压缩
    }
    return this.parent[x];
  }

  union(x, y) {
    const rootX = this.find(x);
    const rootY = this.find(y);
    if (rootX === rootY) return false;

    // 按秩合并：矮树接到高树上
    if (this.rank[rootX] < this.rank[rootY]) {
      this.parent[rootX] = rootY;
    } else if (this.rank[rootX] > this.rank[rootY]) {
      this.parent[rootY] = rootX;
    } else {
      this.parent[rootY] = rootX;
      this.rank[rootX]++;
    }
    this.count--;
    return true;
  }

  connected(x, y) {
    return this.find(x) === this.find(y);
  }
}
```

**路径压缩**：find 时直接把节点指向根，树高变为 1。 **按秩合并**：合并时把矮树接到高树下面，防止退化为链表。

两个优化同时使用，find 操作近似 O(1)（严格说是 O(α(n))，反阿克曼函数）。

## 经典应用

### LC 130. 被围绕的区域

把边界上的 O 和内部的 O 用并查集区分——边界 O 连接到一个虚拟节点，最后没连到虚拟节点的 O 就是被围绕的。

### LC 990. 等式方程的可满足性
javascript

```
function equationsPossible(equations) {
  const uf = new UnionFind(26);
  // 先处理 == 方程，合并相等的变量
  for (const eq of equations) {
    if (eq[1] === '=') {
      uf.union(eq.charCodeAt(0) - 97, eq.charCodeAt(3) - 97);
    }
  }
  // 再检查 != 方程，矛盾则返回 false
  for (const eq of equations) {
    if (eq[1] === '!') {
      if (uf.connected(eq.charCodeAt(0) - 97, eq.charCodeAt(3) - 97)) {
        return false;
      }
    }
  }
  return true;
}
```

## 复杂度

| 操作 | 优化后 |
| --- | --- |
| find | O(α(n)) ≈ O(1) |
| union | O(α(n)) ≈ O(1) |
| 空间 | O(n) |

## LeetCode 练习

- LC 130. 被围绕的区域
- LC 990. 等式方程的可满足性
- LC 947. 移除最多的同行或同列石头
- LC 200. 岛屿数量（并查集解法）
- LC 684. 冗余连接