# 数据结构 DS03 Source-Diff 第一轮

日期：2026-08-12

## 判定

- 类型：Canonical Update
- Knowledge Owner：`30_408/10_数据结构/03_串与模式匹配/DS03_串与模式匹配_方法论手册.tex`
- 代码证据：`code/ds03_string_matching.hpp` 与 `code/ds03_string_matching_test.cpp`

## 旧材料吸收

- 吸收总册中“失配后复用已匹配前缀”的 KMP 母模型。
- 将 `next` 的教材差异解释为 prefix/failure 信息的编码差异，而不是并列定义。

## 代码机制证据

- 同一返回契约下实现朴素匹配、prefix function 和 KMP 主循环。
- 测试覆盖空模式、模式过长、无匹配、重复前后缀、回退后继续匹配及朴素/KMP 结果一致性。
- 正文使用 `\lstinputlisting` 直接引用实现源文件，绑定状态变量、回退不变量与复杂度证明。
