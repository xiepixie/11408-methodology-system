# CodeBrick 算法专题全量 Source Diff v1

日期：2026-08-15  
范围：`../../../../sources/codebrick_408/05_算法专题_ALGO/`，共 66 篇 Markdown、10,151 行。  
排除：按用户要求，未读取 `../../../../sources/codebrick_408/02_数据结构_DS/`。  
任务：以数据结构 Subject Atlas 的 `Workload -> Relation -> Representation -> Invariant -> Algorithm -> Cost Vector` 为骨架，判断外部算法材料应补哪个唯一 Owner，以及现有心智模型是否能生成、校验和反证这些内容。

## 1. 结论级判断

### 1.1 现有心智模型有效，但覆盖层不完整

有效性不是由“能把术语放进目录”证明，而由以下事实证明：

1. **能生成解释**：Hash + Array 的随机集合、Hash + 双链表的 LRU、频率桶 LFU、双堆中位数都能由“API 能力分解 -> 组合状态 -> 同步不变量 -> 成本”推出，而不是靠背题名。
2. **能发现错误泛化**：Top-K 实验的主要瓶颈是顺序读 I/O，JSON 外排实验的主要瓶颈却是解析与比较 CPU；Workload/Cost Vector 能解释结论为何随数据格式和单元素工作量反转。
3. **能阻止错误 Owner**：BFS/DFS、KMP、Heap、Union-Find、排序和 Trie 都有现有结构 Owner；算法笔记中的应用不能借“算法专题”之名复制这些机制。
4. **能提出证明义务**：滑窗必须证明窗口状态可增量维护，双指针必须证明被移动一侧可永久排除，贪心必须证明交换/支配性质，DP 必须证明状态充分且依赖无环。
5. **能识别实现口径污染复杂度**：JavaScript `Array.shift()` 不是常数时间；“原地快排”仍有递归栈；Hash 的 `O(1)` 依赖散列和装填假设；位移、整数域和对象布局都影响材料中的强断言。

但当前 Atlas 主要覆盖“选什么结构、怎样维护结构不变量”，缺少一层独立的**算法设计范式**：怎样组织搜索空间、怎样复用跨状态信息、怎样证明局部淘汰安全、怎样把双重循环压成均摊线性扫描。因此结论不是推翻现有模型，而是保留 12 个 Core Topic，并增加四个具有独立 Mother Question 的算法 Extension Topic。它们不扩张 408 Core Topic 口径，只补齐算法设计层。

### 1.2 拓扑判定与后续晋升

