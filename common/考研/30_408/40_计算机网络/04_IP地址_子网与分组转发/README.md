# IP 地址、子网与分组转发：把全局目的压缩成逐跳动作

状态：Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建。

> **迁移提示**：以下长篇内容是此前误写在 README 中的 working source。它可用于后续 Source Diff，但不再视为 Handbook 正文。正式手册必须迁入同目录 `.tex`；迁移完成后本 README 将压缩为引子、范围、边界和阅读链接。

## 0. 本册定位

本 Topic 回答：在规模巨大、链路技术各异的网络中，一个 router 怎样仅凭 packet 与本地 forwarding state 决定下一跳？

本册拥有 IPv4/IPv6 基础、prefix/CIDR、subnet、LPM、next hop、TTL/Hop Limit、MTU/fragmentation、ARP、DHCP、ICMP、NAT。

本册使用但不拥有 routing state 的生成过程，见[路由](../05_路由_分布式知识与控制平面/README.md)；取得下一跳 MAC 后如何交付 frame，见[单跳交付](../02_单跳交付_帧_MAC_局域网与交换机/README.md)。

## 1. 根本问题：router 不需要知道整条路径

若每台 router 都为每台 host 保存完整路径，状态会随主机数和拓扑变化失控。IP 的关键抽象是分层地址与逐跳转发：

$$
\boxed{
\text{Destination IP}
\to \text{Longest matching prefix}
\to \text{Next hop / output interface}
\to \text{Next-hop MAC}
\to \text{One-hop frame}
}
$$

forwarding 的输出不是“完整路线”，而是当前节点的一个局部动作。下一个 router 对同一 destination IP 再做一次本地判断。

## 2. 地址是聚合坐标，不只是主机编号

IPv4 地址是 32-bit 值。前缀长度 `/p` 将它解释为：

$$
\underbrace{\text{prefix}}_{p\ bits}
\mid
\underbrace{\text{host/interface part}}_{32-p\ bits}.
$$

网络地址由按位与得到：

$$
Network=IP\ \mathrm{AND}\ Mask.
$$

CIDR 的核心价值不是换一种写法，而是让地址分配与路由聚合共享同一种前缀结构。连续地址块可由一个较短前缀概括，使转发表规模不必随每个 host 增长。

### 2.1 Subnetting 与 aggregation 是相反方向

- subnetting：延长前缀，把一个地址块切成更小作用域；
- aggregation：寻找共同前缀，用较短路由概括多个连续地址块。

二者都必须满足块大小与起始地址对齐。VLSM 规划通常按需求从大到小分配，避免小块切碎大块的对齐空间。

## 3. Same subnet? 是主机发送的第一个分叉

主机要发送给 destination IP 时，先用本地 prefix 判断：

```text
destination in local subnet?
├─ yes: next-hop IP = destination IP
└─ no:  next-hop IP = default gateway IP
```

随后 ARP 的目标是 **next-hop IP**，不一定是最终 destination IP。这个分叉连接了端到端 IP 语义与逐跳 MAC 语义。

## 4. LPM：多个真命题中选最具体的一个

一个 destination 可能同时匹配默认路由 `/0`、聚合路由和更具体子网。Longest Prefix Match 选择匹配位数最多的条目，因为更长前缀描述更小、更具体的地址集合。

```text
10.0.0.0/8      -> R1
10.1.0.0/16     -> R2
10.1.2.0/24     -> R3
0.0.0.0/0       -> R4
```

目的 `10.1.2.9` 同时匹配前三条，但应选择 `/24`。Metric/administrative preference 等比较只在候选路由的前缀匹配层级满足具体协议规则后发生，不能用“距离更小”覆盖 LPM。

## 5. Router 转发一个 IPv4 packet 的生命周期

```text
receive frame
-> verify/strip link-layer framing
-> inspect destination IP
-> decrement TTL; if exhausted, discard and usually report ICMP
-> perform LPM
-> choose next hop and output interface
-> check packet size against outgoing MTU
-> resolve/reuse next-hop link address
-> build a new frame and transmit
```

