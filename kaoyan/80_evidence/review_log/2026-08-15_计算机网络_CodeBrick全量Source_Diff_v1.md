# 计算机网络 CodeBrick 全量 Source Diff v1

日期：2026-08-15  
类型：Source Diff / Import Evidence  
来源：[../../sources/codebrick_408/04_计算机网络_CN](../../sources/codebrick_408/04_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C_CN)

## 1. 盘点事实

外部目录实际包含 58 篇专题 Markdown，另有 1 篇学科导航文件，共 59 个 Markdown 文件。外部总索引写作“58 篇”，与文件系统统计相差 1；差异来自导航文件是否计入，暂不修改外部来源。

| 模块 | 文件数 | 主要内容 | 首要去向 |
|---|---:|---|---|
| `overview` | 4 | 网络概述、分层体系、性能坐标、封装与逐跳旅程 | Subject Atlas Foundation、NET01、NET-I01 |
| `physical` | 7 | 信号/码元、调制编码、介质、复用、极限速率、物理设备 | NET01 |
| `datalink` | 17 | framing、检错纠错、MAC、Ethernet/WLAN/VLAN/PPP/HDLC、ARQ | NET02；ARQ 状态机转入 NET03 |
| `network` | 16 | IP 编址/首部/分片、ARP/ICMP/NAT/IPv6/多播/Mobile IP、转发、路由协议、SDN | NET04、NET05 |
| `transport` | 8 | UDP、TCP 首部/连接/可靠性/流控/拥塞控制与计算题 | NET06、NET07；可靠传输调用 NET03 |
| `application` | 6 | C/S/P2P、DNS、WWW/HTTP、FTP、邮件、DHCP | NET08；DHCP 配置机制转入 NET04 |

## 2. 统一吸收骨架

CodeBrick 采用“一篇一个考点”的原子化组织；Canonical Handbook 仍以网络协议分层心智模型为骨架：

```text
Scope
-> Object / PDU
-> Name / State Owner
-> Event
-> Transition / Encapsulation
-> Feedback
-> Cost / Stop Boundary
```

吸收不等于复制。每一篇 Source 都必须拆成以下可核销原子：

1. 定义与对象；
2. 机制生成链；
3. 字段、公式与计算口径；
4. 正常状态轨迹与异常分支；
5. 不变量、边界、反例与易混点；
6. Worked Example 与独立校验；
7. 考纲/题目信号；
8. 真题链接只保留为 Evidence，不成为知识 Owner。

正文核销状态使用：`Covered`、`Expanded`、`Partial`、`Missing`、`Extension`。本 v1 先锁定 Owner；只有逐篇语义 Diff 并写回 Canonical `.tex` 后，才可标记 `Covered/Expanded`。

## 3. 逐文件 Owner 路由

### 3.1 Overview

| Source | Canonical Owner | 拆分与核销要求 |
|---|---|---|
| `overview/network-overview.md` | NET01；分类坐标最小摘要进 Subject Atlas | 三种交换、分类轴、性能指标；Atlas 不展开计算 |
| `overview/architecture.md` | Subject Atlas Foundation；逐层机制由 NET01/02/04/06/08 Own | OSI/TCP-IP、PDU/SDU/PCI、服务/协议/接口、封装开销、设备层级 |
| `overview/performance-metrics.md` | NET01；BDP×Window 调用 NET-B05 | 四时延、RTT、吞吐、利用率、BDP 两种口径与卫星链路算例 |
| `overview/packet-journey.md` | NET-I01；局部规则由 NET02/04/06 Own | 封装/解封装、设备处理层级、IP 与 MAC 逐跳变化、三级分用 |

### 3.2 Physical

| Source | Canonical Owner | 必须吸收的原子 |
|---|---|---|
| `physical/channel-basics.md` | NET01 | 信道/链路/电路、单工半双工全双工、码元与 bit、波特率、调制、QAM、PCM |
| `physical/encoding.md` | NET01 | NRZ/RZ/Manchester/Differential Manchester/NRZI、波形互译、带宽代价 |
| `physical/multiplexing.md` | NET01 | FDM/TDM/STDM/WDM/CDM、保护频带、125us TDM 帧、T1、复用与多址边界 |
| `physical/nyquist-shannon.md` | NET01 | 奈奎斯特/香农前提、2W 与 `+1`、dB、联合上界与反推 |
| `physical/cdma.md` | NET01 | 正交码片、发送 0 的反码语义、内积解码、叠加、扩频代价与反向验算 |
| `physical/transmission-media.md` | NET01 | 双绞/同轴/光纤/无线、全反射、单模多模、卫星时延、物理接口四特性 |
| `physical/physical-devices.md` | NET01 | Repeater/Hub、级联边界、共享带宽、半双工、冲突域/广播域最小接口 |

### 3.3 Data Link

