# 操作系统实战课程 · 质量门禁

> 角色：Course QA / Source Governance。这里只规定 HTML 教学视图怎样保持正确、可追溯、可学习；不拥有 OS 机制本身。

## 1. 每页必须通过的四道 Gate

### Gate A · Source Freshness

每个涉及 MIT/xv6 具体实现的页面必须区分四类来源：

1. **2026 Schedule / Lab**：课程结构、当年实验要求的最高优先级事实；
2. **Current xv6-riscv source**：当前主线实现事实；
3. **Inherited lecture material**：2026 schedule 暂时链接到 2024/2025 讲义时，必须显式标记年份；
4. **Older lab fallback**：只有 2026 页面无法完整抓取时才用于核对细节，并在 Source Manifest 标明“fallback”，不能伪装成 2026 已确认事实。

页面中若出现函数名、字段名、lab task 或 branch-specific 行为，必须能回到 Source Manifest 找到版本边界。

### Gate B · Architecture Boundary

任何“系统调用/异常/页表/中断”叙述必须先分：

```text
架构无关语义
→ RISC-V ISA 语义
→ 当前 xv6 main 实现
→ MIT lab branch 任务
```

严禁把某一层的实现细节提升为跨平台定义。例如：

- trap 不一定由硬件自动切 kernel stack；
- system call 的逻辑恢复点可以是“下一条指令”，但硬件保存的 PC 语义按 ISA 判断；
- Sv39 允许 L2/L1/L0 任一级成为 leaf，而 base xv6 的 `walk()` 只实现了普通 4 KiB leaf 路径；
- `scause=15` 是 RISC-V Store/AMO page fault，不是所有 ISA 的通用编号。

### Gate C · 408 Transfer

每页至少有一个可复原的桥：

```text
真实系统状态
↔ 408 教材抽象
↔ 题面信号 / 第一动作
```

如果某个 MIT task 很有工程价值但很难反哺 408，必须降为“选做/Extension”，不能因为它是官方作业就占据主线。

### Gate D · Retrieval / Adversarial Check

页面结束前至少检查：

- 1 个主链复原；
- 2 个 `A ≠ B` 边界；
- 1 个改变条件后的反例/慢路径；
- 1 个“什么时候停止展开”的 Stop Boundary。

学习目标不是“看完”，而是关闭页面后能在陌生题中重新生成机制。

### Gate E · Readability / Presentation

课程页是长时间学习界面，不以“信息塞得下”为验收标准。所有页面必须共享 `html/course.css` 与 `html/course-ui.js`，并满足：

- **正文行长**：主要解释文字控制在约 `78ch`（中文约 35–42 字/行的量级），表格、流程图、交互区才使用全宽；
- **层级稳定**：Hero → H2 → Panel → Mini/Callout 的视觉层级前后一致；禁止单页自行把普通标题放大成海报级元素；
- **颜色有语义**：Blue=普通机制/桥接，Orange=边界/注意，Red=错误/风险，Green=成功/不变量；颜色不能成为唯一信息载体；
- **长页可导航**：Lesson 自动生成 H2 目录、顶部阅读进度和返回顶部；这些导航由共享脚本生成，不在每页手工维护第二份目录；
- **表格可追行**：桌面有表头/隔行层次，窄屏允许横向滚动；不能为了塞进手机而把列压成不可读碎片；
- **代码优先可读**：正文 inline code 与 block code 有独立字体/底色，代码块允许滚动，不用过小字号换取“一屏装下”；
- **响应式**：`grid2/grid3/grid4/trace/calc/crash` 在窄屏收为单列；前后页导航允许纵向排列；
- **打印退化**：打印时移除进度条、浮动按钮等 UI，转成白底高对比阅读稿；
- **局部 CSS 边界**：共享视觉 Owner 是 `course.css`。快速建设期旧页已经存在的重复 global inline declarations 暂时允许作为 legacy fallback 保留，但不得再分别修改；新增/重构 CSS 只在 inline 中拥有本页专有交互组件。待内容稳定后再统一删除 legacy 重复项。

可读性检查优先问：“连续阅读 20–30 分钟时，眼睛是否能稳定跟踪层级和行宽？”而不是“是否更像炫酷 dashboard”。