在无 NAT、隧道等中间机制时，source/destination IP 保持其端点语义；每一跳的 source/destination MAC 都重新生成。IPv4 TTL 每跳变化，因此 header checksum 也要更新。

## 6. ARP：解析的是本地交付接口

ARP 维护局部软状态：

$$
(IPv4\ next\!\!\!\!-hop\ address)\to(MAC\ address).
$$

缓存未命中时，请求在当前广播域广播，拥有目标 IPv4 地址的节点单播应答。ARP 不穿越 router；跨网段发送时，源主机解析默认网关，后续每条需要二层地址的链路由相应发送节点独立解析下一跳。

因此完整命名链是：

$$
\text{Destination IP}
\to \text{Next-hop IP}
\xrightarrow{ARP}\text{Next-hop MAC}.
$$

## 7. DHCP：在尚无稳定身份时获得启动配置

新主机最初可能不知道自己的 IP、prefix、gateway 和 DNS server。DHCP 用租约状态机解决 bootstrap：

```text
DISCOVER
-> OFFER
-> REQUEST
-> ACK
-> Bound lease
-> Renew / Rebind / Expire
```

初始阶段使用 UDP 和广播，是因为 client 尚不能假定自己拥有可用 IP 或知道 server。DHCP 不只是“分 IP”；它交付的是使主机能进入 IP 转发世界的一组配置与期限。

## 8. TTL、ICMP 与可失败性

分布式路由状态可能短暂不一致并形成 loop。TTL/Hop Limit 给 packet 设置逐跳生命预算，保证循环不会无限占用资源。

ICMP 把部分网络层失败或诊断信息返回源端：

- Time Exceeded 支持 traceroute 的逐跳观察；
- Echo Request/Reply 支持 ping；
- Destination Unreachable 表示路由、主机、协议/端口或分片约束等失败；
- IPv6 Packet Too Big 支持 Path MTU Discovery。

ICMP 是反馈，不是 IP 可靠性承诺。ICMP 报文本身也可能丢失，且协议限制对某些报文再生成差错，避免反馈风暴。

## 9. MTU 与 fragmentation：异构链路的尺寸冲突

### 9.1 IPv4 教材模型

当 packet 超过 outgoing MTU，且允许分片时，IPv4 source 或中间 router 可生成 fragments；重组只在最终 destination 完成。

除最后一片外，fragment payload 通常取不超过 $MTU-H$ 的最大 8-byte 整数倍。片偏移字段为：

$$
Offset_i=\frac{\text{该片 payload 在原 payload 中的起始字节}}{8}.
$$

所有 fragments 共享 Identification；$\text{MF} = 1$ 表示后面还有片，最后一片 $\text{MF} = 0$。任一片丢失会使整个原 packet 无法完成重组，这是分片的放大成本。

### 9.2 IPv6 的责任变化

IPv6 router 不执行路径中的分片。packet 过大时返回 ICMPv6 Packet Too Big，由 source 根据路径 MTU 调整；若 source 需要分片，使用 Fragment extension header。IPv6 把尺寸适配责任推向端点，以简化转发路径。

## 10. NAT：地址稀缺下的有状态改写

NAPT 常维护：

$$
(private\ IP,private\ port,protocol)
\leftrightarrow
(public\ IP,public\ port,protocol).
$$

出站时改写 source tuple 并建立映射；返回流量按 public tuple 找回内部 endpoint。NAT 缓解 IPv4 地址压力，却引入状态、超时、校验和重算和入站可达性问题，也破坏严格的端到端透明性。

NAT 不是 routing protocol，也不是天然的安全边界。它是 forwarding path 上的 middlebox function。

## 11. IPv6：扩大地址并简化逐跳处理

IPv6 地址为 128 bit，基础首部固定 40 B，移除 IPv4 header checksum，把可选功能放入 extension headers；`Hop Limit` 继承 TTL 的逐跳生命预算；`Next Header` 串联扩展首部或上层协议。

IPv6 的关键不是“地址写得更长”，而是把地址扩展、固定基础首部、端点分片责任和邻居发现放入一套更适合扩展的转发接口。408 中需区分教材列出的过渡方式（dual stack、tunneling）与现代部署的具体工程组合。

## 12. 概念边界

