---
title: 哈希表经典应用
source: https://www.codebrick.tech/algo-blog/posts/hash/classic.html
---

# 哈希表经典应用

## 场景引入

哈希表是面试中使用频率最高的数据结构之一。它的核心能力就一个：**O(1) 查找**。大量看似复杂的问题，加上哈希表就能从 O(n²) 降到 O(n)。

## LC 1. 两数之和

给定数组 nums 和目标值 target，找到两个数使其和为 target，返回下标。

### 暴力：O(n²)
javascript

```
for (let i = 0; i < nums.length; i++)
  for (let j = i + 1; j < nums.length; j++)
    if (nums[i] + nums[j] === target) return [i, j];
```

### 哈希表：O(n)
javascript

```
function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
  return [];
}
```

**关键思路**：遍历时边查边存，用哈希表记录「我需要的那个数」是否已经出现过。

## LC 49. 字母异位词分组

给定字符串数组，将字母异位词分组。如 ["eat","tea","ate"] → [["eat","tea","ate"]]javascript

```
function groupAnagrams(strs) {
  const map = new Map();
  for (const s of strs) {
    const key = [...s].sort().join('');
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(s);
  }
  return [...map.values()];
}
```

**关键思路**：字母异位词排序后相同，用排序后的字符串作为哈希表的 key。

## LC 128. 最长连续序列

给定未排序数组，找出最长连续元素序列的长度。要求 O(n) 时间。javascript

```
function longestConsecutive(nums) {
  const set = new Set(nums);
  let maxLen = 0;

  for (const num of set) {
    // 只从序列起点开始计数
    if (!set.has(num - 1)) {
      let current = num;
      let len = 1;
      while (set.has(current + 1)) {
        current++;
        len++;
      }
      maxLen = Math.max(maxLen, len);
    }
  }
  return maxLen;
}
```

**关键思路**：用 Set 实现 O(1) 查找。只从每个序列的**起点**（没有 num-1 的数）开始计数，避免重复计算。

## LC 380. O(1) 时间插入、删除和获取随机元素
javascript

```
class RandomizedSet {
  constructor() {
    this.map = new Map(); // val -> index
    this.list = [];
  }

  insert(val) {
    if (this.map.has(val)) return false;
    this.map.set(val, this.list.length);
    this.list.push(val);
    return true;
  }

  remove(val) {
    if (!this.map.has(val)) return false;
    const idx = this.map.get(val);
    const last = this.list[this.list.length - 1];
    this.list[idx] = last;
    this.map.set(last, idx);
    this.list.pop();
    this.map.delete(val);
    return true;
  }

  getRandom() {
    const idx = Math.floor(Math.random() * this.list.length);
    return this.list[idx];
  }
}
```

**关键思路**：HashMap + 数组。删除时将目标与末尾元素交换，然后 pop，保证 O(1)。

## 哈希表的通用模式

| 模式 | 说明 | 例题 |
| --- | --- | --- |
| 查找配对 | 用哈希表存已遍历元素，查找互补值 | LC 1 |
| 分组归类 | 用特征值作 key，同类元素归到同一组 | LC 49 |
| 去重计数 | 用 Set/Map 记录出现情况 | LC 128 |
| 索引映射 | 维护值到下标的映射，支持 O(1) 定位 | LC 380 |

## 复杂度分析

所有上述解法时间复杂度均为 **O(n)**，空间复杂度 **O(n)**。

## LeetCode 练习

- LC 1. 两数之和 ⭐
- LC 49. 字母异位词分组 ⭐
- LC 128. 最长连续序列 ⭐
- LC 380. O(1) 时间插入、删除和获取随机元素
- LC 242. 有效的字母异位词
- LC 349. 两个数组的交集