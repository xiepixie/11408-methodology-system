# 当前焦点

- **系统阶段**：从“搭建 Handbook”转入“证据验证与跨学科 Bridge 增强”。各科的 Atlas、Topic、Bridge、Integration 和 Rules 已有稳定的 Owner；接下来只因真题、陌生题或逐项 Source Diff 暴露缺口而更新 Canonical。
- **本轮已完成**：2015～2026 共 564 份 408 model-grounded 题解已完成年度闭环。2015 已补齐 Q1～Q47、年度 README 与 `solution_review.md`，并修正 Q11 legacy 学科路由、Q41 链表去重实现、Q42 邻接矩阵幂语义、Q45 过度同步、Q47 MAC 文本污染等 Derived 问题。`exam_solution_quality_assurance.md` 继续作为学生学习责任、固定 H2、Model Feedback Closure 与六道质量 Gate 的唯一 QA Owner。
- **当前最重要的验证问题**：从“题解存在”推进到“题解能让学生复原模型，并能反向修模型”。2015～2026 已连续 12 年完成年度 Gate；下一步进入 2014。Candidate Rule 继续走 Evidence Promotion，但若真题独立证明 Canonical Handbook 存在事实/机制/边界硬错误，则立即进入 Stable Write 并重新验证受影响题解，不再长期只记 Challenge。
- **维护原则**：旧总图、旧 README 和个人 Source 只有在逐项 Source Diff / Owner 对照能证明 Canonical 已无损承接后才允许清理退休副本；未能证明承接关系的历史 Source 继续保留。

## 当前已完成

### 架构与控制

- 408 Course Atlas、四个 Subject Atlas、内部 Bridge Atlas 已改为 Markdown Canonical Map；Topic / Bridge / Integration 的机制正文由各自 `.tex` Owner 持有。
- `check`、`audit`、`publish`、`publish-view` 的职责边界已固定；`PROGRESS.md` 由脚本生成，不手工维护。
- Handbook 写作、Owner / Uses / Boundary、Evidence Promotion、Source Diff 和发布入口已有项目级契约。

### 数学一

- 高数 12 Topic、5 个高数内部 Bridge、H-I01 及数学一跨科 B00--B08 已建立 Canonical 候选正文并发布；高价值 Source 已完成首轮路由，Rules 仍待真题/陌生题攻击。
- 线性代数 Topic01--06 已完成两轮 Source / Model Diff 并重新发布；1987--2025 可用数学一真题已完成按 L01--L06 的全量分类与模型对抗审计，其中 2020 真题补出“两个实对称表示经公共谱坐标合成正交变换”的 Topic06 接口并收窄 R-LA18。Atlas 已补充“任务契约先行”的考场路由；线性代数 Rules 继续保持待验证，下一步是每个 Topic 选陌生题做无提示盲测，已否定的绝对化规则继续保留最小反例。
- 概率统计已完成归档 Source Pack 的反向结构审阅和 Topic01--08 修正；正文与 Rules 尚未因缺少陌生题证据升级为成熟状态，Published View 仍有环境同步债务。

### 408

