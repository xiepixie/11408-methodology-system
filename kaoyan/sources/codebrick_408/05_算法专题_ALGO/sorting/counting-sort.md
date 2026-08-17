---
title: 计数排序
source: https://www.codebrick.tech/algo-blog/posts/sorting/counting-sort.html
---

# 计数排序

## 场景引入

比较类排序有一个理论下界：**O(n log n)**。无论怎么优化，只要排序算法基于元素之间的比较，就不可能更快。

但如果我们知道数据的额外信息呢？比如"所有元素都是 0-100 的整数"——这时候根本不需要比较，直接数每个数出现了几次，按顺序还原就行了。这就是计数排序的思路。

## 核心思路

- 找到数组中的最大值 `max`，创建一个长度为 `max + 1` 的计数数组 `count`
- 遍历原数组，`count[value]++`
- 遍历计数数组，按顺序还原元素

### 稳定版本

上面的简单版本会丢失元素的原始信息（只保留了值）。要实现**稳定排序**（保持相同值元素的原始顺序），需要一个改进：

- 统计每个值的出现次数
- 对计数数组做**前缀和**，使 `count[i]` 表示"值 ≤ i 的元素个数"
- **从后向前**遍历原数组，根据 `count[value]` 确定每个元素在输出数组中的位置，并递减 `count[value]`

从后向前遍历保证了相同值的元素按原始顺序排列。

## 算法流程图

## 代码实现

### 简单版本（只能排纯数字，不保证稳定）
javascript

```
function countingSortSimple(arr) {
  if (arr.length <= 1) return arr;

  const max = Math.max(...arr);
  const count = new Array(max + 1).fill(0);

  // 统计
  for (const val of arr) count[val]++;

  // 还原
  let idx = 0;
  for (let i = 0; i <= max; i++) {
    while (count[i] > 0) {
      arr[idx++] = i;
      count[i]--;
    }
  }

  return arr;
}
```

### 稳定版本（通用）
javascript

```
function countingSort(arr) {
  if (arr.length <= 1) return arr;

  const max = Math.max(...arr);
  const min = Math.min(...arr);
  const range = max - min + 1;
  const count = new Array(range).fill(0);
  const output = new Array(arr.length);

  // 1. 统计每个值的出现次数（偏移 min）
  for (const val of arr) count[val - min]++;

  // 2. 前缀和：count[i] = 值 <= i+min 的元素个数
  for (let i = 1; i < range; i++) count[i] += count[i - 1];

  // 3. 从后向前遍历，保证稳定性
  for (let i = arr.length - 1; i >= 0; i--) {
    const val = arr[i];
    output[count[val - min] - 1] = val;
    count[val - min]--;
  }

  // 4. 复制回原数组
  for (let i = 0; i < arr.length; i++) arr[i] = output[i];

  return arr;
}
```

### 处理负数

注意稳定版本中用了 `val - min` 做偏移。如果数组包含负数（例如 `[-3, -1, 0, 2]`），`min = -3`，偏移后所有值变为非负：`[0, 2, 3, 5]`。

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 所有情况 | O(n + k) | O(n + k) |

其中 `k` 是值域范围（`max - min + 1`）。

**什么时候用计数排序？** 当 `k` 和 `n` 同一量级或 `k < n` 时，计数排序是 O(n) 的，远优于比较排序。但如果 `k >> n`（比如排序 100 个值域在 0-10⁹ 的数），计数数组会极大，完全不适用。

**稳定性**：**稳定**（稳定版本，从后向前遍历时保持了原始顺序）。

## 深入理解

- 计数排序不基于比较，因此能突破 O(n log n) 的下界
- 核心限制是**值域**：值域太大时空间爆炸，不适用
- 计数排序是**基数排序的子过程**——基数排序对每一位用计数排序
- 前缀和 + 从后向前遍历是实现稳定性的关键技巧，这个思路在很多算法中都有应用

## LeetCode 练习

- [LC 912. 排序数组](https://leetcode.cn/problems/sort-an-array/) — 值域适中时可用计数排序
- [LC 75. 颜色分类](https://leetcode.cn/problems/sort-colors/) — 值域只有 {0, 1, 2}，天然适合计数排序
- [LC 274. H 指数](https://leetcode.cn/problems/h-index/) — 计数排序思想的应用