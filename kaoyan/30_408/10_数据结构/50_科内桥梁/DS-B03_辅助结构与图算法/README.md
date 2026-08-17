# DS-B03｜Heap / Union-Find × Graph Algorithm

状态：Canonical 正文已建立；Published PDF 见下方链接。

## Owners
DS05 Heap、DS06 Union-Find ↔ DS08 图上的结构算法。

## Mother Interface
`Graph Algorithm needs operation -> Data Structure provides operation -> Algorithm invariant progresses`

## Owns
优先队列怎样向 Prim/Dijkstra 提供 extremum 操作；Union-Find 怎样向 Kruskal/连通问题提供 Find/Union。

## Boundary
图算法 Own 选择/松弛/连通等全局不变量；本 Bridge 不重新讲 Heap、Union-Find 或图算法完整过程。

## Manual
- Canonical：[DS-B03_辅助结构与图算法_方法论手册.tex](DS-B03_辅助结构与图算法_方法论手册.tex)
- Published：[DS-B03_辅助结构与图算法_方法论手册.pdf](../../../../90_publish/408/DS-B03_辅助结构与图算法_方法论手册.pdf)

## Review v1
已核对 Heap/Union-Find 提供局部操作、图算法维护全局不变量的职责分离。下一轮用 Prim/Dijkstra/Kruskal 的辅助结构替换与失败边界题验证。
