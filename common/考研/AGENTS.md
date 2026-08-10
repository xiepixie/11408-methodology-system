# AGENTS

> 生效范围：本目录 `common/考研/` 及全部子目录。
>
> 这是 Agent 进入考研认知系统后的第一入口。任何上层 `AGENTS.md` 仍然有效；本文件在本目录内增加并覆盖更具体的项目协作规则。

## 0. 每次进入仓库的 Boot Core

开始新的仓库任务时，先建立以下最小上下文：

1. **本文件 `AGENTS.md`**：快速理解项目架构、Ownership 和协作规则；
2. **`CURRENT.md`**：确认当前正在推进什么、哪些结论仍待人工确认；
3. **`00_system/agent_context_protocol.md`**：根据当前场景取得最小 Context Pack。

不要默认通读整个 `00_system/`，也不要默认扫描整个学科目录。

任务明确时优先运行：

```bash
python3 00_system/cognitive_system.py start <scenario> --subject <subject> --topic <topic>
```

常见场景：

```text
explore / model-diff / solve / wrong / adversary
practice / import / review / publish
```

随后按任务读取：

```text
Course / Subject Atlas
-> relevant Topic
-> necessary Bridge / Integration
-> Subject Rules（若涉及做题动作）
-> user material / legacy source / Inbox
```

如果相关 Topic 只有“目录已建立，正文未建”，必须明确说明仓库尚无成熟 Canonical 模型；Agent 自己生成的解释只能标为 provisional model / 工作假设。

## 1. 哪些系统文件什么时候必须读

### 每次任务固定读取

- `CURRENT.md`
- `00_system/agent_context_protocol.md`

本文件已经压缩提供架构、术语和协作基线，因此**不要为了保险每次全文读取全部 system 文件**。

### 任务触发时升级读取

| 任务 | 必须额外读取 |
|---|---|
| 修改稳定资产、导入旧稿、改变状态或目录拓扑 | `00_system/collaboration_workflow.md` |
| 新建/重构 Atlas、Topic、Bridge、Integration、Rules | `00_system/handbook_contract.md` |
| 大规模打磨 Handbook 正文、母模型、章节和验收 | `00_system/handbook_writing_spec.md` |
| 判断唯一 Owner、处理重复定义或跨文件依赖 | `00_system/ownership_matrix.md` |
| 错题诊断、规则晋升、周复盘、证据判断 | `00_system/evidence_promotion.md` |
| 改系统层级、资产模型或协作架构 | `00_system/architecture.md` |
| 术语冲突或语义不确定 | `00_system/terminology.md` |
| 需要通用 Problem-Solving Control | `01_control/problem_solving_kernel.md` |

原则：**最小充分上下文，不是最大上下文。**

## 2. 仓库目标

这是一个 **考研个人认知与考场决策系统**，不是百科全书、题库或教材摘抄库。

目标链：

```text
Understand -> Solve -> Perform -> Learn
```

系统最终保存的是经过理解、推理、反例、题目和真实表现检验后，使用者愿意采用的认知模型和行动规则。

AI 是认知放大器，不是认知代理人。最终决定“相信什么、采用什么”的只能是使用者。

## 3. 三个 Plane 与三类长期资产

```text
Knowledge Plane + Control Plane + Learning Plane
                    |
                    v
             Publication View
```

- **Knowledge Plane → Handbooks**：世界怎样运转；
- **Control Plane → Rules**：题目和考试中具体怎样行动；
- **Learning Plane → Inbox + 真实练习**：暴露、诊断、攻击、验证候选想法；
- **Publication → PDF**：`90_publish/*.pdf` 是由 Handbook Canonical LaTeX 编译得到的发布视图；`.tex` 本身属于 Knowledge Source，不是 Publication。

长期只维护三类资产：

```text
Handbooks / Rules / Inbox
```

### Handbook 的物理真相必须立刻记住

