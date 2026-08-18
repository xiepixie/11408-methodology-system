# 数据结构 CodeBrick 全量 Source Diff v1

日期：2026-08-15  
类型：Source Diff / Import Evidence  
来源：[../../../../sources/codebrick_408/02_数据结构_DS](../../../../sources/codebrick_408/02_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84_DS)

## 1. 盘点事实

外部目录实际包含 130 篇专题/题目 Markdown，另有 1 篇学科导航文件，共 131 个 Markdown 文件。外部总索引写作“130 篇”，与文件系统统计相差 1；差异来自导航文件是否计入，暂不修改外部来源。

| 模块 | 文件数 | 主要内容 | 首要去向 |
|---|---:|---|---|
| `intro` | 2 | 数据结构基本概念、算法评价、复杂度与算法特性 | DS Atlas Foundation |
| `linear` | 7 | 线性表、顺序表、单/双/循环/静态链表、链表通用技法 | DS01 |
| `stack-queue` | 13 | 栈、队列、循环队列、双端队列、共享栈、表达式、递归、数组压缩 | DS02；数组表示补入 DS01；frontier 接 DS-B01 |
| `string` | 4 | 串、BF、KMP、全文搜索扩展 | DS03；全文搜索保留 Extension |
| `tree` | 15 | 树、二叉树、遍历、构造、线索、Huffman、BST、AVL、红黑树、堆、并查集 | DS04；Heap→DS05；Union-Find→DS06；有序树→DS09 |
| `graph` | 14 | 图概念、矩阵/邻接表、DFS/BFS、无权最短路、MST、最短路、拓扑、关键路径、DAG | DS07；目标算法→DS08 |
| `search` | 9 | 顺序/分块/折半查找、BST/B/B+、Hash 两种冲突策略 | DS09；Hash→DS10 |
| `sorting` | 14 | 插入/折半插入/Shell、冒泡、选择、归并、快排、堆排、计数、基数、外排、中间状态 | DS11；外排→DS12；堆排使用 DS05 |
| `c-exam` | 7 | 408 C 语言代码题的语法、指针、下标、递归、答题模板 | DS Rules / Exam Control；不新建机制 Topic |
| `exams` | 45 | 2009--2026 真题、算法拓展题、暴力到最优路径 | Evidence / 题目资产；按 Owner 反向验证 |

## 2. 现有 Owner 对照

当前 DS Canonical 结构已经能够承接外部主体知识；本轮把此前粒度不足的 DS04--DS06、DS09--DS12 逐算法定义、状态轨迹、公式口径和边界分支补入正文。外部材料不能成为第二个知识 Owner。

| 外部知识簇 | Canonical Owner | 吸收方式 |
|---|---|---|
| 数据结构三要素、算法五特性、复杂度、基本操作 | `10_数据结构/README.md` | 补 Foundation 的生成性解释与成本口径 |
| 线性表、数组地址、链表变体与指针题 | DS01 | 增加表示恒等式、操作分支、数组/矩阵压缩、静态链表和链表题策略 |
| 栈/队列容器与表达式、递归调用栈 | DS02 | 增加 ADT、端点约定、优先级、递归帧与题面转换；frontier 只通过 DS-B01 调用 |
| 串与 BF/KMP | DS03 | 保留现有 prefix 模型，补 `next` 口径互译与全文搜索边界 |
| 树/森林/二叉树/线索/Huffman | DS04 | 增加术语、转换、构造、遍历与编码不变量 |
| Heap | DS05 | 增加数组判堆、Sift Down、建堆、堆排/优先队列边界 |
| Union-Find | DS06 | 增加朴素最坏形状、动态连通和路径压缩势能解释 |
| 图表示与覆盖 | DS07 | 增加图分类、边计数、邻接表/矩阵选择、BFS 最短路、DAG 表达式 |
| MST、最短路、拓扑、关键路径 | DS08 | 保留统一候选域骨架，补逐算法可手算轨迹、判定条件和失败分支 |
| 顺序/分块/折半/BST/AVL/RB/B/B+ | DS09 | 增加查找成功/失败 ASL、平衡修复、外存扇出和叶层顺序 |
| Hash 链地址/开放定址 | DS10 | 增加散列函数、装填因子、墓碑、探测终止和成功/失败成本 |
| 内部排序与状态识别 | DS11 | 增加每趟提交的可观察证据、稳定性/原地性/复杂度对照 |
| 外部排序 | DS12 | 增加初始段、归并趟数、败者树、缓冲与 I/O 计算口径 |
| C 语言代码题模板 | DS Rules / Exam Control | 只吸收可执行控制动作，不把语言语法变成 Topic 机制 |
| 历年真题与拓展题 | `80_evidence` / 后续题目资产 | 作为模型验证集，不能直接改写成稳定结论 |

