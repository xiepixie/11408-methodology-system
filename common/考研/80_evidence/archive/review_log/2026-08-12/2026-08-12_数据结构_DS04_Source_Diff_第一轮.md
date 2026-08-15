# 数据结构 DS04 Source-Diff 第一轮

日期：2026-08-12

类型：Canonical Update。

DS04 将旧总册的递归层次、先/中/后序访问时机、层序 frontier 与 Huffman 最小合并主线写入 Canonical `.tex`。新增 C++17 实现覆盖唯一所有权节点、递归/显式栈/队列遍历、高度和 Huffman 合并代价；测试覆盖空树、单节点、非满二叉树、遍历结果与 Huffman 单/空输入。Huffman 只调用优先队列接口，Heap 内部机制继续由 DS05 Own。严格警告编译与 Address/UndefinedBehavior Sanitizer 均通过。
