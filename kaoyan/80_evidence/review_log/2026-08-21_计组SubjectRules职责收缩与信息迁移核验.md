# 计组 Subject Rules 职责收缩与信息迁移核验

日期：2026-08-21  
场景：`adversary / review`  
角色：Adversary + Editor  
状态：完成一轮完整迁移核验。旧版计组 Subject Rules 中 48 条做题控制与 8 条已否定错误命题均找到当前唯一归属；Subject Rules 只保留跨多个训练专题仍需统一维护的控制，局部规则回到 Topic / Bridge / Integration Practice。

---

## 一、这次核验要解决什么

旧版 `30_408/20_计算机组成原理/90_做题规则/README.md` 曾集中保存大量局部规则。它们本身多数正确，但触发信号已经直接指向 Booth、Cache、TLB、流水线、DMA 等具体 Topic。继续把这些内容全部留在 Subject Rules，会形成第二套题型手册，并和 Topic Practice 重复维护。

本轮不以“删短文件”为目标，而以**零信息丢失 + 唯一 Owner**为目标：

```text
旧 Subject Rules 条目
→ 判断真实作用域
→ 跨专题控制继续留 Subject Rules
→ 单一问题族规则下沉对应 Practice
→ 稳定机制/错误命题回到 Canonical Owner
→ 用 README 导航保证可检索
```

项目级题目质量、题目攻击模型与模型回归验证已由 `00_system/problem_model_validation.md` 统一拥有，不再由计组 Subject Rules 重复维护。

---

## 二、44 条原“待验证”规则逐条迁移核验

