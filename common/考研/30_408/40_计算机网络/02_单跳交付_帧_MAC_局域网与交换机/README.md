# 单跳交付：帧、MAC、局域网与交换机

状态：工作稿，待人工确认。

## 0. 本册定位

本 Topic 回答：当若干节点共享一个本地交付环境时，怎样识别一帧、发现传输错误、决定谁能发送，并把 frame 交给正确的下一跳接口？

本册拥有 framing、透明传输、CRC 基础、介质访问控制、Ethernet、WLAN、VLAN、switch table、collision/broadcast domain。

本册只接收已经确定的 next-hop IP 与对应 MAC。IP 如何决定 next hop、ARP 如何取得 MAC 由[IP 分组转发](../04_IP地址_子网与分组转发/README.md)拥有；信号怎样传播由[通信基础](../01_通信基础与网络性能/README.md)拥有。

## 1. 根本问题：一根线不自带“帧”和“轮到谁”

物理层只提供连续的信号或 bit 流。若多个节点直接使用它，会立即出现四个缺口：

1. 接收方不知道一帧从哪里开始、到哪里结束；
2. 数据可能恰好长得像边界标记；
3. 传播中的 bit 可能被破坏；
4. 共享介质上的多个发送者可能同时发送。

于是单跳交付机制按以下链条生成：

$$
\boxed{
\text{Raw channel}
\to \text{Frame boundary}
\to \text{Error detection}
\to \text{Access right}
\to \text{Local forwarding}
}
$$

Frame 解决“这段 bit 属于同一个链路层单元”；MAC 解决“谁能在何时使用共享介质”；switching 解决“已收到的 frame 应去哪个本地端口”。

## 2. 单跳模型

一跳交付的标准表示是：

```text
上层给出 packet + next-hop IP
-> ARP/cache 得到 next-hop MAC
-> 链路层封装 frame
-> 介质访问协议取得发送机会
-> 物理层发送 signal
-> 接收端定界并检错
-> switch/host 按目的 MAC 处理
```

这一过程的核心不变量是：frame 的 MAC 地址只对当前链路有效。路由器转发 packet 时会删除入站 frame，再为下一条链路创建新的 frame。

## 3. Framing：边界必须无歧义

### 3.1 为什么需要透明传输

若用特殊序列标记 frame 边界，而 payload 中允许出现相同序列，接收方就无法区分“数据”与“控制标记”。透明传输的目标是：任意上层 bit 模式都能被无歧义地承载。

- 面向字节的协议可用 byte stuffing：数据中的 flag/escape 先转义；
- 面向 bit 的协议可用 bit stuffing：发送端在特定连续 bit 后插入 bit，接收端再删除；
- 固定或长度字段方案依赖长度值和同步状态正确。

填充改变的是表示，不改变 payload 语义。接收方必须可逆地还原。

### 3.2 CRC：检测，不是修复

发送端把 bit 串视为 $GF(2)$ 上的多项式，用生成多项式 $G(x)$ 做模 2 除法，将余数附在 frame 后；接收端用同一 $G(x)$ 检查余数。

CRC 提供高强度错误检测，但它不说明错误 frame 应如何恢复。Ethernet 通常丢弃坏帧；是否重传由具体链路协议或更高层可靠传输机制决定。

## 4. MAC：共享资源的三种基本治理方式

### 4.1 预先切分

FDM/TDM/CDM 把频率、时间或码空间预先分配给使用者。优点是无冲突、行为可预测；代价是空闲份额可能浪费，并需要同步或码设计。

### 4.2 随机接入

随机接入允许节点有数据就尝试发送，冲突后再恢复，适合突发业务。

```text
ALOHA：直接发，冲突后随机重试
-> CSMA：先侦听再发
-> CSMA/CD：有线共享介质中边发边检测
-> CSMA/CA：无线中通过等待、ACK、可选 RTS/CTS 尽量避免冲突
```

CSMA 仍会冲突，因为侦听结果只反映“过去到达本节点的信号”，无法消除传播时延造成的状态差异。

### 4.3 受控接入

