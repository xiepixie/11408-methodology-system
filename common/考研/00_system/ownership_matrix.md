# Canonical Ownership Matrix

本表只在准备修改稳定 Handbooks 或正式 Rules 时使用。它不约束 Inbox，也不要求预先登记所有知识点。

## 1. 这张表解决什么

发现重复或准备修改核心概念时，只问：

1. 谁负责完整定义它？
2. 其他文件是在 Use、Bridge、Integrate，还是只记录 Extension / Anti-Bridge 关系？
3. 修改以后需要检查哪些下游内容？

Owner 应尽量定位到具体 Handbook 或 Rules 文件。尚未建立工作文档时，只能写“规划归属”，不能假装已经存在 Canonical Owner。

## 2. 简单状态

- **规划**：大致知道归属，但稳定文件还不存在；
- **有效**：唯一 Owner 已存在，可以作为引用入口；
- **冲突**：出现两个定义位置，需要先决定谁拥有；
- **废弃**：旧位置停止维护，只保留新 Owner 指针。

日常不需要为每个概念维护状态。只有真正进入台账的项目才使用。

## 3. 408 当前规划

408 日常唯一 Course Atlas 见 [30_408/README.md](../30_408/README.md)；架构设计依据见 [408 学科架构](../30_408/00_统一总图/408%20学科架构.md)。本表只登记最容易重复或跨界的概念。

### 3.1 数据结构

| 概念或机制 | 规划归属 | 常见使用位置 | 边界提醒 |
|---|---|---|---|
| Complexity / Operation Cost Vector | `10_数据结构/README.md` Atlas Foundation | 全部数据结构 Topic | 是全科学术语/度量语言，不再建立独立 complexity Topic |
| Frontier Traversal Model | `10_数据结构/50_科内桥梁/DS-B01_FrontierTraversal/README.md` | Tree、Graph、Stack、Queue | Tree/Graph 各自拥有结构语义，Bridge 只拥有 frontier 展开接口 |
| Heap / Priority Queue | `10_数据结构/05_Heap与优先队列/README.md` | Heap Sort、Prim、Dijkstra | 排序和图算法只调用优先级操作 |
| Union-Find | `10_数据结构/06_UnionFind与集合划分/README.md` | Kruskal、动态连通 | 图算法只调用 Find/Union |
| Ordered Index Trade-off | `10_数据结构/50_科内桥梁/DS-B02_IndexStrategy与Workload/README.md` | Binary Search、BST、AVL/RB、B/B+、Hash | 各 Topic 拥有机制，Bridge 拥有 workload/cost 比较 |

### 3.2 计算机组成原理与 OS

| 概念或机制 | 规划归属 | 常见使用位置 | 边界提醒 |
|---|---|---|---|
| ISA / Addressing / C Mapping | 计组 ISA 与机器级程序 Topic | CPU、CO-B01 | C→ISA 仍由 ISA Topic Own；CO-B01 只解释 ISA semantic→datapath |
| Datapath / Control Signal | 计组 CPU 数据通路与控制 Topic | Pipeline、Instruction Integration | Pipeline 不重新定义单指令完整微操作 |
| Hardware Cache | 计组 Cache Topic | CO-B02、X-I01 | 不与 OS Page Cache 混同 |
| TLB / Page Walk / VA-to-PA Hardware Path | 计组地址翻译硬件 Topic | CO-B02、X-B02、X-I01 | 计组拥有硬件翻译；OS 拥有映射修复和策略 |
| Process / Thread / Blocking / Wakeup | OS 进程与调度 Topic | I/O、并发、综合过程 | Topic 定义执行实体与状态变化，综合册只追踪过程 |
| Page Fault / Frame Allocation / Replacement / COW | OS 虚拟内存 Topic | X-B02、OS-B02、X-I01 | 翻译硬件、驻留修复和置换策略必须分层 |
| OFD / inode / dentry | OS 文件系统 Topic | Process、fork、dup、unlink、read 综合 | 文件系统定义对象与生命周期；Process 只使用引用 |
| DMA Controller / Bus Transfer | 计组 I/O Topic | X-B03、X-I02 | 计组拥有控制器、总线与传输机制 |
| DMA Submit / Complete / Wake | OS I/O + X-B03 | OS-I01、X-I02 | OS 拥有 request/completion/task state；X-B03 只拥有软硬件 handoff |
| Page Cache | `30_操作系统/60_科内桥梁/OS-B04_VMFileIO/README.md` | VM、文件系统、OS I/O、read Integration | File 拥有内容身份，VM 拥有驻留映射，I/O 拥有 miss/writeback；Hardware Cache ≠ Page Cache |