### Gate F · 408 Quantitative Coverage

只要该 Topic 在 408 中存在稳定高频计算题，HTML 不能停在“机制讲懂”，至少要提供：

1. **Model Assumptions**：先写清题设模型与简化，例如 frame 数、tie rule、初始方向、cache 是否命中；
2. **State Trace**：每一步展示真正变化的状态，而不是只给最终数字；
3. **Formula from Objects**：公式必须由对象关系生成，例如 `K=B/a → d+sK+qK²+tK³`，不能只放背诵盒子；
4. **Interactive / Worked Check**：至少一个可修改 simulator 或完整算例，用于验证手算轨迹；
5. **Reality Boundary**：明确 xv6 / 真实系统与 408 经典模型哪里不同，禁止“实验没有这个 subsystem ⇒ 考点不重要”；
6. **Tie / Convention Disclosure**：同刻到达、同距离、endpoint、扫描轮次等存在歧义时，页面必须声明本模拟器约定，并提醒真题以题设为准。

当前必须维持的定量覆盖：Scheduler、Page Replacement / Working Set、Banker、Disk Scheduling、inode Mixed Index。

## 2. 每页统一证据标签

页面 header 的 metadata 至少包含：

```text
Source: Book / Lecture / Lab
Implementation: current main or lab branch
408 Anchor: Canonical Topic / Bridge / Integration
Priority: P0 / P1
Estimated Time
```

若 lecture 链接实际标题年份不是 2026，写成例如：

```text
2026 schedule → inherited 2025 Lecture 8
```

而不是只写 “MIT 2026 Lecture”。

## 3. 代码展示原则

- 不复制大段官方源码；
- 页面主要展示 `symbol → responsibility → state change`；
- 需要代码时只截取足以解释一个机制的最小片段；
- 每页源码阅读白名单控制在约 3–6 个核心位置；
- lab 解法不给完整可提交答案，重点给不变量、调试问题与验证顺序。

## 4. 实验取舍模板

每个实验都写清：

| 项 | 必须回答 |
|---|---|
| Why | 它让哪个 408 抽象变成可运行模型？ |
| Minimum | 做到哪一小步已经获得主要认知收益？ |
| Full | 官方完整 lab 还增加什么工程训练？ |
| Stop | 什么情况下可以停，不继续消耗复习时间？ |
| Verify | 用什么 test / trace / retrieval question 验证真的理解？ |

## 5. Page Fault / COW 专项质量规则

后续页面不得出现以下错误压缩：

1. `Page Fault = 页面一定在磁盘`：错误。COW、lazy-zero、permission 都可以 fault；
2. `Page Fault = 一定阻塞并调度`：错误。内存内可修复 fault 可以在当前 task 的 kernel path 内完成后直接 retry；只有需要等待 I/O 等条件时才 block；
3. `PTE_W=0 = COW`：错误。代码/只读数据本来就可能不可写；COW 必须保留“原本可写、现在因共享而临时只读”的软件状态；
4. `fork 后共享 page = shared-memory IPC`：错误。COW 是共享物理实现、维持私有地址空间语义；
5. `refcount = 进程数`：错误。它应表达“当前有多少有效映射/owner 仍要求该 frame 存活”，具体计数口径由实现定义；
6. `copyout` 可以完全依赖 user page fault：错误。xv6 的 kernel helper 会显式 walk 用户页表并通过物理映射复制，COW lab 因而要求 `copyout()` 也处理 COW。

## 6. 回归检查

每新增/修改一页至少执行：

```text
HTML parser
JS syntax check（页面脚本 + `course-ui.js`）
共享资产引用检查（全部 16 个 HTML 必须加载 `course.css` / `course-ui.js`）
Headless browser DOM smoke test（TOC / reading-progress / back-to-top 能正常注入）
上一页/下一页导航检查
Source URL 与年份检查
Canonical Owner diff（若外部 Source 暴露稳定模型问题）
repository check（若修改 Canonical）
```

如果外部课程材料只丰富教学例子而没有改变稳定世界模型，结论应是 `No Update`；只有事实/边界错误或重要机制缺口才回写 Canonical Owner。
