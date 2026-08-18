# 2026-08-15 计组 CodeBrick 全量 Source Diff（v1）

## 目的与边界

本记录把外部 `../../../../sources/codebrick_408/03_计算机组成原理_CO/` 的 65 个原子 Markdown 笔记映射到当前计组 Canonical Owner。它是导入证据与覆盖台账，不是第二份计组知识 Owner；稳定机制最终只进入对应 `CO-01`--`CO-08`、CO-B01/CO-B02 或 CO-I01。

当前计组骨架保持：

```text
ISA State -> Data Location -> Datapath / Control -> Timing -> Commit -> Cost
```

外部笔记中的定义、算法、公式、例题、真题入口和模拟器说明均按“原子细节”吸收；不因条目数量直接新增 Topic，也不把题型技巧写进机制正文。

## 来源规模核对

- 外部 CO 导航声称：65 篇 CO 笔记。
- 当前文件系统实际扫描：66 个 Markdown 文件，其中 1 个为 CO 导航页，故原子笔记为 65 个。
- 当前本项目：CO-01 至 CO-08 八册 Canonical `.tex`，CO-B01/CO-B02 两座科内 Bridge，CO-I01 一册 Integration。
- 结论：数量差异可由导航页解释，不是来源丢失；仍需在逐条 Diff 时保留原始路径。

## 总体归属矩阵

| CodeBrick 分组 | 文件数 | Canonical Owner | 吸收策略 |
|---|---:|---|---|
| `overview/` | 2 | CO-02 / CO-03 / CO-04 | 系统层次与 ISA 边界进 CO-02；关键路径与 $IC\times CPI\times T_{clk}$ 进 CO-03/CO-04；吞吐/响应、Amdahl、MIPS/FLOPS 作为 Cost 坐标，不新增第九 Topic |
| `data-repr/` | 15 | CO-01 | 补齐表示、定点运算、ALU、乘除、浮点、校验、对齐与类型转换；保留“位串解释—目标位宽—信息损失”主线 |
| `instruction/` | 7 | CO-02 | 补齐指令格式、扩展操作码、寻址、有效地址、机器级表示、CISC/RISC、汇编表示 |
| `cpu/` | 15 | CO-03 / CO-04 | 单周期、多周期、单总线、指令周期、硬布线/微程序进 CO-03；流水、hazard、多发射、多处理器进 CO-04；模拟器说明转为验证入口 |
| `storage/` | 14 | CO-05 / CO-06 / CO-07 | SRAM/DRAM/扩展/交叉编址/外存进 CO-05；Cache 全部副本机制进 CO-06；虚拟存储硬件与 TLB 组合路径进 CO-07 |
| `bus/` | 5 | CO-08 | 总线分类、事务、定时、仲裁、标准与带宽口径进 CO-08 |
| `io/` | 7 | CO-08；跨 OS 接口进 X-B03 | I/O 接口、查询/中断/DMA/通道进 CO-08；请求完成、阻塞/唤醒只在 Bridge/Integration 调用 |

## 逐组覆盖判定

### CO-01：数据表示与运算

`alu.md`、`booth-multiply.md`、`c-type-conversion.md`、`complement-add.md`、`data-alignment.md`、`error-detection.md`、`float-arithmetic.md`、`float-repr.md`、`hamming-detail.md`、`non-restoring-division.md`、`number-encoding.md`、`number-system.md`、`restoring-division.md`、`shift-operations.md`、`true-value-machine.md`。

状态：**Partial -> 增量扩充**。现有 CO-01 已有有限位宽、补码、移位、Booth、除法、浮点和舍入主干；本轮补回进制转换、机器数四种编码、C 类型转换、对齐/大小端、ALU 进位链、校验码/海明码、恢复/不恢复除法的逐拍不变量与边界。

### CO-02：ISA 与机器级程序

`addressing-calculation.md`、`addressing-modes.md`、`assembly-basics.md`、`cisc-vs-risc.md`、`instruction-design.md`、`instruction-overview.md`、`machine-level-repr.md`。

状态：**Canonical Update**。在保留原有 ISA State 主线的基础上，已补入指令字段与扩展操作码、寻址模式/有效地址与访存次数、数组和 PC-relative、机器级控制流与 ABI、编译—汇编—链接—装载链、伪指令及 CISC/RISC 权衡。

### CO-03：CPU 数据通路与控制

`cpu-overview.md`、`hardwired-control.md`、`instruction-cycle.md`、`microprogrammed.md`、`multi-cycle.md`、`single-bus-datapath.md`、`single-cycle.md`。

状态：**Canonical Update**。已补入寄存器角色与四子周期、单总线单驱动约束和 Y/Z 中间寄存器、单/多周期成本分解、硬布线控制输入—输出状态机、微程序控制存储器/下一地址/编码取舍、异常精确边界与模拟器验证入口。

### CO-04：流水线与指令级并行

`data-hazard-simulator.md`、`exception-interrupt.md`、`instruction-lifecycle-simulator.md`、`multiprocessor.md`、`pipeline-basic.md`、`pipeline-compare-simulator.md`、`pipeline-hazard.md`、`pipeline-performance.md`、`single-cycle.md` 的性能比较部分。

