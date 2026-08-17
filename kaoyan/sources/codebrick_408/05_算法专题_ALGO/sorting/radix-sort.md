---
title: 基数排序
source: https://www.codebrick.tech/algo-blog/posts/sorting/radix-sort.html
---

# 基数排序

## 场景引入

如果要对一组手机号码排序，每个号码 11 位。用比较排序需要 O(n log n) 次比较，每次比较两个 11 位字符串。

换个思路：先按最后一位数字排序，再按倒数第二位排序……依次到第一位。每轮排序只需要把数字分到 0-9 十个桶里（计数排序），O(n) 搞定。排 11 轮，总时间 O(11n) = O(n)。

这就是基数排序——**按位排序，从低位到高位（或从高位到低位），每一位用稳定的计数排序**。

## 核心思路

基数排序有两种方案：

### LSD（Least Significant Digit）— 从低位到高位

- 从最低位开始，对当前位用**稳定排序**（计数排序）
- 逐位向高位推进
- 处理完最高位后，排序完成

**为什么从低位开始？** 因为每轮排序是稳定的——当按第 2 位排序时，第 1 位的顺序被保留。层层叠加，最终所有位都有序。

### MSD（Most Significant Digit）— 从高位到低位

- 先按最高位分桶
- 对每个桶**递归**地按下一位排序
- 类似字典序的排序方式

MSD 适合处理变长字符串（如英文单词），LSD 适合处理等长数据（如固定位数的整数）。

## 算法流程图（LSD）

## 代码实现

### LSD 基数排序（整数）
javascript

```
function radixSort(arr) {
  if (arr.length <= 1) return arr;

  const max = Math.max(...arr);

  // 从个位开始，逐位排序
  for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {
    countingSortByDigit(arr, exp);
  }

  return arr;
}

function countingSortByDigit(arr, exp) {
  const n = arr.length;
  const output = new Array(n);
  const count = new Array(10).fill(0);

  // 统计当前位的数字分布
  for (let i = 0; i < n; i++) {
    const digit = Math.floor(arr[i] / exp) % 10;
    count[digit]++;
  }

  // 前缀和
  for (let i = 1; i < 10; i++) {
    count[i] += count[i - 1];
  }

  // 从后向前遍历，保证稳定性
  for (let i = n - 1; i >= 0; i--) {
    const digit = Math.floor(arr[i] / exp) % 10;
    output[count[digit] - 1] = arr[i];
    count[digit]--;
  }

  // 复制回原数组
  for (let i = 0; i < n; i++) arr[i] = output[i];
}
```

### 处理负数

上面的实现只能处理非负整数。处理负数的常见做法是**分离正负数**，分别排序后合并：javascript

```
function radixSortWithNegative(arr) {
  const negatives = arr.filter(x => x < 0).map(x => -x);
  const positives = arr.filter(x => x >= 0);

  if (negatives.length) radixSort(negatives);
  if (positives.length) radixSort(positives);

  // 负数排序后反转（因为取绝对值后排序，最大的绝对值应该排最前面）
  negatives.reverse();

  let idx = 0;
  for (const val of negatives) arr[idx++] = -val;
  for (const val of positives) arr[idx++] = val;

  return arr;
}
```

## 复杂度分析

|  | 时间复杂度 | 空间复杂度 |
| --- | --- | --- |
| 所有情况 | O(d × (n + k)) | O(n + k) |

- `d` = 最大位数（例如最大值是 999，d = 3）
- `k` = 每一位的值域（十进制下 k = 10）
- 当 `d` 是常数时（如固定位数的整数），时间复杂度为 O(n)

**稳定性**：**稳定**。每轮计数排序都是稳定的，整体也是稳定的。

## 基数排序 vs 比较排序

基数排序看起来是 O(n) 的，比快排的 O(n log n) 更优？不一定：

- 基数排序的 `d` 不是免费的。对 32 位整数排序，`d = 10`（十进制）或 `d = 32`（二进制）
- 基数排序的常数因子大（每轮需要额外数组、前缀和计算等），缓存命中率也不如快排
- 当 n 不够大时，O(n log n) 的快排可能实际更快

**结论**：基数排序适合**数据量大、位数少、值域大**的场景（如大量手机号码、IP 地址排序）。

## 深入理解

- LSD 基数排序依赖每轮排序的**稳定性**——这就是为什么每轮要用计数排序而不是快排
- 基数不一定是 10。用基数 256 可以按字节排序，减少轮数；用基数 2 就是按位排序
- 基数排序是**多关键字排序**的通用思路：先按次要关键字排序，再按主要关键字排序（稳定排序保证次要关键字的顺序被保留）
- 数据库的复合索引排序本质上就是多关键字排序的思想

## LeetCode 练习

- [LC 912. 排序数组](https://leetcode.cn/problems/sort-an-array/) — 基数排序实现
- [LC 164. 最大间距](https://leetcode.cn/problems/maximum-gap/) — 可用基数排序做到 O(n)
- [LC 179. 最大数](https://leetcode.cn/problems/largest-number/) — 自定义排序规则，理解多关键字排序