# IP 地址、子网与逐跳转发

> 训练定位：解决“给出 IP/prefix、路由表、ARP、TTL、MTU、NAT 后，怎样把端到端目的拆成当前节点的一次逐跳动作”的题目族。  
> 模型归属：[NET-04 IP 地址、子网与分组转发](NET-04_IP地址_子网与分组转发_方法论手册.tex)。IPv4/IPv6、CIDR、LPM、ARP、TTL、分片、DHCP、ICMP、NAT 等机制由 Canonical 正文拥有；本文件只训练 Scope、名字类型、逐事件状态与计算检查。

## 母题表示：先写“当前节点—当前名字—当前动作”

IP 题不要从“查路由表”或“发 ARP”开始。草稿第一行固定写：

```text
Current node: host / router / NAT / DHCP client ?
Destination identity: destination IP
Current next-hop identity: next-hop IP
Current link identity: next-hop MAC / configured peer
```

同一个 packet 在路径上通常保持端到端 destination IP 语义，却每跳重新决定 next-hop，并重建当前链路 frame。

## 问题一：主机发送前，Same-Subnet 必须先于 ARP

主机先比较：

$$
IP_{dst}\ \mathrm{AND}\ Mask
\quad\text{与}\quad
IP_{local}\ \mathrm{AND}\ Mask.
$$

若相同：

$$
next\!\!-hop\ IP=destination\ IP.
$$

若不同：

$$
next\!\!-hop\ IP=default\ gateway\ IP.
$$

然后才查询当前 next-hop 的链路层身份。

### 局部规则：ARP 的对象永远是“当前一跳”

**触发信号**：主机访问异网段目标，题目问 ARP 谁、帧目的 MAC 是谁。

**第一动作**：先做 same-subnet 判断，再写 next-hop IP；ARP 只解析这个 next-hop IP。

**检查与退出**：如果异网段情况下直接 ARP 最终远端主机 IP，立即停止；广播不会越过路由器替你寻找远端 MAC。

## 问题二：子网题先把 prefix 当“地址集合大小”

IPv4 `/p` 剩余：

$$
h=32-p
$$

个主机位，对应块大小：

$$
2^h.
$$

传统教材型普通子网常使用：

$$
2^h-2
$$

个可分配主机地址，但这不是对 `/31`、`/32` 等所有语境的无条件定律。

### VLSM 固定算法

```text
1. 需求按主机数从大到小排序
2. 为每项选择能容纳需求的最小 2^h 地址块
3. 当前起点必须按该块大小对齐
4. 写出 prefix / network / usable range / broadcast（若该模型适用）
5. 把下一空闲边界传给下一个需求
```

### 独立检查：按位与 + 边界对齐

十进制看起来“刚好接上”不够。分配起点若不是块大小的整数倍，就不是合法网络边界。

## 问题三：路由器查表只对已安装 FIB 做 LPM

若多个前缀都匹配 destination IP，选前缀长度最长者。

例如：

```text
10.0.0.0/8     -> R1
10.1.0.0/16    -> R2
10.1.2.0/24    -> R3
0.0.0.0/0      -> R4
```

目的 `10.1.2.9` 选择 `/24 -> R3`。

### 局部规则：LPM 与 metric 不在同一层

**触发信号**：题目给不同长度前缀和“距离/metric”。

**第一动作**：先找所有匹配前缀，再以最长 prefix 限定当前转发项。

**检查与退出**：不能用一个较小 metric 的 `/8` 覆盖匹配更具体的 `/24`。Metric/policy 主要属于路线生成/同前缀候选选择，不替代 packet-time LPM。

## 问题四：逐跳转发维护三条状态

路由器收到 frame 后，可把主线压成：

```text
strip incoming frame
-> update/check TTL (or Hop Limit)
-> destination IP -> FIB LPM
-> next-hop / egress
-> compare packet size with outgoing MTU
-> resolve/use current-link identity
-> build a new outgoing frame
```