轮询或令牌把发送权显式交接。它们用管理开销换取无冲突、公平性和高负载下的稳定利用率；控制节点故障、令牌丢失或低负载等待是相应成本。

## 5. CSMA/CD 为什么导出最小帧长

发送端只有在仍在发送时，才能检测从最远端返回的冲突。设冲突域最大单向传播时延为 $\tau$，则 frame 的发送时间必须覆盖最坏往返传播时间：

$$
\frac{L_{min}}{R}\ge 2\tau
\qquad\Longrightarrow\qquad
L_{min}\ge 2\tau R.
$$

这不是孤立公式，而是一个可观测性约束：发送者必须保持“仍在现场”，直到最远冲突有机会返回。

二进制指数退避则解决冲突后的再次同步冲突：冲突越多，随机等待范围越大。它降低再次碰撞概率，但增加不确定等待。

现代交换式全双工 Ethernet 的点到点链路没有共享介质冲突，通常不运行 CSMA/CD；考试中的最小帧长模型针对经典共享/半双工 Ethernet。

## 6. 无线为什么不能简单复制碰撞检测

无线发送端自身信号远强于远端信号，且存在隐藏站、暴露站和覆盖范围不对称，因此可靠地“边发边听冲突”困难。802.11 的基本思想是 CA：

1. 物理/虚拟载波侦听；
2. 信道空闲一段时间后随机退避；
3. 接收方用 ACK 显式证明成功；
4. 可选 RTS/CTS 预约信道并让邻居设置 NAV。

RTS/CTS 不是每帧必用，也不能消除所有碰撞；它用控制开销降低长数据帧冲突的代价。

## 7. Ethernet switch：状态从源地址学习，动作由目的地址决定

交换机维护近似如下的软状态：

$$
(MAC,\ ingress\ port,\ age).
$$

每收到一帧，执行两阶段逻辑：

1. **Learn from source**：记录源 MAC 从哪个端口到达；
2. **Act on destination**：查询目的 MAC。

目的地址查表后的分支：

- 命中其他端口：定向转发；
- 命中入端口：过滤；
- 未知单播：向除入端口外的相关端口泛洪；
- 广播：在当前广播域/VLAN 内泛洪。

表项会老化，因为主机可能移动、拓扑可能变化。MAC table 是从流量观察得到的局部软状态，不是路由协议生成的全网路径。

## 8. 环路、STP 与 VLAN

### 8.1 为什么二层环路危险

Ethernet frame 没有像 IP TTL 那样的逐跳寿命字段。冗余链路形成环路后，广播和未知单播可能被无限复制，源地址还会从不同端口反复出现，造成 broadcast storm 和 MAC table instability。

STP 的核心不是“删除物理冗余”，而是从有环物理图中选择一棵无环的逻辑转发拓扑；故障时再重新计算。它用部分链路闲置和收敛时间换取无环不变量。

### 8.2 VLAN 改变广播作用域

VLAN 把一个物理交换网络切成多个逻辑二层广播域。Access link 把端口归入一个 VLAN；Trunk link 用 802.1Q tag 在交换机之间携带 VLAN 身份。

不同 VLAN 之间不能只靠二层交换互通，需要三层转发。VLAN 隔离的是逻辑广播域，不等于完整的安全策略。

## 9. 概念边界

| 概念 A | ≠ | 概念 B | 真正区别与题目信号 | 混淆后果 |
|---|:---:|---|---|---|
| Hub | ≠ | Switch | Hub 复制 signal；switch 解析 frame 并学习 MAC | 冲突域和带宽计算错误 |
| Collision domain | ≠ | Broadcast domain | 前者是可能碰撞的共享发送范围；后者是二层广播可达范围 | 误判 switch、VLAN、router 的隔离能力 |
| Source learning | ≠ | Destination forwarding | 源地址更新表；目的地址决定动作 | 把学习方向写反 |
| Error detection | ≠ | Reliable delivery | CRC 发现异常；ACK/Timer/Seq 才构成恢复闭环 | 认为有 CRC 就保证到达 |
| CSMA/CD | ≠ | CSMA/CA | 有线检测冲突；无线主要避免并用 ACK 判断结果 | 把最小帧长或 RTS/CTS 套错环境 |
| MAC address | ≠ | IP address | MAC 服务当前链路；IP 服务跨网络转发 | 认为目的 MAC 端到端不变 |
| Physical topology | ≠ | Logical forwarding topology | 物理可有冗余环；STP 选择无环活动路径 | 无法解释“链路存在但阻塞” |

