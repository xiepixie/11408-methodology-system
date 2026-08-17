# OS-B01｜Wait / Block / Wakeup

状态：已采用；Canonical Bridge 正文已建立并发布。

## Owners
OS-01/02 Process/Scheduling ↔ OS-03 Concurrency ↔ OS-05 I/O。

## Mother Interface
`Condition Unsatisfied -> Register Wait + Block Safely -> Event/State Change -> Wake Eligible -> Ready/Runnable -> Scheduler/Dispatch -> Recheck if required`

## Owns
不同机制为什么最终都通过等待队列与 task state 完成“暂停执行—条件满足—恢复竞争 CPU”的交接。

## Boundary
同步条件、I/O 完成机制、调度策略分别由各 Topic Own；本 Bridge 只拥有状态与控制权 handoff。

## Manual
- [Canonical 正文](OS-B01_WaitBlockWakeup_桥梁手册.tex)
- [Published PDF](../../../../90_publish/408/OS-B01_WaitBlockWakeup_桥梁手册.pdf)

## Review v2
已把 Wait Queue / `TASK_*` 从跨系统定义降为实现实例；稳定不变量改为“等待登记与失去运行资格之间不能留下 lost-wakeup 窗口”。`while` 重检只绑定谓词式/条件变量等待，不机械推广到所有等待原语。下一轮用同步、I/O、条件变量三类陌生题验证。
