# DS-I01｜从 Workload 到数据结构选择

状态：Canonical 正文已建立；已完成 外部算法笔记中组合设计、频率 Top-K、信息流与规模升级内容的两轮 Source Diff，Published PDF 见下方链接。

## Initial Problem
给定 API、操作频率、规模、数据分布与资源约束，怎样把需求分解成定位、顺序、极值、随机访问、前缀或外存处理能力，并选择或组合合适的数据结构？

## Composition
`Workload -> API Contract -> Required Capabilities -> Candidate Structures -> Composite Invariants -> Cost Vector -> Choice -> Boundary Check`

## Uses
Data Structure Atlas Foundation、DS01–DS12、DS-B01–DS-B03。重点调用 DS01 的数组/链表表示、DS05 的优先队列、DS09/DS10 的索引策略和 DS12 的外部排序。

## Owns
完整结构选择轨迹、跨结构同步不变量与规模升级过程。正文包含 RandomizedSet、LRU/LFU、Top-K、动态中位数、Hash 分片、海量频率统计和外部处理等生成性案例，但不拥有任何单一数据结构机制。

## Verification
检查是否遗漏主要操作、失败语义、边界条件、平均/最坏/均摊口径、跨索引同步、空间/I-O 代价与数据倾斜，以及选择理由是否随 workload 改变而改变。优化方案应与小规模正确基线做差分验证。

## Manual
- Canonical：[DS-I01_从Workload到数据结构选择_方法论手册.tex](DS-I01_从Workload到数据结构选择_方法论手册.tex)
- Published：[DS-I01_从Workload到数据结构选择_方法论手册.pdf](../../../../90_publish/408/DS-I01_从Workload到数据结构选择_方法论手册.pdf)
