# DNS、HTTP 与应用层时延

> 训练定位：解决“输入域名/URL 后会发生哪些依赖事件，DNS 怎样沿授权链解析，HTTP 多对象下载如何计算 RTT 与传输时间”的题目族。  
> 模型归属：[NET-08 应用层服务语义](NET-08_应用层服务语义_方法论手册.tex)。DNS hierarchy/delegation/cache、HTTP resource/method/status、FTP 与 Mail 的服务语义由 Canonical 正文拥有；本文件只训练依赖图、报文方向、缓存状态与时延计算。

## 母题表示：应用层题先画“对象依赖图”，再数 RTT

看到“访问网页用了多久”“DNS 查询多少次”“输入 URL 后发生什么”，不要先背 `2RTT`。

先画：

```text
URL / domain
-> DNS result? (cache hit / miss)
-> transport connection exists? (new / reusable)
-> HTTP main object
-> parse main representation
-> discover subresources
-> serial / parallel / multiplexed fetches
```

只有不存在依赖边的步骤才有资格并行。

## 问题一：DNS 先分四个角色

- stub resolver：应用/OS 的本地查询入口；
- recursive resolver：替客户端继续解析并缓存；
- root / TLD / delegated server：通过 referral 指向下一权威边界；
- authoritative server：对自己 zone 中的记录给权威答案。

### 局部规则：递归与迭代说的是“继续查找责任交给谁”

**递归**：被询问者承担继续查找直到形成最终结果/错误的责任。  
**迭代**：被询问者若不是最终 authority，返回 referral，让 caller 自己继续问下一位。

经典常见过程：stub 向本地 recursive resolver 请求递归；resolver 对 root/TLD/authority 链执行迭代式追踪。

### 检查与退出

若画成“本地 DNS 把递归请求交给 root，root 再递归问 TLD、TLD 再递归问 authority”，那只是某种抽象递归示意，不应当成现实 root server 的默认工作模式。训练应以“resolver 负责递归，沿授权链逐级获得 referral”作为稳定事件模型。

## 问题二：DNS cache hit 不是“真相永久正确”

Resolver 先查 cache：

```text
hit + TTL still valid -> reuse cached RR
miss / expired -> query authority chain
```

TTL 是缓存可复用的时间预算，不保证全网同时切换到新值。

### 局部规则：题目问查询次数时，先列已有缓存状态

**触发信号**：题面说 root/TLD/authoritative 地址“已经缓存”“TTL 未过期”。

**第一动作**：删掉已经由 cache 提供的查询步骤，再数剩余真正发出的请求。

**检查与退出**：不能看到域名有三层 label 就固定说“总要问 root、TLD、authority 三次”。缓存会改变路径。

## 问题三：最终 authority 到了以后，不再“找下一级 DNS”

例如解析 `www.abc.com`：当 resolver 已到达对 `abc.com` 负责的 authoritative server，下一步是请求 `www.abc.com` 对应的目标 RR（如 A/AAAA），而不是继续寻找一个“www DNS server”。

> Domain label 的层级 ≠ 每个 label 都对应一台 DNS server。

## 问题四：DNS transport 不能缩成“DNS = UDP”

普通查询常用 UDP；响应截断、zone transfer 或题设要求可靠字节流等情况可用 TCP。

做题时：

```text
先解决 hierarchy / authority / cache / RR 语义
再根据题设决定 transport
```

不能用承载方式替代应用层解析过程。

## 问题五：HTTP 时延题先识别“主 HTML 是第一个对象”

若题目说网页由主文档和若干嵌入对象构成，主 HTML 本身也是需要获取的对象，而且后续对象通常只有在主文档到达并解析后才被发现。

所以依赖图常见：

```text
获取 main HTML
-> parse
-> 才知道 image/css/js 等 subresources
```

这个依赖关系决定主对象与后续对象不能无条件并行。

## 问题六：非持久 HTTP 不能无条件写 `N × 2RTT`

对“新建 TCP + 发请求/收到首字节”的经典简化，一次新连接常产生约 2 个 RTT 的固定等待，再加对象传输时间。

但总时间还取决于：

- 主对象是否先单独获取；
- 后续对象是串行还是并行开多个连接；
- TCP 连接是否已经存在；
- 是否忽略 DNS、握手外延、安全握手、处理与慢启动；
- 不同对象大小是否相同。

### 局部规则：先画批次，再写式子

若非持久并行允许最多 $M$ 个并发连接：

1. 主 HTML 是前置批次；
2. 解析后剩余对象按并发上限划分批次；
3. 每批真正耗时取决于该批中最晚完成的对象，而不是简单把每对象时间求和。

