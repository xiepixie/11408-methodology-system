# AGENTS: 考研个人认知与方法论系统维护协议

> **生效范围**：本文件对 `common/考研/` 及其子目录生效；若与仓库根目录的通用教学交付规范冲突，以本文件在该子树内的规定为准。

---

## 1. 系统目标

本目录不是“考研讲义集合”，而是一个能够持续吸收学习、做题和考试反馈，并将其沉淀为稳定世界模型、解题控制规则与考场决策规则的个人认知系统。

系统必须支持完整闭环：
$$
\text{Learn} \longrightarrow \text{Model} \longrightarrow \text{Solve} \longrightarrow \text{Test} \longrightarrow \text{Reflect} \longrightarrow \text{Update} \longrightarrow \text{Model}'
$$

最终服务四种能力：
1. **Understand**：形成正确、有边界、有生成力的学科模型；
2. **Solve**：面对新题时能够识别、规划、执行、校验和表达；
3. **Perform**：在时间、风险和注意力约束下把能力转化为分数；
4. **Learn**：让错误、成功与主观感受经过验证后改进系统。

---

## 2. 四个 Plane 的职责

### 2.1 Knowledge Plane (理解世界)
描述“世界是什么、机制为何存在、对象如何交互”。内部粒度为：
$$
\text{Subject} \longrightarrow \text{Topic} \longrightarrow \text{Bridge} \longrightarrow \text{Integration}
$$
- **Subject / Atlas**：学科总图与核心母问题；
- **Topic Manual**：单一机制的对象、状态、规则、不变量与生命周期；
- **Bridge**：两个专题的接口、责任边界与状态交接；
- **Integration**：多个机制共同参与一个完整过程时的跨系统轨迹。

> Knowledge Plane 不负责回答“考场三分钟无思路时怎么办”。

### 2.2 Control Plane (操作模型)
描述“人怎样操作学科模型”。分为两个时间尺度：
- **Question Control / Micro Control**：一道题内的 $\text{Recognition} \to \text{Planning} \to \text{Execution} \to \text{Verification} \to \text{Expression}$；
- **Exam Control / Macro Control**：整张试卷的 Entry、Exit、Return、Time、Risk、Verification、Expression 与 Attention Policy。

> Control Plane 采用“通用内核 + 学科适配器”：通用控制问题只维护一份，各学科只声明自己的对象语言、典型状态、危险步骤和验证方法。

### 2.3 Learning / Evidence Plane (进化闭环)
描述 Knowledge Plane 与 Control Plane 如何被证据更新。它是输入、验证与演化流水线，不是第四套正式知识。

任何个人感受必须经过：
$$
\text{Observation} \longrightarrow \text{Diagnosis} \longrightarrow \text{Hypothesis} \longrightarrow \text{CandidateRule} \longrightarrow \text{Test} \longrightarrow \text{Promote / Revise / Reject}
$$

> Observation 不得直接写入稳定手册或 Canonical Rule。

### 2.4 Publication Plane (发布视图)
Publication Plane 是前三个 Plane 的发布视图，不是独立知识源。
- **Markdown** 保存工作知识、规则、证据、接口、索引与发布规范；
- **LaTeX / PDF** 保存已经成熟并通过发布检查的稳定手册；
- 不得在 Markdown 与 LaTeX 中并行维护同一阶段、同一职责的两份真相。

---

## 3. Canonical Ownership (唯一归属)

### 3.1 单一所有者
每个概念、规则和模型必须有且只有一个 Canonical Owner。其他文档只能扮演：
- **Use**：直接使用已定义概念；
- **Reference**：链接到所有者；
- **Bridge**：解释两个所有者之间的接口；
- **Integrate**：追踪多个机制在同一过程中的协作。

> 跨专题文档不得为了“阅读完整”而重新完整定义其他专题已经拥有的机制。必要时只能给出最小上下文摘要并链接所有者。

### 3.2 写作前置五问
新增或扩写内容前必须依次回答：
1. 这是 Knowledge、Control、Learning/Evidence 还是 Publication 内容？
2. 它的粒度是 Subject、Topic、Bridge、Integration，还是 Rule/Case？
3. 当前 Canonical Owner 是谁？
4. 本文件是在 Own、Use、Bridge 还是 Integrate？
5. 修改是否会影响依赖它的其他文档？

> 所有权以 `00_system/ownership_matrix.md` 为唯一台账。若发现冲突，先修正 Ownership Matrix，再改正文。

---

## 4. 知识产品类型

正式区分以下产品，不得把所有内容都命名为“方法论手册”：

| 类型 | 核心问题 | 典型稳定性 |
|---|---|---|
| **Atlas (学科总图)** | 这门学科的世界长什么样？ | 很稳定 |
| **Topic Manual (专题手册)** | 单一机制为什么存在、怎样运转？ | 稳定 |
| **Bridge (桥梁手册)** | 两个专题在哪里交接、谁负责什么？ | 稳定 |
| **Integration (综合手册)** | 多个机制怎样共同完成一个过程？ | 稳定 |
| **Practice System (训练系统)** | 做题和考试时怎样判断与行动？ | 持续生长 |
| **Evidence Base (证据库)** | 哪些观察支持或反驳某条规则？ | 持续增长 |

> 新建稳定知识产品时必须遵守 `00_system/handbook_contract.md`。

---

