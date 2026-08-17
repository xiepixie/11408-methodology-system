---
title: 二维数组技巧：旋转与螺旋遍历
source: https://www.codebrick.tech/algo-blog/posts/array/matrix.html
---

# 二维数组技巧：旋转与螺旋遍历

## 场景引入

二维数组（矩阵）类题目在面试中出现频率很高，其中最经典的两类问题是**矩阵旋转**和**螺旋遍历**。

这两类问题看起来花哨，其实都有固定套路。掌握了核心技巧后，不管矩阵怎么变，你都能从容应对。

矩阵旋转的关键洞察是：**旋转 = 转置 + 翻转**，把一个看似复杂的操作拆解为两步简单操作。螺旋遍历的关键则是：**用四个边界变量控制遍历范围**，每遍历完一条边就收缩对应的边界。

## 核心思路

### 矩阵旋转：转置 + 翻转

顺时针旋转 90 度 = 沿对角线转置 + 每行左右翻转：

```
原矩阵       转置         左右翻转(结果)
1 2 3      1 4 7       7 4 1
4 5 6  →   2 5 8   →   8 5 2
7 8 9      3 6 9       9 6 3
```

### 螺旋遍历：四边界收缩

用 `top`、`bottom`、`left`、`right` 四个变量框定当前遍历范围，按"右→下→左→上"的顺序遍历一圈后，四个边界各收缩一格：

```
→ → → →
↑       ↓
↑       ↓
← ← ← ←
```

## 可视化演示

### LC 54. 螺旋矩阵
加载可视化中...

## 代码实现

### LC 48. 旋转图像

原地顺时针旋转 90 度。javascript

```
function rotate(matrix) {
  let n = matrix.length;

  // 第一步：沿主对角线转置
  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      let temp = matrix[i][j];
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = temp;
    }
  }

  // 第二步：每行左右翻转
  for (let i = 0; i < n; i++) {
    let left = 0, right = n - 1;
    while (left < right) {
      let temp = matrix[i][left];
      matrix[i][left] = matrix[i][right];
      matrix[i][right] = temp;
      left++;
      right--;
    }
  }
}
```

推广到其他旋转方向：

| 旋转方向 | 等价操作 |
| --- | --- |
| 顺时针 90° | 转置 + 每行左右翻转 |
| 逆时针 90° | 转置 + 每列上下翻转 |
| 180° | 每行翻转 + 每列翻转 |

### LC 54. 螺旋矩阵

按螺旋顺序返回矩阵中的所有元素。javascript

```
function spiralOrder(matrix) {
  let result = [];
  let top = 0, bottom = matrix.length - 1;
  let left = 0, right = matrix[0].length - 1;

  while (top <= bottom && left <= right) {
    // 从左到右遍历上边
    for (let i = left; i <= right; i++) {
      result.push(matrix[top][i]);
    }
    top++;

    // 从上到下遍历右边
    for (let i = top; i <= bottom; i++) {
      result.push(matrix[i][right]);
    }
    right--;

    // 从右到左遍历下边（注意检查 top <= bottom）
    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        result.push(matrix[bottom][i]);
      }
      bottom--;
    }

    // 从下到上遍历左边（注意检查 left <= right）
    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        result.push(matrix[i][left]);
      }
      left++;
    }
  }

  return result;
}
```

关键细节：

- 遍历下边和左边之前，需要检查边界是否仍然有效（`top <= bottom`、`left <= right`）
- 否则在单行或单列矩阵中会重复遍历

### LC 59. 螺旋矩阵 II

生成一个 n x n 的螺旋矩阵，填入 1 到 n² 的数字。javascript

```
function generateMatrix(n) {
  let matrix = Array.from({ length: n },
    () => new Array(n).fill(0)
  );
  let num = 1;
  let top = 0, bottom = n - 1;
  let left = 0, right = n - 1;

  while (top <= bottom && left <= right) {
    for (let i = left; i <= right; i++) {
      matrix[top][i] = num++;
    }
    top++;

    for (let i = top; i <= bottom; i++) {
      matrix[i][right] = num++;
    }
    right--;

    if (top <= bottom) {
      for (let i = right; i >= left; i--) {
        matrix[bottom][i] = num++;
      }
      bottom--;
    }

    if (left <= right) {
      for (let i = bottom; i >= top; i--) {
        matrix[i][left] = num++;
      }
      left++;
    }
  }

  return matrix;
}
```

和 LC 54 的框架完全一致，只是从"读取"变成了"写入"。

### 补充：对角线遍历

矩阵还有一类常见操作是对角线遍历，这里给出关键观察：javascript

```
// 主对角线：i - j 相同的元素在同一条对角线上
// 副对角线：i + j 相同的元素在同一条对角线上
```

这个性质在很多矩阵题中都有用处（如 LC 498 对角线遍历）。

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| LC 48 旋转图像 | O(n²) | O(1) 原地 |
| LC 54 螺旋矩阵 | O(m * n) | O(1)（不计输出） |
| LC 59 螺旋矩阵 II | O(n²) | O(1)（不计输出） |

所有方法都只需要常数级别的额外空间，时间复杂度等于矩阵元素个数。

## LeetCode 练习

按难度递进：

- LC 48. 旋转图像（中等）
- LC 54. 螺旋矩阵（中等）
- LC 59. 螺旋矩阵 II（中等）
- LC 498. 对角线遍历（中等）
- LC 73. 矩阵置零（中等）
- LC 289. 生命游戏（中等）— 原地修改矩阵的技巧