## 3. 需要特别保留的边界

- `tree/heap.md` 与 `tree/union-find.md` 分别是 DS05、DS06 的 Source，不改变 DS04 的 Owner。
- `search/bst.md`、`avl.md`、`rbt.md`、`b-tree.md`、`b-plus-tree.md` 都归 DS09；DS09 需要补齐比较维度，但不创建多个平行 Topic。
- `sorting/heap-sort.md` 只能调用 DS05 的 Heap 契约；排序过程仍由 DS11 Own。
- `stack-queue/array-*` 的地址映射和特殊矩阵压缩进入 DS01 的表示层；栈/队列目录只是外部来源路径。
- `c-exam` 的答题动作进入 Rules/Exam Control；它不能反向拥有结构定义。
- `exams` 中的真题结论只作为 Evidence。除非多个独立题面暴露稳定机制缺口，否则不把单题技巧写进 Canonical Handbook。
- `string/full-text-search.md`、Trie、LRU/LFU、DP、回溯、复杂图拓展等不是当前 DS12 Topic 的自动新增项；先保留为 Extension / Source，等待考纲与重复调用证据。

## 4. 本轮 Canonical Update 顺序

1. DS01：线性表示、数组/特殊矩阵、链表变体与 Locate/Update 成本。
2. DS02：受限访问 ADT、出栈序列、循环状态、表达式和递归调用栈。
3. DS03：BF/`next` 口径互译、完整失败轨迹与全文搜索边界。
4. DS04--DS06：树族、Heap、Union-Find 的逐算法细节和反例。
5. DS07--DS08：图表示、BFS 最短路、DAG、MST/最短路/关键路径全轨迹。
6. DS09--DS12：查找索引、Hash、排序状态与外存 I/O 口径。
7. DS Rules：从 `c-exam` 和 45 篇题目证据中提炼可验证动作，不提前宣称已采用。

当前记录只证明 Source 已被定位并分流，不证明所有模型已经通过陌生题验证。每次正文扩充后必须重新发布受影响 `.tex`，并运行 `progress --write`、`check`、`audit`。

## 5. 本轮执行结果（2026-08-15）

本轮已完成一轮 Canonical 增量吸收，未删除原有正文：

| Owner | 本轮新增的外部细节 | 发布状态 |
|---|---|---|
| DS01 | 数组/矩阵地址与压缩口径、线性表/链表变体、链表位置算法 | 已重发并通过编译 |
| DS02 | 合法出栈序列、双端队列方向、共享栈、表达式转换、递归栈 | 已发布 |
| DS03 | 串 ADT、BF 双指针回退、全文检索边界 | 已发布 |
| DS04 | 术语/计数不变量、存储表示、遍历迭代模板、序列构造边界、森林转换、线索头结点、Huffman 前缀码与最优性 | 已重发并通过编译 |
| DS05 | 堆三重不变量、0/1 基下标、Sift Down 选择证明、建堆线性证明、改键/任意删除、Top-k、优先队列/堆排边界 | 已重发并通过编译 |
| DS06 | 朴素链、按秩/大小合并、负号存 size、路径压缩、$\alpha(n)$ 复杂度、动态连通边界 | 已重发并通过编译 |
| DS07 | 图计数与连通性、矩阵路径计数、二部图染色、BFS 距离/路径数、DFS 三色环判定、实现边界 | 已重发并通过编译 |
| DS08 | MST 并列/非连通与唯一性、Dijkstra 初始化/过期项、Floyd 路径恢复、拓扑 tie-break/环证据、DAG 表达式、关键路径四时间量与压缩工期 | 已重发并通过编译 |
| DS09 | ASL/判定树、顺序/折半/分块边界、AVL Fibonacci 高度、RB 插入/删除 case、B/B+ 扇出与阶口径 | 已重发并通过编译 |
| DS10 | 哈希函数取值域、链地址/开放定址成本、探测序列、重散列 | 已发布 |
| DS11 | 一趟与稳定性、折半插入、计数排序、LSD/MSD 稳定性、partition 语义、比较下界、状态识别与选型 | 已重发并通过编译 |
| DS12 | 置换选择活动/冻结状态、败者树、记录/缓冲耗尽、最佳归并树、虚段与 I/O 预算 | 已重发并通过编译 |
| DS Rules | C 语言答题合同、数组/指针/递归检查、暴力到最优升级、真题证据路由 | 待验证规则，已写入 Rules |