状态：**Canonical Update**。已补入流水级假设与延迟/吞吐、结构冲突、Produced/Ready/Need 时序检查、forward/stall/flush 分支、两位预测器与 flush 范围、填充排空性能、超标量/动态调度/乱序、SIMD/硬件多线程/多核区分、精确提交与模拟器验证。

### CO-05：主存与存储硬件

`external-storage.md`、`memory-expansion.md`、`memory-hierarchy.md`、`memory-interleave.md`、`memory-overview.md`、`sram-dram.md`。

状态：**Canonical Update**。已补入存储分类轴、随机存取边界、SRAM/DRAM 存储元、三种刷新分布与行缓冲、Flash/SSD 页—块与写放大、ROM 家族、芯片位宽/深度扩展公式、低位/高位交叉编址的流水时间/带宽口径、磁盘访问时间以及 Access/Cycle/Bandwidth/Burst/Bank conflict 的区分。

### CO-06：Cache 与存储层次

`cache-comprehensive.md`、`cache-concept.md`、`cache-mapping.md`、`cache-performance.md`、`cache-replace.md`、`cache-write-policy.md`、`memory-hierarchy-simulator.md`。

状态：**Canonical Update**。已补入速度/容量/成本三重矛盾、局部性与两组缓存关系、寄存器不属于 hit/miss 层、地址位预算、直接/全相联/组相联、FIFO/LRU/Random/Belady/working set、写回/直达 × 写分配/不写分配、完整 miss 生命周期、3C 反事实基线、AMAT 串联/重叠口径、块/页/相联度权衡、PIPT/VIPT/VIVT 与页内偏移约束、Cache 状态表和陌生题重建协议。

### CO-07：地址翻译与虚拟存储硬件

`virtual-memory-hw.md`。

状态：**Canonical Update**。已补入虚存—Cache 同构但由不同 Owner 处理的边界、PTE valid/PFN/dirty/accessed/permission/cache 属性及三种驻留状态、MMU 责任、TLB 全相联/组相联与字段位宽、TLB/页表/Cache 不可能组合、段/段页式精确地址合成与无 TLB 访存次数。

### CO-08：总线与 I/O 硬件

`bus-arbitration-simulator.md`、`bus-arbitration.md`、`bus-overview.md`、`bus-standard.md`、`bus-timing.md`、`channel.md`、`dma.md`、`io-compare.md`、`io-interface.md`、`io-methods-compare-simulator.md`、`io-overview.md`、`programmed-interrupt.md`。

状态：**Canonical Update**。已补入事务四阶段与突发/非突发、数据/地址/控制信号判据、基础时钟与有效传输频率、总线分层与桥接、同步/半同步/异步三互锁/分离事务、集中与分布式仲裁线数—延迟—公平性、I/O 端口状态机与特权边界、中断三条件/隐含入口/向量/屏蔽/嵌套/EOI、DMA 寄存器与停止/周期挪用/交替访存、通道层级与三类通道、总线标准四类特性及并行→串行/共享→点对点演进。

## 不迁入 CO Topic 的内容

- 外部笔记的 Obsidian 导航、链接、模拟器操作界面：作为 Source/验证入口，不成为知识 Owner。
- 具体历年题链接：进入题目/证据层，不复制进机制正文。
- 多核 Cache 一致性、具体 x86/ARM/MIPS 工具链细节：只有在当前 408 范围能形成稳定接口时，才作为 Extension 或最小例子保留。
- OS 的页框分配、置换策略、文件系统策略：CO-07/CO-08 只拥有硬件边界，软件策略交给 OS 或 X-B03。

## 本轮决策

- **Canonical Update**：CO-01 至 CO-08 八册均完成增量扩充，原文全部保留；新增内容分别回接 ISA State、Data Location、Datapath/Control、Timing、Commit、Cost 坐标。
- **Source-only**：CodeBrick 导航、链接、模拟器 UI 与历年题链接继续作为来源/验证入口，不制造第二知识 Owner。
- **No Update**：不新增 CO-09，不改变现有 Atlas、Bridge、Integration Owner。

## 模型验证状态

八册已逐册通过 `cognitive_system.py publish`。随后在
`2026-08-15_CO_Mental_Model_Adversarial_Validation_v1.md` 中用五类陌生组合题验证：

1. 定点位宽/溢出与 ALU 状态提交；
2. 陌生 ISA 在单总线上的微操作排程；
3. TLB/页表/Cache 的反事实组合与 fault 重试；
4. 流水线 load-use、forward/stall/flush 与精确提交；
5. DMA 请求、总线仲裁、IRQ 与有效带宽。

六类题均能从“状态/位置 → 硬件动作 → 时序证据 → 提交/成本”独立重建，且能在 ISA/平台条件缺失时明确停止强推。下一轮若真实历年题或学生错题暴露重复缺口，再进入 Candidate 记录，而不是直接增加 Topic。
