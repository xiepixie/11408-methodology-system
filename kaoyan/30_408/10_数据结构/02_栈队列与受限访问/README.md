# DS02｜栈、队列与受限访问

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
限制元素进入和离开的端点，为什么能够编码过程的时间秩序？

## Mother Model
`Access Restriction -> Temporal Order -> State Transition -> Invariant -> Application`

## Owns
栈、队列、循环队列、双端队列及其合法状态与操作语义。

## Uses
DS01 的底层顺序/链接表示；DS-B01 的 traversal frontier 接口。

## Does Not Own
递归、树遍历、图遍历本体；这些只通过 Bridge 调用栈/队列能力。

## Manual
- Canonical：[栈队列与受限访问：方法论手册 (TeX)](DS02_栈队列与受限访问_方法论手册.tex)
- Published：[栈队列与受限访问：方法论手册 (PDF)](../../../90_publish/408/DS02_栈队列与受限访问_方法论手册.pdf)
- 完整实现：[`ds02_restricted_access.hpp`](code/ds02_restricted_access.hpp)
- 边界测试：[`ds02_restricted_access_test.cpp`](code/ds02_restricted_access_test.cpp)

## Code Contract
本册代码按 `Operation Contract -> State Fields -> Core Transition -> Invariant Repair -> Boundary Branches -> Complexity -> Executable Tests` 组织。正文中的代码块直接抽取上述实现文件；顺序栈、链栈、循环队列、链队列与循环双端队列共享一套受限访问语义，但分别维护自己的物理状态。

递归、表达式求值、树/图遍历和单调结构只作为调用示例：Frontier 的可复用接口由 DS-B01 Own，树和图上的正确性分别由 DS04、DS07 Own。
