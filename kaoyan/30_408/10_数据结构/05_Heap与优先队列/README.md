# DS05｜Heap 与优先队列

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
怎样不维护完全有序，却始终高效获得当前最高优先级元素？

## Mother Model
`Partial Order -> Extremum at Root -> Local Repair -> Heap Invariant -> Operation Cost`

## Owns
堆、优先队列、建堆、插入、删除极值、上滤/下滤及 heap sort 所调用的堆机制。

## Uses
Atlas Foundation；DS-B03 与图算法交接。

## Does Not Own
一般树结构、排序全过程、Prim/Dijkstra 本体。

## Manual
- Canonical：[DS05_Heap与优先队列_方法论手册.tex](DS05_Heap与优先队列_方法论手册.tex)
- Published：[DS05_Heap与优先队列_方法论手册.pdf](../../../90_publish/408/DS05_Heap与优先队列_方法论手册.pdf)
- 完整实现：[ds05_heap.hpp](code/ds05_heap.hpp)
- 边界测试：[ds05_heap_test.cpp](code/ds05_heap_test.cpp)

## Code Contract
本册代码按 `Operation Contract -> State Fields -> Core Transition -> Invariant Repair -> Boundary Branches -> Complexity -> Executable Tests` 组织。实现固定为最小堆：根保存当前极小值，完全二叉树下标映射保证紧凑形状，`push/pop` 通过上滤/下滤恢复父子偏序，`build_heap` 使用底向上调整。DS04 的 Huffman、DS08 的图算法与 DS11 的堆排序只调用相应优先队列接口。
