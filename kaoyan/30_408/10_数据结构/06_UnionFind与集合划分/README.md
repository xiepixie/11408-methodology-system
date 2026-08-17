# DS06｜Union-Find 与集合划分

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
怎样在不断合并集合的过程中，高效回答两个元素当前是否属于同一集合？

## Mother Model
`Partition -> Representative -> Find / Union -> Path Compression / Rank -> Set Invariant`

## Owns
并查集对象、代表元、Find、Union、按秩/大小合并、路径压缩及动态连通语义。

## Uses
Atlas Foundation；DS-B03 与 Kruskal/图连通问题交接。

## Does Not Own
一般树结构、Kruskal 算法本体。

## Manual
- Canonical：[DS06_UnionFind与集合划分_方法论手册.tex](DS06_UnionFind与集合划分_方法论手册.tex)
- Published：[DS06_UnionFind与集合划分_方法论手册.pdf](../../../90_publish/408/DS06_UnionFind与集合划分_方法论手册.pdf)
- 完整实现：[ds06_union_find.hpp](code/ds06_union_find.hpp)
- 边界测试：[ds06_union_find_test.cpp](code/ds06_union_find_test.cpp)

## Code Contract
本册代码按 `Operation Contract -> State Fields -> Core Transition -> Invariant Repair -> Boundary Branches -> Complexity -> Executable Tests` 组织。实现维护 `parent/rank/components`，`find` 做路径压缩，`unite` 按秩合并；重复合并不减少集合数，越界元素显式拒绝。Kruskal 只调用 `connected/unite`，不复制底层实现。
