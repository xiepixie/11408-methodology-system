# 应用层：把通信能力组织成可发现、可解释的服务

状态：Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建。

> **迁移提示**：以下长篇内容是此前误写在 README 中的 working source。它可用于后续 Source Diff，但不再视为 Handbook 正文。正式手册必须迁入同目录 `.tex`；迁移完成后本 README 将压缩为引子、范围、边界和阅读链接。

## 0. 本册定位

本 Topic 回答：端到端传输只提供 byte stream 或 datagram，应用怎样定义对象、名字、操作、响应和状态，使不同程序能够共同完成 DNS、Web、文件与邮件服务？

本册拥有 application architecture、DNS、HTTP semantics、FTP 与电子邮件的服务分工，以及 application protocol 对 transport service 的选择逻辑。

DHCP 虽以 UDP application protocol 形式运行，但在本项目中由[IP 配置与转发](../04_IP地址_子网与分组转发/README.md)拥有，因为其主要输出是主机进入 IP 世界所需的启动配置。

## 1. 根本问题：transport 不知道“这段 byte 意味着什么”

TCP 可以保证 byte 顺序，却不知道这段 byte 是域名查询、HTTP request、邮件命令还是文件内容。Application protocol 必须定义：

$$
\boxed{
\text{Application object}
\to \text{Name/identifier}
\to \text{Operation}
\to \text{Message representation}
\to \text{Response/state transition}
}
$$

它不仅规定报文格式，还规定动作的语义与交互顺序。相同 transport 可以承载完全不同服务；相同服务语义也可以演进出不同 transport bindings。

## 2. 应用架构：谁长期持有状态

### 2.1 Client/Server

server 通常在稳定地址/名字上等待请求并持有共享服务状态；client 主动发起交互。集中服务便于管理、一致性和发现，代价是容量、故障和运营中心化。

### 2.2 Peer-to-Peer

peer 同时消费和提供资源，容量可随参与者增加，但发现、可用性、信任、NAT 穿越和一致性更复杂。

C/S 与 P2P 是状态与职责的组织方式，不等同于 TCP/UDP，也不由“是否有服务器进程”一个表象决定。

## 3. DNS：把一个集中表拆成层次化授权系统

### 3.1 为什么单一 `hosts` 文件失败

全网共享一份名字表会遇到：更新冲突、分发延迟、单点容量与管理边界。DNS 的生成链是：

$$
\boxed{
\text{Global flat file fails}
\to \text{Hierarchical namespace}
\to \text{Delegated zones}
\to \text{Distributed authoritative servers}
\to \text{Resolver + cache}
}
$$

Domain namespace 是名字树；zone 是某个 authority 实际管理的数据边界。树的结构与管理分区相关，但 domain 不等于一台主机或一个物理网络。

### 3.2 四类对象

- stub resolver：应用/OS 发起查询的本地接口；
- recursive resolver：代用户完成后续查询并缓存；
- authoritative name server：对某 zone 的数据负责；
- root/TLD/other delegated servers：通过 referral 把查询逐步引向 authority。

### 3.3 一次 cache miss 的解析轨迹

```text
application asks local resolver
-> recursive resolver checks cache
-> root referral identifies TLD servers
-> TLD referral identifies authoritative servers
-> authoritative answer returns records
-> resolver caches answer/referrals under TTL
-> result returns to application
```

迭代查询返回“我不知道最终答案，但下一步问谁”；递归查询把继续查找的责任交给被询问方。实际 client-to-recursive 常请求递归，resolver 对 authority 链执行迭代式追踪。

### 3.4 Cache 的正确性边界

cache 用旧信息换低延迟和低查询负载。TTL 限制可复用时间，但 DNS 不是瞬时全局一致系统：更新在 TTL 生命周期内可能与缓存旧值并存。

DNS 并非只能用 UDP。经典普通查询常用 UDP；响应截断、zone transfer 等情形可使用 TCP，现代部署还存在加密传输。408 做题要服从题设，不能把“DNS=UDP”写成协议语义。

