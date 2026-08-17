---
title: 排列/组合/子集：三类九题一网打尽
source: https://www.codebrick.tech/algo-blog/posts/backtrack/permutation-combination.html
---

# 排列/组合/子集：三类九题一网打尽

## 场景引入

刷 LeetCode 时你一定遇到过这类题：给一组数字，求所有子集、所有组合、所有排列。它们看起来很像，代码也很像，但总有些微妙的区别让人搞混。

本文将这类题目按 **3 种类型 x 3 种变体** 整理为一张 3x3 表格，让你一次性搞清楚所有变种。

## 核心思路

### 三类问题的本质区别

| 类型 | 关注顺序？ | 关注个数？ | 遍历起点 |
| --- | --- | --- | --- |
| **子集** | 不关注 | 不限制 | `start` 往后 |
| **组合** | 不关注 | 固定 k 个 | `start` 往后 |
| **排列** | 关注 | 固定 n 个 | 每次从 0 开始 |

- 子集/组合不关注顺序，所以用 `start` 参数保证只往后选，避免 `[1,2]` 和 `[2,1]` 重复
- 排列关注顺序，所以每次从 0 开始遍历，用 `used` 数组标记已选元素

### 3x3 九题表格

|  | 无重复无复选 | 有重复无复选 | 无重复可复选 |
| --- | --- | --- | --- |
| **子集** | LC 78 | LC 90 | - |
| **组合** | LC 77 | LC 40 | LC 39 |
| **排列** | LC 46 | LC 47 | - |

掌握第一列（无重复无复选）的基础模板后，只需做两种修改：

- **有重复** → 排序 + 跳过相邻重复元素
- **可复选** → 递归时不用 `i + 1`，继续用 `i`

### 三类回溯模式对比

## 可视化演示

下面用子集问题 `[1,2,3]` 演示回溯过程：加载可视化中...

## 代码实现

### 第一类：无重复无复选（基础模板）

**LC 78. 子集**javascript

```
function subsets(nums) {
  const result = [];
  const path = [];
  backtrack(nums, 0, path, result);
  return result;
}

function backtrack(nums, start, path, result) {
  result.push([...path]); // 每个节点都是一个子集
  for (let i = start; i < nums.length; i++) {
    path.push(nums[i]);
    backtrack(nums, i + 1, path, result);
    path.pop();
  }
}
```

**LC 77. 组合**（在子集基础上加一个长度限制）javascript

```
function combine(n, k) {
  const result = [];
  const path = [];
  backtrack(1, n, k, path, result);
  return result;
}

function backtrack(start, n, k, path, result) {
  if (path.length === k) {
    result.push([...path]);
    return; // 子集是每个节点收集，组合是到达指定长度才收集
  }
  for (let i = start; i <= n; i++) {
    path.push(i);
    backtrack(i + 1, n, k, path, result);
    path.pop();
  }
}
```

**LC 46. 全排列**（从 0 开始遍历，用 `used` 数组标记已选元素，详见[[05_算法专题_ALGO/backtrack/framework.md|回溯框架篇]]）

### 第二类：有重复无复选（排序 + 剪枝）

关键技巧：**先排序，再跳过同层重复元素**。

**LC 90. 子集 II**javascript

```
function subsetsWithDup(nums) {
  nums.sort((a, b) => a - b); // 排序是前提
  const result = [];
  const path = [];
  backtrack(nums, 0, path, result);
  return result;
}

function backtrack(nums, start, path, result) {
  result.push([...path]);
  for (let i = start; i < nums.length; i++) {
    // 同层跳过重复元素
    if (i > start && nums[i] === nums[i - 1]) continue;
    path.push(nums[i]);
    backtrack(nums, i + 1, path, result);
    path.pop();
  }
}
```

**LC 40. 组合总和 II** 和 **LC 47. 全排列 II** 同理，核心都是 `if (i > start && nums[i] === nums[i-1]) continue;`。

对于排列的去重，条件稍有不同：javascript

```
// 排列去重条件
if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue;
```

### 第三类：无重复可复选（递归不 +1）

**LC 39. 组合总和**javascript

```
function combinationSum(candidates, target) {
  const result = [];
  const path = [];
  backtrack(candidates, 0, target, path, result);
  return result;
}

function backtrack(candidates, start, target, path, result) {
  if (target === 0) {
    result.push([...path]);
    return;
  }
  if (target < 0) return;
  for (let i = start; i < candidates.length; i++) {
    path.push(candidates[i]);
    backtrack(candidates, i, target - candidates[i], path, result); // 注意：i 不加 1
    path.pop();
  }
}
```

唯一的区别就是递归时传 `i` 而不是 `i + 1`，允许重复选择同一个元素。

## 复杂度分析

| 类型 | 时间复杂度 | 结果数量 |
| --- | --- | --- |
| 子集 | O(2^n * n) | 2^n |
| 组合 C(n,k) | O(C(n,k) * k) | C(n,k) |
| 排列 | O(n! * n) | n! |

## 总结：三个修改点

记住基础模板后，只需关注三个修改点：

- **收集时机**：子集在每个节点收集，组合/排列在叶子节点收集
- **遍历起点**：子集/组合用 `start`，排列从 0 开始 + `used`
- **变体处理**：有重复加剪枝，可复选改递归参数

## LeetCode 练习

基础三题：

- [LC 78. 子集](https://leetcode.cn/problems/subsets/)
- [LC 77. 组合](https://leetcode.cn/problems/combinations/)
- [LC 46. 全排列](https://leetcode.cn/problems/permutations/)

去重变体：

- [LC 90. 子集 II](https://leetcode.cn/problems/subsets-ii/)
- [LC 40. 组合总和 II](https://leetcode.cn/problems/combination-sum-ii/)
- [LC 47. 全排列 II](https://leetcode.cn/problems/permutations-ii/)

可复选变体：

- [LC 39. 组合总和](https://leetcode.cn/problems/combination-sum/)