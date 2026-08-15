# 当前焦点

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