```text
README.md               = Landing Page / 导航与引子
<Handbook>.tex          = Canonical Handbook Source / 唯一正文 (.tex)
90_publish/*.pdf        = Published View / 编译结果 (.pdf)
Subject Rules           = Control Plane Rules / 做题指南 (Markdown)
Inbox / System          = Learning & System Metadata (Markdown)
```

因此，Agent 进入某个 Topic 时：**先读 README 定位，再读 `.tex` 获取模型正文。没有 `.tex` 就必须声明“Canonical Handbook 尚未建立”；旧长 README 只能作为 Source / legacy working draft（产生的解释标为 provisional model）。**

不要为了目录整齐引入新的日常填表、ID、YAML 或数据库负担。

## 4. Knowledge Plane：四种 Handbook

稳定 Handbook 只有：

```text
Atlas -> Topic -> Bridge -> Integration
```

它们是解释责任，不是简单章节层级。

### Atlas = Map

回答：

```text
Why + Where + Relationship
```

拥有学科母问题、对象地图、Topic 地图和依赖关系，不展开全部机制。

### Topic = Depth

单一核心机制的 Canonical Owner。

标准生成链：

```text
Problem
-> Naive Approach
-> Failure
-> Mechanism
-> Invariant / Boundary
-> Cost / Tradeoff
```

### Bridge = Interface

回答：**两个已有模块为什么能接？**

```text
A output -> translation/shared structure -> B input
```

只有删除具体题目后仍然存在稳定、普遍、可复用的共享机制，才独立建立 Bridge。

### Integration = Composition

回答：**多个成熟模块怎样在一个完整问题/过程中一起运行？**

```text
Problem
-> Module Recognition
-> Module Composition
-> Execution
-> Verification
```

Integration 拥有协作轨迹，不重新拥有参与机制。

最短判据：

```text
Bridge = 两个模块为什么能接（例如 X-B01 Privilege/Syscall 硬件与 OS 控制权切换）
Integration = 多个模块怎样一起工作（例如 OS-I01 BlockingRead 磁盘、内存与进程阻塞读全生命周期）
```

## 5. Extension 与 Anti-Bridge

它们不是第五、第六种 Handbook，而是稳定知识中的关系角色。

### Extension

```text
True Structural Connection + Outside Current Core Scope
```

真连接，但暂时不进入当前主干；只在相关 Atlas / Topic / Bridge 中留下最小指针。

### Anti-Bridge

主动阻断：

```text
表面相似 != 结构相同
```

至少说明为什么容易混淆、真正判据是什么、哪些结论禁止互推。

禁止为 Extension / Anti-Bridge 新建平行资产树。

## 6. Canonical Ownership

任何稳定内容必须先判断：

```text
Own / Use / Bridge / Integrate / Extension / Anti-Bridge
```

- **Own**：完整定义；
- **Use**：调用已有 Owner，不复制；
- **Bridge**：拥有接口；
- **Integrate**：拥有协作轨迹；
- **Extension**：真连接但暂不展开；
- **Anti-Bridge**：明确禁推关系。

同一机制只能有一个 Canonical Owner。

准备修改稳定资产前必须：

1. 判断 Knowledge 还是 Control；
2. 找唯一 Owner；
3. 搜索已有重复定义；
4. 找 Uses / Bridges / Integrations 下游依赖；
5. 只修改有解释责任的位置；
6. Owner 不清楚时先留 Inbox，不为了“有地方放”制造第二份稳定真相。

## 7. 学科解耦与层级

### 7.1 数学一的层级

数学一不共享一个强行统一的世界模型。

```text
Math 1 Course Atlas
        |
        +-- Calculus Subject Atlas
        +-- Linear Algebra Subject Atlas
        +-- Probability & Statistics Subject Atlas
        |
        +-- Cross-Subject Bridges
        +-- Cross-Subject Integrations
```

入口：

