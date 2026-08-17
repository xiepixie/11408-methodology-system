# 计算机网络 Subject Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Subject Atlas。31 份个人旧笔记已完成全科 Source Routing；NET01--NET08 八个 Topic 均已建立并发布 Canonical LaTeX 候选正文，NET-I01 已建立并发布 Integration。

## 学科母问题

计算机网络研究：在机器彼此独立、链路有限、传输有时延、数据可能丢失、资源需要共享、系统没有全局即时状态的条件下，怎样让不同机器上的进程完成通信。

网络不是协议字段集合，而是分布式状态机。观察任一机制时沿同一条主轴追踪：

$$
\text{Scope}
\to \text{State}
\to \text{Event}
\to \text{Transition}
\to \text{Feedback}
\to \text{Cost}
$$

八个 Topic 由六类现实约束生成，而不是按协议名机械堆叠：Distance 生成时延/BDP/流水发送，Finite Capacity 生成队列与拥塞反馈，Unreliability 生成 Seq/ACK/Timer/Retransmission，Sharing 生成 MAC 与端口复用，Heterogeneity/Scale 生成分层与前缀聚合，No Global Instant State 生成分布式路由控制。应用层再负责把可传输的 bytes 解释成名字、资源和操作语义。

## Foundation：先建立网络的坐标系

### 网络由什么组成，又提供什么

计算机网络由一组相互独立的端系统、连接它们的链路与交换设备，以及约束通信行为的协议共同组成。它的基本功能不是“让机器都连在一根线上”，而是在给定作用域内提供数据通信、资源共享和分布式应用承载。

网络分类必须先声明分类轴，不能把不同维度混成一棵树：

| 分类轴 | 典型类别 | 真正回答的问题 |
|---|---|---|
| 覆盖与管理范围 | PAN / LAN / MAN / WAN | 谁管理、多远、采用何种接入与互连结构 |
| 交换服务 | 电路 / 报文 / 分组；数据报 / 虚电路 | 何时建立状态、按多大粒度存储转发 |
| 传输介质 | 有线 / 无线 | 信号在哪种物理通道中传播 |
| 拓扑 | 总线 / 星形 / 环形 / 网状 | 节点与链路怎样连接，不直接等于协议行为 |
| 使用者关系 | 公用 / 专用 | 资源和管理责任属于谁 |

同一个网络可以同时是“局域网、星形拓扑、交换式 Ethernet、专用网络”。这些词不是互斥答案。

### 分层：把复杂协作切成稳定责任

分层同时存在两种方向：

```text
横向：同层实体按 protocol 解释彼此的 PDU
纵向：下层经 interface 向上层提供 service
```

- **协议 Protocol**：对等实体之间交换报文时必须共同遵守的格式、语义和次序；
- **服务 Service**：下层向上层承诺“能做什么”，不暴露全部实现；
- **接口 Interface**：相邻层调用服务的位置与操作边界；
- **SDU**：上层交给本层处理的数据；
- **PDU**：本层给 SDU 加入本层控制信息后形成的协议数据单元。

发送端执行 `上层 SDU -> 加本层控制信息 -> 本层 PDU -> 作为下层 SDU`；接收端反向解释。这里的箭头表示封装关系，不表示每层都与远端建立物理连接。

### OSI 与 TCP/IP：责任地图，不是两套物理网络

| OSI 参考模型 | TCP/IP 常用映射 | 主要责任 | 典型对象 / PDU |
|---|---|---|---|
| Application / Presentation / Session | Application | 应用语义、表示与会话组织 | message |
| Transport | Transport | process 间复用、可靠性与端到端状态 | segment / datagram |
| Network | Internet | 跨网络寻址、路由与逐包转发 | packet / datagram |
| Data Link | Link / Network Access | 当前链路的成帧、访问与一跳交付 | frame |
| Physical | Link 的物理实现 | bit 的信号表示与传播 | bit / signal |

OSI 是七层参考模型；Internet 协议族的工程分层通常把 OSI 的上三层合入 Application，并把 Data Link 与 Physical 视为 Link/Network Access 的不同实现责任。教材使用“五层模型”时，是为分析方便重新展开 Physical 与 Data Link，不表示出现了第三套协议族。

判断一道分层题时不要只背协议名，先问：当前控制信息由哪一层解释？状态由谁持有？当前对象是 message、segment、packet、frame 还是 signal？

## 旧 Deep Map / Source

