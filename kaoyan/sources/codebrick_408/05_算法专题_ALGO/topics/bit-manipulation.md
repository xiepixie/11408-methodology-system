---
title: 位运算技巧
source: https://www.codebrick.tech/algo-blog/posts/topics/bit-manipulation.html
---

# 位运算技巧

## 核心操作

| 操作 | 符号 | 规则 |
| --- | --- | --- |
| 与 | `&` | 都为 1 才是 1 |
| 或 | `\|` | 有一个 1 就是 1 |
| 异或 | `^` | 不同为 1 |
| 取反 | `~` | 0 变 1，1 变 0 |
| 左移 | `<<` | 乘以 2 |
| 右移 | `>>` | 除以 2 |

### 位运算技巧决策树

## 常用技巧

### 1. `n & (n - 1)`：消除最低位的 1

```
n     = 1010100
n-1   = 1010011
n&n-1 = 1010000  → 最后一个 1 被消除
```

应用：判断 2 的幂、统计 1 的个数。

### 2. `n & (-n)`：获取最低位的 1

```
n    = 1010100
-n   = 0101100
n&-n = 0000100  → 只保留最低位的 1
```

### 3. 异或的三个性质

- `a ^ a = 0`（自己异或自己等于 0）
- `a ^ 0 = a`（任何数异或 0 等于自己）
- 交换律和结合律

## LC 136. 只出现一次的数字

数组中只有一个数出现一次，其余都出现两次。找出那个数。javascript

```
function singleNumber(nums) {
  let result = 0;
  for (const num of nums) {
    result ^= num; // 成对的数异或抵消为 0
  }
  return result;
}
```

## LC 191. 位 1 的个数
javascript

```
function hammingWeight(n) {
  let count = 0;
  while (n) {
    n = n & (n - 1); // 每次消除一个 1
    count++;
  }
  return count;
}
```

## LC 231. 2 的幂

2 的幂的二进制只有一个 1：javascript

```
function isPowerOfTwo(n) {
  return n > 0 && (n & (n - 1)) === 0;
}
```

## LC 268. 丢失的数字

[0, n] 中缺少一个数，找出来。javascript

```
function missingNumber(nums) {
  let xor = nums.length;
  for (let i = 0; i < nums.length; i++) {
    xor ^= i ^ nums[i];
  }
  return xor;
}
```

原理：`[0..n]` 全部异或 再异或数组所有元素，成对的抵消，剩下的就是缺失的。

## 复杂度

所有题目：时间 O(n)，空间 O(1)。

## LeetCode 练习

- LC 136. 只出现一次的数字 ⭐
- LC 191. 位 1 的个数
- LC 231. 2 的幂
- LC 268. 丢失的数字
- LC 338. 比特位计数
- LC 371. 两整数之和（不用 +/- 运算符）