- Course Atlas：`10_数学一/README.md`
- 高数：`10_数学一/10_高等数学/README.md`
- 线代：`10_数学一/20_线性代数/README.md`
- 概率：`10_数学一/30_概率论/README.md`
- 跨科 Bridge：`10_数学一/50_桥梁专题/README.md`
- 跨科 Integration：`10_数学一/60_综合专题/README.md`
- 数学 Rules：`10_数学一/90_学科做题规则/`

单科任务只读 Course Atlas + 对应 Subject Atlas + 必要 Topic/Rules；不要无差别加载三科世界模型。

跨学科接口问题才进入 Math 1 Cross-Subject Bridge / Integration。

### 7.2 408 的层级

408 同样使用 Course Atlas → Subject Atlas，但四科保留各自世界模型：

```text
408 Course Atlas
        |
        +-- Data Structure Subject Atlas
        +-- Computer Organization Subject Atlas
        +-- Operating System Subject Atlas
        +-- Computer Network Subject Atlas
        |
        +-- Cross-Subject Core Bridges
        +-- Cross-Subject Integrations
```

入口：

- Course Atlas：`30_408/README.md`
- 数据结构：`30_408/10_数据结构/README.md`
- 计组：`30_408/20_计算机组成原理/README.md`
- OS：`30_408/30_操作系统/README.md`
- 网络：`30_408/40_计算机网络/README.md`
- 跨科 Bridge：`30_408/50_桥梁专题/README.md`
- 跨科 Integration：`30_408/60_综合专题/README.md`
- 408 Rules：`30_408/90_408做题规则/README.md`

当前 Cross-Subject Core Bridge 只有 X-B01 privilege/exception × OS、X-B02 hardware translation × OS VM、X-B03 interrupt/DMA × OS I/O；X-B04 process/socket × transport endpoint 是 Candidate Core。Graph Algorithm × Routing 等真连接当前优先记为 Use/Extension，不因为类比漂亮就独立建册。

数据结构 complexity 与 OS 基础概念属于各自 Atlas Foundation；Foundation 不是第五种 Handbook 类型。

单科任务只读 Course Atlas + 对应 Subject Atlas + 必要 Topic/Rules；跨科问题才加载 Cross-Subject Bridge / Integration。

## 8. Control Plane：机制与调用动作必须分开

“机制为什么成立”和“题里什么时候调用”不是同一个 Owner。

例如：

```text
分部积分机制、条件、结构变化 -> 积分 Topic
看到何种结构考虑分部积分、拆法怎么选 -> Subject Rules
```

通用控制镜头：

```text
Object
-> Goal
-> Structure
-> Representation
-> Transformation / Route
-> Invariant
-> Execute
-> Verify
```

它只是共同控制语言，不得替代各学科自己的世界模型和 Adapter。

## 9. Learning Plane：默认先诊断，不默认更新

```text
Observation
-> Diagnosis
-> Hypothesis
-> Candidate Rule / Model Challenge
-> Independent Test
-> Promote / Revise / Reject / No Update
```

五个主要断点已经足够：

1. 模型；
2. 识别；
3. 路径；
4. 执行 / 检查 / 表达；
5. 考试决策。

模型层需要时再细分：

```text
Topic mechanism / Bridge interface / Integration composition
```

“粗心、状态差、基础差”不是最终诊断；必须继续落到具体行为，或承认证据不足。

No Update 是正式结果。不是每做一道题都必须增加知识节点或规则。

## 10. 默认场景与角色

| 场景 | 主要角色 | 第一目标 |
|---|---|---|
| `explore` | Mapper + Socratic Tutor | 找母问题，暴露当前模型 |
| `model-diff` | Socratic Tutor + Mapper | 找主干、混淆、缺口、边界 |
| `solve` | Model-Grounded Solver | 沿现有模型解题并 Verification |
| `wrong` | Debugger | 找 First Divergence，不先重做 |
| `adversary` | Adversary | 找最小反例、失效条件和成本 |
| `practice` | Coach | 针对已确认断点出少量诊断题 |
| `import` | Mapper + Editor | Handbook Diff + Owner 定位 |
| `review` | Adversary + Editor + Coach | 复盘 Inbox / Rules / 表现 |
| `publish` | Editor | 同步已采用 Canonical 内容 |

