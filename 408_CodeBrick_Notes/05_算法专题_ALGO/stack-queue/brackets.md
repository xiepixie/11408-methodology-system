---
title: 括号匹配：栈的经典应用
source: https://www.codebrick.tech/algo-blog/posts/stack-queue/brackets.html
---

# 括号匹配：栈的经典应用

## 场景引入

括号匹配是栈最经典的应用场景。编辑器的括号高亮、编译器的语法检查、HTML 标签配对，底层都是同一个原理。面试中括号类题目出现频率很高，而且万变不离其宗——核心都是用栈来匹配。

为什么用栈？因为括号匹配具有**后进先出**的特性：最后出现的左括号，应该最先被匹配。这和栈的 LIFO 特性完美契合。

## 核心思路

### 基本框架
javascript

```
function isValid(s) {
  let stack = [];

  for (let c of s) {
    if (是左括号(c)) {
      stack.push(c);
    } else {
      // 右括号：检查栈顶是否匹配
      if (stack.length === 0 || 栈顶不匹配(c)) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0; // 栈空说明全部匹配
}
```

三个判断无效的时机：

- **遇到右括号但栈为空**：右括号多了
- **遇到右括号但栈顶不匹配**：括号类型不对
- **遍历结束但栈非空**：左括号多了

## 可视化演示

### LC 20. 有效的括号
加载可视化中...

## 代码实现

### LC 20. 有效的括号
javascript

```
function isValid(s) {
  let stack = [];
  let map = { ')': '(', ']': '[', '}': '{' };

  for (let i = 0; i < s.length; i++) {
    let c = s[i];
    if (c === '(' || c === '[' || c === '{') {
      stack.push(c);
    } else {
      if (stack.length === 0 || stack[stack.length - 1] !== map[c]) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}
```

用一个 `map` 存储右括号到左括号的映射，比用三个 if-else 更简洁。

### LC 921. 使括号有效的最少添加

这道题问的是：最少需要插入多少个括号才能让字符串有效？javascript

```
function minAddToMakeValid(s) {
  let needLeft = 0;  // 需要的左括号数量
  let needRight = 0; // 需要的右括号数量

  for (let c of s) {
    if (c === '(') {
      needRight++; // 左括号需要一个右括号来匹配
    } else {
      if (needRight > 0) {
        needRight--; // 匹配一个
      } else {
        needLeft++; // 没有左括号可匹配，需要插入一个
      }
    }
  }

  return needLeft + needRight;
}
```

**思路**：不需要真正的栈，只需要两个计数器。`needRight` 记录待匹配的左括号数（等价于栈的大小），`needLeft` 记录无法匹配的右括号数。

### LC 1541. 平衡括号字符串的最少插入次数

这题的规则是：每个左括号需要**两个连续的右括号**来匹配，即 `(` 必须匹配 `))`。javascript

```
function minInsertions(s) {
  let insertions = 0; // 需要插入的数量
  let needRight = 0;  // 需要的右括号数量

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      needRight += 2; // 每个左括号需要两个右括号
      // 如果当前需要奇数个右括号，说明之前有单独的右括号
      if (needRight % 2 === 1) {
        insertions++; // 补一个右括号凑成偶数
        needRight--;
      }
    } else {
      needRight--;
      if (needRight < 0) {
        insertions++; // 需要插入一个左括号
        needRight = 1; // 这个左括号还需要一个右括号
      }
    }
  }

  return insertions + needRight;
}
```

## 括号题的通用技巧

- **用栈模拟匹配过程**：遇左括号压栈，遇右括号弹栈
- **用计数器代替栈**：如果只有一种括号，栈可以简化为计数器
- **注意边界**：栈为空时遇到右括号、遍历完栈不为空
- **多种括号的优先级**：有些题需要考虑括号的嵌套顺序

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 有效的括号 | O(n) | O(n) |
| 最少添加 | O(n) | O(1) |
| 最少插入次数 | O(n) | O(1) |

只有 LC 20 需要真正的栈（因为有三种括号需要匹配类型），后两题用计数器就够了。

## LeetCode 练习

按难度递进：

- LC 20. 有效的括号（简单）
- LC 921. 使括号有效的最少添加（中等）
- LC 1541. 平衡括号字符串的最少插入次数（中等）
- LC 32. 最长有效括号（困难）
- LC 1249. 移除无效的括号（中等）