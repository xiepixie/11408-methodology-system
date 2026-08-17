# 计算机网络做题规则

状态：工作稿；旧笔记已形成待验证动作与已否定口诀，尚无已采用规则。

## 已采用

暂无。以下动作必须经过真题/陌生题攻击，不能因写入本文自动晋升。

## 待验证

### 第一问先定 Scope

做网络题前先写当前讨论的是信号/一跳、端到端、一个 area、一个 AS 还是跨 AS。字段、状态和反馈必须放回其有效范围。

### 名字必须写类型

出现“地址”“目的地”“端点”时，明确它是 domain、destination IP、next-hop IP、MAC、port 还是 socket endpoint。跨路由器同时维护 destination IP、next-hop IP、next-hop MAC 三种身份。

### 表的生成、安装与使用分开

把 advertisement、RIB candidate、selected route、installed FIB 和 packet-time LPM 分栏写；先判断题目在模拟 routing update，还是使用已有 FIB。

### 协议流程必须逐事件维护状态

为通信双方或设备分栏，逐行写“触发事件 → 报文与关键字段 → 接收方校验 → 本地状态变化 → 响应或超时分支 → 停止条件”。只背 DORA、三次握手或五类 OSPF 报文名称，不足以回答序号、时延和状态题。

### Same-Subnet 先于 ARP

主机先用本地 prefix 判断目的是否直连：直连时解析 destination IP，异网段时解析 gateway/next-hop IP。缓存未命中才触发解析，不能预设固定 ARP 次数。

### LPM 先限定最具体前缀

对当前 destination 先找最长匹配前缀；metric/policy 只在路由生成或题设允许的同前缀候选中比较，不能用“小 metric”跨前缀覆盖 LPM。

### 子网题先写适用假设与对齐

先声明传统 `2^h-2` 模型是否适用，再按需求从大到小选择块并检查起点对齐；用按位与或块边界复核，不把 `/30` 写成所有点到点场景的永恒最优。

### 分片题逐片维护状态表

逐片记录 payload、total length、offset、MF，并检查 payload 守恒和 8-byte 对齐；同时先定 IPv4/IPv6 与重组 Owner，不能只套一个公式。

### NAT 题维护双向 Tuple

写出改写前后 `(IP, port, protocol)` 和反向命中条件；每次事件推进 mapping/timeout/checksum，不能把 NAT 状态省略成一次地址替换。

### 路由更新必须沿时间轴

先写谁观察 event，再写 advertisement freshness、candidate update、selection 和 FIB install；不得用最终收敛表覆盖 transient loop、black hole 或旧 FIB。

### DV 更新先更新“经该邻居的候选”

收到邻居 vector 后先加本地邻接 cost；若当前 route 来自该邻居，即使 metric 变差也要更新该候选，再与其他候选重选，不能只接受更小值。

### OSPF 分开 LSA、LSDB、SPF 与 FIB

逐事件写 `link event → newer LSA → flooding → LSDB → SPF → install`。同一 LSDB 上的树无环，不推出收敛中间态永远无环。

### BGP 先过滤与策略，后看路径属性

按 `receive → import policy → loop/validity → decision → export` 推进；只有题设给定属性顺序时才执行具体 tie-break，不能把最短 AS_PATH 当通用第一规则。

### SDN 分开逻辑控制与物理部署

先写 controller 提供的逻辑视图，再写实例复制/分片、事件传播和 rule install；“逻辑集中”不推出“物理单点、即时一致或必然全局最优”。

### 可靠、流控、拥塞先写受保护对象

先判断问题保护的是 data delivery、receiver buffer 还是 network capacity，再选择 sequence/ACK、`rwnd` 或 `cwnd` 模型。

### 性能题先画时间线并声明成本模型

分开 transmission、propagation、processing、queueing、ACK 等待和可并行段；throughput 的瓶颈链路结论只作上界，BDP 是指定路径和时间尺度的在途量，不是“最大容量”。

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
