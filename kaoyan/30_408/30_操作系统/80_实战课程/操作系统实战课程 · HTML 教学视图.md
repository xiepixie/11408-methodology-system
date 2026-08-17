# 操作系统实战课程 · HTML 教学视图

> 状态：Prototype / Derived Learning View（非 Canonical Knowledge Owner）
>
> 目标：把 MIT 6.1810 / xv6 的公开课程、实验与源码，重新组织成服务 408 的中文交互式 HTML 教学页。

## 1. 边界

本目录不是第六个 OS Topic，也不替代现有 Handbook。

- **408 稳定知识 Owner**：仍由 `../README.md`、五个 Core Topic 的 Canonical `.tex`、Bridge / Integration 与 `../90_做题规则/README.md` 持有。
- **MIT / xv6**：作为真实系统 Source 与实验载体，用来让抽象机制“跑起来”。
- **HTML**：Derived Learning View。负责教学顺序、动画、源码路径、实验提示、408 Bridge 与 retrieval check；若 HTML 与 Canonical Handbook 冲突，以 Canonical Owner 为准，并回到 Owner 做 Source Diff。
- **不镜像课程网页**：正文重新讲解，只保留必要的来源链接、源码定位和实验任务摘要。

## 2. 文件结构

```text
80_实战课程/
├── 操作系统实战课程 · HTML 教学视图.md
├── QUALITY.md
├── MIT 6.1810  xv6 Source Manifest（2026-08-15 快照）.md
└── html/
    ├── course.css
    ├── course-ui.js
    ├── index.html
    ├── 01-os-interface.html
    ├── 02-system-call.html
    ├── 03-trap.html
    ├── 04-page-table.html
    ├── 05-page-fault-cow.html
    ├── 06-process-scheduler.html
    ├── 07-locking.html
    ├── 08-sleep-wakeup.html
    ├── 09-deadlock-banker.html
    ├── 10-io-driver.html
    ├── 11-file-system.html
    ├── 12-logging.html
    ├── 13-mmap.html
    ├── 14-blocking-read.html
    └── 15-fork-cow-resource.html
```

后续 HTML 一页一个教学单元，保持可直接在浏览器打开，不依赖构建系统。来源版本、架构边界、408 Transfer 与 Retrieval Gate 统一执行 [`QUALITY.md`](QUALITY.md)，避免课程越写越多却把具体实现误当成通用 OS 定义。

## 3. 课程主线

```text
程序看到的 OS 接口
-> user/kernel 与 system call
-> trap / interrupt / exception
-> page table / address space
-> page fault / COW
-> process / scheduling / context switch
-> lock / sleep / wakeup / coordination
-> deadlock（408 定制实验）
-> device / interrupt / DMA / I/O
-> file / inode / block / logging
-> mmap 与 VM × File
-> Blocking read / fork+COW 综合追踪
```

MIT 6.1810 提供真实机制与 xv6 实验；408 缺而 MIT 不以考试形式覆盖的部分（调度算法、Banker、典型页面置换等）由我们补成短实验。

## 4. 页面统一结构

每页尽量固定为：

1. **Mother Question**：这一页真正解决什么问题；
2. **Minimum Model**：最小对象 / 关系 / 队列；
3. **Mechanism Trace**：一次真实事件怎样推进状态；
4. **xv6 Code Path**：代码入口、关键 struct / function；
5. **Interactive Lab**：可观察、可修改、可验证；
6. **408 Bridge**：教材抽象 ↔ xv6 对象 ↔ 考题语言；
7. **Boundary / Anti-Pattern**：最容易混淆的边界；
8. **Retrieval Check**：关闭页面后必须能复原的起手与主链。

### 4.1 视觉与阅读层的唯一 Owner

所有页面统一加载：

```html
<link rel="stylesheet" href="course.css">
<script src="course-ui.js" defer></script>
```

职责固定为：

- `course.css`：全局字体、正文宽度、层级间距、对比度、表格、代码块、Callout、移动端与打印样式；
- `course-ui.js`：长页阅读进度、本页目录锚点、返回顶部；
- 每个 Lesson 的 inline CSS 最终只应拥有该页特有的交互组件（例如 Scheduler Gantt、COW Trace、Crash Slider）；快速建设期遗留的全局重复声明先作为 fallback 保留，但共享层后加载并拥有最终视觉解释权，后续不得再按页分别演化；
- 以后若要调整“全课程阅读体验”，先改共享层，再检查局部组件；避免 15 页分别漂移。

共享层的阅读目标不是“视觉炫”，而是：中文正文单行约 35–42 个汉字、正文与 muted text 对比足够、标题不会占掉整屏、表格能追行、移动端能横向查看宽表、长页能快速定位与回顶。

## 5. 当前进度

- [x] 建立 MIT 6.1810 / xv6 Source Manifest；
- [x] 建立 HTML 课程总览页；
- [x] 第一页：操作系统接口——从用户程序到内核；
- [x] 第二页：System Call——一次受控的控制权转移；
- [x] 第三页：Trap——异常、中断与系统调用为何能共用入口；
- [x] 第四页：Page Table——地址空间怎样被映射与保护；
- [x] 第五页：Page Fault → COW——Fault 分类、lazy repair、COW、refcount 与 copyout 完整性；
- [x] 第六页：Process / Scheduler——xv6 context-switch mechanism × 408 Scheduler Simulator；
- [x] 第七页：Locking——共享不变量、Atomic RMW、memory ordering、spin/block 与 lock granularity；
- [x] 第八页：Sleep / Wakeup——Lost Wakeup、condition lock handoff、pipe/console/wait/kill；
- [x] 第九页：Deadlock / Banker——408 自建 Safety/Request 交互模拟器与题型路由；
- [x] 第十页：Interrupt / Driver / DMA——四轴 I/O 模型、virtio/UART/E1000 与 DMA ownership；
- [x] 第十一页：File System——pathname/fd/inode/block、open-reference 生命周期与二级间接索引；
- [x] 第十二页：Logging——redo log、commit point、recovery 与 crash slider；
- [x] 第十三页：mmap——VMA、lazy file-backed fault、MAP_SHARED/PRIVATE 与 munmap/fork 生命周期；
- [x] 第十四页：Blocking read Integration——cache hit/miss 两条全生命周期与四条并行轨迹；
- [x] 第十五页：fork + COW + Resource Reference——Process/VM/File 关系向量与选择性分化；
- [x] 建立课程质量门禁 `QUALITY.md`，固定 Source Freshness / Architecture Boundary / 408 Transfer / Retrieval Check；
- [x] 操作系统第一版 15 页 P0/P1 HTML 主线全部建立，进入回归、Source Refresh 与逐页教学打磨阶段；
- [x] 建立共享阅读层 `course.css + course-ui.js`，统一 16 个页面的排版、可读宽度、表格/代码块、移动端、打印与长页导航；
- [x] 第二轮 408 高频定量补强：Lesson 05 增加 Swap/OPT-FIFO-LRU-CLOCK/Belady/CLOCK-NRU/Working Set-PFF；Lesson 06 增加 HRRN/带权周转/MLFQ 与抢占点；Lesson 08 增加 counting semaphore→生产者消费者→读者写者；Lesson 10 增加 HDD 几何与六种磁盘调度模拟；Lesson 11 增加 direct/single/double/triple 通用混合索引计算器。
