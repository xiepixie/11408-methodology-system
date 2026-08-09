# 一个网络请求的一生：从 URL 到可解释的响应

状态：工作稿，待人工确认。

## 0. 本册定位

本 Integration 追踪一个典型 Web request 怎样依次调用 application、transport、network、link 和 physical mechanisms。

本册只拥有协作顺序、状态交接、Fast/Slow Path 和失败分支；各机制的定义仍归对应 Topic。为保持轨迹清晰，母例先采用“IPv4 + Ethernet/WLAN + TCP + HTTP/1.1/2 风格 transport”路径，HTTP/3、IPv6、proxy、CDN、TLS 细节在边界处标明，不强行塞入主路径。

## 1. 初始状态与结束状态

### 初始状态

用户输入 `https://www.example.test/index.html`。浏览器拥有 URL，但以下状态可能存在或缺失：

- host 是否已有 IP/prefix/default gateway/DNS server；
- DNS/cache 是否已有 destination address；
- route/ARP cache 是否已有 next-hop mapping；
- 是否已有可复用 transport/security connection；
- HTTP cache 是否已有 fresh representation。

### 结束状态

浏览器收到并解释 HTTP response，对 representation 做缓存/渲染处理；transport 更新 ACK/window/congestion state；各层软状态在 TTL、lease、aging 或 connection lifetime 内继续存在。

“请求完成”不等于所有状态销毁。

## 2. 四条必须并行维护的轨迹

| 轨迹 | 起点 | 过程 | 终点/持续状态 |
|---|---|---|---|
| Name/Address | URL/domain | DNS -> destination IP -> next-hop IP -> MAC | resource/endpoint identity |
| Encapsulation | HTTP message | TCP bytes -> IP packet -> frame -> signal | 远端逐层解封装 |
| State | caches/config | lease、DNS cache、ARP table、switch table、route、TCP state | 更新、老化或释放 |
| Scope | application | global naming -> end-to-end -> per-hop -> physical | 反向恢复 application semantics |

任何一步只沿一条轨迹叙述都会丢失关键交接。

## 3. Phase A：先检查是否需要网络

浏览器根据 HTTP cache/freshness 判断目标 representation 是否可直接复用。

```text
fresh cache hit?
├─ yes: use cached representation; network main path may stop
└─ no: resolve/revalidate/fetch
```

这是第一个 Fast Path。它说明 application state 可以让整个下层过程不发生。

Owner：[应用层](../08_应用层_DNS_HTTP与服务语义/README.md)。

## 4. Phase B：主机先获得网络身份与出口配置

若 host 尚无有效配置，它需要 DHCP 等 bootstrap 过程取得：

- local IP address；
- subnet prefix/mask；
- default gateway；
- DNS resolver；
- lease lifetime。

初始 client 尚无稳定 IP，因此 DISCOVER/OFFER/REQUEST/ACK 可能使用本地广播。完成后 host 才具备判断 same subnet 和发起普通 IP forwarding 的基础状态。

```text
valid lease/config?
├─ yes: reuse
└─ no: DHCP state machine -> install local config
```

Owner：[IP 地址与分组转发](../04_IP地址_子网与分组转发/README.md)。

## 5. Phase C：Domain name 变成 destination IP

浏览器/OS 先检查本地和 resolver cache：

```text
DNS cache hit within TTL?
├─ yes: return cached record
└─ no: recursive resolver follows referrals to authority
```

cache miss 时，resolver 可能从 root 得到 TLD referral，再从 TLD 得到 authoritative server referral，最后取得 A/AAAA 等 record。返回值给出 destination IP 候选，却不告诉主机当前链路应该使用哪个 MAC，也不提供逐跳 route。

Owner：[应用层 DNS](../08_应用层_DNS_HTTP与服务语义/README.md)。

## 6. Phase D：Destination IP 变成当前 next hop

host 用 local prefix 做 same-subnet 判断：

```text
destination IP in local subnet?
├─ yes: next-hop IP = destination IP
└─ no:  route lookup -> next-hop IP = gateway/selected router
```

