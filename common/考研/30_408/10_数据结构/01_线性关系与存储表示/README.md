# DS01｜线性关系与存储表示

状态：LaTeX 工作稿，待人工确认；已建立并发布 Canonical 深度正文。

## Position
数据结构 Topic。

## Mother Problem
同一线性逻辑关系为什么需要连续、链接等不同物理表示？

## Mother Model
`Linear Relation -> Representation -> Operation -> Invariant -> Cost`

## Owns
顺序表、链式表示、插入删除访问的结构差异、地址/指针关系及边界状态。

## Uses
Atlas Foundation 的 complexity / cost vector。

## Does Not Own
栈队列的受限访问语义；数组地址映射若只是计算技巧进入 Rules/附录。

## Manual

- Canonical 正文：[DS01_线性关系与存储表示_方法论手册.tex](DS01_线性关系与存储表示_方法论手册.tex)
- Published View：[DS-01_线性关系与存储表示_方法论手册.pdf](../../../90_publish/DS01_线性关系与存储表示_方法论手册.pdf)
- 完整实现：[ds01_linear_list.hpp](code/ds01_linear_list.hpp)
- 断言测试：[ds01_linear_list_test.cpp](code/ds01_linear_list_test.cpp)

正文主线是 `Linear Relation -> Operation Contract -> Representation -> Local Update -> Invariant -> Cost Vector`，重点区分“已知位置/已知前驱”和“仍需查找”。
