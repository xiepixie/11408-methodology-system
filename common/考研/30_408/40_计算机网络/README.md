# 计算机网络驾驶舱

当前状态：框架已采用，专题正文待建。

## 学科母问题

计算机网络研究：在机器彼此独立、链路有限、传输有时延、数据可能丢失、资源需要共享、系统没有全局即时状态的条件下，怎样让不同机器上的进程完成通信。

网络不是协议字段集合，而是分布式状态机：

$$
\text{Scope}
\to \text{State}
\to \text{Event}
\to \text{Transition}
\to \text{Feedback}
\to \text{Cost}
$$

## Atlas

[网络统一总图](00_网络统一总图/README.md)负责六个根本矛盾、作用域、封装、命名交付链和八个 Topic 的导航。

## 八个核心 Topic

| Topic | 唯一母问题 | 规划 Owner |
|---|---|---|
| [通信基础与网络性能](01_通信基础与网络性能/README.md) | bit 穿过有限信道需要付出什么时间和容量代价？ | signal/symbol/bit、delay、throughput、BDP、switching、media |
| [单跳交付](02_单跳交付_帧_MAC_局域网与交换机/README.md) | 相邻节点怎样组织 frame、共享介质并完成一跳交付？ | framing、error detection、MAC、Ethernet/WLAN/VLAN、switch table |
| [可靠传输](03_可靠传输_序号_ACK_定时器与滑动窗口/README.md) | 不可靠信道怎样通过端点状态机表现为可靠服务？ | Seq、ACK、Timer、Retransmission、Window、Stop-and-Wait、GBN、SR |
| [IP 地址、子网与分组转发](04_IP地址_子网与分组转发/README.md) | 巨大异构网络中 packet 的下一跳去哪？ | IPv4/IPv6、CIDR、LPM、forwarding、TTL/MTU、ARP、DHCP、ICMP、NAT |
| [路由](05_路由_分布式知识与控制平面/README.md) | 没有全局即时状态时，转发表从哪里来？ | DV/LS、RIP/OSPF/BGP、AS、convergence、control plane |
| [传输层、UDP 与 TCP](06_传输层_端点_UDP与TCP状态机/README.md) | host 通信怎样变成 process 间有状态通信？ | ports、multiplexing、UDP、TCP connection/sequence state、flow control |
| [拥塞控制](07_拥塞_共享资源与反馈控制/README.md) | 共享网络怎样通过反馈避免 offered load 压垮容量？ | congestion signal、cwnd、slow start、AIMD、avoidance、fast recovery 教材模型 |
| [应用层服务语义](08_应用层_DNS_HTTP与服务语义/README.md) | 端到端通信能力怎样成为可发现、可解释的服务？ | DNS、HTTP semantics、C/S、P2P、FTP、SMTP、POP3、MIME |

规划目录为 `01_` 到 `08_`。开始写正文时再创建 Topic 文件。

## 已锁定 Ownership

| 概念 | Canonical Owner | 其他位置怎样使用 |
|---|---|---|
| Sliding Window | 可靠传输 | TCP 只解释自己的实例化和参数语义 |
| Flow Control | Transport/TCP | 拥塞册只与 `cwnd` 比较，不重定义 receiver constraint |
| Congestion Control | 拥塞专题 | TCP 册提供最小接口和链接 |
| ARP | IP 转发 | 单跳册只解释取得 MAC 后 frame 怎样交付 |
| Switch Table | 单跳交付 | 综合册只调用 source learning/destination forwarding |
| Routing Table 的使用 | IP 转发 | 执行 LPM 和 next-hop lookup |
| Routing Table 的生成 | 路由专题 | 解释 distributed knowledge 怎样形成 forwarding state |
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

## Integration

规划产品：[《一个网络请求的一生：从域名到网页返回》](60_综合专题/README.md)。

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

## 跨学科 Bridge

`OS x Network：Socket、网络栈、中断与进程` 放在全局 [跨学科 Bridge](../50_桥梁专题/408%20跨学科%20Bridge.md)，因为它同时依赖 OS 和 Network Owner。

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
