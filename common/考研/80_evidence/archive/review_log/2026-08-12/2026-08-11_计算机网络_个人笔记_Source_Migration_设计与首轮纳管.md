# 计算机网络个人笔记 Source Migration 设计与首轮纳管

> 日期：2026-08-11
>
> 性质：Evidence 层 Source Diff / Owner Diff 记录，不是知识 Owner。
>
> 来源一：`学习领域/卡片盒笔记主题索引卡/` 中全部 12 个 `CN-*.md`，共约 1,963 行。
>
> 来源二：`学习领域/归档/408/计算机网络/` 中全部 19 个 Markdown 文件，共约 2,435 行；其中 6 个为空壳。

## 1. 本轮判断与产品边界

本轮先完成 31 份旧来源的全科路由，再按 `CURRENT.md` 建设 NET04 与 NET05。其余六册继续保留现有 Markdown Source，不能因已经读过就宣称完成迁移。

判断顺序为：Knowledge/Control → unique Owner → Canonical/Extension/Rule/Reject → 物理资产 → 状态更新。未经人工确认的正文只标“Canonical 候选”，不标“已采用”。

## 2. 来源攻击后保留的全科心智模型

Subject Atlas 的分布式状态机仍成立，本轮把调用坐标收紧为：

```text
Scope
-> Name / Representation
-> State Owner
-> Event / Transition / Feedback
-> Cost
```

NET04 的生成链为：

```text
Destination IP -> Prefix Scope -> LPM -> Next-hop IP/Interface
-> Link Identity -> New Frame
```

NET05 的生成链为：

```text
Local Observation -> Advertisement -> Knowledge Merge
-> Decision under Objective/Policy -> Install Forwarding State
```

两册以 `RIB candidate/selection -> FIB install -> packet-time LPM` 交接。该接口是本轮 Source Diff 的主要 Canonical Update。

## 3. 卡片盒 12 张主题卡路由

| Source | Owner / 路由 | Diff 结论 |
|---|---|---|
| `CN-移动IP协议.md` | NET04 Extension | 身份—位置分离、binding、anchor/tunnel、triangle routing 保留；HA/FA 与蜂窝核心网组件硬等同 Reject |
| `CN-网络拓扑.md` | Atlas Foundation；NET02/05 Use | 拓扑作用域和冗余关系最小吸收；设备表与路由机制送回各 Owner |
| `CN-软件定义网络SDN.md` | NET05；Rules | logical centralization、reactive/proactive、match-action 进入 Canonical；物理单点/即时最优 Reject |
| `CN-交换技术与分层架构.md` | NET02；Atlas Use | frame/switching、collision/broadcast domain 归 NET02；跨层设备清单不建立第二套 Owner |
| `CN-RIP与OSPF对比.md` | NET05；Rules | DV/LS knowledge representation 和生命周期进入 Canonical；OSPF 永久无环 Reject |
| `CN-边界界定与完整性校验.md` | Atlas / Rules | scope、name type、Owner、invariant 转化为全科调用坐标，不作为协议知识重复拥有 |
| `CN-ARQ自动重传请求.md` | NET03 | Seq/ACK/Timer/Window Source；“默认滑窗=GBN”进入 Reject |
| `CN-网络性能指标.md` | NET01；Rules | delay/throughput/BDP Source；瓶颈速率仅作上界，BDP 非“最大容量” |
| `CN-路由协议.md` | NET05 | DV/LS、控制/数据平面、收敛 Source Pack |
| `CN-网络校验码.md` | NET02；CO01/Extension Note | CRC 检错归 NET02；Hamming/ECC 高级内容不扩张网络 Core；“通过校验=无错误” Reject |
| `CN-边界网关协议BGP.md` | NET05；Rules | path-vector、AS_PATH 防环、policy 进入 Canonical；固定万能选路顺序 Reject |
| `CN-随机访问控制-ALOHA与CSMA.md` | NET02 | ALOHA/CSMA/CD/CA 归单跳交付；不进入 NET04/05 |

## 4. 归档目录 19 个文件路由

| Source | Owner / 路由 | Diff 结论 |
|---|---|---|
| `网络层-IP协议.md` | NET04 | IPv4/IPv6、ARP、ICMP、NAT、fragmentation 主 Source；修正 IPv6 分片责任 |
| `物理层-数据通信基础.md` | NET01 | Empty Source；不产生更新 |
| `物理层-传输媒体与设备.md` | NET01/02/04/05 Split | 介质归 NET01，switch/domain 归 NET02，next hop/NAT 归 NET04，AS routing 归 NET05 |
| `链路层-局域网与广域网.md` | NET02 | Ethernet/WLAN/PPP 等 Source；不重复进入 NET04 |
| `链路层-流量控制与可靠传输.md` | NET03 | Stop-and-Wait/GBN/SR Source |
| `应用层-DNS.md` | NET08 | Empty Source；不产生更新 |
| `网络层-子网划分与路由基础.md` | NET04；Rules | CIDR/VLSM/LPM Source；补充对齐、`/31`/`/32` 边界 |
| `传输层-传输层功能与UDP.md` | NET06 | Empty Source；不产生更新 |
| `应用层-FTP,SMTP,POP3,DHCP.md` | NET08 / NET04 Split | DHCP 配置输出归 NET04；FTP/SMTP/POP3 归 NET08 |
| `传输层-TCP.md` | NET06 | Empty Source；不产生更新 |
| `网络层-SDN.md` | NET05 | SDN Canonical Source；逻辑集中与物理分布明确分层 |
| `物理层-编码与调制.md` | NET01 | encoding/modulation Source；不进入路由/转发 |
| `网络概述.md` | Atlas Foundation / NET01 | 学科范围与 delay/switching 起点；不建立第二 Atlas |
| `公式汇总.md` | NET01/02/03/04/06/07；Rules | Split Source；每个公式送回机制 Owner，并补齐假设和时间线 |
| `网络层-路由协议.md` | NET05 | RIP/OSPF/BGP Source Pack；经 RIB/FIB 与收敛时间轴重构 |
| `术语汇总.md` | Atlas / Rules / 各 Topic | Routing index；术语本身不升级为并列知识 Owner |
| `链路层-介质访问控制（MAC）.md` | NET02 | 随机/受控接入与 CSMA Source |
| `链路层-设备与差错控制.md` | NET02 | Empty Source；不产生更新 |
| `应用层-WWW与HTTP.md` | NET08 | Empty Source；不产生更新 |

