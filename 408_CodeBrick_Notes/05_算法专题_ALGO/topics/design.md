---
title: 设计类题目：数据结构组合的艺术
source: https://www.codebrick.tech/algo-blog/posts/topics/design.html
---

# 设计类题目：数据结构组合的艺术

## 场景引入

设计类题目是面试中的"综合题"——考的不是某个算法，而是你能否**选择并组合合适的数据结构**来满足多个约束条件（如同时要求 O(1) 查找和 O(1) 删除）。

## 解题思路

- **明确 API**：需要支持哪些操作？
- **分析复杂度要求**：每个操作的时间复杂度要求？
- **选择数据结构**：哪些数据结构能满足这些要求？通常需要组合多个。
- **实现并验证**

### 设计题解题流程

## LC 380. O(1) 时间插入、删除和获取随机元素

**约束**：insert、remove、getRandom 都要 O(1)。

**分析**：

- O(1) 查找 → 需要 HashMap
- O(1) 删除 → 数组尾部删除是 O(1)
- O(1) 随机 → 数组支持随机索引

**方案**：HashMap（值→下标） + 数组javascript

```
class RandomizedSet {
  constructor() {
    this.map = new Map();
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
    // 将末尾元素移到被删位置
    this.list[idx] = last;
    this.map.set(last, idx);
    this.list.pop();
    this.map.delete(val);
    return true;
  }

  getRandom() {
    return this.list[Math.floor(Math.random() * this.list.length)];
  }
}
```

**关键技巧**：删除时，将目标元素与末尾元素交换，然后 pop 末尾。

## LC 355. 设计推特

支持：postTweet、getNewsFeed（最近 10 条）、follow、unfollow。

**方案**：HashMap（用户关注列表） + 每个用户的推文链表 + 合并 K 个有序链表javascript

```
class Twitter {
  constructor() {
    this.tweets = new Map();   // userId -> [{id, time}]
    this.follows = new Map();  // userId -> Set<userId>
    this.time = 0;
  }

  postTweet(userId, tweetId) {
    if (!this.tweets.has(userId)) this.tweets.set(userId, []);
    this.tweets.get(userId).push({ id: tweetId, time: this.time++ });
  }

  getNewsFeed(userId) {
    // 收集自己和关注者的所有推文
    const users = [userId, ...(this.follows.get(userId) || [])];
    const allTweets = [];
    for (const uid of users) {
      const tweets = this.tweets.get(uid) || [];
      allTweets.push(...tweets);
    }
    // 按时间降序，取前 10
    allTweets.sort((a, b) => b.time - a.time);
    return allTweets.slice(0, 10).map(t => t.id);
  }

  follow(followerId, followeeId) {
    if (!this.follows.has(followerId)) this.follows.set(followerId, new Set());
    this.follows.get(followerId).add(followeeId);
  }

  unfollow(followerId, followeeId) {
    this.follows.get(followerId)?.delete(followeeId);
  }
}
```

## 设计题的常见组合

| 需求 | 数据结构组合 |
| --- | --- |
| O(1) 查找 + O(1) 删除 | HashMap + 双向链表 |
| O(1) 查找 + O(1) 随机 | HashMap + 数组 |
| 按时间/频率排序 | HashMap + 堆/有序集合 |
| 前缀搜索 | Trie 树 |
| 合并有序序列 | 堆（优先队列） |

## 面试建议

- 先和面试官确认 API 和复杂度要求
- 分析每个操作需要什么能力（查找？删除？排序？）
- 选择数据结构组合，解释为什么
- 写代码前先说清楚设计思路

## LeetCode 练习

- LC 146. LRU 缓存 ⭐
- LC 380. O(1) 时间插入、删除和获取随机元素
- LC 355. 设计推特
- LC 460. LFU 缓存
- LC 895. 最大频率栈