| # | 旧规则 | 当前唯一归属 / 主要入口 | 核验结果 |
|---|---|---|---|
| 1 | 先定位数据，再画通路 | 计组 Subject Rules「先表示状态、位置和路径」；CO-03《单总线数据通路与微程序控制》 | 保留跨专题骨架，数据通路细节下沉 |
| 2 | 区分可用时刻与提交时刻 | CO-04《流水线时空图、旁路与阻塞》；CO-I01《一条指令全过程推演》 | 完整保留 |
| 3 | 指令全过程题画三条线 | CO-I01《一条指令全过程推演》 | 完整下沉 Integration Practice |
| 4 | 流水线题先声明时序假设 | CO-04《流水线时空图、旁路与阻塞》「先抄模型，不先画气泡」 | 完整保留 |
| 5 | 依赖题比较 need 与 ready | CO-04 Practice | 完整保留 |
| 6 | Stall 与 Flush 分别追踪保留和作废 | CO-04 Practice 的 Bubble / Stall / Flush 状态规则 | 完整保留 |
| 7 | 分支惩罚从决策级和冲刷范围数 | CO-04 Practice | 完整保留 |
| 8 | 每个 miss/fault 写处理者 | 计组 Subject Rules「谁发现、谁处理、从哪重试」；CO-I01 Practice | 保留跨层骨架，细节归 Integration |
| 9 | 定长数题先声明“位串解释”和“目标位宽” | CO-01《机器数解释与补码速算》；《类型转换与混合表达式》 | 完整保留 |
| 10 | 扩展与截断题用“截后再扩”验证 | CO-01《类型转换与混合表达式》 | 原动作与停止条件均保留 |
| 11 | Carry 与 Overflow 分开判 | CO-02《标志比较与条件转移》；CO-01 Canonical | 完整保留，并进一步区分 CF/OF/ZF/SF |
| 12 | 乘除迭代题先固定寄存器布局和循环不变量 | CO-01《移位、Booth乘法与迭代除法》 | 完整保留 |
| 13 | 乘法溢出从足宽乘积压回目标格式 | CO-01《移位、Booth乘法与迭代除法》 | 完整保留 |
| 14 | 浮点运算先分类，再保留 GRS 舍入证据 | CO-01《IEEE754编码与浮点舍入》 | 完整保留 |
| 15 | 扩展操作码题画“剩余编码树” | CO-02《指令格式、扩展操作码与相对寻址》 | 完整保留 |
| 16 | 指令题先写架构状态差 | CO-03《单总线数据通路与微程序控制》；CO-02 Canonical 输出 Read/Derived/Write/Next PC | 保留为 ISA→Datapath 调用接口 |
| 17 | 寻址题先分 value、address、address-of-address | CO-02《指令格式、扩展操作码与相对寻址》 | 完整保留 |
| 18 | 寻址题先写 EA 生成式，再数访存 | CO-02《指令格式、扩展操作码与相对寻址》与《字节序对齐与有效地址》 | 完整保留 |
| 19 | 编码题逐层扣除扩展前缀 | CO-02《指令格式、扩展操作码与相对寻址》 | 与第 15 条合并为同一编码树模型，无信息删除 |
| 20 | 字节序题画地址—字节表 | CO-02《字节序对齐与有效地址》 | 完整保留 |
| 21 | 函数调用题分 ISA、ABI 与编译器选择 | CO-02《函数调用、ABI与编译器边界》 | 独立 Practice 新入口，完整保留并扩充边界 |
| 22 | 地址宽度与指令长度分开预算 | CO-02《指令格式、扩展操作码与相对寻址》 | 完整保留 |
| 23 | 数据通路题从 State Delta 开始 | CO-03《单总线数据通路与微程序控制》 | 完整保留 |
| 24 | 微操作并行性过四道 Gate | CO-03《单总线数据通路与微程序控制》 | 四个 Gate 原样保留为检查条件 |
| 25 | 单周期/多周期比较使用完整 CPU time | CO-03 Practice；跨专题性能控制仍由计组 Subject Rules / 性能工具承接 | 完整保留 |
| 26 | 流水线依赖写四个时刻 | CO-04 Practice 的 Produced / Ready / Need / Commit | 原四时刻模型完整保留 |
| 27 | 主存芯片题拆“字数”和“字长” | CO-05《主存组织与访问成本》 | 完整保留 |
| 28 | 存储题先列四种粒度 | CO-05《主存组织与访问成本》开篇粒度账本；计组 Subject Rules 的对象/单位控制 | 语义完整保留，表达更直接 |
| 29 | 存储性能题分 latency、cycle、bandwidth | CO-05《主存组织与访问成本》；CO-06《存储层次与AMAT》 | 完整保留，并补 throughput/access time |
| 30 | 交叉编址题区分一次延迟与稳态吞吐 | CO-05《主存组织与访问成本》 | 完整保留 |
| 31 | 磁盘题保持 LBA 与物理位置分层 | CO-05《主存组织与访问成本》 | 完整保留 |
| 32 | Cache 程序题先生成 reference stream | CO-06《Cache访问流与命中率》 | 完整保留 |
| 33 | 连续对象先算 footprint，再谈块数/页数 | CO-06《Cache访问流与命中率》；跨页接口由 CO-B02 Practice 调用 | 完整保留 |
| 34 | Cache 题先做地址三分，再跑状态机 | CO-06《Cache访问流与命中率》 | 完整保留 |
| 35 | Cache 题先统一“块、组、字节”单位 | CO-06《Cache访问流与命中率》 | 完整保留 |
| 36 | 地址翻译题先拆 VA，再分三种缺失 | CO-07《TLB与硬件地址翻译》 | 完整保留，明确 TLB miss / translation fault / Cache miss 分流 |
| 37 | TLB/Cache 组合题先检查索引是否落在页内偏移 | CO-B02《地址翻译与Cache综合训练》 | 完整下沉 Bridge Practice，并用 page-offset 位预算生成 VIPT 条件 |
| 38 | Cache miss 写完整生命周期 | CO-06《Cache访问流与命中率》与 Canonical | 完整保留 |
| 39 | AMAT 题先声明“平均谁、路径是什么、额外时间是什么” | CO-06《存储层次与AMAT》 | 完整保留并成为该训练文件主线 |
| 40 | 存储性能题先数事件，再给事件定价 | 计组 Subject Rules「先数事件，再给事件定价」；《存储系统真题训练总索引》 | 作为跨 Topic 控制保留，存储实例进入索引 |
| 41 | 总线和 DMA 题同时追踪三种占用 | CO-08《总线仲裁、中断与DMA状态推演》；计组 Subject Rules 状态/资源与事件成本骨架 | 核心信息保留为共享资源时间线与可重叠工作 |
| 42 | 总线/I-O 题先拆请求、事务与完成 | CO-08《总线仲裁、中断与DMA状态推演》 | 完整保留 |
| 43 | DMA 题先写控制器描述符与所有权转移 | CO-08 Canonical +《总线仲裁、中断与DMA状态推演》 | source/destination/length/direction/descriptor、仲裁与完成边界均保留 |
| 44 | 性能公式先声明串行项、并行项和单位 | 计组 Subject Rules「性能比较只认完整工作量和完整时间」；《性能指标与程序执行时间》；CO-08 总线性能 Practice | 跨专题骨架保留，具体成本模型分流 |

---

## 三、旧“性能工具箱”中的 4 条控制核验

| # | 旧规则 | 当前归属 | 核验结果 |
|---|---|---|---|
| 45 | 性能题先走完整 Cost 坐标 | 计组 Subject Rules 的对象→状态/路径→事件→成本；《性能指标与程序执行时间》 | 被压缩成跨专题主线，没有删除 |
| 46 | CPI 低不等于程序必然快 | 《性能指标与程序执行时间》；计组 Subject Rules「性能比较只认完整工作量和完整时间」 | 完整保留 |
| 47 | 流水线题分 throughput 与 latency | CO-04《流水线时空图、旁路与阻塞》 | 完整保留 |
| 48 | 带宽题写瓶颈与协议效率 | CO-08《总线事务、定时与有效带宽》 | 完整保留，并细化 transaction / payload / wait / burst |

`90_做题规则/性能指标与程序执行时间.md` 现在明确标注为**跨 Topic 训练工具，不是 Subject Rule，也不是新的 Handbook 类型**；`存储系统真题训练总索引.md` 同样只做跨 Owner 训练导航。

