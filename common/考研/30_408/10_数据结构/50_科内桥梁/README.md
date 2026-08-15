# 数据结构 Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas，B01–B03 已建立并发布深度正文。

Bridge 只拥有 Topic 之间稳定、可复用的接口，不重讲 Topic。

- [DS-B01 Frontier Traversal](DS-B01_FrontierTraversal/README.md)：Recursion/Stack/Queue 与 Tree/Graph traversal 的 frontier 语义。
- [DS-B02 Index Strategy × Workload](DS-B02_IndexStrategy与Workload/README.md)：不同索引策略怎样用维护成本换查询能力。
- [DS-B03 Auxiliary Structure × Graph Algorithm](DS-B03_辅助结构与图算法/README.md)：Heap/Union-Find 向图算法提供什么操作接口。

Graph Algorithm × Routing、External-Memory × Block I/O 当前不在这里升级成独立跨科 Core Bridge。

## Review v1

DS-B01--B03 已完成首轮审阅；每册均把辅助结构的局部操作与算法的全局不变量分开，下一轮用容器替换、workload 变化和失败分支题验证。
