# 计算机网络做题规则

状态：工作稿；305 道正式题已完成首轮攻击。7 条跨 Topic 控制规则已有迁移证据并进入“已采用”；Same-Subnet、LPM、分片、DV、OSPF、BGP 等局部规则回归各 Topic 训练文档，不在这里维护第二份协议手册。

## 已采用

### 快速路由先做 Scope → Object/Owner → Event

**触发信号**：任何陌生网络题，尤其题面同时出现多个协议名或多个层次对象。

**第一动作**：先回答三个问题：当前作用域在哪里；当前正在处理什么对象、谁拥有状态；刚发生了什么事件。只有路由完成后才进入 Topic 内部算法。

**检查与退出**：若一上来就因为看到“ARP/TCP/OSPF”套固定流程，却还说不清当前节点、状态 Owner 或事件，停止计算并重新定位。

### 名字必须带类型

**触发信号**：题面出现“地址、目的地、端点、下一跳”等容易裸写的名词。

**第一动作**：显式写成 domain、destination IP、prefix、next-hop IP、MAC、port、socket endpoint、multicast group 或 tuple。

**检查与退出**：若同一个符号在推理中从 IP 变成 MAC、从 port 变成 process，或让 MAC 越过 router 继续有效，说明名字类型已经丢失。

### 状态的生成、安装与使用必须分开

**触发信号**：出现 routing table、cache、window、mapping、flow rule 或任何“表已经有了/刚更新”的描述。

**第一动作**：分清状态从哪里生成、何时成为可执行状态、当前事件又在使用哪一版状态。例如 routing 题保留 `advertisement -> candidate -> selected RIB -> installed FIB -> packet lookup`。

**检查与退出**：收到一条控制消息不等于 packet 已使用新状态；算出一个值也不等于它已经被安装或反馈给对端。

### 状态存在不推出服务语义

**触发信号**：题目同时出现“建立、连接、表、窗口、缓存、映射”等状态词，以及“可靠、面向连接、可达、可执行”等服务性质。

**第一动作**：分别写 `State Owner` 和 `Service Claim`：谁保存了什么状态？题目声称的性质又需要哪些额外机制才能成立？例如 PPP 的 LCP state 不等于可靠重传，TCP `Window` 字段不等于 `cwnd`，selected route 不等于 installed executable FIB。

**检查与退出**：若推理形式只是“因为建立了状态，所以可靠/可达/已连接”，却没有指出 ACK/重传、install、resolution 或 application authority 等真正证据，停止并回到 Owner 边界。703、818、930、988 这类题正是在攻击这种错误迁移。

### 协议流程按 Event Ledger 推进

**触发信号**：题目要求握手、关闭、路由更新、ARP/DHCP、交换机学习、窗口或 ACK/Timer 状态变化。

**第一动作**：为参与实体分栏，逐事件写 `输入/触发 -> 能证明什么 -> 本地状态变化 -> 输出/等待 -> 停止条件`。

**检查与退出**：不能用最终状态倒推中间过程；若某一步修改了一个当前报文根本观察不到的远端状态，回到上一个事件寻找 First Divergence。

### 可靠、流控、拥塞先写受保护对象

**触发信号**：同时看到 ACK、window、loss、buffer、`rwnd`、`cwnd` 等反馈变量。

**第一动作**：先问在保护什么：可靠性保护 delivery invariant，flow control 保护 receiver capacity，congestion control 保护 shared path/queue；再调用 Seq/ACK、`rwnd` 或 `cwnd`。

**检查与退出**：数值都叫“窗口”不代表状态 Owner 相同；若拿 `rwnd` 更新拥塞门限、或把 duplicate ACK 直接写成 receiver buffer 满，立即退出当前路线。

### 性能题先画依赖时间线，再声明 Cost Model

**触发信号**：题目问 RTT、完成时间、利用率、吞吐、窗口、网页加载或多包多跳。

**第一动作**：标出 transmission、propagation、processing、queueing、feedback、可并行与不可并行依赖，再决定哪些时间相加、哪些取最大、哪些能流水。

**检查与退出**：传播项不能随 packet 长度变化，发送项不能随距离变化；并行步骤不能重复相加，throughput/BDP 只给约束或在途量时不能冒充实际完成时间。

## 待验证

### 跨层综合题先找“第一个未满足的前置条件”

当前题库的 997 等题只对协议组合做了初步识别，还不足以证明这条规则在复杂 Integration 中已经稳定迁移。候选动作是：面对一次 URL/网络请求故障，不从最熟悉协议开始，而从配置、名字、FIB/next-hop、链路身份、transport state、application semantics 中寻找第一个尚未满足的前置条件；需要更多完整状态题继续攻击后再决定是否晋升。

## 已否定

- “滑动窗口默认就是 GBN”；必须由 ACK 语义、接收窗口和失序处理判断协议模型。
- “经过 $N$ 个路由器固定需要 $N+1$ 次 ARP”；缓存、链路类型和 IPv6 邻居发现会改变事件数。
- “OSPF/Dijkstra 天然且始终无环”；一致输入下的计算树不等于收敛期间所有 FIB 一致。
- “BGP 总是选择最短 AS_PATH，因此更近或时延更低”；跨域选择受策略和属性约束。
- “SDN controller 必然是一台物理超级计算机，并拥有即时全局最优”；逻辑集中与物理部署、最优性、收敛性不同。
- “IPv6 不允许分片”；路径中的 router 不分片，但 source 可使用 Fragment extension header。
- “NAT 就是防火墙”；映射改写与安全策略不是同一机制。
- “每个子网可用主机数无条件为 $2^h-2$，且 `/30` 永远是点到点最优”；必须保留 `/31`、`/32` 与题设边界。
- “吞吐量必然等于最慢链路速率，BDP 是链路最大容量”；前者还受协议、窗口和开销约束，后者是速率与指定时延的乘积。
- “CRC 余数为零就证明没有错误”；它只表示错误未被检测到，检测能力依赖生成多项式与错误模式。