| Source | Canonical Owner | 必须吸收的原子 |
|---|---|---|
| `datalink/framing.md` | NET02 | 链路/数据链路/帧、服务类型、MTU、字符计数/字节填充/零比特填充/违规编码 |
| `datalink/error-detection.md` | NET02 | 差错分类、奇偶、CRC 多项式/模二除法/FCS/检错能力与不足位补零 |
| `datalink/hamming-code.md` | NET02 | 码距、`2^r >= k+r+1`、校验位位置、校正因子、扩展海明码与能力边界 |
| `datalink/aloha.md` | NET02 | Pure/Slotted ALOHA、易受攻击时间、`S=Ge^{-2G}`/`Ge^{-G}`、峰值与反推 |
| `datalink/csma-cd.md` | NET02 | `2tau`、最小帧长、JAM、截断二进制退避、参数 `a` 与利用率 |
| `datalink/csma-ca.md` | NET02 | hidden/exposed、DCF、IFS、backoff freeze、RTS/CTS、NAV 与代价判断 |
| `datalink/token-passing.md` | NET02 | 令牌生命周期、释放时机、环时延/bit 容量、最坏等待、维护失败 |
| `datalink/ethernet.md` | NET02 | LAN/LLC/MAC/802、MAC 位语义、帧字段与两笔帧长账、冲突域/广播域 |
| `datalink/switch-learning.md` | NET02 | 自学习、过滤/转发/泛洪、老化、交换结构、STP 与逐帧表演化 |
| `datalink/vlan.md` | NET02 | VLAN 划分、802.1Q、Access/Trunk、tag 生命周期、跨 VLAN Stop Boundary |
| `datalink/wireless-lan.md` | NET02 | BSS/ESS、DCF/PCF、802.11 首部/四地址、完整 RTS/CTS 时序 |
| `datalink/ppp.md` | NET02 | WAN 边界、PPP 三组件/帧/透明传输、LCP→NCP 状态机与限制 |
| `datalink/hdlc.md` | NET02 | 站/方式最小范围、I/S/U 帧、零比特填充、与 PPP 的可靠性边界 |
| `datalink/stop-and-wait.md` | NET03 | 四种异常分支、1-bit 序号、timeout、利用率与 ACK/处理时延口径 |
| `datalink/gbn.md` | NET03 | 累积 ACK、丢弃乱序、`W_T <= 2^n-1`、单 timer、回退重传与利用率 |
| `datalink/sr.md` | NET03 | 逐个 ACK、乱序缓存、`W_T+W_R <= 2^n`、窗口歧义反例与成本 |
| `datalink/sliding-window-compare.md` | NET03；TCP 差异由 NET-B03 接口 | 发送窗口四区、三协议统一约束、满载条件、同一丢帧场景对照 |

### 3.4 Network Layer

| Source | Canonical Owner | 必须吸收的原子 |
|---|---|---|
| `network/network-layer-functions.md` | NET04；路由状态生成转入 NET05 | 异构互联、数据报/虚电路、路由与转发分工、分层路由 |
| `network/ip-addressing.md` | NET04 | 分类编址、子网、CIDR、掩码/前缀、地址块合法性、聚合与反推 |
| `network/ip-datagram.md` | NET04 | IPv4 首部逐字段、IHL/总长/校验和、TTL/Protocol、选项与开销 |
| `network/ip-fragment.md` | NET04；尺寸交接调用 NET-B06 | MTU、DF/MF/offset、8-byte 口径、逐片长度、重装与二次分片 |
| `network/arp.md` | NET04；逐跳交接调用 NET-B01 | 同网/跨网四场景、广播请求/单播应答、cache 生命周期与欺骗边界 |
| `network/icmp.md` | NET04 | 差错/询问报文、禁止发送 ICMP 的条件、ping/traceroute 与失败反馈边界 |
| `network/nat.md` | NET04 | NAT/NAPT 映射、端口改写、出站建表/返回匹配、端到端语义代价 |
| `network/ipv6.md` | NET04 | 地址压缩/还原、首部、扩展首部、ND、fragment responsibility、过渡机制 |
| `network/multicast.md` | NET04；分发树算法只作 NET05 Use | IPv4 多播地址、IGMP 成员关系、组播 MAC 映射、RPF/剪枝最小接口 |
| `network/mobile-ip.md` | NET04 | home/foreign agent、care-of address、registration、tunneling、triangle routing |
| `network/router.md` | NET04；RIB/FIB 交接调用 NET-B02 | 输入/交换结构/输出、排队丢包、线速、LPM、路由表/转发表 |
| `network/routing-algorithms.md` | NET05 | 静态/动态、DV/LS/path-vector、Bellman-Ford/Dijkstra、层次与收敛失败 |
| `network/rip.md` | NET05 | hop 口径、三条更新规则、下一跳同源无条件更新、16、防环与坏消息慢 |
| `network/ospf.md` | NET05 | LSA flooding、LSDB/SPF、area、报文、邻居/邻接、DR/BDR 与数量计算 |
| `network/bgp.md` | NET05 | policy/scale、AS-PATH 防环、递归 next-hop、eBGP/iBGP、消息与选路边界 |
| `network/sdn.md` | NET05 | 三层架构、north/southbound、OpenFlow match/action、table-miss、流表边界 |

### 3.5 Transport

