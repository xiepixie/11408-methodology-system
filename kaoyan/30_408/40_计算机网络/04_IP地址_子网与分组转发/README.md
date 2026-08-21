# IP 地址、子网与分组转发：把全局目的压缩成逐跳动作

状态：待人工确认；Canonical 深度正文已建立并发布，本轮 305 题中的对应题目已完成首轮验证。Core Mother Model 覆盖充分，当前缺口主要是二次分片、NAT 生命周期及多播/移动性组合变式。

## Hook

路由器不需要保存每台主机的完整旅程。它把 destination IP 放入前缀作用域，用 LPM 得到 next hop，再为当前链路解析身份并重建 frame。本册用“Scope → Name → Owner → Event/Cost”把地址、转发、ARP、MTU 与改写状态接成一条生命周期。

## Scope / Stop Boundary

本册 Owns IPv4/IPv6 地址与首部、prefix/CIDR/subnet、same-subnet、FIB/LPM、router composition、next hop、TTL/Hop Limit、ICMP、MTU/fragmentation、ARP、DHCP、NAT、IP multicast 与 Mobile IP 的 408 核心流程。

不拥有 RIP/OSPF/BGP 的路由知识生成、二层交换动作、可靠传输、TCP 或 DNS 服务语义。

## Owns / Uses

- Uses NET-05 输出的 selected route 与 installed FIB；
- Outputs next-hop IP/interface 给 NET-B01 与 NET-02；
- 与 NET-B02 通过 `RIB selection → FIB install → LPM action` 交接；
- Mobile IP 不与蜂窝核心网组件建立硬等同；IP multicast 的本地成员状态不替代 NET05 的路由知识生成。

## Read Next

- [NET-05 路由与控制平面](../05_路由_分布式知识与控制平面/README.md)
- [NET-B01 IP Forwarding × Single-Hop Delivery](../50_科内桥梁/NET-B01_IPForwarding与SingleHop/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-04_IP地址_子网与分组转发_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-04_IP地址_子网与分组转发_方法论手册.pdf)

## Practice Adapter

- [IP 地址、子网与逐跳转发](IP地址、子网与逐跳转发.md)：Scope/名字类型 → Same-Subnet/LPM → 当前 next hop → TTL/MTU/frame/NAT 状态推进。

## 当前状态

协议流程复核已完成：12 页 Published View 已覆盖 IPv4/IPv6 首部与地址作用域、same-subnet/ARP、DHCP DORA/租约、ICMP、MTU/分片数值流程、NAT/NAPT、IPv6 ND、路由器输入/交换结构/输出队列、IP multicast 成员/分发边界，以及 Mobile IP 发现—注册—隧道—注销流程。

首轮 Source Diff 已完成：IP、CIDR、子网、ARP/DHCP/ICMP、MTU/分片、NAT、组播与 Mobile IP 已分流；固定 ARP 次数、`/30` 永远最优、IPv6 完全不分片、IGMP 等于组播路由、NAT 天然等于安全以及 Mobile IP/蜂窝组件硬等同均未进入稳定正文。正文仍是待人工确认候选。
