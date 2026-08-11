# X-B01｜Privilege / Exception / System Call × OS Control

状态：目录已建立，正文未建。

## Owners
CO02/CO03 ISA & CPU ↔ OS01 Process/Control，并使用 OS Atlas Foundation 的 user/kernel 基础语义。

## Mother Interface
`User Execution -> Trap/Exception/System Call -> Save Architectural State -> Privileged Entry -> Kernel Control -> Return/Resume`

## Owns
软件可见执行怎样跨越 privilege boundary；异常/系统调用入口与 OS 控制权取得之间的 handoff。

## Responsibility Split
- 计组：ISA exception semantics、privilege state、硬件入口/返回所需体系结构状态；
- OS：进入内核后怎样解释原因、选择处理机制并改变 task/system state。

## Boundary
调度、同步、VM 修复由 OS Topic Own；中断/DMA 设备完成路径进入 X-B03。
