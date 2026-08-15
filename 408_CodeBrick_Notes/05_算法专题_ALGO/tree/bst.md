---
title: 二叉搜索树：中序有序的妙用
source: https://www.codebrick.tech/algo-blog/posts/tree/bst.html
---

# 二叉搜索树：中序有序的妙用

## 场景引入

二叉搜索树（BST）的核心性质：**左子树所有节点 < 根 < 右子树所有节点**。

这意味着 BST 的**中序遍历结果是升序的**。利用这个性质，很多问题迎刃而解。

## BST 的中序遍历 = 升序序列
javascript

```
function inorder(root) {
  if (!root) return;
  inorder(root.left);
  console.log(root.val); // 升序输出
  inorder(root.right);
}
```

### LC 230. 二叉搜索树中第 K 小的元素
javascript

```
function kthSmallest(root, k) {
  let count = 0, result = 0;
  function inorder(node) {
    if (!node) return;
    inorder(node.left);
    count++;
    if (count === k) { result = node.val; return; }
    inorder(node.right);
  }
  inorder(root);
  return result;
}
```

### LC 538. 把 BST 转换为累加树

反向中序遍历（右→根→左）= 降序遍历：javascript

```
function convertBST(root) {
  let sum = 0;
  function traverse(node) {
    if (!node) return;
    traverse(node.right);
    sum += node.val;
    node.val = sum;
    traverse(node.left);
  }
  traverse(root);
  return root;
}
```

## BST 操作流程图

## BST 的基本操作

### 查找
javascript

```
function searchBST(root, val) {
  if (!root) return null;
  if (val === root.val) return root;
  if (val < root.val) return searchBST(root.left, val);
  return searchBST(root.right, val);
}
```

### 插入
javascript

```
function insertIntoBST(root, val) {
  if (!root) return new TreeNode(val);
  if (val < root.val) root.left = insertIntoBST(root.left, val);
  else root.right = insertIntoBST(root.right, val);
  return root;
}
```

### 删除（最复杂）

删除节点有三种情况：

- **叶子节点**：直接删
- **只有一个子节点**：用子节点替代
- **有两个子节点**：用右子树最小节点（后继）替代javascript

```
function deleteNode(root, key) {
  if (!root) return null;
  if (key < root.val) {
    root.left = deleteNode(root.left, key);
  } else if (key > root.val) {
    root.right = deleteNode(root.right, key);
  } else {
    // 找到要删除的节点
    if (!root.left) return root.right;
    if (!root.right) return root.left;
    // 两个子节点：找右子树最小值替代
    let minNode = root.right;
    while (minNode.left) minNode = minNode.left;
    root.val = minNode.val;
    root.right = deleteNode(root.right, minNode.val);
  }
  return root;
}
```

### LC 98. 验证二叉搜索树
javascript

```
function isValidBST(root) {
  function validate(node, min, max) {
    if (!node) return true;
    if (node.val <= min || node.val >= max) return false;
    return validate(node.left, min, node.val)
        && validate(node.right, node.val, max);
  }
  return validate(root, -Infinity, Infinity);
}
```

## BST 操作模式
javascript

```
function BST(root, target) {
  if (root.val === target) {
    // 找到目标，做操作
  }
  if (target < root.val) {
    BST(root.left, target);  // 去左子树找
  }
  if (target > root.val) {
    BST(root.right, target); // 去右子树找
  }
}
```

利用 BST 的有序性，不需要遍历整棵树，每次排除一半——类似二分查找。

## 复杂度分析

| 操作 | 平均 | 最坏（退化为链表） |
| --- | --- | --- |
| 查找 | O(log n) | O(n) |
| 插入 | O(log n) | O(n) |
| 删除 | O(log n) | O(n) |

## LeetCode 练习

- LC 700. 二叉搜索树中的搜索
- LC 701. 二叉搜索树中的插入操作
- LC 450. 删除二叉搜索树中的节点 ⭐
- LC 98. 验证二叉搜索树 ⭐
- LC 230. 二叉搜索树中第 K 小的元素 ⭐
- LC 538. 把二叉搜索树转换为累加树
- LC 96. 不同的二叉搜索树