## 10. 代价与权衡

| 设计 | 能力 | 代价 |
|---|---|---|
| Shared Ethernet | 低成本共享介质 | 冲突、半双工、规模受 $2\tau$ 约束 |
| Switched Ethernet | 每端口独立转发、可全双工 | 交换状态、缓冲与环路控制 |
| VLAN | 逻辑广播域隔离 | 标签、配置与跨 VLAN 路由 |
| STP | 冗余物理拓扑下保持二层无环 | 部分路径闲置与收敛时间 |
| RTS/CTS | 缓解隐藏站和长帧碰撞成本 | 额外握手，不适合所有小帧 |

## 11. 做题调用协议

1. 先定场景：共享/交换、半双工/全双工、有线/无线；
2. 标出当前作用域：冲突域、广播域还是 VLAN；
3. 区分输入对象是 signal、frame、packet 还是 table entry；
4. 交换机题固定写“源学习、目的决策”；
5. CSMA/CD 题先画最远冲突往返时间线，再写 $L/R\ge2\tau$；
6. 无线题问清物理侦听、NAV、退避、ACK、RTS/CTS 各自解决什么；
7. 跨路由器时停止沿用当前 MAC，转入 IP next-hop 模型。

## 12. 贯穿母例：同一 packet 经过交换机和路由器

主机 A 发送给异网段主机 B：

```text
A 查路由：目的不在本地 subnet
-> ARP 默认网关，得到 R1 入接口 MAC
-> frame(MAC_A -> MAC_R1) 承载 packet(IP_A -> IP_B)
-> switch 从源 MAC_A 学习端口，按 MAC_R1 转发
-> R1 删除旧 frame，查 IP 转发表
-> R1 对下一跳重新解析/使用 MAC
-> 新 frame(MAC_R1_out -> MAC_next) 继续承载该 packet
```

在无 NAT 等中间改写时，packet 的端点 IP 语义贯穿路径；frame 的 MAC 只跨一跳。这个母例是[一个网络请求的一生](../60_综合专题/README.md)的局部片段。

## 13. 高频 First Divergence

- 交换机收到帧后先看目的 MAC 学习：把状态来源写反；
- 未知单播说成“广播帧”：混淆 frame 类型与交换动作；
- 认为 switch 隔离广播域：没有区分端口微分段与 VLAN；
- 在全双工交换 Ethernet 中继续计算 collision：没有检查介质共享前提；
- ARP 目的 IP 直接写远端主机：没有先判断 same subnet；
- 把 CRC 说成纠错或可靠送达：没有建立检测与恢复的责任边界。

## 14. 一页压缩与复原问题

$$
\boxed{
\text{Frame the bits}
\to \text{Detect corruption}
\to \text{Acquire medium}
\to \text{Learn source}
\to \text{Forward by destination}
}
$$

1. 为什么传播时延会让“先听后发”仍然冲突？
2. 最小帧长为什么本质上是可观测性条件？
3. 交换机为什么从 source 学、却按 destination 转？
4. 为什么二层环路比普通重复转发更危险？
5. VLAN、交换机端口和路由器分别改变哪个作用域？

## 15. 来源与校正说明

- 归档笔记《链路层-介质访问控制》《链路层-局域网与广域网》《物理层-传输媒体与设备》提供旧考点覆盖；
- 原笔记中的设备、PPP、NAT、路由内容已按 Owner 拆分，未因旧文件名继续混放；
- 本册保留 408 的经典共享 Ethernet 与 WLAN 模型，并显式区分现代交换式全双工场景。
