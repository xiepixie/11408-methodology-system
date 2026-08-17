# OS HTML · 408 高频定量 Overlay QA（2026-08-15）

## 1. 目标

在保持 MIT 6.1810 / xv6 真实机制主线的前提下，补齐 xv6 教学实现天然缺失、但 408 高频真题稳定要求的计算模型与经典同步题型。HTML 仍为 Derived Learning View；稳定定义由现有 Canonical Owner 持有。

## 2. 本轮补强

| Lesson | 新增内容 | Owner / 边界 |
|---|---|---|
| 05 Page Fault → COW | xv6 resident-only vs Swap/request paging；OPT/FIFO/LRU/CLOCK 交互置换；CLOCK/NRU/Enhanced CLOCK 区分；Belady/stack-property；Working Set/PFF/Thrashing | OS-04；current xv6 main 无完整 swap/replacement |
| 06 Process / Scheduler | HRRN；Weighted Turnaround；MLFQ/MFQ 参数模型；timer/wakeup 产生 preemption decision opportunity 的真实位置 | OS-01/02；xv6 只作为 switch mechanism，不伪装成 HRRN/MLFQ scheduler |
| 08 Sleep / Wakeup | `spinlock + sleep/wakeup → counting semaphore`；Producer-Consumer；Readers-Writers 读优先/写优先 | OS-03 + OS-B01；PV permit semantics 由 OS-03 持有 |
| 10 I/O / Driver | HDD track/cylinder/sector；`Tseek + Trotation + Ttransfer`；FCFS/SSTF/SCAN/C-SCAN/LOOK/C-LOOK simulator | OS-05；机械寻道模型不外推到 SSD |
| 11 File System | `K=floor(B/a)`；`d+sK+qK²+tK³`；最大文件大小；LBN 分层定位；direct/single/double/triple 经典 I/O 次数 | OS-06/07；xv6 11+single+double 只是 lab 特例 |

## 3. 关键事实校准

### 3.1 CLOCK / NRU

- Basic CLOCK / Second Chance：reference/access bit + circular hand；
- NRU：通常以 `(A/R,D/M)` 分类，并周期性重置访问位；
- Enhanced/Improved CLOCK：把访问位、脏位与环形扫描组合；具体扫描轮次按教材/题设；
- A/R 估计近期使用，D/M 估计 eviction write-back cost；两者职责不同。

Canonical OS-04 已同步补充该边界，并把“CLOCK 只牺牲极微小准确度”的过强表述改为“牺牲精确 LRU 次序”。

### 3.2 Page Replacement

- `Page Fault ≠ Page Replacement`；只有合法页需要驻留且没有空闲 frame 才进入 victim policy；
- OPT 作为知道未来的离线理论下界，不作为在线 OS 实现；
- FIFO 可能出现 Belady anomaly；理想 LRU/OPT 的 stack property 不允许 frame 增加导致 fault 增加；该性质不能无条件搬给 CLOCK。

### 3.3 Scheduling

- HRRN `R=(W+S)/S` 是调度决策点的动态 ordering key；最终 Weighted Turnaround `T/S` 是完成后的评价指标；
- MLFQ 必须显式给 queue membership / quantum / demotion / boost / preemption rule，否则不存在唯一甘特图；
- timer interrupt、I/O wakeup 等先改变 decision opportunity / candidate set，policy 再决定是否抢占，context switch 是后续 mechanism。

### 3.4 Semaphore Bridge

- xv6 `spinlock + sleep(chan, lock) + wakeup(chan)` 足以展示 counting semaphore 的底层实现责任；
- 真实实现可保持 permit count 非负，等待者由 wait relation 单独表示；不要求采用教材“负值=等待人数”的编码；
- `wakeup` 不等于 permit ownership，多个 waiter 竞争时必须在锁下 `while(value==0)` 重检。

### 3.5 Disk / Mixed Index

- 磁盘模拟器显式声明初始方向、物理端点和静态请求快照约定；真题以题设为准；
- Mixed Index 计算必须先由块大小和地址项大小生成 `K`，再逐层计算容量；“二级间接=3 次 I/O”只在 inode 已驻留且两级索引块/数据块均未缓存的特定口径成立。

## 4. 自动验证

### Static / Syntax

```text
HTML parse: 16/16 OK
Local assets/links: OK
Inline/shared JS syntax: OK
05/06/08/10/11 section numbering: contiguous OK
```

### Chrome Headless DOM smoke

```text
Headless DOM smoke: 16/16 OK
```

默认定量用例输出：

```text
Lesson 05 OPT default: Faults = 7
Lesson 05 Working Set default: |W| = 4
Lesson 06 FCFS default: Avg weighted turnaround = 3.50
Lesson 10 FCFS default: Total head movement = 640 cylinders
Lesson 11 default mixed index: 17,247,250,432 bytes ≈ 16.1 GiB
```

其中磁盘默认队列为 `53 → [98,183,37,122,14,124,65,67]`，FCFS 总移动量人工复核为 640。

## 5. Canonical / Repository

- 修改：`OS-04_虚拟内存与地址翻译_方法论手册.tex`，补 CLOCK/NRU/Enhanced CLOCK 边界；
- Publish：成功，输出 `90_publish/408/OS-04_虚拟内存与地址翻译_方法论手册.pdf`，25 页；
- Repository hard check：`OK: repository hard checks passed.`

## 6. 课程治理更新

`QUALITY.md` 新增 Gate F · 408 Quantitative Coverage：高频计算 Topic 必须同时有模型假设、逐步状态轨迹、由对象生成公式、交互/完整算例、xv6-vs-408 边界以及 tie/convention 声明。

Source Manifest 新增 4.16 高频定量 Overlay，避免未来更新 MIT/xv6 时误把这些 408 桥接实验删除或当成 MIT 官方 lab。
