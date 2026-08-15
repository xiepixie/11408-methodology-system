# 数据结构 DS08 Source-Diff 第一轮

日期：2026-08-12

类型：Canonical Update。

DS08 接续已有草稿并完成代码覆盖矩阵：保留 Dijkstra、Kruskal、拓扑排序，新增 Prim、Bellman-Ford 与 DAG 关键路径最早时刻。实现通过 DS05/DS06 的优先队列/并查集边界交接，不复制其内部机制。测试覆盖正常路径、负边、可达负环、非连通图、有环图和关键路径时序；严格警告编译与 Address/UndefinedBehavior Sanitizer 已通过。