### 三个关键不变量

1. **Destination IP**：无 NAT/隧道等改写时维持端点语义；
2. **TTL/Hop Limit**：每经过 router 消耗一份 hop budget；
3. **MAC / link identity**：逐跳重建，不能端到端沿用。

## 问题五：TTL 不背“n+1”，按逐路由事件推进

上传速记稿给出了“有 $n$ 个路由器时初始 TTL 至少为 $n+1$”的快捷结论。它只有在特定计数口径下才成立，训练不把它提升为无条件公式。

### 稳健做法

对每台 router 依次写：

```text
arrive with TTL = x
-> decrement/check according to题设教材语义
-> 若耗尽：discard + possible ICMP Time Exceeded
-> 否则 forward
```

题目问“最多还能经过几台 router”时，用逐事件表比背快捷式更稳健，也能避免把“经过的路由器数”和“链路/节点总数”混成同一个 $n$。

### 检查

TTL 是 hop budget，不是严格按秒倒计时；提高链路速率也不会改变它每跳减一的规则。

## 问题六：IPv4 分片必须逐片做状态表

先计算普通非末片可承载 payload：

$$
Payload_{regular}
=8\left\lfloor\frac{MTU-H}{8}\right\rfloor.
$$

然后逐片写：

| fragment | payload bytes | total length | offset | MF |
|---|---:|---:|---:|---:|
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

Offset 的单位是 8 Byte：

$$
Offset_i=\frac{\text{该片 payload 在原 payload 中的起始字节}}{8}.
$$

### 局部规则：先声明 IPv4/IPv6 和 DF

**触发信号**：packet 大于 MTU。

**第一动作**：先问：IPv4 还是 IPv6？IPv4 是否允许分片（DF）？是谁负责分片/重组？

**检查与退出**：IPv6 应写“路径 router 不分片”，不能写成“IPv6 完全不允许任何分片”。

## 问题七：二次分片继续使用原 datagram 坐标

若父片原 offset 为 $o$，子片在父片 payload 内起点为 $x$ Byte：

$$
Offset_{child}=o+\frac{x}{8}.
$$

不能把每个子片重新从 0 编号。

最后一个子片的 MF 也不能机械置 0：只有它同时是原 datagram 的真正末尾时才为 0；否则要继承“后面还有原始数据”的事实。

## 问题八：NAT/NAPT 题必须维护双向 tuple

NAPT 不只是“把私网 IP 换成公网 IP”，而是维护状态：

$$
(private\ IP,private\ port,protocol)
\leftrightarrow
(public\ IP,public\ port,protocol).
$$

### 局部规则：出站和返回分两次推进

出站：

```text
private tuple
-> lookup / allocate mapping
-> rewrite source tuple
-> update relevant checksums
-> forward
```

返回：

```text
public destination tuple
-> hit mapping
-> restore internal destination tuple
-> update checksums
-> forward internally
```

**检查与退出**：如果入站 packet 没有匹配映射，却直接“根据公网 IP 找到任意内网主机”，说明漏掉了 NAT 的状态依赖。

## 问题九：DHCP、ARP、ICMP 不要合成“网络层辅助协议”一句话

| 机制 | 当前问题 | 产生/维护的状态 |
|---|---|---|
| DHCP | 主机还没有完整 IP 配置，怎样 bootstrap | lease、prefix、gateway、DNS 等配置 |
| ARP | 已知本地 next-hop IPv4，怎样找到当前链路身份 | IP→MAC 邻居缓存 |
| ICMP | 转发/诊断过程中怎样反馈部分事件 | Time Exceeded、Unreachable、Echo 等报文，不形成可靠交付 |

题目出现多个机制时，要按事件依赖顺序调用，而不是因为都“辅助 IP”就混成一步。

## 问题十：IP 多播先分“组身份、成员关系、复制位置”

多播不是“把一个单播地址改成广播地址”。训练时至少分三件事：

