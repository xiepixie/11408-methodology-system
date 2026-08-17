---
title: 回溯算法框架：穷举决策树
source: https://www.codebrick.tech/algo-blog/posts/backtrack/framework.html
---

# 回溯算法框架：穷举决策树

## 场景引入

你参加一个密码锁解谜游戏：锁有 3 位，每位可选 1、2、3，你需要试出所有可能的密码。你会怎么做？

先固定第一位为 1，然后尝试第二位的所有选择，再尝试第三位……试完后回到第二位换一个数字继续。这个"尝试 - 撤销 - 再尝试"的过程，就是**回溯算法**。

回溯算法本质上就是**在决策树上做 DFS**（深度优先搜索）。每到一个节点，做一个选择，然后继续往下走；走到底或发现不合法时，**撤销选择**（回溯），换一条路继续走。

## 核心思路

### 回溯三要素

- **路径（path）**：已经做出的选择
- **选择列表（choices）**：当前可以做的选择
- **结束条件（base case）**：到达决策树的叶子节点

### 回溯流程图

### 决策树结构

### 算法模板
javascript

```
function backtrack(path, choices) {
    if (满足结束条件) {
        result.push([...path]); // 收集结果
        return;
    }
    for (const choice of choices) {
        // 做选择
        path.push(choice);
        // 进入下一层决策树
        backtrack(path, 剩余选择);
        // 撤销选择（回溯）
        path.pop();
    }
}
```

这个模板的关键在于 `for` 循环里的**做选择**和**撤销选择**。做选择就是把当前选项加入路径，撤销选择就是把它移出路径，这样才能回到上一步去尝试其他选项。

### 决策树图示

以全排列 `[1, 2, 3]` 为例，决策树如下：

```
                    []
           /        |        \
         [1]       [2]       [3]
        /   \     /   \     /   \
     [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
      |      |     |     |     |      |
   [1,2,3][1,3,2][2,1,3][2,3,1][3,1,2][3,2,1]
```

每个节点就是一个"状态"，从根节点到叶子节点的路径就是一个排列。回溯算法就是遍历这棵树的所有路径。

## 可视化演示
加载可视化中...

## 代码实现

以 LC 46 全排列为例：javascript

```
function permute(nums) {
  const result = [];
  const path = [];
  const used = new Array(nums.length).fill(false);
  backtrack(nums, path, used, result);
  return result;
}

function backtrack(nums, path, used, result) {
  if (path.length === nums.length) {
    result.push([...path]);
    return;
  }
  for (let i = 0; i < nums.length; i++) {
    if (used[i]) continue; // 跳过已使用的元素
    path.push(nums[i]);    // 做选择
    used[i] = true;
    backtrack(nums, path, used, result); // 进入下一层
    path.pop();            // 撤销选择
    used[i] = false;
  }
}
```

**要点解读：**

- `used` 数组记录哪些元素已在路径中，避免重复使用
- `result.push([...path])` 必须用扩展运算符拷贝，否则后续回溯会修改 result 中的引用
- 每次循环都从 `i = 0` 开始，因为排列关注顺序，`[1,2]` 和 `[2,1]` 是不同结果

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 全排列 | O(n! * n) | O(n) 递归栈深度 |

全排列共 `n!` 个结果，每个结果需要 O(n) 时间拷贝，所以总时间是 O(n! * n)。

回溯算法的时间复杂度通常很高，因为本质是穷举。但很多问题确实只能穷举，回溯算法的价值在于提供了**系统化穷举**的框架，并且可以通过**剪枝**提前排除无效分支。

## 常见误区

- **忘记撤销选择**：只 `push` 不 `pop`，导致路径越来越长，结果全部错误
- **忘记拷贝路径**：`result.push(path)` 推入的是引用，后续回溯会把 result 里的数组也清空
- **混淆排列和组合的遍历起点**：排列从 0 开始（关注顺序），组合从 `start` 开始（不关注顺序）

## 回溯 vs 动态规划 vs 贪心

|  | 回溯 | 动态规划 | 贪心 |
| --- | --- | --- | --- |
| 本质 | 穷举所有可能 | 穷举 + 记忆化 | 局部最优 |
| 适用 | 求所有方案 | 求最优值 | 求最优值（特殊结构） |
| 时间 | 指数级 | 多项式级 | 线性级 |

## LeetCode 练习

- [LC 46. 全排列](https://leetcode.cn/problems/permutations/)（本文例题）
- [LC 78. 子集](https://leetcode.cn/problems/subsets/)（入门级回溯）
- [LC 77. 组合](https://leetcode.cn/problems/combinations/)（组合型回溯）
- [LC 22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)（隐式决策树）