---
title: 双指针技巧：左右指针
source: https://www.codebrick.tech/algo-blog/posts/array/two-pointer-left-right.html
---

# 双指针技巧：左右指针

## 场景引入

给你一个有序数组和一个目标值，找出数组中两个数使它们的和等于目标值。暴力枚举所有组合需要 O(n²)，有没有更快的方法？

左右指针（又叫对撞指针）就是解决这类问题的杀手锏：**left 从最左端出发，right 从最右端出发，两个指针相向而行**，根据当前状态决定移动哪个指针。

与快慢指针的"同向而行"不同，左右指针是"相向而行"，利用的是数组的有序性或某种单调性质来缩小搜索空间。

## 核心思路

左右指针的通用框架：javascript

```
function leftRightPointer(nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    // 根据当前 left、right 的状态做判断
    if (/* 找到答案 */) {
      return [left, right];
    } else if (/* 需要增大 */) {
      left++;
    } else {
      right--;
    }
  }
}
```

关键点：

- left 和 right 从两端出发，每次至少移动一个指针
- 循环终止条件通常是 `left < right` 或 `left <= right`
- 每一步通过比较来决定移动哪个指针，从而排除不可能的候选

## 可视化演示

### LC 167. 两数之和 II
加载可视化中...

## 代码实现

### LC 167. 两数之和 II - 输入有序数组
javascript

```
function twoSum(numbers, target) {
  let left = 0;
  let right = numbers.length - 1;

  while (left < right) {
    let sum = numbers[left] + numbers[right];
    if (sum === target) {
      return [left + 1, right + 1];
    } else if (sum < target) {
      left++; // 和太小，增大左边
    } else {
      right--; // 和太大，减小右边
    }
  }

  return [-1, -1];
}
```

为什么这样是对的？因为数组有序：

- `sum < target` 时，left 右移可以增大 sum，而 right 左移只会减小 sum
- `sum > target` 时，right 左移可以减小 sum

### LC 11. 盛最多水的容器
javascript

```
function maxArea(height) {
  let left = 0;
  let right = height.length - 1;
  let maxWater = 0;

  while (left < right) {
    let w = right - left;
    let h = Math.min(height[left], height[right]);
    maxWater = Math.max(maxWater, w * h);

    // 移动较矮的那一边，才有可能找到更大的面积
    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxWater;
}
```

关键洞察：宽度一定在缩小，所以只有移动较矮的边才可能让高度增加，从而获得更大面积。

### LC 15. 三数之和
javascript

```
function threeSum(nums) {
  nums.sort((a, b) => a - b);
  let result = [];

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue; // 跳过重复

    let left = i + 1;
    let right = nums.length - 1;
    let target = -nums[i];

    while (left < right) {
      let sum = nums[left] + nums[right];
      if (sum === target) {
        result.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
      } else if (sum < target) {
        left++;
      } else {
        right--;
      }
    }
  }

  return result;
}
```

思路：先排序，固定一个数 `nums[i]`，对剩余部分用左右指针做两数之和。去重是难点：外层跳过重复的 `nums[i]`，内层跳过重复的 left 和 right。

### LC 42. 接雨水
javascript

```
function trap(height) {
  let left = 0, right = height.length - 1;
  let leftMax = 0, rightMax = 0;
  let water = 0;

  while (left < right) {
    leftMax = Math.max(leftMax, height[left]);
    rightMax = Math.max(rightMax, height[right]);

    if (leftMax < rightMax) {
      water += leftMax - height[left];
      left++;
    } else {
      water += rightMax - height[right];
      right--;
    }
  }

  return water;
}
```

关键洞察：每个位置能接的雨水 = `min(leftMax, rightMax) - height[i]`。当 `leftMax < rightMax` 时，左边一定是瓶颈，可以确定 left 位置的雨水量，然后移动 left。

## 框架对比

| 题目 | 指针移动策略 | 核心判断 |
| --- | --- | --- |
| 两数之和 | sum 小则左移，sum 大则右移 | 有序数组的单调性 |
| 盛水容器 | 移动较矮的边 | 宽度递减，只有高度增加才有意义 |
| 三数之和 | 固定一个 + 两数之和 | 排序后降维 |
| 接雨水 | 移动 max 较小的一侧 | 短板决定水量 |

## 复杂度分析

| 题目 | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| LC 167 两数之和 II | O(n) | O(1) |
| LC 11 盛水容器 | O(n) | O(1) |
| LC 15 三数之和 | O(n²) | O(1)（不计输出） |
| LC 42 接雨水 | O(n) | O(1) |

## LeetCode 练习

按难度递进：

- LC 167. 两数之和 II - 输入有序数组（中等）
- LC 11. 盛最多水的容器（中等）
- LC 15. 三数之和（中等）
- LC 42. 接雨水（困难）
- LC 16. 最接近的三数之和（中等）
- LC 18. 四数之和（中等）