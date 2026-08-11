# NET-B04｜Flow Control × Congestion Control

状态：目录已建立，正文未建。

## Owners
NET06 Transport/TCP ↔ NET07 Congestion Control。

## Mother Interface
`Receiver Capacity Constraint + Network Capacity Constraint -> Sender Effective Window`

核心压缩：`W_send = min(rwnd, cwnd)`。

## Owns
receiver-side flow control 与 path-side congestion control 怎样同时约束发送者，以及两种反馈为什么不能混同。

## Anti-Bridge
`rwnd` 保护 receiver；`cwnd` 保护 network path。可靠性、流控、拥塞控制不是同一问题。