[网络统一总图旧稿](00_网络统一总图/README.md)保留作用域、封装、状态所有者和概念边界的详细展开，可继续作为已完成 Source Diff 的历史证据；六类生成约束已迁入本 README，当前唯一 Subject Atlas Owner 仍是本 README。

## 八个核心 Topic

| Topic | 唯一母问题 | 规划 Owner |
|---|---|---|
| [通信基础与网络性能](01_通信基础与网络性能/README.md) | bit 穿过有限信道需要付出什么时间和容量代价？ | signal/symbol/bit、delay、throughput、BDP、switching、media |
| [单跳交付](02_单跳交付_帧_MAC_局域网与交换机/README.md) | 相邻节点怎样组织 frame、共享介质并完成一跳交付？ | framing、error control、MAC、Ethernet/WLAN/VLAN/PPP、switch table |
| [可靠传输](03_可靠传输_序号_ACK_定时器与滑动窗口/README.md) | 不可靠信道怎样通过端点状态机表现为可靠服务？ | Seq、ACK、Timer、Retransmission、Window、Stop-and-Wait、GBN、SR |
| [IP 地址、子网与分组转发](04_IP地址_子网与分组转发/README.md) | 巨大异构网络中 packet 的下一跳去哪？ | IPv4/IPv6、CIDR、router/FIB/LPM、TTL/MTU、ARP、DHCP、ICMP、NAT、multicast、Mobile IP |
| [路由](05_路由_分布式知识与控制平面/README.md) | 没有全局即时状态时，转发表从哪里来？ | DV/LS/path-vector、RIP/OSPF/BGP、RIB/FIB install、convergence、SDN；Canonical 候选已发布 |
| [传输层、UDP 与 TCP](06_传输层_端点_UDP与TCP状态机/README.md) | host 通信怎样变成 process 间有状态通信？ | ports、UDP/TCP headers、multiplexing、connection/sequence state、flow control |
| [拥塞控制](07_拥塞_共享资源与反馈控制/README.md) | 共享网络怎样通过反馈避免 offered load 压垮容量？ | congestion signal、cwnd、slow start、AIMD、avoidance、fast recovery 教材模型 |
| [应用层服务语义](08_应用层_DNS_HTTP与服务语义/README.md) | 端到端通信能力怎样成为可发现、可解释的服务？ | DNS、HTTP semantics、C/S、P2P、FTP、SMTP、POP3、MIME |

目录为 `01_` 到 `08_`。八册均已由旧 README Source 完成逐项迁入 `.tex` 并发布；“候选”表示仍需题目验证心智模型，不表示正文缺失或存在第二个 Owner。

## 已锁定 Ownership

| 概念 | Canonical Owner | 其他位置怎样使用 |
|---|---|---|
| Sliding Window | 可靠传输 | TCP 只解释自己的实例化和参数语义 |
| Flow Control | Transport/TCP | 拥塞册只与 `cwnd` 比较，不重定义 receiver constraint |
| Congestion Control | 拥塞专题 | TCP 册提供最小接口和链接 |
| ARP | IP 转发 | 单跳册只解释取得 MAC 后 frame 怎样交付 |
| Switch Table | 单跳交付 | 综合册只调用 source learning/destination forwarding |
| FIB 的使用 | IP 转发 | 对当前 packet 执行 LPM 和 next-hop action |
| RIB 选择与 FIB 安装 | 路由专题 | 解释 distributed knowledge 怎样形成候选、选择并安装 forwarding state |
| DNS | 应用层 | 综合册只调用 Name -> IP |

## 三个必须反复区分的关系

### 名字与交付

$$
\text{Domain Name}
\to \text{Destination IP}
\to \text{Next-hop IP}
\to \text{MAC}
\to \text{Signal}
$$

Domain、IP、MAC 和 Port 不是同一种名字。无 NAT 等中间机制时，目的 IP 通常保持端到端语义；目的 MAC 随每一跳重新封装。

### 转发与路由

$$
\text{Routing/Control Plane}
\to \text{Forwarding State}
$$

$$
\text{Forwarding/Data Plane}
\to \text{Apply State to Packet}
$$

### 可靠、流控与拥塞

- Reliability：数据是否正确、完整、有序到达；
- Flow Control：receiver 是否接得住，典型约束为 `rwnd`；
- Congestion Control：network path 是否扛得住，典型约束为 `cwnd`。

