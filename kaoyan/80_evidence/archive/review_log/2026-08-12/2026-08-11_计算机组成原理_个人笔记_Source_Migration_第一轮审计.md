# 计算机组成原理个人笔记 Source Migration 第一轮审计

> 日期：2026-08-11
>
> 性质：Evidence 层 Source Diff / Owner Diff 记录，不是知识 Owner。
>
> 来源一：`学习领域/卡片盒笔记主题索引卡/` 中全部 29 个 `CO-*.md`。
>
> 来源二：`学习领域/归档/408/计算机组成原理/` 中全部 23 个 Markdown 文件，共约 5,686 行；其中 7 个为空壳。

## 1. 本轮产品与判断口径

当前八个 Topic 原本都只有 Markdown Source，没有 Canonical `.tex`。本轮先完成全科 Source Routing，并把最能检验母模型的 CO-03 建为第一册 Canonical LaTeX 候选正文。

判断顺序：

1. 先问内容属于 Knowledge 还是 Control；
2. 再找唯一 Topic Owner；
3. 区分可移植机制、教学机假设、ISA/平台特例；
4. 重复内容不扩写，错误绝对化结论明确 Reject；
5. 题面信号、第一动作和验证进入待验证 Rules；
6. 未经用户确认的正文只标“待人工确认”，不标“已采用”。

## 2. 经来源攻击后保留的学科母模型

当前 Atlas 的母问题仍成立：

```text
ISA Semantic
-> Data Movement
-> Hardware Path
-> Timing
-> Architectural State Commit
```

做题 Adapter 继续使用：

```text
State -> Location -> Path -> Resource -> Timing -> Commit
```

本轮没有建立第二套全科模型。来源中“控制权不断下放”的视角只适合解释 CPU/Cache/DMA/中断/仲裁器的局部协作，不能取代 ISA 语义与精确提交这条主线。

八个 Topic 的生成性问题分别是：

| Topic | 生成性模型 |
|---|---|
| CO01 数据表示与运算 | `Bit Pattern -> Interpretation -> Exact Value -> Operation -> Finite-width Result -> Lost Information/Flags` |
| CO02 ISA 与机器级程序 | `Program Intent -> Architectural State -> Encoding/Address Semantics -> Next Architectural State` |
| CO03 CPU 数据通路与控制 | `State Delta -> Values -> Dependency Graph -> Datapath -> Schedule -> Control -> Commit` |
| CO04 流水线与 ILP | `Dependency -> Need/Ready Time -> Legal Overlap -> Forward/Stall/Flush -> Ordered Commit` |
| CO05 主存与存储硬件 | `Address -> Chip/Bank/Row/Column -> Transaction -> Latency/Bandwidth` |
| CO06 Cache | `Address -> Candidate Set -> Tag/Valid -> Hit/Miss -> Replace/Write` |
| CO07 地址翻译硬件 | `VA -> VPN/Offset -> TLB/Page Walk -> PA -> Cache/Memory` |
| CO08 总线与 I/O 硬件 | `Request -> Interface State -> Arbitration -> Transaction -> Transfer -> Completion Signal` |

## 3. 卡片盒 29 张主题卡路由

### 3.1 CO01 数据表示与运算

| Source | 路由 | Diff 结论 |
|---|---|---|
| `CO-数据的表示及运算.md` | CO01；Rules | Source；位权、补码、移位和标志位进入后续正文 Diff，C/C++ 语言未定义行为只作边界 |
| `CO-浮点数与IEEE754.md` | CO01 | Source；保留编码分区、对阶、规格化、舍入和阶码溢出链 |
| `CO-原码一位乘法.md` | CO01 | Source；符号/数值分离与部分积迭代 |
| `CO-序贯移位乘法器.md` | CO01 | Source；时间换空间，具体门数和延迟须服从题设 |
| `CO-并行阵列乘法器.md` | CO01 | Extension；保留空间换时间与关键路径，不把现代优化扩成 408 主干 |
| `CO-Booth乘法推导.md` | CO01 | Source；相邻位重编码与算术移位，具体 Booth 变体必须先声明 |
| `CO-原码乘法与Booth算法对比.md` | CO01 | Source；比较编码、移位和部分积数量，不保留“永远更快”式结论 |
| `CO-定点乘法溢出判断.md` | CO01；Rules | Candidate；目标宽度与符号扩展判据 |
| `CO-原码不恢复余数除法.md` | CO01 | Source；余数符号控制下一次加减 |
| `CO-补码不恢复余数除法.md` | CO01 | Source/Challenge；“末位恒置 1”等必须绑定教材算法版本，不能脱离寄存器布局 |
| `CO-定点除法溢出判断.md` | CO01；Rules | Candidate + Reject mix；保留“商能否装入目标格式”，否定整数除法永不溢出 |
| `CO-除零检测硬件机制.md` | CO01 / CO03 / X-B01 Use | Candidate + Reject mix；零检测电路真实，异常语义依 ISA，不接受“所有硬件必然中断” |

