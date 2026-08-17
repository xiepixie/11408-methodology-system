---
title: 回文链表判断
source: https://www.codebrick.tech/algo-blog/posts/linked-list/palindrome.html
---

# 回文链表判断

## 场景引入

判断一个字符串是否是回文很简单——双指针从两端向中间靠拢即可。但链表只能单向遍历，没有"从尾部往前走"的能力。如何在 O(1) 空间内判断链表是否回文？

这道题巧妙地综合了链表的两个基础操作：**快慢指针找中点**和**链表反转**。如果你已经掌握了这两个技巧，这道题就是把它们组合起来。

## 核心思路

### 方法一：找中点 + 反转后半部分 + 比较

- 用快慢指针找到链表中点
- 反转后半部分链表
- 从头和从中间同时遍历，逐个比较

```
原始:  1 -> 2 -> 3 -> 2 -> 1
找中点: slow 停在 3
反转后半: 1 -> 2 -> 3  1 -> 2
比较:   1==1, 2==2 => 回文!
```

### 方法二：递归后序遍历

利用递归的**后序位置**，相当于从链表尾部开始逆序访问节点。同时维护一个从头部正序访问的指针，两者对比。javascript

```
let left = head;
function check(right) {
  if (right === null) return true;
  let res = check(right.next); // 先递归到底
  // 后序位置：right 从右往左
  res = res && (left.val === right.val);
  left = left.next; // left 从左往右
  return res;
}
```

## 可视化演示

### 方法一：找中点 + 反转 + 比较
加载可视化中...

## 代码实现

### 方法一：找中点 + 反转（推荐）
javascript

```
function isPalindrome(head) {
  // 第一步：快慢指针找中点
  let slow = head, fast = head;
  while (fast !== null && fast.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // 第二步：反转后半部分
  let prev = null;
  let curr = slow;
  while (curr !== null) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  // 第三步：从两端向中间比较
  let left = head, right = prev;
  while (right !== null) {
    if (left.val !== right.val) return false;
    left = left.next;
    right = right.next;
  }
  return true;
}
```

注意几个细节：

- **奇数长度**：`1->2->3->2->1`，slow 停在 3，反转后半 `1->2->3` 和 `1->2->3`，比较 3 个节点
- **偶数长度**：`1->2->2->1`，slow 停在第二个 2，反转后半 `1->2` 和 `1->2`，比较 2 个节点
- 两种情况都能正确处理，因为我们只比较到 `right` 为 null

### 方法二：递归后序遍历
javascript

```
function isPalindrome(head) {
  let left = head;

  function check(right) {
    if (right === null) return true;

    // 先递归到链表末尾
    let res = check(right.next);

    // 后序位置：right 从右向左回溯
    res = res && (left.val === right.val);
    left = left.next; // left 从左向右前进

    return res;
  }

  return check(head);
}
```

递归法代码更简洁，但空间复杂度为 O(n)（递归栈）。面试中如果面试官要求 O(1) 空间，必须用方法一。

## 奇偶长度的处理

```
奇数: 1 -> 2 -> 3 -> 2 -> 1
                s         f=null
      反转后半: 1 -> 2 -> 3   null <- 3 <- 2 <- 1

偶数: 1 -> 2 -> 2 -> 1
                s    f=null (f.next=null)
      反转后半: 1 -> 2   null <- 2 <- 1
```

快慢指针结束后，`slow` 指向后半部分的起点。无论奇偶，从 `slow` 开始反转再比较都能正确工作。

## 复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 找中点+反转 | O(n) | O(1) |
| 递归后序遍历 | O(n) | O(n) |

方法一在时间和空间上都是最优的，面试首选。

## 扩展思考

如果面试官追问"能否在不修改原链表的情况下判断回文"，可以：

- 用方法一，但在比较完成后再把后半部分反转回来
- 用方法二递归法，不会修改链表结构
- 将链表值复制到数组，用双指针判断（空间 O(n)）

## LeetCode 练习

- LC 234. 回文链表（简单）
- LC 143. 重排链表（中等，也需要找中点+反转）
- LC 9. 回文数（简单，数字版本，不用链表但思路类似）