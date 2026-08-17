---
title: 二分查找：三种边界搜索模板
source: https://www.codebrick.tech/algo-blog/posts/array/binary-search.html
---

# 二分查找：三种边界搜索模板

## 场景引入

二分查找看似简单，但实际写代码时总是容易出错：`while` 里是 `<=` 还是 `<`？`right` 是 `mid` 还是 `mid - 1`？返回 `left` 还是 `right`？

更麻烦的是，很多题目不是简单地"找一个数"，而是找"第一个大于等于 target 的位置"或者"最后一个等于 target 的位置"。这就需要**左边界二分**和**右边界二分**。

本文给出三种统一模板，记住它们就能覆盖几乎所有二分查找问题。

## 核心思路

二分查找的本质是：**在一个有序序列中，利用单调性每次排除一半的搜索空间**。

三种模板的关键区别在于**找到 target 后的行为**：

| 模板 | 找到 target 后 | 搜索目标 |
| --- | --- | --- |
| 基础二分 | 直接返回 | 任意一个等于 target 的位置 |
| 左边界 | 收缩右边界 `right = mid - 1` | 第一个等于 target 的位置 |
| 右边界 | 收缩左边界 `left = mid + 1` | 最后一个等于 target 的位置 |

## 可视化演示

### 基础二分查找
加载可视化中...

## 代码实现

### 模板一：基础二分查找
javascript

```
function binarySearch(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}
```

要点：

- 搜索区间 `[left, right]` 是**闭区间**
- `while (left <= right)` 因为 `left === right` 时区间 `[left, left]` 仍有一个元素
- 找到就返回，找不到返回 -1

### 模板二：左边界二分查找
javascript

```
function leftBound(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) {
      right = mid - 1; // 关键：不返回，继续向左收缩
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  // left 就是第一个 >= target 的位置
  if (left >= nums.length || nums[left] !== target) {
    return -1;
  }
  return left;
}
```

要点：

- 找到 target 时，**不立即返回**，而是收缩右边界 `right = mid - 1`
- 循环结束后 `left` 指向第一个等于 target 的位置
- 需要额外检查 `left` 是否越界以及 `nums[left]` 是否等于 target

### 模板三：右边界二分查找
javascript

```
function rightBound(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) {
      left = mid + 1; // 关键：不返回，继续向右收缩
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  // right 就是最后一个 <= target 的位置
  if (right < 0 || nums[right] !== target) {
    return -1;
  }
  return right;
}
```

要点：

- 找到 target 时，收缩左边界 `left = mid + 1`
- 循环结束后 `right` 指向最后一个等于 target 的位置
- 需要检查 `right` 是否越界以及 `nums[right]` 是否等于 target

### 三种模板的统一理解

统一使用 `while (left <= right)` 闭区间写法，区别仅在于找到 target 后的行为：javascript

```
// 基础：直接返回
if (nums[mid] === target) return mid;

// 左边界：锁定左端，继续向左搜
if (nums[mid] === target) right = mid - 1;

// 右边界：锁定右端，继续向右搜
if (nums[mid] === target) left = mid + 1;
```

## 实战应用

### LC 34. 在排序数组中查找元素的第一个和最后一个位置
javascript

```
function searchRange(nums, target) {
  return [leftBound(nums, target), rightBound(nums, target)];
}
```

直接组合左边界和右边界两个模板。

### LC 875. 爱吃香蕉的珂珂
javascript

```
function minEatingSpeed(piles, h) {
  let left = 1;
  let right = Math.max(...piles);

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let hours = 0;
    for (let pile of piles) {
      hours += Math.ceil(pile / mid);
    }
    if (hours <= h) {
      right = mid - 1; // 可以更慢，向左搜
    } else {
      left = mid + 1; // 太慢了，加速
    }
  }

  return left;
}
```

这是**二分答案**的经典应用：答案具有单调性（速度越快，花的时间越少），对答案进行二分搜索。

### LC 1011. 在 D 天内送达包裹的船的能力
javascript

```
function shipWithinDays(weights, days) {
  let left = Math.max(...weights);
  let right = weights.reduce((a, b) => a + b, 0);

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let needDays = 1, curWeight = 0;
    for (let w of weights) {
      if (curWeight + w > mid) {
        needDays++;
        curWeight = 0;
      }
      curWeight += w;
    }
    if (needDays <= days) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
}
```

同样是二分答案：运载能力越大，需要的天数越少。

## 复杂度分析

- **时间复杂度**：O(log n)。每次排除一半搜索空间。
- **空间复杂度**：O(1)。只用了几个变量。
- **二分答案类题目**：O(n log m)，其中 n 是验证一次答案的代价，m 是答案的搜索范围。

## LeetCode 练习

按难度递进：

- LC 704. 二分查找（简单）
- LC 35. 搜索插入位置（简单）
- LC 34. 在排序数组中查找元素的第一个和最后一个位置（中等）
- LC 875. 爱吃香蕉的珂珂（中等）
- LC 1011. 在 D 天内送达包裹的船的能力（中等）
- LC 410. 分割数组的最大值（困难）