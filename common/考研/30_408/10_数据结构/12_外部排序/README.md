# DS12｜外部排序

状态：目录已建立，正文未建。

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
