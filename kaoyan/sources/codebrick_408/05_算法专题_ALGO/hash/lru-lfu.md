---
title: LRU / LFU 缓存
source: https://www.codebrick.tech/algo-blog/posts/hash/lru-lfu.html
---

# LRU / LFU 缓存

## 场景引入

操作系统的内存管理、数据库的缓冲池、CDN 的内容缓存——所有缓存系统都面临一个问题：**缓存满了该淘汰谁？**

LRU（Least Recently Used）淘汰最久没被使用的，LFU（Least Frequently Used）淘汰使用次数最少的。这两道题是面试中最经典的数据结构设计题。

## LC 146. LRU 缓存

要求：`get` 和 `put` 都是 O(1)。

### 设计思路

- **哈希表**：O(1) 查找 key 对应的节点
- **双向链表**：O(1) 插入和删除，维护使用顺序

链表头部 = 最近使用，链表尾部 = 最久未使用。

### 实现
javascript

```
class ListNode {
  constructor(key, val) {
    this.key = key;
    this.val = val;
    this.prev = null;
    this.next = null;
  }
}

class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.map = new Map();
    // 虚拟头尾节点，避免边界判断
    this.head = new ListNode(0, 0);
    this.tail = new ListNode(0, 0);
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  _remove(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }

  _addToHead(node) {
    node.next = this.head.next;
    node.prev = this.head;
    this.head.next.prev = node;
    this.head.next = node;
  }

  get(key) {
    if (!this.map.has(key)) return -1;
    const node = this.map.get(key);
    this._remove(node);
    this._addToHead(node); // 移到头部（标记为最近使用）
    return node.val;
  }

  put(key, value) {
    if (this.map.has(key)) {
      const node = this.map.get(key);
      node.val = value;
      this._remove(node);
      this._addToHead(node);
    } else {
      const node = new ListNode(key, value);
      this.map.set(key, node);
      this._addToHead(node);
      if (this.map.size > this.capacity) {
        const lru = this.tail.prev; // 尾部 = 最久未使用
        this._remove(lru);
        this.map.delete(lru.key);
      }
    }
  }
}
```

### 关键点

- **虚拟头尾节点**：避免 null 边界判断，简化代码
- **节点存 key**：淘汰时需要从 Map 中删除，所以节点要记住自己的 key
- **每次 get/put 都移到头部**：保持链表按使用时间排序

## LC 460. LFU 缓存

LFU 比 LRU 复杂：淘汰使用频率最低的，频率相同则淘汰最久未使用的。

### 设计思路

- **keyMap**：key →
- **freqMap**：freq → 该频率下的所有 key（用 LinkedHashSet 保持插入顺序）
- **minFreq**：当前最小频率javascript

```
class LFUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.keyMap = new Map();    // key -> { val, freq }
    this.freqMap = new Map();   // freq -> Set (保持插入顺序)
    this.minFreq = 0;
  }

  _increaseFreq(key) {
    const { val, freq } = this.keyMap.get(key);
    this.keyMap.set(key, { val, freq: freq + 1 });
    // 从旧频率集合移除
    this.freqMap.get(freq).delete(key);
    if (this.freqMap.get(freq).size === 0) {
      this.freqMap.delete(freq);
      if (this.minFreq === freq) this.minFreq++;
    }
    // 加入新频率集合
    if (!this.freqMap.has(freq + 1)) this.freqMap.set(freq + 1, new Set());
    this.freqMap.get(freq + 1).add(key);
  }

  get(key) {
    if (!this.keyMap.has(key)) return -1;
    this._increaseFreq(key);
    return this.keyMap.get(key).val;
  }

  put(key, value) {
    if (this.capacity === 0) return;
    if (this.keyMap.has(key)) {
      this.keyMap.get(key).val = value;
      this._increaseFreq(key);
      return;
    }
    if (this.keyMap.size >= this.capacity) {
      // 淘汰 minFreq 中最早插入的 key
      const keys = this.freqMap.get(this.minFreq);
      const evictKey = keys.values().next().value; // Set 的第一个元素
      keys.delete(evictKey);
      if (keys.size === 0) this.freqMap.delete(this.minFreq);
      this.keyMap.delete(evictKey);
    }
    this.keyMap.set(key, { val: value, freq: 1 });
    if (!this.freqMap.has(1)) this.freqMap.set(1, new Set());
    this.freqMap.get(1).add(key);
    this.minFreq = 1;
  }
}
```

## LRU vs LFU 对比

|  | LRU | LFU |
| --- | --- | --- |
| 淘汰策略 | 最久未使用 | 使用次数最少 |
| 数据结构 | HashMap + 双向链表 | HashMap + 频率桶 |
| 实现复杂度 | 中等 | 较高 |
| 适用场景 | 访问模式有时间局部性 | 访问频率差异大 |

## 复杂度分析

两种缓存的 get/put 均为 **O(1)** 时间，**O(capacity)** 空间。

## 面试要点

- LRU 是必须能手写的题目，面试出现频率极高
- 理解「为什么需要双向链表而不是单链表」（删除操作需要 O(1)）
- 理解「为什么节点要存 key」（淘汰时需要从 Map 中删除）