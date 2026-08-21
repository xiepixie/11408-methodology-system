# NET-B01｜IP Forwarding × Single-Hop Delivery

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
NET04 IP 地址与分组转发 ↔ NET02 单跳交付。

## Mother Interface
`(Packet, Egress, Next Hop) -> LinkAdapter(Egress) -> Link Unit -> One-Hop Delivery`

## Owns
IP 层决定 egress/next hop 后，怎样按 Ethernet/WLAN、PPP 或 tunnel 等链路类型生成一跳交付对象；哪些状态逐跳重建。

## Boundary
ARP 的 `NextHopIP -> MAC` 语义由 NET04 Own；frame/MAC/switch 交付由 NET02 Own。

## Manual
- [Canonical 正文](NET-B01_IPForwarding与SingleHop_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/NET-B01_IPForwarding与SingleHop_桥梁手册.pdf)

## Review v1
已重构为 link-adapter 接口，不再把 `NextHopIP -> MAC` 写成所有链路的固定流程；新增 direct route、neighbor pending、PPP peer 与 tunnel 分支。

## Question Evidence

305 题中 860、862、865–867、908 直接验证了 `destination IP -> next-hop -> current-link identity -> new frame` 的 Ethernet 分支；818/PPP 题则支持“控制状态存在不等于 Ethernet 式 MAC 解析”的边界。**核心接口已验证**，但 PPP egress、tunnel outer packet 与 neighbor pending 的跨链路变式仍缺直接综合题。