## 4. HTTP：操作资源的统一语义

HTTP 的核心对象不是“网页文件”，而是由 URI 标识的 resource。消息传输的是 resource 的 representation，method 表达 client 希望对目标执行的语义。

$$
\boxed{
\text{Target resource}
\to \text{Method semantics}
\to \text{Request metadata/content}
\to \text{Status}
\to \text{Representation/metadata}
}
$$

### 4.1 Resource 不等于 representation

同一 resource 可根据时间、语言、编码或内容协商产生不同 representation。response body 是某次选定表示，不等于资源本身的全部身份。

### 4.2 Method 属性改变重试决策

- safe：语义上只读，例如 GET/HEAD；
- idempotent：重复执行与执行一次具有相同预期 effect，例如 PUT、DELETE 以及 safe methods；
- POST 通常不假定 idempotent。

这些属性不是礼貌标签，而是 cache、proxy、client 在失败后能否自动重试的重要决策依据。

### 4.3 Stateless 不等于“服务没有状态”

HTTP stateless 表示每个 request 的语义不依赖 server 必须记住此前 protocol request context。应用仍可通过 cookie、token、database 和 server-side session 建立业务状态。

### 4.4 语义与连接版本分离

- HTTP/1.1 和 HTTP/2 通常在 TCP 上承载；
- HTTP/3 使用 QUIC over UDP；
- 核心 method、status、representation 和 cache semantics 在版本间保持共同定义。

因此“HTTP 使用 TCP”是特定版本/部署的 transport mapping，不是 HTTP resource semantics 本身。

## 5. Web 性能从依赖图生成

取得一个 URL 可能依次触发：DNS、transport/security establishment、HTTP request/response、HTML parsing、更多 subresource requests。

总时间不能只数“几个 RTT”，必须先画依赖关系：哪些步骤串行、哪些 connection 可复用、哪些 object 可并行、哪些命中 cache。

Persistent connection 减少重复建立连接；multiplexing 允许多个 request/response 共享连接并发推进；cache 用 freshness/validation 状态减少传输。三者解决的瓶颈不同。

## 6. FTP：控制状态与数据传输分离

FTP 的母问题是跨异构系统可靠操作和传输文件。它使用持久 control connection 交换命令与会话状态，并为目录/文件数据建立独立 data connection。

这种 out-of-band control 让命令不被大文件数据阻塞，也带来额外连接管理、主动/被动模式和 NAT/firewall 适配成本。FTP 的两条 TCP connections 是应用层设计，不是 TCP 自动生成的“控制通道”。

## 7. 电子邮件：提交、转发、存储、读取不是一个协议

邮件系统至少有：user agent、mail server、message transfer 和 mailbox access。

```text
sender user agent
-> submission / SMTP transfer
-> one or more mail servers
-> recipient mailbox
-> POP3 or IMAP access
-> recipient user agent
```

- SMTP 负责提交/服务器间 push 式传送；
- POP3 提供较简单的 mailbox download/access 模型；
- IMAP 更强调服务器端 mailbox 状态与多设备同步；
- MIME 扩展 message representation，使非 ASCII 内容和附件可被邮件体系承载。

“发邮件”和“收邮件”必须分开建模，不能把所有过程归给 SMTP。

## 8. 怎样选择 transport service

应用选择的不是协议名偏好，而是约束组合：

| 应用需求 | 需要观察的 transport 能力 |
|---|---|
| 不能丢 byte、允许额外延迟 | reliable ordered stream |
| 保留 message boundary、自定义恢复 | datagram |
| 极低启动延迟 | connection setup cost |
| 多路流并发且减少队头阻塞 | multiplexing semantics |
| 广播 bootstrap | local datagram/broadcast support |
| 安全身份与机密性 | security layer/secure transport |

“实时应用一定用 UDP”“可靠应用一定用 TCP”都过度简化。应用可在 UDP 之上实现可靠/拥塞控制，或为穿越部署环境选择 TCP；判断必须回到服务需求与实现责任。

## 9. 概念边界

