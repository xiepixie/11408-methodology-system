---
title: 打家劫舍系列
source: https://www.codebrick.tech/algo-blog/posts/dp/house-robber.html
---

# 打家劫舍系列

### 打家劫舍状态转移

## LC 198. 打家劫舍

不能偷相邻的房屋，求能偷到的最大金额。

`dp[i]` = 前 i 间房能偷到的最大金额。javascript

```
function rob(nums) {
  const n = nums.length;
  if (n === 1) return nums[0];
  let prev2 = 0, prev1 = 0;
  for (const num of nums) {
    const curr = Math.max(prev1, prev2 + num);
    prev2 = prev1;
    prev1 = curr;
  }
  return prev1;
}
```

状态转移：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`（偷或不偷第 i 间）

## LC 213. 打家劫舍 II（环形）

房屋首尾相连形成环，第一间和最后一间不能同时偷。

**技巧**：拆成两个子问题——不偷第一间 or 不偷最后一间，取最大值。javascript

```
function rob(nums) {
  const n = nums.length;
  if (n === 1) return nums[0];

  function robRange(lo, hi) {
    let prev2 = 0, prev1 = 0;
    for (let i = lo; i <= hi; i++) {
      const curr = Math.max(prev1, prev2 + nums[i]);
      prev2 = prev1;
      prev1 = curr;
    }
    return prev1;
  }

  return Math.max(robRange(0, n - 2), robRange(1, n - 1));
}
```

## LC 337. 打家劫舍 III（树形 DP）

房屋排列成二叉树，不能偷直接相连的节点。

每个节点返回两个值：`[不偷该节点的最大值, 偷该节点的最大值]`javascript

```
function rob(root) {
  function dfs(node) {
    if (!node) return [0, 0]; // [不偷, 偷]

    const left = dfs(node.left);
    const right = dfs(node.right);

    // 不偷当前节点：子节点可偷可不偷，取最大值
    const notRob = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    // 偷当前节点：子节点不能偷
    const doRob = node.val + left[0] + right[0];

    return [notRob, doRob];
  }

  const result = dfs(root);
  return Math.max(result[0], result[1]);
}
```

## 三道题的递进关系

| 题目 | 结构 | DP 类型 |
| --- | --- | --- |
| LC 198 | 线性数组 | 一维 DP |
| LC 213 | 环形数组 | 分两段一维 DP |
| LC 337 | 二叉树 | 树形 DP（后序遍历） |

## 复杂度

- LC 198/213：时间 O(n)，空间 O(1)
- LC 337：时间 O(n)，空间 O(h)

## LeetCode 练习

- LC 198. 打家劫舍 ⭐
- LC 213. 打家劫舍 II
- LC 337. 打家劫舍 III ⭐