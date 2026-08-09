# 路由：不完整知识怎样收敛为可用转发状态

状态：工作稿，待人工确认。

## 0. 本册定位

本 Topic 回答：每个 router 只能直接观察局部邻接、消息会延迟或丢失、拓扑还会变化时，网络怎样生成可供 forwarding 使用的状态？

本册拥有 distance vector、link state、path vector、RIP、OSPF、BGP、AS、convergence、control/data plane 边界，以及 SDN 的逻辑集中控制模型。

本册不执行 packet 的 LPM 和逐跳重封装，见[IP 分组转发](../04_IP地址_子网与分组转发/README.md)。算法细节只解释其怎样改变路由知识，不把本册写成纯算法章节。

## 1. 根本问题：网络中没有天然的全局真相副本

router 开机时只知道直连网络。要形成远端可达性，必须经历：

$$
\boxed{
\text{Local observation}
\to \text{Advertisement}
\to \text{Knowledge merge}
\to \text{Path decision}
\to \text{Forwarding state}
}
$$

当链路变化时，这条链必须再次运行。在传播完成前，不同 router 可以拥有不同版本的世界。Routing 的核心不是“求一次最短路”，而是维护一个会变化、可能暂时不一致的分布式知识系统。

## 2. 控制平面与数据平面

```text
Control plane:
topology/reachability messages
-> routing information base / topology database
-> decision process
-> forwarding entries

Data plane:
packet arrives
-> lookup installed forwarding entry
-> execute local action
```

control plane 的时间尺度较慢，处理状态生成和收敛；data plane 对每个 packet 快速执行。两者可以同机实现，也可以在 SDN 中逻辑分离，但职责不能混合。

## 3. 三种知识表示

### 3.1 Distance Vector：邻居告诉我“它离目的多远”

每个节点维护到目的的当前代价，并与邻居交换 vector。Bellman-Ford 形式为：

$$
D_x(y)=\min_{v\in N(x)}\{c(x,v)+D_v(y)\}.
$$

节点不需要全局拓扑，只比较经每个邻居的候选代价。优点是状态和计算简单；问题是节点无法看见邻居通告背后的真实路径，故障信息可能在相互引用中形成 loop 和 count-to-infinity。

### 3.2 Link State：大家同步事实，各自计算结论

每个 router 发布自身邻接与链路代价，信息可靠洪泛后形成 link-state database。若同一区域 router 的 LSDB 一致，它们可各自以自己为根运行 shortest-path algorithm，生成本地 forwarding state。

关键分离是：

$$
\boxed{\text{LSA = topology fact}}
\neq
\boxed{\text{routing table = local decision}}.
$$

优点是知识更完整、故障传播通常更直接；代价是洪泛、数据库、序列/老化管理和 SPF 重算。

### 3.3 Path Vector：跨自治域传播“可达性 + 经历路径 + 属性”

Internet 跨 AS 不是一个统一管理员下的最短路问题。BGP 通告 prefix 及 path attributes，`AS_PATH` 记录可达性经过的 AS 序列，既帮助防环，也为 policy decision 提供输入。

BGP 的选择目标是 policy-compliant reachability，不保证选择全局代价最小路径。商业关系、出口偏好和流量工程可以优先于 hop count。

## 4. RIP：DV 的教材实例

RIP 用 hop count 作为 distance，最大可用距离受限，周期性交换路由信息。一次更新的正确推演是：

```text
receive neighbor vector
-> add cost to neighbor
-> compare with current candidates
-> update next hop/metric when rule permits
-> later advertise local result
```

### 4.1 “坏消息传得慢”怎样生成

链路失效后，邻居可能仍互相通告基于对方的旧可达性。每个局部更新看起来都合法，但信息形成循环依赖，distance 逐步增加到“不可达”。

- split horizon：不要从学到某路由的接口再通告回去；
- poison reverse：向该邻居明确通告为不可达；
- triggered update：变化后尽快通告，而不只等周期。

这些机制都在减少旧知识循环自证，但不能把异步分布式收敛变成瞬时全局一致。

## 5. OSPF：LS 的协议化实现

OSPF 在一个 AS 内运行。它通过 neighbor discovery、adjacency、LSA flooding 和 LSDB synchronization，使区域内 router 获得一致拓扑数据库，再计算 shortest-path tree。

