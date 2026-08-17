# 数据结构算法 Extension Topic

本目录不是第五种 Handbook 类型，也不扩张 408 数据结构考纲。DS-A01--A04 仍是 Topic；`Extension` 只说明它们补足 外部算法笔记中超出 12 个 Core Topic、但能与数据结构母模型稳定连接的算法设计层。

## Routing

| 问题信号 | 进入 Owner | 不应误入 |
|---|---|---|
| 区间重复查询/修改、窗口、双指针、矩阵边界 | [DS-A01 序列扫描与区间状态](DS-A01_序列扫描与区间状态/README.md) | 二分谓词回 DS09；单调队列回 DS02 |
| 全排列/组合/子集、约束满足、做选择与撤销 | [DS-A02 状态空间搜索与回溯](DS-A02_状态空间搜索与回溯/README.md) | 树/图 DFS 机制回 DS04/07 |
| 重复子问题、最优值/计数/可行性、滚动数组 | [DS-A03 动态规划与状态压缩](DS-A03_动态规划与状态压缩/README.md) | 具体表示与遍历回相应结构 Owner |
| 区间调度、跳跃边界、局部选择的全局承诺 | [DS-A04 贪心选择与交换证明](DS-A04_贪心选择与交换证明/README.md) | 没有证明的启发式不进入稳定 Knowledge |

## Shared Boundary

四册共同使用 Atlas Foundation 的 `Object/State -> Operation -> Invariant -> Boundary -> Cost`，但分别拥有不同正确性义务：A01 证明候选可永久淘汰；A02 证明搜索覆盖且剪枝不漏解；A03 证明状态充分、转移完备、依赖有序；A04 证明局部承诺可交换进某个最优解或始终不落后。

外部算法笔记 66 篇的逐文件 Owner 路由与纠偏记录见 evidence/review_log 的算法来源核对台账。