用户不需要主动选择角色，Agent 自动路由。

## 11. 默认人机协作顺序

学习和建模场景默认：

```text
用户先解释 / 判断
-> AI 检查、攻击、指出差异
-> 用户修正
-> AI 给反例或诊断题
-> 用户再次解释 / 执行
```

除非用户明确要求直接讲解，不要一开始就用完整标准答案覆盖用户自己的模型。

用户明确要求解题时，可以直接完成，但输出必须沿：

```text
Model Anchor
-> Problem Representation
-> Path Choice
-> Solution Chain
-> Verification
-> Compression Signal
```

## 12. 旧笔记、教材、LaTeX、PDF 的导入规则

所有旧材料首先都是 **Source Corpus**，不是 Canonical Owner。

先拆：

```text
Knowledge / Control / Evidence / Publication
```

Knowledge 再判断：

```text
Atlas / Topic / Bridge / Integration
```

迁移流程：

```text
Locate
-> Find Owner
-> Handbook Diff
-> Split responsibilities
-> Human decision
-> Update correct Owner / create work draft
-> Update status & dependencies if needed
```

旧文件数量绝不等于未来 Handbook 数量。不要为了保留旧稿完整阅读体验整篇复制。

## 13. 系统权威定义源

当本文件的压缩说明不足时，按职责升级读取；其他文件不得另造定义。

| 文件 | Canonical Responsibility |
|---|---|
| `00_system/architecture.md` | Plane、资产、Knowledge topology、快慢循环与系统边界 |
| `00_system/terminology.md` | 核心术语 |
| `00_system/agent_context_protocol.md` | 自动场景路由与 Context Pack |
| `00_system/collaboration_workflow.md` | 写入/更新动作、文件更新矩阵、结束条件 |
| `00_system/handbook_contract.md` | Handbook / Rules 最低契约 |
| `00_system/handbook_writing_spec.md` | 心智模型正文生成结构、写作和验收 |
| `00_system/ownership_matrix.md` | 唯一 Owner 与跨文件边界 |
| `00_system/evidence_promotion.md` | Inbox、诊断、规则验证和晋升 |
| `01_control/problem_solving_kernel.md` | 通用 Problem-Solving Control |

若系统契约之间冲突，不要静默选择；指出冲突并优先修配置。

## 14. 修改稳定资产时的强制流程

只要任务会改变 Handbook、正式 Rules、Ownership、状态或目录拓扑：

1. 读取 `00_system/collaboration_workflow.md`；
2. Handbook 任务读取 `handbook_contract.md`；大规模正文重构再读 `handbook_writing_spec.md`；
3. 检查 `ownership_matrix.md` 和相关 Atlas；
4. 搜索重复定义和下游依赖；
5. 修改唯一 Owner；
6. 必要时同步 Use / Bridge / Integration 链接；
7. 只有真实成熟度变化才改 `状态：...`；
8. 当前焦点变化才更新 `CURRENT.md`；
9. 稳定更新结束后运行 progress / check；
10. 明确报告仍待人工决定的结论。

工具环境禁止写入时，不用 shell 绕过约束。

## 15. Handbook 物理契约、Publication 与状态

### 15.1 Handbook Package

所有正式 `Atlas / Topic / Bridge / Integration` 必须使用：

```text
<Handbook Directory>/
├── README.md          # Landing Page
├── <Handbook>.tex     # Canonical Handbook Source
└── assets/            # 可选

90_publish/
└── <Handbook>.pdf     # Published View
```

物理 Source of Truth 锁定为：

```text
Handbook Knowledge -> .tex
Navigation / Hook  -> README.md
Published Reading -> 90_publish/*.pdf
Rules / Inbox      -> Markdown
System Contracts   -> Markdown
```

**README 绝不能成为第二份简化正文。** 它只负责：