---

## 四、8 条旧“已否定”命题逐条核验

| # | 旧错误命题 | 当前 Owner | 核验结果 |
|---|---|---|---|
| 1 | “同位宽整数除法永不溢出” | CO-01 Canonical +《移位、Booth乘法与迭代除法》 | 保留 `minint / -1` 反例 |
| 2 | “除零一定由硬件中断，所有架构处理相同” | CO-01 Canonical +《移位、Booth乘法与迭代除法》 | 保留“硬件可检测，架构结果由 ISA 决定”边界 |
| 3 | “RISC 必然硬布线，CISC 必然微程序” | CO-02 / CO-03 Canonical；CO-02 指令格式 Practice | 明确 ISA 设计轴 ≠ 控制实现轴 |
| 4 | “单周期处理器必然使用哈佛结构” | CO-03 Canonical + Practice | 保留资源冲突判据与多种实现选择 |
| 5 | “DMA 传输让 CPU 开销恒为 O(1)” | CO-08 Canonical + DMA Practice | 保留描述符、映射、一致性、完成处理等成本 |
| 6 | “PC、PSW、Cache、MMU 对所有软件都完全不可见” | CO-02 Canonical | 保留 ISA / 特权级 / 平台接口相对可见性 |
| 7 | “寄存器可访问性有跨架构固定四级清单” | CO-02 Canonical | 保留“读取/写入/配置/间接影响”判据，不维护固定跨架构清单 |
| 8 | “流水线越深一定越快” | CO-04 Canonical + Practice + 性能工具 | 保留完整 CPU time 与寄存器/分支/依赖成本边界 |

这些错误命题不再需要在 Subject Rules 中重复一遍；它们已经进入最相关 Canonical / Practice 的失败边界，复习具体 Topic 时可以直接看到。

---

## 五、项目级规则重构核验

本轮新增或调整的系统职责形成下面的唯一 Owner 关系：

| 任务 | 唯一 Owner |
|---|---|
| 单题怎样表示、选路径、执行、校验 | `01_control/problem_solving_kernel.md` |
| 题面是否自洽、题目是否打穿模型、模型修改后怎样回测 | `00_system/problem_model_validation.md` |
| 候选规则是否值得保留、作用域在哪里、是否晋升 | `00_system/evidence_promotion.md` |
| 局部训练 Markdown 应怎样组织 | `00_system/topic_practice_writing_spec.md` |
| Handbook 机制正文怎样写、怎样收束 | `00_system/handbook_writing_spec.md` |
| 真题 Derived Solution 的质量门 | `00_system/exam_solution_quality_assurance.md` |

关键路由已同步到 `AGENTS.md`、`agent_context_protocol.md`、`architecture.md`、`handbook_contract.md`、`collaboration_workflow.md`、`ownership_matrix.md` 与真题题解执行/写作规范。

### 当前统一的作用域闸门

```text
触发信号已经是某个 Topic 专有对象
→ 默认进该 Topic / Bridge / Integration Practice

同一动作跨多个独立训练专题仍成立
+ 去掉具体 Topic 名仍然清楚
+ 统一维护确实减少重复
→ 才考虑 Subject Rules

跨学科、跨考试仍然成立
→ 优先检查 problem_solving_kernel.md
```

位置与成熟度分开判断：局部规则即使验证成熟，也不因为“成熟”自动上移 Subject Rules。

---

## 六、验证结论

1. 旧计组 Subject Rules 中 **44 条待验证规则 + 4 条性能工具控制 + 8 条已否定命题，共 56 项**，本轮逐项核验均有当前归属；没有因为职责收缩而删除唯一知识或训练信息。
2. 当前计组 Subject Rules 只保留真正跨专题的控制：对象/口径、实现条件、状态/路径、事件计数、跨层处理者、前置/后置 Verification、完整性能成本。
3. 所有本轮新增的计组 Practice 文件均具有“训练定位 + 模型归属”头部，并已进入各 Topic / Integration README 的正式训练导航。
4. `性能指标与程序执行时间.md` 与 `存储系统真题训练总索引.md` 已明确为跨 Topic 的 Learning / Practice 工具，不因位于 `90_做题规则/` 而获得 Subject Rule 或 Handbook 身份。
5. 真题与可编辑练习题在题目质量门上的处理已分开：练习题可先修题面；真题保持 Canonical Source 原文，只在题解 / review 记录歧义。
6. Handbook 新增“扰动 / 拒绝”成熟度检查，并要求一页压缩之后不再出现新的主干机制；模型更新后的回归由 Practice 中少量代表题承担，不建立额外数据库。

因此，本轮属于**职责重排与控制接口清理，不是知识删减**。后续若再出现“某一条规则该放哪里”的争议，先按 `problem_model_validation.md` 和 `evidence_promotion.md` 判断问题层与作用域，不再把内容默认堆回 Subject Rules。
