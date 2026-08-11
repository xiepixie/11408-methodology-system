# 数据结构学科总图

状态：Source；Atlas Foundation / Deep Map 旧工作稿，待与 Canonical Data Structure Subject Atlas README 做 Source Diff；不再迁成第二份 Atlas LaTeX。

标题：《408 数据结构学科总图：关系、表示、操作、不变量与代价》。

## Position

本文件是 [Data Structure Subject Atlas](../README.md) 的 **Atlas Foundation / Deep Map Supplement**，不是第二个独立 Atlas Owner。根 `README.md` 拥有正式 Topic/Bridge/Integration 导航；本文件集中展开所有数据结构 Topic 共用的 Relation、Representation、Workload、Invariant 与 Cost 语言，不拥有具体算法步骤。

## 核心模型

$$
\text{Problem}
\to \text{Relation}
\to \text{Operations / Workload}
\to \text{Representation}
\xleftrightarrow{\text{Algorithm}}
\text{Invariant}
\to \text{Cost Vector}
$$

数据结构研究的不是“有哪些容器”，而是：面对某种数据关系与操作需求，怎样选择可维护的表示，使关键操作在保持正确性的前提下具有可接受的代价。

不存在脱离 workload 的最好结构。若操作 $O_i$ 的出现频率为 $f_i$，选择结构时首先比较：

$$
C_{total}\approx\sum_i f_i C(O_i)
$$

这里的 $C$ 不只包含渐近时间，还可能包含比较、移动、访存、额外空间、递归深度、最坏界和外存 I/O。

## 五个核心对象

| 对象 | 必须回答的问题 |
|---|---|
| Relation | 数据之间是线性、层次、网络关系，还是集合、映射等 ADT 语义？ |
| Operations / Workload | 需要哪些查询和修改？输入输出是什么？操作频率与最坏要求是什么？ |
| Representation | 关系怎样编码到数组位置、节点指针、矩阵、邻接表、索引或槽位？ |
| Invariant | 哪些条件定义了结构合法性，局部修改后怎样保持或恢复？ |
| Cost Vector | 获得查询、更新或遍历能力分别付出什么时间、空间和 I/O 代价？ |

算法是表示上的状态转移：操作前有合法状态，局部动作扩大已确定区域或缩小未处理区域，操作后重新满足不变量。代码只是这条证明链的一种表达。

## 必须建立的区分

1. 逻辑结构不等于存储表示；
2. 数据结构优劣取决于所需操作集合；
3. 算法不是代码清单，而是不变量维护过程；
4. 成本应是操作成本向量，不是孤立的一个复杂度；
5. 树和图遍历都可观察为 frontier 的维护与展开。

## 生成性理解

### Workload 先于结构名称

“查找”必须继续区分按下标定位、按关键字判存在、取极值和范围查询；“删除”必须区分已知位置、已知节点还是只给关键字。操作契约不同，即使使用同一种逻辑结构，候选表示也会改变。

### 不变量先于代码

连续区域、指针闭合、有序性、平衡性、父子偏序、代表元和已确定集合等不变量，才是结构或算法的真正定义。每个修改步骤都应说明：哪些区域已经正确，局部动作怎样扩大正确区域，未处理区域保留什么性质。

### 遍历统一为 frontier

递归调用栈、显式栈、队列和优先队列都在维护“已经发现但尚未展开”的状态。树遍历、DFS、BFS 和多种图算法首先由 frontier 的取出规则区分，再由各自 Topic 定义具体正确性条件。

### 冗余与约束换取速度

排序结果、索引、平衡信息、散列桶和失败函数都保存额外结构。查询因此减少工作，更新则需要支付维护成本。预处理、时间、空间和 I/O 是同一组权衡。

### 边界属于合法状态集合

空结构、单元素、首尾节点、重复关键字、不连通和越界不是算法写完后的补丁。它们决定表示允许哪些状态，必须在不变量和操作契约中提前处理。

## Owns

- Linear / Hierarchical / Network 三类逻辑关系；
- Relation、Representation、Operation、Invariant、Cost 的统一语言；
- 六个知识域和十四个 Topic 的导航关系。

## Uses

不使用任何尚未建立的 Topic 作为前置真相。专题建成后，本 Atlas 只链接和压缩其主干。

## Stop Boundary

不展开链表操作、树旋转、图算法步骤、Hash 冲突处理、KMP `next` 推导或排序过程。

不拥有具体做题动作。题目起手、检查和退出规则归 `90_做题规则/README.md`；具体机制归各 Topic。

## 计划压缩页

一张“Workload -> Representation -> Operation Cost Vector”选择图，加一张 Topic/Bridge 地图。