| 概念 A | ≠ | 概念 B | 真正区别与题目信号 | 混淆后果 |
|---|:---:|---|---|---|
| Domain name | ≠ | IP address | 人/组织命名与网络定位；DNS 维护映射 | 把 DNS 当逐跳路由 |
| Domain | ≠ | Zone | 名字树节点/子树与 authority 管理边界 | 授权与层次结构混乱 |
| Recursive query | ≠ | Iterative query | 被询问方完成解析；被询问方返回 referral | DNS 报文轨迹画错 |
| Resource | ≠ | Representation | 被标识对象与某次可传输表示 | 缓存和内容协商理解错误 |
| HTTP stateless | ≠ | Application has no state | 协议请求独立与业务状态存在可并存 | 认为登录/cookie 违反 HTTP |
| HTTP semantics | ≠ | HTTP transport version | method/status/resource 与具体连接承载分离 | 把 HTTP/3 误判为非 HTTP |
| SMTP | ≠ | POP3/IMAP | 邮件传送与 mailbox access | 邮件全流程协议归属错误 |
| FTP control connection | ≠ | FTP data connection | 命令状态与内容传输分离 | 端口/连接数量推演错误 |

## 10. 做题调用协议

1. 写应用对象：name、resource、file、message 还是 lease/config；
2. 写谁持有 authority/state，谁只是 cache/client；
3. 画 request/response 或 push/pull 的事件方向；
4. DNS 题区分 recursion、iteration、authority、cache TTL；
5. HTTP 题区分 resource、representation、method 和 connection；
6. 邮件题拆成 submission/transfer/storage/access；
7. 性能题画依赖 DAG，再数不可并行的 RTT/transfer；
8. 最后检查 transport 选择是否来自应用约束而非口诀。

## 11. 贯穿母例：输入 URL 后第一个 HTTP request 为什么还不能立刻发

```text
URL identifies scheme + authority + target
-> resolver needs server IP (unless cached)
-> IP forwarding needs next hop and local MAC (unless cached)
-> transport/security context may need establishment
-> HTTP request names resource and method
-> response carries status + selected representation
-> representation may reveal more resource dependencies
```

URL、domain、IP、port、MAC 分别服务不同作用域。把它们压成一句“浏览器访问服务器”，会隐藏几乎所有可诊断的状态交接。

## 12. 高频 First Divergence

- 把 DNS 说成从 root 一次返回最终 IP：漏掉 delegation/referral；
- 认为 cache 命中永远是最新真相：忽略 TTL 与弱一致时间窗；
- 写“DNS 用 UDP，HTTP 用 TCP”作为完整机制：把常见承载当唯一语义；
- 把 HTTP stateless 理解成网站不能登录：混淆 protocol context 与 application state；
- 把 response body 等同 resource：混淆对象与 representation；
- 用 SMTP 从 mailbox 下载邮件：没有分开 transfer 与 access。

## 13. 一页压缩与复原问题

$$
\boxed{
\text{Name an application object}
\to \text{Choose operation semantics}
\to \text{Represent in messages}
\to \text{Map onto transport}
\to \text{Evolve application state}
}
$$

1. DNS 怎样用 delegation 替代全球单表？
2. cache 为什么同时提高性能并引入旧信息窗口？
3. HTTP resource 与 representation 为什么必须分开？
4. stateless protocol 怎样支撑有状态登录业务？
5. SMTP、POP3/IMAP 和 MIME 分别拥有邮件过程的哪一段？

## 14. 来源与校正说明

- 归档笔记《应用层-FTP,SMTP,POP3,DHCP》提供传统应用协议覆盖；《应用层-DNS》《应用层-WWW与HTTP》为空文件，未被当作已有正文；
- DNS 的 hierarchy、delegation、resolver、authority 与 cache 边界依据 [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034.html) 校正；
- HTTP 的 stateless semantics、resource/representation 和跨版本语义边界依据 [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) 校正；
- DHCP 已按当前 Ownership 移入 IP Topic，不在应用册重复拥有。
