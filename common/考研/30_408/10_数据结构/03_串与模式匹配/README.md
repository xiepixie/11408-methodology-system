# DS03｜串与模式匹配

状态：目录已建立，正文未建。

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
