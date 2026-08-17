# DS09｜查找与有序索引

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
愿意提前维护多少有序结构，可以换取多少查找能力，同时怎样承担更新成本？

## Mother Model
`Order / Index -> Search Reduction -> Update Repair -> Balance/Height Invariant -> Cost Tradeoff`

## Owns
顺序/折半查找、BST、平衡树、红黑树、B/B+ 树等有序索引的生成逻辑与维护代价。

## Uses
Atlas Foundation；DS-B02 做跨表示 workload 比较。

## Does Not Own
Hash 的映射机制；具体实现细节超出 408 核心时标 Extension。

## Manual
- Canonical：[DS09_查找与有序索引_方法论手册.tex](DS09_查找与有序索引_方法论手册.tex)
- Published：[DS09_查找与有序索引_方法论手册.pdf](../../../90_publish/408/DS09_查找与有序索引_方法论手册.pdf)
- 完整实现：[ds09_ordered_index.hpp](code/ds09_ordered_index.hpp)
- 断言测试：[ds09_ordered_index_test.cpp](code/ds09_ordered_index_test.cpp)

## Code Contract
本册代码覆盖 BST 的查找、插入、三类删除分支、有序输出，以及 AVL 的 LL/RR/LR/RL 插入旋转、查找、高度和有序/平衡不变量。B/B+ 的根分裂、节点合并与外存 I/O 作为正文机制和后续扩展边界。
