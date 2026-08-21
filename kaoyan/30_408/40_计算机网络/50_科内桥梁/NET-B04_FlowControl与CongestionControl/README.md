# NET-B04｜Flow Control × Congestion Control

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
NET06 Transport/TCP ↔ NET07 Congestion Control。

## Mother Interface
`Receiver Capacity Constraint + Network Capacity Constraint -> Sender Effective Window`

核心压缩：`Usable = max(0, min(rwnd, cwnd) - FlightSize)`。

## Owns
receiver-side flow control 与 path-side congestion control 怎样同时约束发送者，以及两种反馈为什么不能混同。

## Anti-Bridge
`rwnd` 保护 receiver；`cwnd` 保护 network path。可靠性、流控、拥塞控制不是同一问题。

## Manual
- [Canonical 正文](NET-B04_FlowControl与CongestionControl_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/NET-B04_FlowControl与CongestionControl_桥梁手册.pdf)

## Review v1
已重构为 receiver/path 两个独立反馈回路；补入 `FlightSize`、zero-window probe、四种约束组合与“状态上限不等于新增发送量”的边界。

## Question Evidence

930、933 直接区分 `rwnd` 与 `cwnd` Owner，948、953 又要求实际发送受 `min(cwnd,rwnd)` 约束，944 提供 byte-window 的量纲接口。**核心 Bridge 已被直接验证**。剩余缺口主要是显式给出 `FlightSize` 的三变量可发送量题，以及 zero-window persist 与 congestion event 同时出现时的双回路状态推进。
