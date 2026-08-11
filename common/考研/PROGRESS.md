# 项目进度

> 本文件由 `python3 00_system/cognitive_system.py progress --write` 生成，请勿手工修改。

## 当前焦点

- **已完成**：考研数学一三门核心主干手册 (高等数学 v2、线性代数 v2、概率论与数理统计 v2) 的图表拓扑重构、出版级 5 列【概念边界】长表格升级与 100% 编译发布。
- **当前阶段**：Handbook 物理契约已按解释责任重切：`Atlas = Canonical Markdown README`；`Topic / Bridge / Integration = README Landing + Canonical .tex -> safe publish -> PDF`。Atlas 不再为了格式统一重复维护 `.tex` 正文；旧 Atlas LaTeX/PDF 只作为 Source / 旧视觉视图。深度 Handbook 仍通过 `cognitive_system.py publish` 安全发布。

## 当前已完成

- 408 Course Atlas、四个 Subject Atlas 与 internal Bridge Atlas 已改为 Markdown Canonical Map；旧 `408_Course_Atlas.tex` / PDF 降为扩展排版 Source，不再拥有地图语义；
- 408 Canonical Ownership 边界：Foundation 不伪装 Topic，Bridge 使用两道 Gate，Cross-Subject 收敛为 3 Core + 1 Candidate Core；
- 数据结构已重切为 Atlas Foundation + 12 Topic + 3 internal Bridge + 1 Integration；计组、OS、网络的 internal Bridge/Integration 骨架已补齐；
- 学习、错题、规则验证、手册导入、周复盘和发布的更新协议；
- 仓库维护脚本已明确拆分：`check` 只拦截机器可确定的硬错误，`audit` 只报告维护债务；`publish` 只发布 Topic / Bridge / Integration 的 Canonical `.tex`，`publish-view` 只发布 Atlas `assets/` 下的派生视觉海报；关键状态、Atlas/Depth 分流与发布边界均有回归测试。
- 数学一 Course Atlas、Cross-Subject Core Bridge Atlas、Integration Layer，以及 Extension / Anti-Bridge 边界规则。
- 高数旧库 Source Routing 表、12 Topic + 5 internal Bridge + H-I01 骨架，并完成 Jacobian/Hessian 等跨学科 Owner 上移。
- 概率统计 Subject Atlas 已明确以 README 作为 Canonical Atlas 候选，当前待人工确认；八个 Topic 仍是 Source 工作稿，后续逐册迁入 Canonical LaTeX。
- 线性代数 Subject Atlas 已回归 Markdown Canonical Map，当前待人工确认；上一轮 `线性代数_Subject_Atlas.tex` / PDF 降为扩展排版 Source。Topic01《向量空间：生成、基与坐标》仍是有效 Canonical LaTeX Topic 并已发布；Topic02–06 继续逐册迁移。
- 计算机网络 Atlas/八个 Topic 的旧 README 工作稿已明确降为 Source 待迁移；NET-B01–B04 internal Bridge 与 NET-I01 Integration 骨架保留。
- 计算机组成原理 Atlas/Topic 的旧 README/Markdown 工作稿已明确降为 Source 待迁移；旧 `C × ISA × CPU` 已拆为 CO-B01/CO-B02 internal Bridge 与 CO-I01《一条指令的一生》Integration。

## 下一步候选

1. 继续线性代数逐册 Model Diff：进入 Topic02《线性映射、矩阵与行列式》，重点验证“映射对象 ≠ 矩阵表示”、行列式是否只作为方阵映射的结构量，以及与 Topic03 rank / Topic04 方程组的边界；
2. 逐册审查概率统计 Topic，优先确认“随机世界 / 观察函数 / 信息操作”是否作为长期一级术语；
3. 用陌生题攻击数学一待验证 Rules，并检查 Topic 的调用协议是否真正能生成起手；
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

## 状态汇总

| 状态 | 数量 |
|---|---:|
| Candidate | 2 |
| Handbook Source 待迁移 | 33 |
| 工作稿 | 5 |
| 已发布 | 1 |
| 已采用 | 14 |
| 待人工确认 | 2 |
| 旧发布物待纳管 | 6 |
| 框架/目录已建立 | 76 |

## 资产明细

