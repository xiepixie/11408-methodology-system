# 数据结构 Bridge / Integration Source-Diff 第一轮

日期：2026-08-12

类型：Canonical Update。

## 迁移结论

数据结构 Atlas 的 3 个 internal Bridge 与 1 个 Integration 已从目录骨架升级为唯一 Canonical `.tex` 正文，并通过项目 `publish` 生成集中发布视图。它们只保留接口、组合轨迹与验证问题，不复制 Topic 的完整机制。

| 资产 | 当前 Owner | 吸收内容 | 明确不吸收 |
|---|---|---|---|
| DS-B01 Frontier Traversal | `50_科内桥梁/DS-B01_FrontierTraversal/` | frontier、visited 时机、LIFO/FIFO、树/图覆盖边界 | Tree/Graph/Stack/Queue 本体 |
| DS-B02 Index Strategy × Workload | `50_科内桥梁/DS-B02_IndexStrategy与Workload/` | workload、冗余、查询/更新/空间/I-O 成本比较 | BST、B+Tree、Hash 内部步骤 |
| DS-B03 Auxiliary Structure × Graph Algorithm | `50_科内桥梁/DS-B03_辅助结构与图算法/` | Heap/Union-Find 的调用契约与图算法交接 | Heap、Union-Find、图算法完整证明 |
| DS-I01 从 Workload 到数据结构选择 | `60_综合专题/DS-I01_从Workload到数据结构选择/` | 关系→操作→候选→不变量→成本→边界的决策轨迹 | 任一单一结构机制 |

## 旧总图核销状态

旧 `408统一总图_心智模型手册_v3.tex` 中与数据结构有关的母模型、Heap 母例、成本边界、Topic 地图和跨册关系，现分别由 Subject Atlas、Atlas Foundation、DS05、DS-B01–B03 与 DS-I01 承担。当前只完成章节级与抽样级核销，旧总图仍保留为 Source；逐句核销完成前禁止删除其 `.tex` 或 PDF。

## 验证证据

- DS01–DS12 的 C++17 严格警告测试通过；DS07 新增邻接矩阵 `has_edge` 的有向/无向边断言通过。
- DS01–DS12、DS-B01–B03、DS-I01 的 Canonical `.tex` 均已通过 `cognitive_system.py publish`。
- `cognitive_system.py check`、系统单元测试和自动 `PROGRESS.md` 生成均通过。

## 下一道 Gate

用 408 真题与陌生综合题验证 Bridge/Integration 是否能改变第一步结构选择；证据不足时只记录 Candidate Rule，不反向扩张 Topic 或删除旧 Source。
