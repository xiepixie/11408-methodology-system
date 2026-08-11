# NET-B03｜Reliable Transfer × TCP

状态：目录已建立，正文未建。

## Owners
NET03 可靠传输 ↔ NET06 TCP。

## Mother Interface
`Generic Reliability Mechanism -> TCP State/Fields -> Concrete ACK/Sequence/Window/Timer Behavior`

## Owns
Seq、ACK、Timer、Retransmission、Sliding Window 等一般可靠传输机制怎样在 TCP 中被实例化。

## Boundary
GBN/SR 等一般机制由 NET03 Own；TCP connection state、segment 语义和 flow control 由 NET06 Own。
