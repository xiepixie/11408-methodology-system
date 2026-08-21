# 拥塞控制：在不知道路径容量时闭环试探

状态：待人工确认；Canonical 深度正文已建立并发布，本轮 305 题中的对应题目已完成首轮验证。基础 cwnd/ssthresh 轨迹已稳定，后续重点补 Tahoe/Reno duplicate-ACK、fast recovery 与 AQM/ECN 证据。

## Hook

多个 sender 看不到全局负载，却共同挤压同一瓶颈。拥塞控制用 ACK/loss/delay/ECN 等反馈更新本地 `cwnd`，在利用率、排队、丢包与公平之间持续试探。

## Scope / Stop Boundary

本册 Owns 网络拥塞现象、事前/open-loop 与反馈/closed-loop 控制分类，congestion signal、`cwnd`、`ssthresh`、slow start、congestion avoidance、AIMD、fast retransmit/recovery 与经典 Tahoe/Reno 题设模型。

不拥有 `rwnd`、TCP connection 或通用可靠传输；这些状态分别来自 NET06 与 NET03。

## Read Next

- [NET06 传输层与 TCP](../06_传输层_端点_UDP与TCP状态机/README.md)
- [NET-B04 Flow Control × Congestion Control](../50_科内桥梁/NET-B04_FlowControl与CongestionControl/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-07_拥塞控制_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-07_拥塞控制_方法论手册.pdf)

## Practice Adapter

- [TCP 拥塞窗口轮次推演](TCP拥塞窗口轮次推演.md)：先锁题设口径，再按阶段/事件更新 `cwnd`、`ssthresh` 与实际发送上限。

## Source Diff

旧 README 已完整迁入 `.tex`；新增逐事件状态转移表与 network/endpoint Owner 分类，明确事前策略、反馈闭环、slow start/avoidance、timeout、Tahoe 与 Reno duplicate-ACK 分支。6 页 Published View 已同步；具体窗口常数继续服从题设，不被升级为协议永恒事实。
