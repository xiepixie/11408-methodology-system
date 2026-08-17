# 408 Exam Archive

本目录保存 2009～2026 年 408 真题的抓取原料与正式可编辑版本。

## 目录约定

每个年度目录通常包含：

```text
YYYY年真题/
├── q01_*.md ... q47_*.md   # 网页/初步提取原料，保留答案解析供参考
├── assets/                 # 题图 / Semantic SVG；已升级图可含 light/ 亮色版本
├── solutions/              # Derived Solution Layer；不拥有题面或知识机制
│   ├── q01.md ... q47.md
│   ├── README.md
│   └── solution_review.md
├── YYYY 年全国硕士研究生招生考试.md   # Canonical Exam Source，干净题面
└── exam.json               # 年度机器元数据
```

2025 年高清精校版现已并入本 Archive，`2025年真题/2025 年全国硕士研究生招生考试.md` 即 Canonical Source；原 `kaoyan/80_evidence/inbox/2025_408真题/` 只保留兼容指针，不再拥有题面。

## 正式版边界

正式版统一执行 [`../../00_system/exam_source_agent_prompt.md`](../../00_system/exam_source_agent_prompt.md) + [`../../00_system/exam_source_conversion_spec.md`](../../00_system/exam_source_conversion_spec.md)。这套流程与后续数学一真题共用；408 自己的题号/学科结构只由 `../../00_system/exam_profiles/408.json` 负责：

- 正文使用 Markdown / LaTeX / fenced code；
- 题图优先使用可编辑 SVG；
- 不混入答案、解析、OCR 日志和历史争议；
- 明显 OCR/排版错误直接恢复；
- 仍需高清原卷确认的项目统一记录在 `00_408真题可疑点与复核清单.md`。

## 408 题号路由

客观题长期稳定：

- Q1～Q11：数据结构
- Q12～Q22：计算机组成原理
- Q23～Q32：操作系统
- Q33～Q40：计算机网络

综合应用题通常为 Q41～42 数据结构、Q43～44 计组、Q45～46 OS、Q47 网络，但 **2016 年存在历史例外**。机器路由统一读取 [`../../00_system/exam_profiles/408.json`](../../00_system/exam_profiles/408.json)，不得只凭文件名硬编码。

## Derived Solution Layer

题解统一执行：

- [`../../00_system/exam_solution_agent_prompt.md`](../../00_system/exam_solution_agent_prompt.md)：Agent 执行顺序与最小 Context；
- [`../../00_system/exam_solution_authoring_spec.md`](../../00_system/exam_solution_authoring_spec.md)：题解生成结构与知识 Ownership；
- [`../../00_system/exam_solution_quality_assurance.md`](../../00_system/exam_solution_quality_assurance.md)：学生学习责任、跨年度风格一致性、质量 Gate 与 Model Feedback Closure。

当前 2017～2026 共 10 个年度已经建立完整 Derived Solution Layer，共 470 题。Q1～Q40 固定为：

```text
Model Anchor -> 解题链 -> 选项判断 -> Verification -> Compression -> 易错边界
```

Q41～Q47 固定为：

```text
Model Anchor -> Problem Representation -> Decision Points -> Solution Chain
-> Verification -> Compression -> 易错边界
```

算法题的 `Why Correct / Complexity` 只能作为 `Solution Chain` 内部子节，不新增平行 H2；Source Gap、Legacy Difference 与 Candidate Evidence 统一进入年度 `solution_review.md`。

题解的目标不是“把标准答案写长”，而是让学生能够复原：

```text
题目信号 -> 第一动作 -> 表征 -> 决策 -> 机制/状态推进 -> 独立校验 -> 下次调用
```

学习时推荐先独立作答，再逐层揭示 `Model Anchor / Representation / Decision / Solution / Verification / Compression`。如果遮住答案后仍不能复原第一动作和关键转折，就不能只因为“看懂解析”而视为掌握。

## 题解 QA

`python3 00_system/cognitive_system.py check` 已对已建立的 408 `solutions/` 增加 `E-EXAM-SOLUTION-*` 硬检查，覆盖：47/47 Coverage、年度 README/review、Frontmatter、Exam Profile 路由、Q1～Q40 答案一致性、Source/Legacy 链接、固定 H2、题目信号与第一动作。

机器只保护可确定的文件事实；推理正确性、Verification 独立性、Model Owner 是否正确、Handbook 是否需要修订仍必须经过内容审阅。跨年 QA 记录见 [`../../80_evidence/review_log/2026-08-16_408真题题解跨年质量审阅_v1.md`](../../80_evidence/review_log/2026-08-16_408真题题解跨年质量审阅_v1.md)。

若题解发现的只是可复用做题动作，进入 Candidate Rule Evidence；若独立确认 Canonical Handbook 存在事实、机制或适用边界硬错误，则在同一维护闭环中 Stable Write 修正唯一 Owner，并重新验证受影响题解，不能为了“证据晋升纪律”继续传播已知错误。
