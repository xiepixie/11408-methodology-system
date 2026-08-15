---
title: 单调栈：下一个更大元素问题
source: https://www.codebrick.tech/algo-blog/posts/stack-queue/monotonic-stack.html
---

# 单调栈：下一个更大元素问题

## 场景引入

给你一个数组，对每个元素，找到它右边第一个比它大的元素。暴力做法是对每个元素向右扫描，时间 O(n^2)。有没有 O(n) 的做法？

**单调栈**就是解决这类"下一个更大/更小元素"问题的利器。它在面试中出现频率很高，一旦掌握了模板，这类题都能秒杀。

## 核心思路

### 为什么叫"单调栈"

单调栈就是栈内元素保持**单调递增或单调递减**的栈。每次入栈前，把破坏单调性的元素弹出。被弹出的那一刻，弹出元素就找到了它的答案。

### 模板：从右往左遍历

想象你站在一排身高不同的人中间，要找到右边第一个比你高的人。你只需要看到第一个比你高的人就够了，比你矮的人会被挡住（出栈）。

```
数组: [2, 1, 2, 4, 3]
从右往左遍历，栈维护"还没被挡住的人":

i=4: 3, 栈空 => result[4]=-1, push(3)      栈: [3]
i=3: 4, 弹出3(<=4), 栈空 => result[3]=-1, push(4)  栈: [4]
i=2: 2, 栈顶4>2 => result[2]=4, push(2)    栈: [4,2]
i=1: 1, 栈顶2>1 => result[1]=2, push(1)    栈: [4,2,1]
i=0: 2, 弹出1(<=2), 栈顶2<=2弹出, 栈顶4>2 => result[0]=4, push(2)  栈: [4,2]

结果: [4, 2, 4, -1, -1]
```

## 可视化演示

### LC 496. 下一个更大元素
加载可视化中...

### LC 739. 每日温度
加载可视化中...

## 代码实现

### 模板一：从右往左，栈存值
javascript

```
function nextGreaterElement(nums) {
  let n = nums.length;
  let result = new Array(n).fill(-1);
  let stack = []; // 栈存储值

  for (let i = n - 1; i >= 0; i--) {
    // 弹出所有不大于当前元素的值
    while (stack.length > 0 && stack[stack.length - 1] <= nums[i]) {
      stack.pop();
    }
    // 栈顶就是右边第一个更大的
    if (stack.length > 0) {
      result[i] = stack[stack.length - 1];
    }
    stack.push(nums[i]);
  }

  return result;
}
```

### 模板二：从左往右，栈存索引
javascript

```
function dailyTemperatures(temperatures) {
  let n = temperatures.length;
  let result = new Array(n).fill(0);
  let stack = []; // 栈存储索引

  for (let i = 0; i < n; i++) {
    // 当前温度比栈顶高，栈顶找到了答案
    while (stack.length > 0 && temperatures[stack[stack.length - 1]] < temperatures[i]) {
      let j = stack.pop();
      result[j] = i - j; // 距离
    }
    stack.push(i);
  }

  return result;
}
```

**两种模板的区别**：

- 从右往左：当前元素问栈"谁是我的答案？"
- 从左往右：当前元素告诉栈中的元素"我就是你的答案！"

### LC 503. 下一个更大元素 II（循环数组）

循环数组的技巧：把数组"拼接"一份，用 `i % n` 取模模拟循环。javascript

```
function nextGreaterElements(nums) {
  let n = nums.length;
  let result = new Array(n).fill(-1);
  let stack = [];

  // 遍历两倍长度，模拟循环
  for (let i = 2 * n - 1; i >= 0; i--) {
    while (stack.length > 0 && stack[stack.length - 1] <= nums[i % n]) {
      stack.pop();
    }
    if (stack.length > 0) {
      result[i % n] = stack[stack.length - 1];
    }
    stack.push(nums[i % n]);
  }

  return result;
}
```

## 单调栈为什么是 O(n)

虽然有嵌套循环（for + while），但每个元素**最多入栈一次、出栈一次**。所以总操作数是 2n，时间复杂度是 O(n)。

这是分摊分析（amortized analysis）的经典案例。

## 什么时候用单调栈

看到以下关键词就应该想到单调栈：

- "下一个更大/更小的元素"
- "右边第一个比它大/小的"
- "左边第一个比它大/小的"
- "每日温度"类距离问题

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 下一个更大元素 | O(n) | O(n) |
| 每日温度 | O(n) | O(n) |
| 循环数组下一个更大 | O(n) | O(n) |

## LeetCode 练习

按难度递进：

- LC 496. 下一个更大元素 I（简单）
- LC 739. 每日温度（中等）
- LC 503. 下一个更大元素 II（中等，循环数组）
- LC 901. 股票价格跨度（中等）
- LC 84. 柱状图中最大的矩形（困难，单调栈经典难题）
- LC 42. 接雨水（困难，单调栈或双指针）