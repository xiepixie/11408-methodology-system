# DS04｜树与二叉树

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
层次关系怎样被递归表示、系统遍历，并通过局部重组维护全局结构？

## Mother Model
`Hierarchy -> Recursive Representation -> Traversal -> Local Change -> Structural Invariant`

## Owns
树/二叉树表示、遍历、线索、Huffman 树与编码等树结构应用。

## Uses
DS-B01 Frontier Traversal；Atlas Foundation 成本语言。

## Does Not Own
Heap 的优先队列机制、Union-Find 集合划分、BST/平衡索引的完整查找机制。

## Manual
- Canonical：[树与二叉树：方法论手册 (TeX)](DS04_树与二叉树_方法论手册.tex)
- Published：[树与二叉树：方法论手册 (PDF)](../../../90_publish/408/DS04_树与二叉树_方法论手册.pdf)
- 完整实现：[`ds04_tree_binary.hpp`](code/ds04_tree_binary.hpp)
- 边界测试：[`ds04_tree_binary_test.cpp`](code/ds04_tree_binary_test.cpp)

## Code Contract
代码覆盖树节点所有权、递归先/中/后序、显式栈先序/中序、队列层序、高度与 Huffman 最小合并代价。Huffman 只调用优先队列接口；堆的实现与不变量由 DS05 Own。