## 5. 认知成熟度 (Rule Maturity)

内容成熟度与知识粒度是两条独立坐标：
- `O (Observation)`：原始观察
- `H (Hypothesis)`：假设
- `C (Candidate)`：候选规则
- `V (Validated)`：验证有效
- `K (Canonical)`：标准宿主定本
- `P (Published)`：发布状态
- `X (Rejected)`：否定废弃

> - 只有 `K` 可以作为其他正式规则的稳定依赖；
> - `V` 表示已有支持证据，但作用域或代价仍需继续校准；
> - `P` 是某个 `K` 内容的发布状态，不创造新的语义所有权；
> - `X` 必须保留拒绝理由和反例，避免未来重复提出同一错误规则。
>
> 完整晋升协议见 `00_system/evidence_promotion.md`。

---

## 6. Control Plane 规则

### 6.1 通用内核只维护一份
通用题目控制内核固定围绕九问：
1. **Target**：目标与得分要求是什么？
2. **Objects**：已知对象及其类型是什么？
3. **Constraints**：条件、边界和隐含限制是什么？
4. **Structure**：它属于什么结构或母题？
5. **Output Shape**：答案应具有什么形式、范围或量级？
6. **Candidate Paths**：有哪些候选路径，为什么选择当前路径？
7. **Risk Point**：哪一步最危险？
8. **Verification**：怎样尽早发现错误？
9. **Expression**：怎样形成最小完整得分链？

### 6.2 学科只维护 Adapter
- **数学一**：$\text{Object} \to \text{Structure} \to \text{Representation} \to \text{Transformation} \to \text{Invariant} \to \text{Target}$；
- **408**：$\text{Object} \to \text{State} \to \text{Event} \to \text{Rule} \to \text{New State} \to \text{Cost}$；
- **英语一**：$\text{Sentence Structure} \to \text{Reference} \to \text{Discourse Function} \to \text{Author Intent} \to \text{Evidence}$。

> Adapter 可以扩展通用内核，但不得复制整套通用协议。

---

## 7. Evidence 规则与安全脱敏

1. **原始观察**：原始 Observation 保留原话、日期、场景和题目标识，不做事后美化；
2. **行为诊断**：Diagnosis 必须翻译成可观察行为，禁止只写“粗心、状态差、感觉不好”；
3. **可证伪假设**：Hypothesis 必须可被新题反驳；
4. **明确代价**：Candidate Rule 必须声明适用范围、预期收益、额外成本和失效条件；
5. **独立测试**：Test 必须尽量使用独立新题或新考试场景；
6. **综合评估**：不能仅凭证据数量晋升，还要检查证据独立性、反例、时间成本和迁移性；
7. **Single Source of Truth**：晋升后规则移动到 Canonical Owner，原证据只保留 `promoted_to` 指针；同一规则不得同时存在于 `inbox`、`validated rules` 与专题手册中成为三份真相。
8. **安全去标识化 (De-identification)**：本仓库为公开仓库。进入版本控制的 Evidence 必须去除姓名、联系方式、账号、未公开试卷和其他敏感信息；无法安全去标识化的原始材料不得提交。

---

## 8. 变更与依赖检查 Protocol

修改母模型、术语定义、控制内核或 Canonical Rule 时：
1. 在 Ownership Matrix 中确认所有者；
2. 搜索所有 Used By / Depends On 文档；
3. 区分语义变化与措辞变化；
4. 语义变化必须同步检查 Bridge、Integration、学科 Adapter 和发布产物；
5. 记录仍未处理的依赖，不得假装全仓库已经一致。

> 禁止通过复制旧段落来“快速保持一致”。

---

## 9. 现有 LaTeX / PDF 的渐进式纳管原则

当前 `90_publish/` 中的 `.tex` / `.pdf` 是既有成果，Bootstrap 阶段不得为了目录整齐而批量搬迁。采用渐进式纳管：
1. 先登记产品类型、Scope、Owns、Uses 与成熟度；
2. 再识别重复与所有权冲突；
3. 只在有真实内容修改时迁移到目标目录；
4. 发布路径变化必须同时修正交叉引用与构建脚本；
5. PDF 只能由对应的 Canonical LaTeX 源生成，不接受手工修改 PDF。

---

## 10. 学科 README 驾驶舱契约

每个学科 README 是驾驶舱，不是静态文件列表，至少展示：
1. 学科研究对象与母问题；
2. Atlas / Topic / Bridge / Integration 地图；
3. 当前完成度与可信度；
4. 推荐学习顺序；
5. Control Adapter 与做题协议入口；
6. 最近晋升规则；
7. 未解决问题和所有权冲突；
8. 对应发布手册。

> 只有证据支持的信息才能进入“当前薄弱区域”，不得凭印象长期固化。

---

## 11. 提交前检查清单 (Pre-commit Checklist)

- [ ] Plane 与内容类型明确；
- [ ] 粒度与成熟度分别标注；
- [ ] Canonical Owner 唯一且已登记；
- [ ] 没有跨专题复制完整机制；
- [ ] Observation 未越级进入 Stable Core；
- [ ] 新规则附有证据、作用域、成本和反例记录；
- [ ] 依赖文档已检查；
- [ ] Markdown 与 LaTeX 没有形成双份真相；
- [ ] Evidence 已去标识化；
- [ ] 链接、术语和发布路径有效。