### 3.2 CO02 ISA 与机器级程序

| Source | 路由 | Diff 结论 |
|---|---|---|
| `CO-程序机器级表示与指令系统设计.md` | CO02；CO03 Use；Rules | Source Pack；扩展操作码、EA、C 到机器状态与 ABI 边界；MIPS 固定格式仅作例子 |
| `CO-函数调用栈帧.md` | CO02 | Source；调用约定和栈帧归 ABI，不写成 ISA 自动规则 |
| `CO-寄存器按可访问性分类.md` | CO02 / X-B01 Use | Challenge；保留 ISA 可达性视角，拒绝固定四级清单和“OS 边界等于 ISA 边界” |

### 3.3 CO03 CPU 数据通路与控制

| Source | 路由 | Diff 结论 |
|---|---|---|
| `CO-CPU控制器-解释程序驱动计算.md` | CO03 | Canonical Update；取指/译码/执行被重建为状态差、依赖、调度和提交 |
| `CO-硬布线与微程序对比.md` | CO03 | Canonical Update + Reject；保留控制映射，否定与 RISC/CISC 一一绑定 |
| `CO-控制器-分层协同体系.md` | Atlas Use / CO03/06/08 | Bridge Note；“专用控制器分责”保留，不能成为第二学科母模型 |

### 3.4 CO05–CO08

| Source | 路由 | Diff 结论 |
|---|---|---|
| `CO-RAM-SRAM与DRAM.md` | CO05 | Source Pack；存储单元、二维阵列、刷新、时序；具体 DDR 参数只作 Extension |
| `CO-统一内存访问UMA.md` | CO05 Extension | Source；UMA/NUMA 为多处理器扩展，不进入当前 408 主干 |
| `CO-Cache控制器-硬件透明加速.md` | CO06 | Source；地址查找、hit/miss、替换和写策略 |
| `CO-IO接口-CPU与外设桥梁.md` | CO08 | Source；接口寄存器和协议适配 |
| `CO-IO控制方式演进.md` | CO08 / X-B03 Use | Source；按“谁等待、谁搬运、谁通知”重建 |
| `CO-中断控制器-变轮询为事件驱动.md` | CO08 / X-B01/X-B03 Use | Source；只 Own 硬件请求、判优、向量和入口交接 |
| `CO-DMA控制器-自动化数据搬运.md` | CO08 | Duplicate Source；进入 DMA Source Pack |
| `CO-DMA控制器-硬件接管数据传输.md` | CO08 / X-B03 Use；Rules | Source；预处理、传输、完成和总线争用 |
| `CO-DMA控制器-硬件自治.md` | CO08 / X-B03 Use；Rules | Source + Reject mix；保留 scatter-gather 和阈值权衡，拒绝通用 O(1) CPU 开销 |
| `CO-总线仲裁器.md` | CO08 | Source；仲裁只决定共享事务发起权，不拥有 OS 设备分配 |

## 4. 归档目录 23 个文件路由

