# 可靠传输：用有限状态驯服丢失、损坏与乱序

状态：工作稿，待人工确认。

## 0. 本册定位

本 Topic 回答：下层只提供可能损坏、丢失、重复和乱序的交付时，通信端点怎样共同制造“正确且不重复”的可靠服务？

本册拥有 sequence number、ACK、timer、retransmission、sender/receiver window、Stop-and-Wait、GBN、SR，以及窗口利用率与序号空间约束。

本册建立通用可靠传输机制，不把它等同于 TCP。TCP 如何把 byte stream、连接状态与这些机制组合，见[传输层与 TCP](../06_传输层_端点_UDP与TCP状态机/README.md)；`cwnd` 不属于本册，见[拥塞控制](../07_拥塞_共享资源与反馈控制/README.md)。

## 1. 根本问题：沉默不能说明发生了什么

发送一个数据单元后没有收到反馈，至少存在三种解释：

1. 数据丢失；
2. 数据到达，但 ACK 丢失；
3. 数据或 ACK 仍在路上。

端点没有全局观察者，不能直接知道网络内部发生了什么。可靠传输只能通过有限的报文和本地时间推断状态：

$$
\boxed{
\text{Error detection}
\to \text{Identity}
\to \text{Feedback}
\to \text{Timeout}
\to \text{Retransmission}
\to \text{Duplicate suppression}
}
$$

可靠不是某一个字段的性质，而是发送方与接收方状态机形成的闭环。

## 2. 五个最小机制为什么缺一不可

### 2.1 Error detection：先知道“这个副本不能信”

校验和或 CRC 让接收方检测部分传输错误。检测失败通常触发丢弃或 NAK，但它不能恢复原数据。

### 2.2 Sequence number：给传输实例一个可比较身份

重传会产生多个内容相同的副本。若没有序号，接收方无法判断“这是新数据还是旧数据重传”。序号还为顺序和累计确认提供坐标系。

### 2.3 ACK：把接收端知识反馈给发送端

ACK 的语义必须先写清：确认单个序号、累计确认到某个序号，还是声明下一个期望序号。不同教材或协议可能采用不同记法，不能只凭 `ACK(n)` 猜。

### 2.4 Timer：把无限等待变成可执行分支

发送方无法等到“确定丢失”，只能在等待超过阈值后推定本次尝试失败。Timer 太短会产生伪重传，太长会延迟恢复。

### 2.5 Retransmission + duplicate suppression

超时重传解决可能丢失；序号与接收状态消除重传造成的重复交付。二者共同把“至少一次尝试”收缩为“至多一次向上交付”。

## 3. Stop-and-Wait：最小闭环

发送方状态：

```text
Ready(n)
-> send packet(n), start timer
-> WaitACK(n)
   -> valid ACK(n): stop timer, n toggles, Ready(next)
   -> timeout: resend packet(n), restart timer
```

接收方状态：

```text
Expect(n)
-> valid packet(n): deliver once, send ACK(n), Expect(next)
-> duplicate/out-of-order: do not deliver, repeat appropriate ACK
-> corrupted: discard or send feedback according to protocol
```

1-bit 序号足以支持 Stop-and-Wait，因为任意时刻只需区分当前新 packet 与上一个 packet 的迟到/重传副本。

### 3.1 正确性不变量

- 发送方收到足以推进状态的确认前，不复用当前序号；
- 接收方只把当前期望序号向上交付一次；
- ACK 丢失可以造成重复传输，但不能造成重复交付。

### 3.2 性能失败

若数据发送时间为 $T_D$、单向传播时延为 $T_P$，并把 $RTT$ 简化为 $2T_P$，忽略 ACK 发送与处理：

$$
U\approx\frac{T_D}{T_D+RTT}.
$$

当 $RTT\gg T_D$，链路大部分时间空闲。可靠性已经成立，但吞吐能力没有被利用，于是需要流水线。