### 3.3 计算机网络

| 概念或机制 | 规划归属 | 常见使用位置 | 边界提醒 |
|---|---|---|---|
| Sliding Window / GBN / SR | 可靠传输 Topic | TCP | TCP 只解释协议实例化 |
| Flow Control / `rwnd` | Transport/TCP Topic | 拥塞专题、网络综合 | 保护 receiver，不等于保护 network |
| Congestion Control / `cwnd` | 拥塞专题 | TCP、网络综合 | TCP 只引用具体拥塞状态和动作 |
| ARP | IP 地址与分组转发 Topic | 单跳交付、网络综合 | 解决 NextHopIP -> MAC；单跳册拥有 frame 交付 |
| Switch Table | 单跳交付 Topic | 网络综合 | Source learning 与 destination forwarding |
| Forwarding Table Lookup | IP 地址与分组转发 Topic | 路由、网络综合 | 使用表执行 LPM |
| Forwarding Table Generation | 路由 Topic | IP 转发 | DV/LS/BGP 等负责生成和更新状态 |
| TCP Connection State | Transport/TCP Topic | X-B04 Candidate Core、网络综合 | 网络拥有协议状态；OS 拥有 process/socket object；X-B04 只拥有 endpoint handoff |
| DNS | 应用层 Topic | 网络综合 | Integration 只调用 Name -> IP |

### 3.4 408 Cross-Subject

| 接口/过程 | 规划归属 | 状态/边界 |
|---|---|---|
| Privilege / Exception / System Call × OS Control | `30_408/50_桥梁专题/X-B01_PrivilegeExceptionSystemCall与OSControl/README.md` | Core Bridge；计组 Own privilege/exception entry，OS Own kernel-side mechanism |
| Hardware Address Translation × OS VM | `30_408/50_桥梁专题/X-B02_HardwareAddressTranslation与OSVirtualMemory/README.md` | Core Bridge；PTE/fault/retry handoff；TLB miss ≠ Page Fault |
| Interrupt / DMA × OS I/O | `30_408/50_桥梁专题/X-B03_InterruptDMA与OSIO/README.md` | Core Bridge；硬件 transfer/delivery 与 OS completion/wakeup 分责 |
| Process / Socket × Transport Endpoint | `30_408/50_桥梁专题/X-B04_ProcessSocket与TransportEndpoint/README.md` | Candidate Core；接口结构已确认，是否升级为 Core 待考纲/真题覆盖证据 |
| Graph Algorithm × Routing | Network Routing `Use` DS08 | 不独立建 Core；保留 Candidate/Extension note |
| External-Memory × Block I/O | DS12 `Use` block-I/O cost model | 不独立建 Core；只有当两侧反复重复解释或长期说不清交接责任时再重判 |
| Data Structure × Systems | 不建立大桥 | 系统 Topic 直接 Use 具体 DS Owner |
| LOAD / Memory Access slow path | `30_408/60_综合专题/X-I01_LOAD与MemoryAccess慢路径/README.md` | Cross-Subject Integration；不重新拥有 TLB/Cache/Page Fault |
| Blocking File read lifecycle | `30_408/60_综合专题/X-I02_BlockingFileRead完整生命周期/README.md` | Cross-Subject Integration；组合 OS-I01、CO I/O、X-B01/X-B03 |

这些是规划 Owner / 框架状态，不代表正文已经人工采用。

正式 OS Subject 入口见 [30_408/30_操作系统/README.md](../30_408/30_操作系统/README.md)。

## 4. 数学一当前归属