| Source | Owner | Diff 结论 |
|---|---|---|
| `计组发展与概念.md` | Atlas Foundation / Rules | Duplicate；CPU time、上下文解释和体系参数已有稳定位置 |
| `定点小数.md`、`IEEE.md`、`浮点数.md` | CO01 | Source Pack；内容高度重叠，后续只维护一个表示/运算 Owner |
| `指令格式,寻址方式,指令类型.md` | CO02；X-B01/OS Use | Source Pack；指令格式和 EA 留在 CO02，上下文切换与 blocking read 不进入 CO02 |
| `CPU与数据通路.md` | CO03 / CO04 Extension | Canonical Update；单/多周期进入 CO03，多核/Flynn 留作 Extension |
| `总线结构.md` | CO08；CO03 Use | Source Pack；外部总线事务归 CO08，内部单总线教学机供 CO03 母例 |
| `指令流水线.md` | CO04 | Source Pack；固定停顿数改写为 need/ready/forwarding 条件 |
| `主存储器.md`、`存储器层次.md` | CO05；CO06 Use | Source Pack；介质/芯片/刷新归 CO05，副本机制归 CO06 |
| `Cache.md` | CO06 | Source Pack；映射、状态机、写策略、3C 和容量题 |
| `虚拟存储.md` | CO07 / OS-04 / CO-B02 | Split Source；TLB/Page Walk/PIPT/VIPT 归 CO07/Bridge，页框/置换/工作集归 OS，不复制 |
| `DMA.md` | CO08 / X-B03 | Source Pack；硬件事务归 CO08，OS mapping/completion 归 X-B03/OS |
| `IO控制方式.md` | CO08 / OS-05 | Split Source；接口、PIO/中断/DMA 硬件半程归 CO08，缓冲/SPOOLing/设备分配归 OS |
| `中断处理.md` | CO08 / CO04 / X-B01/X-B03 / OS | Split Source；硬件入口、精确提交和 OS handler 分责，不建立平行“全生命周期” Owner |
| `磁盘.md` | CO05 / CO08；OS-05/06 Use | Split Source；介质和传输硬件归计组，调度/文件映射归 OS；LBA 不推出真实物理连续 |
| `CISC与RISC.md`、`IO接口.md`、`总线计算.md`、`指令周期与时序.md`、`指令执行过程.md`、`运算电路.md`、`页面置换.md` | 对应 CO01–08 | Empty Source；7 个文件均为 0 行，不产生知识更新 |

## 5. 已明确拒绝进入稳定知识的说法

1. 同位宽整数除法永不溢出；反例是补码最小负数除以 $-1$。
2. 所有 ISA 的整数除零都触发同一种硬件中断或 OS 行为。
3. RISC 必然硬布线、CISC 必然微程序，或定长/变长、寄存器数量存在普适二分。
4. 单周期处理器必然采用哈佛结构、LOAD 必然是最长路径、寄存器堆读口永远无使能。
5. PC、PSW、Cache、MMU 对所有软件层都完全不可见，或 OS 管理边界等同 ISA 边界。
6. DMA 让 CPU 对任意传输的总开销恒为 $O(1)$，或 DMAC 永远只接受裸物理地址。
7. 仅凭阶码差达到有效位数就断言小数操作数对舍入完全无影响；guard/round/sticky 与舍入模式仍可能重要。
8. 把固定九节拍、固定 PC 步长、某套 MIPS ABI 或某个 Booth/除法变体当作所有机器的通用规律。
9. 工作集总和超过内存当且仅当系统已经颠簸；该 OS 来源不进入 CO07。

## 6. 本轮 Canonical Update

- 新建 CO-03 Canonical LaTeX 候选正文。
- 把“取指/译码/执行”升级为“State Delta -> Values -> Dependency Graph -> Datapath -> Schedule -> Control -> Commit”。
- 明确 architecture vs microarchitecture、produced vs available vs committed、datapath vs control 等边界。
- 将固定九拍 LOAD 降为带假设的贯穿母例。
- 将 Topic README 收缩为 Landing Page，并发布 13 页阅读视图。
- 新增计组待验证 Rules 与六条已否定绝对化规则。

## 7. 人工决定与下一步

本轮结果是 **Canonical Candidate + Candidate Rules + Explicit Rejects**，不是“已采用”。

下一步最小动作：

1. 人工审阅 CO-03 的 Mother Model、Owner 边界和 LOAD 母例；
2. 迁移 CO-02，把指令编码、EA、机器级程序与 ABI 分层写入唯一 `.tex`；
3. CO-02/03 都稳定后建立 CO-B01；
4. 用真实数据通路、微操作和性能题攻击新增 Rules；
5. CO-I01 必须等待 CO04、CO06/07 的相关 Owner 成熟，不提前用综合册替代缺失 Topic。

