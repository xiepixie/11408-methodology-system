---
title: 编辑距离：DP 的经典中的经典
source: https://www.codebrick.tech/algo-blog/posts/dp/edit-distance.html
---

# 编辑距离：DP 的经典中的经典

## 场景引入

搜索引擎的"你是不是要搜索..."功能，就是在计算你输入的词和字典中的词的**编辑距离**——把一个字符串变成另一个字符串最少需要几步操作。

## LC 72. 编辑距离

给定两个单词 word1 和 word2，计算将 word1 转换为 word2 所需的最少操作数。可执行三种操作：插入、删除、替换。

### 状态定义

`dp[i][j]` = 将 `word1[0..i-1]` 转换为 `word2[0..j-1]` 的最少操作数。

### 状态转移

```
if word1[i-1] === word2[j-1]:
    dp[i][j] = dp[i-1][j-1]        // 字符相同，不需要操作
else:
    dp[i][j] = min(
        dp[i-1][j] + 1,            // 删除 word1[i-1]
        dp[i][j-1] + 1,            // 在 word1 插入 word2[j-1]
        dp[i-1][j-1] + 1           // 替换 word1[i-1] 为 word2[j-1]
    )
```

### 编辑距离状态转移流程

### Base case

- `dp[0][j] = j`：word1 为空，需要插入 j 个字符
- `dp[i][0] = i`：word2 为空，需要删除 i 个字符

### 实现
javascript

```
function minDistance(word1, word2) {
  const m = word1.length, n = word2.length;
  const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));

  // base case
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      if (word1[i - 1] === word2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1];
      } else {
        dp[i][j] = Math.min(
          dp[i - 1][j] + 1,     // 删除
          dp[i][j - 1] + 1,     // 插入
          dp[i - 1][j - 1] + 1  // 替换
        );
      }
    }
  }
  return dp[m][n];
}
```

### DP 表格示例

将 "horse" 转换为 "ros"：

```
    ""  r  o  s
""   0  1  2  3
h    1  1  2  3
o    2  2  1  2
r    3  2  2  2
s    4  3  3  2
e    5  4  4  3
```

答案：`dp[5][3] = 3`（horse → rorse → rose → ros）

## 理解三种操作

在 DP 表格中：

- **dp[i-1][j] + 1**（上方 +1）= 删除 word1 的当前字符
- **dp[i][j-1] + 1**（左方 +1）= 插入 word2 的当前字符
- **dp[i-1][j-1] + 1**（对角 +1）= 替换

## 复杂度

- 时间：O(m × n)
- 空间：O(m × n)，可优化为 O(n)

## 面试要点

- 编辑距离是 DP 最经典的题目之一，必须能手写
- 理解三种操作在 DP 表格中的含义
- 能画出 DP 表格推导过程

## LeetCode 练习

- LC 72. 编辑距离 ⭐
- LC 583. 两个字符串的删除操作
- LC 712. 两个字符串的最小 ASCII 删除和