---
title: 快速排序
source: https://www.codebrick.tech/algo-blog/posts/sorting/quick-sort.html
---

# 快速排序

## 场景引入

如果只能掌握一种排序算法，应该选哪个？答案是**快速排序**。

快速排序是实际应用中最广泛使用的排序算法。C 语言标准库的 `qsort`、C++ 的 `std::sort`（结合插入排序和堆排序的 IntroSort）都以快速排序为核心。它的平均时间复杂度为 O(n log n)，且常数因子小、缓存友好，在大多数场景下都比归并排序和堆排序更快。

## 核心思路

快速排序同样基于**分治思想**，但与归并排序的策略相反：

- **归并排序**：先递归分解，再合并（重点在"合"）
- **快速排序**：先分区处理，再递归（重点在"分"）

### 算法步骤

- **选择基准（Pivot）**：从数组中选一个元素作为基准
- **分区（Partition）**：将数组重新排列，使得基准左边的元素都 <= 基准，右边的都 > 基准
- **递归**：对基准左右两部分分别递归排序

### Partition 函数详解（Lomuto 方案）

Lomuto 分区方案以数组最后一个元素为基准：

- 维护指针 `i`，指向"小于基准区间"的右边界
- 用指针 `j` 从左到右扫描
- 如果 `arr[j] < pivot`，将 `arr[j]` 与 `arr[i]` 交换，`i++`
- 扫描完成后，将 pivot 放到 `i` 的位置

分区结束后，pivot 就在它最终排序后应该在的位置上。

## 算法流程图

## 可视化演示
加载可视化中...

## 代码实现

### 基础版本
javascript

```
function quickSort(arr, lo = 0, hi = arr.length - 1) {
  if (lo >= hi) return arr;

  // Lomuto 分区
  const pivot = arr[hi];
  let i = lo;
  for (let j = lo; j < hi; j++) {
    if (arr[j] < pivot) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
    }
  }
  [arr[i], arr[hi]] = [arr[hi], arr[i]];

  quickSort(arr, lo, i - 1);
  quickSort(arr, i + 1, hi);
  return arr;
}
```

### 优化一：随机选择基准

固定选最后一个元素做基准，当数组已排序时会退化到 O(n²)。随机选基准可以避免：javascript

```
function quickSortRandom(arr, lo = 0, hi = arr.length - 1) {
  if (lo >= hi) return arr;

  // 随机选基准，与最后一个元素交换
  const randIdx = lo + Math.floor(Math.random() * (hi - lo + 1));
  [arr[randIdx], arr[hi]] = [arr[hi], arr[randIdx]];

  const pivot = arr[hi];
  let i = lo;
  for (let j = lo; j < hi; j++) {
    if (arr[j] < pivot) {
      [arr[i], arr[j]] = [arr[j], arr[i]];
      i++;
    }
  }
  [arr[i], arr[hi]] = [arr[hi], arr[i]];

  quickSortRandom(arr, lo, i - 1);
  quickSortRandom(arr, i + 1, hi);
  return arr;
}
```

### 优化二：三路分区

当数组中有大量重复元素时，标准分区效率很低。三路分区将数组分为三部分：`< pivot`、`== pivot`、`> pivot`：javascript

```
function quickSort3Way(arr, lo = 0, hi = arr.length - 1) {
  if (lo >= hi) return arr;

  const pivot = arr[lo];
  let lt = lo;     // arr[lo..lt-1]  < pivot
  let gt = hi;     // arr[gt+1..hi]  > pivot
  let i = lo + 1;  // arr[lt..i-1]  == pivot

  while (i <= gt) {
    if (arr[i] < pivot) {
      [arr[lt], arr[i]] = [arr[i], arr[lt]];
      lt++;
      i++;
    } else if (arr[i] > pivot) {
      [arr[i], arr[gt]] = [arr[gt], arr[i]];
      gt--;
    } else {
      i++;
    }
  }

  quickSort3Way(arr, lo, lt - 1);
  quickSort3Way(arr, gt + 1, hi);
  return arr;
}
```

