# DS08｜图上的结构算法

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
在图的关系空间上，怎样通过局部更新逐步建立满足全局目标的结构？

## Mother Model
`Goal -> Candidate State -> Local Selection/Relaxation -> Invariant -> Global Structure`

## Owns
最小生成树、最短路径、拓扑排序、关键路径等图上目标算法的核心不变量与更新机制。

## Uses
DS05 Heap、DS06 Union-Find，经 DS-B03 交接；DS07 图表示。

## Does Not Own
Heap/Union-Find 内部机制；网络路由协议本体。Routing 只可 Use 本 Topic，不自动形成跨科 Core Bridge。

## Manual
- Canonical：[DS08_图上的结构算法_方法论手册.tex](DS08_图上的结构算法_方法论手册.tex)
- Published：[DS08_图上的结构算法_方法论手册.pdf](../../../90_publish/DS08_图上的结构算法_方法论手册.pdf)
- 完整实现：[ds08_graph_algorithms.hpp](code/ds08_graph_algorithms.hpp)
- 断言测试：[ds08_graph_algorithms_test.cpp](code/ds08_graph_algorithms_test.cpp)

## Code Contract
本册代码覆盖 Prim/Kruskal、Dijkstra、Bellman-Ford、Floyd、拓扑排序，以及包含最早事件、最迟事件与零时差活动判定的完整 AOE 关键路径。

Kruskal 直接复用 DS06 Union-Find；Prim/Dijkstra 复用 DS05 的“按优先级取候选”抽象契约，但当前实现分别采用数组扫描与标准库最小优先队列，不声称复用了 DS05 的整数最大堆类。

统一记忆骨架为：`Goal -> Candidate Domain -> Local Action -> Commit Point -> Invariant -> Failure Evidence`。测试覆盖负边、负环、非连通、有环、不可达、64 位路径代价，以及关键路径正反两遍的完整结果。
