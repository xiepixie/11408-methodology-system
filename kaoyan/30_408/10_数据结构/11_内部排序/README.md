# DS11｜内部排序

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
当全部数据可在内存中参与操作时，怎样通过局部比较、交换、插入、选择或分治逐步制造全局有序？

## Mother Model
`Local Operation -> Progress Measure -> Ordering Invariant -> Termination -> Cost/Stability`

## Owns
插入、交换、选择、归并、基数等内部排序机制，稳定性、移动/比较代价与过程不变量。

## Uses
DS05 Heap 作为 heap sort 的底层机制；Atlas Foundation。

## Does Not Own
外部排序的 block-I/O 模型；“看到什么选哪种排序”的考试动作进入 Rules。

## Manual
- Canonical：[内部排序：方法论手册 (TeX)](DS11_内部排序_方法论手册.tex)
- Published：[内部排序：方法论手册 (PDF)](../../../90_publish/408/DS11_内部排序_方法论手册.pdf)
- 完整实现：[`ds11_internal_sort.hpp`](code/ds11_internal_sort.hpp)
- 边界测试：[`ds11_internal_sort_test.cpp`](code/ds11_internal_sort_test.cpp)

## 训练导航
- [排序过程、稳定性与基数排序](排序过程、稳定性与基数排序.md)：从一趟后的“已提交区域”反推算法，分栏比较/移动/空间，并维护 LSD 各位稳定性。

## Code Contract
本册代码覆盖插入、选择、归并、快速、堆和非负整数 LSD 基数排序；堆排序在本册实现排序过程，但 Heap 的优先队列机制仍由 DS05 Own。测试覆盖空、已排序、重复、逆序和基数排序负值拒绝。
