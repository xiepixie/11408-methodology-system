# DS03｜串与模式匹配

状态：Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接。

## Position
数据结构 Topic。

## Mother Problem
模式匹配失败后，怎样复用已经获得的匹配信息，而不是把搜索完全退回重来？

## Mother Model
`Matched Prefix -> Mismatch -> Reusable Structure -> Next Alignment -> Continue`

## Owns
串的基本对象、朴素匹配、KMP、prefix/failure 信息及 mismatch 后状态迁移。

## Uses
Atlas Foundation 的成本模型。

## Does Not Own
一般序列存储机制；完整自动机理论只作 Extension。

## Manual
- Canonical：[DS03_串与模式匹配_方法论手册.tex](DS03_串与模式匹配_方法论手册.tex)
- Published：[DS03_串与模式匹配_方法论手册.pdf](../../../90_publish/408/DS03_串与模式匹配_方法论手册.pdf)
- 完整实现：[ds03_string_matching.hpp](code/ds03_string_matching.hpp)
- 边界测试：[ds03_string_matching_test.cpp](code/ds03_string_matching_test.cpp)

## Code Contract
本册代码按 `Operation Contract -> State Fields -> Core Transition -> Invariant Repair -> Boundary Branches -> Complexity -> Executable Tests` 组织。朴素匹配保留“每个起点重新比较”的基线；KMP 通过 prefix function 记录模式自身的最长真前后缀，在 mismatch 时只回退模式状态，主串下标不倒退。

记忆锚点不是 `next` 数组初值，而是：`matched=j` 表示当前文本后缀等于模式前缀 `P[0..j)`；失配候选只能沿 border 链 `j -> prefix[j-1] -> ... -> 0` 缩短。正文包含 `ababaca` 的逐项 prefix 构造和一次完整失配轨迹，测试另用短二字母串穷举对拍朴素算法。
