# OS-B01｜Wait / Block / Wakeup

状态：目录已建立，正文未建。

## Owners
OS01 Process/Scheduling ↔ OS02 Concurrency ↔ OS04 I/O。

## Mother Interface
`Condition Unsatisfied -> Enqueue -> Block -> Event/Condition Change -> Wake -> Runnable -> Schedule`

## Owns
不同机制为什么最终都通过等待队列与 task state 完成“暂停执行—条件满足—恢复竞争 CPU”的交接。

## Boundary
同步条件、I/O 完成机制、调度策略分别由各 Topic Own；本 Bridge 只拥有状态与控制权 handoff。