- 数据结构 12 个 Core Topic、DS-B01--B03、DS-I01 已完成 Source Diff、代码与测试核对并发布；外部算法笔记 66 篇已逐篇路由并完成第二轮机制级核销。DS-I01 已补组合设计、频率 Top-K、信息流与规模升级；DS-A01--A04 已补数组、回溯、DP、贪心的边界与证明；DS04/09/11 已补最小深度、BST 派生查询、逆序对与负数排序。当前只剩真实题目上的迁移证据，Rules 仍保持 Candidate。
- 计算机组成原理 CO01--08、CO-B01/02、CO-I01 已建立并发布；本轮已完成外部 CO 笔记 65 个原子条目的 Source Diff 与 CO-01--08 增量吸收，补齐表示/ALU、ISA 工具链、CPU 控制器、流水/并行、主存/Cache/虚存、总线/I/O 的细节，并用六类陌生组合题完成第一轮心智模型对抗验证；Rules 仍待真实题面重复验证。
- 操作系统外部笔记 76 篇已完成全量 Source Diff 与六册 Handbook 增量吸收：OS-00 23 页、OS-01/02 50 页、OS-03 36 页、OS-04 25 页、OS-05 31 页、OS-06/07 24 页均已发布并完成页面检查；OS-B01--B04 已完成第二轮接口语义收敛并重发，OS-I01 Blocking `read()` 与 OS-I02 `fork()`+COW+资源引用已建立 5 页 Canonical Integration 阅读版。模拟器仅吸收生成性算例与观察变量，未迁移 UI 指南；Rules 与新 Integration 仍待真实题面重复验证。
- 计算机网络已按 2026 转载考纲基线完成结构覆盖补缺：Atlas Foundation、NET01/02/04/05/06/07/08 已补齐原 B/C 缺口并发布；NET-B01--B04 已重构，NET-B05（BDP×Window）与 NET-B06（MTU×Segmentation）通过 Gate、建册并发布。2025 Q33～Q40 与 Q47 已完成 model-grounded 真题校准，覆盖交换性能、码距、CSMA/CD、DHCP、NAT、TCP 窗口、应用层时序与卫星链路/GBN/VLSM；X-B04 仍保持 Candidate Core。
- 2025 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2025年真题/solutions/`。年度 `solution_review.md` 已把 legacy correction、模型澄清、解题质量改进与候选 Rules Evidence 分层记录；当前没有因单年样本直接改写 Handbook。
- 2026 年 408 已完成 Q1～Q47 全套心智模型题解并完成第二轮格式统一审阅，入口为 `archives/408/2026年真题/solutions/`。本轮同时修正 Q43 指令格式恢复、Q37 路由聚合答案分叉等 Derived/Source 问题，并把 Q28 PTE 隐含条件、Q44 分值元数据、Q47 初始拥塞窗口条件等集中记录到年度 `solution_review.md`。
- 2024 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2024年真题/solutions/`。题解过程中确认原 Canonical Q12～Q32 存在系统性错位，并连同 Q4/Q9/Q10/Q11/Q33～Q40 一并恢复；Q41 拓扑唯一性、Q42 开放定址、Q46 最少信号量、Q40 HTTP RTT 等 legacy 解析错误已在 Derived Layer 修正。
- 2023 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2023年真题/solutions/`。本轮修正 Q21 Canonical 语义错误与 Q11 学科路由；Q42 Replacement Selection、Q43 Page/Block/Set、Q44 Next-PC/Endian、Q45 原子互斥、Q46 I/O 等待-唤醒、Q47 FTP/TCP 均完成模型化推导与独立校验。
- 2022 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2022年真题/solutions/`。本轮修正 Q11 学科路由，并对 Q17 DRAM 地址复用、Q19 扩展操作码、Q30 缺页率边界、Q41 BST 不变量、Q42 Top-K 大根堆、Q43 单总线控制、Q44 DMA、Q45 inode 身份、Q46 偏序同步、Q47 二层/无线地址语义完成独立模型化审阅。
- 2021 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2021年真题/solutions/`。本轮修正 Q02 输出受限双端队列术语与 Q11 学科路由，并对 Q41 邻接矩阵维度错误、Q42 稳定性 tie-breaking、Q43 位宽 Owner/溢出、Q44 TLB 组内 LRU、Q45 Safety+Progress、Q47 DNS/ARP/交换机事件链完成独立模型化审阅。
- 2020 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2020年真题/solutions/`。本轮修正 Q11 学科路由、Q41“正数”与负数示例的 Canonical 冲突，并清除 Q47 正式题面中误混入的已填 NAT 答案图；Q41～Q47 均按 Problem Representation / Decision Points / Verification 深度 Gate 重写。
- 2019 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2019年真题/solutions/`。本轮确认 2019 是独立历史路由变体：Q43～Q44 属于操作系统、Q45～Q46 属于组成原理；同步修正 `exam_profiles/408.json`、年度分值元数据与索引。Q43 的 `min(m,n-1)`、Q45 的 Next-PC/小端/有符号 OF、Q46 的页内偏移到 Cache set、Q47 的三层 Scope 均完成独立模型化验证。
- 2018 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2018年真题/solutions/`。本轮修正 Q11 legacy 学科路由；Q41 明确候选域 `[1,n+1]` 并修复 legacy 越界，Q42 恢复两棵总费用 16 的 MST 并按方案分别验证 TTL，Q44 强化 `VA→PA→Cache` 分层，Q45 以 Address-Space Owner 判断 PDBR，Q46 以 inode/data 双资源瓶颈与索引深度推导容量/访问时间，Q47 完成 `/25` Scope 与 IPv4 分片守恒验证。
- 2017 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2017年真题/solutions/`。本轮修正 Q11 legacy 学科路由；Q41 用树结构 Owner 生成中缀表达式，Q42 用 Prim cut invariant 与 exchange 判断唯一性，Q43 分离 unsigned/signed/float precision/range，Q45 固化 `Blocked→Ready≠Running`，Q46 以 R/W conflict graph 保留 reader-reader 并发，Q47 用 `send_base/recv_next` 双账本重建 GBN 累计确认、回退重传和 50% 利用率。
- 2016 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2016年真题/solutions/`。综合题按年度 Profile override 路由：Q41 网络、Q42～Q43 数据结构、Q44～Q45 计组、Q46～Q47 OS；年度 README 与 `solution_review.md` 已建立，Derived 错误与 Handbook Challenge 已分层记录。
- 2015 年 408 已完成 Q1～Q47 全套心智模型题解，入口为 `archives/408/2015年真题/solutions/`。本轮纠正 Q11 legacy 学科路由；Q18 用 `bank identity + timing` 重建交叉存储冲突条件；Q41 用有限值域直接寻址实现 $O(m)$ 链表去重；Q42 恢复完整邻接矩阵与 walk-count 模型；Q45 区分 semantic permit 与 implementation mutex；Q47 按 DHCP/ARP/next-hop Scope 重建地址生命周期。
- **408 题解 QA 已纳管**：2015～2026 的 564 份题解均受选择题 `Model Anchor→解题链→选项判断→Verification→Compression→易错边界`、综合题 `Model Anchor→Problem Representation→Decision Points→Solution Chain→Verification→Compression→易错边界` 的 hard gate 约束；跨年审阅记录见 `80_evidence/review_log/2026-08-16_408真题题解跨年质量审阅_v1.md`。格式一致性进入仓库 hard check，语义正确性仍由独立推导、年度 Verification 与 Model Feedback Closure 负责。