因此 `N × (2RTT + T_data)` 只适用于明确的逐对象串行新连接模型。

## 问题七：持久连接只省“重复建连”，不自动让所有对象同时完成

经典 HTTP/1.1 持久非流水：

- 首对象仍需要建立连接；
- 后续对象可以复用连接；
- 若请求/响应仍串行，每个后续对象仍要等待自己的请求/响应周期。

流水线或 multiplexing 改变的是并发依赖关系，不只是“少一个 RTT”。

### 检查与退出

若把“persistent”直接等同于“所有剩余对象只需 1 个 RTT 总共”，必须先确认题设还允许 pipeline/multiplexing，以及是否忽略数据传输和队头阻塞等因素。

## 问题八：HTTP 总时间固定拆成“依赖等待 + 数据时间”

对每个阶段分别写：

$$
T_{stage}=T_{setup/feedback}+T_{transfer}+T_{processing\ if\ given}.
$$

多个阶段总时间按依赖图取：

- 串行节点：相加；
- 真正并行节点：取完成时间的最大值；
- 有共享瓶颈时：还要服从链路容量，不能让多个“并行下载”各自同时独占满带宽。

## 问题九：TCP 慢启动只在题设要求时加入，不和 HTTP RTT 口诀重复计费

上传速记稿提醒了慢启动可能影响 HTTP 传输，但它给出的固定 RTT 结构不能直接泛化。

训练顺序：

```text
1. 先画 HTTP / TCP 依赖事件
2. 若题设明确给初始 cwnd、MSS、对象大小：
   计算每个 RTT 能发送多少数据
3. 把数据传输轮次接到连接已建立之后
```

不能一边在 `2RTT` 中把 request/response 数据过程完整算过，又额外无条件加一组“慢启动 RTT”。

## 问题十：URL、DNS、IP、Port、MAC 的作用域不能压成一个“地址”

一次 Web 请求可按：

```text
URL identifies application resource
-> DNS maps host name to IP
-> TCP uses IP + port to identify transport endpoints
-> IP forwarding chooses current next hop
-> link layer resolves current-link identity/MAC
```

每个名字服务不同层次。题目一旦跨层，就分别记录，不要让 MAC 或 Port 替代 IP/域名。

## 代表母题 A：DNS cache miss

本地 resolver 没有相关缓存，要解析 `www.example.com`：

```text
stub -> recursive resolver
resolver -> root: ask where .com is
root -> referral to .com
resolver -> .com TLD: ask where example.com is
TLD -> referral to authoritative server
resolver -> authoritative: ask A/AAAA for www.example.com
authoritative -> final RR
resolver caches under TTL -> stub
```

如果 `.com` referral 已在 cache，则跳过 root 查询；如果 `example.com` authority 地址也缓存，继续减少前置步骤。

## 代表母题 B：HTTP 多对象依赖

网页包含：

- 1 个主 HTML；
- 6 个嵌入对象；
- 非持久连接；
- 浏览器最多并行 3 条连接；
- 暂忽略对象传输时间和 DNS。

依赖：

```text
main HTML: 1 batch
parse
6 subresources: ceil(6/3)=2 batches
```

若经典每个新连接批次约付 2 RTT，则固定 RTT 部分是：

$$
2RTT + 2\times2RTT=6RTT.
$$

这里不是 `7对象 × 2RTT = 14RTT`，因为后 6 个对象分两批并行；也不是全部只需 2RTT，因为主 HTML 的发现依赖不能被跳过。

## 问题十一：FTP 与 Mail 题也先拆状态轨迹

### FTP

```text
persistent control connection
-> command decides active/passive data endpoint
-> one data connection for current transfer
-> data connection closes
-> control state remains
```

控制连接与数据连接是两个应用层状态，不要把 FTP 写成“一条 TCP 连接”。

### Mail

```text
user agent submission
-> SMTP relay hop(s)
-> recipient mailbox
-> POP3/IMAP access
```

SMTP 的“下一跳接受”不等于收件人已经读取；MIME 是内容表示扩展，不是 mailbox access 协议。

## 题库验证：代表题与变式轴

应用层题库已经覆盖 DNS、FTP、Mail、HTTP 的主要服务语义，并且能验证“先画对象依赖，再数连接/RTT”的训练方向：

