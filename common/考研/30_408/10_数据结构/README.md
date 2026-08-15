# 数据结构 Subject Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Subject Atlas，Atlas Foundation、12 个 Topic、3 个 internal Bridge、1 个 Integration 均已建立深度正文与发布视图；当前进入真题/陌生题验证阶段。

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

贯穿母例：若任务是持续插入并反复取得/删除最大值，目标操作只要求极值，不要求全序。Heap 用完全二叉树的紧凑表示和父子偏序作为不变量，使 `FindMax = O(1)`，插入与删除极值通过上滤/下滤在 `O(log n)` 内恢复合法状态。具体机制归 DS05；Atlas 只用它说明 `Workload -> Representation -> Invariant -> Cost` 怎样运行。

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

复杂度只是成本坐标之一。同为 `O(n)` 的表示仍可能因 cache locality、指针追踪或外存 I/O 产生不同机器代价；涉及硬件层次时，数据结构只声明自身访问模式与成本向量，真实机器成本调用计组/系统的相应模型。

### 核心分流边界

| 不能混用 | 判据 |
|---|---|
| Logical Structure / Storage Representation | 关系是什么，与机器用数组、指针、矩阵或索引怎样编码，是两层问题 |
| Structure / Algorithm | 结构给出合法状态与不变量；算法给出改变状态并恢复不变量的过程 |
| Heap Order / Total Order | Heap 只保证父子偏序，不保证兄弟或跨子树全序 |
| Average `O(1)` / Worst-case `O(1)` | 平均结论依赖分布、装填或随机性假设；最坏界要求覆盖所有合法输入 |
| Shortest Path / MST | 前者优化指定点间路径；后者优化覆盖全部顶点的连通子图总权重 |
| Stable / In-place | 稳定性检查相等 key 的相对次序；原地性检查额外空间 |
| Asymptotic / Actual Machine Cost | 渐近阶不包含常数、局部性和 I/O 层次；机器代价需调用相应成本模型 |

这些是后续所有 Topic 的分析与度量语言，不是一个独立数据结构机制。

### 代码是机制证据，不是附录装饰

数据结构的核心机制最终必须落实为可执行的状态转移。每个 Topic 的 Canonical 深度正文除定义、推导、图示和例题外，还应包含与核心机制对应的代码；代码必须能反向解释本册的对象、表示、不变量、边界和成本，而不是只展示语言 API。

Topic 的代码交付遵循同一契约：

```text
Operation Contract
-> State Fields
-> Core Transition
-> Invariant Repair
-> Boundary Branches
-> Complexity
-> Executable Tests
```

- Canonical `.tex` 直接讲解并引用关键代码段；
- 同目录 `code/` 保存可编译、可测试的完整实现与最小断言测试，作为正文的伴随实现，不成为第二知识 Owner；
- 默认使用贴近 408 伪代码和指针模型的 C++17；只有专题本身需要语言无关伪代码或另一语言才能表达核心机制时才例外；
- 测试至少覆盖正常主路径、空/单元素等边界、一次失败输入，以及本册声称维护的关键不变量；
- 代码复杂度必须绑定输入契约和基本操作，不能用库函数调用掩盖机制成本。

Bridge 只展示接口所需的最小调用代码，Integration 可以组合已有 Topic 代码；两者都不得复制完整实现。

### 十二个 Topic 的代码覆盖矩阵

下表定义“这一册的机制必须最终在哪些代码上落地”，不是要求把所有教材变体塞进正文。每册至少选择能生成其余变体的核心实现，并用测试覆盖关键不变量。

| Topic | Canonical 代码主干 | 必须验证的状态/边界 |
|---|---|---|
| DS01 线性关系与存储表示 | 顺序表、单/双链表、定位与局部插删 | `length/capacity`、`head/tail`、空表、首尾、非法位置、可达性 |
| DS02 栈队列与受限访问 | 顺序栈、链栈、循环队列、链队列、双端队列核心操作 | 上溢/下溢、队空/队满判据、环形下标、FIFO/LIFO |
| DS03 串与模式匹配 | 朴素匹配、prefix/failure 构造、KMP 主循环 | 空模式、完全/部分匹配、重复前后缀、失配回退不倒退主串 |
| DS04 树与二叉树 | 二叉树构造、递归/迭代遍历、层序、线索化或 Huffman 主干 | 空树、叶子、遍历覆盖、递归返回、编码前缀性 |
| DS05 Heap 与优先队列 | 上滤、下滤、建堆、插入、取极值、删除极值 | 完全树形状、父子偏序、根/叶边界、容量变化 |
| DS06 Union-Find | MakeSet、Find、Union、路径压缩、按秩/大小合并 | 代表元、森林无环、集合划分、重复合并 |
| DS07 图的表示与遍历 | 邻接矩阵/表、DFS、BFS、连通分量扫描 | 有向/无向边、visited 时机、不连通图、重复边/自环题设 |
| DS08 图上的结构算法 | Prim/Kruskal、Dijkstra/Floyd、拓扑排序、关键路径主干 | cut/relax/入度不变量、不可达、负权边适用边界、环 |
| DS09 查找与有序索引 | 折半查找、BST、AVL，B/B+ 树保留核心分裂/合并过程 | 区间边界、重复 key 约定、平衡因子、有序性、根分裂/收缩 |
| DS10 Hash 与直接定位 | 散列、开放定址、链地址、插入/查找/删除 | 负载因子、探测终止、删除标记、满表、冲突统计 |
| DS11 内部排序 | 插入、交换、选择、归并、快速、堆、基数排序核心版本 | 已排序区、partition、稳定性、最坏输入、辅助空间 |
| DS12 外部排序 | 置换选择、败者树、$k$ 路归并与缓冲区模拟 | run 边界、I/O 轮次、输入耗尽、缓冲区与归并终止 |

实现粒度服从 Owner：例如 Heap Sort 在 DS11 只调用 DS05 的 Heap 接口，Kruskal 在 DS08 只调用 DS06 的 Union-Find，不复制完整底层实现。

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
