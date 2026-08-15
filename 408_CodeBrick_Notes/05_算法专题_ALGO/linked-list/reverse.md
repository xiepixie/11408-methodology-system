---
title: 链表反转：递归与迭代
source: https://www.codebrick.tech/algo-blog/posts/linked-list/reverse.html
---

# 链表反转：递归与迭代

## 场景引入

链表反转是面试中出现频率最高的链表题之一。它看似简单，但递归和迭代两种写法各有巧妙之处，而且它是很多链表进阶题的基础操作——比如**区间反转**和 **K 个一组反转**都是在基础反转上的扩展。

我们从最简单的全链表反转开始，逐步进阶到区间反转和 K 个一组反转。

## 核心思路

### 迭代法：三指针就地翻转

维护三个指针 `prev`、`curr`、`next`，每一步把 `curr.next` 指向 `prev`，然后三个指针整体右移。

```
初始:  null <- 1    2 -> 3 -> 4 -> null
              prev  curr
一步:  null <- 1 <- 2    3 -> 4 -> null
                    prev curr
```

### 递归法：后序位置反转指针

递归到链表末尾，在**回溯时**（后序位置）修改指针方向。核心是 `head.next.next = head`，让下一个节点指回自己。

## 可视化演示

### 迭代反转
加载可视化中...

### 递归反转
加载可视化中...

## 代码实现

### LC 206. 反转链表 —— 迭代法
javascript

```
function reverseList(head) {
  let prev = null;
  let curr = head;

  while (curr !== null) {
    let next = curr.next;   // 先保存下一个
    curr.next = prev;       // 反转指针
    prev = curr;            // prev 前进
    curr = next;            // curr 前进
  }

  return prev; // prev 就是新的头节点
}
```

**要点**：一定要先保存 `curr.next`，否则反转后就找不到下一个节点了。

### LC 206. 反转链表 —— 递归法
javascript

```
function reverseList(head) {
  // base case：空节点或只有一个节点
  if (head === null || head.next === null) {
    return head;
  }

  // 递归反转后面的部分，last 是反转后的新头
  let last = reverseList(head.next);

  // 让下一个节点指回自己
  head.next.next = head;
  // 自己指向 null（后续递归会修正）
  head.next = null;

  return last;
}
```

**递归理解要点**：

- `reverseList(head.next)` 会把 `head` 后面的链表全部反转，返回新头
- 此时 `head.next` 是反转后链表的**尾节点**
- `head.next.next = head` 让尾节点指回 `head`
- `head.next = null` 让 `head` 变成新尾

### LC 92. 反转链表 II —— 区间反转
javascript

```
function reverseBetween(head, left, right) {
  let dummy = new ListNode(-1);
  dummy.next = head;
  let pre = dummy;

  // 走到 left 的前一个节点
  for (let i = 0; i < left - 1; i++) {
    pre = pre.next;
  }

  // 头插法反转区间内的节点
  let curr = pre.next;
  for (let i = 0; i < right - left; i++) {
    let next = curr.next;
    curr.next = next.next;
    next.next = pre.next;
    pre.next = next;
  }

  return dummy.next;
}
```

**头插法**的核心思想：每次把 `curr` 后面的节点摘下来，插到 `pre` 后面。这样区间内的节点就自然逆序了。

### LC 25. K 个一组翻转链表
javascript

```
function reverseKGroup(head, k) {
  // 检查剩余节点是否足够 k 个
  let check = head;
  for (let i = 0; i < k; i++) {
    if (check === null) return head;
    check = check.next;
  }

  // 反转前 k 个
  let prev = null, curr = head;
  for (let i = 0; i < k; i++) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  // head 现在是这组的尾部，连接下一组的结果
  head.next = reverseKGroup(curr, k);
  return prev;
}
```

## 三种反转的关系

```
反转整个链表 (LC 206)
     ↓ 加上区间限制
反转区间 [left, right] (LC 92)
     ↓ 分段重复
K 个一组反转 (LC 25)
```

这三道题是递进关系。掌握了基础反转，后面两道就是在此基础上的变形。

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 反转链表（迭代） | O(n) | O(1) |
| 反转链表（递归） | O(n) | O(n) 递归栈 |
| 反转链表 II | O(n) | O(1) |
| K 个一组反转 | O(n) | O(n/k) 递归栈 |

递归法虽然代码优雅，但有 O(n) 的栈空间开销。面试中如果被问到空间优化，应该给出迭代解法。

## LeetCode 练习

按难度递进：

- LC 206. 反转链表（简单）
- LC 92. 反转链表 II（中等）
- LC 24. 两两交换链表中的节点（中等，K=2 的特例）
- LC 25. K 个一组翻转链表（困难）