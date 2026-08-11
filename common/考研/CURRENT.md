# 当前焦点

- **已完成**：考研数学一三门核心主干手册 (高等数学 v2、线性代数 v2、概率论与数理统计 v2) 的图表拓扑重构、出版级 5 列【概念边界】长表格升级与 100% 编译发布。
- **当前阶段**：线性代数已完成第二轮旧稿 Source Migration：`学习领域/归档/线性代数/` 的 11 篇高质量个人笔记已逐篇做 Source Diff / Owner Diff，高价值主干已拆入 Topic01–06 Canonical `.tex`，考试动作已收敛到线性代数待验证 Rules；高级/超纲内容继续留作 Source / Extension。下一阶段进入真题与陌生题攻击，不再继续无证据扩写。

## 当前已完成

- 408 Course Atlas、四个 Subject Atlas 与 internal Bridge Atlas 已改为 Markdown Canonical Map；旧 `408_Course_Atlas.tex` / PDF 降为扩展排版 Source，不再拥有地图语义；
- 408 Canonical Ownership 边界：Foundation 不伪装 Topic，Bridge 使用两道 Gate，Cross-Subject 收敛为 3 Core + 1 Candidate Core；
- 数据结构已重切为 Atlas Foundation + 12 Topic + 3 internal Bridge + 1 Integration；计组、OS、网络的 internal Bridge/Integration 骨架已补齐；
- 学习、错题、规则验证、手册导入、周复盘和发布的更新协议；
- 仓库维护脚本已明确拆分：`check` 只拦截机器可确定的硬错误，`audit` 只报告维护债务；`publish` 只发布 Topic / Bridge / Integration 的 Canonical `.tex`，`publish-view` 只发布 Atlas `assets/` 下的派生视觉海报；关键状态、Atlas/Depth 分流与发布边界均有回归测试。
- 数学一 Course Atlas、Cross-Subject Core Bridge Atlas、Integration Layer，以及 Extension / Anti-Bridge 边界规则。
- 高数旧库 Source Routing 表、12 Topic + 5 internal Bridge + H-I01 骨架，并完成 Jacobian/Hessian 等跨学科 Owner 上移。
- 概率统计 Subject Atlas 已明确以 README 作为 Canonical Atlas 候选，当前待人工确认；八个 Topic 仍是 Source 工作稿，后续逐册迁入 Canonical LaTeX。
- 线性代数 Subject Atlas 继续作为 Markdown Canonical Map；Topic01–06 已完成两轮 Source Diff / Model Diff 并全部重新发布。第二轮完整审阅归档旧稿约 9,000 行：补入子空间和/交、determinant 合法计算边界、rank-one 与乘积 rank 取等、同解/包含的拼接 rank 判据、零化多项式与抽象表示对角化、可交换子空间结构、配方法失败分支与二次型零点分类；SVD/伪逆、Sherman–Morrison/Woodbury、Kronecker/Sylvester/Lyapunov、Courant–Fischer 等保留为 Extension / Source。线性代数 Rules 已建立 21 条待验证规则与 5 条已否定规则。
- 计算机网络 Atlas/八个 Topic 的旧 README 工作稿已明确降为 Source 待迁移；NET-B01–B04 internal Bridge 与 NET-I01 Integration 骨架保留。
- 计算机组成原理 Atlas/Topic 的旧 README/Markdown 工作稿已明确降为 Source 待迁移；旧 `C × ISA × CPU` 已拆为 CO-B01/CO-B02 internal Bridge 与 CO-I01《一条指令的一生》Integration。

## 下一步候选

1. 用考研真题/陌生题攻击线性代数 21 条待验证 Rules，重点先测 determinant 路由、齐次/非齐次同解、重根可对角化、三阶实对称速解与二次型方法选择；根据真实表现晋升、收窄或否定 Rule。
2. 做线性代数六册跨册验收，重点攻击 Topic02→03→04 的“映射—自由度—逆像”交接，以及 Topic05→06 的“相似谱—合同惯性”边界；只有真题暴露真实模型缺口才继续改 Canonical。
3. 逐册审查概率统计 Topic，优先确认“随机世界 / 观察函数 / 信息操作”是否作为长期一级术语；
4. 从数据结构 DS01《线性关系与存储表示》开始 Source Diff，并直接生成 Canonical LaTeX Handbook package；
5. 从计组 CO03 开始把旧 README Source 迁入 `.tex`，随后建设 CO-B01 与 CO-I01，优先攻击“ISA semantic -> datapath -> timing -> commit”；
6. 从 OS Atlas Foundation + OS01 开始纳管旧 LaTeX 手册，再验证 OS-B01 Wait/Block/Wakeup；
7. 从网络 NET04/NET05 开始把旧 README Source 迁入 `.tex`，再验证 NET-B02 routing/forwarding 的 Owner 边界；
8. 开始高等数学第一轮 Topic Handbook 重构，从 Topic01《函数对象、表示与结构》做 Source Diff。

## 待人工决定

- 线性代数、概率统计的 Atlas 地图直接在 Canonical README 中人工确认；只有 Topic / Bridge / Integration 的深度机制正文迁入 Canonical `.tex`；
- 计组、网络旧 README/Markdown 仅作为 Source，不再需要先决定“是否把 README 采用为 Handbook”，而是直接在 Source Diff 中决定哪些内容进入新 LaTeX Owner；
- 新建目录、Landing Page 或 PDF 本身都不作为认知成熟证据；
- 当前 4 份 Atlas 根级旧 `.tex`（408 Course、线代 Subject、OS Internal Bridge、408 Cross-Subject Bridge）已不再是 Owner。后续真实需要视觉图时，再决定将有价值部分重做为 `assets/*_Poster.tex`，否则保持 legacy Source。

## 当前阻塞

- 考研仓库当前无阻塞：Handbook 发布已由 `cognitive_system.py publish` 安全入口隔离。
- 上层 `common/scripts/compile_tex.py` 仍是 common 级共享工具，缺少考研项目的 Canonical / scope preflight；当前 DevSpace2 workspace 不允许修改该上层路径。该债务不阻塞考研项目，但后续获得上层 workspace 时应修复共享发布路由，避免其他项目直接调用时发生跨项目输出。
