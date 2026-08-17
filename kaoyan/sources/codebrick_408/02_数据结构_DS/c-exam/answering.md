---
title: 卷面答题模板与 18 题训练路线
source: https://www.codebrick.tech/ds-full/posts/c-exam/answering.html
---

# 卷面答题模板与 18 题训练路线

代码题不是只判最终代码。历年题面通常要求“设计思想—程序实现—复杂度”，**官方评分也就是这三档**。本文在前面多加一个「约定」，指的是动笔前的审题动作，它本身不单独占分，作用是让后面思想、代码、复杂度三段都不因看错题而失分。所以最稳的答题顺序是：**约定（审题）→ 思想 → 代码 → 复杂度。**

## 动笔前先圈四类信息

- **输入是什么**：数组、带头链表、树根还是图结构体？
- **输出是什么**：返回值、打印、输出数组还是修改原结构？
- **硬约束是什么**：不改变原结构、空间 `O(1)`、尽可能高效？
- **特殊约定是什么**：下标起点、空结点标记、边的方向、是否可能无解？

这些信息决定 C 写法。算法想对但违反“不修改链表”，仍然会失去关键正确性分。

## 第一段：设计思想写成可执行步骤

不要只写“使用双指针法”。至少交代初始化、推进和结束：

令 fast、slow 均指向首个数据结点。先令 fast 前进 k 步；若途中到达 NULL，则链表长度不足。随后两指针同步前进，直到 fast 为 NULL，此时 slow 指向倒数第 k 个结点。

这段文字即使代码出现局部笔误，也能让阅卷人识别你的主体方法。

## 第二段：代码只写题目要求的函数

通用骨架：c

```
ReturnType solve(Parameters) {
    /* ① 边界与初始化 */

    /* ② 主体循环或递归 */

    /* ③ 返回、输出或收尾 */
}
```

卷面代码应做到：

- 函数签名照抄；
- 关键变量初始化；
- 关键步骤有简短注释；
- 不补 `main`、输入、建表等测试壳；
- 不混写 C 与 C++，例如一边 `malloc` 一边 `new`。

## 第三段：复杂度必须与代码一致
text

```
时间 O(n)：每个结点至多访问常数次。
空间 O(1)：只使用常数个指针变量。
```

不要只有结论，要给一句依据。递归题写空间时记得调用栈 `O(h)`；邻接矩阵完整扫描通常为 `O(n²)`；题目提供的输出数组不计辅助空间。

若只写出了正确的朴素算法，就诚实分析它的复杂度。把双重循环谎报成 `O(n)` 会同时损伤代码可信度和复杂度得分。

还要知道一条阅卷规则：**正确性分和最优性分是分开给的。** 2013 主元素、2016 集合划分、2025 后缀最大乘积等多道题，都设了独立的「最优性」得分点。想不到最优解时，先把正确的朴素解写完整、复杂度如实标注，正确性分照样拿；**千万别因为“不是最优”就把整题留空。**

## 七类高频卷面骨架

### 一次扫描维护状态
c

```
State state = initial;
for (int i = 0; i < n; i++) {
    update(state, A[i]);
}
return answer(state);
```

对应：2013 主元素、2025 后缀最大乘积。

### 多指针同步推进
c

```
while (allPointersValid) {
    inspectCurrentValues();
    moveOneOrMorePointers();
}
```

对应：2009、2012、2019、2020。

### 值域标记
c

```
mark = calloc(range, sizeof(char));
for (...) if (valueInRange) mark[value] = 1;
/* 查询 mark */
free(mark);
```

对应：2015、2018。

### 原地区间操作
c

```
while (low < high) {
    swap(A[low], A[high]);
    low++;
    high--;
}
```

对应：2010、2016、2019。

### 树递归
c

```
if (root == NULL) return identity;
if (isTarget(root)) return contribution(root);
return combine(solve(root->left), solve(root->right));
```

对应：2014、2017、2022。

### 邻接矩阵双循环
c

```
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        if (G.Edge[i][j] != 0) process(i, j);
```

