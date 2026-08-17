---
title: 双指针技巧：快慢指针
source: https://www.codebrick.tech/algo-blog/posts/array/two-pointer-fast-slow.html
---

# 双指针技巧：快慢指针

## 场景引入

给你一个**有序数组**，要求原地删除重复元素，返回去重后的长度。不能使用额外数组，只能在原数组上操作。

暴力做法是每遇到重复就把后面的元素整体前移，时间复杂度 O(n²)。有没有办法一次遍历就搞定？

快慢指针就是解决这类**原地修改数组**问题的利器。核心思想：**slow 指针维护结果区域的边界，fast 指针负责扫描整个数组**。两个指针同向而行，fast 跑得快，slow 跑得慢，因此叫"快慢指针"。

## 核心思路

快慢指针的通用框架：javascript

```
function fastSlowPointer(nums) {
  let slow = 0;

  for (let fast = 0; fast < nums.length; fast++) {
    if (/* fast 指向的元素满足保留条件 */) {
      nums[slow] = nums[fast];
      slow++;
    }
  }

  return slow; // slow 就是结果数组的长度
}
```

关键点：

- **slow 指针**左边（不含 slow）的元素都是已确认保留的结果
- **fast 指针**负责逐个扫描，判断当前元素是否该保留
- 满足条件时，把 fast 处的值赋给 slow 处，然后 slow 前进
- 最终 slow 就是结果长度

## 可视化演示

### LC 26. 删除有序数组中的重复项
加载可视化中...

## 代码实现

### LC 26. 删除有序数组中的重复项
javascript

```
function removeDuplicates(nums) {
  if (nums.length === 0) return 0;
  let slow = 0;
  let fast = 1;

  while (fast < nums.length) {
    if (nums[fast] !== nums[slow]) {
      slow++;
      nums[slow] = nums[fast];
    }
    fast++;
  }

  return slow + 1;
}
```

思路：有序数组中，相同元素一定相邻。fast 每次和 slow 比较，不同就保留。

### LC 27. 移除元素
javascript

```
function removeElement(nums, val) {
  let slow = 0;

  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] !== val) {
      nums[slow] = nums[fast];
      slow++;
    }
  }

  return slow;
}
```

思路：fast 扫描所有元素，不等于 val 的就保留到 slow 位置。

### LC 283. 移动零
javascript

```
function moveZeroes(nums) {
  let slow = 0;

  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] !== 0) {
      // 交换而非覆盖，保证零被移到后面
      let temp = nums[slow];
      nums[slow] = nums[fast];
      nums[fast] = temp;
      slow++;
    }
  }
}
```

思路：和"移除元素"几乎一样，区别在于用**交换**代替覆盖，这样零会自然移到数组末尾。

## 三道题的统一视角

| 题目 | 保留条件 | 操作方式 | 返回值 |
| --- | --- | --- | --- |
| LC 26 删除重复项 | `nums[fast] !== nums[slow]` | 覆盖 | `slow + 1` |
| LC 27 移除元素 | `nums[fast] !== val` | 覆盖 | `slow` |
| LC 283 移动零 | `nums[fast] !== 0` | 交换 | 无（原地修改） |

可以看到，三道题本质上是同一个框架，只是保留条件和操作方式略有不同。

## 复杂度分析

- **时间复杂度**：O(n)。fast 指针遍历一次数组，slow 指针最多移动 n 次。
- **空间复杂度**：O(1)。只使用了两个指针变量，原地修改。

## LeetCode 练习

按难度递进：

- LC 26. 删除有序数组中的重复项（简单）
- LC 27. 移除元素（简单）
- LC 283. 移动零（简单）
- LC 80. 删除有序数组中的重复项 II（中等）— 每个元素最多保留两次
- LC 844. 比较含退格的字符串（简单）— 从后往前的快慢指针变体