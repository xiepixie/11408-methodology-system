---
title: 构造二叉树
source: https://www.codebrick.tech/algo-blog/posts/tree/construct.html
---

# 构造二叉树

## 场景引入

给你一棵二叉树的前序遍历和中序遍历结果，你能还原出这棵树吗？这是数据结构课的经典问题，也是面试高频题。

核心思路：前序遍历的第一个元素是根节点，用它在中序遍历中定位，就能划分左右子树。

## 核心框架

构造二叉树的通用模式：

- 确定根节点
- 递归构造左子树
- 递归构造右子树

## 构造流程图

## LC 105. 从前序与中序遍历序列构造二叉树

```
前序: [3, 9, 20, 15, 7]  → 根在最前
中序: [9, 3, 15, 20, 7]  → 根的左边是左子树，右边是右子树
```
javascript

```
function buildTree(preorder, inorder) {
  const inMap = new Map();
  inorder.forEach((val, idx) => inMap.set(val, idx));

  function build(preStart, preEnd, inStart, inEnd) {
    if (preStart > preEnd) return null;

    const rootVal = preorder[preStart];
    const root = new TreeNode(rootVal);
    const inRoot = inMap.get(rootVal);
    const leftSize = inRoot - inStart;

    root.left = build(preStart + 1, preStart + leftSize, inStart, inRoot - 1);
    root.right = build(preStart + leftSize + 1, preEnd, inRoot + 1, inEnd);
    return root;
  }

  return build(0, preorder.length - 1, 0, inorder.length - 1);
}
```

**关键**：用 HashMap 预存中序遍历的值→下标映射，避免每次 O(n) 查找。

## LC 106. 从中序与后序遍历序列构造二叉树

后序遍历的**最后一个元素**是根节点，其余逻辑相同。javascript

```
function buildTree(inorder, postorder) {
  const inMap = new Map();
  inorder.forEach((val, idx) => inMap.set(val, idx));

  function build(inStart, inEnd, postStart, postEnd) {
    if (inStart > inEnd) return null;

    const rootVal = postorder[postEnd];
    const root = new TreeNode(rootVal);
    const inRoot = inMap.get(rootVal);
    const leftSize = inRoot - inStart;

    root.left = build(inStart, inRoot - 1, postStart, postStart + leftSize - 1);
    root.right = build(inRoot + 1, inEnd, postStart + leftSize, postEnd - 1);
    return root;
  }

  return build(0, inorder.length - 1, 0, postorder.length - 1);
}
```

## LC 654. 最大二叉树

根节点是数组最大值，左子树由最大值左边的子数组构建，右子树由右边的子数组构建。javascript

```
function constructMaximumBinaryTree(nums) {
  function build(lo, hi) {
    if (lo > hi) return null;
    let maxIdx = lo;
    for (let i = lo + 1; i <= hi; i++) {
      if (nums[i] > nums[maxIdx]) maxIdx = i;
    }
    const root = new TreeNode(nums[maxIdx]);
    root.left = build(lo, maxIdx - 1);
    root.right = build(maxIdx + 1, hi);
    return root;
  }
  return build(0, nums.length - 1);
}
```

## 构造类题目的统一模式

```
1. 找到根节点（前序第一个 / 后序最后一个 / 数组最大值）
2. 确定左右子树的范围（用中序定位 / 用规则划分）
3. 递归构造左右子树
```

## 复杂度分析

| 题目 | 时间 | 空间 |
| --- | --- | --- |
| LC 105/106 | O(n)（用 HashMap） | O(n) |
| LC 654 | O(n²) 最坏 | O(n) |

## LeetCode 练习

- LC 105. 从前序与中序遍历序列构造二叉树 ⭐
- LC 106. 从中序与后序遍历序列构造二叉树
- LC 654. 最大二叉树
- LC 889. 根据前序和后序遍历构造二叉树