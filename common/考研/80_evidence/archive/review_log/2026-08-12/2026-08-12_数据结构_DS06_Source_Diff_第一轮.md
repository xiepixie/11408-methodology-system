# 数据结构 DS06 Source-Diff 第一轮

日期：2026-08-12

类型：Canonical Update。

DS06 将“动态划分—代表元—Find/Union—路径压缩/按秩”写入 Canonical 正文。新增 C++17 实现与测试，覆盖 MakeSet、越界、重复 Union、组件数、连通性和路径压缩；正文通过源代码直引绑定分区不变量。Kruskal 只调用 `connected/unite`，其边权排序与生成树证明不在本册重复。严格警告编译与 Address/UndefinedBehavior Sanitizer 已通过。
