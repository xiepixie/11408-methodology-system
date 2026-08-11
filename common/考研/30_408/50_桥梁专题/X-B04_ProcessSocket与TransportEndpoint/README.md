# X-B04｜Process / Socket × Transport Endpoint

状态：Candidate Core；接口结构已确认，是否升级为 Core 待 408 考纲/真题覆盖证据与重复调用证据。

## Owners
OS01 Process/Control、OS04 I/O ↔ NET06 Transport/TCP。

## Mother Interface
`Process Action -> System Call / Socket Object -> Transport Endpoint/Port/Connection State -> Data/Event -> Buffer/Availability -> Wake/Return`

## Owns
process-visible send/receive 行为怎样与 transport endpoint 的网络状态交接；blocking receive 的“数据未到—等待—事件到达—可返回”接口。

## Responsibility Split
- OS：process、system call、socket/file-like object、block/wakeup 与本地 buffer 可用性；
- Network：port、UDP/TCP endpoint、connection/sequence state 与 transport semantics。

## Extension Boundary
完整 kernel protocol stack、driver ring、NIC queue、NAPI、zero-copy 等工程细节不进入 408 Core。

## Promotion Evidence Needed
真题/大纲中是否反复要求该接口；是否在多个独立问题中产生不可替代的新推理。未验证前不得把“工程上真实”自动等同“408 Core”。