| Source | Canonical Owner | 必须吸收的原子 |
|---|---|---|
| `transport/tcp-vs-udp.md` | NET06 | host→process、port 分类、TCP/UDP 分用键、socket/connection、message/byte stream |
| `transport/udp.md` | NET06 | UDP 特性/首部、伪首部 checksum 完整计算、端口不存在与 ICMP、应用可靠性 |
| `transport/tcp-basics.md` | NET06 | TCP 五特征、首部字段、flags、seq/ack、MSS、window scale/timestamp、四元组 |
| `transport/tcp-connection.md` | NET06 | 三次握手、四次挥手、half-close、TIME-WAIT/2MSL、timer、十一状态与同时开关 |
| `transport/tcp-reliable.md` | NET06；通用机制调用 NET03/NET-B03 | byte sequence、累计 ACK、发送窗口三边界、RTO/RTTS/Karn/SACK 与丢包判据 |
| `transport/tcp-flow-control.md` | NET06；与拥塞交接调用 NET-B04 | rwnd、zero window/probe、Nagle、糊涂窗口、`min(cwnd,rwnd)` 与吞吐上界 |
| `transport/tcp-congestion.md` | NET07 | 拥塞生成、信号、slow start/CA/fast retransmit/recovery、AIMD、Tahoe/Reno |
| `transport/tcp-congestion-detail.md` | NET07 | 轮次口径、阈值相等/越过、逐轮表、累计发送量、曲线反推与四类自检 |

### 3.6 Application

| Source | Canonical Owner | 必须吸收的原子 |
|---|---|---|
| `application/app-model.md` | NET08 | C/S 三重不对称、瓶颈公式、P2P 自扩展分发时间/反例与定位方式 |
| `application/dns.md` | NET08 | 域名/区、服务器角色、recursive/iterative、8 步与时延、cache、RR、transport |
| `application/www.md` | NET08 | WWW/Internet、URL/URI、超文本、静态/动态、完整工作流 |
| `application/http.md` | NET08 | method/message/status、stateless/connection、RTT 计数、版本、cache/conditional GET/cookie |
| `application/email.md` | NET08 | UA/server、SMTP 三阶段、message/envelope、MIME、POP3/IMAP/Webmail 与路径计数 |
| `application/ftp-dhcp.md` | FTP→NET08；DHCP→NET04 | FTP 控制/数据、active/passive/TFTP；DHCP UDP/DORA/lease/relay |

## 4. Owner 压力与防重复边界

- 链路层目录中的 Stop-and-Wait、GBN、SR 是 NET03 的可靠传输机制；NET02 只说明链路层为何可能调用可靠服务。
- CRC/Hamming 属于 NET02 的帧级差错控制；UDP/TCP checksum 属于 NET06，IP header checksum 属于 NET04。算法相似不能合并 Owner。
- Router 的 packet action、IPv4/IPv6、ARP、ICMP、NAT 归 NET04；RIP/OSPF/BGP/SDN 怎样生成状态归 NET05。
- TCP reliable 的实例细节归 NET06；通用 Seq/ACK/Timer/Window 理论归 NET03；两者交接归 NET-B03。
- TCP flow control 归 NET06，congestion control 归 NET07，发送额度的组合接口归 NET-B04。
- DHCP 虽位于外部 `application/ftp-dhcp.md`，但它拥有主机进入 IP 作用域的配置生命周期，归 NET04；FTP 归 NET08。
- `packet-journey.md` 只进入 NET-I01 的组合轨迹，不能在 Integration 重新定义各层机制。
- CodeBrick 的真题链接与站内交互组件是 Evidence/Source 线索；除非题面已被本地保存并核验，不能据链接宣称模型已通过验证。

## 5. 本轮 Canonical Update 顺序

1. NET01：吸收全部 Physical 与性能计算口径，建立 bit/signal 生成链。
2. NET02：吸收 framing、检错纠错、MAC、LAN/WAN 协议与逐帧状态。
3. NET03：吸收三种 ARQ 的完整双端状态机、窗口歧义反例与利用率。
4. NET04：吸收 IP 编址/首部/分片、辅助协议、NAT、IPv6、Multicast、Mobile IP。
5. NET05：吸收 DV/LS/path-vector、RIP/OSPF/BGP/SDN 的报文与收敛细节。
6. NET06：吸收 UDP/TCP 字段、连接、可靠性、RTO、流控与边界。
7. NET07：吸收拥塞模型、Tahoe/Reno 逐轮计算与口径自检。
8. NET08：吸收应用模型、DNS/WWW/HTTP/FTP/邮件的消息轨迹和时延计算。
9. NET-I01：只核销 `packet-journey.md` 的跨层轨迹，不复制局部机制。
10. Coverage Appendix：每册保留逐 Source/考纲映射，证明 58 篇正文均已被核销。

当前记录证明 58 篇 Source 已被逐文件定位并分流，不证明正文已经完成全量语义吸收，也不证明心智模型已经通过陌生题验证。每册扩充后必须重新发布受影响 `.tex`，并运行 `progress --write`、`check`、`audit`。