## 应用：快速选择（Quick Select）

利用 partition 的性质，可以在 O(n) 平均时间内找到第 K 大/小的元素，无需完整排序：javascript

```
function findKthLargest(nums, k) {
  const target = nums.length - k; // 第 k 大 = 排序后下标 n-k

  function quickSelect(lo, hi) {
    const pivot = nums[hi];
    let i = lo;
    for (let j = lo; j < hi; j++) {
      if (nums[j] < pivot) {
        [nums[i], nums[j]] = [nums[j], nums[i]];
        i++;
      }
    }
    [nums[i], nums[hi]] = [nums[hi], nums[i]];

    if (i === target) return nums[i];
    if (i < target) return quickSelect(i + 1, hi);
    return quickSelect(lo, i - 1);
  }

  return quickSelect(0, nums.length - 1);
}
```

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 最好 | O(n log n) — 每次均匀分区 | O(log n) 递归栈 |
| 平均 | O(n log n) | O(log n) |
| 最坏 | O(n²) — 每次分区极端不均（已排序+固定基准） | O(n) 递归栈 |

**稳定性**：**不稳定**。分区过程中元素交换会改变相等元素的相对顺序。

### 递归树与最坏情况退化

快速排序的性能取决于分区是否均匀。用递归树来直观理解：

**理想情况：每次均匀分区**

```
          partition(0,7)        → 扫描 n 个元素
          /            \
    sort(0,3)      sort(4,7)    → 各扫描 n/2
     /    \          /    \
  (0,1) (2,3)    (4,5) (6,7)   → 各扫描 n/4
```

树高 = `log₂(n)`，每层总扫描 n 个元素 → 时间 O(n log n)，递归栈深度 O(log n)。

**最坏情况：已排序 + 固定选末尾做 pivot**

```
  partition(0,7)                → 扫描 n 个元素
  |            \
  sort(0,6)    (7)              → 扫描 n-1
  |        \
  sort(0,5) (6)                 → 扫描 n-2
  |      \
  ...                           → ...
```

树退化成一条链！高度 = n，每层扫描递减 → 时间 O(n²)，递归栈深度 O(n)。

**即使不那么极端**（比如每次 9:1 分区），时间复杂度仍然是 O(n log n)：

```
T(n) = T(n/10) + T(9n/10) + n
```

递归树虽然不平衡，但总层数仍为 O(log n)，每层总工作量仍为 O(n)。

### 实测：观察数据分布对快排的影响
数组大小502001,0005,00010,000数据分布随机已排序逆序基本有序 点击「运行测试」，在你的浏览器中实时运行排序算法，统计比较和交换次数。

切换「已排序」试试——比较次数和交换次数会急剧增加（使用的是固定末尾 pivot 的基础版本）。这就是为什么实际工程中必须用**随机化 pivot**。

**为什么快速排序实际上比归并排序快？**

- **缓存友好**：快排在原数组上操作，内存访问连续；归并需要额外数组，缓存命中率低
- **常数因子小**：分区操作比 merge 操作简单
- **尾递归优化**：可以对较短的分区使用尾递归，减少栈深度

## 深入理解

- partition 函数是快速排序的核心，理解它就理解了整个算法
- 最坏情况 O(n²) 的根因是分区不均，随机化 pivot 可以有效避免
- 三路分区解决重复元素问题（LC 75 颜色分类就是三路分区的应用）
- Quick Select 是快排思想的延伸——不需要完整排序就能找到第 K 大元素

## LeetCode 练习

- [LC 912. 排序数组](https://leetcode.cn/problems/sort-an-array/) — 快排标准实现（注意随机化，否则会超时）
- [LC 215. 数组中的第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) — Quick Select 经典应用
- [LC 75. 颜色分类](https://leetcode.cn/problems/sort-colors/) — 三路分区的直接应用
- [LC 347. 前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) — 可用 Quick Select 求解