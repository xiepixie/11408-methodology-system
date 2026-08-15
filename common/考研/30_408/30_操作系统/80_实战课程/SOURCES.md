# MIT 6.1810 / xv6 Source Manifest（2026-08-15 快照）

> 用途：给 `html/` 教学页提供可追溯 Source。此文件只登记来源、版本边界和 408 路由，不成为知识 Owner。

## 1. 当前课程版本边界

MIT 6.1810 Fall 2026 官方 schedule 已公开，课程主线和实验安排包括：Unix utilities、system calls、page tables、traps、copy-on-write fork、network driver、parallelism/locking、file system、mmap。

但 2026 schedule 顶部明确说明：**未来日期的 notes / videos 等链接暂时复制自 2024 版本，课程进行中会继续更新。** 因此本项目采取：

1. **课程结构**：以 2026 schedule 为准；
2. **实验规格**：优先使用 `/2026/labs/...` 当前页面快照；
3. **xv6 机制**：以官方 `mit-pdos/xv6-riscv` 与 `xv6-riscv-book` 为稳定 Source；
4. **实验代码仓库**：2026 `util` 页面当前仍指向 `xv6-labs-2025`，在官方页面变更前不擅自假定存在 `xv6-labs-2026`；
5. HTML 页必须在 Source 区标注使用的是“2026 schedule / 2026 lab snapshot / current xv6 book / current source”的哪一种。

## 2. 一级官方来源

| Source | 作用 | 地址 |
|---|---|---|
| MIT 6.1810 Fall 2026 Schedule | 课程顺序、lecture/lab 路由、版本警告 | https://pdos.csail.mit.edu/6.S081/2026/schedule.html |
| MIT 6.1810 General Information | 课程定位、lab 占比、教材 | https://pdos.csail.mit.edu/6.S081/2026/general.html |
| xv6 Book（HTML） | 机制解释与源码交叉链接 | https://mit-pdos.github.io/xv6-riscv-book/ |
| xv6 RISC-V Source | 稳定源码基线 | https://github.com/mit-pdos/xv6-riscv |
| xv6 RISC-V Book Source | 书稿源码、图与章节结构 | https://github.com/mit-pdos/xv6-riscv-book |
| 6.1810 Tools（当前可用安装基线） | QEMU / RISC-V GCC / GDB 环境 | https://pdos.csail.mit.edu/6.S081/2025/tools.html |

## 3. xv6 Book 章节地图

当前官方 xv6 RISC-V Book 目录：

| Chapter | 主题 | 408 对应 |
|---:|---|---|
| 1 | Operating system interfaces | OS 基础、进程、文件接口 |
| 2 | Operating system organization | user/kernel、内核组织、隔离 |
| 3 | Page tables | 地址空间、页表、VM |
| 4 | Traps and system calls | 系统调用、中断/异常、控制权切换 |
| 5 | Page faults | 缺页、lazy allocation、COW 基础 |
| 6 | Interrupts and device drivers | I/O、中断、设备驱动 |
| 7 | Locking | 并发、锁、互斥 |
| 8 | Scheduling | 调度、context switch |
| 9 | Sleep and Wakeup | 阻塞、唤醒、条件同步 |
| 10 | File system | inode、目录、block、buffer cache |
| 11 | Logging | 崩溃一致性、日志 |
| 12 | Concurrency revisited | 多核并发综合 |
| 13 | Summary | 总结 |

## 4. Fall 2026 实验地图

| MIT Lab | 官方页面 | 408 价值 | 我们的处理 |
|---|---|---|---|
| Unix utilities | `/2026/labs/util.html` | 熟悉 fork/exec/wait、fd、目录、用户/内核边界 | **精选**：只做能建立接口模型的任务，不为刷 C 题耗时 |
| System calls | `/2026/labs/syscall.html` | 系统调用分派、进程状态、保护边界 | **核心** |
| Page tables | `/2026/labs/pgtbl.html` | VA→PTE→PA、权限、页表树、TLB 直觉 | **核心** |
| Traps | `/2026/labs/traps.html` | trapframe、trampoline、user↔kernel | **核心** |
| Copy-on-write fork | `/2026/labs/cow.html` | page fault、PTE 权限、引用计数、延迟复制 | **核心** |
| Network driver | `/2026/labs/net.html` | interrupt/device driver、descriptor ring | **选做**：OS I/O 视角；网络协议主体留给 CS144 |
| Parallelism/locking | `/2026/labs/lock.html` | race、spinlock、lock contention、多核 | **核心** |
| File system | `/2026/labs/fs.html` | inode、直接/间接索引、pathname、symbolic link | **核心** |
| mmap | `/2026/labs/mmap.html` | VM × File、page fault、lazy mapping | **核心扩展** |