## 4. Sliding Window：把等待时间变成在途数据

窗口不是“批量发送”的口诀，而是对允许未确认序号集合的约束：

$$
\boxed{
\text{Past ACKed}
\mid \text{Sent unACKed}
\mid \text{Usable unsent}
\mid \text{Not yet allowed}
}
$$

ACK 到达使左边界右移，释放新的序号。窗口同时承担：

- correctness：限制哪些序号当前合法；
- flow of work：允许多少数据在反馈返回前继续发送；
- bounded state：限定发送方、接收方和缓冲区必须维护多少状态。

若窗口含 $W$ 个等长 frame，ACK 发送时间为 $T_{ACK}$，理想无差错利用率近似：

$$
U=\min\left(1,\frac{W T_D}{T_D+RTT+T_{ACK}}\right).
$$

公式必须从时间线生成。题目忽略 ACK 发送时间时才去掉 $T_{ACK}$。

## 5. GBN：用接收端简单换取批量回退

GBN 的接收窗口通常为 1：只接收当前期望 frame，失序 frame 不缓存。发送方允许多个未确认 frame 在途，并使用累计确认。

### 5.1 生命周期

```text
sender sends base ... nextseq-1
-> receiver accepts only expected frame
-> cumulative ACK advances base
-> if oldest unACKed timer expires
-> resend base and every later outstanding frame
```

### 5.2 为什么只需一个主计时器

累计确认使最老未确认 frame 成为窗口能否前进的阻塞点。其超时后，后续在途 frame 即使曾正确到达也可能因接收方不缓存而需要一起重传。

### 5.3 序号空间约束

若序号字段为 $k$ bit，在 408 常用模型中：

$$
W_T\le 2^k-1,
\qquad W_R=1.
$$

必须保留至少一个序号不在当前发送窗口中，才能让新一轮窗口与旧副本保持可区分。

## 6. SR：用更多状态换取精准恢复

SR 的接收方可以缓存窗口内失序 frame，并逐个确认；发送方通常为每个未确认 frame 维护独立计时状态。丢一个 frame 时只重传所缺 frame。

### 6.1 生命周期

```text
frame n arrives within receive window
-> if first valid copy: buffer and ACK n
-> if n equals receive base: deliver n and consecutive buffered frames
-> slide receive window over delivered prefix
```

接收方可以“已收到但暂不能交付”。这说明 reception state 与 delivery state 不是同一件事。

### 6.2 序号复用为什么会产生歧义

序号是有限循环空间。若发送窗口和接收窗口覆盖范围过大，一个迟到的旧 frame 可能落入新一轮接收窗口，并被误认为新 frame。

通用不歧义条件是：

$$
W_T+W_R\le 2^k.
$$

常用对称窗口下：

$$
W_T=W_R\le 2^{k-1}.
$$

这个约束不是为了“方便计算”，而是为了让接收方仅凭有限序号和当前窗口就能判定身份。

## 7. GBN 与 SR 的真正权衡

| 维度 | GBN | SR |
|---|---|---|
| 接收失序 frame | 丢弃 | 缓存 |
| ACK | 通常累计 | 通常逐 frame |
| 超时恢复 | 从缺口开始批量重传 | 只重传具体缺失 frame |
| 接收端状态 | 小 | 大 |
| 发送端 timer | 通常最老 frame 一个主 timer | 每个未确认 frame 独立状态 |
| 高误码链路代价 | 重传浪费较大 | 状态和实现复杂度较大 |

SR 不是无条件更好。链路很可靠、窗口较小或接收资源受限时，GBN 的简单性可能更值钱。

## 8. 概念边界