## 5. 已明确拒绝进入稳定知识的说法

1. 经过 $N$ 个路由器必然发生固定次数 ARP，或 ARP 能跨路由器解析远端 MAC。
2. 所有子网无条件使用 $2^h-2$，且 `/30` 永远是点到点最优。
3. IPv6 不允许任何分片；准确边界是中间 router 不分片，source 仍可分片。
4. NAT 等于 firewall，或地址改写不需要双向 per-flow state。
5. Mobile IP 的 HA/FA 与 4G/5G 核心网组件存在稳定一一映射。
6. OSPF/Dijkstra 在拓扑变化和 FIB 安装期间也必然无环。
7. BGP 总按固定四步选择最短 AS_PATH，因而得到最低时延/最近路径。
8. SDN controller 必然是单台物理超级计算机、拥有即时一致视图并自动得到全局最优。
9. CRC 检查通过证明传输绝无错误，或检错码自动提供恢复。
10. throughput 必然等于最慢链路速率，BDP 是链路“最大容量”。
11. DNS 永远只用 UDP、HTTP 永远只用 TCP，或 BGP 因 TCP 承载就由应用层语义拥有。

## 6. 本轮 Canonical Update

- 新建并发布 NET04 与 NET05 Canonical LaTeX 候选正文；经统一总图协议流程复核后扩充为 10 页与 9 页。
- 把 NET04 重构为 prefix scope、same-subnet、FIB/LPM、next-hop identity 与逐跳状态生命周期。
- 把 NET05 重构为 observation、advertisement、knowledge merge、policy decision、install 与 convergence。
- 显式建立 RIB candidate/selection、FIB install 和 packet-time LPM 的 Owner 边界。
- Mobile IP 保留为 NET04 Extension；交换、ARQ、性能、TCP、应用层材料送回对应 Topic。
- NET04 补入 IPv4/IPv6 首部、ARP、DHCP、ICMP、分片、NAT 与 ND 的报文/字段流程；NET05 补入 RIP、OSPF、BGP、SDN 的报文与 FSM。
- 新增网络 Candidate Rules 与 Explicit Rejects；未将任何规则标为 adopted。

## 7. 人工决定与下一步

本轮结果是 **Canonical Candidate + Candidate Rules + Explicit Rejects**，不是成熟状态。

下一步最小动作：人工审阅两册 Mother Model 与 RIB/FIB 接口；用真题攻击 LPM、VLSM、fragmentation、DV update、OSPF lifecycle 和 BGP policy Rules；两侧 Owner 通过后再验证 NET-B02 Standalone Promotion，不提前用 Bridge 重复两册正文。其余六册已完成逐册 Source Diff 与 Canonical 迁移，网络全科当前进入题目验证阶段。

## 8. 2026-08-12 完成核销

| 资产 | 结果 | 物理 Owner / 发布状态 |
|---|---|---|
| NET01 通信基础与性能 | Source 全量迁入并补齐编码/调制、交换时序、流水线流程 | `NET-01_通信基础与网络性能_方法论手册.tex`；Published PDF 6 页 |
| NET02 单跳交付 | Source 全量迁入并补齐 framing、CRC、ALOHA/CSMA、交换机/VLAN/PPP 流程 | `NET-02_单跳交付_方法论手册.tex`；Published PDF 6 页 |
| NET03 可靠传输 | Source 全量迁入并补齐 Stop-and-Wait、GBN、SR 状态事件账本 | `NET-03_可靠传输_方法论手册.tex`；Published PDF 7 页 |
| NET06 Transport/TCP | Source 全量迁入并补齐 UDP、握手、数据/ACK、流控、关闭与异常状态 | `NET-06_传输层与TCP_方法论手册.tex`；Published PDF 7 页 |
| NET07 拥塞控制 | Source 全量迁入并补齐慢启动、拥塞避免、超时、重复 ACK、Tahoe/Reno | `NET-07_拥塞控制_方法论手册.tex`；Published PDF 6 页 |
| NET08 应用层 | Source 全量迁入并补齐 DNS、HTTP、FTP、SMTP/POP3/IMAP 服务流程 | `NET-08_应用层服务语义_方法论手册.tex`；Published PDF 7 页 |
| NET-B02 | 在两侧 Topic 就绪后完成 handoff、FIB 版本与失败分支复核 | Canonical Bridge v2；Published PDF 2 页 |
| NET-I01 | 在 Topic/Bridge Owner 就绪后建立组合正文并明确停止边界 | Canonical Integration；Published PDF 4 页 |

本记录的迁移结论已完成；后续网络工作转为真题/陌生题验证，不再把“Source 已读”作为完成标准。