```text
multicast group address
-> 当前链路哪些 receiver 对该 group 感兴趣
-> router / forwarding state 在哪些分叉点复制 packet
```

IPv4 多播地址落在 `224.0.0.0/4`。映射到 Ethernet 多播 MAC 时，只复制 IP 多播地址的一部分低位，因此这是**有损映射**，不能用一个多播 MAC 唯一反推出一个 IPv4 group。

### 局部规则：多播题先问“复制发生在哪里”

**触发信号**：题目比较多播与多份单播，或问多播地址/MAC 映射。

**第一动作**：先区分“发送端复制多份单播”与“网络在共享路径之后的分叉点复制多播 packet”。

**检查与退出**：若把多播优势写成“无论接收者多少，网络开销都不变”，立即停止；收益来自共享前缀路径上的复制压缩，不是零成本复制。

## 问题十一：Mobile IP 的核心是 Identity 与 Locator 分离

经典 Mobile IPv4 教材模型维护：

```text
stable home address = identity
current care-of address = current locator
home agent binding: home -> care-of
```

发往 home address 的 packet 按普通路由先到归属网络，再由 home agent 根据 binding 隧道转送到当前位置。移动节点对外发送与对端发往其 home address 的入站路径可以不对称。

### 局部规则：不要把“能发”与“能按 home address 直接收”绑成同一结论

**触发信号**：移动主机已经离开 home subnet，题目问是否还能直接发送/接收。

**第一动作**：分别判断 outbound 普通路由是否可用，以及 inbound `home address` 是否仍会被普通 Internet routing 导向原归属网络。

**检查与退出**：若因为移动节点拥有稳定 home address，就推出普通路由能直接把入站 packet 送到新 LAN，说明漏掉了 locator 变化与 HA binding。

## 题库验证：代表题与变式轴

当前正式题库对 NET04 的覆盖最强，既有地址计算，也有逐跳状态和扩展边界：

| 证据题 | 表面题型 | 实际验证的母模型 |
|---|---|---|
| 847、909 | 路由表 / 默认路由 | packet-time 只对 installed FIB 做 LPM，`/0` 只是最低具体度兜底 |
| 848–859 | 分类地址、CIDR、VLSM、汇总、点到点 | prefix 是地址集合；块大小与对齐先于十进制直觉 |
| 839–846、854 | IPv4 首部/分片/重组 | payload、offset、MF、Identification 分开维护，重组 Owner 在目的主机 |
| 860、862、865–867 | MAC / ARP / 异网段 | Same-Subnet/LPM 先确定 next hop，ARP 只解析当前一跳 |
| 868、869 | TTL / ICMP | hop budget 与差错反馈是逐事件状态，不是“路由器数公式” |
| 870–873 | IPv6 | router 不分片、基础首部无 checksum；“IPv6 完全不能分片”被明确否定 |
| 968 | DHCP 前置条件 | 没有 IP 配置时先 bootstrap，不能跳过配置直接 DNS/TCP |
| 1000 | NAPT | mapping 按 tuple 区分，同一内部 IP 的不同 port 不是同一映射 |
| 891–893 | IPv4 multicast | group address 与 Ethernet 映射、共享路径复制语义 |
| 894–899 | Mobile IP | stable home identity 与 changing care-of locator 分离 |

### 变式轴

1. **Scope**：本地 subnet / 当前 hop / 整条 IP path / mobility binding；
2. **名字类型**：destination IP / prefix / next-hop IP / MAC / NAT tuple / multicast group；
3. **边界计算**：prefix block、LPM、MTU、8-byte offset；
4. **状态创建**：ARP cache、DHCP lease、NAT mapping、HA binding；
5. **协议版本**：IPv4 fragmentation 与 IPv6 PMTU 分支；
6. **逐跳不变量**：无改写时 endpoint IP 保持，而 TTL 与 frame/link identity 改变。

