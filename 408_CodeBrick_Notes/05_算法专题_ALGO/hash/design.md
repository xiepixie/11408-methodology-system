---
title: 哈希表原理：从 Word 拼写检查说起
source: https://www.codebrick.tech/algo-blog/posts/hash/design.html
---

# 哈希表原理：从 Word 拼写检查说起

## 场景引入

你在 Word 里打字，每个单词下面如果拼错了会立刻出现红色波浪线。Word 的字典里有几十万个单词，它是怎么做到**瞬间判断**一个单词是否存在的？

答案就是哈希表。它能在 **O(1)** 时间内完成查找、插入和删除操作。

## 核心原理

### 哈希函数

哈希函数的作用是把**任意大小的 key** 映射到**固定范围的数组下标**。javascript

```
function hash(key, tableSize) {
  let h = 0;
  for (let i = 0; i < key.length; i++) {
    h = (h * 31 + key.charCodeAt(i)) % tableSize;
  }
  return h;
}
```

好的哈希函数应满足：

- **确定性**：相同的 key 一定得到相同的值
- **均匀性**：不同的 key 尽量分散到不同的槽位
- **高效性**：计算速度快

### 冲突解决

不同的 key 可能映射到同一个位置，这就是**哈希冲突**。两种主要解决策略：

#### 拉链法（Chaining）

每个槽位存一个链表，冲突的元素追加到链表尾部。javascript

```
class HashMapChaining {
  constructor(size = 16) {
    this.table = new Array(size).fill(null).map(() => []);
    this.size = size;
  }

  _hash(key) {
    let h = 0;
    for (const ch of String(key)) {
      h = (h * 31 + ch.charCodeAt(0)) % this.size;
    }
    return h;
  }

  put(key, value) {
    const idx = this._hash(key);
    const bucket = this.table[idx];
    for (const pair of bucket) {
      if (pair[0] === key) { pair[1] = value; return; }
    }
    bucket.push([key, value]);
  }

  get(key) {
    const idx = this._hash(key);
    for (const pair of this.table[idx]) {
      if (pair[0] === key) return pair[1];
    }
    return undefined;
  }
}
```

**优点**：实现简单，删除方便 **缺点**：链表过长时退化为 O(n)（Java 8 中 HashMap 链表超过 8 个会转红黑树）

#### 开放寻址法（Open Addressing）

冲突时探测下一个空位。常见策略：

- **线性探测**：`(hash + i) % size`
- **二次探测**：`(hash + i²) % size`
- **双重哈希**：`(hash1 + i * hash2) % size`javascript

```
// 线性探测示例
put(key, value) {
  let idx = this._hash(key);
  while (this.table[idx] !== null && this.table[idx].key !== key) {
    idx = (idx + 1) % this.size; // 线性探测
  }
  this.table[idx] = { key, value };
}
```

**优点**：缓存友好（数据连续存储） **缺点**：删除复杂（需要标记墓碑），容易聚集

### 负载因子与扩容

**负载因子** = 已存元素数 / 数组容量

- 拉链法一般在负载因子 > 0.75 时扩容（Java HashMap 的默认阈值）
- 开放寻址法一般在 > 0.5 时就需要扩容

扩容 = 创建 2 倍大小的新数组 → 所有元素重新哈希插入（**rehash**）。

## 工业级哈希表的设计要点

| 要点 | 说明 |
| --- | --- |
| 初始容量 | 通常为 2 的幂（方便位运算取模） |
| 负载因子阈值 | 0.75 是性能和空间的平衡点 |
| 扩容策略 | 2 倍扩容，渐进式 rehash（Redis 做法） |
| 哈希函数 | 乘法+位运算混合，避免简单取模 |
| 冲突退化 | 链表 → 红黑树（Java 8 HashMap） |

## 复杂度分析

| 操作 | 平均 | 最坏 |
| --- | --- | --- |
| 查找 | O(1) | O(n) |
| 插入 | O(1) | O(n) |
| 删除 | O(1) | O(n) |

最坏情况：所有 key 哈希到同一个槽位，退化为链表。

## 面试要点

- 理解哈希表为什么是 O(1)（哈希函数 + 数组随机访问）
- 知道冲突解决的两种策略及各自优劣
- 了解扩容机制和负载因子
- 能手写一个简单的哈希表