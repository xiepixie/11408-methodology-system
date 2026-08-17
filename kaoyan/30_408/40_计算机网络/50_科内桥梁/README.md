# 计算机网络 Internal Bridge Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设。

- [NET-B01｜IP Forwarding × Single-Hop Delivery](NET-B01_IPForwarding与SingleHop/README.md)
- [NET-B02｜Routing × Forwarding](NET-B02_Routing与Forwarding/README.md)
- [NET-B03｜Reliable Transfer × TCP](NET-B03_ReliableTransfer与TCP/README.md)
- [NET-B04｜Flow Control × Congestion Control](NET-B04_FlowControl与CongestionControl/README.md)
- [NET-B05｜BDP × Window](NET-B05_BDP与Window/README.md)
- [NET-B06｜MTU × Segmentation](NET-B06_MTU与Segmentation/README.md)

这些 Bridge 只处理网络 Topic 内部接口。Process/Socket × Transport Endpoint 若晋升为 Core，统一由 408 Cross-Subject Bridge Own。

## Review v2

NET-B01、B03、B04 已按接口合同重构；B05、B06 经考纲覆盖审计满足独立 Bridge 门槛并建立 Canonical 正文。六桥分别覆盖链路适配、路由/转发、可靠性/TCP、双窗口反馈、BDP/窗口利用率和 MTU/分段责任；协议内部细节仍留在 Topic。
