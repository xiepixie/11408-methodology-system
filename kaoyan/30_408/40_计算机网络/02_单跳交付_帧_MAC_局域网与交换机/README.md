# 单跳交付：帧、MAC、局域网与交换机

状态：待人工确认；Canonical 深度正文已建立并发布，本轮 305 题中的对应题目已完成首轮验证。Core Mother Model 暂未发现需重写问题，剩余压力转向训练变式与跨 Topic 迁移。

## Hook

一根共享链路不自带 frame boundary、检错、发送权或转发表。本册追踪 raw bits 怎样成为可定界、可检错、可竞争发送并可被交换机交付的一跳 frame。

## Scope / Stop Boundary

本册 Owns framing/transparent transmission、码距与海明码、CRC、ALOHA、CSMA/CD、CSMA/CA、轮询/令牌、Ethernet/WLAN、switch learning/forwarding、VLAN、STP 与 PPP 的 408 边界。

不拥有 next-hop 选择或 ARP；NET04/NET-B01 输出 next-hop identity 后，本册只负责当前链路的 frame 与 local delivery。

## Read Next

- [NET04 IP 转发](../04_IP地址_子网与分组转发/README.md)
- [NET-B01 IP Forwarding × Single-Hop](../50_科内桥梁/NET-B01_IPForwarding与SingleHop/README.md)
- [网络做题规则](../90_做题规则/README.md)

## Canonical Manual

- [Canonical LaTeX 正文](NET-02_单跳交付_方法论手册.tex)
- [Published PDF](../../../90_publish/408/NET-02_单跳交付_方法论手册.pdf)

## Practice Adapter

- [帧、透明传输与介质访问](帧、透明传输与介质访问.md)：定界/填充 → 检错 → 发送权 → 交换机本跳动作；显式处理 NRZI 与零比特填充的易错边界。

## Source Diff

旧 README 的机制、母例和边界已完整迁入 `.tex`。本轮按 408 覆盖审计新增码距/海明码、轮询/令牌权限模型、LAN/WAN 分类边界、Ethernet 帧、802.11 BSS/ESS 与地址角色，以及 PPP 帧字段、LCP/NCP 协商和失败边界。9 页 Published View 已同步；ARP、路由与可靠恢复仍由相邻 Owner 承担。