$$
W_{send}=\min(rwnd,cwnd)
$$

### 其他核心分流边界

| 不能混用 | 判据 |
|---|---|
| Name / IP / MAC / Port | 分别服务应用命名、网络层定位、当前链路交付和主机内端点分用 |
| Transmission / Propagation Delay | `L/R` 由数据量与发送速率决定；`D/v` 由距离与传播速度决定 |
| Connection / Physical Path | TCP connection 是端点维护的逻辑状态；中间物理路径可变化且普通路由器不保存该连接状态 |
| Link / End-to-End Reliability | 一跳修复与两个端点之间的服务语义属于不同 Scope，即使都使用 ACK/重传也不能合并 |
| TCP State / Router State | seq/window 由端点拥有；prefix/next-hop 由路由或转发组件拥有 |
| Layering / Physical Law | 分层是责任与接口地图；middlebox、offload 等实现可跨层，但分析仍需先明确 Scope 和 Owner |

## Internal Bridge

网络内部建立六座稳定接口：

- [NET-B01｜IP Forwarding × Single-Hop Delivery](50_科内桥梁/NET-B01_IPForwarding与SingleHop/README.md)；
- [NET-B02｜Routing × Forwarding](50_科内桥梁/NET-B02_Routing与Forwarding/README.md)；
- [NET-B03｜Reliable Transfer × TCP](50_科内桥梁/NET-B03_ReliableTransfer与TCP/README.md)；
- [NET-B04｜Flow Control × Congestion Control](50_科内桥梁/NET-B04_FlowControl与CongestionControl/README.md)。
- [NET-B05｜BDP × Window](50_科内桥梁/NET-B05_BDP与Window/README.md)；
- [NET-B06｜MTU × Segmentation](50_科内桥梁/NET-B06_MTU与Segmentation/README.md)。

RIP、OSPF、BGP、PPP 都是 Topic 内的协议机制；协议细节多不等于存在跨 Owner 的稳定接口，因此不各自建立 Bridge。

Graph Algorithm × Routing 当前只作为 Routing Topic 对数据结构图算法的 `Use / Candidate Connection`，不因为 Dijkstra/Bellman-Ford 类比漂亮就建立 Cross-Subject Core Bridge。

## Integration

Canonical product：[NET-I01｜一个网络请求的一生](60_综合专题/NET-I01_一个网络请求的一生/README.md)，已发布阅读版。

它只追踪：

```text
URL
-> DHCP（若尚未配置）
-> DNS
-> Same Subnet?
-> Gateway / ARP
-> Ethernet / Switch
-> Router / LPM / Re-encapsulation
-> TCP State
-> HTTP Request/Response
```

同时维护 Name/Address、Encapsulation、Distributed State 和 Scope 四条轨迹，不重写任何协议机制。

## Cross-Subject Bridge

`Process / Socket × Transport Endpoint` 已确认为真实 OS ↔ Network 接口，但当前状态为 **Candidate Core**：结构成立，是否作为 408 核心独立 Bridge 的优先级还需真题/覆盖证据。工程化的完整 kernel stack / NIC 路径只作 Extension。

全局入口见 [408 Cross-Subject Bridge Atlas](../50_桥梁专题/README.md)。

## Question Control Adapter：网络八问

1. 当前作用域是一跳、端到端、一个 AS 还是全球 Internet？
2. 当前通信对象是 process、host、switch、router 还是 application？
3. 当前使用 domain、IP、MAC、port 中哪一种名字？
4. 当前状态由 endpoint、switch、router 还是 name server 持有？
5. 什么事件发生？
6. 状态、报文头和封装怎样变化？
7. 反馈信号是什么？
8. 时间、带宽、队列、丢包或状态成本是什么？

规则入口：[网络做题规则](90_做题规则/README.md)。

## 学习入口

机制生成顺序：

```text
00 -> 01 -> 02 -> 04 -> 05 -> 03 -> 06 -> 07 -> 08 -> Integration
```

课程同步顺序也允许：

```text
01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08
```

Atlas 必须支持两种入口，不把编号误当作唯一认知顺序。

## 来源分层

- 考试范围：当年官方考试大纲为最终依据；用户提供的新东方转载只作临时覆盖检查；
- TCP 工程语义：[RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html)；
- HTTP 语义：[RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)；
- DNS 概念：[RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html)。

RFC 用于校正机制边界，不要求把工程细节全部写入 408 核心册。
