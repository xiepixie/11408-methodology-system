# TCP 丢包证据与可靠性映射

> 训练定位：解决“同一个 TCP 丢包/乱序事件，怎样同时用通用可靠传输不变量和 TCP byte sequence 解释，并判断 ACK、duplicate ACK、RTO、重传到底能证明什么”的跨接口题。  
> 模型归属：[NET-B03 Reliable Transfer × TCP](NET-B03_ReliableTransfer与TCP_桥梁手册.tex)。NET03 拥有一般可靠性机制与不变量，NET06 拥有 TCP byte stream/segment/connection state；本文件只训练两套语言的映射与类比停止条件。

## 母题表示：先写“真实事件”，再写“发送端可观察证据”

网络中真实发生的事情和发送端能知道的事情不是同一个对象。

例如某 TCP data segment 丢失：

```text
真实网络事件：middle byte interval 没到接收端
发送端直接可见：无
后续证据：duplicate ACK / SACK / RTO 等
```

因此不能写：

```text
segment 丢失
-> sender 立刻知道丢失
-> sender 立刻重传
```

发送端只能根据有限证据推断。

### 局部规则：先区分 Truth 与 Evidence

**触发信号**：题目写“某段丢失/乱序”，又要求发送端动作。

**第一动作**：分两栏：左边写题设告诉我们的真实事件；右边只写 sender 实际收到的 ACK/SACK/timer evidence。

**检查与退出**：若 sender 的动作依赖一个它当前没有收到的事实，停止并寻找真正的观测信号。

## 代表母题 A：中间字节区间丢失，后段先到

A 连续发送：

```text
S1 = [1000,1500)
S2 = [1500,2000)
S3 = [2000,2500)
```

假设 S2 丢失，S1、S3 到达 B，B 允许缓存失序数据。

### 用一般可靠传输语言看

必须保持：

- 已正确交付的连续前缀不能出现洞；
- 重复到达不能重复交付；
- 丢失数据最终要通过某种证据触发恢复。

### 用 TCP byte-space 看

收到 S1 后：

```text
continuous prefix = [1000,1500)
ACK = 1500
```

S3 先到：

```text
[2000,2500) 可缓存
但 [1500,2000) 仍缺
累计 ACK 仍停在 1500
```

如果更多后续 segment 到达，它们可能继续触发 `ACK=1500` 的 duplicate ACK。若达到题设 fast-retransmit 阈值，或 RTO 先到期，sender 才进入对应重传分支。

S2 重传并补洞后，若 S3 已缓存：

```text
continuous prefix 一次推进到 2500
ACK 可跳到 2500
```

这不是“ACK 跳过了未收到数据”，而是缺口补齐后原缓存区间一起进入连续前缀。

## 映射表：一般机制如何落成 TCP 字段/状态

| 通用可靠性对象 | TCP 投影 |
|---|---|
| 数据身份 | byte sequence interval `[SEQ, SEQ+LEN)` |
| 正确认可证据 | cumulative ACK；可选 SACK |
| 未确认集合 | sent but not cumulatively ACKed byte intervals |
| 恢复触发 | RTO、duplicate ACK pattern 等 |
| 重复抑制 | receive byte state / already received intervals |
| 按序交付 | 只把连续 byte prefix 推给应用 |

### 局部规则：ACK number 是边界，不是“某个包编号”

**触发信号**：题目同时给 `SEQ`、payload length 与 ACK。

**第一动作**：把每个 TCP segment 先翻译成半开 byte interval，再维护连续前缀边界。

**检查与退出**：若 `ACK=1500` 被解释为“1500 号 segment 已收到”，或每个 segment 只让序号 `+1`，说明仍在用 frame-sequence 直觉硬套 TCP。

## 问题二：为什么 GBN 类比有用，但不能把 TCP 判成 GBN

GBN 帮助解释：

- cumulative ACK；
- 连续前缀前不能越过洞；
- 一个缺口可能让后续确认不推进。

但 TCP 不能因此等同 GBN，因为 TCP：

