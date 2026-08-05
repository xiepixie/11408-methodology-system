# 规则晋升与证据链协议 (evidence_promotion.md)

> **核心原则**：做题感悟不能直接写入正式方法论。做题感受（Observation）只是一条原始数据，并非规则（Rule）。必须经过诊断、假设、候选规则提炼与实战测试后，才能按证据链规则晋升。

---

## 一、 认知规则成熟度六阶段流水线 (Rule Maturity Pipeline)

$$
\boxed{
\text{Stage 0: Observation}
\to
\text{Stage 1: Diagnosis}
\to
\text{Stage 2: Hypothesis}
\to
\text{Stage 3: Candidate}
\to
\text{Stage 4: Test}
\to
\text{Stage 5: Promotion}
}
$$

---

### Stage 0: Observation (原始感知)
- **定位**：做题现场的原始感受与自我陈述（原话保存，不删改）。
- **存放位置**：`80_evidence/inbox/YYYY-MM-DD_topic.md`
- **示例**：
  > “我觉得这道题很简单，所以直接在草稿纸上心算省略了中间步骤，最后因为符号看错扣了分。”

### Stage 1: Diagnosis (行为归因诊断)
- **定位**：剔除情绪，将口语化感受翻译为描述**具体操作/行为卡点**的语言。
- **转化标准**：必须说明 1. 发生在哪一步；2. 属于识别/路径/执行/检查/表达哪种断点。
- **示例**：
  > “识别出题型后直接进入心算执行，在执行阶段省略了中间状态记录（执行断点 + 检查断点）。”

### Stage 2: Hypothesis (提出可证伪假设)
- **定位**：提出具备明确适用条件与可否定反例的解法/防错假设。
- **示例**：
  > “并非计算能力不足，而是‘熟悉感引发的跳步’破坏了中间状态校验；如果在超过两步的代数变换中强行写出一个中间状态，计算错误率将显著下降。”

### Stage 3: Candidate Rule (提炼候选操作规则)
- **定位**：写成行动导向（Action-oriented）的规范操作指令，附带 YAML 元数据。
- **存放位置**：`80_evidence/candidate_rules/rule_xxx.md`
- **YAML 示例**：
  ```yaml
  rule: 出现两级以上代数变换或换元时，必须在草稿纸写出至少一个显式中间状态
  status: C
  scope: 数学一/高数/导数与积分
  evidence_count: 1
  counterexamples: 0
  created_at: 2026-08-05
  ```

### Stage 4: Test (多场景实战验证)
- **定位**：在新题与摸底测试中进行针对性验证：
  - 规则是否有效提高正确率？
  - 额外的时间成本是多少？
  - 是否存在失效的边缘反例（Counterexamples）？

### Stage 5: Promotion / Revise / Reject (规则终局)
- **Promote (晋升为 Validated / Canonical Core)**：
  - 条件：连续在 $\ge 3$ 次独立新题场景中验证有效，且没有致命反例。
  - 动作：将规则合并转移至对应学科的 `90_学科做题规则/` 或 `01_control/` 中，并在 `80_evidence/inbox` 中标注 `promoted_to: ...`。
- **Revise (修正范围)**：如果遇到局部反例，收窄 `scope` 适用条件后返回 Stage 3 继续测试。
- **Reject (废弃)**：经测试增加额外时间过多或无法提高正确率，移入 `80_evidence/rejected/` 封存。

---

## 二、 单一真理原则 (One Rule $\to$ One Canonical Location)

- 规则一旦被 **Promote** 到正式做题规则库（`90_学科做题规则/`）中，**必须从 `inbox/` 与 `candidate_rules/` 物理移动或更新为引用链接**。
- 严禁在 `inbox/` 保留一份、在 `candidate_rules/` 保留一份、在 `.tex` 中又抄写一份。全系统必须保持 **Single Source of Truth**。
