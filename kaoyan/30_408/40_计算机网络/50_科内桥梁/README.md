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

## Review v3｜305 题首轮 Bridge 验证

六座 Bridge 都通过了 **Validity Gate**：删掉具体题目后仍存在稳定的 `A 输出 -> 接口翻译 -> B 输入`。题库证据强度并不相同：

| Bridge | 当前证据 | 判断 |
|---|---|---|
| NET-B01 IP Forwarding × Single-Hop | 860、862、865–867、908 | 核心 Ethernet 交接已验证；PPP/tunnel 分支待补 |
| NET-B02 Routing × Forwarding | 830、847、874–890、903–906 | 两侧对象与方向成立；FIB install/version 中间态仍缺直接题 |
| NET-B03 Reliable Transfer × TCP | 761–773、913、932/937/945/946 | 一般机制→TCP byte state 映射成立；RTO/dupACK/SACK 接口仍缺直接综合题 |
| NET-B04 Flow × Congestion | 930、933、944、948、953 | `rwnd/cwnd` Owner 与共同约束已直接验证；FlightSize/zero-window 联合变式待补 |
| NET-B05 BDP × Window | 734、761/762/772、949/953 | 速率时间→在途量→窗口需求已直接验证 |
| NET-B06 MTU × Segmentation | 846、923–926、929 | transport/IP/link 尺寸责任已直接验证 |

因此下一轮 **不再新增 Bridge**。优先补 B02、B03 的状态型跨接口母题；B01/B04 做少量边界变式；B05/B06 进入维护状态。
