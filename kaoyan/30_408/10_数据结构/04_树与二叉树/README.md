# DS04｜树与二叉树

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
普通树问题要解决的是：父子、兄弟和左右子树这些关系怎样存下来，并能被正确遍历、恢复和转换？Huffman 则进一步问：怎样安排叶节点深度，使带权路径长度最小？

## Mother Model
普通树主干：`层次关系 -> 存储表示 -> 递归拆成子树 -> 遍历/转换 -> 检查结构`；
Huffman 分支：`字符权值 -> 叶深 -> WPL -> 合并最小权值 -> 前缀码`。

## Owns
树/二叉树表示、DFS/BFS 遍历、遍历序列与结构恢复、线索、Huffman 树与编码等树结构应用。

## Uses
DS-B01 Frontier Traversal；Atlas Foundation 成本语言。

## Does Not Own
Heap 的优先队列机制、Union-Find 集合划分、BST/平衡索引的完整查找机制。

## Manual
- Canonical：[树与二叉树：方法论手册 (TeX)](DS04_树与二叉树_方法论手册.tex)
- Published：[树与二叉树：方法论手册 (PDF)](../../../90_publish/408/DS04_树与二叉树_方法论手册.pdf)
- 完整实现：[`ds04_tree_binary.hpp`](code/ds04_tree_binary.hpp)
- 边界测试：[`ds04_tree_binary_test.cpp`](code/ds04_tree_binary_test.cpp)

## 训练导航
- [二叉树遍历与序列重建](二叉树遍历与序列重建.md)：前/中/后/层序手算、DFS/BFS 识别、序列重建、二维表建系、唯一性与 $2^k$ 歧义计数、祖先判据、叶节点相对次序、遍历序列相等/逆序速判、完全二叉树单序列恢复。
- [线索二叉树的前驱、后继与空链域](线索二叉树的前驱后继.md)：先看 tag 分清孩子与线索，再判断先/中/后序的前驱后继；同时处理哪些方向需要父节点、线索化后还剩多少空链域。
- [树、森林与孩子兄弟转换](树森林与孩子兄弟转换.md)：`L=firstChild`、`R=nextSibling` 路径翻译、森林根链、子树规模、叶节点与空左指针、空右指针和存储节省。
- [树的计数、层容量与存储账本](树的计数与存储账本.md)：从 $E=n-1$ 推度数与叶数关系、用 $\Delta n_i$ 处理局部变化、计算各层容量和所需上层节点，并统一处理完全二叉树编号与空指针计数。
- [Huffman 编码与前缀码](Huffman编码与前缀码.md)：二叉/$m$ 叉 Huffman 的合并过程、补零或首轮少合并、按树边与按 bit 计算码长、Trie 前缀判定，以及最大码长下还能放多少码字。

## Code Contract
代码覆盖树节点所有权、递归先/中/后序、显式栈先序/中序、队列层序、高度与**二叉** Huffman 最小合并代价。遍历重建、线索前驱后继、孩子兄弟转换、计数手算与 Huffman/前缀码的考场步骤放在同目录训练文件中，不在 Canonical 正文里再复制一套。$m$ 叉 Huffman 与 Kraft 容量模型当前由 Canonical + 训练层负责，不声称伴随 C++ 已实现；Huffman 底层只调用优先队列接口，堆的实现与不变量由 DS05 Own。
