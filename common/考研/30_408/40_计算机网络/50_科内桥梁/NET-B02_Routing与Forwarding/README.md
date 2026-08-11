# NET-B02｜Routing × Forwarding

状态：目录已建立，正文未建。

## Owners
NET05 Routing/Control Plane ↔ NET04 IP Forwarding/Data Plane。

## Mother Interface
`Distributed/Control Knowledge -> Forwarding State -> LPM/Next-Hop Lookup -> Packet Action`

## Owns
路由如何生成/更新转发状态，而转发如何消费该状态处理单个 packet；控制平面与数据平面的 handoff。

## Boundary
DV/LS/BGP 等机制由 Routing Topic Own；LPM 与 packet forwarding 由 NET04 Own。
