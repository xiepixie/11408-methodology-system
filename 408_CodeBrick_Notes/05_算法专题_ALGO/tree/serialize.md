---
title: 二叉树的序列化与反序列化
source: https://www.codebrick.tech/algo-blog/posts/tree/serialize.html
---

# 二叉树的序列化与反序列化

## 场景引入

如何把一棵二叉树保存到文件里，之后再完整地恢复？这就是序列化和反序列化问题。

与"从遍历序列构造二叉树"不同，序列化需要**包含空节点信息**，这样单靠一种遍历就能唯一确定一棵树。

## 序列化与反序列化流程

## LC 297. 二叉树的序列化与反序列化

### 方法一：前序遍历
javascript

```
function serialize(root) {
  if (!root) return '#';
  return root.val + ',' + serialize(root.left) + ',' + serialize(root.right);
}

function deserialize(data) {
  const nodes = data.split(',');
  let idx = 0;

  function build() {
    if (nodes[idx] === '#') { idx++; return null; }
    const node = new TreeNode(parseInt(nodes[idx]));
    idx++;
    node.left = build();
    node.right = build();
    return node;
  }

  return build();
}
```

序列化结果示例：`1,2,#,#,3,4,#,#,5,#,#`

### 方法二：层序遍历（BFS）
javascript

```
function serialize(root) {
  if (!root) return '';
  const queue = [root];
  const result = [];

  while (queue.length) {
    const node = queue.shift();
    if (node) {
      result.push(node.val);
      queue.push(node.left);
      queue.push(node.right);
    } else {
      result.push('#');
    }
  }
  return result.join(',');
}

function deserialize(data) {
  if (!data) return null;
  const nodes = data.split(',');
  const root = new TreeNode(parseInt(nodes[0]));
  const queue = [root];
  let i = 1;

  while (queue.length) {
    const parent = queue.shift();
    if (nodes[i] !== '#') {
      parent.left = new TreeNode(parseInt(nodes[i]));
      queue.push(parent.left);
    }
    i++;
    if (nodes[i] !== '#') {
      parent.right = new TreeNode(parseInt(nodes[i]));
      queue.push(parent.right);
    }
    i++;
  }
  return root;
}
```

### 两种方法对比

|  | 前序遍历 | 层序遍历 |
| --- | --- | --- |
| 实现难度 | 简单（递归） | 中等（队列） |
| 字符串长度 | 相同（都记录空节点） | 相同 |
| 面试推荐 | 更容易写对 | 更直观 |

## 关键点

- **必须记录空节点**（用 `#` 或 `null`），否则无法唯一确定树结构
- 前序序列化时，反序列化也必须按前序顺序读取
- 层序序列化更符合人的直觉，但代码稍长

## 复杂度分析

时间 O(n)，空间 O(n)。

## LeetCode 练习

- LC 297. 二叉树的序列化与反序列化 ⭐
- LC 449. 序列化和反序列化二叉搜索树