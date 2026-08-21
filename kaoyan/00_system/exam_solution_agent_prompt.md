# 真题题解执行提示词

本文件是 `exam-solution` 场景的**执行提示词唯一 Owner**。你正在维护 I.P.A.R.A 考研真题的 Derived Solution Layer（派生题解层）。目标不是把旧网站解析重新排版，而是让每道题真正成为心智模型的运行样本。

## 任务目标

对指定年度/题号：

1. 只从 Canonical Exam Source 获取题面事实；
2. 定位对应 Subject / Topic / Bridge / Integration；
3. 读取该 Owner 的 Canonical Handbook；若存在当前问题族训练 Markdown，先读局部 Practice；只有确实需要跨多个训练专题的统一控制时，再补读 Subject Rules；
4. 把旧 `qNN_*.md` 当作 legacy derived reference，只用来比较答案与发现遗漏；
5. 独立求解；
6. 生成 `solutions/qNN.md`；
7. 做源题 / 模型 / 校验 / 压缩质量门；
8. 若暴露**疑似**模型缺口，先登记 Challenge；若已独立确认 Canonical Handbook 存在事实、机制或适用边界硬错误，则立即走 Stable Write 更新唯一 Owner，并重新验证受影响题解。无论哪种情况，都不得在题解正文里悄悄重定义 Handbook 机制。

具体写作合同由 [`exam_solution_authoring_spec.md`](exam_solution_authoring_spec.md) 统一拥有；学生学习责任、跨年度一致性、质量门与模型反馈闭环由 [`exam_solution_quality_assurance.md`](exam_solution_quality_assurance.md) 统一拥有。本文件只负责执行顺序，不复制第二套写作或 QA 规则。

## 必读上下文顺序

```text
AGENTS.md
-> CURRENT.md
-> agent_context_protocol.md
-> exam_solution_authoring_spec.md
-> exam_solution_quality_assurance.md
-> problem_solving_kernel.md
-> 对应 408 Course / Subject Atlas
-> 当前题真正调用的 Topic / Bridge / Integration Canonical .tex
-> 当前问题族训练 Markdown（若存在）
-> Subject Rules（仅在需要跨专题控制时）
-> 年度 *_正式版.md 对应题
-> legacy qNN_*.md
```

不要为了“全面”把所有 Handbook 一次性塞进上下文。按题读取最小但足够的 Owner。

## 解题时必须做的事

### 1. 模型锚点

写出：

- 这题真正属于哪个机制；
- 题面哪个信号触发它；
- 第一动作是什么。

### 2. 问题表征

把题面翻译为该学科的对象：

- DS：关系 / 表示 / workload / invariant / cost；
- CO：state / location / path / resource / timing / commit；
- OS：objects / relations / queues / event / mechanism / policy；
- NET：scope / name / state owner / event / transition / feedback / cost。

### 3. 关键决策

说明为什么走当前路径，尤其要排除最容易混淆的竞争路径。

### 4. 求解链

逐步推导。公式必须从对象、约束或不变量长出来，不用“记公式”代替机制。

### 5. 校验

给出尽量独立的检查：范围、数量级、结构不变量、守恒、单位、边界、反算等。

### 6. 压缩

压成：

```text
题目信号 -> 第一动作 -> 关键不变量 / 方程 -> 停止条件 / 检查
```

这条压缩必须带适用前提。

## 单项选择题写作要求

- 给最终答案；
- **固定保留** `模型锚点 / 解题链 / 选项判断 / 校验 / 压缩 / 易错边界` 六个一级结构，不因题目简单而合并标题；
- `模型锚点` 固定写清 `Topic / 题目信号 / 第一动作`；
- 主推理尽量控制在能复原机制的最短长度；
- 高混淆题解释错误选项偷换了什么；
- 不把四个选项都写成重复教材段落。

## 填空题写作要求

- 明确给出最终填写内容；
- **固定保留** `模型锚点 / 解题链 / 校验 / 压缩 / 易错边界` 五个一级结构；
- 不虚构 `选项判断`，也不为了形式统一强行增加综合题专用栏目；
- 数值、区间、表达式、矩阵等结果保留决定答案的关键中间量，并至少给出一个独立校验。

## 解答题 / 综合应用题写作要求

- **固定保留** `模型锚点 / 问题表征 / 关键决策 / 求解链 / 校验 / 压缩 / 易错边界` 七个一级结构；
- `模型锚点` 固定写清 `Topic / 题目信号 / 第一动作`；
- 按小问组织；
- 每一问明确输入状态与输出要求；
- 数值题写单位；
- 状态、地址、位宽、窗口、资源或矩阵题优先写状态表、字段预算或关键中间量；
- 算法题必须有正确性不变量与复杂度；
- 代码只表达题目合同，不补无关框架。

## Source 边界

- 不复制 legacy q 文件中的题面；
- 不把 OCR 错字带进新题解；
- 图中事实必须来自正式版题图；
- 正式版与 legacy 解析冲突时，先独立求解，再判断 legacy 是否错误；
- 不因旧答案存在就假定它正确。

## 批量格式质量门

批量生成时，**结构一致性与答案正确性同级**。题型、题号范围和完成覆盖必须从 Exam Profile / 年度 `exam.json` 读取，不能在通用合同里硬编码某一门考试的题号结构。写完一个 Subject 或一整年后，必须从目录视角再验一次，而不是只逐题自检：

```text
覆盖率
-> 头部元数据
-> 必需标题
-> 标题顺序
-> 模型锚点三要素
-> 答案 / 索引一致性
-> 链接完整性
-> 重复 Owner 检查
```

出现“某些题只有答案 + 解析”“选择题没有选项判断”“填空题没有明确填写结果”“解答题缺少关键决策”等情况时，视为**未完成**，必须先统一结构再交付。

可读性优先采用：短段落、状态表、对齐公式、事件时间线；禁止用长段落把对象、机制、计算和校验揉成一块。

## 批量策略

推荐顺序：

```text
选择一个题源质量高、年度元数据完整的校准年
-> 按 Subject + 题型批量处理
-> 高推理风险的解答题 / 综合题单独做深度 Gate
-> 校准稳定后再按目标年份顺序推进
```

同一 Subject 批量时，先读 Atlas/Rules；切 Topic 时再加载对应 Canonical `.tex`。具体 Subject 顺序服从当前 Course Atlas 与任务范围，不在通用合同里硬编码。不要一题一题重复读整门学科。

## 每题结束内部分类

不一定写进题解正文，但必须判断：

- `No Update`
- `Candidate Rule Evidence`
- `Handbook Challenge`
- `Bridge Evidence`

若只是证据不足的 Challenge，写入年度 `solutions/solution_review.md`，继续处理其余题；不要因为一个局部疑点停止整批。

若已能确认 Canonical Handbook 存在事实、机制或适用边界硬错误，则不能把它永久降格为 `Challenge`：先排除 Source/legacy 问题，再按 Stable Write 更新唯一 Handbook Owner，检查受影响 Rules / Bridge / Integration，并重新验证当前题与受影响旧题解。规则技巧仍须走 Evidence Promotion，二者不得混为一谈。
