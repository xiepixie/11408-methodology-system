# 路由与控制平面：不完整知识怎样收敛为可用转发状态

状态：已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证。

## Hook

路由不是求一次最短路，而是在局部观察、消息延迟、拓扑变化和策略约束下持续维护知识。本册追踪“观察 → 通告 → 合并 → 按目标/策略选择 → 安装 → 随时间收敛”。

## Scope / Stop Boundary

本册 Owns connected/static/default/dynamic route 来源，DV/LS/path-vector、RIP/OSPF/BGP、AS/area、RIB candidate/selection、convergence、control/data plane 和 SDN 的逻辑集中控制模型。

不执行当前 packet 的 LPM、ARP 与逐跳重封装；图算法只作为计算工具，不因算法同名自动建立跨科 Bridge。

## Owns / Uses

- Uses 图与最短路算法，但 Owns 输入知识怎样形成、辨新旧和传播；
- Outputs selected prefix route、next hop/interface 与 action attributes 给 NET-04；
- 与 NET-B02 通过 `RIB selection → FIB install → LPM action` 交接；
- BGP 只承诺策略约束下的可达性选择，不承诺全网最短或最低时延。

## Read Next

- [NET-04 IP 地址、子网与分组转发](../04_IP地址_子网与分组转发/README.md)
- [NET-B02 Routing × Forwarding](../50_科内桥梁/NET-B02_Routing与Forwarding/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-05_路由与控制平面_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-05_路由与控制平面_方法论手册.pdf)

## 当前状态

协议流程复核已完成：10 页 Published View 已覆盖 connected/static/default route、RIP Request/Response/定时器、OSPF Hello/DD/LSR/LSU/LSAck 与邻居 FSM、BGP FSM/四类消息、SDN Packet-In/Flow-Mod/Packet-Out。

首轮 Source Diff 已完成：RIP/OSPF/BGP、SDN 与拓扑材料已按知识表示和生命周期重构；固定 BGP 万能选路顺序、OSPF 永久无环、Area 0 无例外、controller 物理唯一且拥有即时全局最优等绝对表述均未进入稳定正文。正文仍是待人工确认候选。
