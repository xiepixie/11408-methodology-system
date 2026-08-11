# DS11｜内部排序

状态：目录已建立，正文未建。

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