本轮仍不把 45 篇 `exams` 题解复制进 Handbook；它们继续作为跨 Topic 的验证集。新增正文已通过逐篇 `publish` 编译，下一步是统一完整性检查、代码回归和陌生题抽样验证，再决定哪些待验证规则可以晋升。

## 6. 心智模型有效性结论（当前证据）

### 已支持的部分

1. `Workload -> Logical Relation -> Required Operations -> Representation -> Invariant -> Algorithm -> Cost Vector` 能覆盖外部笔记的主干：线性表/矩阵落在表示与访问成本，栈队列落在受限 frontier，树/图落在关系与覆盖，查找/Hash 落在秩序或映射的预付成本，排序/外排落在进展量与 I/O 成本。
2. `Goal -> Candidate Domain -> Commit Point -> Invariant -> Failure Evidence` 能统一解释 MST、最短路、拓扑和关键路径，并能把“算法名相同但提交时刻不同”的错因显式化。
3. Owner 分层有效地阻止了重复知识：Heap、Union-Find、BST、Hash、外排和 C 语言答题动作各自落到已有 Topic/Rules；历年题保留为验证集而非第二知识库。

### 仍需验证的部分

- 查找 ASL、图的边数/连通性计数、排序中间态和外排最佳归并树，当前已由推导、编译和现有代码回归支持，但仍需要在 45 篇 evidence 题目上完成逐题抽样记录。
- `Rules` 中新增的函数合同、暴力到最优升级和 30 秒终检仍是“待验证”，不能直接写成已采用规则。
- 红黑树删除、B/B+ 树全套插删和败者树手算目前是 Canonical 机制说明，代码证据仍保持最小主干；若后续真题显示这些分支成为稳定缺口，再增加专门测试/实现。

因此当前结论是：心智模型作为骨架有效，扩充方向继续沿“缺失的状态变量、提交条件、边界和成本证明”渐进推进，而不是改成外部笔记的目录镜像。

## 7. 逐文件覆盖索引（非 exams）

以下清单用于证明外部专题文件已经逐文件定位到唯一 Owner；同一行的文件共享同一机制簇，但不表示把它们的题解复制进 Handbook。

| Source 目录 | 文件清单 | Owner |
| -------------- | --------------------------------- | ------------- |
| `intro` | `complexity.md`, `concepts.md` | DS Atlas Foundation |
| `linear` | `circular-linked-list.md`, `concepts.md`, `doubly-linked-list.md`, `linked-list-algorithms.md`, `sequential-list.md`, `singly-linked-list.md`, `static-linked-list.md` | DS01 |
| `stack-queue` | `array-matrix.md`, `array-storage.md`, `bracket-matching.md`, `circular-queue.md`, `concepts.md`, `deque.md`, `expression-eval.md`, `linked-stack.md`, `queue.md`, `recursion.md`, `sequential-stack.md`, `shared-stack.md`, `special-matrix.md` | DS02；数组表示由 DS01 Own |
| `string` | `bf.md`, `concepts.md`, `full-text-search.md`, `kmp.md` | DS03；全文检索为 Extension |
| `tree` | `avl.md`, `bst.md`, `concepts.md`, `construct-binary-tree.md`, `forest-conversion.md`, `general-tree.md`, `heap.md`, `huffman.md`, `inorder.md`, `level-order-traversal.md`, `postorder.md`, `preorder.md`, `rbt.md`, `threaded-binary-tree.md`, `union-find.md` | DS04；Heap→DS05；Union-Find→DS06；有序树→DS09 |
| `graph` | `adjacency-list.md`, `adjacency-matrix.md`, `bfs-shortest.md`, `bfs.md`, `concepts.md`, `critical-path.md`, `cross-list.md`, `dag-expression.md`, `dfs.md`, `dijkstra.md`, `floyd.md`, `kruskal.md`, `prim.md`, `topological-sort.md` | DS07；目标算法→DS08 |
| `search` | `b-plus-tree.md`, `b-tree.md`, `binary-search.md`, `block-search.md`, `comparison.md`, `concepts.md`, `hash-chaining.md`, `hash-open-addressing.md`, `sequential-search.md` | DS09；Hash→DS10 |
| `sorting` | `binary-insertion-sort.md`, `bubble-sort.md`, `comparison.md`, `concepts.md`, `counting-sort.md`, `external-sort.md`, `heap-sort.md`, `identify-state.md`, `insertion-sort.md`, `merge-sort.md`, `quick-sort.md`, `radix-sort.md`, `selection-sort.md`, `shell-sort.md` | DS11；外排→DS12；堆排使用 DS05 |
| `c-exam` | `answering.md`, `arrays-matrices.md`, `functions-control-flow.md`, `index.md`, `memory-io.md`, `recursion-state.md`, `structs-pointers.md` | DS Rules / Exam Control |

