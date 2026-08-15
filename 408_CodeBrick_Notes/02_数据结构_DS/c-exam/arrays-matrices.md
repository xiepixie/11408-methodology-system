---
title: 数组、下标与二维矩阵
source: https://www.codebrick.tech/ds-full/posts/c-exam/arrays-matrices.html
---

# 数组、下标与二维矩阵

数组是历年代码题出现最多的语法载体。2010、2011、2013、2016、2018、2020、2025 直接以一维数组为主，2021、2023、2024 又把二维数组放进图结构体里。

数组题真正考的不是声明数组，而是三件事：**有效区间、多个下标各自的含义、写入是否越界。**

## 数组参数不包含长度
c

```
int solve(int A[], int n)
```

进入函数后，`A` 提供首元素位置，但 C 不会自动告诉函数数组有多长。因此题面通常另给 `n`。不要尝试在函数里用 `sizeof(A) / sizeof(A[0])` 求长度；参数位置的 `A` 已按指针传递，这个公式不会得到原数组长度。

卷面默认有效下标：text

```
0, 1, 2, ..., n-1
```

对应的标准扫描是：c

```
for (int i = 0; i < n; i++) {
    /* 使用 A[i] */
}
```

## 先写清区间是闭还是开

2010·42 的三次逆置通常使用闭区间 `A[low..high]`：c

```
void reverse(int A[], int low, int high) {
    while (low < high) {
        int temp = A[low];
        A[low] = A[high];
        A[high] = temp;
        low++;
        high--;
    }
}
```

若左移 `p` 位，三个闭区间分别是：c

```
reverse(A, 0, p - 1);
reverse(A, p, n - 1);
reverse(A, 0, n - 1);
```

把 `p` 和 `p-1` 混用，算法思想完全正确也会在边界上失分。

## 多下标：每个下标只能有一个职责

2020·41 同时扫描三个升序数组：c

```
int i = 0, j = 0, k = 0;

while (i < n1 && j < n2 && k < n3) {
    int a = A[i], b = B[j], c = C[k];
    /* 计算当前三元组；让最小值对应的下标前进 */
}
```

这里 `i` 永远属于 A，`j` 永远属于 B，`k` 永远属于 C。不要为了少声明一个变量而复用下标；408 卷面更看重可判读性。

双层循环同样要区分职责：c

```
for (int i = 0; i < n; i++) {          /* 枚举候选 */
    int count = 0;
    for (int j = 0; j < n; j++)         /* 统计候选出现次数 */
        if (A[j] == A[i]) count++;
}
```

## 反向扫描：把“后缀”变成已知信息

题目出现“从 i 到 n-1”“后缀最大值”时，经常从右向左写：c

```
int curMax = A[n - 1];
int curMin = A[n - 1];

for (int i = n - 2; i >= 0; i--) {
    if (A[i] > curMax) curMax = A[i];
    if (A[i] < curMin) curMin = A[i];
    /* 利用当前后缀状态计算答案 */
}
```

2025·41 就是这个骨架。初始化放在 `A[n-1]`，循环从 `n-2` 开始，避免最后一个元素被重复或漏算。

注意这里同时维护了 `curMax` 和 `curMin`：因为 2025 求的是乘积，`A[i]` 为负时，乘后缀里绝对值最大的负数（`curMin`）反而更大——负负得正。只留 `curMax` 会漏掉这种情况，正好丢掉阅卷单列的那一分。什么时候要连最小值一起留，取决于后续运算是否会让"小值翻大"。

## 值作下标：先检查范围，再访问

2015·41 和 2018·41 都把有限值域映射到标记数组：c

```
if (A[i] >= 1 && A[i] <= n) {
    mark[A[i]] = 1;
}
```

顺序不能反。若先写 `mark[A[i]]` 再检查，负数和大数已经造成越界。看到“值作为下标”，立即问：

- 最小合法值是多少？
- 最大合法值是多少？
- 辅助数组需要开多长？

## 二维数组：先认行列，再写双循环

图题常给：c

```
typedef struct {
    int numVertices, numEdges;
    char VerticesList[MAXV];
    int Edge[MAXV][MAXV];
} MGraph;
```

若 `Edge[i][j] != 0` 表示有边 `i -> j`：

- 固定 `i` 扫第 i 行，统计顶点 i 的出度；
- 固定 `j` 扫第 j 列，统计顶点 j 的入度。c

```
int out = 0, in = 0;
for (int j = 0; j < n; j++) {
    if (G.Edge[i][j] != 0) out++;
    if (G.Edge[j][i] != 0) in++;
}
```

2021·41 是无向图，矩阵一行之和就是顶点度数；2023·41 是有向图，行列不能混；2024·41 先按列统计所有入度，再逐步更新。

## 辅助数组必须初始化

固定上限数组可直接清零：c

```
int inDegree[MAXV] = {0};
```

动态长度数组则使用 `calloc`，详见[动态内存、字符与输出](./memory-io.html)。不要写：c

```
int inDegree[MAXV];   /* 随后直接 ++，错误：初值未知 */
```

## 立即写：闭区间原地逆置

只补完 `reverse`。默认输入要求把下标 1 到 5 的部分逆置，正确输出为 `10 60 50 40 30 20 70`。

写完后修改标准输入，测试 `low == high` 和整个数组逆置。

## 立即写：邻接矩阵出入度

近四年图题连考，卷面重心就是这个动作。补完 `degreeOf`：扫第 `v` 行累加出度，扫第 `v` 列累加入度。默认输入查顶点 0，正确输出为 `out=2 in=1`。

写完盯住一件事：出度扫的是 `Edge[v][j]`（行固定），入度扫的是 `Edge[j][v]`（列固定），行列一旦写反，有向图立刻算错。

## 对应真题练习

- [2010·42 数组循环左移](https://www.codebrick.tech/oj/problems/ds-2010-42-cyclic-left-shift)：闭区间、辅助函数。
- [2013·41 主元素](https://www.codebrick.tech/oj/problems/ds-2013-41-majority-element)：状态变量与两次扫描。
- [2018·41 最小未出现正整数](https://www.codebrick.tech/oj/problems/ds-2018-41-min-missing-positive)：值作下标与范围过滤。
- [2020·41 三元组最小距离](https://www.codebrick.tech/oj/problems/ds-2020-41-min-triple-distance)：三个数组、三个下标。
- [2023·41 有向图 K 顶点](https://www.codebrick.tech/oj/problems/ds-2023-41-graph-k-vertices)：邻接矩阵行列。
- [2025·41 后缀最大乘积](https://www.codebrick.tech/oj/problems/ds-2025-41-reverse-scan-mulmax)：反向扫描。

## 本篇卷面检查

- 有效下标到底是 `0..n-1` 还是题面另有约定？
- 区间端点是包含还是不包含？
- 每个下标变量属于哪个数组？
- 反向循环是否会访问 `A[-1]`？
- 用值访问辅助数组前是否先检查范围？
- 邻接矩阵的行列方向是否符合题面定义？

下一篇：[结构体、指针与链式结点](./structs-pointers.html)。