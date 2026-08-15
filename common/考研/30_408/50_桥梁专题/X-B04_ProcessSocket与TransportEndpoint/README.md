# X-B04｜Process / Socket × Transport Endpoint

状态：Candidate Core；接口结构已确认，是否升级为 Core 待 408 考纲/真题覆盖证据与重复调用证据。

## Owners
OS01 Process/Control、OS04 I/O ↔ NET06 Transport/TCP。

## Mother Interface
`Process Action -> System Call / Socket Object -> Transport Endpoint/Port/Connection State -> Data/Event -> Buffer/Availability -> Wake/Return`

网络接收侧候选轨迹：

```text
remote packet
-> NIC / DMA / completion
-> kernel network stack
-> transport endpoint lookup
-> socket receive buffer
-> blocked process wakeup
-> scheduler
-> recv/read returns to application
```

这条轨迹只用于核对交接点：NIC/DMA/中断属于 X-B03 及计组/OS I/O，transport endpoint 与报文语义属于网络，socket object、buffer availability、block/wakeup 与返回属于 OS。是否建立完整跨科 Integration 仍受本 Bridge 的 Promotion Evidence Gate 约束。

## Owns
process-visible send/receive 行为怎样与 transport endpoint 的网络状态交接；blocking receive 的“数据未到—等待—事件到达—可返回”接口。

## Responsibility Split
- OS：process、system call、socket/file-like object、block/wakeup 与本地 buffer 可用性；
- Network：port、UDP/TCP endpoint、connection/sequence state 与 transport semantics。

## Extension Boundary
完整 kernel protocol stack、driver ring、NIC queue、NAPI、zero-copy 等工程细节不进入 408 Core。

## Promotion Evidence Needed
真题/大纲中是否反复要求该接口；是否在多个独立问题中产生不可替代的新推理。未验证前不得把“工程上真实”自动等同“408 Core”。

## Review v1

接口通过第一道 Bridge Validity：process-visible action、socket object、transport endpoint、buffer availability 和 wake/return 的交接可稳定复用。第二道 Promotion Gate 尚未通过；下一轮需用 408 真题/考纲确认重复调用，并区分 `recv` 阻塞、TCP 状态和 X-B03 设备完成路径。

## Coverage Audit v1（2026-08-12）

覆盖核对结论仍为 **Candidate Core / No Canonical Update**。RFC 9293 与 POSIX `recv()` 证实该接口在真实系统中存在；NET06 已拥有端点/端口/连接语义，OS Topic 已拥有进程、文件式对象和阻塞/唤醒机制，NET-I01 明确在内核接收唤醒前停止。仓库目前没有两道独立的 408 题目证据，能证明该交接产生不可替代的重复推理，因此不新建 X-B04 `.tex`，也不把工程栈细节并入 408 Core。

详细事实、门槛判定与下一步证据要求见 [X-B04 覆盖核对记录](../../../80_evidence/archive/review_log/2026-08-12/2026-08-12_X-B04_覆盖核对.md)。