## 8. 验证状态与下一步

- 11 个受影响 Canonical `.tex` 已用 `cognitive_system.py publish` 重编译，均无未决引用；DS10 本轮无正文变更。
- 12 个 DS C++ 核心测试继续通过 `-std=c++17 -Wall -Wextra -Werror -pedantic`；新增推导暂不伪装成已经有代码实现的机制。
- 45 篇 `exams` 文件仍只作验证集，下一小步是按 Owner 抽取每个模块 1--2 道陌生题，记录 `Goal/Candidate/Commit/Invariant/Failure` 是否能独立复原。
- Rules 中的函数合同、暴力到最优升级与 30 秒终检仍是 Candidate，不在本日志中晋升为稳定规则。

## 9. 陌生题抽样路由（第一轮）

抽样不把题解搬进 Handbook，而是检查心智模型能否在陌生题面上复原状态变量与停止条件：

| 题目                              | Owner     | Goal            | Candidate / Commit                     | Invariant / Failure                        |
| --------------- | ---------- | ------------ | ------------ | ------------ |
| `2009-42-find-kth-from-tail.md` | DS01      | 找倒数第 $k$ 个结点且只读 | 双指针保持 $k$ 间隔；fast 到尾时提交 slow           | 间隔恒定；先走阶段遇空即 $k>n$                         |
| `2019-41-reorder-list.md`       | DS01      | $O(1)$ 空间重排链表   | 快慢找中点、切断、逆置、交叉合并                       | 每个结点恰一次入新链；奇偶长度与尾指针是失败证据                   |
| `2019-42-circular-queue.md`     | DS02      | 固定空间且可复用槽位      | 环形下标与 size/tag 协议；入队提交 rear、出队提交 front | 空/满状态可区分；模运算不能越界                           |
| `ext-kmp.md`                    | DS03      | 线性时间定位模式匹配      | 前缀函数候选边界；失配回退而不回退主串                    | `matched` 表示已匹配前缀长度；重叠匹配回到 `pi[matched-1]` |
| `2014-41-binary-tree-wpl.md`    | DS04      | 求前缀码 WPL        | 候选为两个最小权；合并后重新进入候选                     | 叶深度加权等于合并累计值；单符号边界代价为 0                    |
| `2022-42-top-k-min.md`          | DS05      | 保留前 $k$ 小       | 大小为 $k$ 的最大堆；新值优于堆顶才替换                 | 堆根是当前第 $k$ 小上界；$k=0$ 与重复值需显式处理             |
| `ext-connected-components.md`   | DS06/DS07 | 统计无向图分量         | 每次从 unseen 顶点启动 frontier；扩展时标记并查集合并    | visited/代表元分区不变量；非连通分量必须外层补齐               |
| `2024-41-topo-uniqueness.md`    | DS08      | 判断拓扑序存在且是否唯一    | 当前零入度集合为候选；候选数大于 1 即不唯一                | 每次删除一层前置约束；输出少于 $V$ 即有环                    |
| `2022-41-verify-bst-array.md`   | DS09      | 验证顺序存储 BST      | 中序 frontier；维护一个 `prev` 并在访问点提交比较      | 严格递增；0 下标孩子公式与 `-1`/越界双空条件                 |
| `ext-count-inversions.md`       | DS11      | 统计逆序对并保持排序      | 归并时右半元素先出则一次累加左侧剩余数                    | 左右半区有序；计数用 `long long` 防溢出                 |
| `sorting/external-sort.md`      | DS12      | 在内存受限下最小化块 I/O  | 初始 runs + $k$ 路候选；败者树提交当前最小记录          | 每路有序且指针单调；记录耗尽与缓冲块耗尽分离                     |

这一轮抽样结果支持两条模型判断：链表/队列/堆/归并题仍可回到 `Workload -> Representation -> Invariant -> Cost`，而图算法/拓扑/Huffman/KMP 的正确性都能用 `Goal -> Candidate -> Commit -> Failure` 复原。尚未对 45 篇 evidence 全量逐题打勾，因此不把“全量真题已验证”写成事实。
