---
title: 二叉树遍历框架：DFS 与 BFS
source: https://www.codebrick.tech/algo-blog/posts/tree/traversal.html
---

# 二叉树遍历框架：DFS 与 BFS

## 场景引入

二叉树是面试中**题量最大**的数据结构。几乎所有二叉树题目都建立在遍历的基础上——你能遍历二叉树，就能解决绝大多数二叉树问题。

理解前序、中序、后序的含义，不仅仅是记住"根左右"、"左根右"、"左右根"的顺序，更重要的是理解：**前序位置是进入节点时执行，后序位置是离开节点时执行**。

## 核心框架

二叉树的遍历框架只有两种：**DFS（深度优先）** 和 **BFS（广度优先）**。

### DFS 递归框架
javascript

```
function traverse(root) {
  if (root === null) return;

  // 前序位置：进入节点时
  traverse(root.left);
  // 中序位置：左子树遍历完时
  traverse(root.right);
  // 后序位置：离开节点时
}
```

这个框架是所有二叉树递归解法的基础。不同题目只是在不同"位置"做不同的事。

### BFS 层序遍历框架
javascript

```
function levelOrder(root) {
  if (!root) return [];
  const queue = [root];
  const result = [];

  while (queue.length > 0) {
    const levelSize = queue.length;
    const level = [];
    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      level.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    result.push(level);
  }
  return result;
}
```

## 可视化演示

### 前序遍历（根→左→右）
加载可视化中...

## 三种遍历的本质区别

```
      1
     / \
    2   3
   / \   \
  4   5   6
```

| 遍历方式 | 结果 | 理解 |
| --- | --- | --- |
| 前序 | 1,2,4,5,3,6 | 第一次到达节点时记录 |
| 中序 | 4,2,5,1,3,6 | 左子树遍历完后记录 |
| 后序 | 4,5,2,6,3,1 | 左右子树都遍历完后记录 |
| 层序 | [1],[2,3],[4,5,6] | 一层一层从左到右 |

## 前序/中序/后序的意义

- **前序位置**：刚进入节点，适合做"自顶向下"的操作（如传递参数给子节点）
- **中序位置**：左子树遍历完，对 BST 来说就是升序遍历
- **后序位置**：即将离开节点，适合做"自底向上"的操作（如收集子树信息）

理解这三个位置的含义，比死记遍历顺序重要 100 倍。

## 复杂度分析

|  | DFS | BFS |
| --- | --- | --- |
| 时间 | O(n) | O(n) |
| 空间 | O(h)，h 为树高 | O(w)，w 为最大宽度 |

## LeetCode 练习

- LC 144. 二叉树的前序遍历
- LC 94. 二叉树的中序遍历
- LC 145. 二叉树的后序遍历
- LC 102. 二叉树的层序遍历
- LC 104. 二叉树的最大深度（前序 or 后序都能做）
- LC 226. 翻转二叉树（前序位置操作）