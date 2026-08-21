# 可靠传输：用有限状态驯服丢失、损坏与乱序

状态：待人工确认；Canonical 深度正文已建立并发布，本轮 305 题中的对应题目已完成首轮验证。Core Mother Model 暂未发现需重写问题，剩余压力转向 SR/ACK 丢失等复杂状态变式与跨 Topic 迁移。

## Hook

“没有收到 ACK”无法区分数据丢失、ACK 丢失或仍在途中。可靠性来自 Seq、ACK、Timer、Retransmission 与 Duplicate Suppression 共同维持的发送/接收状态机，而不是一个字段。

## Scope / Stop Boundary

本册 Owns Stop-and-Wait、GBN、SR、sender/receiver window、ACK 语义、timer、序号空间与不歧义条件。

不把通用 ARQ 等同 TCP；NET06 Owns byte sequence/connection/flow control，NET07 Owns `cwnd`。

## Read Next

- [NET06 传输层与 TCP](../06_传输层_端点_UDP与TCP状态机/README.md)
- [NET-B03 Reliable Transfer × TCP](../50_科内桥梁/NET-B03_ReliableTransfer与TCP/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-03_可靠传输_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-03_可靠传输_方法论手册.pdf)

## Practice Adapter

- [GBN、SR 与窗口状态推演](GBN、SR与窗口状态推演.md)：先声明 ACK/缓存/Timer 语义，再逐事件维护 sender/receiver 双账本与序号空间约束。

## Source Diff

旧 README 已完整迁入 `.tex`；新增统一事件账本、Stop-and-Wait 四类异常分支、GBN 的 base/nextseq/timer 状态和 SR 的 receive/buffer/deliver 分层。7 页 Published View 已同步，GBN/SR 与 TCP 的停止类比已显式写入正文。
