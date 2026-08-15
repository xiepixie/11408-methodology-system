---
title: 如何实现一个计算器
source: https://www.codebrick.tech/algo-blog/posts/stack-queue/calculator.html
---

# 如何实现一个计算器

## 场景引入

给你一个字符串表达式 `"3+2*2-1"`，让你计算出结果。如果只有加减法，从左到右算就行。但加上乘除法后，就需要处理**运算符优先级**——乘除要比加减先算。再加上括号，就更复杂了。

这类问题的标准解法是**用栈来延迟计算**。核心洞察是：遇到高优先级运算符就立即算，遇到低优先级运算符就先存起来。

## 核心思路

### 处理加减乘除的框架

关键设计：用一个 `sign` 变量记录**上一个运算符**，当我们遇到新运算符或字符串结束时，根据 `sign` 来决定如何处理当前数字。

```
遍历 "3+2*2-1":
  遇到 3, sign='+' => push(3)         栈: [3]
  遇到 2, sign='+' => push(2)         栈: [3, 2]
  遇到 2, sign='*' => push(pop()*2)   栈: [3, 4]
  遇到 1, sign='-' => push(-1)        栈: [3, 4, -1]
  最后求和: 3+4+(-1) = 6
```

巧妙之处：

- 加法直接入栈
- 减法入栈负数
- 乘除立即和栈顶计算，结果入栈
- 最后栈中所有数求和

## 可视化演示

### LC 227. 基本计算器 II（加减乘除）
加载可视化中...

## 代码实现

### 第一步：只有加减法
javascript

```
function calculate(s) {
  let stack = [];
  let num = 0;
  let sign = '+';

  for (let i = 0; i <= s.length; i++) {
    let c = s[i];

    if (c >= '0' && c <= '9') {
      num = num * 10 + Number(c); // 处理多位数
      continue;
    }

    if (c === ' ') continue; // 跳过空格

    // 遇到运算符或字符串结束
    if (sign === '+') stack.push(num);
    if (sign === '-') stack.push(-num);

    sign = c;
    num = 0;
  }

  // 栈中所有数求和
  return stack.reduce((a, b) => a + b, 0);
}
```

### 第二步：加上乘除法（LC 227）

只需要在处理运算符时加上乘除的逻辑：javascript

```
function calculate(s) {
  let stack = [];
  let num = 0;
  let sign = '+';

  for (let i = 0; i <= s.length; i++) {
    let c = s[i];

    if (c >= '0' && c <= '9') {
      num = num * 10 + Number(c);
      continue;
    }

    if (c === ' ') continue;

    if (sign === '+') stack.push(num);
    if (sign === '-') stack.push(-num);
    if (sign === '*') stack.push(stack.pop() * num);
    if (sign === '/') stack.push(Math.trunc(stack.pop() / num));

    sign = c;
    num = 0;
  }

  return stack.reduce((a, b) => a + b, 0);
}
```

乘除法可以立即计算，因为它们的优先级最高。`stack.pop() * num` 取出栈顶（前一个数），乘以当前数，结果压回栈。

### 第三步：加上括号（LC 224）

括号的本质是**递归**。遇到 `(` 就递归处理括号内的子表达式，遇到 `)` 就返回结果。javascript

```
function calculate(s) {
  let i = 0;

  function calc() {
    let stack = [];
    let num = 0;
    let sign = '+';

    while (i < s.length) {
      let c = s[i];
      i++;

      if (c >= '0' && c <= '9') {
        num = num * 10 + Number(c);
      }

      if (c === '(') {
        num = calc(); // 递归计算括号内的值
      }

      if (c === ')' || i === s.length || (c !== ' ' && (c < '0' || c > '9') && c !== '(')) {
        if (sign === '+') stack.push(num);
        if (sign === '-') stack.push(-num);
        if (sign === '*') stack.push(stack.pop() * num);
        if (sign === '/') stack.push(Math.trunc(stack.pop() / num));
        sign = c;
        num = 0;
        if (c === ')') break; // 括号结束，返回
      }
    }

    return stack.reduce((a, b) => a + b, 0);
  }

  return calc();
}
```

## 三步扩展的思路

```
只有加减  →  加上乘除  →  加上括号
 (LC 无)     (LC 227)    (LC 224)
```

每一步都是在前一步的基础上做最小的扩展：

- 加减 → 加乘除：多两个 if 分支，乘除立即计算
- 加乘除 → 加括号：遇到 `(` 递归，遇到 `)` 返回

## 运算符优先级的处理原理

为什么栈能处理优先级？

- **加减法**：不确定后面是否有更高优先级的运算，所以先存入栈
- **乘除法**：优先级最高，可以立即和前一个操作数计算
- **括号**：开辟新的计算空间，相当于在栈上创建了一个"局部作用域"

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 基本计算器 II（加减乘除） | O(n) | O(n) |
| 基本计算器（加减括号） | O(n) | O(n) |

## LeetCode 练习

按难度递进：

- LC 227. 基本计算器 II（中等）—— 加减乘除，无括号
- LC 224. 基本计算器（困难）—— 加减和括号，无乘除
- LC 772. 基本计算器 III（困难，会员题）—— 加减乘除括号全套