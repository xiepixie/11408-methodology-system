---
title: 桶排序
source: https://www.codebrick.tech/algo-blog/posts/sorting/bucket-sort.html
---

# 桶排序

## 场景引入

假设要对 100 万个均匀分布在 [0, 1) 之间的浮点数排序。用快排需要 O(n log n)，但有更快的方法：把 [0, 1) 分成 1000 个区间（桶），每个数放进对应的桶里，桶内再排序。如果数据均匀分布，每个桶只有约 1000 个元素，桶内排序很快，总时间接近 O(n)。

这就是桶排序的思路——**先按范围分桶，桶内再用其他排序算法**。

## 核心思路

- 根据数据的范围，创建若干个"桶"（每个桶负责一个值域区间）
- 遍历原数组，将每个元素放入对应的桶中
- 对每个桶内部进行排序（通常用插入排序）
- 按桶的顺序依次取出元素，拼接成最终结果

### 关键：分桶策略

桶排序的性能完全取决于数据能否**均匀地分配到各个桶中**：

- **理想情况**：每个桶中元素数量接近 `n/k`（k 为桶数），每个桶内排序时间 O((n/k)²)，总时间 O(n + k × (n/k)²) = O(n + n²/k)。当 `k ≈ n` 时，总时间 O(n)。
- **最坏情况**：所有元素落入同一个桶，退化为 O(n²)（取决于桶内排序算法）。

## 算法流程图

## 代码实现
javascript

```
function bucketSort(arr, bucketCount = 10) {
  if (arr.length <= 1) return arr;

  const min = Math.min(...arr);
  const max = Math.max(...arr);

  if (min === max) return arr; // 所有元素相同

  const range = max - min;
  const buckets = Array.from({ length: bucketCount }, () => []);

  // 分桶
  for (const val of arr) {
    const idx = Math.min(
      Math.floor(((val - min) / range) * bucketCount),
      bucketCount - 1
    );
    buckets[idx].push(val);
  }

  // 桶内排序 + 拼接
  let pos = 0;
  for (const bucket of buckets) {
    // 桶内用插入排序（小数组效率高）
    insertionSort(bucket);
    for (const val of bucket) {
      arr[pos++] = val;
    }
  }

  return arr;
}

function insertionSort(arr) {
  for (let i = 1; i < arr.length; i++) {
    const key = arr[i];
    let j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}
```

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 最好 | O(n + k) — 数据均匀分布 | O(n + k) |
| 平均 | O(n + k) — 数据近似均匀 | O(n + k) |
| 最坏 | O(n²) — 所有元素落入同一桶 | O(n + k) |

**稳定性**：**稳定**（前提是桶内排序算法稳定，如插入排序）。

## 桶排序 vs 计数排序

|  | 计数排序 | 桶排序 |
| --- | --- | --- |
| 适用数据类型 | 整数 | 任意可排序数据（包括浮点数） |
| 空间开销 | O(值域范围) | O(桶数 + n) |
| 桶内处理 | 直接计数 | 需要排序 |
| 核心假设 | 值域不大 | 数据分布均匀 |

计数排序可以看成桶排序的特例——每个桶的范围恰好是 1（即每个值一个桶）。

## 深入理解

- 桶排序的核心不是排序本身，而是**分桶策略**——如何让数据均匀分配
- 数据分布不均时，可以用**自适应分桶**（如按分位数分桶）来改善
- "分桶"的思想在工程中很常见：HashMap 的哈希桶、数据库的分区、负载均衡的分片
- 桶数 `k` 的选择是时间与空间的权衡：桶越多排序越快，但空间越大

## LeetCode 练习

- [LC 912. 排序数组](https://leetcode.cn/problems/sort-an-array/) — 数据均匀时可用桶排序
- [LC 164. 最大间距](https://leetcode.cn/problems/maximum-gap/) — 桶排序思想的经典应用，利用鸽巢原理
- [LC 220. 存在重复元素 III](https://leetcode.cn/problems/contains-duplicate-iii/) — 桶排序思想用于滑动窗口