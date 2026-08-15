---
title: 回溯经典：N 皇后与数独
source: https://www.codebrick.tech/algo-blog/posts/backtrack/classic.html
---

# 回溯经典：N 皇后与数独

## 场景引入

学完回溯框架和排列组合之后，你可能会想：这些套路能解决"真正难"的题吗？

答案是可以。N 皇后、数独、括号生成这三道经典题，本质上都是**在决策树上穷举 + 用约束条件剪枝**。只要你能把问题翻译成"每一步做什么选择、什么选择不合法"，回溯框架就能直接套用。

## 核心思路

回溯的通用模板不变，区别在于：

- **选择是什么**：N 皇后选列位置，数独选填 1-9 的哪个数字，括号选放左括号还是右括号
- **约束是什么**：N 皇后不能同行/同列/同对角线，数独不能同行/同列/同宫格重复，括号要合法嵌套
- **何时结束**：N 皇后放满 n 行，数独填满所有空格，括号用完所有字符

### 对应框架

```
回溯模板:
  if 结束条件 → 收集结果
  for 当前可选项:
      if 不合法(约束条件) → continue (剪枝)
      做选择
      backtrack(下一步)
      撤销选择
```

### N 皇后约束检查流程

## 可视化演示

以 4 皇后问题演示回溯搜索过程：加载可视化中...

## 代码实现

### LC 51. N 皇后

**问题**：在 n x n 棋盘上放 n 个皇后，使它们互不攻击（不在同行、同列、同对角线）。javascript

```
function solveNQueens(n) {
  const result = [];
  const board = Array.from({length: n}, () => new Array(n).fill('.'));
  backtrack(board, 0, result);
  return result;
}

function backtrack(board, row, result) {
  if (row === board.length) {
    result.push(board.map(r => r.join('')));
    return;
  }
  for (let col = 0; col < board.length; col++) {
    if (!isValid(board, row, col)) continue; // 剪枝
    board[row][col] = 'Q';        // 做选择：放皇后
    backtrack(board, row + 1, result); // 下一行
    board[row][col] = '.';        // 撤销选择
  }
}

function isValid(board, row, col) {
  const n = board.length;
  // 检查同列
  for (let i = 0; i < row; i++) {
    if (board[i][col] === 'Q') return false;
  }
  // 检查左上对角线
  for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
    if (board[i][j] === 'Q') return false;
  }
  // 检查右上对角线
  for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
    if (board[i][j] === 'Q') return false;
  }
  return true;
}
```

**框架映射**：

- 选择 = 每行选一个列放皇后
- 约束 = `isValid` 检查三个方向
- 结束 = 所有行都放完（`row === n`）

### LC 37. 解数独

**问题**：填完一个 9x9 的数独。javascript

```
function solveSudoku(board) {
  backtrack(board);
}

function backtrack(board) {
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] !== '.') continue;
      for (let num = 1; num <= 9; num++) {
        const ch = String(num);
        if (!isValid(board, i, j, ch)) continue;
        board[i][j] = ch;           // 做选择
        if (backtrack(board)) return true; // 找到一个解就返回
        board[i][j] = '.';          // 撤销选择
      }
      return false; // 1-9 都不行，说明前面的选择有误
    }
  }
  return true; // 所有格子都填完了
}

function isValid(board, row, col, ch) {
  for (let k = 0; k < 9; k++) {
    if (board[row][k] === ch) return false;   // 同行
    if (board[k][col] === ch) return false;   // 同列
    // 同 3x3 宫格
    const r = Math.floor(row / 3) * 3 + Math.floor(k / 3);
    const c = Math.floor(col / 3) * 3 + (k % 3);
    if (board[r][c] === ch) return false;
  }
  return true;
}
```

**与 N 皇后的区别**：数独只需要一个解，找到就返回 `true`，不需要继续搜索。N 皇后要找所有解。

### LC 22. 括号生成

**问题**：生成 n 对合法括号的所有组合。javascript

```
function generateParenthesis(n) {
  const result = [];
  backtrack('', 0, 0, n, result);
  return result;
}

function backtrack(path, open, close, n, result) {
  if (path.length === 2 * n) {
    result.push(path);
    return;
  }
  // 选择 1：放左括号（只要还有剩余）
  if (open < n) {
    backtrack(path + '(', open + 1, close, n, result);
  }
  // 选择 2：放右括号（右括号数量不能超过左括号）
  if (close < open) {
    backtrack(path + ')', open, close + 1, n, result);
  }
}
```

**框架映射**：

- 选择 = 放 `(` 或 `)`
- 约束 = 左括号不超过 n，右括号不超过左括号数
- 结束 = 字符串长度达到 2n

这道题的巧妙之处在于约束条件本身就隐含了剪枝，不需要显式的 `isValid` 函数。

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| N 皇后 | O(n!) | O(n^2) 棋盘 |
| 数独 | O(9^m)，m 为空格数 | O(m) 递归栈 |
| 括号生成 | O(4^n / sqrt(n)) 卡特兰数 | O(n) |

N 皇后虽然看起来是 O(n^n)（每行 n 种选择 x n 行），但因为剪枝，实际远小于此，约为 O(n!)。

## 回溯剪枝的通用策略

- **可行性剪枝**：当前选择违反约束，直接跳过（本文所有例子都是这种）
- **最优性剪枝**：当前路径不可能比已知最优解更好，提前终止（常见于求最值问题）
- **对称性剪枝**：利用问题的对称性减少搜索（如 N 皇后只搜索一半棋盘）

## LeetCode 练习

- [LC 51. N 皇后](https://leetcode.cn/problems/n-queens/)（经典回溯）
- [LC 52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/)（只求方案数）
- [LC 37. 解数独](https://leetcode.cn/problems/sudoku-solver/)（约束满足问题）
- [LC 22. 括号生成](https://leetcode.cn/problems/generate-parentheses/)（隐式决策树）
- [LC 79. 单词搜索](https://leetcode.cn/problems/word-search/)（网格上的回溯）
- [LC 93. 复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/)（字符串切割回溯）