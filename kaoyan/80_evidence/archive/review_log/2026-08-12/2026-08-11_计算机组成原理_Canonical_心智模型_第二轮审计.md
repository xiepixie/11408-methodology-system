# 计算机组成原理 Canonical 心智模型第二轮审计

日期：2026-08-11

结论类型：**Canonical Update**（物理正文与 Owner 完成）；认知状态仍为**待人工确认**，Rules 仍为**待验证**。

## 1. Context Used

- Canonical Subject Atlas：`30_408/20_计算机组成原理/README.md`；
- 第一轮 Source Routing：`2026-08-11_计算机组成原理_个人笔记_Source_Migration_第一轮审计.md`；
- Handbook / Rule / Ownership / Evidence / Integrity contracts；
- 29 张 `CO-*` 卡片与归档 23 文件的既有逐项路由结论。

本轮不重新扫描个人笔记源，也不建立第二份 Source 路由表；第一轮审计是来源去向证据，本日志只记录 Canonical 迁移、跨册接口与发布结果。

## 2. Canonical Assets

| ID | 类型 | 唯一生成模型 / 接口 | Canonical 资产 | 发布页数 |
|---|---|---|---|---:|
| CO-01 | Topic | `Bit Pattern -> Interpretation -> Exact Value -> Operation -> Finite-width Result -> Lost Information/Flags` | `10_数据表示与运算/CO-01_数据表示与运算_方法论手册.tex` | 6 |
| CO-02 | Topic | `Program Intent -> Architectural State -> Encoding/Address Semantics -> Next Architectural State` | `20_ISA与机器级程序/CO-02_ISA与机器级程序_方法论手册.tex` | 9 |
| CO-03 | Topic | `State Delta -> Values -> Dependency Graph -> Datapath -> Schedule -> Control -> Commit` | `30_CPU数据通路与控制/CO-03_CPU数据通路与控制_方法论手册.tex` | 13 |
| CO-04 | Topic | `Dependency -> Need/Ready -> Legal Overlap -> Forward/Stall/Flush -> Precise Commit` | `40_流水线与指令级并行/CO-04_流水线与指令级并行_方法论手册.tex` | 8 |
| CO-05 | Topic | `Address/Granularity -> Chip/Bank/Row/Column -> Transfer -> Latency/Bandwidth` | `50_主存与存储硬件/CO-05_主存与存储硬件_方法论手册.tex` | 6 |
| CO-06 | Topic | `Locality -> Block -> Placement -> Tag/Valid -> Replacement/Write -> AMAT` | `60_Cache与存储层次/CO-06_Cache与存储层次_方法论手册.tex` | 6 |
| CO-07 | Topic | `VA -> VPN/Offset -> TLB/Page Walk -> Permission -> PA -> Cache/Memory` | `70_地址翻译与虚拟存储硬件/CO-07_地址翻译与虚拟存储硬件_方法论手册.tex` | 4 |
| CO-08 | Topic | `Request -> Interface State -> Arbitration -> Transaction -> Transfer -> Completion Signal` | `80_总线与IO硬件/CO-08_总线与IO硬件_方法论手册.tex` | 6 |
| CO-B01 | Bridge | `Instruction Semantic -> Architectural Delta Packet -> Value Dependency Contract -> Datapath Input` | `85_科内桥梁/CO-B01_ISA语义与数据通路/CO-B01_ISA语义与数据通路_桥梁手册.tex` | 4 |
| CO-B02 | Bridge | `VA Access Request -> Translation Result Packet -> Cache Address/Attribute Packet -> Hit/Miss Path` | `85_科内桥梁/CO-B02_地址翻译与Cache访问/CO-B02_地址翻译与Cache访问_桥梁手册.tex` | 4 |
| CO-I01 | Integration | `ISA Semantic -> Fetch/Decode -> Datapath/Pipeline -> EA -> Translation/Cache/Memory -> Result -> Precise Commit` | `86_综合专题/CO-I01_一条指令的一生/CO-I01_一条指令的一生_综合手册.tex` | 7 |

全部 PDF 已由 `python3 00_system/cognitive_system.py publish <target.tex>` 生成到 `90_publish/`；Topic/Bridge/Integration 源目录没有保留同名 PDF 或 LaTeX 辅助文件。

## 3. Owner Diff

### Topic Owner

