# 项目进度

> 本文件由 `python3 00_system/cognitive_system.py progress --write` 生成，请勿手工修改。

## 当前焦点

- **系统阶段**：从“搭建 Handbook”转入“证据验证与跨学科 Bridge 增强”。各科的 Atlas、Topic、Bridge、Integration 和 Rules 已有稳定的 Owner；接下来只因真题、陌生题或逐项 Source Diff 暴露缺口而更新 Canonical。
- **本轮已完成**：32 个具体 Bridge 已逐册完成 v1 审阅；其中 31 个已有唯一 Canonical `.tex`，X-B04 仍保持 Candidate。Bridge 审阅台账与 X-B02 调研证据已形成可追溯记录。
- **当前最重要的验证问题**：已发布的正文不等于已采用的心智模型。高数、线代、概率、408 四科的 Candidate Rules 需要用真实题面和陌生题验证“第一动作、接口、检查、退出”是否可复原。
- **维护原则**：旧总图、旧 README 和个人 Source 仍是待核销证据；本轮只归档 review log，不删除任何知识 Source。只有逐项 Source Diff 完成且唯一 Owner 可定位后，才讨论删除旧文件。

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

- 数据结构 DS01--DS12、DS-B01--B03、DS-I01 已完成第一轮 Source Diff、代码与测试核对并发布；本批次进一步补齐 DS01 多维数组/特殊矩阵、DS04 树森林/线索树、DS07 十字链表/邻接多重表、DS09 分块/红黑/B/B+、DS11 折半插入/Shell/基数等考纲机制。下一步仍须用陌生题检验学习者能否无提示复原这些不变量，不能以静态正文和测试通过替代记忆效果证据。
- 计算机组成原理 CO01--08、CO-B01/02、CO-I01 已建立并发布；本批次补齐 CO02 编译—汇编—链接—装入生命周期、CO04 Flynn/SIMD/MIMD/多核/硬件多线程、CO07 分段/段页式，并在 Atlas 增加存储程序与性能指标入口；Rules 仍待验证。
- 操作系统已完成两处个人 Source 的逐篇 Owner Diff；OS-00 与五个 Core Topic、OS-B01--B04、OS-I01 已形成候选正文并发布，本批次在 OS-05 增补网络设备 descriptor/ownership/completion 接口；考试动作仍待验证。
- 计算机网络已按 2026 转载考纲基线完成结构覆盖补缺：Atlas Foundation、NET01/02/04/05/06/07/08 已补齐原 B/C 缺口并发布；NET-B01--B04 已重构，NET-B05（BDP×Window）与 NET-B06（MTU×Segmentation）通过 Gate、建册并发布。当前结论只到“Canonical 结构可支撑”，真题/陌生题成熟度仍待验证；X-B04 仍保持 Candidate Core。

### 跨学科 Bridge

- Bridge v1 审阅覆盖数学、数据结构、计组、OS、网络和跨科目录，共 32 个具体目录；本轮确认了接口、独立不变量、最小例子、调用时机、停止条件和 Anti-Bridge 边界。
- OS-B01--B04、NET-B01--B06、X-B01、X-B02、X-B03 已有唯一深度正文；X-B04 与 AI 跨 Area Bridge 继续保持 Candidate，不因目录存在而提前成熟化。

## 下一步候选

1. **真题 / 陌生题证据攻击**：优先验证高数、线代、概率和 408 Rules 的触发信号、第一动作、接口与退出条件；只记录可观察的题面行为，不用静态发布视图替代使用证据。
2. **408 网络题目验证**：用真题/陌生题攻击 NET01--NET08 的协议流程、LPM、RIB/FIB handoff、TCP/拥塞和应用时序；若出现缺口，再按 Source Diff 重新打开对应记录。
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
- **维护债务**：概率统计受 `STHeiti` 字体环境影响；上层 `common/scripts/compile_tex.py` 尚无考研 scope preflight；网络八册与 NET-I01 的 Published View 已同步，这些事项不阻断当前证据攻击。
- **证据债务**：大多数 Rules 只有 Source / 机制重建支持，尚缺使用者在陌生题中的重复验证；因此当前状态应读作“Canonical 候选 + Candidate Rules”，不是“全部成熟”。

## 复盘入口

- 当前日志索引：[review_log/README.md](80_evidence/review_log/README.md)
- 已完成审阅归档：[archive/review_log/README.md](80_evidence/archive/review_log/README.md)
- Bridge 审阅台账（归档）：[2026-08-12_Bridge逐册审阅台账_v1.md](80_evidence/archive/review_log/2026-08-12/2026-08-12_Bridge逐册审阅台账_v1.md)

## 状态汇总

| 状态 | 数量 |
|---|---:|
| Candidate | 3 |
| Handbook Source 待迁移 | 8 |
| 其他 | 12 |
| 工作稿 | 5 |
| 已发布 | 27 |
| 已采用 | 48 |
| 待人工确认 | 44 |
| 待验证 | 2 |
| 旧发布物待纳管 | 1 |
| 框架/目录已建立 | 17 |

## 资产明细