### 5.1 从链路事件到新表项

```text
link state changes
-> router originates newer LSA
-> reliable flooding within scope
-> routers install fresh LSA in LSDB
-> SPF recalculation
-> routes selected and installed
```

序列号、age 与 acknowledgment 用来区分新旧事实并可靠传播；Dijkstra 只是这条生命周期中的 path computation，不拥有邻接和洪泛过程。

### 5.2 Area 为什么出现

单一区域扩张会使每次变化传播到更多 router、每台设备保存更大 LSDB 并更频繁重算。Area 把详细拓扑的洪泛与计算限制在作用域内，由 ABR 在区域间传播摘要/可达性；backbone area 连接区域间路由。

Area 用信息隐藏和层次化换可扩展性，代价是配置、摘要造成的可见性损失与路径选择约束。

## 6. BGP：AS 之间交换可达性承诺

一个 AS 是共同管理与对外路由策略下的一组网络。BGP speaker 通过 TCP connection 与 peer 交换 route information。

核心消息生命周期：

```text
OPEN establishes BGP session
-> KEEPALIVE maintains liveness
-> UPDATE advertises NLRI + path attributes or withdraws routes
-> local policy imports candidates
-> decision process selects route
-> export policy decides what to announce
-> NOTIFICATION reports fatal protocol error and closes session
```

### 6.1 eBGP 与 iBGP 分工

- eBGP 在不同 AS 之间交换外部 reachability；
- iBGP 在同一 AS 内传播外部可达性，使内部 router 能把 traffic 送往选定 egress；
- IGP 仍负责在 AS 内真正到达 BGP next hop。

因此“BGP 选哪个出口”与“OSPF 怎样到该出口”是两个嵌套问题。

### 6.2 AS_PATH 的两种作用

1. 若本 AS 已在 path 中，拒绝该通告以防 AS-level loop；
2. path length 可成为 decision input，但不是唯一、更不是始终最高优先级的策略。

## 7. Convergence：正确性发生在时间轴上

拓扑变化后的状态轨迹通常是：

$$
S_{old}
\xrightarrow{event}
S_{mixed}
\xrightarrow{messages/calculation}
S_{new}.
$$

`S_mixed` 中可能出现 transient loop、black hole 或 suboptimal route。评价 routing protocol 不能只问最终路径是否正确，还要问：

- 变化怎样被发现；
- 新旧消息怎样区分；
- 错误状态传播多远；
- 多久恢复；
- 收敛期间 packet 会怎样失败。

## 8. SDN：逻辑集中，不等于物理单点

传统 router 常把 routing process 与 forwarding hardware 垂直集成。SDN 把控制逻辑抽象到 controller，通过 southbound interface 管理 programmable forwarding state：

$$
\text{Application intent}
\to \text{Controller global view}
\to \text{Match-action rules}
\to \text{Data-plane execution}.
$$

Reactive 模式在 table miss 后向 controller 请求决定；proactive 模式预先安装规则。

必须区分：

- **logically centralized**：应用面对统一控制抽象；
- **physically centralized**：只有一台 controller 实例。

工程 SDN 控制器可以复制、分片和分布部署。逻辑集中换来可编程与全局策略，也带来 controller consistency、rule installation delay、failure handling 和 control-channel cost。

## 9. 概念边界

| 概念 A | ≠ | 概念 B | 真正区别与题目信号 | 混淆后果 |
|---|:---:|---|---|---|
| Routing | ≠ | Forwarding | 前者生成状态；后者使用状态处理 packet | 把 SPF 与 LPM 写成同一步 |
| Advertisement | ≠ | Forwarding entry | 前者是输入知识；后者是本地决策结果 | 认为收到 LSA/DV 就直接照抄表项 |
| Neighbor | ≠ | Next hop | 邻居是协议/链路关系；next hop 是某条选定路由的动作 | 把所有 peer 都当作当前路径 |
| LSDB | ≠ | Routing table | LSDB 描述拓扑；routing table 描述本地最佳动作 | 无法解释每台 router 结论不同 |
| Shortest path | ≠ | Policy path | IGP 常优化 metric；BGP 满足跨域 policy | 用 Dijkstra 解释 BGP 决策 |
| Convergence | ≠ | Instant consistency | 收敛是从旧状态到新状态的过程 | 忽略 transient loop/black hole |
| Logical centralization | ≠ | Physical single controller | 前者是控制抽象；后者是部署选择 | 把 SDN 必然等同单点故障 |
| IGP next-hop reachability | ≠ | BGP route selection | IGP 到出口；BGP 选外部 route/egress | 跨 AS 路径推演断链 |

