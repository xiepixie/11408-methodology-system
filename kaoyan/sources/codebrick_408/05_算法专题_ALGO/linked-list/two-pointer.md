---
title: 链表双指针技巧
source: https://www.codebrick.tech/algo-blog/posts/linked-list/two-pointer.html
---

# 链表双指针技巧

## 场景引入

链表题在面试中出现频率极高，而其中大部分都可以用**双指针**技巧解决。和数组双指针不同，链表双指针不能随机访问，只能沿着 `next` 指针移动。正因如此，链表双指针的套路更加固定，掌握几个核心模式就能覆盖绝大多数题目。

本文梳理链表双指针的三大类应用：**虚拟头节点 + 双指针合并**、**快慢指针**、**先后指针**。

## 核心思路

### 模式一：虚拟头节点 + 双指针合并

合并类问题的标准套路：创建一个 `dummy` 虚拟头节点，用一个指针 `p` 在新链表上前进，两个指针分别遍历两个原链表。javascript

```
let dummy = new ListNode(-1);
let p = dummy;
// p1, p2 分别指向两个链表
while (p1 !== null && p2 !== null) {
  if (/* 选 p1 的条件 */) {
    p.next = p1;
    p1 = p1.next;
  } else {
    p.next = p2;
    p2 = p2.next;
  }
  p = p.next;
}
```

### 模式二：快慢指针

快指针走两步，慢指针走一步。用于：

- **找中点**：快指针到末尾时，慢指针正好在中间
- **检测环**：如果有环，快慢指针必然相遇
- **找环入口**：相遇后，一个从头走，一个从相遇点走，再次相遇就是入口

### 模式三：先后指针

让一个指针先走 k 步，然后两个一起走。用于：

- **删除倒数第 N 个节点**：先走 N 步，保持间距
- **找倒数第 K 个节点**

## 可视化演示

### LC 21. 合并两个有序链表
加载可视化中...

### LC 876. 链表的中间节点
加载可视化中...

### LC 19. 删除链表的倒数第 N 个节点
加载可视化中...

## 代码实现

### 合并两个有序链表（LC 21）
javascript

```
function mergeTwoLists(l1, l2) {
  let dummy = new ListNode(-1);
  let p = dummy;
  let p1 = l1, p2 = l2;

  while (p1 !== null && p2 !== null) {
    if (p1.val <= p2.val) {
      p.next = p1;
      p1 = p1.next;
    } else {
      p.next = p2;
      p2 = p2.next;
    }
    p = p.next;
  }

  if (p1 !== null) p.next = p1;
  if (p2 !== null) p.next = p2;

  return dummy.next;
}
```

### 快慢指针找中点（LC 876）
javascript

```
function middleNode(head) {
  let slow = head, fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
  return slow;
}
```

### 删除倒数第 N 个节点（LC 19）
javascript

```
function removeNthFromEnd(head, n) {
  let dummy = new ListNode(-1);
  dummy.next = head;
  let fast = dummy, slow = dummy;

  for (let i = 0; i <= n; i++) {
    fast = fast.next;
  }

  while (fast !== null) {
    slow = slow.next;
    fast = fast.next;
  }

  slow.next = slow.next.next;
  return dummy.next;
}
```

### 环形链表检测（LC 141）
javascript

```
function hasCycle(head) {
  let slow = head, fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}
```

### 环形链表入口（LC 142）
javascript

```
function detectCycle(head) {
  let slow = head, fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) break;
  }
  if (fast === null || fast.next === null) return null;

  // 一个从头走，一个从相遇点走
  slow = head;
  while (slow !== fast) {
    slow = slow.next;
    fast = fast.next;
  }
  return slow;
}
```

**为什么相遇点到入口的距离等于起点到入口的距离？** 设起点到入口距离为 `a`，入口到相遇点为 `b`，相遇点回到入口为 `c`。快指针走了 `a+b+c+b`，慢指针走了 `a+b`。因为快指针速度是慢指针的 2 倍：`a+b+c+b = 2(a+b)`，化简得 `c = a`。

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 合并两个有序链表 | O(n + m) | O(1) |
| 链表中点 | O(n) | O(1) |
| 删除倒数第N个 | O(n) | O(1) |
| 环形链表检测 | O(n) | O(1) |
| 环形链表入口 | O(n) | O(1) |

所有双指针解法的空间复杂度都是 O(1)，这正是链表双指针的优势。

## LeetCode 练习

按难度递进：

- LC 21. 合并两个有序链表（简单）
- LC 876. 链表的中间节点（简单）
- LC 141. 环形链表（简单）
- LC 160. 相交链表（简单）
- LC 19. 删除链表的倒数第 N 个结点（中等）
- LC 142. 环形链表 II（中等）
- LC 86. 分隔链表（中等）
- LC 23. 合并 K 个升序链表（困难）