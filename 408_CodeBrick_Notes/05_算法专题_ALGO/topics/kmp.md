---
title: KMP 算法：字符串匹配的利器
source: https://www.codebrick.tech/algo-blog/posts/topics/kmp.html
---

# KMP 算法：字符串匹配的利器

## 场景引入

在文本编辑器中按 Ctrl+F 搜索一个词，背后就是字符串匹配算法。暴力匹配是 O(mn)，而 KMP 算法可以做到 O(m+n)。

## 暴力匹配的问题
javascript

```
function bruteForce(text, pattern) {
  for (let i = 0; i <= text.length - pattern.length; i++) {
    let j = 0;
    while (j < pattern.length && text[i + j] === pattern[j]) j++;
    if (j === pattern.length) return i;
  }
  return -1;
}
```

当不匹配时，暴力解法让 `i` 回退到 `i+1`，浪费了已匹配的信息。

## KMP 的核心：不回退文本指针

KMP 的关键洞察：**匹配失败时，利用已匹配部分的信息，让模式串滑动到正确位置，文本指针不回退**。

### next 数组（失败函数）

`next[j]` = 模式串 `pattern[0..j-1]` 的最长相等前后缀长度。

```
pattern:  A B A B C
next:    [0,0,1,2,0]
```

含义：`pattern[0..2] = "ABA"`，最长相等前后缀是 "A"（长度 1）。

### 构建 next 数组
javascript

```
function buildNext(pattern) {
  const next = new Array(pattern.length).fill(0);
  let len = 0; // 前缀长度
  let i = 1;

  while (i < pattern.length) {
    if (pattern[i] === pattern[len]) {
      len++;
      next[i] = len;
      i++;
    } else if (len > 0) {
      len = next[len - 1]; // 回退到更短的前缀
    } else {
      next[i] = 0;
      i++;
    }
  }
  return next;
}
```

### KMP 主算法
javascript

```
function kmpSearch(text, pattern) {
  if (pattern.length === 0) return 0;
  const next = buildNext(pattern);
  let j = 0; // 模式串指针

  for (let i = 0; i < text.length; i++) {
    while (j > 0 && text[i] !== pattern[j]) {
      j = next[j - 1]; // 利用 next 数组回退模式串
    }
    if (text[i] === pattern[j]) {
      j++;
    }
    if (j === pattern.length) {
      return i - pattern.length + 1; // 找到匹配
    }
  }
  return -1;
}
```

### KMP 匹配流程图

## 图解匹配过程

```
text:    A B A B A B C
pattern: A B A B C
              ↑ 不匹配，j=4

next[3]=2，模式串滑动到 j=2 继续比较：
text:    A B A B A B C
pattern:     A B A B C
                  ↑ 继续匹配
```

关键：`next[3]=2` 表示 "ABAB" 的最长前后缀 "AB" 长度为 2，所以直接从 j=2 继续。

## 复杂度

- 构建 next 数组：O(m)
- 匹配过程：O(n)
- 总时间：O(m + n)
- 空间：O(m)

## 面试要点

- 理解 next 数组的含义（最长相等前后缀）
- 知道为什么 KMP 是 O(m+n)（文本指针不回退）
- KMP 面试考得不多，但被问到时必须能讲清楚原理

## LeetCode 练习

- LC 28. 找出字符串中第一个匹配项的下标
- LC 459. 重复的子字符串（利用 KMP 的 next 数组）