| ID | Handbook 类型 / 关系角色 | Mother Question | 主要 Source |
|---|---|---|---|
| DS-A01 | Topic / Extension | 怎样用边界、顺序与可增量摘要，让一次扫描永久排除候选并复用区间信息？ | prefix/diff/window/two-pointer/matrix |
| DS-A02 | Topic / Extension | 怎样把解空间表示成决策树，并用可撤销状态完整且不重地枚举、可靠剪枝？ | backtrack/* |
| DS-A03 | Topic / Extension | 怎样找到充分状态和无环依赖，使重复子问题只求一次，并证明压缩后的更新顺序仍合法？ | dp/* |
| DS-A04 | Topic / Extension | 在什么结构条件下局部选择可承诺为某个全局最优解的一部分？ | greedy/*，以及区间/跳跃/部分图算法的证明接口 |

`Extension` 只是关系角色，物理类型仍为 Topic。本日志完成后，DS-A01--A04 已建立 Canonical `.tex`、Landing Page、Atlas 路由、Ownership 条目和 Published PDF，故已由 Source Diff 阶段的 Candidate 晋升为稳定 Extension Topic。二分查找、BFS/DFS、单调栈队列、图算法、排序等继续由既有 Owner 拥有，四个新 Topic 只引用它们的接口或抽取算法范式。

## 2. 全量逐文件路由

状态说明：下表保留 Source Diff 当时的路由判定。`Canonical Update` 表示应补唯一 Owner；`Candidate Topic` 表示先进入候选并经物理资产与验证后晋升（DS-A01--A04 现已完成晋升）；`Use` 表示只建立引用；`No Update` 表示材料有效但不应进入稳定 Knowledge；`Correct` 表示吸收前必须修正或条件化。

### 2.1 导航与学习方法（4）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `00_算法专题_ALGO_知识全景导航.md` | Evidence / Use | 保留为 Source 清单；其目录分类不成为 Canonical 拓扑。 |
| `intro/why-algo.md` | No Update / Control | 面试动机、筛选与沟通不属于 Knowledge；可为练习规则提供情境，不写入 Handbook。 |
| `intro/how-to-practice.md` | Candidate Rule | “按框架学习、间隔复测、限时后看提示”属于 Control/Learning；不能把代码模板等同于可迁移心智模型。 |
| `intro/complexity.md` | Atlas Foundation / Correct | 吸收递归树、均摊分析、约束倒推；纠正“大 O=增长趋势”的不精确口径、固定规模阈值的机器依赖、快排空间忽略递归栈等。 |

### 2.2 数组与序列技巧（7）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `array/binary-search.md` | DS09 Canonical Update | 增加 lower/upper boundary、闭/半开区间合同、答案二分；核心不是三套模板，而是单调谓词与不变量。 |
| `array/prefix-sum.md` | DS-A01 Candidate Topic | 吸收哨兵前缀、二维容斥、前缀和 + Hash；补充群/可逆运算边界和溢出。 |
| `array/diff-array.md` | DS-A01 Candidate Topic | 吸收区间端点事件、前缀恢复、半开/闭区间转换；空数组和在线查询是边界。 |
| `array/sliding-window.md` | DS-A01 Candidate Topic | 吸收双边界与增量状态；必须区分固定/可变窗口，并证明收缩条件的方向性，不把所有子数组题都套窗。 |
| `array/two-pointer-fast-slow.md` | DS-A01 Candidate Topic / DS01 Use | 以“已确认输出区 + 未扫描区”循环不变量解释原地筛选；覆盖/交换语义分开。 |
| `array/two-pointer-left-right.md` | DS-A01 Candidate Topic | 吸收有序和、容器、三数和、接雨水；每种移动策略必须给出支配淘汰证明。 |
| `array/matrix.md` | DS-A01 Candidate Topic | 吸收坐标变换、四边界收缩、单行单列防重复；矩阵存储机制仍归 DS01。 |

### 2.3 回溯（3）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `backtrack/framework.md` | DS-A02 Candidate Topic | 路径、选择、结束、做/撤销；补状态恢复不变量、输出敏感复杂度与可变对象别名。 |
| `backtrack/permutation-combination.md` | DS-A02 Candidate Topic | 吸收 3×3 变体；把 `start/used/i or i+1` 解释为解空间去重约束，而不是记忆差异。 |
| `backtrack/classic.md` | DS-A02 Candidate Topic | 吸收 N 皇后、数独、括号及可行/最优/对称剪枝；剪枝必须证明不删除可行最优叶子。 |

### 2.4 BFS、DFS 与图（8）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `bfs/framework.md` | DS-B01 + DS07 Canonical Update | 补状态图建模、层边界、双向 BFS；“首次到达最短”仅限等权边且 discovery 时标记。 |
| `dfs/islands.md` | DS07 Canonical Update | 补网格隐式图、原地 visited、边界先消除、形状编码；修改输入必须显式声明。 |
| `graph/basics.md` | DS07 Canonical Update | 邻接表/矩阵与遍历应用；“树不需 visited”需限定根向下、无父回边。 |
| `graph/bipartite.md` | DS08 Canonical Update | 二着色不变量、非连通分量扫描、奇环反证。 |
| `graph/dijkstra.md` | DS08 Canonical Update / DS05 Use | 补 lazy heap、过期条目、非负权 settle 证明；“BFS + 贪心”仅作直观，不替代 relax 不变量。 |
| `graph/mst.md` | DS08 Canonical Update / DS06/05 Use | 补 Kruskal/Prim 代码应用与 cut property；“Prim 适合稠密图”取决于矩阵或堆实现。 |
| `graph/topo-sort.md` | DS08 Canonical Update | 补 Kahn 剩余入度不变量、三色 DFS 与 cycle witness；拓扑序一般不唯一。 |
| `graph/union-find.md` | DS06 Canonical Update | 补连通性应用；纠正“路径压缩后树高永久为 1”，保留均摊 $\alpha(n)$ 条件。 |

### 2.5 动态规划（7）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `dp/framework.md` | DS-A03 Candidate Topic | 暴力递归→memo→tabulation；把“状态/选择/base”升级为状态充分性、转移完备性和依赖 DAG。 |
| `dp/knapsack.md` | DS-A03 Candidate Topic | 0-1/完全背包、布尔/计数/最值目标；一维倒序/正序由同轮依赖语义证明。 |
| `dp/path.md` | DS-A03 Candidate Topic | 正向/反向网格 DP；地下城例说明“方向”取决于何处能形成充分状态。 |
| `dp/house-robber.md` | DS-A03 Candidate Topic / DS04 Use | 线性、环形拆分、树形后序 DP；统一为约束图上的 include/exclude 状态。 |
| `dp/edit-distance.md` | DS-A03 Candidate Topic | 二维前缀状态、插删改转移与 base；补每个转移对应最后一步的完备/互斥论证。 |
| `dp/stock.md` | DS-A03 Candidate Topic | 状态机 DP、交易次数、持有状态、冷冻/手续费；交易次数定义与同日更新顺序需固定。 |
| `dp/subsequence.md` | DS-A03 Candidate Topic / DS09 Use | LIS/LCS；`tails` 不是实际 LIS，需用支配关系证明长度正确并调用 lower_bound。 |

### 2.6 贪心（2）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `greedy/interval.md` | DS-A04 Candidate Topic | 右端点调度、区间刺点、左端点合并；三个问题目标不同，必须分别证明而非按“区间套路”混同。 |
| `greedy/jump-game.md` | DS-A04 Candidate Topic / DS-B01 Use | 可达前缀与最远边界；Jump II 是层边界承诺，不是每次真的跳到当前最远下标。 |

### 2.7 Hash、Heap 与组合设计（7）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `hash/design.md` | DS10 Canonical Update / Correct | 散列、链地址、开放寻址、装填与 rehash；语言/平台阈值降为 Extension，平均与均摊口径分开。 |
| `hash/classic.md` | DS10 Canonical Update / DS-I01 Use | 配对、分组、起点去重、RandomizedSet；所有 `O(1)` 绑定散列假设。 |
| `hash/lru-lfu.md` | DS-I01 Canonical Update / DS01/10 Use | LRU/LFU 组合状态已纳入；补同步不变量、容量 0、频率桶内 LRU tie-break。 |
| `heap/basics.md` | DS05 Canonical Update | 数组映射、swim/sink、Floyd 建堆；补空堆 API、比较器与 $O(n)$ 证明。 |
| `heap/applications.md` | DS05 Canonical Update / DS-I01 Use | Top-K、Quickselect 对比、双堆中位数；分区有序与大小平衡须同时成立。 |
| `topics/design.md` | DS-I01 Canonical Update | API→能力→组合；RandomizedSet、Feed 等轨迹，Feed 全量排序只是基线，堆归并才体现规模约束。 |
| `topics/trie.md` | DS09 Canonical Update / Correct | 前缀索引、终止标记、字典序遍历；空间取决于总节点数与 children 表示，不能写成固定乘 $\Sigma$。 |

### 2.8 链表（3）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `linked-list/reverse.md` | DS01 Canonical Update | 全链、区间、K 组反转；用“未处理后缀仍可达、已反转前缀正确终止”不变量解释断边顺序。 |
| `linked-list/two-pointer.md` | DS01 Canonical Update | dummy、合并、快慢、定距、环入口；环入口等式需包含快指针可能多绕 $k$ 圈的一般证明。 |
| `linked-list/palindrome.md` | DS01 Canonical Update / DS04 Use | 中点+反转+比较与递归后序；若 API 要求输入保持不变，比较后必须恢复链。 |

### 2.9 栈、队列与单调候选（4）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `stack-queue/brackets.md` | DS02 Canonical Update | LIFO 嵌套、计数器退化条件、三类失败状态。 |
| `stack-queue/calculator.md` | DS02 Canonical Update | 延迟归约、优先级、括号递归；必须定义一元运算、除法截断与非法输入合同。 |
| `stack-queue/monotonic-stack.md` | DS02 Canonical Update | 支配候选、索引/值、左右扫描双模板；均摊线性由每元素至多入出一次证明。 |
| `stack-queue/monotonic-queue.md` | DS02 Canonical Update / DS-A01 Use | 单调性 + 过期双不变量；代码不能用 `shift()` 后仍宣称实现级 $O(n)$。 |

### 2.10 排序（11）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `sorting/comparison.md` | DS11 Canonical Update / Correct | 吸收决策矩阵与比较下界；所有“唯一”“默认最快”和固定规模阈值改为条件化结论。 |
| `sorting/bubble-sort.md` | DS11 Canonical Update | 有序后缀、提前终止、相邻交换次数=逆序对。 |
| `sorting/insertion-sort.md` | DS11 Canonical Update | 有序前缀、移动而非交换、二分只降比较不降搬移、近有序/在线特性。 |
| `sorting/selection-sort.md` | DS11 Canonical Update | 已定位前缀、固定比较次数、低交换量与不稳定反例。 |
| `sorting/shell-sort.md` | DS11 Canonical Update / Correct | $h$-sorted 不变量和增量依赖；经验复杂度不得写成普遍定理。 |
| `sorting/merge-sort.md` | DS11 Canonical Update / DS12 Use | merge 合同、稳定条件、逆序对；“唯一稳定 $O(n\log n)$”与“外排唯一方案”均需删除。 |
| `sorting/quick-sort.md` | DS11 Canonical Update | Lomuto/三路分区、随机 pivot、Quickselect；补 partition 精确区间与最坏栈防御。 |
| `sorting/heap-sort.md` | DS11 Canonical Update / DS05 Use | 最大堆有效前缀 + 已排序后缀；缓存/常数差异只作条件化工程说明。 |
| `sorting/counting-sort.md` | DS11 Canonical Update / DS-A01 Use | 值域、偏移、前缀定位、反向稳定放置；简单重写数值不等于对记录稳定。 |
| `sorting/bucket-sort.md` | DS11 Canonical Update / DS12 Use | 范围分桶、分布假设、桶内算法与倾斜；平均线性必须声明概率模型。 |
| `sorting/radix-sort.md` | DS11 Canonical Update | LSD 稳定多关键字、MSD 递归、负数/变长 key；$d$、radix 与字长都进入成本。 |

### 2.11 位运算与字符串匹配（2）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `topics/bit-manipulation.md` | Candidate Extension Note / CO boundary | XOR、lowbit、清最低 1 可作为状态编码工具；移位=乘除只在无溢出、符号和语言语义满足时成立。位级机器语义不由 DS 重写。 |
| `topics/kmp.md` | DS03 Canonical Update | prefix/failure、主串不回退、空模式；统一 `next` 下标语义，补线性复杂度的回退势能证明。 |

### 2.12 海量数据（3）

| Source | 路由 | 动作与边界 |
|---|---|---|
| `massive-data/external-sort.md` | DS12 + DS-I01 Canonical Update | run、$k$ 路归并、范围桶、并发/GC 实验；实验瓶颈只对给定 JSON/JVM/硬件成立。 |
| `massive-data/topk-and-frequency.md` | DS-I01 Canonical Update / DS05/10/12 Use | 流式 Top-K、局部到全局合并、Hash 分片词频、Count-Min；补局部 Top-K 可合并证明、tie 和 distinct 语义。 |
| `massive-data/query-dedup-intersect.md` | DS-I01 Canonical Update / DS10/12 Use | 存在/去重/交集的精确与近似分流、bitmap/Bloom、同函数分片与倾斜；Hash 分片不是外部全序排序的万能替代。 |

## 3. 需要进入 Canonical 的关键纠偏

1. `O(1)` Hash 必须写 average/expected/amortized 的具体口径与前提。
2. BFS 首次发现最短只适用于边代价相同或已转换成层数相同的状态图。
3. DFS 空间不是天然小于 BFS；它取决于深度 $h$ 与 frontier 宽度 $w$，二者都可达 $O(V)$。
4. DP 不是所有“穷举 + 备忘录”的同义词；状态合并必须满足相同状态拥有相同未来价值。
5. 贪心不是“每次选眼前最大/最小”，而是带证明的承诺；没有交换、cut、stays-ahead 或支配证明时只是启发式。
6. 回溯剪枝不能只写“减少搜索”；必须证明被删子树不含所需解或不可能改善 incumbent。
7. 单调栈/队列丢弃元素的理由是 dominance，不是为了让容器好看；相等元素的弹出策略受题目 strict/non-strict 语义控制。
8. 前缀和/差分的对偶依赖所用运算和边界约定；非可逆聚合不能机械相减。
9. 排序比较下界只约束 comparison decision tree；计数、桶、基数借助 key 域信息，不是无条件突破。
10. “I/O-bound / CPU-bound / 多线程有效”都是 workload 结论，必须重新测量，不能从单次实验晋升为平台无关事实。

## 4. 渐进实施顺序与连锁防御

1. 先完成 DS-I01 的组合/规模化增量（已完成首轮），不复制 DS05/10/12 的局部机制。
2. 建立 DS-A01–A04 Canonical 深度正文与 Landing，明确均为 Topic、在 Atlas 中是 Extension 关系，不改变 12 个 408 Core Topic 的考试范围。
3. 再按现有 Owner 小步回填 DS01–DS12；每次只增加该结构拥有的机制、应用和反例，遇到当前工作树中的他人改动就基于最新文本合并。
4. Atlas 只更新地图、Routing 和状态，不展开四本正文；Rules 只吸收识别/验证/退出动作。
5. 每个新 Topic 至少通过三类攻击：能否从不变量生成代码；换题面后能否迁移；前提破坏时能否主动拒绝模板。

## 5. 当前证据状态

- **事实**：66/66 篇已读取；文件清单与行数已核对；所有条目已有 Owner 路由。
- **Canonical Update**：DS-I01 已完成首轮深度扩充并发布 11 页阅读视图。
- **Canonical Update**：DS-A01--A04 已建立独立 Mother Question、Stop Boundary、Canonical `.tex`、Landing、Atlas/Ownership 路由与 Published PDF；按不改变 408 Core 范围的方案作为算法扩展分区显示。
- **既有 Owner 增量**：DS04/05/07/09/10/11/12 已分别吸收序列化与后序摘要、双堆与 $K$ 路候选、隐式图与 Flood Fill、答案二分与 Trie、Hash 应用、Quickselect/桶排序/自然 runs、范围分桶与 workload 瓶颈测量。
- **No Update / Control Candidate**：学习练习方法仍不写入 Handbook；只有在建立独立证据晋升流程后，才考虑进入 Rules。

## 6. 深度核销 v2：从“有去向”到“正文能生成机制”

首轮路由只证明 66/66 篇 Source 都能定位到 Owner；本轮继续逐项核查“机制、变体、边界、证明、复杂度和测试义务”是否已经进入正文。结论是：没有发现需要新增第五个算法 Handbook 的独立母问题，但发现并补入了以下此前只有概念级覆盖的高价值细节：

| Source 细节 | 唯一 Owner | 本轮补入的可生成机制 |
|---|---|---|
| \`graph/basics.md\` 的 LC 797 全路径 | DS-A02 | DAG 路径的 \`path\` 追加/弹出、结果快照、一般图的本路径 visited、输出敏感复杂度；与可达性/最短路合同分流 |
| \`bfs/framework.md\` 的 LC 111 | DS04 | 层序首个叶节点最小深度、节点数/边数口径、空树边界、BFS/DFS 空间对比 |
| \`tree/bst.md\` 的 LC 230/538/98 | DS09 | 中序秩计数、反中序累加、严格上下界验证，明确局部孩子比较不能证明全局 BST |
| \`massive-data/topk-and-frequency.md\` | DS-I01 | 频次聚合后固定 $K$ 最小堆、tie-break、分片候选合并、Count-Min 预筛与精确二次确认 |
| \`topics/design.md\` 的 LC 355 | DS-I01 | follow 图 + 作者时间线 + $K$ 路堆归并，区分全量排序基线与 $O(F+K\log F)$ 扩展接口 |
| \`sorting/merge-sort.md\` | DS11 | 归并时左段剩余数的逆序对证明、严格比较、宽整数和对拍基线 |
| \`sorting/counting-sort.md\` / \`radix-sort.md\` | DS11 | \`key-min\` 值域偏移、稀疏值域边界、负数拆分/符号映射、LSD 稳定与 MSD 不可混用 |
| \`array/*\` / \`backtrack/*\` / \`dp/*\` / \`greedy/*\` | DS-A01--A04 | 首轮正文继续补齐前缀频次、差分事件、窗口状态协议、k-sum 去重、矩阵旧新状态、回溯 alias/返回合同、MRV/位掩码、DP 哨兵/目标和/LIS 重建、区间端点和 Jump II 边界 |

本轮发布与页面抽查结果：

- DS-A01 6 页、DS-A02 5 页、DS-A03 9 页、DS-A04 4 页；
- DS04 11 页、DS09 10 页、DS11 10 页、DS-I01 11 页；
- 以上 8 份 PDF 均通过 \`cognitive_system.py publish\`，抽查首页与新增段落页无溢出、重叠或未决引用。

仍然保留的边界：\`intro/why-algo.md\` 是动机材料，\`intro/how-to-practice.md\` 是学习控制候选，\`topics/bit-manipulation.md\` 的机器位语义仍由 CO/语言语义 Owner 负责；它们不因“算法目录”而复制成第二份稳定知识。静态 Source Diff 与正文核销不能替代真实题目上的重复使用证据，Rules 仍保持 Candidate。
