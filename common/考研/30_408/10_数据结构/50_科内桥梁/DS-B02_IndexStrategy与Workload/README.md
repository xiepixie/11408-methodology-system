# DS-B02｜Index Strategy × Workload

状态：Canonical 正文已建立；Published PDF 见下方链接。

## Owners
DS09 有序索引 ↔ DS10 Hash，并调用 Atlas Foundation 的 cost vector。

## Mother Interface
`Workload -> Required Operations -> Maintained Redundancy/Order -> Search/Update/Space/I-O Cost`

## Owns
不同索引策略在 workload 改变时怎样比较；为什么“更强查询能力”来自预先维护结构并支付更新/空间成本。

## Boundary
不重新讲 BST、B+ Tree、Hash 的内部机制；具体选型口诀进入 Rules。

## Manual
- Canonical：[DS-B02_IndexStrategy与Workload_方法论手册.tex](DS-B02_IndexStrategy与Workload_方法论手册.tex)
- Published：[DS-B02_IndexStrategy与Workload_方法论手册.pdf](../../../../90_publish/DS-B02_IndexStrategy与Workload_方法论手册.pdf)

## Review v1
已核对 workload、必需操作、维护冗余与查询/更新/空间/I-O 成本；明确选型不是固定“Hash 更快”。下一轮用范围查询、动态更新和外存 workload 验证。
