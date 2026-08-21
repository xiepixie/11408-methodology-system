# RIP、OSPF、BGP 与路由收敛推演

> 训练定位：解决“收到路由消息、链路变化或控制器事件后，怎样逐步更新知识、候选路线、选择结果和 FIB”的题目族。  
> 模型归属：[NET-05 路由与控制平面](NET-05_路由与控制平面_方法论手册.tex)。DV/LS/Path Vector、RIP/OSPF/BGP、RIB/FIB、收敛与 SDN 的机制归 Canonical；本文件只训练事件账本与计算/判断路径。

## 母题表示：路由题先分“知识生成”和“分组使用”

看到 routing table、RIP、OSPF、BGP、Dijkstra、Bellman-Ford 时，草稿先写五格：

```text
Observation / Advertisement
-> Candidate knowledge
-> Local selection
-> FIB installation
-> Packet-time lookup
```

前四格属于控制面，最后一格才是数据面。

> **停止条件：**若“收到一个路由消息”后直接把所有后续 packet 写成已经走新路，说明跳过了本地候选、选择和 FIB install。

## 问题一：DV/RIP 收到邻居向量后，先更新“经这个邻居的候选”

节点 $x$ 从邻居 $v$ 收到目的 $y$ 的距离 $D_v(y)$，先构造：

$$
D_x^{(v)}(y)=c(x,v)+D_v(y).
$$

再与来自其他邻居的候选比较：

$$
D_x(y)=\min_vD_x^{(v)}(y).
$$

### 局部规则：当前 route 来自该邻居时，坏消息也要接收

**触发信号**：邻居把某目的的 metric 变大或宣布不可达。

**第一动作**：先把“经该邻居”的候选更新为新值，即使它更差；然后再与其他候选重选。

**检查与退出**：如果只在新 metric 更小时才更新，会把已经失效的旧好消息永久留在表中。

## 问题二：Count-to-Infinity 用“依赖环”解释

失败后不要只背“距离越来越大”。画出谁的当前结论依赖谁：

```text
A 的 route 依赖 B
B 失去真实路径
但 B 又把 A 的旧结论当成另一条路径
A 再引用 B 的新结论
-> 旧知识循环自证
```

Split horizon / poison reverse / triggered update 的作用，是限制错误知识回流或缩短坏消息传播时间；不能升级成“任意拓扑绝对消环”。

## 问题三：OSPF 一定按四层状态推进

经典主线：

```text
link/neighbor event
-> newer LSA
-> reliable flooding
-> LSDB update
-> SPF(Dijkstra)
-> RIB selection
-> FIB install
```

### 四个对象不能混

| 对象 | 它是什么 |
|---|---|
| LSA | 一条链路状态事实/通告 |
| LSDB | 当前作用域内的事实集合 |
| SPF tree | 对某一版本 LSDB 运行 Dijkstra 的计算结果 |
| FIB | packet 到达时真正使用的快速转发动作 |

### 局部规则：Dijkstra 只消费已知图，不负责传播知识

**触发信号**：题目同时给 OSPF 报文和最短路径图。

**第一动作**：先完成邻接/LSA/LSDB 的事件，再在确定的一份 LSDB 上执行 SPF。

**检查与退出**：若把 Dijkstra 的“松弛”步骤写成路由器彼此交换距离，就已经把 LS 写成 DV。

## 问题四：OSPF 邻居与邻接不要一看到 Hello 就等同

经典报文角色：

```text
Hello -> 发现/保活/参数相容
DD/DBD -> 摘要数据库
LSR -> 请求缺失或更新的 LSA
LSU -> 携带 LSA
LSAck -> 确认可靠洪泛
```

广播型多路访问网络还可能有 DR/BDR。题目问 adjacency 数量时，先确认网络类型和谁需要形成完整邻接，不能默认所有 neighbor 两两 Full。

## 问题五：BGP 先做策略与有效性，再看路径属性

稳定的处理顺序：

