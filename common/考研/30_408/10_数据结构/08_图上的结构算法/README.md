# DS08｜图上的结构算法

状态：目录已建立，正文未建。

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