八册 Topic 分别拥有局部机制：有限格式、ISA 契约、单指令通路、多指令时序、主存硬件、Cache 副本、地址翻译、总线/I/O。README 只保留 Hook、Scope、Stop Boundary 和阅读链接，深层定义全部进入同目录 `.tex`。

### Bridge Validity

- CO-B01：CO-02 输出架构状态差，CO-03 输入值依赖/通路需求；Bridge 只拥有六字段语义包与翻译顺序。
- CO-B02：CO-07 输出 PA/permission/attributes/status，CO-06 输入物理身份、地址字段与访问属性；Bridge 只拥有位来源、串并行条件和 miss/fault 路由。

两册 Bridge 均存在明确上下游、稳定接口和跨题型复用；未把 Topic 内部机制复制进 Bridge。

### Integration Validity

CO-I01 在 CO01–08 与 CO-B01/B02 都有 Owner 后建立，以 LOAD 组合 instruction fetch、decode、EA、translation、Cache/memory、ready/forward/commit。它只拥有跨 Owner 顺序、fast/slow path 与停止条件；ADD/STORE/BRANCH 是删改母轨迹的验证变体，不建立新 Topic。

## 4. Facts vs Hypotheses

### 已由当前工作树证明的事实

- 八个 Topic、两个 Bridge、一个 Integration 均有 Canonical `.tex`、Landing README 和发布 PDF；
- Atlas、Rules、Ownership Matrix 与 `CURRENT.md` 已指向上述资产；
- 公共模型保持 `ISA Semantic -> Data Movement -> Hardware Path -> Timing -> Architectural State Commit`；
- TLB miss、Page Fault、Cache miss，以及 DREQ、bus grant、IRQ 已保持不同状态机；
- OS 的 page repair、block/wakeup、DMA mapping/completion 没有写成计组硬件动作。

### 尚待证据确认的假设

- 各册压缩信号在真实 408 题上是否能减少首步选择错误；
- CO-B01 六字段包和 CO-B02 Translation Result Packet 是否覆盖所有常见综合题；
- CO-I01 的 LOAD 母轨迹是否能以最小改动迁移到 STORE、BRANCH 与 MMIO；
- Candidate Rules 的措辞是否需要按题型继续参数化。

因此本轮不把 Topic/Bridge/Integration 从“待人工确认”升级为“已采用”，也不把 Rules 从“待验证”升级为“已采用”。

## 5. Rejected Stable Claims

沿用并显式保留以下拒绝：固定 Booth/除法位序口诀、同位宽整数除法永不溢出、除零必然产生同一种硬件中断、RISC/CISC 与控制器实现一一绑定、经典五级固定停顿数、流水线越深必然越快、TLB miss 等于 Page Fault、Cache hit 等于访问有权限、DMA 对任意传输恒为 $O(1)$ CPU 开销、DREQ 等于 CPU IRQ。

这些说法只可在题设明确具体 ISA/微架构/算法版本时作为局部条件，不能进入全局 Canonical 不变量。

## 6. 下一验证步

1. 用真题分别攻击 CO01/02 的解释与 ISA 边界、CO03/04 的 ready/need/commit、CO06/07/B02 的三类 miss/fault；
2. 用 LOAD/STORE/BRANCH/MMIO 综合题攻击 CO-I01 的删改轨迹；
3. 用 interrupt/DMA 与 OS I/O 题检查 CO08 到 X-B03 的 handoff；
4. 只有独立题目反复支持后，才把对应 Candidate Rule 升级为已采用。

## 7. v3 统一总图对照增补

随后对 `30_408/00_统一总图/408统一总图_心智模型手册_v3.tex` 做了 Model Diff。该文件作为 Atlas Deep Map / Source 使用，不复制为第二个 Owner，也不沿用其中与当前目录冲突的旧 CO 编号。

本轮将 v3 中计组章节的覆盖契约落回当前 Owner：Subject Atlas 增加六格坐标、四条学习轴、`LOAD rd, disp(rs)` 六格贯穿母例、六组核心边界与六步做题入口；八个 Topic 正文各增加 Map Coordinate 与上下游 handoff；计组 Rules 增加 Cost 坐标、CPI/总时间、throughput/latency 与带宽瓶颈规则。八册 Topic 已重新发布，CO-06 因增补后为 6 页。
