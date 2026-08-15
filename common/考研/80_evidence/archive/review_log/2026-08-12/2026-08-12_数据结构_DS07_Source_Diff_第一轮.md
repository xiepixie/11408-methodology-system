# 数据结构 DS07 Source-Diff 第一轮

日期：2026-08-12

类型：Canonical Update。

核对更正：本册代码现同时维护邻接表与邻接矩阵，并由测试验证 `has_edge` 的有向/无向语义；旧记录中的实现描述已按当前源文件复核。

DS07 将图关系—表示—frontier—visited—覆盖模型写入 Canonical 正文。新增 C++17 图实现同时维护邻接表与邻接矩阵，覆盖有向/无向边、自环、重复边、DFS、BFS、不连通图组件入口和越界；测试验证发现即标记、顺序、覆盖与表示成本边界。严格警告编译与 Address/UndefinedBehavior Sanitizer 已通过。最短路、MST、拓扑排序保留给 DS08。
