# DS01｜线性关系与存储表示

状态：LaTeX 工作稿，待人工确认；已建立并发布 Canonical 深度正文。

## Position
数据结构 Topic。

## Mother Problem
同一线性逻辑关系为什么需要连续、链接等不同物理表示？

## Mother Model

同一线性逻辑关系与操作契约允许选择不同物理表示；表示决定局部更新要维护的不变量与成本向量。Canonical 不再用一条裸箭头把建模顺序、因果和状态流混成同一种关系。

## Owns
顺序表、链式表示、插入删除访问的结构差异、地址/指针关系及边界状态。

## Uses
Atlas Foundation 的 complexity / cost vector。

## Does Not Own
栈队列的受限访问语义；数组地址映射若只是计算技巧进入 Rules/附录。

## 训练导航

- [线性表、顺序表与链表](线性表、顺序表与链表.md)：训练逻辑结构/存储结构分层、线性表与数组辨析、顺序表随机访问、链表按位查找、头指针/头结点/首元结点、逆置防丢链，以及“链表插入 $O(1)$”的真实前提。

## Manual

- Canonical 正文：[线性关系与存储表示：方法论手册 (TeX)](DS01_线性关系与存储表示_方法论手册.tex)
- Published View：[线性关系与存储表示：方法论手册 (PDF)](../../../90_publish/408/DS01_线性关系与存储表示_方法论手册.pdf)
- 完整实现：[`ds01_linear_list.hpp`](code/ds01_linear_list.hpp)
- 断言测试：[`ds01_linear_list_test.cpp`](code/ds01_linear_list_test.cpp)

正文主线区分逻辑对象、操作契约、物理表示、不变量与成本，重点锁定“按位/按值”“位序已知/前驱已知”和“定位成本/局部更新成本”三组边界。