| 证据题 | 表面题型 | 实际验证的母模型 |
|---|---|---|
| 959–962 | C/S 与 P2P | 应用角色组织与底层物理网络/transport 不是同一个维度 |
| 963–973 | DNS | namespace、resolver、authority、recursion/iteration、cache 状态分开 |
| 968、987 | 首次访问前置条件 | 无 IP 配置先 DHCP；有域名且 cache miss 先 DNS，不能直接 TCP |
| 974–981 | FTP | control connection 与 data connection 两条状态轨迹，生命周期不同 |
| 982–986 | SMTP/POP3/MIME | submission/transfer、mailbox access、content representation 分工 |
| 988、990、998 | HTTP Host/method/Cookie | application semantics 不能缩成“端口 + TCP”；业务状态与 HTTP stateless 可并存 |
| 989、991–996、999 | persistent / non-persistent / pipeline / 多对象 | 主 HTML 是依赖前置；先分连接复用与并行批次，再计算 RTT |
| 997 | URL 成功访问所需协议 | DNS、HTTP、TCP、ARP 分属不同 Scope，是否出现由当前状态决定 |

### 变式轴

1. **Authority/Cache**：无缓存、部分 delegation 命中、最终 RR 命中；
2. **查询责任**：recursive / iterative；
3. **连接状态**：新 TCP / persistent reuse / non-persistent；
4. **对象依赖**：main HTML、后续 subresources、是否先解析才能发现；
5. **并发模型**：serial / parallel connections / pipeline / multiplexing；
6. **应用状态**：HTTP stateless 与 Cookie/session、SMTP relay 与 mailbox access。

> **仍需补的证据：**题库对 DNS TTL 更新窗口/negative cache、HTTP resource vs representation、HTTP/2/3 multiplexing 语义、条件请求/cache validator 的训练不足。现有 Canonical 已拥有这些边界，下一步应补代表题而不是复制理论。

## 题目攻击：应用层题先攻击“依赖是否真的存在”

### 攻击 967：DNS 的第一跳由已有知识决定

本地 resolver 只有在“没有该域名、相关 delegation 或更具体 authority 信息”时才从 root 开始。若 `.com` referral 或 `b.com` authority 已缓存，第一跳就应前移到更具体层次。

**First Divergence**：根据域名 label 数量机械决定查询次数，而没有先检查 cache/delegation state。

### 攻击 988：同一个 IP:port 仍可能对应不同 HTTP authority

`www.a.com` 与 `www.b.com` 可以解析到同一服务器 IP、使用同一 TCP port，但 HTTP/1.1 的 `Host`（或后续版本的 authority）仍把两个应用名字空间区分开。transport endpoint 只把 bytes 交给服务进程，不能替应用层决定目标 virtual host。

### 攻击 995：`HTTP/1.1` 本身不能推出 RTT 数

995 之所以是 2 RTT，是因为题干同时给出：TCP 已建立、persistent、先收到 HTML 才知道 3 个图片 URL、随后允许一次 pipeline 三个请求、忽略传输时间。删掉任一条件，答案都可能变化。

**升级动作**：RTT 题先写四格：

```text
connection already established?
persistent?
pipeline / multiplex / parallel?
resource dependency: what must arrive before next request is knowable?
```

### 攻击 997：协议是否出现由初始状态决定，不是固定协议清单

997 指定 DNS 未缓存、next-hop MAC 未缓存，所以 DNS 与 ARP 都会出现；若第二次立即访问且两类 cache 均有效，它们都可能消失。一次 Web 访问不是固定 `DNS→ARP→TCP→HTTP` 列表，而是 `URL + current state` 驱动的事件 DAG；跨层继续转入 [跨层网络请求状态推演](../60_综合专题/NET-I01_一个网络请求的一生/跨层网络请求状态推演.md)。

## 陌生应用层题固定落笔协议

```text
1. 当前应用对象是 domain / resource / file / message？
2. 谁是 authority / owner，谁只是 resolver/cache/client？
3. 先画依赖 DAG，不先数 RTT。
4. DNS：cache -> referral chain -> authority -> RR。
5. HTTP：main object -> parse -> subresources；标串行/并行/复用。
6. 每个 RTT 公式都写明连接是否新建、是否持久、是否流水/并行。
7. 数据传输时间与固定反馈等待分开。
8. 若题设给 TCP cwnd/MSS，再调用 NET06/NET07 加入传输轮次。
9. 最后检查：有没有把 DNS transport 当 DNS 语义、把 HTTP persistent 当自动并行、把 SMTP 当完整邮件读取流程？
```

## 最短压缩

> **应用层性能题先画依赖图：DNS 沿授权链找名字，HTTP 先主对象再发现子资源；串行相加、并行取最慢，RTT 公式必须绑定具体连接模型。**