| 概念 A | ≠ | 概念 B | 真正区别与题目信号 | 混淆后果 |
|---|:---:|---|---|---|
| Detection | ≠ | Recovery | 检错指出异常；反馈/超时/重传恢复 | 认为 CRC 自带重传 |
| Receive | ≠ | Deliver | frame 可到达并缓存，但未必按序交给上层 | SR 状态推演错误 |
| ACK loss | ≠ | Data loss | 前者接收方已有数据；后者没有 | 漏掉重复抑制分支 |
| Window size | ≠ | Sequence space | 窗口是当前合法集合；序号空间是循环身份全集 | GBN/SR 最大窗口算错 |
| Reliability | ≠ | Flow control | 前者保护数据交付；后者保护接收缓冲 | 把 `rwnd` 当作可靠性条件 |
| Flow control | ≠ | Congestion control | 前者看 receiver；后者看 network path | 把 `rwnd`、`cwnd` 合并成一个含义 |
| Timeout | ≠ | Proof of loss | 超时是基于本地时钟的推断，不是全局事实 | 无法解释伪重传 |

## 9. Verification：状态题怎样提前发现错误

每一步检查四个集合：

1. 已确认/已交付的连续前缀；
2. 已发送未确认集合；
3. 已接收但未交付缓存；
4. 当前窗口允许的新序号。

再检查三个不变量：

- 同一数据不能向上交付两次；
- 窗口只跨过连续满足条件的前缀；
- 当前接受区间不能与仍可能出现的旧副本产生身份歧义。

## 10. 做题调用协议

1. 先写 ACK 语义和接收方是否缓存失序 frame；
2. 画 sender/receiver 两条时间线，标出发送、到达、ACK、超时；
3. 每个事件后更新 base、nextseq、buffer、timer；
4. 窗口题先判断 GBN 还是 SR，再写对应不歧义条件；
5. 利用率题从一个 frame 的反馈周期推导，不先套公式；
6. 有误码/丢包时同时算重传数据量和状态成本；
7. 最后用“是否可能重复交付”攻击结果。

## 11. 贯穿母例：ACK 丢失为什么不会破坏可靠性

Stop-and-Wait 中，发送方发送 frame 0；接收方正确接收、交付并回 ACK 0，但 ACK 丢失：

```text
sender remains WaitACK(0)
-> timer expires
-> sender retransmits frame 0
-> receiver is already Expect(1)
-> recognizes duplicate 0, does not deliver again
-> repeats ACK 0
-> sender advances to frame 1
```

重传保证 progress，序号与接收状态保证 safety。可靠性的两面分别是：

$$
\boxed{\text{eventually make progress}}
\qquad
\boxed{\text{never deliver the wrong instance twice}}.
$$

## 12. 高频 First Divergence

- 看见丢包直接重传：没有说明谁、凭什么知道丢失；
- ACK 到达就把窗口跳到该序号之后：没有确认 ACK 是累计还是选择确认；
- SR 收到失序 frame 立即交付：混淆 buffer 与 in-order delivery；
- GBN 只重传超时的一个 frame：把恢复策略套成 SR；
- 只背 $2^k-1$ 或 $2^{k-1}$：没有从旧/新副本不歧义生成约束；
- 利用率超过 1：没有执行饱和截断或时间线有重复计数。

## 13. 一页压缩与复原问题

$$
\boxed{
\text{Detect}
\to \text{Number}
\to \text{Acknowledge}
\to \text{Time out}
\to \text{Retransmit}
\to \text{Suppress duplicate}
}
$$

1. 为什么“没收到 ACK”不能等价为“数据丢了”？
2. Stop-and-Wait 为什么 1-bit 序号足够？
3. 窗口怎样把传播等待转化为在途数据？
4. GBN 和 SR 各把复杂度放在哪一端？
5. SR 的序号空间约束怎样从迟到旧 frame 推出？

## 14. 来源与校正说明

- 归档笔记《链路层-流量控制与可靠传输》《公式汇总》提供 GBN/SR 考点和旧计算模型；
- 本册把可靠传输提升为跨层可复用机制，避免被旧目录永久绑定在链路层；
- ACK 记号在不同教材中可能不同，正文要求先声明语义，不把单一记法冒充协议普遍事实。
