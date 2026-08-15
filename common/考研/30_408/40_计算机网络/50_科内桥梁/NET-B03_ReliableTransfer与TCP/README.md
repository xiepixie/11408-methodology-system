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
- [Published PDF](../../../../90_publish/NET-B03_ReliableTransfer与TCP_桥梁手册.pdf)

## Review v1
已重构为 `delivery invariant -> TCP byte interval -> segment evidence -> action`；新增累计前缀、乱序缓存、RTO/duplicate ACK 证据边界及 GBN/SR 类比停止条件。
