# OS-B01｜Wait / Block / Wakeup

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS01 Process/Scheduling ↔ OS02 Concurrency ↔ OS04 I/O。

## Mother Interface
`Condition Unsatisfied -> Enqueue -> Block -> Event/Condition Change -> Wake -> Runnable -> Schedule`

## Owns
不同机制为什么最终都通过等待队列与 task state 完成“暂停执行—条件满足—恢复竞争 CPU”的交接。

## Boundary
同步条件、I/O 完成机制、调度策略分别由各 Topic Own；本 Bridge 只拥有状态与控制权 handoff。

## Manual
- [Canonical 正文](OS-B01_WaitBlockWakeup_桥梁手册.tex)
- [Published PDF](../../../../90_publish/OS-B01_WaitBlockWakeup_桥梁手册.pdf)

## Review v1
已核对 lost wakeup、wake 不等于立即运行、wake 后重新检查条件三个边界；下一轮用同步、I/O、条件变量三类题分别验证。
