# FIB 版本与收敛中间态

> 训练定位：解决“控制平面已经学到/选出新路线，但数据平面何时真正使用，以及不同路由器版本不一致时当前 packet 怎么走”的跨接口题。  
> 模型归属：[NET-B02 Routing × Forwarding](NET-B02_Routing与Forwarding_桥梁手册.tex)。NET05 拥有 route knowledge/selection，NET04 拥有 installed FIB/LPM；本文件只训练两者交接的版本、安装与失败边界。

## 母题表示：同一时刻必须同时写 Control Version 与 FIB Version

最危险的错误是：

```text
收到新路由消息
=> 当前 packet 立刻走新路径
```

实际至少分五个事件：

```text
advertisement received
-> candidate updated
-> local route selected
-> FIB action installed
-> later packet consumes that installed version
```

因此草稿固定记录：

```text
RIB/selection version = ?
FIB installed version = ?
packet arrival time = ?
next hop executable/resolvable? = ?
```

### 局部规则：packet 只消费“到达时已经安装”的 FIB

**触发信号**：题目出现“刚收到更新、已经算出新最短路、尚未更新转发表、某时刻 packet 到达”。

**第一动作**：把 control-plane selection time 与 FIB install time 分开，在 packet arrival 的时间点读取 installed FIB。

**检查与退出**：若 packet 到达时间早于 install，却使用了新路线，说明把“知道”写成了“已执行”。

## 代表母题 A：控制面已选新路，FIB 还没装

路由器 R 原有：

```text
FIB v1:
10.0.0.0/8 -> R1
```

`t=10 ms`：控制面收到并选出更具体的新 route：

```text
selected RIB v2:
10.1.0.0/16 -> R2
```

`t=13 ms`：`/16 -> R2` 才完成 FIB install。

现在两个 packet 目的均为 `10.1.2.3`：

- P1 在 `t=11 ms` 到达；
- P2 在 `t=14 ms` 到达。

推演：

```text
P1 arrival @11 ms
-> FIB 仍是 v1
-> /8 match -> R1

P2 arrival @14 ms
-> FIB 已是 v2
-> /16 LPM -> R2
```

同一个 destination，因为消费的 FIB 版本不同，可以在短时间内采取不同动作。

## 代表母题 B：route 已选中，但 next hop 不可执行

BGP/IGP 控制面选中：

```text
203.0.113.0/24 -> BGP next hop H
```

但本地当前没有任何 connected/IGP route 能解析到 H。

正确判断：

```text
selected route exists
!= executable forwarding action exists
```

必须先完成：

```text
H -> reachable egress / recursive resolution
```

才能形成可执行 FIB action。不能从“BGP UPDATE 已收到且被选中”直接推出 packet 可达。

### 局部规则：RIB 有 route，不等于 FIB 一定能装

**触发信号**：题目给 selected route 和 next hop，但又给 next-hop unreachable / adjacency missing。

**第一动作**：先检查 recursive resolution 是否能落到直连接口或可执行 adjacency。

**检查与退出**：若 next hop 无法解析，却仍然写出具体出口 MAC/接口，说明越过了 Bridge 的合法性条件。

## 问题三：多设备异步安装为什么会出现 transient loop / black hole

设故障后最终稳定状态应为：

```text
A -> C
B -> C
```

但某一中间时刻：

```text
A 已安装新 FIB: destination -> B
B 仍保留旧 FIB: destination -> A
```

则即使两台路由器的控制算法最终都会收敛，当前 packet 仍可能：

```text
A -> B -> A -> B ...
```

形成 transient loop，直到其中一台安装状态继续推进。

另一种安装顺序可能让某节点暂时没有可执行 route，于是产生 black hole。

### 局部规则：收敛题必须保存每台设备自己的版本

**触发信号**：题面写“部分路由器已更新、某路由器仍旧状态、更新传播中”。

**第一动作**：分别写每台 router 的 installed FIB，不允许用最终全局表覆盖当前混合状态。

**检查与退出**：若你只画一张“全网当前路由表”，却题目明确各节点更新时间不同，模型已经丢失分布式时间轴。

## 题库证据与验证位置

现有题库提供了两侧证据：

- 874–890：route knowledge、DV/LS/BGP、OSPF SPF；
- 847、909：installed FIB 上的 LPM/default action；
- 906：RIB/route generation 与 forwarding state 的控制/数据面关系；
- 890：先由 OSPF 得路径，再计算数据面存储转发成本。

但这些题没有直接给出 `selection time != FIB install time`。因此训练不凭空再造一套机制，而是从 **890** 做最小压力变形：保留同一拓扑与 OSPF 最终最短路，只把“所有路由器均已收敛”改成“R1 已安装新 FIB、R3 仍使用旧 FIB”，再问当前 packet 的实际路径。若答案仍直接套 890 的最终稳定路径，就证明 Bridge 没有真正建立。后续若有真题/错题直接命中，应把题号回填为代表证据。

### 回归攻击：稳定态答案不能偷渡到中间态

对任何由 890 派生的 mixed-state 题，至少做两次回归：

1. 把所有 FIB 都设回旧版本，应恢复故障前路径；
2. 把所有 FIB 都设成新版本，应恢复最终收敛路径。

只有中间版本组合才允许产生 transient loop、black hole 或暂时次优路径。这样可以独立检查“版本状态”是否真的参与了推理，而不是在答案里只出现了几个新名词。

## 变式轴

1. route 更具体 / 同前缀替换；
2. control selection 与 install 延迟大小；
3. packet 在 install 前/后到达；
4. next-hop resolvable / unresolvable；
5. 单机版本差 / 多机异步版本差；
6. transient loop / black hole / suboptimal old path。

## 陌生题固定落笔协议

```text
1. 当前控制面知道什么版本？
2. 当前已经 selected 什么 route？
3. next hop 是否能递归解析？
4. 何时安装进 FIB？
5. packet 到达时消费哪一版 FIB？
6. 多 router 时逐台写版本，不写一张全局表。
7. 最后才执行 LPM / next-hop / link delivery。
```

## 最短压缩

> **路由“算出来”与 packet“用起来”之间隔着 resolution 与 install；收敛正确性必须在每台设备自己的 FIB 版本时间线上判断。**