| 范围 | 资产 | 状态 |
|---|---|---|
| 数学一 / 高等数学 | [高等数学旧库迁移与重构规划](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/00_%E8%BF%81%E7%A7%BB%E4%B8%8E%E9%87%8D%E6%9E%84%E8%A7%84%E5%88%92.md) | 架构与 Source Routing 已确认；12 Topic、5 个内部 Bridge、H-I01 与 B00--B08 Cross-Subject Bridge 已建立 Canonical 工作稿，待人工确认和陌生题验证 |
| 数学一 / 高等数学 | [函数对象、表示与结构](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/01_%E5%87%BD%E6%95%B0%E5%AF%B9%E8%B1%A1_%E8%A1%A8%E7%A4%BA%E4%B8%8E%E7%BB%93%E6%9E%84/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [极限与连续：邻域、尺度与存在性](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/02_%E6%9E%81%E9%99%90%E4%B8%8E%E8%BF%9E%E7%BB%AD_%E9%82%BB%E5%9F%9F%E5%B0%BA%E5%BA%A6%E4%B8%8E%E5%AD%98%E5%9C%A8%E6%80%A7/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [一元局部模型：导数、微分与 Taylor](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/03_%E4%B8%80%E5%85%83%E5%B1%80%E9%83%A8%E6%A8%A1%E5%9E%8B_%E5%AF%BC%E6%95%B0%E5%BE%AE%E5%88%86%E4%B8%8ETaylor/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [局部到整体：中值定理与函数形状](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/04_%E5%B1%80%E9%83%A8%E5%88%B0%E6%95%B4%E4%BD%93_%E4%B8%AD%E5%80%BC%E5%AE%9A%E7%90%86%E4%B8%8E%E5%87%BD%E6%95%B0%E5%BD%A2%E7%8A%B6/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [一元累积：原函数、定积分与反常积分](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/05_%E4%B8%80%E5%85%83%E7%B4%AF%E7%A7%AF_%E5%8E%9F%E5%87%BD%E6%95%B0%E5%AE%9A%E7%A7%AF%E5%88%86%E4%B8%8E%E5%8F%8D%E5%B8%B8%E7%A7%AF%E5%88%86/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [空间对象与方向表示](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/06_%E7%A9%BA%E9%97%B4%E5%AF%B9%E8%B1%A1%E4%B8%8E%E6%96%B9%E5%90%91%E8%A1%A8%E7%A4%BA/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [多元局部模型：可微、梯度、隐函数与极值](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/07_%E5%A4%9A%E5%85%83%E5%B1%80%E9%83%A8%E6%A8%A1%E5%9E%8B_%E5%8F%AF%E5%BE%AE%E6%A2%AF%E5%BA%A6%E9%9A%90%E5%87%BD%E6%95%B0%E4%B8%8E%E6%9E%81%E5%80%BC/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [高维累积：区域、坐标与 Jacobian](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/08_%E9%AB%98%E7%BB%B4%E7%B4%AF%E7%A7%AF_%E5%8C%BA%E5%9F%9F%E5%9D%90%E6%A0%87%E4%B8%8EJacobian/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [定向积分与向量场](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/09_%E5%AE%9A%E5%90%91%E7%A7%AF%E5%88%86%E4%B8%8E%E5%90%91%E9%87%8F%E5%9C%BA/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [数项级数：尾部与敛散](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/10_%E6%95%B0%E9%A1%B9%E7%BA%A7%E6%95%B0_%E5%B0%BE%E9%83%A8%E4%B8%8E%E6%95%9B%E6%95%A3/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [函数展开：幂级数、Taylor 与 Fourier](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/11_%E5%87%BD%E6%95%B0%E5%B1%95%E5%BC%80_%E5%B9%82%E7%BA%A7%E6%95%B0Taylor%E4%B8%8EFourier/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [常微分方程：局部规律与整体轨迹](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/12_%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B_%E5%B1%80%E9%83%A8%E8%A7%84%E5%BE%8B%E4%B8%8E%E6%95%B4%E4%BD%93%E8%BD%A8%E8%BF%B9/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [H-B01｜函数结构在运算中的传播](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B01_%E5%87%BD%E6%95%B0%E7%BB%93%E6%9E%84%E5%9C%A8%E8%BF%90%E7%AE%97%E4%B8%AD%E7%9A%84%E4%BC%A0%E6%92%AD/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [H-B02｜局部模型与区间定理：中值点、余项与误差控制](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B02_%E5%B1%80%E9%83%A8%E6%A8%A1%E5%9E%8B%E4%B8%8E%E5%8C%BA%E9%97%B4%E5%AE%9A%E7%90%86_%E4%B8%AD%E5%80%BC%E7%82%B9%E4%BD%99%E9%A1%B9%E4%B8%8E%E8%AF%AF%E5%B7%AE%E6%8E%A7%E5%88%B6/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [H-B03｜微分与累积：基本定理及正则性边界](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B03_%E5%BE%AE%E5%88%86%E4%B8%8E%E7%B4%AF%E7%A7%AF_%E5%9F%BA%E6%9C%AC%E5%AE%9A%E7%90%86%E5%8F%8A%E6%AD%A3%E5%88%99%E6%80%A7%E8%BE%B9%E7%95%8C/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [H-B04｜连续无限累积与离散无限累积](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B04_%E8%BF%9E%E7%BB%AD%E6%97%A0%E9%99%90%E7%B4%AF%E7%A7%AF%E4%B8%8E%E7%A6%BB%E6%95%A3%E6%97%A0%E9%99%90%E7%B4%AF%E7%A7%AF/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [H-B05｜有限 Taylor 模型与无限 Taylor 表示](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/H-B05_%E6%9C%89%E9%99%90Taylor%E6%A8%A1%E5%9E%8B%E4%B8%8E%E6%97%A0%E9%99%90Taylor%E8%A1%A8%E7%A4%BA/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [高等数学 Internal Bridge Atlas](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 数学一 / 高等数学 | [H-I01｜微积分建模：从局部微元到整体量](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/H-I01_%E5%BE%AE%E7%A7%AF%E5%88%86%E5%BB%BA%E6%A8%A1_%E4%BB%8E%E5%B1%80%E9%83%A8%E5%BE%AE%E5%85%83%E5%88%B0%E6%95%B4%E4%BD%93%E9%87%8F/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [高等数学 Integration Layer](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；Canonical 正文由下级 H-I01 目录唯一维护，尚未完成使用者审阅 |
| 数学一 / 高等数学 | [高等数学 Subject Atlas](10_%E6%95%B0%E5%AD%A6%E4%B8%80/10_%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6/README.md) | 已采用；README 是 Canonical Subject Atlas，Topic / Bridge / Integration 按当前路由逐册重构 |
| 数学一 / 线性代数 | [向量空间：生成、基与坐标](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/01_%E5%90%91%E9%87%8F%E7%A9%BA%E9%97%B4_%E7%94%9F%E6%88%90%E5%9F%BA%E4%B8%8E%E5%9D%90%E6%A0%87/README.md) | 待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认 |
| 数学一 / 线性代数 | [线性映射、矩阵与行列式](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/02_%E7%BA%BF%E6%80%A7%E6%98%A0%E5%B0%84_%E7%9F%A9%E9%98%B5%E4%B8%8E%E8%A1%8C%E5%88%97%E5%BC%8F/README.md) | 待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认 |
| 数学一 / 线性代数 | [线性映射、矩阵与行列式](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/02_%E7%BA%BF%E6%80%A7%E6%98%A0%E5%B0%84_%E7%9F%A9%E9%98%B5%E4%B8%8E%E8%A1%8C%E5%88%97%E5%BC%8F/%E7%BA%BF%E6%80%A7%E6%98%A0%E5%B0%84%E3%80%81%E7%9F%A9%E9%98%B5%E4%B8%8E%E8%A1%8C%E5%88%97%E5%BC%8F.md) | Source；第一轮 Markdown 工作稿已迁入 Canonical LaTeX，仅保留作 Source Diff 记录，不再作为正文 Owner |
| 数学一 / 线性代数 | [秩、基本子空间与等价](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/03_%E7%A7%A9_%E5%9F%BA%E6%9C%AC%E5%AD%90%E7%A9%BA%E9%97%B4%E4%B8%8E%E7%AD%89%E4%BB%B7/README.md) | 待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认 |
| 数学一 / 线性代数 | [秩、基本子空间与等价](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/03_%E7%A7%A9_%E5%9F%BA%E6%9C%AC%E5%AD%90%E7%A9%BA%E9%97%B4%E4%B8%8E%E7%AD%89%E4%BB%B7/%E7%A7%A9%E3%80%81%E5%9F%BA%E6%9C%AC%E5%AD%90%E7%A9%BA%E9%97%B4%E4%B8%8E%E7%AD%89%E4%BB%B7.md) | Source；原 README 工作稿，保留作 Topic03 Source Diff 记录，不再作为 Canonical 正文 |
| 数学一 / 线性代数 | [线性方程组：可达性与解空间](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/04_%E7%BA%BF%E6%80%A7%E6%96%B9%E7%A8%8B%E7%BB%84_%E5%8F%AF%E8%BE%BE%E6%80%A7%E4%B8%8E%E8%A7%A3%E7%A9%BA%E9%97%B4/README.md) | 待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认 |
| 数学一 / 线性代数 | [线性方程组：可达性与解空间](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/04_%E7%BA%BF%E6%80%A7%E6%96%B9%E7%A8%8B%E7%BB%84_%E5%8F%AF%E8%BE%BE%E6%80%A7%E4%B8%8E%E8%A7%A3%E7%A9%BA%E9%97%B4/%E7%BA%BF%E6%80%A7%E6%96%B9%E7%A8%8B%E7%BB%84%EF%BC%9A%E5%8F%AF%E8%BE%BE%E6%80%A7%E4%B8%8E%E8%A7%A3%E7%A9%BA%E9%97%B4.md) | Source；原 README 工作稿，保留作 Topic04 Source Diff 记录，不再作为 Canonical 正文 |
| 数学一 / 线性代数 | [特征结构：相似与对角化](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/05_%E7%89%B9%E5%BE%81%E7%BB%93%E6%9E%84_%E7%9B%B8%E4%BC%BC%E4%B8%8E%E5%AF%B9%E8%A7%92%E5%8C%96/README.md) | 待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认 |
| 数学一 / 线性代数 | [特征结构：相似与对角化](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/05_%E7%89%B9%E5%BE%81%E7%BB%93%E6%9E%84_%E7%9B%B8%E4%BC%BC%E4%B8%8E%E5%AF%B9%E8%A7%92%E5%8C%96/%E7%89%B9%E5%BE%81%E7%BB%93%E6%9E%84%EF%BC%9A%E7%9B%B8%E4%BC%BC%E4%B8%8E%E5%AF%B9%E8%A7%92%E5%8C%96.md) | Source；原 README 工作稿，保留作 Topic05 Source Diff 记录，不再作为 Canonical 正文 |
| 数学一 / 线性代数 | [二次型：合同、惯性与正定](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/06_%E4%BA%8C%E6%AC%A1%E5%9E%8B_%E5%90%88%E5%90%8C%E6%83%AF%E6%80%A7%E4%B8%8E%E6%AD%A3%E5%AE%9A/README.md) | 待人工确认；已发布。Canonical LaTeX 第一版正文与 PDF 已建立，等待内容确认 |
| 数学一 / 线性代数 | [二次型：合同、惯性与正定](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/06_%E4%BA%8C%E6%AC%A1%E5%9E%8B_%E5%90%88%E5%90%8C%E6%83%AF%E6%80%A7%E4%B8%8E%E6%AD%A3%E5%AE%9A/%E4%BA%8C%E6%AC%A1%E5%9E%8B%EF%BC%9A%E5%90%88%E5%90%8C%E3%80%81%E6%83%AF%E6%80%A7%E4%B8%8E%E6%AD%A3%E5%AE%9A.md) | Source；原 README 工作稿，保留作 Topic06 Source Diff 记录，不再作为 Canonical 正文 |
| 数学一 / 线性代数 | [线性代数 Subject Atlas：空间、映射、表示与不变量](10_%E6%95%B0%E5%AD%A6%E4%B8%80/20_%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0%20Subject%20Atlas%EF%BC%9A%E7%A9%BA%E9%97%B4%E3%80%81%E6%98%A0%E5%B0%84%E3%80%81%E8%A1%A8%E7%A4%BA%E4%B8%8E%E4%B8%8D%E5%8F%98%E9%87%8F.md) | 已采用；README 是 Canonical Subject Atlas |
| 数学一 / 概率统计 | [随机世界：事件与概率](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/01_%E9%9A%8F%E6%9C%BA%E4%B8%96%E7%95%8C_%E4%BA%8B%E4%BB%B6%E4%B8%8E%E6%A6%82%E7%8E%87/README.md) | Canonical LaTeX 工作稿；P01-A/P01-B 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [条件概率、独立性与 Bayes：信息怎样重分配概率](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/02_%E6%9D%A1%E4%BB%B6%E6%A6%82%E7%8E%87_%E7%8B%AC%E7%AB%8B%E6%80%A7%E4%B8%8EBayes/README.md) | Canonical LaTeX 工作稿；P02-A/P02-B/P02-C 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [随机变量与一维分布：把随机世界映射到数轴](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/03_%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E4%B8%8E%E4%B8%80%E7%BB%B4%E5%88%86%E5%B8%83/README.md) | Canonical LaTeX 工作稿；P03-A/P03-B 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [联合分布、条件分布与变换：概率质量怎样重组](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/04_%E8%81%94%E5%90%88%E5%88%86%E5%B8%83_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B8%83%E4%B8%8E%E5%8F%98%E6%8D%A2/README.md) | Canonical LaTeX 工作稿；P04-A/P04-B 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [数字特征与依赖摘要：怎样压缩分布而不忘记损失](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/05_%E6%95%B0%E5%AD%97%E7%89%B9%E5%BE%81%E4%B8%8E%E4%BE%9D%E8%B5%96%E6%91%98%E8%A6%81/README.md) | Canonical LaTeX 工作稿；P05-A 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [大数定律与中心极限定理：稳定位置与剩余波动](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/06_%E5%A4%A7%E6%95%B0%E5%AE%9A%E5%BE%8B%E4%B8%8E%E4%B8%AD%E5%BF%83%E6%9E%81%E9%99%90%E5%AE%9A%E7%90%86/README.md) | Canonical LaTeX 工作稿；P06-A 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [总体、样本与抽样分布：统计量为什么仍然随机](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/07_%E6%80%BB%E4%BD%93%E6%A0%B7%E6%9C%AC%E4%B8%8E%E6%8A%BD%E6%A0%B7%E5%88%86%E5%B8%83/README.md) | Canonical LaTeX 工作稿；P07-A/P07-B/P07-C 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [参数估计与假设检验：用抽样分布校准逆向推断](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/08_%E5%8F%82%E6%95%B0%E4%BC%B0%E8%AE%A1%E4%B8%8E%E5%81%87%E8%AE%BE%E6%A3%80%E9%AA%8C/README.md) | Canonical LaTeX 工作稿；P08-A/P08-B/P08-C/P08-D 已按 Source Diff 重构并进入逐项核销，尚未完成跨册与人工确认，不视为成熟手册 |
| 数学一 / 概率统计 | [概率论与数理统计统一总图](10_%E6%95%B0%E5%AD%A6%E4%B8%80/30_%E6%A6%82%E7%8E%87%E8%AE%BA/README.md) | 待人工确认；README 是 Canonical Subject Atlas 候选，八个 Topic 已完成首轮迁移与本轮整体结构审阅，仍需真题/陌生题验证跨册 Owner、术语、参数化与 Rules。考试动作另见概率统计做题规则 |
| 数学一 / 跨科 Bridge | [B00｜内积、正交与投影](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B00_%E5%86%85%E7%A7%AF%E6%AD%A3%E4%BA%A4%E4%B8%8E%E6%8A%95%E5%BD%B1/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B01｜局部线性化：微分 × 线性映射](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B01_%E5%B1%80%E9%83%A8%E7%BA%BF%E6%80%A7%E5%8C%96_%E5%BE%AE%E5%88%86%E4%B8%8E%E7%BA%BF%E6%80%A7%E6%98%A0%E5%B0%84/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B02｜Jacobian 与行列式：坐标变换 × 局部体积缩放](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B02_Jacobian%E4%B8%8E%E8%A1%8C%E5%88%97%E5%BC%8F_%E5%9D%90%E6%A0%87%E5%8F%98%E6%8D%A2%E4%B8%8E%E5%B1%80%E9%83%A8%E4%BD%93%E7%A7%AF%E7%BC%A9%E6%94%BE/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B03｜Hessian 与二次型：二阶局部形状 × 正定性](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B03_Hessian%E4%B8%8E%E4%BA%8C%E6%AC%A1%E5%9E%8B_%E4%BA%8C%E9%98%B6%E5%B1%80%E9%83%A8%E5%BD%A2%E7%8A%B6%E4%B8%8E%E6%AD%A3%E5%AE%9A%E6%80%A7/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B04｜梯度、正交与 Lagrange：约束极值 × 子空间几何](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B04_%E6%A2%AF%E5%BA%A6%E6%AD%A3%E4%BA%A4%E4%B8%8ELagrange_%E7%BA%A6%E6%9D%9F%E6%9E%81%E5%80%BC%E4%B8%8E%E5%AD%90%E7%A9%BA%E9%97%B4%E5%87%A0%E4%BD%95/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B05｜线性方程与线性微分方程：一点 + Kernel](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B05_%E7%BA%BF%E6%80%A7%E6%96%B9%E7%A8%8B%E4%B8%8E%E7%BA%BF%E6%80%A7%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B_%E4%B8%80%E7%82%B9%E5%8A%A0Kernel/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B06A｜PDF 与 CDF：局部概率密度 × 累积](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B06A_PDF%E4%B8%8ECDF_%E5%B1%80%E9%83%A8%E6%A6%82%E7%8E%87%E5%AF%86%E5%BA%A6%E4%B8%8E%E7%B4%AF%E7%A7%AF/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B06B｜期望、联合概率与边缘化：概率的积分语言](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B06B_%E6%9C%9F%E6%9C%9B%E8%81%94%E5%90%88%E6%A6%82%E7%8E%87%E4%B8%8E%E8%BE%B9%E7%BC%98%E5%8C%96_%E6%A6%82%E7%8E%87%E7%9A%84%E7%A7%AF%E5%88%86%E8%AF%AD%E8%A8%80/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B07｜随机变量变换与 Jacobian：概率质量守恒](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B07_%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E5%8F%98%E6%8D%A2%E4%B8%8EJacobian_%E6%A6%82%E7%8E%87%E8%B4%A8%E9%87%8F%E5%AE%88%E6%81%92/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [B08｜Fourier 与正交基：函数表示 × 正交投影](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/B08_Fourier%E4%B8%8E%E6%AD%A3%E4%BA%A4%E5%9F%BA_%E5%87%BD%E6%95%B0%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%AD%A3%E4%BA%A4%E6%8A%95%E5%BD%B1/README.md) | 待人工确认；已建立 Canonical LaTeX 工作稿，尚未完成使用者审阅 |
| 数学一 / 跨科 Bridge | [数学一 Core Bridge Atlas](10_%E6%95%B0%E5%AD%A6%E4%B8%80/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/README.md) | 已采用；README 是 Canonical Bridge Atlas，B00--B08 Canonical Bridge 工作稿已建立，均待人工确认 |
| 数学一 / 跨科 Integration | [I01｜二维正态分布：三科汇流验收](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/I01_%E4%BA%8C%E7%BB%B4%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83_%E4%B8%89%E7%A7%91%E6%B1%87%E6%B5%81%E9%AA%8C%E6%94%B6/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Integration | [I02｜二维随机变量线性变换](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/I02_%E4%BA%8C%E7%BB%B4%E9%9A%8F%E6%9C%BA%E5%8F%98%E9%87%8F%E7%BA%BF%E6%80%A7%E5%8F%98%E6%8D%A2/README.md) | 目录已建立，正文未建 |
| 数学一 / 跨科 Integration | [I03｜线性常微分方程组](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/I03_%E7%BA%BF%E6%80%A7%E5%B8%B8%E5%BE%AE%E5%88%86%E6%96%B9%E7%A8%8B%E7%BB%84/README.md) | 目录已建立，正文未建；部分内容属于 Extension 验收 |
| 数学一 / 跨科 Integration | [数学一 Integration Layer](10_%E6%95%B0%E5%AD%A6%E4%B8%80/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，Integration 正文未建 |
| 数学一 / 数学 Rules | [数学一 学科做题规则](10_%E6%95%B0%E5%AD%A6%E4%B8%80/90_%E5%AD%A6%E7%A7%91%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 目录已建立，规则正在积累 |
| 数学一 / 数学 Rules | [线性代数 学科做题规则](10_%E6%95%B0%E5%AD%A6%E4%B8%80/90_%E5%AD%A6%E7%A7%91%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0.md) | 待验证；已完成第一轮 AI 反例/边界攻击，尚未经过使用者陌生题/真题调用验证 |
| 数学一 / 数学 Rules | [高等数学做题规则](10_%E6%95%B0%E5%AD%A6%E4%B8%80/90_%E5%AD%A6%E7%A7%91%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/%E9%AB%98%E7%AD%89%E6%95%B0%E5%AD%A6.md) | 待验证；当前收录高数 Topic01--12、H-B01--H-B05、H-I01 及其跨学科 Bridge 的控制动作 |
| 数学一 | [数学一认知体系总架构](10_%E6%95%B0%E5%AD%A6%E4%B8%80/README.md) | 已采用；README 是 Canonical Course / Exam Atlas，Subject Topic / Bridge / Integration 正文分阶段建设中 |
| 408 / 总图 | [408 学科架构：Canonical Topology 设计依据](30_408/00_%E7%BB%9F%E4%B8%80%E6%80%BB%E5%9B%BE/408%20%E5%AD%A6%E7%A7%91%E6%9E%B6%E6%9E%84.md) | 框架已采用；本文件记录为什么这样切，不承担日常导航。日常入口见 408 Course Atlas |
| 408 / 数据结构 | [数据结构学科总图](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/00_%E5%AD%A6%E7%A7%91%E6%80%BB%E5%9B%BE/README.md) | Source；非 Handbook Owner；Atlas Foundation / Deep Map 旧工作稿，待与 Canonical Data Structure Subject Atlas README 做 Source Diff；不再迁成第二份 Atlas LaTeX |
| 408 / 数据结构 | [DS01｜线性关系与存储表示](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/01_%E7%BA%BF%E6%80%A7%E5%85%B3%E7%B3%BB%E4%B8%8E%E5%AD%98%E5%82%A8%E8%A1%A8%E7%A4%BA/README.md) | LaTeX 工作稿，待人工确认；已建立并发布 Canonical 深度正文 |
| 408 / 数据结构 | [DS02｜栈、队列与受限访问](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/02_%E6%A0%88%E9%98%9F%E5%88%97%E4%B8%8E%E5%8F%97%E9%99%90%E8%AE%BF%E9%97%AE/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS03｜串与模式匹配](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/03_%E4%B8%B2%E4%B8%8E%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS04｜树与二叉树](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/04_%E6%A0%91%E4%B8%8E%E4%BA%8C%E5%8F%89%E6%A0%91/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS05｜Heap 与优先队列](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/05_Heap%E4%B8%8E%E4%BC%98%E5%85%88%E9%98%9F%E5%88%97/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS06｜Union-Find 与集合划分](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/06_UnionFind%E4%B8%8E%E9%9B%86%E5%90%88%E5%88%92%E5%88%86/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS07｜图的表示与遍历](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/07_%E5%9B%BE%E7%9A%84%E8%A1%A8%E7%A4%BA%E4%B8%8E%E9%81%8D%E5%8E%86/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS08｜图上的结构算法](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/08_%E5%9B%BE%E4%B8%8A%E7%9A%84%E7%BB%93%E6%9E%84%E7%AE%97%E6%B3%95/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS09｜查找与有序索引](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/09_%E6%9F%A5%E6%89%BE%E4%B8%8E%E6%9C%89%E5%BA%8F%E7%B4%A2%E5%BC%95/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS10｜Hash 与直接定位](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/10_Hash%E4%B8%8E%E7%9B%B4%E6%8E%A5%E5%AE%9A%E4%BD%8D/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS11｜内部排序](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/11_%E5%86%85%E9%83%A8%E6%8E%92%E5%BA%8F/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS12｜外部排序](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/12_%E5%A4%96%E9%83%A8%E6%8E%92%E5%BA%8F/README.md) | Canonical 正文、C++17 伴随实现与边界测试已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS-B01｜Frontier Traversal](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/DS-B01_FrontierTraversal/README.md) | Canonical 正文已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS-B02｜Index Strategy × Workload](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/DS-B02_IndexStrategy%E4%B8%8EWorkload/README.md) | Canonical 正文已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [DS-B03｜Heap / Union-Find × Graph Algorithm](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/DS-B03_%E8%BE%85%E5%8A%A9%E7%BB%93%E6%9E%84%E4%B8%8E%E5%9B%BE%E7%AE%97%E6%B3%95/README.md) | Canonical 正文已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [数据结构 Internal Bridge Atlas](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，B01–B03 已建立并发布深度正文 |
| 408 / 数据结构 | [DS-I01｜从 Workload 到数据结构选择](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/DS-I01_%E4%BB%8EWorkload%E5%88%B0%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E9%80%89%E6%8B%A9/README.md) | Canonical 正文已建立；Published PDF 见下方链接 |
| 408 / 数据结构 | [数据结构 Integration Layer](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；DS-I01 已建立并发布深度正文 |
| 408 / 数据结构 | [数据结构做题规则](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / 数据结构 | [数据结构 Subject Atlas](30_408/10_%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/README.md) | 已采用；README 是 Canonical Subject Atlas，Atlas Foundation、12 个 Topic、3 个 internal Bridge、1 个 Integration 均已建立深度正文与发布视图；当前进入真题/陌生题验证阶段 |
| 408 / 计组 | [计算机组成原理学科总图：ISA 语义如何成为硬件时序](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/00_%E5%AD%A6%E7%A7%91%E6%80%BB%E5%9B%BE/README.md) | Source；Atlas Deep Map 工作稿，待与根目录 Canonical Subject Atlas README 做 Source Diff |
| 408 / 计组 | [数据表示与运算](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/10_%E6%95%B0%E6%8D%AE%E8%A1%A8%E7%A4%BA%E4%B8%8E%E8%BF%90%E7%AE%97/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [ISA 与机器级程序：软件意图怎样成为可执行契约](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/20_ISA%E4%B8%8E%E6%9C%BA%E5%99%A8%E7%BA%A7%E7%A8%8B%E5%BA%8F/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [CPU 数据通路与控制：把指令契约落实为状态转移](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/30_CPU%E6%95%B0%E6%8D%AE%E9%80%9A%E8%B7%AF%E4%B8%8E%E6%8E%A7%E5%88%B6/README.md) | 待人工确认；Canonical LaTeX 候选正文已建立并发布 |
| 408 / 计组 | [流水线与指令级并行：重叠执行怎样保持顺序语义](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/40_%E6%B5%81%E6%B0%B4%E7%BA%BF%E4%B8%8E%E6%8C%87%E4%BB%A4%E7%BA%A7%E5%B9%B6%E8%A1%8C/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [主存与存储硬件：地址怎样落到物理介质](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/50_%E4%B8%BB%E5%AD%98%E4%B8%8E%E5%AD%98%E5%82%A8%E7%A1%AC%E4%BB%B6/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [Cache 与存储层次：怎样维护一个正确的高速副本](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/60_Cache%E4%B8%8E%E5%AD%98%E5%82%A8%E5%B1%82%E6%AC%A1/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [地址翻译与虚拟存储硬件：VA 怎样成为可访问的 PA](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/70_%E5%9C%B0%E5%9D%80%E7%BF%BB%E8%AF%91%E4%B8%8E%E8%99%9A%E6%8B%9F%E5%AD%98%E5%82%A8%E7%A1%AC%E4%BB%B6/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [总线与 I/O 硬件](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/80_%E6%80%BB%E7%BA%BF%E4%B8%8EIO%E7%A1%AC%E4%BB%B6/README.md) | LaTeX 工作稿待人工确认；Canonical 深度正文已建立并发布 |
| 408 / 计组 | [CO-B01｜ISA Semantic × Datapath](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/CO-B01_ISA%E8%AF%AD%E4%B9%89%E4%B8%8E%E6%95%B0%E6%8D%AE%E9%80%9A%E8%B7%AF/README.md) | LaTeX 工作稿待人工确认；Canonical Bridge 正文已建立并发布 |
| 408 / 计组 | [CO-B02｜Address Translation × Cache Access](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/CO-B02_%E5%9C%B0%E5%9D%80%E7%BF%BB%E8%AF%91%E4%B8%8ECache%E8%AE%BF%E9%97%AE/README.md) | LaTeX 工作稿待人工确认；Canonical Bridge 正文已建立并发布 |
| 408 / 计组 | [计算机组成原理 Internal Bridge Atlas](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas。CO-B01 与 CO-B02 的 Canonical 候选正文均已建立并发布，待真题攻击与人工确认 |
| 408 / 计组 | [计组科内桥梁与综合：从 C 语句到一次精确提交](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/85_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81%E4%B8%8E%E7%BB%BC%E5%90%88/%E8%AE%A1%E7%BB%84%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81%E4%B8%8E%E7%BB%BC%E5%90%88%EF%BC%9A%E4%BB%8E%20C%20%E8%AF%AD%E5%8F%A5%E5%88%B0%E4%B8%80%E6%AC%A1%E7%B2%BE%E7%A1%AE%E6%8F%90%E4%BA%A4.md) | legacy-unregistered Source；不再作为 Canonical Bridge / Integration Owner |
| 408 / 计组 | [CO-I01｜一条指令的一生](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/86_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/CO-I01_%E4%B8%80%E6%9D%A1%E6%8C%87%E4%BB%A4%E7%9A%84%E4%B8%80%E7%94%9F/README.md) | LaTeX 工作稿待人工确认；Canonical Integration 正文已建立并发布 |
| 408 / 计组 | [计算机组成原理 Integration Layer](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/86_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；CO-I01 Canonical Integration 候选正文已建立并发布，待真题攻击与人工确认 |
| 408 / 计组 | [计组做题规则与性能工具箱](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / 计组 | [计算机组成原理 Subject Atlas](30_408/20_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E5%8E%9F%E7%90%86/README.md) | 已采用；README 是 Canonical Subject Atlas。52 份个人旧笔记已完成全科 Source Routing；CO-01 至 CO-08 均已建立并发布 Canonical LaTeX 候选正文，待统一真题攻击与人工确认 |
| 408 / OS | [操作系统学科总图](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/00_%E5%AD%A6%E7%A7%91%E6%80%BB%E5%9B%BE/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-00 操作系统基础与程序运行环境](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/05_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E5%9F%BA%E7%A1%80%E4%B8%8E%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83/README.md) | Canonical LaTeX 第一版正文已建立并已有 Published PDF；待真题与已有笔记继续校验 |
| 408 / OS | [进程、线程、调度与控制权](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/10_%E8%BF%9B%E7%A8%8B%E7%BA%BF%E7%A8%8B%E8%B0%83%E5%BA%A6%E4%B8%8E%E6%8E%A7%E5%88%B6%E6%9D%83/README.md) | 待人工确认；已发布。历史长笔记、主题卡与 `codebrick_os_blog` 标准 408 Coverage Source Diff 已完成，Canonical LaTeX 候选正文已纳管 |
| 408 / OS | [并发、同步与死锁](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/20_%E5%B9%B6%E5%8F%91%E5%90%8C%E6%AD%A5%E4%B8%8E%E6%AD%BB%E9%94%81/README.md) | 待人工确认；已发布。历史 PV/死锁笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管 |
| 408 / OS | [虚拟内存与页生命周期](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/30_%E8%99%9A%E6%8B%9F%E5%86%85%E5%AD%98%E4%B8%8E%E9%A1%B5%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F/README.md) | 待人工确认；已发布。历史内存/页框笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管 |
| 408 / OS | [I/O 请求、等待与完成](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/40_IO%E8%AF%B7%E6%B1%82%E7%AD%89%E5%BE%85%E4%B8%8E%E5%AE%8C%E6%88%90/README.md) | 待人工确认；已发布。历史磁盘/I-O 笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管 |
| 408 / OS | [文件系统](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/50_%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/README.md) | 待人工确认；已发布。历史文件系统笔记与主题卡 Source Diff 已完成，Canonical LaTeX 候选正文已纳管 |
| 408 / OS | [OS-B01｜Wait / Block / Wakeup](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B01_WaitBlockWakeup/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / OS | [OS-B02｜Process × Virtual Memory](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B02_Process%E4%B8%8EVirtualMemory/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / OS | [OS-B03｜Process × File Reference](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B03_Process%E4%B8%8EFileReference/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / OS | [OS-B04｜VM × File × I/O](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/OS-B04_VMFileIO/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / OS | [OS Internal Bridge Atlas](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/60_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 按当前 Owner 边界逐册重构 |
| 408 / OS | [OS-I01｜一次 Blocking `read()`](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/70_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/OS-I01_BlockingRead/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS-I02｜`fork()` + COW + Resource Reference](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/70_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/OS-I02_ForkCOW%E4%B8%8E%E8%B5%84%E6%BA%90%E5%BC%95%E7%94%A8/README.md) | 目录已建立，正文未建 |
| 408 / OS | [OS Integration Layer](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/70_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用，正文待重构 |
| 408 / OS | [操作系统实战课程 · HTML 教学视图](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/80_%E5%AE%9E%E6%88%98%E8%AF%BE%E7%A8%8B/README.md) | Prototype / Derived Learning View（非 Canonical Knowledge Owner） |
| 408 / OS | [操作系统做题规则](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，待验证规则已建立，尚无已采用规则 |
| 408 / OS | [操作系统 Subject Atlas](30_408/30_%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/README.md) | 已采用；README 是 Canonical Subject Atlas。OS-00 与五个 Core Topic 的 Source Diff / Owner Diff 已完成，六册 Canonical LaTeX 均已纳管并有发布视图；新增 Rules 仍待真题验证与人工确认 |
| 408 / 网络 | [计算机网络统一总图：分布式状态、作用域与报文的一生](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/00_%E7%BD%91%E7%BB%9C%E7%BB%9F%E4%B8%80%E6%80%BB%E5%9B%BE/README.md) | Source；Atlas Deep Map 工作稿，待与根目录 Canonical Subject Atlas README 做 Source Diff |
| 408 / 网络 | [通信基础与网络性能：把信息送过有限信道](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/01_%E9%80%9A%E4%BF%A1%E5%9F%BA%E7%A1%80%E4%B8%8E%E7%BD%91%E7%BB%9C%E6%80%A7%E8%83%BD/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [单跳交付：帧、MAC、局域网与交换机](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/02_%E5%8D%95%E8%B7%B3%E4%BA%A4%E4%BB%98_%E5%B8%A7_MAC_%E5%B1%80%E5%9F%9F%E7%BD%91%E4%B8%8E%E4%BA%A4%E6%8D%A2%E6%9C%BA/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [可靠传输：用有限状态驯服丢失、损坏与乱序](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/03_%E5%8F%AF%E9%9D%A0%E4%BC%A0%E8%BE%93_%E5%BA%8F%E5%8F%B7_ACK_%E5%AE%9A%E6%97%B6%E5%99%A8%E4%B8%8E%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [IP 地址、子网与分组转发：把全局目的压缩成逐跳动作](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/04_IP%E5%9C%B0%E5%9D%80_%E5%AD%90%E7%BD%91%E4%B8%8E%E5%88%86%E7%BB%84%E8%BD%AC%E5%8F%91/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [路由与控制平面：不完整知识怎样收敛为可用转发状态](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/05_%E8%B7%AF%E7%94%B1_%E5%88%86%E5%B8%83%E5%BC%8F%E7%9F%A5%E8%AF%86%E4%B8%8E%E6%8E%A7%E5%88%B6%E5%B9%B3%E9%9D%A2/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [传输层：从 host 交付到 process 会话](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/06_%E4%BC%A0%E8%BE%93%E5%B1%82_%E7%AB%AF%E7%82%B9_UDP%E4%B8%8ETCP%E7%8A%B6%E6%80%81%E6%9C%BA/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [拥塞控制：在不知道路径容量时闭环试探](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/07_%E6%8B%A5%E5%A1%9E_%E5%85%B1%E4%BA%AB%E8%B5%84%E6%BA%90%E4%B8%8E%E5%8F%8D%E9%A6%88%E6%8E%A7%E5%88%B6/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [应用层：把通信能力组织成可发现、可解释的服务](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/08_%E5%BA%94%E7%94%A8%E5%B1%82_DNS_HTTP%E4%B8%8E%E6%9C%8D%E5%8A%A1%E8%AF%AD%E4%B9%89/README.md) | 已采用候选；Canonical 深度正文已建立并发布，心智模型仍待题目验证 |
| 408 / 网络 | [NET-B01｜IP Forwarding × Single-Hop Delivery](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B01_IPForwarding%E4%B8%8ESingleHop/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 网络 | [NET-B02｜Routing × Forwarding](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B02_Routing%E4%B8%8EForwarding/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 网络 | [NET-B03｜Reliable Transfer × TCP](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B03_ReliableTransfer%E4%B8%8ETCP/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 网络 | [NET-B04｜Flow Control × Congestion Control](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B04_FlowControl%E4%B8%8ECongestionControl/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 网络 | [BDP × Window：用在途预算填满反馈管道](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B05_BDP%E4%B8%8EWindow/README.md) | 已采用；Canonical Bridge 正文已建立并发布，待题目验证 |
| 408 / 网络 | [MTU × Segmentation：四层尺寸责任](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/NET-B06_MTU%E4%B8%8ESegmentation/README.md) | 已采用；Canonical Bridge 正文已建立并发布，待题目验证 |
| 408 / 网络 | [计算机网络 Internal Bridge Atlas](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/50_%E7%A7%91%E5%86%85%E6%A1%A5%E6%A2%81/README.md) | 已采用；README 是 Canonical Internal Bridge Atlas，下游 Bridge 仍按规划逐册建设 |
| 408 / 网络 | [NET-I01｜一个网络请求的一生：从域名到网页返回](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/NET-I01_%E4%B8%80%E4%B8%AA%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82%E7%9A%84%E4%B8%80%E7%94%9F/README.md) | 已采用候选；Canonical Integration 正文已建立并发布，组合边界已复核 |
| 408 / 网络 | [计算机网络 Integration Layer](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；NET-I01 已完成组合边界复核并发布 Canonical LaTeX 阅读版 |
| 408 / 网络 | [计算机网络做题规则](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/90_%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿；旧笔记已形成待验证动作与已否定口诀，尚无已采用规则 |
| 408 / 网络 | [计算机网络 Subject Atlas](30_408/40_%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C/README.md) | 已采用；README 是 Canonical Subject Atlas。31 份个人旧笔记已完成全科 Source Routing；NET01--NET08 八个 Topic 均已建立并发布 Canonical LaTeX 候选正文，NET-I01 已建立并发布 Integration |
| 408 / 跨科 Bridge | [408 Cross-Subject Bridge Atlas](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/README.md) | 已采用；README 是 Canonical Cross-Subject Bridge Atlas，3 个 Core Bridge 与 1 个 Candidate Core 按当前边界逐册建设 |
| 408 / 跨科 Bridge | [X-B01｜Privilege / Exception / System Call × OS Control](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B01_PrivilegeExceptionSystemCall%E4%B8%8EOSControl/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 跨科 Bridge | [X-B02｜Hardware Address Translation × OS Virtual Memory](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B02_HardwareAddressTranslation%E4%B8%8EOSVirtualMemory/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 跨科 Bridge | [X-B03｜Interrupt / DMA × OS I/O](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B03_InterruptDMA%E4%B8%8EOSIO/README.md) | 已采用；Canonical Bridge 正文已建立并发布 |
| 408 / 跨科 Bridge | [X-B04｜Process / Socket × Transport Endpoint](30_408/50_%E6%A1%A5%E6%A2%81%E4%B8%93%E9%A2%98/X-B04_ProcessSocket%E4%B8%8ETransportEndpoint/README.md) | Candidate Core；接口结构已确认，是否升级为 Core 待 408 考纲/真题覆盖证据与重复调用证据 |
| 408 / 跨科 Integration | [408 Cross-Subject Integration Layer](30_408/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 框架已采用；2 个核心 Integration 已建立骨架，综合发布物待按新 Ownership 纳管 |
| 408 / 跨科 Integration | [X-I01｜一次 LOAD / Memory Access 的完整慢路径](30_408/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/X-I01_LOAD%E4%B8%8EMemoryAccess%E6%85%A2%E8%B7%AF%E5%BE%84/README.md) | 目录已建立，正文未建 |
| 408 / 跨科 Integration | [X-I02｜一次 Blocking File `read()` 的完整生命周期](30_408/60_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/X-I02_BlockingFileRead%E5%AE%8C%E6%95%B4%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F/README.md) | 目录已建立，正文未建 |
| 408 / 408 Rules | [408 通用做题规则](30_408/90_408%E5%81%9A%E9%A2%98%E8%A7%84%E5%88%99/README.md) | 工作稿，通用入口已建立，规则尚待证据化 |
| 408 | [408 Course Atlas](30_408/README.md) | 已采用；README 是 Canonical Course Atlas，四个 Subject 与下游 Handbook 按当前拓扑继续建设 |
| 系统 | [问题求解 Area Atlas：在显式候选空间中找到解](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/10_%E9%97%AE%E9%A2%98%E6%B1%82%E8%A7%A3/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [知识表示与推理 Area Atlas：把世界结构变成可操作的显式知识](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/20_%E7%9F%A5%E8%AF%86%E8%A1%A8%E7%A4%BA%E4%B8%8E%E6%8E%A8%E7%90%86/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [概率推理与不确定性 Area Atlas：用分布表示未知并吸收证据](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/30_%E6%A6%82%E7%8E%87%E6%8E%A8%E7%90%86%E4%B8%8E%E4%B8%8D%E7%A1%AE%E5%AE%9A%E6%80%A7/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [机器学习 Area Atlas：从经验中选择能泛化的模型](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/40_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [优化与学习计算 Area Atlas：把目标函数变成可执行更新](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/50_%E4%BC%98%E5%8C%96%E4%B8%8E%E5%AD%A6%E4%B9%A0%E8%AE%A1%E7%AE%97/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [深度学习 Area Atlas：构造可训练的层级函数与表示](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/60_%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [决策、控制与强化学习 Area Atlas：从 belief 到长期行为](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/70_%E5%86%B3%E7%AD%96_%E6%8E%A7%E5%88%B6%E4%B8%8E%E5%BC%BA%E5%8C%96%E5%AD%A6%E4%B9%A0/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [生成模型 Area Atlas：学习生成规律并把模型变成样本](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/80_%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B/README.md) | 已采用；Area Boundary v1 + Leaf Boundary v1 已锁定。Leaf Topic 仅建立 Canonical 归属与依赖，不批量创建深度正文 |
| 系统 | [AI Cross-Area Bridge Atlas](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/85_%E8%B7%A8%E5%9F%9F%E6%A1%A5%E6%A2%81/README.md) | 已采用；Leaf Boundary v1 端点已登记。这里只登记跨 Area 稳定接口与 Candidate，不预建未成熟 Bridge 正文 |
| 系统 | [AI Integration Atlas：把多个成熟机制跑成完整过程](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/90_%E7%BB%BC%E5%90%88%E4%B8%93%E9%A2%98/README.md) | 已采用；只拥有跨 Area 的完整过程，不拥有任何单点机制 |
| 系统 | [AI Research Direction Atlas：纵向研究路线的调用地图](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/95_%E7%A0%94%E7%A9%B6%E6%96%B9%E5%90%91/README.md) | 已采用；这里只负责研究方向 Routing，不复制 Core Area 的机制 |
| 系统 | [人工智能与机器学习 Subject Atlas：智能体、推理、学习与决策](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/README.md) | Area Boundary v1 + Leaf Boundary v1 已采用；八个 Core Area 的 Canonical Scope / Stop Boundary、Leaf Topic 归属与内部 Dependency DAG 已锁定。Bridge / Integration 深度正文仍按真实学习逐步建立 |
| 系统 | [人工智能与机器学习：文件夹与 Handbook 架构](40_%E5%A4%8D%E8%AF%95/10_%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%EF%BC%9A%E6%96%87%E4%BB%B6%E5%A4%B9%E4%B8%8E%20Handbook%20%E6%9E%B6%E6%9E%84.md) | Area Boundary v1 + Leaf Boundary v1 已采用；八个 Core Area 的物理层级、Canonical Scope、Leaf Topic 归属与内部依赖已锁定。深度正文仍按真实学习逐步建立 |
| 系统 | [复试 Course / Exam Atlas](40_%E5%A4%8D%E8%AF%95/README.md) | Atlas 工作稿，待人工确认；当前只建立 AI / Machine Learning 学习支线，其他复试模块按真实需要再建 |
| 系统 | [2023 数一线代真题：审计合并指针](80_evidence/archive/review_log/2026-08-12/2026-08-11_2023%E6%95%B0%E4%B8%80%E7%BA%BF%E4%BB%A3%E7%9C%9F%E9%A2%98_Rules%E4%B8%8ETopic%E6%98%A0%E5%B0%84%E5%AE%A1%E8%AE%A1.md) | 已合并，不再作为独立审计正文 |
| 系统 | [概率统计归档笔记 Source Migration 设计](80_evidence/review_log/2026-08-11_%E6%A6%82%E7%8E%87%E7%BB%9F%E8%AE%A1_%E5%BD%92%E6%A1%A3%E7%AC%94%E8%AE%B0_Source_Migration_%E8%AE%BE%E8%AE%A1.md) | 首轮 Source Diff 与本轮整体结构审阅已完成；进入真题/陌生题 Rules 攻击与跨册参数化验证 |
| 系统 | [数学一真题：按心智模型主题分类总索引](80_evidence/review_log/2026-08-12_%E6%95%B0%E5%AD%A6%E4%B8%80%E7%9C%9F%E9%A2%98_%E5%BF%83%E6%99%BA%E6%A8%A1%E5%9E%8B%E4%B8%BB%E9%A2%98%E5%88%86%E7%B1%BB.md) | 分类底账已建立；残损题保留“待回图复核”。本文件是外部真题的证据索引，不是三科 Handbook 的知识 Owner |
| 系统 | [数学一线性代数真题：心智模型检验与分类](80_evidence/review_log/2026-08-12_%E6%95%B0%E5%AD%A6%E4%B8%80%E7%BA%BF%E6%80%A7%E4%BB%A3%E6%95%B0%E7%9C%9F%E9%A2%98_%E5%BF%83%E6%99%BA%E6%A8%A1%E5%9E%8B%E6%A3%80%E9%AA%8C%E4%B8%8E%E5%88%86%E7%B1%BB.md) | Candidate；本文件是外部真题的证据索引，不是线性代数知识 Owner |

## 怎样更新

1. 当前工作方向变化时，修改 `CURRENT.md`；
2. 某项资产的物理文件或人工决定发生真实变化时，修改其入口顶部的 `状态：...`；
3. 运行进度生成与系统检查；
4. 不为了让数字增长而修改状态。