然后查询 ARP/neighbor cache：

```text
next-hop mapping cached?
├─ yes: reuse MAC
└─ no: local ARP request -> reply -> cache mapping
```

关键交接：DNS 的 destination IP 被保存进 packet；ARP 解析的是 next-hop IP，结果进入当前 frame 的 destination MAC。

Owner：[IP 转发/ARP](../04_IP地址_子网与分组转发/README.md)。

## 7. Phase E：当前广播域完成第一跳交付

host 构造 frame：

```text
Dst MAC = next-hop MAC
Src MAC = host interface MAC
Payload = IP packet
```

若经过 Ethernet switch：

1. switch 从 source MAC 学习 ingress port；
2. 按 destination MAC 查 table；
3. 命中则定向转发，未知则在 VLAN 内泛洪；
4. frame 到达 gateway interface。

若是 WLAN，发送前还需执行相应介质访问与 ACK/退避逻辑。物理层负责把 frame 表示成 signal，承担 transmission/propagation cost。

Owners：[单跳交付](../02_单跳交付_帧_MAC_局域网与交换机/README.md)、[通信基础](../01_通信基础与网络性能/README.md)。

## 8. Phase F：每个 router 重复局部 forwarding

router 收到 frame 后：

```text
strip incoming L2 frame
-> inspect destination IP
-> decrement TTL / update IPv4 header checksum
-> LPM in forwarding table
-> choose next hop + output interface
-> handle MTU constraint
-> resolve/reuse output-link address
-> create new L2 frame
```

router 使用的 forwarding table 早已由 routing control plane 生成。OSPF/RIP/BGP/SDN 等不必为当前 packet 临时计算整条路径；它们在更慢时间尺度上维护 state。

Owners：[IP Forwarding](../04_IP地址_子网与分组转发/README.md)、[Routing](../05_路由_分布式知识与控制平面/README.md)。

### 8.1 每跳保持与改变

| 对象 | 通常保持 | 每跳改变 |
|---|---|---|
| Application target | URL/resource semantics | 通常不参与 router 处理 |
| TCP connection identity | endpoint pair（无 NAT 时） | sequence/window 随事件更新，不按 router 改 |
| IP packet | source/destination IP（无 NAT/tunnel 时） | TTL、IPv4 checksum，可能 fragment |
| Link frame | 无 | source/destination MAC、FCS、link format |
| Signal | 无 | 每条介质重新编码/发送 |

NAT、tunnel、proxy 等会改变这张表的前提，必须显式加入 middlebox state，不能继续声称 IP/transport tuple 恒定。

## 9. Phase G：建立 transport 与 security context

若没有可复用 connection，TCP 双方同步 initial sequence spaces：

```text
client SYN
-> server SYN+ACK
-> client ACK
-> ESTABLISHED at both endpoints
```

随后若使用 TLS，还会进行身份验证、密钥协商和安全参数建立。TLS 属于本 Integration 的外部接口：它位于 application semantics 与 transport delivery 之间，但当前网络 Topic 没有独立 Owner，本册不展开 cryptographic mechanism。

HTTP/3 分支使用 QUIC over UDP，把 transport/security/multiplexing 以不同方式组合；HTTP resource/method/status semantics 仍由 Application Topic 拥有。

Owner：[传输层](../06_传输层_端点_UDP与TCP状态机/README.md)。

## 10. Phase H：HTTP request 变成受窗口约束的 bytes

浏览器构造 HTTP request，指定 method、target 和 metadata。TCP 把 byte stream 划入 sequence space 和 segments：

$$
FlightSize\le\min(rwnd,cwnd).
$$

- reliable state 决定哪些 bytes 已 ACK、需要重传或暂不能复用序号；
- `rwnd` 表达 server 接收能力；
- `cwnd` 表达 client sender 对 path congestion 的推断；
- IP 和 link layers 为每个 segment 提供逐跳交付。