| 范围 | 资产 | 状态 |
|---|---|---|
| 数学一 / 高等数学 | [高等数学旧库迁移与重构规划](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/00_%E8%BF%81%E7%A7%BB%E4%B8%8E%E9%87%8D%E6%9E%84%E8%A7%84%E5%88%92.md) | 架构与 Source Routing 已确认，正文待逐册重构 |
| 数学一 / 高等数学 | [函数对象、表示与结构](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/01_%E5%87%BD%E6%95%B0%E5%AF%B9%E8%B1%A1_%E8%A1%A8%E7%A4%BA%E4%B8%8E%E7%BB%93%E6%9E%84/README.md) | Markdown 工作稿待迁入 LaTeX；已完成第一轮 Source Diff，待正文迁入 Canonical LaTeX 后再人工确认 |
| 数学一 / 高等数学 | [极限与连续：邻域、尺度与存在性](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/02_%E6%9E%81%E9%99%90%E4%B8%8E%E8%BF%9E%E7%BB%AD_%E9%82%BB%E5%9F%9F%E5%B0%BA%E5%BA%A6%E4%B8%8E%E5%AD%98%E5%9C%A8%E6%80%A7/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [一元局部模型：导数、微分与 Taylor](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/03_%E4%B8%80%E5%85%83%E5%B1%80%E9%83%A8%E6%A8%A1%E5%9E%8B_%E5%AF%BC%E6%95%B0%E5%BE%AE%E5%88%86%E4%B8%8ETaylor/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [局部到整体：中值定理与函数形状](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/04_%E5%B1%80%E9%83%A8%E5%88%B0%E6%95%B4%E4%BD%93_%E4%B8%AD%E5%80%BC%E5%AE%9A%E7%90%86%E4%B8%8E%E5%87%BD%E6%95%B0%E5%BD%A2%E7%8A%B6/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [一元累积：原函数、定积分与反常积分](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/05_%E4%B8%80%E5%85%83%E7%B4%AF%E7%A7%AF_%E5%8E%9F%E5%87%BD%E6%95%B0%E5%AE%9A%E7%A7%AF%E5%88%86%E4%B8%8E%E5%8F%8D%E5%B8%B8%E7%A7%AF%E5%88%86/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [空间对象与方向表示](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/06_%E7%A9%BA%E9%97%B4%E5%AF%B9%E8%B1%A1%E4%B8%8E%E6%96%B9%E5%90%91%E8%A1%A8%E7%A4%BA/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [多元局部模型：可微、梯度、隐函数与极值](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/07_%E5%A4%9A%E5%85%83%E5%B1%80%E9%83%A8%E6%A8%A1%E5%9E%8B_%E5%8F%AF%E5%BE%AE%E6%A2%AF%E5%BA%A6%E9%9A%90%E5%87%BD%E6%95%B0%E4%B8%8E%E6%9E%81%E5%80%BC/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [高维累积：区域、坐标与 Jacobian](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/08_%E9%AB%98%E7%BB%B4%E7%B4%AF%E7%A7%AF_%E5%8C%BA%E5%9F%9F%E5%9D%90%E6%A0%87%E4%B8%8EJacobian/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [定向积分与向量场](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/09_%E5%AE%9A%E5%90%91%E7%A7%AF%E5%88%86%E4%B8%8E%E5%90%91%E9%87%8F%E5%9C%BA/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [数项级数：尾部与敛散](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/10_%E6%95%B0%E9%A1%B9%E7%BA%A7%E6%95%B0_%E5%B0%BE%E9%83%A8%E4%B8%8E%E6%95%9B%E6%95%A3/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [函数展开：幂级数、Taylor 与 Fourier](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/11_%E5%87%BD%E6%95%B0%E5%B1%95%E5%BC%80_%E5%B9%82%E7%BA%A7%E6%95%B0Taylor%E4%B8%8EFourier/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [常微分方程：局部规律与整体轨迹](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/12_%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B_%E5%B1%80%E9%83%A8%E8%A7%84%E5%BE%8B%E4%B8%8E%E6%95%B4%E4%BD%93%E8%BD%A8%E8%BF%B9/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [H-B01｜函数结构在运算中的传播](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B01_%E5%87%BD%E6%95%B0%E7%BB%93%E6%9E%84%E5%9C%A8%E8%BF%90%E7%AE%97%E4%B8%AD%E7%9A%84%E4%BC%A0%E6%92%AD/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [H-B02｜局部模型与区间定理：中值点、余项与误差控制](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B02_%E5%B1%80%E9%83%A8%E6%A8%A1%E5%9E%8B%E4%B8%8E%E5%8C%BA%E9%97%B4%E5%AE%9A%E7%90%86_%E4%B8%AD%E5%80%BC%E7%82%B9%E4%BD%99%E9%A1%B9%E4%B8%8E%E8%AF%AF%E5%B7%AE%E6%8E%A7%E5%88%B6/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [H-B03｜微分与累积：基本定理及正则性边界](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B03_%E5%BE%AE%E5%88%86%E4%B8%8E%E7%B4%AF%E7%A7%AF_%E5%9F%BA%E6%9C%AC%E5%AE%9A%E7%90%86%E5%8F%8A%E6%AD%A3%E5%88%99%E6%80%A7%E8%BE%B9%E7%95%8C/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [H-B04｜连续无限累积与离散无限累积](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B04_%E8%BF%9E%E7%BB%AD%E6%97%A0%E9%99%90%E7%B4%AF%E7%A7%AF%E4%B8%8E%E7%A6%BB%E6%95%A3%E6%97%A0%E9%99%90%E7%B4%AF%E7%A7%AF/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [H-B05｜有限 Taylor 模型与无限 Taylor 表示](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B05_%E6%9C%89%E9%99%90Taylor%E6%A8%A1%E5%9E%8B%E4%B8%8E%E6%97%A0%E9%99%90Taylor%E8%A1%A8%E7%A4%BA/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [高等数学 Internal Bridge Atlas](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 数学一 / 高等数学 | [H-I01｜微积分建模：从局部微元到整体量](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/H-I01_%E5%BE%AE%E7%A7%AF%E5%88%86%E5%BB%BA%E6%A8%A1_%E4%BB%8E%E5%B1%80%E9%83%A8%E5%BE%AE%E5%85%83%E5%88%B0%E6%95%B4%E4%BD%93%E9%87%8F/README.md) | 目录已建立，正文未建 |
| 数学一 / 高等数学 | [高等数学 Integration Layer](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，正文未建 |
| 数学一 / 高等数学 | [高等数学 Subject Atlas](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md) | 已采用；README 是 Canonical Subject Atlas，Topic / Bridge / Integration 按当前路由逐册重构 |
| 数学一 / 线性代数 | [向量空间：生成、基与坐标](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/01_%E5%90%91%E9%87%8F%E7%A9%BA%E9%97%B4_%E7%94%9F%E6%88%90%E5%9F%BA%E4%B8%8E%E5%9D%90%E6%A0%87/README.md) | 待人工确认；Canonical LaTeX 第一版正文已建立，PDF 已生成 |
| 数学一 / 线性代数 | [线性映射、矩阵与行列式](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/02_%E7%BA%BF%E6%80%A7%E6%98%A0%E5%B0%84_%E7%9F%A9%E9%98%B5%E4%B8%8E%E8%A1%8C%E5%88%97%E5%BC%8F/README.md) | Markdown 工作稿待迁入 LaTeX；已完成映射表示、复合、可逆与行列式机制的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 线性代数 | [秩、基本子空间与等价](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/03_%E7%A7%A9_%E5%9F%BA%E6%9C%AC%E5%AD%90%E7%A9%BA%E9%97%B4%E4%B8%8E%E7%AD%89%E4%BB%B7/README.md) | Markdown 工作稿待迁入 LaTeX；已完成自由度分解、四大基本子空间与等价机制的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 线性代数 | [线性方程组：可达性与解空间](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/04_%E7%BA%BF%E6%80%A7%E6%96%B9%E7%A8%8B%E7%BB%84_%E5%8F%AF%E8%BE%BE%E6%80%A7%E4%B8%8E%E8%A7%A3%E7%A9%BA%E9%97%B4/README.md) | Markdown 工作稿待迁入 LaTeX；已完成逆像模型、解集结构与同解边界的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 线性代数 | [特征结构：相似与对角化](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/05_%E7%89%B9%E5%BE%81%E7%BB%93%E6%9E%84_%E7%9B%B8%E4%BC%BC%E4%B8%8E%E5%AF%B9%E8%A7%92%E5%8C%96/README.md) | Markdown 工作稿待迁入 LaTeX；已完成自然方向、相似、对角化、实对称谱结构与可交换边界的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 线性代数 | [二次型：合同、惯性与正定](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/06_%E4%BA%8C%E6%AC%A1%E5%9E%8B_%E5%90%88%E5%90%8C%E6%83%AF%E6%80%A7%E4%B8%8E%E6%AD%A3%E5%AE%9A/README.md) | Markdown 工作稿待迁入 LaTeX；已完成去耦合、合同、惯性与正定机制的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 线性代数 | [线性代数 Subject Atlas：空间、映射、表示与不变量](线性代数%20Subject%20Atlas：空间、映射、表示与不变量.md) | 已采用；README 是 Canonical Subject Atlas |
| 数学一 / 概率统计 | [随机世界：事件与概率](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/01_%E9%9A%8F%E6%9C%BA%E4%B8%96%E7%95%8C_%E4%BA%8B%E4%BB%B6%E4%B8%8E%E6%A6%82%E7%8E%87/README.md) | Markdown 工作稿待迁入 LaTeX；已完成母模型、边界与调用协议的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [条件概率、独立性与 Bayes：信息怎样重分配概率](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/02_%E6%9D%A1%E4%BB%B6%E6%A6%82%E7%8E%87_%E7%8B%AC%E7%AB%8B%E6%80%A7%E4%B8%8EBayes/README.md) | Markdown 工作稿待迁入 LaTeX；已完成信息更新母模型与主要边界的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [随机变量与一维分布：把随机世界映射到数轴](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/03_%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E4%B8%8E%E4%B8%80%E7%BB%B4%E5%88%86%E5%B8%83/README.md) | Markdown 工作稿待迁入 LaTeX；已完成观察函数与分布表示母模型的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [联合分布、条件分布与变换：概率质量怎样重组](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/04_%E8%81%94%E5%90%88%E5%88%86%E5%B8%83_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B8%83%E4%B8%8E%E5%8F%98%E6%8D%A2/README.md) | Markdown 工作稿待迁入 LaTeX；已完成支撑几何、信息操作与变量变换模型的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [数字特征与依赖摘要：怎样压缩分布而不忘记损失](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/05_%E6%95%B0%E5%AD%97%E7%89%B9%E5%BE%81%E4%B8%8E%E4%BE%9D%E8%B5%96%E6%91%98%E8%A6%81/README.md) | Markdown 工作稿待迁入 LaTeX；已完成分布摘要、误差分解与依赖边界的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [大数定律与中心极限定理：稳定位置与剩余波动](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/06_%E5%A4%A7%E6%95%B0%E5%AE%9A%E5%BE%8B%E4%B8%8E%E4%B8%AD%E5%BF%83%E6%9E%81%E9%99%90%E5%AE%9A%E7%90%86/README.md) | Markdown 工作稿待迁入 LaTeX；已有笔记对应文件为空，本 Source 工作稿依据 Atlas 母模型补建，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [总体、样本与抽样分布：统计量为什么仍然随机](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/07_%E6%80%BB%E4%BD%93%E6%A0%B7%E6%9C%AC%E4%B8%8E%E6%8A%BD%E6%A0%B7%E5%88%86%E5%B8%83/README.md) | Markdown 工作稿待迁入 LaTeX；已完成样本对象分层、正态样本几何与抽样分布生成链的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [参数估计与假设检验：用抽样分布校准逆向推断](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/08_%E5%8F%82%E6%95%B0%E4%BC%B0%E8%AE%A1%E4%B8%8E%E5%81%87%E8%AE%BE%E6%A3%80%E9%AA%8C/README.md) | Markdown 工作稿待迁入 LaTeX；已完成点估计、区间与检验统一校准模型的 Source 工作稿，待迁入 Canonical LaTeX 后再由使用者审查 |
| 数学一 / 概率统计 | [概率论与数理统计统一总图](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/README.md) | 待人工确认；README 是 Canonical Subject Atlas 候选，八个 Topic 仍是 Source 工作稿。考试动作另见概率统计做题规则 |
| 数学一 / 跨科 Bridge | [B00｜内积、正交与投影](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B00_%E5%86%85%E7%A7%AF%E6%AD%A3%E4%BA%A4%E4%B8%8E%E6%8A%95%E5%BD%B1/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B01｜局部线性化：微分 × 线性映射](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B01_%E5%B1%80%E9%83%A8%E7%BA%BF%E6%80%A7%E5%8C%96_%E5%BE%AE%E5%88%86%E4%B8%8E%E7%BA%BF%E6%80%A7%E6%98%A0%E5%B0%84/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B02｜Jacobian 与行列式：坐标变换 × 局部体积缩放](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B02_Jacobian%E4%B8%8E%E8%A1%8C%E5%88%97%E5%BC%8F_%E5%9D%90%E6%A0%87%E5%8F%98%E6%8D%A2%E4%B8%8E%E5%B1%80%E9%83%A8%E4%BD%93%E7%A7%AF%E7%BC%A9%E6%94%BE/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B03｜Hessian 与二次型：二阶局部形状 × 正定性](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B03_Hessian%E4%B8%8E%E4%BA%8C%E6%AC%A1%E5%9E%8B_%E4%BA%8C%E9%98%B6%E5%B1%80%E9%83%A8%E5%BD%A2%E7%8A%B6%E4%B8%8E%E6%AD%A3%E5%AE%9A%E6%80%A7/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B04｜梯度、正交与 Lagrange：约束极值 × 子空间几何](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B04_%E6%A2%AF%E5%BA%A6%E6%AD%A3%E4%BA%A4%E4%B8%8ELagrange_%E7%BA%A6%E6%9D%9F%E6%9E%81%E5%80%BC%E4%B8%8E%E5%AD%90%E7%A9%BA%E9%97%B4%E5%87%A0%E4%BD%95/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B05｜线性方程与线性微分方程：一点 + Kernel](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B05_%E7%BA%BF%E6%80%A7%E6%96%B9%E7%A8%8B%E4%B8%8E%E7%BA%BF%E6%80%A7%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B_%E4%B8%80%E7%82%B9%E5%8A%A0Kernel/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B06A｜PDF 与 CDF：局部概率密度 × 累积](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B06A_PDF%E4%B8%8ECDF_%E5%B1%80%E9%83%A8%E6%A6%82%E7%8E%87%E5%AF%86%E5%BA%A6%E4%B8%8E%E7%B4%AF%E7%A7%AF/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B06B｜期望、联合概率与边缘化：概率的积分语言](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B06B_%E6%9C%9F%E6%9C%9B%E8%81%94%E5%90%88%E6%A6%82%E7%8E%87%E4%B8%8E%E8%BE%B9%E7%BC%98%E5%8C%96_%E6%A6%82%E7%8E%87%E7%9A%84%E7%A7%AF%E5%88%86%E8%AF%AD%E8%A8%80/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B07｜随机变量变换与 Jacobian：概率质量守恒](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B07_%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E5%8F%98%E6%8D%A2%E4%B8%8EJacobian_%E6%A6%82%E7%8E%87%E8%B4%A8%E9%87%8F%E5%AE%88%E6%81%92/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [B08｜Fourier 与正交基：函数表示 × 正交投影](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B08_Fourier%E4%B8%8E%E6%AD%A3%E4%BA%A4%E5%9F%BA_%E5%87%BD%E6%95%B0%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%AD%A3%E4%BA%A4%E6%8A%95%E5%BD%B1/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Bridge | [数学一 Core Bridge Atlas](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/README.md) | 已采用；README 是 Canonical Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 数学一 / 跨科 Integration | [I01｜二维正态分布：三科汇流验收](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/I01_%E4%BA%8C%E7%BB%B4%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83_%E4%B8%89%E7%A7%91%E6%B1%87%E6%B5%81%E9%AA%8C%E6%94%B6/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Integration | [I02｜二维随机变量线性变换](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/I02_%E4%BA%8C%E7%BB%B4%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E7%BA%BF%E6%80%A7%E5%8F%98%E6%8D%A2/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Integration | [I03｜线性常微分方程组](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/I03_%E7%BA%BF%E6%80%A7%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B%E7%BB%84/README.md) | 目录已建立，正文未建；部分内容属于 Extension 验收 |
| 数学一 / 跨科 Integration | [数学一 Integration Layer](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，Integration 正文未建 |
| 数学一 / 数学 Rules | [数学一 学科做题规则](10_%E6%95%B0%E5%AD%A6%E4%B8%80/90_%E5%AD%A6%E7%A7%91%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 目录已建立，规则正在积累 |
| 数学一 | [数学一认知体系总架构](10_%E6%95%B0%E5%AD%A6%E4%B8%80/README.md) | 已采用；README 是 Canonical Course / Exam Atlas，Subject Topic / Bridge / Integration 正文分阶段建设中 |
| 408 / 总图 | [408 学科架构：Canonical Topology 设计依据](30_408/00_%E7%BB%9F%E4%B8%80%E6%80%BB%E5%9B%BE/408%20%E5%AD%A6%E7%A7%91%E6%9E%B6%E6%9E%84.md) | 框架已采用；本文件记录为什么这样切，不承担日常导航。日常入口见 408 Course Atlas |
| 408 / 数据结构 | [数据结构学科总图](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/00_%E5%AD%A6%E7%A7%91%E6%80%BB%E5%9B%BE/README.md) | Source；Atlas Foundation / Deep Map 旧工作稿，待与 Canonical Data Structure Subject Atlas README 做 Source Diff；不再迁成第二份 Atlas LaTeX |
| 408 / 数据结构 | [DS01｜线性关系与存储表示](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/01_%E7%BA%BF%E6%80%A7%E5%85%B3%E7%B3%BB%E4%B8%8E%E5%AD%98%E5%82%A8%E8%A1%A8%E7%A4%BA/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS02｜栈、队列与受限访问](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/02_%E6%A0%88%E9%98%9F%E5%88%97%E4%B8%8E%E5%8F%97%E9%99%90%E8%AE%BF%E9%97%AE/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS03｜串与模式匹配](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/03_%E4%B8%B2%E4%B8%8E%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS04｜树与二叉树](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/04_%E6%A0%91%E4%B8%8E%E4%BA%8C%E5%8F%89%E6%A0%91/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS05｜Heap 与优先队列](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/05_Heap%E4%B8%8E%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS06｜Union-Find 与集合划分](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/06_UnionFind%E4%B8%8E%E9%9B%86%E5%90%88%E5%88%92%E5%88%86/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS07｜图的表示与遍历](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/07_%E5%9B%BE%E7%9A%84%E8%A1%A8%E7%A4%BA%E4%B8%8E%E9%81%8D%E5%8E%86/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS08｜图上的结构算法](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/08_%E5%9B%BE%E4%B8%8A%E7%9A%84%E7%BB%93%E6%9E%84%E7%AE%97%E6%B3%95/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS09｜查找与有序索引](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/09_%E6%9F%A5%E6%89%BE%E4%B8%8E%E6%9C%89%E5%BA%8F%E7%B4%A2%E5%BC%95/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS10｜Hash 与直接定位](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/10_Hash%E4%B8%8E%E7%9B%B4%E6%8E%A5%E5%AE%9A%E4%BD%8D/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS11｜内部排序](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/11_%E5%86%85%E9%83%A8%E6%8E%92%E5%BA%8F/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS12｜外部排序](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/12_%E5%A4%96%E9%83%A8%E6%8E%92%E5%BA%8F/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS-B01｜Frontier Traversal](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/DS-B01_FrontierTraversal/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS-B02｜Index Strategy × Workload](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/DS-B02_IndexStrategy%E4%B8%8EWorkload/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [DS-B03｜Heap / Union-Find × Graph Algorithm](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/DS-B03_%E8%BE%85%E5%8A%A9%E7%BB%93%E6%9E%84%E4%B8%8E%E5%9B%BE%E7%AE%97%E6%B3%95/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [数据结构 Internal Bridge Atlas](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 408 / 数据结构 | [DS-I01｜从 Workload 到数据结构选择](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/DS-I01_%E4%BB%8EWorkload%E5%88%B0%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E9%80%89%E6%8B%A9/README.md) | 目录已建立，正文未建 |
| 408 / 数据结构 | [数据结构 Integration Layer](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，正文未建 |
| 408 / 数据结构 | [数据结构做题规则](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / 数据结构 | [数据结构 Subject Atlas](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/README.md) | 已采用；README 是 Canonical Subject Atlas，Atlas Foundation、12 个 Topic、3 个 internal Bridge、1 个 Integration 已锁定，下游深度 Handbook 按册建设 |
| 408 / 计组 | [计算机组成原理学科总图：ISA 语义如何成为硬件时序](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/00_%E5%AD%A6%E7%A7%91%E6%80%BB%E5%9B%BE/README.md) | Source；Atlas Deep Map 工作稿，待与根目录 Canonical Subject Atlas README 做 Source Diff |
| 408 / 计组 | [数据表示与运算：有限位宽怎样保持可解释](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/10_%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%A4%BA%E4%B8%8E%E8%BF%90%E7%AE%97/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [ISA 与机器级程序：软件意图怎样成为可执行契约](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/20_ISA%E4%B8%8E%E6%9C%BA%E5%99%A8%E7%BA%A7%E7%A8%8B%E5%BA%8F/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [CPU 数据通路与控制：把指令语义编排成状态转移](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/30_CPU%E6%95%B0%E6%8D%AE%E9%80%9A%E8%B7%AF%E4%B8%8E%E6%8E%A7%E5%88%B6/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [流水线与指令级并行：重叠执行怎样保持顺序语义](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/40_%E6%B5%81%E6%B0%B4%E7%BA%BF%E4%B8%8E%E6%8C%87%E4%BB%A4%E7%BA%A7%E5%B9%B6%E8%A1%8C/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [主存与存储硬件：地址怎样落到物理介质](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/50_%E4%B8%BB%E5%AD%98%E4%B8%8E%E5%AD%98%E5%82%A8%E7%A1%AC%E4%BB%B6/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [Cache 与存储层次：怎样维护一个正确的高速副本](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/60_Cache%E4%B8%8E%E5%AD%98%E5%82%A8%E5%B1%82%E6%AC%A1/Cache%20%E4%B8%8E%E5%AD%98%E5%82%A8%E5%B1%82%E6%AC%A1%EF%BC%9A%E6%80%8E%E6%A0%B7%E7%BB%B4%E6%8A%A4%E4%B8%80%E4%B8%AA%E6%AD%A3%E7%A1%AE%E7%9A%84%E9%AB%98%E9%80%9F%E5%89%AF%E6%9C%AC.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [地址翻译与虚拟存储硬件：VA 怎样成为可访问的 PA](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/70_%E5%9C%B0%E5%9D%80%E7%BF%BB%E8%AF%91%E4%B8%8E%E8%99%9A%E6%8B%9F%E5%AD%98%E5%82%A8%E7%A1%AC%E4%BB%B6/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [总线与 I/O 硬件：同步处理器怎样与异步设备合作](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/80_%E6%80%BB%E7%BA%BF%E4%B8%8EIO%E7%A1%AC%E4%BB%B6/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 计组 | [CO-B01｜ISA Semantic × Datapath](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/CO-B01_ISA%E8%AF%AD%E4%B9%89%E4%B8%8E%E6%95%B0%E6%8D%AE%E9%80%9A%E8%B7%AF/README.md) | 目录已建立，正文未建 |
| 408 / 计组 | [CO-B02｜Address Translation × Cache Access](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/CO-B02_%E5%9C%B0%E5%9D%80%E7%BF%BB%E8%AF%91%E4%B8%8ECache%E8%AE%BF%E9%97%AE/README.md) | 目录已建立，正文未建 |
| 408 / 计组 | [计算机组成原理 Internal Bridge Atlas](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 408 / 计组 | [计组科内桥梁与综合：从 C 语句到一次精确提交](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81%E4%B8%8E%E7%BB%BC%E5%90%88/%E8%AE%A1%E7%BB%84%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81%E4%B8%8E%E7%BB%BC%E5%90%88%EF%BC%9A%E4%BB%8E%20C%20%E8%AF%AD%E5%8F%A5%E5%88%B0%E4%B8%80%E6%AC%A1%E7%B2%BE%E7%A1%AE%E6%8F%90%E4%BA%A4.md) | legacy-unregistered Source；不再作为 Canonical Bridge / Integration Owner |
| 408 / 计组 | [CO-I01｜一条指令的一生](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/86_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/CO-I01_%E4%B8%80%E6%9D%A1%E6%8C%87%E4%BB%A4%E7%9A%84%E4%B8%80%E7%94%9F/README.md) | 目录已建立，正文未建 |
| 408 / 计组 | [计算机组成原理 Integration Layer](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/86_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，正文未建 |
| 408 / 计组 | [计组做题规则与性能工具箱](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / 计组 | [计算机组成原理 Subject Atlas](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/README.md) | 已采用；README 是 Canonical Subject Atlas，八个 Topic 的Markdown 工作稿仍是 Source，深度正文按册迁入 Canonical LaTeX |
| 408 / OS | [操作系统学科总图](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/00_%E5%AD%A6%E7%A7%91%E6%80%BB%E5%9B%BE/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-00 操作系统基础与程序运行环境](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/05_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%9F%BA%E7%A1%80%E4%B8%8E%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83/README.md) | Canonical LaTeX 第一版正文已建立并已有 Published PDF；待真题与已有笔记继续校验 |
| 408 / OS | [进程、线程、调度与控制权](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/10_%E8%BF%9B%E7%A8%8B%E7%BA%BF%E7%A8%8B%E8%B0%83%E5%BA%A6%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%9D%83/README.md) | 目录已建立，已有发布物待纳管 |
| 408 / OS | [并发、同步与死锁](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/20_%E5%B9%B6%E5%8F%91%E5%90%8C%E6%AD%A5%E4%B8%8E%E6%AD%BB%E9%94%81/README.md) | 目录已建立，已有发布物待纳管 |
| 408 / OS | [虚拟内存与页生命周期](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/30_%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98%E4%B8%8E%E9%A1%B5%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F/README.md) | 目录已建立，已有发布物待纳管 |
| 408 / OS | [I/O 请求、等待与完成](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/40_IO%E8%AF%B7%E6%B1%82%E7%AD%89%E5%BE%85%E4%B8%8E%E5%AE%8C%E6%88%90/README.md) | 目录已建立，已有发布物待纳管 |
| 408 / OS | [文件系统](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/50_%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/README.md) | 目录已建立，已有发布物待纳管 |
| 408 / OS | [OS-B01｜Wait / Block / Wakeup](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B01_WaitBlockWakeup/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-B02｜Process × Virtual Memory](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B02_Process%E4%B8%8EVirtualMemory/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-B03｜Process × File Reference](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B03_Process%E4%B8%8EFileReference/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-B04｜VM × File × I/O](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B04_VMFileIO/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS Internal Bridge Atlas](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 按当前 Owner 边界逐册重构 |
| 408 / OS | [OS-I01｜一次 Blocking `read()`](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/70_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/OS-I01_BlockingRead/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-I02｜`fork()` + COW + Resource Reference](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/70_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/OS-I02_ForkCOW%E4%B8%8E%E8%B5%84%E6%BA%90%E5%BC%95%E7%94%A8/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS Integration Layer](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/70_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，正文待重构 |
| 408 / OS | [操作系统做题规则](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / OS | [操作系统 Subject Atlas](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/README.md) | 已采用；README 是 Canonical Subject Atlas，五个 Core Topic 的历史 LaTeX/发布物待逐册纳管 |
| 408 / 网络 | [计算机网络统一总图：分布式状态、作用域与报文的一生](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/00_%E7%BD%91%E7%BB%9C%E7%BB%9F%E4%B8%80%E6%80%BB%E5%9B%BE/README.md) | Source；Atlas Deep Map 工作稿，待与根目录 Canonical Subject Atlas README 做 Source Diff |
| 408 / 网络 | [通信基础与网络性能：把信息送过有限信道](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/01_%E9%80%9A%E4%BF%A1%E5%9F%BA%E7%A1%80%E4%B8%8E%E7%BD%91%E7%BB%9C%E6%80%A7%E8%83%BD/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [单跳交付：帧、MAC、局域网与交换机](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/02_%E5%8D%95%E8%B7%B3%E4%BA%A4%E4%BB%98_%E5%B8%A7_MAC_%E5%B1%80%E5%9F%9F%E7%BD%91%E4%B8%8E%E4%BA%A4%E6%8D%A2%E6%9C%BA/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [可靠传输：用有限状态驯服丢失、损坏与乱序](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/03_%E5%8F%AF%E9%9D%A0%E4%BC%A0%E8%BE%93_%E5%BA%8F%E5%8F%B7_ACK_%E5%AE%9A%E6%97%B6%E5%99%A8%E4%B8%8E%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [IP 地址、子网与分组转发：把全局目的压缩成逐跳动作](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/04_IP%E5%9C%B0%E5%9D%80_%E5%AD%90%E7%BD%91%E4%B8%8E%E5%88%86%E7%BB%84%E8%BD%AC%E5%8F%91/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [路由：不完整知识怎样收敛为可用转发状态](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/05_%E8%B7%AF%E7%94%B1_%E5%88%86%E5%B8%83%E5%BC%8F%E7%9F%A5%E8%AF%86%E4%B8%8E%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [传输层：从 host 交付到 process 会话](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/06_%E4%BC%A0%E8%BE%93%E5%B1%82_%E7%AB%AF%E7%82%B9_UDP%E4%B8%8ETCP%E7%8A%B6%E6%80%81%E6%9C%BA/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [拥塞控制：在不知道路径容量时闭环试探](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/07_%E6%8B%A5%E5%A1%9E_%E5%85%B1%E4%BA%AB%E8%B5%84%E6%BA%90%E4%B8%8E%E5%8F%8D%E9%A6%88%E6%8E%A7%E5%88%B6/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [应用层：把通信能力组织成可发现、可解释的服务](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/08_%E5%BA%94%E7%94%A8%E5%B1%82_DNS_HTTP%E4%B8%8E%E6%9C%8D%E5%8A%A1%E8%AF%AD%E4%B9%89/README.md) | Markdown 工作稿待迁入 LaTeX；Canonical LaTeX 正文未建 |
| 408 / 网络 | [NET-B01｜IP Forwarding × Single-Hop Delivery](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B01_IPForwarding%E4%B8%8ESingleHop/README.md) | 目录已建立，正文未建 |
| 408 / 网络 | [NET-B02｜Routing × Forwarding](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B02_Routing%E4%B8%8EForwarding/README.md) | 目录已建立，正文未建 |
| 408 / 网络 | [NET-B03｜Reliable Transfer × TCP](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B03_ReliableTransfer%E4%B8%8ETCP/README.md) | 目录已建立，正文未建 |
| 408 / 网络 | [NET-B04｜Flow Control × Congestion Control](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B04_FlowControl%E4%B8%8ECongestionControl/README.md) | 目录已建立，正文未建 |
| 408 / 网络 | [计算机网络 Internal Bridge Atlas](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 408 / 网络 | [NET-I01｜一个网络请求的一生：从域名到网页返回](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/NET-I01_%E4%B8%80%E4%B8%AA%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82%E7%9A%84%E4%B8%80%E7%94%9F/README.md) | 目录已建立；已有综合工作稿可作为 Source，正文待按新 Ownership 复核 |
| 408 / 网络 | [计算机网络 Integration Layer](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；NET-I01 已建立目录，已有综合 Source 待按新 Bridge 边界复核，Canonical LaTeX 正文未建 |
| 408 / 网络 | [计算机网络做题规则](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / 网络 | [计算机网络 Subject Atlas](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/README.md) | 已采用；README 是 Canonical Subject Atlas，八个 Topic 的Markdown 工作稿仍是 Source，深度正文按册迁入 Canonical LaTeX |
| 408 / 跨科 Bridge | [408 Cross-Subject Bridge Atlas](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/README.md) | 已采用；README 是 Canonical Cross-Subject Bridge Atlas，3 个 Core Bridge 与 1 个 Candidate Core 按当前边界逐册建设 |
| 408 / 跨科 Bridge | [X-B01｜Privilege / Exception / System Call × OS Control](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B01_PrivilegeExceptionSystemCall%E4%B8%8EOSControl/README.md) | 目录已建立，正文未建 |
| 408 / 跨科 Bridge | [X-B02｜Hardware Address Translation × OS Virtual Memory](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B02_HardwareAddressTranslation%E4%B8%8EOSVirtualMemory/README.md) | 目录已建立，正文未建 |
| 408 / 跨科 Bridge | [X-B03｜Interrupt / DMA × OS I/O](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B03_InterruptDMA%E4%B8%8EOSIO/README.md) | 目录已建立，正文未建 |
| 408 / 跨科 Bridge | [X-B04｜Process / Socket × Transport Endpoint](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B04_ProcessSocket%E4%B8%8ETransportEndpoint/README.md) | Candidate Core；接口结构已确认，是否升级为 Core 待 408 考纲/真题覆盖证据与重复调用证据 |
| 408 / 跨科 Integration | [408 Cross-Subject Integration Layer](30_408/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；2 个核心 Integration 已建立骨架，综合发布物待按新 Ownership 纳管 |
| 408 / 跨科 Integration | [X-I01｜一次 LOAD / Memory Access 的完整慢路径](30_408/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/X-I01_LOAD%E4%B8%8EMemoryAccess%E6%85%A2%E8%B7%AF%E5%BE%84/README.md) | 目录已建立，正文未建 |
| 408 / 跨科 Integration | [X-I02｜一次 Blocking File `read()` 的完整生命周期](30_408/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/X-I02_BlockingFileRead%E5%AE%8C%E6%95%B4%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F/README.md) | 目录已建立，正文未建 |
| 408 / 408 Rules | [408 通用做题规则](30_408/90_408%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，通用入口已建立，规则尚待证据化 |
| 408 | [408 Course Atlas](30_408/README.md) | 已采用；README 是 Canonical Course Atlas，四个 Subject 与下游 Handbook 按当前拓扑继续建设 |

## 怎样更新

1. 当前工作方向变化时，修改 `CURRENT.md`；
2. 某项资产的物理文件或人工决定发生真实变化时，修改其入口顶部的 `状态：...`；
3. 运行进度生成与系统检查；
4. 不为了让数字增长而修改状态。