| 概念 A | ≠ | 概念 B | 真正区别与题目信号 | 混淆后果 |
|---|:---:|---|---|---|
| Destination IP | ≠ | Next-hop IP | 前者是最终网络层目标；后者是本跳交付对象 | 跨网段时 ARP 错对象 |
| Next-hop IP | ≠ | Next-hop MAC | 前者来自 forwarding decision；后者服务当前链路 | 把 route table 写成 MAC table |
| Routing | ≠ | Forwarding | routing 生成状态；forwarding 对当前 packet 使用状态 | 把 Dijkstra 与 LPM 混在一步 |
| Prefix match | ≠ | Classful category | CIDR 用任意前缀长度；A/B/C 是历史覆盖模型 | 子网与聚合按默认类别误算 |
| Subnet | ≠ | VLAN | subnet 是三层 prefix 作用域；VLAN 是二层广播域 | 认为二者天然一一对应 |
| TTL | ≠ | Deadline | TTL/Hop Limit 计逐跳预算，不计真实秒数 | 把它当端到端时延字段 |
| Fragmentation | ≠ | Segmentation | IP 适配 MTU；transport segmentation 构造上层传输单元 | 首部、编号和重组责任混乱 |
| NAT | ≠ | Routing | NAT 改写 tuple 并持有映射；routing 选择下一跳 | 忽略 NAT 的状态与反向映射 |

## 13. 做题调用协议

1. 写明当前节点是 host 还是 router；
2. 标出 source/destination IP、local prefix 和 routing table；
3. 主机先判断 same subnet，router 直接执行 LPM；
4. 明确 next-hop IP，再决定是否需要 ARP；
5. 每经过 router 更新 TTL/Hop Limit，并在 IPv4 中处理 checksum；
6. 比较 packet size 与 outgoing MTU，区分 IPv4/IPv6 责任；
7. NAT 场景维护双向 tuple mapping；
8. 用“哪一层、哪个作用域、谁持有状态”复核每个字段。

## 14. 贯穿母例：远端 IP 为什么不能直接 ARP

主机 A：`192.0.2.10/24`，默认网关 `192.0.2.1`，要发往 `198.51.100.20`。

```text
198.51.100.20 AND /24 != 192.0.2.0
-> destination is remote
-> next-hop IP = 192.0.2.1
-> ARP 192.0.2.1, not 198.51.100.20
-> frame destination = gateway MAC
-> packet destination remains 198.51.100.20
```

若直接广播询问远端 IP 的 MAC，请求不会越过 router；问题不在 ARP “没记住”，而在 next-hop representation 尚未建立。

## 15. 高频 First Divergence

- 先 ARP 最终 destination：漏做 same-subnet 分叉；
- LPM 后比较所有条目的 metric：没有先限定最长匹配集合；
- 认为 route table 保存完整路径：混淆逐跳状态与路径生成；
- 每跳都改变 destination IP：把 frame 重封装误投射到 packet；
- IPv6 让中间 router 分片：沿用 IPv4 责任模型；
- 把 NAT 当防火墙或路由协议：没有识别 tuple rewrite 和 state table。

## 16. 一页压缩与复原问题

$$
\boxed{
\text{Destination IP}
\to \text{LPM}
\to \text{Next-hop IP}
\to \text{Next-hop MAC}
\to \text{New frame}
}
$$

1. 为什么层次化 prefix 能压缩 forwarding state？
2. Same-subnet 判断怎样决定 ARP 对象？
3. LPM 为什么不是“随便选一条匹配路由”？
4. IP 与 MAC 在多跳过程中各保持什么、改变什么？
5. IPv6 为什么把 fragmentation 移出 router？

## 17. 来源与校正说明

- 归档笔记《网络层-IP协议》《网络层-子网划分与路由基础》《公式汇总》提供 IPv4、CIDR、ARP、ICMP、NAT 和分片覆盖；
- IPv6 分片责任依据 [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200.html) 校正：只由 source node 执行，不由路径中的 router 执行；
- 旧笔记中“每跳固定发生一次 ARP”等说法已收窄为需要二层解析且缓存未命中的场景，避免把实现缓存和链路类型抹掉。
