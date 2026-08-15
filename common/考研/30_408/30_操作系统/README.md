# 操作系统 Subject Atlas

> 类型：Atlas
> 状态：已采用；README 是 Canonical Subject Atlas。OS-00 与五个 Core Topic 的 Source Diff / Owner Diff 已完成，六册 Canonical LaTeX 均已纳管并有发布视图；新增 Rules 仍待真题验证与人工确认。

> 一个程序看起来像在“独占机器”，但真实系统里 CPU、内存、设备和文件都在被多个执行流共享。OS 的核心不是背功能列表，而是追踪：**谁拥有状态、什么事件改变状态、什么坏状态必须被阻止、最小机制怎样恢复 Safety / Liveness。**

## 这门课研究什么

操作系统研究：怎样在并发、资源有限和硬件异步事件存在的条件下，为程序提供受保护、可组合、可管理的执行环境。

统一推演镜头：

```text
State
-> Transition
-> Bad State
-> Safety / Liveness
-> Minimal Mechanism
-> Tradeoff
```

本 README 直接拥有 Subject Atlas 地图。

OS 状态坐标压缩为 `S = (Objects, Relations, Queues)`：先列内核管理的对象、引用/映射关系和等待队列，再用 `Event + Mechanism + Policy` 推演新状态。任何转换都必须说明触发事件，并分别检查 Safety / Liveness、不变量与成本。

OS 的五项上位职责是 Control、Virtualization、Coordination、Protection 与 Persistence。它们只是跨 Topic 的导航坐标：控制权进入进程/调度，协调进入调度/并发/I/O，保护进入权限与 VM，持久化进入文件系统；不据此新增第五册之外的平行机制 Topic。

## Atlas Foundation

[OS-00 操作系统基础与程序运行环境](05_操作系统基础与程序运行环境/README.md) 是 Atlas-owned Foundation Supplement，不与五个机制 Topic 平级。它提供 abstraction、virtualization、protection、user/kernel、程序运行环境等共同入口。

## 五个 Core Topic

1. [进程、线程、调度与控制权](10_进程线程调度与控制权/README.md)
2. [并发、同步与死锁](20_并发同步与死锁/README.md)
3. [虚拟内存与页生命周期](30_虚拟内存与页生命周期/README.md)
4. [I/O 请求、等待与完成](40_IO请求等待与完成/README.md)
5. [文件系统与持久化](50_文件系统/README.md)

## Internal Bridge / Integration

- [OS Internal Bridge Atlas](60_科内桥梁/README.md)
- [OS Integration Layer](70_综合专题/README.md)

优先桥梁：Wait/Block/Wakeup、Process × VM、Process × File Reference、VM × File × I/O。

优先综合过程：Blocking `read()`；`fork()` + COW + Resource Reference。

## 做题入口

[OS 做题规则](90_做题规则/README.md)

做题时先问：当前有哪些 Object / Relation / Queue？发生了什么 Event？如果完全不控制会出现什么 Bad State？要保护的是 Safety 还是 Liveness？最小 Mechanism 是什么？代价是什么？

README 到这里停止。完整机制、边界、反例和 Worked Example 必须进入各册 Canonical `.tex`。