对应：2021、2023、2024。

### BST 单路径下降
c

```
while (cur != NULL) {
    updateCandidate(cur);
    cur = key < cur->data ? cur->left : cur->right;
}
```

对应：2026。

## 18 题训练顺序

不要机械按年份刷。按语法难度分四轮：

### 第一轮：先把数组与控制流写顺

- [2010·42 数组循环左移](https://www.codebrick.tech/oj/problems/ds-2010-42-cyclic-left-shift)
- [2013·41 主元素](https://www.codebrick.tech/oj/problems/ds-2013-41-majority-element)
- [2018·41 最小未出现正整数](https://www.codebrick.tech/oj/problems/ds-2018-41-min-missing-positive)
- [2025·41 后缀最大乘积](https://www.codebrick.tech/oj/problems/ds-2025-41-reverse-scan-mulmax)
- [2020·41 三元组最小距离](https://www.codebrick.tech/oj/problems/ds-2020-41-min-triple-distance)

### 第二轮：攻克结点指针

- [2009·42 倒数第 k 个结点](https://www.codebrick.tech/oj/problems/ds-2009-42-find-kth-from-tail)
- [2012·42 两链表共同后缀](https://www.codebrick.tech/oj/problems/ds-2012-42-list-common-suffix)
- [2015·41 链表去重](https://www.codebrick.tech/oj/problems/ds-2015-41-list-dedup-by-abs)
- [2019·41 链表重排](https://www.codebrick.tech/oj/problems/p2313-reorder-list)

### 第三轮：递归与树

- [2014·41 二叉树 WPL](https://www.codebrick.tech/oj/problems/ds-2014-41-binary-tree-wpl)
- [2017·41 表达式树转中缀](https://www.codebrick.tech/oj/problems/ds-2017-41-expr-tree-to-infix)
- [2022·41 顺序存储判 BST](https://www.codebrick.tech/oj/problems/ds-2022-41-bst-validate-array)
- [2026·41 BST 最近关键字](https://www.codebrick.tech/oj/problems/ds-2026-41-bst-closest-key)

### 第四轮：矩阵与综合控制

- [2021·41 EL 路径](https://www.codebrick.tech/oj/problems/ds-2021-41-graph-euler-path)
- [2023·41 有向图 K 顶点](https://www.codebrick.tech/oj/problems/ds-2023-41-graph-k-vertices)
- [2024·41 拓扑序唯一性](https://www.codebrick.tech/oj/problems/ds-2024-41-topo-uniqueness)
- [2011·42 两升序序列中位数](https://www.codebrick.tech/oj/problems/ds-2011-42-median-of-two-sorted)
- [2016·43 集合划分](https://www.codebrick.tech/oj/problems/ds-2016-43-set-partition-max-diff)

最后两题 C 语法并不新，但算法边界较密，适合放在最后检验“思想能否稳定落成代码”。

## Playground 与 OJ 各自怎么用

- 文章内 Playground：只练一个语法动作，可以立即改函数、编译、看输出。
- 真题 OJ：完整提交并由测试数据检查边界。
- 正式卷面：先写思想，再写题目指定函数，不写测试壳。

推荐闭环：**看模板 → Playground 补 5～15 行 → 关闭文章手写一遍 → OJ 完整提交。**只在编辑器里修改到通过，不等于考场上能独立写出。

## 30 秒终检表

- [ ] 函数签名和返回约定未擅自修改。
- [ ] 数组端点、链表头结点、空树标记与题面一致。
- [ ] 所有变量在第一次读取前已初始化。
- [ ] `NULL` 判定发生在 `->` 解引用之前。
- [ ] 删除或逆置结点前保存了后继。
- [ ] 循环每轮都向结束条件推进。
- [ ] 输出、返回、修改原结构三者没有混淆。
- [ ] 时间和空间复杂度与实际代码一致。
- [ ] 关键位置有注释，但没有抄写无关 `main`。

回到[专题总览](./index.html)，或进入[现有真题解析专题](./../exams/brute-to-optimal.html)逐题复盘算法。