完整 URL 前缀：`https://pdos.csail.mit.edu/6.S081/2026/labs/`

## 5. 408 定制实验：MIT 没有按考研题型直接覆盖的部分

这些不强行套 MIT lab，而是自己做短实验：

| 408 实验 | 目的 | 输出 |
|---|---|---|
| Scheduler Simulator | FCFS/SJF/SRTF/RR/Priority 状态推进 | Gantt + turnaround/wait/response |
| Semaphore / Monitor Trace | 把 PV、condition variable 变成共享谓词与队列状态 | step-by-step state trace |
| Banker / Deadlock Detector | 区分 deadlock detection 与 safe-state avoidance | Need + safe sequence / unsafe witness |
| Page Replacement Simulator | FIFO/LRU/CLOCK 与 frame allocation 分轴 | fault trace + victim reason |
| I/O Timeline Simulator | CPU / task / device / DMA / interrupt 三线并行 | data/control/task timeline |

## 6. 408 HTML 路线与 Source 绑定

| HTML 单元 | MIT/xv6 Source | 408 Canonical Anchor | 优先级 |
|---|---|---|---:|
| 01 操作系统接口：从用户程序到内核 | Book Ch.1 + util | OS-00 / OS-01 | P0 |
| 02 System Call：受控控制权转移 | Book Ch.2,4 + syscall | OS-00 / X-B01 | P0 |
| 03 Trap：异常、中断、系统调用的共同框架 | Book Ch.4 + traps | OS-00 / OS-05 / X-B01 | P0 |
| 04 Page Table：地址空间是怎样被制造出来的 | Book Ch.3 + pgtbl | OS-04 / X-B02 | P0 |
| 05 Page Fault → COW | Book Ch.5 + cow | OS-04 / OS-I02 | P0 |
| 06 Process / Scheduler / Context Switch | Book Ch.8 + xv6 proc.c + 自建 Scheduler | OS-01/02 | P0 |
| 07 Locking：共享状态与不变量 | Book Ch.7 + lock | OS-03 | P0 |
| 08 Sleep / Wakeup / Coordination | Book Ch.9 + proc.c/pipe.c | OS-B01 | P0 |
| 09 Deadlock / Banker | 408 自建实验 | OS-03 | P0 |
| 10 Interrupt / Driver / DMA / I/O | Book Ch.6 + net（选） | OS-05 / X-B03 | P1 |
| 11 File System：pathname→inode→block | Book Ch.10 + fs | OS-06/07 | P0 |
| 12 Logging / Crash Recovery | Book Ch.11 + log.c + 2026 LEC18 | OS-06/07 | P1 |
| 13 mmap：VM × File | mmap | OS-B04 | P1 |
| 14 Integration：Blocking read | 多章源码追踪 | OS-I01 / X-I02 | P0 |
| 15 Integration：fork + COW + fd 引用 | cow + proc/file 源码 | OS-I02 | P0 |

## 7. 源码阅读白名单（按 408 收益优先）

优先让 HTML 引导读这些文件，而不是要求一开始“读完整个 kernel”：

```text
user/user.h
user/usys.pl / generated usys.S
kernel/syscall.c
kernel/syscall.h
kernel/sysproc.c
kernel/proc.h
kernel/proc.c
kernel/trampoline.S
kernel/trap.c
kernel/riscv.h
kernel/memlayout.h
kernel/vm.c
kernel/kalloc.c
kernel/spinlock.h
kernel/spinlock.c
kernel/sleeplock.c
kernel/pipe.c
kernel/uart.c
kernel/console.c
kernel/file.c
kernel/fs.c
kernel/bio.c
kernel/log.c
```

原则：每页只开放本页主路径需要的 3–6 个文件，避免“源码浏览 = 学会 OS”的错觉。

## 8. 内容复用与版权边界

- 不把 MIT lab / xv6 book 整页复制进本地 HTML；
- 可引用极短源码符号、函数名、结构体名与必要的小片段用于讲解；
- 大段源码通过官方 GitHub 链接定位；
- HTML 的解释、图、状态机、408 Bridge 和实验提示均重新组织；
- 课程页面发生变化时，先更新本 Manifest，再决定是否影响 HTML。
