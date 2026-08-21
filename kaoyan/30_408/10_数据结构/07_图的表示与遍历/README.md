# DS07｜图的表示与遍历

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
任意关系怎样被表示，并从一个起点系统访问所有可达对象而不重复失控？

## Mother Model
`Graph Relation -> Representation -> Frontier -> Visit State -> Expansion -> Coverage`

## Owns
图的基本对象、邻接矩阵/表、DFS/BFS 在图语义下的遍历、visited 状态、连通与遍历森林基础。

## Uses
DS-B01 Frontier Traversal；Atlas Foundation。

## Does Not Own
最短路、最小生成树、拓扑排序等图上目标算法。

## Manual
- Canonical：[图的表示与遍历：方法论手册 (TeX)](DS07_图的表示与遍历_方法论手册.tex)
- Published：[图的表示与遍历：方法论手册 (PDF)](../../../90_publish/408/DS07_图的表示与遍历_方法论手册.pdf)
- 完整实现：[`ds07_graph_traversal.hpp`](code/ds07_graph_traversal.hpp)
- 边界测试：[`ds07_graph_traversal_test.cpp`](code/ds07_graph_traversal_test.cpp)

## 训练导航
- [图表示、BFS 与 DFS 状态推演](图表示、BFS与DFS状态推演.md)：表示语义 → Unseen/Discovered/Expanded → frontier → 连通分量与无权最短层数。

## Code Contract
本册代码按 `Operation Contract -> Representation -> Frontier -> Visit State -> Expansion -> Coverage` 组织。实现同时保留邻接表（遍历）与邻接矩阵（判边）以对照表示成本；DFS/BFS 在发现时标记 `visited`，不连通图通过遍历森林补齐组件。DS08 只调用图表示和遍历接口，不复制底层实现。

记忆锚点固定为 `Discover -> Mark -> Enqueue/Push -> Expand`：frontier 中的顶点已经处于 Discovered 状态，不能等取出时才标记。DFS/BFS 共享 Unseen/Discovered/Expanded 三态，只改变 frontier 的取出顺序。