Owners：[应用层](../08_应用层_DNS_HTTP与服务语义/README.md)、[传输层](../06_传输层_端点_UDP与TCP状态机/README.md)、[可靠传输](../03_可靠传输_序号_ACK_定时器与滑动窗口/README.md)、[拥塞控制](../07_拥塞_共享资源与反馈控制/README.md)。

## 11. Phase I：server 解释请求并返回 representation

server transport demultiplexes connection to the owning socket/process。HTTP layer 解释 method 与 target，应用生成或选择 representation，并返回 status、metadata 和 content。

response 沿相同层次反向发送，但逐跳 route 和 queue 不必与 request 完全相同。client 收到连续 bytes 后解析 response；HTML 等 representation 可能生成新的依赖图，引发 CSS、JS、image 等后续 requests。

Persistent connection、HTTP multiplexing、DNS/HTTP cache 和 CDN 等会改变后续请求的 Fast Path，但不改变各 Owner 的责任边界。

## 12. Slow Path 与失败路由

| 观察 | 首个应检查的状态/Owner | 可能分支 |
|---|---|---|
| 没有本地 IP | DHCP lease / IP Topic | discover、renew、fail |
| 域名无结果 | resolver/cache/authority / Application | retry、negative answer、alternate record |
| ARP 无应答 | same-subnet/next-hop mapping / IP | gateway/config/link failure |
| frame 校验失败 | Link | discard，依赖上层恢复 |
| router 无匹配 route | Forwarding state / IP+Routing | default route、drop、ICMP |
| TTL 耗尽 | packet life budget / IP | drop + ICMP Time Exceeded |
| packet 超过 MTU | IP version/DF/PMTU | fragment、Packet Too Big、resize |
| SYN 无响应 | endpoint/retransmission/path | retry、timeout、RST |
| receiver 窗口为 0 | `rwnd` / Transport | pause + persist probing |
| congestion signal | `cwnd` / Congestion | reduce rate/retransmit |
| HTTP 4xx/5xx | application semantics | client or server handling |

失败诊断应找到最早没有完成的状态交接，不要从最后的“页面没打开”反推唯一原因。

## 13. 成本怎样累积

总体完成时间不是固定 RTT 倍数。它由以下因素共同决定：

$$
T_{total}=
T_{bootstrap}
+T_{name}
+T_{connect/security}
+T_{request}
+T_{server}
+T_{response}
+T_{dependent\ resources},
$$

其中很多项可因 cache/connection reuse 消失，也可能并行重叠。每个传输阶段又包含 serialization、propagation、processing、queueing 和 retransmission。

性能题应先画依赖 DAG 和时间线，再数不可并行的 critical path。

## 14. 一页压缩

```text
URL/resource
-> [HTTP cache?]
-> host config / DHCP
-> DNS: domain -> destination IP
-> route: destination IP -> next-hop IP
-> ARP: next-hop IP -> MAC
-> frame/signal: one-hop delivery
-> router LPM + new frame, repeated
-> TCP/security context
-> HTTP bytes under reliable/rwnd/cwnd state
-> server operation + response representation
-> caches and connections retain reusable state
```

复原问题：

1. 哪些 cache hit 可以让哪些阶段完全不发生？
2. destination IP、next-hop IP 和 destination MAC 在哪一步产生？
3. forwarding table 是何时、由谁生成的？
4. HTTP request 被发送时同时受哪三套 transport 状态约束？
5. 页面失败时，怎样找第一次未完成的状态交接？

## 15. 人工确认与扩展边界

本工作稿尚需使用者确认母例是否优先采用经典 $\text{DNS} \rightarrow \text{TCP} \rightarrow \text{HTTP}$ 路径。确认后可按需求新增以下分支，但不应重写主干：

- IPv6 Neighbor Discovery 与 Path MTU；
- TLS 1.3 handshake；
- HTTP/3 over QUIC；
- recursive resolver、CDN、reverse proxy 与 load balancer；
- OS x Network 的 socket、system call、NIC interrupt/DMA 路径，该部分应进入全局跨学科 Bridge/Integration。
