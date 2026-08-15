---
title: 二叉树的递归思维：遍历 vs 分解
source: https://www.codebrick.tech/algo-blog/posts/tree/recursion.html
---

# 二叉树的递归思维：遍历 vs 分解

## 场景引入

很多人觉得二叉树的递归"玄学"——能看懂答案，但自己写不出来。原因是没有理解递归的两种模式。

掌握这两种模式后，二叉树问题就变成了填空题：**我应该在哪个位置做什么操作？**

## 两种递归模式

### 模式一：遍历思维

像遍历数组一样遍历二叉树，用**外部变量**记录结果。javascript

```
// 求二叉树最大深度 — 遍历思维
let maxDepth = 0;
function traverse(root, depth) {
  if (root === null) return;
  // 到达叶子节点，更新最大深度
  if (!root.left && !root.right) {
    maxDepth = Math.max(maxDepth, depth);
  }
  traverse(root.left, depth + 1);
  traverse(root.right, depth + 1);
}
```

特点：**自顶向下传递参数**，需要外部变量收集结果。

### 模式二：分解思维

把问题分解为子问题，通过**返回值**向上汇报。javascript

```
// 求二叉树最大深度 — 分解思维
function maxDepth(root) {
  if (root === null) return 0;
  const leftMax = maxDepth(root.left);
  const rightMax = maxDepth(root.right);
  return Math.max(leftMax, rightMax) + 1;
}
```

特点：**自底向上汇总结果**，利用返回值，不需要外部变量。

### 决策流程图

### 如何选择？

|  | 遍历思维 | 分解思维 |
| --- | --- | --- |
| 数据流向 | 自顶向下（参数传递） | 自底向上（返回值汇总） |
| 外部变量 | 需要 | 不需要 |
| 适用场景 | 需要遍历路径信息 | 需要子树的汇总信息 |
| 代码位置 | 前序位置 | 后序位置 |

经验法则：如果题目需要子树的信息（如高度、节点数），优先用分解思维。

## 前序 vs 后序的意义
javascript

```
function traverse(root) {
  if (!root) return;
  // 【前序位置】—— 进入节点时执行
  // 此时只知道从根到当前节点的路径信息
  traverse(root.left);
  // 【中序位置】
  traverse(root.right);
  // 【后序位置】—— 离开节点时执行
  // 此时已经知道左右子树的所有信息
}
```

## 经典例题

### LC 226. 翻转二叉树（分解思维）
javascript

```
function invertTree(root) {
  if (!root) return null;
  const left = invertTree(root.left);
  const right = invertTree(root.right);
  root.left = right;
  root.right = left;
  return root;
}
```

### LC 543. 二叉树的直径（后序位置）

直径 = 经过某个节点的左子树深度 + 右子树深度的最大值。javascript

```
function diameterOfBinaryTree(root) {
  let maxDiameter = 0;
  function maxDepth(node) {
    if (!node) return 0;
    const left = maxDepth(node.left);
    const right = maxDepth(node.right);
    // 后序位置：左右子树深度都知道了
    maxDiameter = Math.max(maxDiameter, left + right);
    return Math.max(left, right) + 1;
  }
  maxDepth(root);
  return maxDiameter;
}
```

### LC 114. 二叉树展开为链表（后序）
javascript

```
function flatten(root) {
  if (!root) return;
  flatten(root.left);
  flatten(root.right);
  // 后序位置：左右子树已经展开为链表
  const left = root.left;
  const right = root.right;
  root.left = null;
  root.right = left;
  let p = root;
  while (p.right) p = p.right;
  p.right = right;
}
```

### LC 236. 最近公共祖先（后序经典）
javascript

```
function lowestCommonAncestor(root, p, q) {
  if (!root || root === p || root === q) return root;
  const left = lowestCommonAncestor(root.left, p, q);
  const right = lowestCommonAncestor(root.right, p, q);
  if (left && right) return root; // p 和 q 分别在左右子树
  return left || right;
}
```

## 复杂度分析

所有递归遍历：时间 O(n)，空间 O(h)，h 为树高（最坏 O(n)）。

## LeetCode 练习

- LC 104. 二叉树的最大深度 ⭐（两种思维都试一遍）
- LC 226. 翻转二叉树 ⭐
- LC 543. 二叉树的直径 ⭐
- LC 114. 二叉树展开为链表 ⭐
- LC 116. 填充每个节点的下一个右侧节点指针
- LC 124. 二叉树中的最大路径和 ⭐
- LC 236. 二叉树的最近公共祖先 ⭐