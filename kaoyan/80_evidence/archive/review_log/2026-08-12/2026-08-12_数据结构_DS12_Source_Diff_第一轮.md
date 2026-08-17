# 数据结构 DS12 Source-Diff 第一轮

日期：2026-08-12

类型：Canonical Update。

DS12 将外部排序的 I/O 成本主线写入 Canonical 正文，并补齐此前缺失的代码证据：初始 runs、k 路归并候选和归并轮数估算。实现明确是内存模拟，不冒充文件系统实现；测试覆盖空 run、单 run、多路耗尽、零容量和非法 fan-in。严格警告编译与 Address/UndefinedBehavior Sanitizer 已通过。