| 内容 | 规划归属 | 边界提醒 |
|---|---|---|
| 数学一 Course / Exam Atlas、三科地图、共享 Control Language | `10_数学一/README.md` | 上层 Atlas 只组织三门 Subject 与跨学科接口，不强迫三科共享统一世界模型 |
| 高等数学学科母模型与 Topic 地图 | `10_数学一/10_高等数学/README.md` | Subject Atlas 拥有高数生成结构、Topic 地图与 internal Bridge 导航；旧 PDF 不拥有工作态知识 |
| 数学一 Cross-Subject Core Bridge Atlas | `10_数学一/50_桥梁专题/README.md` | 只拥有跨 Subject 稳定接口；高数/线代/概率 Topic 保留本体机制 |
| B00 内积、正交与投影 | `10_数学一/50_桥梁专题/B00_内积正交与投影/README.md` | 几何↔内积/正交/投影翻译；不把正交等同概率独立 |
| B01 局部线性化 | `10_数学一/50_桥梁专题/B01_局部线性化_微分与线性映射/README.md` | 拥有“可微=最佳局部线性映射”接口，不重新拥有微分或线性映射本体 |
| B02 Jacobian 与行列式 | `10_数学一/50_桥梁专题/B02_Jacobian与行列式_坐标变换与局部体积缩放/README.md` | Cross-Subject 唯一 Owner；高数 Topic07/08 只 Use |
| B03 Hessian 与二次型 | `10_数学一/50_桥梁专题/B03_Hessian与二次型_二阶局部形状与正定性/README.md` | Cross-Subject 唯一 Owner；高数多元极值和线代二次型分别保留本体机制 |
| B04 梯度、正交与 Lagrange | `10_数学一/50_桥梁专题/B04_梯度正交与Lagrange_约束极值与子空间几何/README.md` | 拥有切空间/法空间接口，不重新定义高数 Lagrange 或线代正交 |
| B05 线性方程与线性微分方程 | `10_数学一/50_桥梁专题/B05_线性方程与线性微分方程_一点加Kernel/README.md` | 拥有“特解+kernel”共享结构；矩阵系统深层结构可标 Extension |
| B06A PDF 与 CDF | `10_数学一/50_桥梁专题/B06A_PDF与CDF_局部概率密度与累积/README.md` | 拥有 density↔accumulation 的 FTC 接口，不把 density 值当概率 |
| B06B 期望、联合概率与边缘化 | `10_数学一/50_桥梁专题/B06B_期望联合概率与边缘化_概率的积分语言/README.md` | 拥有概率质量/权重怎样调用积分汇总的接口，不拥有概率定义 |
| B07 随机变量变换与 Jacobian | `10_数学一/50_桥梁专题/B07_随机变量变换与Jacobian_概率质量守恒/README.md` | 拥有坐标重表达下概率质量守恒；必须同步变换 support |
| B08 Fourier 与正交基 | `10_数学一/50_桥梁专题/B08_Fourier与正交基_函数表示与正交投影/README.md` | 只拥有正交投影理解接口；无限维理论标 Extension |
| 数学一 Integration Layer | `10_数学一/60_综合专题/README.md` | 只拥有代表性完整问题（Canonical Problem）的模块组合轨迹，不重新拥有 Topic/Bridge |
| 高数 internal Bridge | `10_数学一/10_高等数学/50_桥梁专题/README.md` | 只处理高数 Topic↔Topic 接口；Jacobian/Hessian 等跨 Subject 接口必须上移 |
| 高数微积分建模 Integration | `10_数学一/10_高等数学/60_综合专题/H-I01_微积分建模_从局部微元到整体量/README.md` | 拥有完整建模协作轨迹，不拥有局部积分/求导机制 |
| 定义域、非零和等价性检查 | 数学 Subject Rules | 是操作检查，不重新定义函数和代数机制 |
| 分部积分机制 | 高数积分 Topic | 负责公式、适用条件和结构变化 |
| 分部积分拆法选择 | 高数做题 Rules | 负责识别信号和起手动作，引用机制 Topic |
| 线性代数学科母模型与 Topic 地图 | `10_数学一/20_线性代数/README.md` | Canonical Subject Atlas；README 直接拥有“对象—表示—合法变换—不变量—最简合法表示”、三类标准化关系、Topic 地图与跨册路由。旧 Atlas `.tex` 只作为 Source / 旧阅读视图 |
| 线性组合、基、维数、坐标与正交 | `10_数学一/20_线性代数/01_向量空间_生成基与坐标/向量空间_生成基与坐标.tex` | Canonical Topic01；README 只做 Landing。拥有表示骨架，不拥有映射作用、rank 的统一机制与谱结构 |
| 线性映射、矩阵表示、可逆与行列式 | `10_数学一/20_线性代数/02_线性映射_矩阵与行列式/README.md` | 工作稿 Owner；行列式按体积因子与可逆性解释，计算技巧留给 Rules |
| rank、基本子空间与矩阵等价 | `10_数学一/20_线性代数/03_秩_基本子空间与等价/README.md` | 工作稿 Owner；拥有初等变换下的自由度不变量，不拥有具体右端项解集 |
| 线性方程组、逆像、基础解系与同解 | `10_数学一/20_线性代数/04_线性方程组_可达性与解空间/README.md` | 工作稿 Owner；用 image/kernel 研究可达性和仿射解集 |
| 特征结构、相似、对角化与可交换接口 | `10_数学一/20_线性代数/05_特征结构_相似与对角化/README.md` | 工作稿 Owner；拥有算子自然坐标，不拥有二次型惯性 |
| 二次型、合同、惯性与正定 | `10_数学一/20_线性代数/06_二次型_合同惯性与正定/README.md` | 工作稿 Owner；拥有变量换元下的符号结构，调用实对称谱定理 |
| 概率统计学科母模型与 Topic 地图 | `10_数学一/30_概率论/README.md` | Atlas 只拥有母模型、Topic 地图和跨册压缩 |
| 事件、样本空间与概率公理 | `10_数学一/30_概率论/01_随机世界_事件与概率/README.md` | 工作稿 Owner；不拥有条件更新与随机变量分布 |
| 条件概率、独立性、全概率与 Bayes | `10_数学一/30_概率论/02_条件概率_独立性与Bayes/README.md` | 工作稿 Owner；连续条件分布的计算接口交给联合分布 Topic |
| 随机变量与一维分布 | `10_数学一/30_概率论/03_随机变量与一维分布/README.md` | 工作稿 Owner；拥有观察函数、CDF、PMF、密度与分布生成语义 |
| 联合、条件、边缘与变量变换 | `10_数学一/30_概率论/04_联合分布_条件分布与变换/README.md` | 工作稿 Owner；拥有支撑几何与概率质量重组 |
| 期望、方差、协方差与条件摘要 | `10_数学一/30_概率论/05_数字特征与依赖摘要/README.md` | 工作稿 Owner；只拥有摘要机制，不拥有完整分布 |
| 大数定律与中心极限定理 | `10_数学一/30_概率论/06_大数定律与中心极限定理/README.md` | 工作稿 Owner；区分稳定位置与标准化波动 |
| 总体、样本、统计量与抽样分布 | `10_数学一/30_概率论/07_总体样本与抽样分布/README.md` | 工作稿 Owner；拥有统计随机标尺，不作推断决策 |
| 参数估计、置信区间与假设检验 | `10_数学一/30_概率论/08_参数估计与假设检验/README.md` | 工作稿 Owner；用抽样分布校准逆向推断 |
| 概率统计目标层识别、路径选择与校验 | `10_数学一/90_学科做题规则/概率统计.md` | 当前为待验证 Rules，不重复定义分布机制 |

“机制”和“怎样在题中选择机制”属于不同职责，不能因为写在同一篇文章里就混成同一个 Owner。

## 5. 英语一

英语一尚未形成稳定 Ownership。开始建设时，优先区分：

- 句法和篇章机制属于 Knowledge；
- 阅读、翻译和写作动作属于 Rules；
- 干扰项或个人错误经验先进入 Inbox。

## 6. 既有发布物

`90_publish/` 中既有 PDF 若尚未能追溯到当前唯一 Canonical `.tex` Owner，则暂称 `legacy-unregistered`。这只表示它们尚未完成当前 Ownership 与 Source-of-Truth 梳理，不评价内容质量。

不为目录整齐批量搬迁。只有真实修改某本手册时，才顺手确认它拥有、使用和发布了什么。

## 7. 修改稳定内容时的最小流程

1. 全文搜索现有定义和同义词；
2. 判断这是机制、接口、综合轨迹还是做题规则；
3. 选择唯一 Owner；
4. 其他位置改成最小摘要和引用；
5. 搜索受影响的 Bridge、Integration、Rules 和发布稿；
6. 同步能处理的内容，明确留下不能处理的依赖。

若归属争议暂时无法解决，内容继续留在 Inbox 或标记冲突，不通过复制绕开问题。
