# 数据结构 Subject Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Subject Atlas，Atlas Foundation、12 个 Topic、3 个 internal Bridge、1 个 Integration 已锁定，下游深度 Handbook 按册建设。

## 1. 学科母问题

数据结构研究：面对某种数据关系与 workload，怎样选择表示并维护必要不变量，使关键操作以可接受的代价完成。

```text
Workload
-> Logical Relation
-> Required Operations
-> Representation
-> Invariant
-> Algorithm
-> Cost Vector
```

不存在脱离 workload 的“最好数据结构”。

## 2. Atlas Foundation

以下内容由 Atlas Own，不再建立独立“算法复杂度 Topic”：

- input size 与 basic operation；
- time / space complexity；
- asymptotic comparison；
- worst / average cost；
- operation cost vector；
- Logical Relation ≠ Representation；
- Workload first；
- Invariant before code；
- Boundary 是合法状态集合的一部分。

这些是后续所有 Topic 的分析与度量语言，不是一个独立数据结构机制。

## 3. 12 个 Topic

| ID | Topic | 母问题 |
|---|---|---|
| DS01 | [线性关系与存储表示](01_线性关系与存储表示/README.md) | 同一线性关系为什么需要连续与链接等不同物理表示？ |
| DS02 | [栈、队列与受限访问](02_栈队列与受限访问/README.md) | 限制访问位置为什么能够编码过程的时间秩序？ |
| DS03 | [串与模式匹配](03_串与模式匹配/README.md) | mismatch 后怎样复用已经得到的匹配信息？ |
| DS04 | [树与二叉树](04_树与二叉树/README.md) | 层次关系怎样被递归表示、遍历和重组？ |
| DS05 | [Heap 与优先队列](05_Heap与优先队列/README.md) | 怎样不维护完全有序，却始终高效取得极值？ |
| DS06 | [Union-Find 与集合划分](06_UnionFind与集合划分/README.md) | 怎样动态维护“哪些元素属于同一集合”？ |
| DS07 | [图的表示与遍历](07_图的表示与遍历/README.md) | 任意关系怎样编码，并确保目标节点被系统访问？ |
| DS08 | [图上的结构算法](08_图上的结构算法/README.md) | 怎样在图上维护连通、路径、代价和偏序不变量？ |
| DS09 | [查找与有序索引](09_查找与有序索引/README.md) | 愿意预先维护多少有序结构，可以换取多少查询能力？ |
| DS10 | [Hash 与直接定位](10_Hash与直接定位/README.md) | 怎样用空间和冲突管理把搜索逼近直接访问？ |
| DS11 | [内部排序](11_内部排序/README.md) | 怎样通过局部操作逐步制造全局有序？ |
| DS12 | [外部排序](12_外部排序/README.md) | 当真正昂贵的是块 I/O 时，算法应该怎样改变？ |

Huffman 留在 Tree Topic 作为树构造/编码应用；Heap 与 Union-Find 各自拥有独立母问题，不再并入“编码、集合与优先级”。

## 4. Internal Bridge

- [DS-B01 Frontier Traversal](50_科内桥梁/DS-B01_FrontierTraversal/README.md)
- [DS-B02 Index Strategy × Workload](50_科内桥梁/DS-B02_IndexStrategy与Workload/README.md)
- [DS-B03 Heap / Union-Find × Graph Algorithm](50_科内桥梁/DS-B03_辅助结构与图算法/README.md)

Bridge 只解释接口；Tree/Graph/Heap/Union-Find 本体仍由各 Topic Own。

## 5. Integration

- [DS-I01｜从 Workload 到数据结构选择](60_综合专题/DS-I01_从Workload到数据结构选择/README.md)

```text
Workload
-> Required Operations
-> Candidate Structures
-> Invariants
-> Cost Vector
-> Choice
```

## 6. Control Adapter

```text
Relation
-> Workload
-> Representation
-> Operation
-> Invariant
-> Boundary
-> Cost
```

Rules：[数据结构做题规则](90_做题规则/README.md)。