> **仍需补的证据：**二次分片、NAT 返回方向 timeout/回收、DHCP lease 更新生命周期，以及“多播成员状态 × 路由复制状态”的组合题仍偏少。这些是训练层证据缺口，不是 Canonical 机制缺口。

## 题目攻击：逐跳题的答案必须从“当前事件”生成

### 攻击 860：端到端目的与当前链路目的必须同时保留

主机 1 发往远端主机 2 时，IP 首部目的仍是主机 2；Ethernet 1 上的帧目的却是 R1 本地接口 MAC。把两者都写成主机 2，是让 MAC 跨越了 router；把两者都写成 R1，则把 next hop 偷换成 endpoint identity。

**升级动作**：每一跳固定写两行：

```text
packet destination IP = ?
current-link destination identity = ?
```

二者只有在同网段直接交付时才可能指向同一台最终主机。

### 攻击 866：ARP 次数是触发事件数，不是路由器数公式

866 之所以得到 6，是因为题干同时锁死了三个条件：A→B 有 6 段相邻 Ethernet；相关 cache 全空；每段发送者都要先得到本段 next-hop MAC。只要把任一段改成 PPP、把某 cache 改成 hit，或换成 IPv6 ND，固定的“6 次 ARP”立即失效。

**First Divergence**：从拓扑结构直接数 ARP，而没有逐段检查 `Ethernet + next-hop known + cache miss`。

### 攻击 846：分片不是“MTU-首部”一次除法

MTU=1400、header=20 时，普通非末片 payload 不能取 1380，而要向下对齐到 8 B 整数倍 1376；各片 Identification 保持相同，offset 使用原 payload 坐标。题目只要改 header length、再发生二次分片或令 DF=1，机械模板就会失效。

**升级动作**：分片题先建立逐片状态表，再用 payload 守恒、8 B 对齐和最终 MF=0 三类不变量反向验算。

## 代表母题 A：异网段发送时地址分别是谁

主机 A：`192.0.2.10/24`  
默认网关：`192.0.2.1`  
目的 B：`198.51.100.20`

判断：目的不属于 `192.0.2.0/24`。

于是：

```text
packet: src IP = 192.0.2.10, dst IP = 198.51.100.20
next-hop IP = 192.0.2.1
ARP target = 192.0.2.1
outgoing frame dst MAC = gateway MAC
```

路由器收到后删除这个 frame，再为下一跳生成新的 frame；destination IP 在无改写机制时仍是 B。

## 代表母题 B：IPv4 分片

原 payload 为 4000 B，IPv4 header 为 20 B，输出 MTU 为 1500 B。

非末片 payload 最大：

$$
1480\text{ B}.
$$

状态表：

| 片 | payload | total length | offset | MF |
|---|---:|---:|---:|---:|
| 1 | 1480 | 1500 | 0 | 1 |
| 2 | 1480 | 1500 | 185 | 1 |
| 3 | 1040 | 1060 | 370 | 0 |

检查：payload 总和 $1480+1480+1040=4000$ B；前两片 payload 是 8 B 的整数倍；offset 均对应原 payload 坐标。

## 陌生 IP 题固定落笔协议

```text
1. 当前节点是谁？host / router / NAT / DHCP client？
2. 当前名字是什么？destination IP / next-hop IP / MAC / tuple？
3. host 先 Same-Subnet；router 对已安装 FIB 做 LPM。
4. next-hop 确定后才谈 ARP/邻居身份。
5. 每跳维护 TTL/Hop Limit 和新 frame。
6. 比较 packet size 与 outgoing MTU；声明 IPv4/IPv6、DF 和重组 Owner。
7. NAT 写正反向 tuple，不只写一次地址改写。
8. 最后检查作用域：有没有让 MAC、ARP、VLAN 或私网地址越过它不该越过的边界？
```

## 最短压缩

> **先定 Scope 和名字类型：Same-Subnet/LPM 得到 next hop，ARP 只解析当前一跳；逐跳改 TTL 与 frame，分片/NAT 必须维护显式状态表。**