```text
Receive route
-> Import policy
-> Validity / loop checks
-> Local decision process
-> selected RIB route
-> recursive next-hop resolution
-> FIB install
-> Export policy
```

### 局部规则：AS_PATH 不是万能第一比较项

**触发信号**：题目给多条 BGP 路线、AS_PATH、local preference 等属性。

**第一动作**：严格执行题设给出的决策顺序；若题设只问概念，先说 BGP 是 policy-constrained reachability selection。

**检查与退出**：不能因为一条 AS_PATH 更短，就无条件推出它被选择、更低时延或更少物理 hop。

## 问题六：BGP 选出 next hop 后，还要能“到达 next hop”

假设 BGP 选出：

$$
(P, H, attributes).
$$

本地仍需用 IGP/connected knowledge 解析怎样到达 $H$，最终得到：

$$
(P, out\!\!-if, link\ next\ hop).
$$

因此至少区分：

```text
BGP session established
route received
route selected
BGP next hop resolvable
FIB installed
```

任何一格失败，都不能直接推出数据面可达。

## 问题七：收敛题必须保留中间态

拓扑变化：

$$
S_{old}\to S_{mixed}\to S_{new}.
$$

训练至少记录：

1. 谁先观察故障；
2. 什么消息传播新事实；
3. 不同节点何时更新候选；
4. 何时重新计算；
5. 何时安装 FIB；
6. 中间是否可能 transient loop / black hole / suboptimal path。

### 局部规则：最终最短路不能覆盖中间过程

**触发信号**：题目写“链路突然断开”“收敛过程中”“某路由器还未收到更新”。

**第一动作**：为每台 router 写它当前持有的知识版本，而不是先算最终稳定拓扑。

## 问题八：SDN 题分开逻辑集中与物理 controller

Reactive 教材流程：

```text
packet table miss
-> Packet-In
-> controller policy/path computation
-> Flow-Mod
-> Packet-Out / release buffered packet
-> subsequent packets hit installed rule
```

Proactive 则把规则提前安装。

### 检查

- logical centralized ≠ 物理只有一台 controller；
- controller 算出规则 ≠ 所有设备瞬时完成 install；
- flow table ≠ MAC learning table ≠ IP LPM FIB。

## 代表母题 A：RIP 坏消息

A 当前到网络 N 的 route 是经 B，metric=3。现在 B 通告 N 的 metric 变为 16（不可达）。

正确顺序：

1. 更新“经 B 到 N”的候选为不可达；
2. 查看其他邻居是否还有可用候选；
3. 若有，重选 next hop；若无，本地 N 不可达；
4. 再讨论 triggered/periodic advertisement。

错误路径是“16 比 3 大，所以保留原来 3”。原来 3 的来源就是 B，来源已经撤回。

## 代表母题 B：OSPF 链路失效

某链路 down 后，不写“一瞬间全网新最短路”，而写：

```text
端点 router 检测事件
-> 生成新序号 LSA
-> 邻居接收并 ACK / 继续洪泛
-> 各 router 在不同时刻安装新 LSA
-> 各自重跑 SPF
-> route selection
-> FIB install
```

若两个相邻 router 在某时刻分别使用新旧 FIB，就要允许题目出现暂时环路或黑洞。

## 题库验证：代表题、已验证边界与空白

当前题库已经充分验证“交换什么知识”和“如何从知识得到本地结果”，但对收敛中间态与策略组合的压力还不够：

| 证据题 | 表面题型 | 实际验证的母模型 |
|---|---|---|
| 874、875 | 静态/动态、分层路由 | 状态来源与 Scope 分层；规模化靠隐藏细节而不是所有人掌握全网 |
| 878、879、881、889 | RIP / DV | 邻居向量先加本地 cost，再更新该邻居候选；旧知识异步循环产生回路 |
| 876、877、883–885 | OSPF Hello/Area/角色 | 邻居、Area、LSA/LSDB 作用域与角色边界分开 |
| 880、882、884 | RIP vs OSPF | DV 交换压缩结论，LS 洪泛事实后本地 SPF |
| 886–888 | OSPF/BGP/封装分类 | BGP 是跨 AS path-vector/policy reachability；协议承载层与功能分类是不同维度 |
| 837、838 | SDN | control/data plane separation、OpenFlow 南向接口、逻辑 controller 与设备角色分离 |
| 890 | OSPF + 端到端性能 | 先由 control plane 得到路径，再把路径交给 data-plane/store-forward 成本模型 |