- 一段让学生知道“为什么值得读”的引子；
- 本册 Mother Question；
- Scope / Owns / Uses / Stop Boundary；
- 当前状态；
- Canonical `.tex` 链接；
- 已发布 PDF 链接；
- 推荐前置与下一册。

完整定义、推导、机制生成、边界表、Worked Example、Problem Action 和压缩页只能进入 `.tex`。

**过渡态判定规则**：若某 Topic 处于从旧 Markdown 向 LaTeX 迁移阶段、尚未建立 Canonical `.tex`，现有长篇 README 只能标注为 `legacy working draft`，Agent 生成或引用的任何结论均需明确标记为 `provisional model`，不得替代 Canonical 正文。

### 15.2 编译与发布

从本目录 `common/考研/` 执行：

```bash
python3 ../scripts/compile_tex.py "<target.tex>"
```

脚本会多遍 XeLaTeX 编译并把最终 PDF 移动到 `90_publish/` 根目录；专题目录保持零同名 PDF。

发布链只有：

```text
README Landing Page
-> Canonical .tex
-> compile_tex.py
-> 90_publish/<same-stem>.pdf
```

- `.tex` 是 Handbook 唯一正文真相；
- PDF 不得手工修改；
- README 不得与 `.tex` 复制竞争；
- 旧 Markdown 长篇手册在迁移完成前只能标记为 Source / legacy working draft；
- 旧发布物在 Ownership 梳理前保持 `legacy-unregistered`；
- “已发布”不等于“已采用”。

进度入口：

- `CURRENT.md`：人工维护的当前焦点；
- `PROGRESS.md`：生成型资产状态快照。

稳定更新结束后：

```bash
python3 00_system/cognitive_system.py progress --write
python3 00_system/cognitive_system.py check
```

`cognitive_system.py check` 为项目自动化防线，硬性拦截 5 类异常：
1. **包结构与状态契约**：缺 `.tex` 正文的 Topic 严禁虚报为 `已采用` / `Canonical`；
2. **README 越权防护**：非 legacy README 超过 200 行上限自动报警；
3. **Owner 唯一性与矩阵校验**：校验 `ownership_matrix.md` 引用及非 legacy H1 冲突；
4. **断链防护**：扫描所有 Markdown（含 `Subject Rules`、Bridge、Integration）相对链接；
5. **`CURRENT.md` 鲜活性**：确保当前焦点文件有效且已被更新。

不要为了让进度数字增长而修改状态。

## 16. 完成任务前自检

### Knowledge / Writing

- 找到唯一 Owner 了吗？
- Topic / Bridge / Integration 职责混了吗？
- 把 Extension 扩成主干了吗？
- 应该加 Anti-Bridge 而不是再造连接吗？
- 把 Rules 偷塞进 Handbook 了吗？
- 重复定义已有机制了吗？

### Learning / Diagnosis

- 保留用户原始过程了吗？
- 找的是 First Divergence 而不是最后错误吗？
- 区分事实、假设和建议了吗？
- 考虑 No Update 了吗？
- 有没有把旧题即时重做冒充迁移证据？

### Repository

- 只改有职责的文件了吗？
- 状态与真实成熟度一致吗？
- 必要依赖同步了吗？
- 是否避免扩大无关修改？
- 可运行的结构检查执行了吗？

## 17. 每次交付说明

复杂仓库任务结束时简要说明：

1. 当前场景和主要角色；
2. 实际读取了哪些 Context / Source；
3. 哪些是仓库事实、工作假设、人工决定；
4. 最终是 No Update、Candidate 还是 Canonical Update；
5. 修改了哪些文件，为什么是这些 Owner；
6. 哪些仍待人工确认；
7. 下一次最小动作。

**核心底线：不是每遇到一个新知识或新题就增加一个节点，而是先判断它究竟在深化哪个 Topic、暴露哪个 Bridge、需要哪个 Integration，还是只形成一条 Control Rule。**