### 跨学科 Bridge

- Bridge v1 审阅覆盖数学、数据结构、计组、OS、网络和跨科目录，共 32 个具体目录；本轮确认了接口、独立不变量、最小例子、调用时机、停止条件和 Anti-Bridge 边界。
- OS-B01--B04、NET-B01--B06、X-B01、X-B02、X-B03 已有唯一深度正文；X-B04 与 AI 跨 Area Bridge 继续保持 Candidate，不因目录存在而提前成熟化。

## 下一步候选

1. **408 历年真题题解批处理**：2015～2026 已完成年度闭环，下一年度进入 2014。继续按 `Source -> Model Anchor -> Representation/Decision -> Solution -> Verification -> Compression -> Model Feedback Closure` 倒序推进；partial 年度只接受题级 Gate，整年完成时必须通过 47/47 + README + `solution_review.md` 的年度 hard gate。
2. **Rules Evidence 累积**：跨年份统计重复出现的题目信号、第一动作、风险点与校验动作；只有稳定跨题迁移后才通过 Evidence Promotion 更新四科 Rules。2025 的单年模式先保持 Candidate Evidence。
3. **Handbook Challenge 路由**：若历年题与 Canonical Handbook 真正冲突，先确认题面、适用边界与 Owner；局部 legacy 题解错误只修 Derived Solution，不反向污染 Handbook。
3. **X-B04 Promotion Evidence**：收集两道独立 408 题或明确考纲覆盖，验证阻塞接收、socket buffer 与 endpoint demux 是否产生不可替代推理；在此之前保持 Candidate。
4. **概率发布与验证**：解决 `STHeiti` 环境导致的 Published View 同步问题，然后用陌生题验证非矩形支撑、变量变换、抽样分流、MLE 和区间/检验尾部对偶。
5. **旧 Source 逐项核销**：继续审计 408 统一总图及根级旧 Atlas `.tex`；完成前只保留/标注 Source，不删除。
6. **LaTeX Semantic-Margin Gate**：仅在不抢占证据验证资源的前提下，用少量真实边栏对象验证检索收益；不再以“能否排下”为主要目标。

## 待人工决定

- 线性代数、概率统计 Atlas 的地图状态仍需人工确认；正文已建和 Rules 待验证不能直接改成已采用。
- 旧总图、旧 Atlas `.tex` 和旧 README 是否可删除，必须等 Source Diff 明确列出 Covered / Update / Reject / 未决项；本轮 review log 归档不改变这一门槛。
- X-B04、AI 跨 Area Bridge 是否值得建立独立正文，等考纲覆盖与重复调用证据，不因“接口看起来合理”提前升级。

## 当前阻塞

- **无硬阻塞**：仓库检查与 Bridge 发布入口可用。
- **维护债务**：概率统计仍受 `STHeiti` 字体环境影响；共享编译机制已切到 `infra/scripts/compile_tex.py`，Kaoyan publish preflight 与 `90_publish/` 路由继续由 `cognitive_system.py` 显式拥有；网络八册与 NET-I01 的 Published View 已同步。当前无由 Infra Cutover 引入的新硬阻塞。
- **证据债务**：大多数 Rules 只有 Source / 机制重建支持，尚缺使用者在陌生题中的重复验证；因此当前状态应读作“Canonical 候选 + Candidate Rules”，不是“全部成熟”。

## 复盘入口

- 当前日志索引：[review_log/README.md](80_evidence/review_log/README.md)
- 已完成审阅归档：[archive/review_log/README.md](80_evidence/archive/review_log/README.md)
- Bridge 审阅台账（归档）：[2026-08-12_Bridge逐册审阅台账_v1.md](80_evidence/archive/review_log/2026-08-12/2026-08-12_Bridge逐册审阅台账_v1.md)