- sequence unit 是 byte，不是 frame；
- receiver 可以缓存失序 data；
- 可有 SACK；
- 重传策略不必是“从 base 起把所有 outstanding 全部重传”。

### 局部规则：类比只保留共享不变量，不复制完整状态机

**触发信号**：题目问“TCP 更像 GBN 还是 SR”或要求用滑动窗口模型解释 TCP。

**第一动作**：先指出具体共享结构，如 cumulative ACK 或 out-of-order buffering，再明确不同点。

**检查与退出**：一旦类比要求 TCP 丢弃所有失序段、或每次超时重传全部 outstanding，就应停止类比并回到 TCP 自身状态。

## 问题三：RTO 与 duplicate ACK 为什么是不同证据

### RTO

表示某个可靠发送对象在足够长时间内没有获得所需确认。它是“等待过久”的证据，不直接说明究竟是 data、ACK 丢失还是异常延迟。

### Duplicate ACK

重复声明同一连续前缀，通常说明：

```text
缺口仍在
但缺口之后又有一些 data 到达
```

因此它比单纯沉默提供了更多结构信息，但仍不是数学上百分之百的“该 segment 必丢失证明”，因为 reordering 也可能制造重复 ACK。

### 检查与退出

可靠性层只负责“哪个 evidence 足以触发 recovery”；duplicate ACK / timeout 导致 `cwnd` 怎样变化则进入 NET07，不在本 Bridge 里重复拥有。

## 题库证据与当前缺口

现有题库已经分别验证：

- 761–773：Stop-and-Wait / GBN / SR 的一般 Seq-ACK-Timer-Window 模型；
- 913：可靠性来自确认、序号与必要重传的闭环；
- 932、937、945、946：TCP cumulative ACK 与 byte sequence；
- 951、956：ACK 粒度与 TCP 拥塞窗口增长不能混淆。

但没有单题真正要求把“通用可靠性不变量 -> TCP byte interval -> duplicate ACK/RTO evidence -> recovery action”完整走完。因此下一轮直接从 **945/946** 做最小攻击变形：保留它们的 byte-sequence 计算，只让中间区间丢失、后续区间先到，再追加“接收端缓存失序数据、随后出现若干 duplicate ACK”。若解题仍只会算 ACK 数值、却不能区分 Truth/Evidence 和 recovery trigger，就说明 Topic 知识尚未跨过 B03。后续应优先用真题/错题替换或补强。

### 回归攻击：ACK 跳跃必须由“补洞 + 已缓存区间”解释

从 945 派生的缺口题完成重传后，把后续缓存区间删除再重算：累计 ACK 不应再一次跳过它；把缓存区间恢复，ACK 才能在缺口补齐后跨越多个 byte interval。这个对照只改变一个状态变量，可以检查学习者究竟理解了“连续前缀”，还是只背了某个 ACK 数字。

## 变式轴

1. 缺口在第一个/中间/最后 segment；
2. receiver 丢弃或缓存失序 bytes；
3. 后续到达数量是否足以形成 fast-retransmit evidence；
4. RTO 与 duplicate ACK 谁先发生；
5. ACK 丢失但后续 cumulative ACK 覆盖；
6. SACK 开/关；
7. 重传后 ACK 一次跳过多个已缓存区间。

## 陌生题固定落笔协议

```text
1. 把每个 TCP segment 写成 byte interval。
2. 分开真实网络事件与 sender 可见 evidence。
3. 维护 receiver 连续前缀与可选乱序缓存。
4. cumulative ACK 只移动到第一个缺口。
5. timer / duplicate ACK 只在满足题设阈值后触发恢复。
6. 重传后重新判断连续前缀是否可一次跨过缓存区间。
7. 拥塞窗口变化交给 NET07，不在可靠性桥里抢 Owner。
8. 最后检查：类比 GBN/SR 是否越过共同不变量的边界。
```

## 最短压缩

> **TCP 可靠性题先做 Truth/Evidence 分离：字节区间是真正的数据身份，ACK 是连续前缀证据，RTO/dupACK 只是恢复触发信号；GBN/SR 只能解释共享不变量，不能替代 TCP 自身状态机。**
