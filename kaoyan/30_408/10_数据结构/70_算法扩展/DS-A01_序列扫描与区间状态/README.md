# DS-A01｜序列扫描与区间状态

状态：Canonical 正文已建立；算法 Extension Topic，不改变 408 Core Topic 范围。Published PDF 见下方链接。

## Mother Question

> 怎样利用顺序、边界与可增量摘要，让一次扫描永久排除不可能候选，并把区间查询/修改从重复计算降到可审计的成本？

## Scope / Boundary

Owns：前缀和与差分的对偶、固定/可变滑动窗口、快慢/左右双指针、矩阵边界收缩与坐标变换，以及这些模板何时可以安全淘汰候选。Uses DS01 的顺序/矩阵表示、DS02 的单调队列、DS09 的二分、DS10 的 Hash 摘要。Stops：二分的单调谓词与有序索引回 DS09，链表指针机制回 DS01，单调栈/队列回 DS02。

## Manual

- Canonical：[序列扫描与区间状态：方法论手册 (TeX)](DS-A01_序列扫描与区间状态_方法论手册.tex)
- Published：[序列扫描与区间状态：方法论手册 (PDF)](../../../../90_publish/408/DS-A01_序列扫描与区间状态_方法论手册.pdf)