### 变式轴

1. **知识表示**：distance / link-state fact / path attributes / controller view；
2. **作用域**：neighbor / area / AS / inter-AS / controller domain；
3. **事件类型**：好消息、坏消息、链路 down、邻接失效、withdraw；
4. **决策层级**：candidate / selected RIB / next-hop resolution / installed FIB；
5. **时间版本**：所有节点一致稳定，还是部分节点仍在旧状态；
6. **目标函数**：metric optimization 还是 policy-constrained reachability。

> **关键验证结论：**现有题库足以支持 Canonical 的 DV/LS/PV 三种知识表示和 RIB/FIB 边界，不需要重写 NET05 主干。

> **仍需补的证据：**几乎没有题真正让两台或多台 router 在 `S_mixed` 中持有不同版本 FIB，并追问 transient loop / black hole；也缺少“BGP 多属性决策 + IGP 递归解析 next hop”的完整状态题。下一轮应优先补这两类母题，而不是继续增加 RIP/OSPF 定义选择题。

## 题目攻击：从“稳定表”继续攻击到“版本化控制面”

### 攻击 889：DV 更新的是候选列，不是整张表

来自 B/D/E 的三个向量分别只产生“经该邻居”的候选：`local cost + neighbor vector`。逐目的取最小以后才得到 C 的新本地结论。若收到 B 的向量后直接覆盖 C 的整张 route table，就丢掉了其他邻居作为独立解释来源。

### 攻击 890：OSPF 只决定路径，完成时间仍由另一个 Owner 计算

890 先用 OSPF metric 选出 `A-R1-R3-R4-R2-B`，然后才进入 NET01 的 store-and-forward 流水时间。若把“OSPF cost=9”直接拿去当毫秒数，说明把 control-plane metric 与 data-plane physical cost 混成了同一量。

### 压力变式：把 890 从稳定态改成 `S_mixed`

若故障后 R1 已完成新 SPF 并安装新 FIB，而 R3 仍使用旧 FIB，则当前 packet 不能再用“最终最短路径”统一描述。必须逐台写：

```text
R1 installed FIB version = new
R3 installed FIB version = old
packet arrives now
```

再沿每台设备当前实际 FIB 推进。这个变式正是 [FIB 版本与收敛中间态](../50_科内桥梁/NET-B02_Routing与Forwarding/FIB版本与收敛中间态.md) 要训练的 Bridge。

### 攻击 886：BGP 的“最优”不是统一物理最短路

BGP 交换 prefix 与 path attributes，本地 policy 决定可接受和偏好；选出的 BGP next hop 还必须由 IGP/connected knowledge 递归解析。若只看到较短 `AS_PATH` 就直接写“时延最小且一定安装”，同时跳过了 policy 与 executability 两层。

## 陌生路由题固定落笔协议

```text
1. 当前 scope：neighbor / area / AS / inter-AS / controller domain？
2. 当前知识对象：distance / link-state fact / path attributes / flow rule？
3. 收到消息只先改变 candidate/knowledge，不直接跳到 packet action。
4. DV：加本地 cost -> 更新该邻居候选 -> 重选。
5. OSPF：LSA -> LSDB -> SPF -> RIB -> FIB。
6. BGP：import/policy/loop -> decision -> next-hop resolution -> install。
7. 收敛题保留每台设备的版本差异和时间线。
8. 最后才把 selected route 交给 NET04 做 LPM/next-hop forwarding。
```

## 最短压缩

> **路由题不是“算最短路”，而是“知识怎样变成可执行状态”：消息 → 候选 → 选择 → 安装 → 分组使用；收敛中间态必须保留。**
