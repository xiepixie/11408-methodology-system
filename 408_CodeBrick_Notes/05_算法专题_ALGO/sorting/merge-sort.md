---
title: 归并排序
source: https://www.codebrick.tech/algo-blog/posts/sorting/merge-sort.html
---

# 归并排序

## 场景引入

归并排序是第一个打破 O(n²) 屏障的排序算法，也是**分治思想**最经典的应用之一。它的核心理念简洁而有力：把一个大问题拆成两个小问题，分别解决后再合并结果。

在实际工程中，归并排序有不可替代的价值：

- **稳定的 O(n log n)**：不像快速排序那样有最坏退化的风险
- **天然适合链表排序**：不需要随机访问，额外空间可降到 O(1)
- **外部排序的基础**：当数据量超出内存时，归并排序是唯一可行的方案

## 核心思路

归并排序遵循经典的**分治三步**：

- **分（Divide）**：将数组从中间一分为二
- **治（Conquer）**：递归地对左半和右半分别排序
- **合（Merge）**：将两个有序数组合并为一个有序数组

### merge 函数详解

归并排序的核心在于 `merge` 函数——将两个**已排序**的数组合并为一个有序数组：

- 准备两个指针 `i` 和 `j`，分别指向左右数组的头部
- 比较 `left[i]` 和 `right[j]`，将较小的放入结果数组
- 移动对应指针
- 当一个数组遍历完后，将另一个数组的剩余元素全部放入结果

这个过程是 O(n) 的，因为每个元素恰好被放入结果数组一次。

## 算法流程图

## 可视化演示
加载可视化中...

## 代码实现

### 递归版（自顶向下）
javascript

```
function mergeSort(arr) {
  if (arr.length <= 1) return arr;

  const mid = Math.floor(arr.length / 2);
  const left = mergeSort(arr.slice(0, mid));
  const right = mergeSort(arr.slice(mid));

  return merge(left, right);
}

function merge(left, right) {
  const result = [];
  let i = 0, j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] <= right[j]) {
      result.push(left[i++]);
    } else {
      result.push(right[j++]);
    }
  }

  // 将剩余元素追加到结果
  while (i < left.length) result.push(left[i++]);
  while (j < right.length) result.push(right[j++]);

  return result;
}
```

### 原地归并（减少空间开销）

LeetCode 中通常使用原地归并以减少 `slice` 的开销：javascript

```
function mergeSortInPlace(arr, left = 0, right = arr.length - 1) {
  if (left >= right) return;

  const mid = (left + right) >> 1;
  mergeSortInPlace(arr, left, mid);
  mergeSortInPlace(arr, mid + 1, right);

  // 原地合并 [left, mid] 和 [mid+1, right]
  const temp = [];
  let i = left, j = mid + 1;
  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) temp.push(arr[i++]);
    else temp.push(arr[j++]);
  }
  while (i <= mid) temp.push(arr[i++]);
  while (j <= right) temp.push(arr[j++]);

  for (let k = 0; k < temp.length; k++) {
    arr[left + k] = temp[k];
  }
}
```

## 应用：归并排序求逆序对

归并排序的 merge 过程天然适合计算**逆序对**数量。当 `left[i] > right[j]` 时，`left[i..mid]` 中的所有元素都与 `right[j]` 构成逆序对。javascript

```
function countInversions(arr, left = 0, right = arr.length - 1) {
  if (left >= right) return 0;

  const mid = (left + right) >> 1;
  let count = 0;
  count += countInversions(arr, left, mid);
  count += countInversions(arr, mid + 1, right);

  const temp = [];
  let i = left, j = mid + 1;
  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) {
      temp.push(arr[i++]);
    } else {
      count += mid - i + 1; // 关键：left[i..mid] 都大于 right[j]
      temp.push(arr[j++]);
    }
  }
  while (i <= mid) temp.push(arr[i++]);
  while (j <= right) temp.push(arr[j++]);

  for (let k = 0; k < temp.length; k++) arr[left + k] = temp[k];
  return count;
}
```

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 最好 | O(n log n) | O(n) |
| 平均 | O(n log n) | O(n) |
| 最坏 | O(n log n) | O(n) |

**稳定性**：**稳定**。merge 时 `left[i] <= right[j]` 使用 `<=`，保证相等元素保持原有相对顺序。

### 递归树与空间复杂度

归并排序的递归调用形成一棵**满二叉树**：

```
                mergeSort(0,7)
               /              \
        mergeSort(0,3)    mergeSort(4,7)
         /        \         /        \
    sort(0,1)  sort(2,3) sort(4,5) sort(6,7)
     / \        / \        / \       / \
   (0) (1)   (2) (3)   (4) (5)   (6) (7)
```

- 树的高度 = `log₂(n)`
- 每一层的 merge 操作总共处理 n 个元素 → 每层时间 O(n)
- 总时间 = O(n) × O(log n) = **O(n log n)**

**空间怎么算？**

关键在于：虽然递归树有很多节点，但**同一时刻只有一个 merge 在执行**。`mergeSort` 函数本身只做分割（O(1) 空间），真正需要临时数组的是 `merge` 函数。

- `merge` 函数的临时数组最大为 n → O(n)
- 递归栈深度 = O(log n)
- 总空间 = O(n) + O(log n) = **O(n)**

**为什么不是 O(n log n) 空间？** 因为每层的 merge 临时数组用完就释放了，不会同时存在多个大数组。

### 实测比较与拷贝次数
数组大小502001,0005,00010,000数据分布随机已排序逆序基本有序 点击「运行测试」，在你的浏览器中实时运行排序算法，统计比较和交换次数。

## 深入理解

- 归并排序是唯一**稳定的** O(n log n) 比较类排序算法
- merge 函数是核心——很多题目本质上都是"合并两个有序序列"
- 分治递归的时间复杂度推导：T(n) = 2T(n/2) + O(n) = O(n log n)
- 求逆序对是归并排序的经典应用，值得深入理解

## LeetCode 练习

- [LC 912. 排序数组](https://leetcode.cn/problems/sort-an-array/) — 归并排序标准实现
- [LC 148. 排序链表](https://leetcode.cn/problems/sort-list/) — 链表归并排序，空间可优化到 O(1)
- [LC 剑指 Offer 51. 数组中的逆序对](https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/) — 归并排序经典应用
- [LC 315. 计算右侧小于当前元素的个数](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/) — 归并排序进阶应用
- [LC 23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/) — merge 思想的扩展