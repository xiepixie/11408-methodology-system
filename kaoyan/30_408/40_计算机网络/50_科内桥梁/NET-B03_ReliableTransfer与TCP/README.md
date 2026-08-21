# NET-B03｜Reliable Transfer × TCP

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
NET03 可靠传输 ↔ NET06 TCP。

## Mother Interface
`Generic Reliability Mechanism -> TCP State/Fields -> Concrete ACK/Sequence/Window/Timer Behavior`

## Owns
Seq、ACK、Timer、Retransmission、Sliding Window 等一般可靠传输机制怎样在 TCP 中被实例化。

## Boundary
GBN/SR 等一般机制由 NET03 Own；TCP connection state、segment 语义和 flow control 由 NET06 Own。

## Manual
- [Canonical 正文](NET-B03_ReliableTransfer与TCP_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/NET-B03_ReliableTransfer与TCP_桥梁手册.pdf)

## Training
- [TCP 丢包证据与可靠性映射](TCP丢包证据与可靠性映射.md)：把通用 delivery invariant 映射到 TCP byte interval、cumulative ACK、duplicate ACK/RTO evidence，并明确 GBN/SR 类比停止边界。

## Review v1
已重构为 `delivery invariant -> TCP byte interval -> segment evidence -> action`；新增累计前缀、乱序缓存、RTO/duplicate ACK 证据边界及 GBN/SR 类比停止条件。

## Question Evidence

913 提供一般可靠性闭环，932、937、945、946 提供 TCP byte-space / cumulative ACK 的具体实例，761–773 又验证 GBN/SR 的一般窗口与恢复模型。**桥梁的核心映射已经成立，但仍是部分验证**：现有题没有把同一条 TCP 丢包事件同时要求用“通用可靠性不变量”和“TCP byte interval/duplicate ACK/RTO”两套语言解释，SACK/RTO 类比停止边界也缺直接题证。
