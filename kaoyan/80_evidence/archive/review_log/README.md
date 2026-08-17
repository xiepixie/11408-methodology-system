# Review Log Archive

这里保存已经完成当前决策闭环的历史 review log。归档是可逆的整理动作，不是删除；文件中的事实、反例、Source Diff 和外部证据仍可回溯。

## 归档批次

### `2026-08-12/`

- 数学一高数 Topic01--12、H-B01--H-B05、H-I01 与 B00--B07 的 Source Diff / 路由记录；
- 线性代数 2021--2025 真题映射、Source Migration 和 Rules 静态对抗审计；
- 数据结构 DS01--DS12、DS-B / DS-I01 的第一轮 Source Diff；
- 计算机组成原理和操作系统的 Source / Model Diff；
- Bridge v1 逐册审阅台账与 X-B02 跨学科调研证据包。
- 计算机网络八册 Source Diff、408 协议流程覆盖矩阵、NET-B02 v2 与 NET-I01 组合边界核销；X-B04 覆盖审计保留为 Candidate Core。

对应原始记录：

- [计算机网络个人笔记 Source Migration](2026-08-12/2026-08-11_计算机网络_个人笔记_Source_Migration_设计与首轮纳管.md)
- [计算机网络 408 协议流程矩阵](2026-08-12/2026-08-11_计算机网络_408协议流程覆盖矩阵.md)
- [X-B04 覆盖核对](2026-08-12/2026-08-12_X-B04_覆盖核对.md)

这些记录的结论已压缩进根目录 `CURRENT.md`。它们仍然是证据，不代表其中的 Candidate Rules 已升级为已采用。

## 重新打开

需要再次验证某条结论时，在活动目录建立新的日期记录，并在开头注明：

```text
Previous record: ../archive/review_log/2026-08-12/<filename>
Reason to reopen: <new question or new evidence>
```

不要直接修改已归档记录，以免历史结论和新证据混在一起。
