# NET-B02｜Routing × Forwarding

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
NET05 Routing/Control Plane ↔ NET04 IP Forwarding/Data Plane。

## Mother Interface
`Distributed/Control Knowledge -> Forwarding State -> LPM/Next-Hop Lookup -> Packet Action`

## Owns
路由如何生成/更新转发状态，而转发如何消费该状态处理单个 packet；控制平面与数据平面的 handoff。

## Boundary
DV/LS/BGP 等机制由 Routing Topic Own；LPM 与 packet forwarding 由 NET04 Own。

## Manual
- [Canonical 正文](NET-B02_Routing与Forwarding_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/NET-B02_Routing与Forwarding_桥梁手册.pdf)

## Training
- [FIB 版本与收敛中间态](FIB版本与收敛中间态.md)：专门训练 `selection != install != packet-time use`、next-hop resolution 和多设备异步 FIB 版本。

## Review v1
已核对控制面收敛、FIB 安装、LPM 查找和逐包 action 的时间尺度；下一轮用路由更新期间的 packet 题验证版本边界。

## Boundary Validation v2

两侧 Topic 已完成 Source Diff 后复核通过：NET05 输出 selected prefix、next hop/interface、action attributes 与 install event；NET04 只消费 installed FIB，对当前 destination 执行 LPM。Bridge 新增 next-hop recursive resolution、旧/新 FIB 版本、邻接未就绪和异步安装四类失败分支，不复制 RIP/OSPF/BGP 或 IP forwarding 正文。

## Question Evidence

830、847、874–890、903–906 已分别验证“路由状态生成”和“packet-time FIB/LPM 使用”两侧对象，890 还完成了 `OSPF 选路 -> 既定路径上的逐包成本` 的一次跨接口调用。**接口方向成立，但证据仍是部分验证**：当前没有题明确给出“control plane 已选出新 route、FIB 尚未安装/不同 router 安装版本不同”再追问当前 packet action，因此 version/install boundary 仍是下一轮优先母题。