## 10. Correctness、Cost 与 Tradeoff

| 模型 | 信息范围 | 主要能力 | 主要代价/失败形态 |
|---|---|---|---|
| DV/RIP | 邻居给出的距离结论 | 状态简单、分布式更新 | count-to-infinity、坏消息慢、规模限制 |
| LS/OSPF | 区域拓扑事实 | 快速局部计算、完整可见性 | 洪泛、LSDB、SPF 与区域配置成本 |
| Path Vector/BGP | 跨 AS path + attributes | policy、可扩展跨域 reachability | 收敛复杂、策略交互、不保证最短 |
| SDN | controller 聚合的逻辑全局视图 | 可编程、集中策略、通用 match-action | 控制一致性、规则下发、控制通道与故障设计 |

## 11. 做题调用协议

1. 先定 scope：单 router、一个 area、一个 AS 还是跨 AS；
2. 写当前知识表示：distance、topology facts、path attributes 或 controller view；
3. 区分收到的 advertisement 与最终 installed route；
4. 按事件时间顺序更新，不用收敛后的答案覆盖中间状态；
5. RIP 题执行“接收—加邻接代价—比较—更新—通告”；
6. OSPF 题分开 LSA/LSDB、SPF tree 与 forwarding entry；
7. BGP 题先应用 policy/loop constraints，再谈路径长度；
8. 最后问 forwarding plane 将使用哪个 next hop。

## 12. 贯穿母例：一条链路失效后谁先知道

设 router A 与 B 的链路断开：

- A/B 先由本地接口事件知道；
- DV 中，邻居接收新的 distance 结论并逐步重算，旧结论可能形成相互引用；
- LS 中，A/B 发布更新后的 link state，区域内节点安装新事实后各自重跑 SPF；
- SDN 中，device 报告 port event，controller 更新逻辑拓扑、重算并下发新 rules；
- 若改变 AS 的外部 reachability，BGP 还需 withdraw/update 并经过各 AS policy 传播。

同一个物理故障在不同控制模型中改变的是不同的知识对象。先问“谁拥有哪份状态”，比先背报文名更稳定。

## 13. 高频 First Divergence

- 收到 neighbor 的表就原样复制：漏加本地到 neighbor 的 cost；
- OSPF 直接交换 routing table：混淆 topology fact 与 local decision；
- 说 BGP 选择 AS_PATH 最短：抹掉 policy 与其他 attributes；
- 看到 link down 立刻写所有 router 新表：跳过传播和收敛；
- 把 data plane 的 LPM 写成 routing algorithm：没有区分状态生成与使用；
- 把 SDN controller 放在每台 OpenFlow switch 内，或必然只部署一台：混淆逻辑与物理架构。

## 14. 一页压缩与复原问题

$$
\boxed{
\text{Observe locally}
\to \text{Advertise}
\to \text{Merge knowledge}
\to \text{Choose under objective/policy}
\to \text{Install forwarding state}
}
$$

1. DV 为什么可能让旧知识循环自证？
2. LS 为什么必须把事实同步和路径计算分开？
3. OSPF Area 用什么信息损失换取什么规模收益？
4. BGP 为什么不是“Internet 上的最短路算法”？
5. SDN 的 logically centralized 到底集中什么？

## 15. 来源与校正说明

- 归档笔记《网络层-路由协议》《网络层-SDN》《公式汇总》提供 RIP、OSPF、BGP 与 SDN 覆盖；
- OSPF 的 link-state database 与 shortest-path tree 边界依据 [RFC 2328](https://www.rfc-editor.org/rfc/rfc2328.html) 校正；
- BGP 的 inter-AS reachability、AS_PATH 与 policy 边界依据 [RFC 4271](https://www.rfc-editor.org/rfc/rfc4271.html) 校正；
- 旧笔记中的“集中控制器拥有全局最优”“OSPF 天然无环”等绝对表述已改为带时间、作用域和部署条件的模型。
