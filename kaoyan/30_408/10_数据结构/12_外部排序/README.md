# DS12｜外部排序

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
当数据不能全部进入内存、真正昂贵的操作变成块 I/O 时，怎样重新设计排序过程以减少数据搬运轮数？

## Mother Model
`Block-I/O Cost -> Initial Runs -> Multiway Merge -> Pass Count -> I/O Tradeoff`

## Owns
外部排序、初始归并段、多路归并、败者树等 408 核心机制及 I/O 成本语言在本 Topic 中的实例化。

## Uses
Atlas Foundation 的 cost vector；存储系统的 block 概念只作 Use/Extension，不自动建立跨科 Core Bridge。

## Does Not Own
内部排序机制、磁盘/文件系统完整机制。

## Manual
- Canonical：[DS12_外部排序_方法论手册.tex](DS12_外部排序_方法论手册.tex)
- Published：[DS12_外部排序_方法论手册.pdf](../../../90_publish/408/DS12_外部排序_方法论手册.pdf)
- 完整实现：[ds12_external_sort.hpp](code/ds12_external_sort.hpp)
- 边界测试：[ds12_external_sort_test.cpp](code/ds12_external_sort_test.cpp)

## Code Contract
本册代码用内存中的 sorted runs 模拟外部边界：按内存容量生成初始归并段，多路合并维护每一路当前首元素候选，并计算 fan-in 对应的归并轮数。代码不伪装真实文件 I/O；block、缓冲区和设备语义仍由系统专题 Own。
