# 11408-methodology-system: 考研个人认知与考场决策系统

> **系统总宣告**：本系统不是静态讲义的堆砌，而是一个**可持续吸收学习、做题和考试反馈，并将其沉淀为稳定心智模型、解题控制规则与考场决策规则的个人认知系统**。
>
> 核心运作循环：
> \[
> \boxed{\text{Learn (学习反馈)}} \rightarrow \boxed{\text{Model (构建模型)}} \rightarrow \boxed{\text{Solve (解题控制)}} \rightarrow \boxed{\text{Test (实战测试)}} \rightarrow \boxed{\text{Reflect (反思诊断)}} \rightarrow \boxed{\text{Update (规则迭代)}}
> \]

---

## 🏛️ 系统架构地图 (Three Planes + Publication View)

```text
common/考研/
├── 00_system/               # [系统宪法] 架构定义、手册契约、唯一归属矩阵与规则晋升协议
├── 01_control/              # [控制平面] 通用解题内核 (Generic Kernel) 与考场决策 (Exam Control)
├── 10_数学一/               # [知识平面] 数学一：总图 -> 高数 -> 线代 -> 概率 -> 学科做题规则
├── 20_英语一/               # [知识平面] 英语一：总图 -> 阅读 -> 新题型 -> 翻译 -> 写作 -> 做题规则
├── 30_408/                  # [知识平面] 408 计算机综合：统一总图 -> 四科专题 -> 桥梁 -> 综合 -> 做题规则
├── 80_evidence/             # [学习/证据平面] 原始错题 Inbox -> 诊断 -> 候选规则 -> 验证/废弃库
└── 90_publish/              # [发布平面] 阶段性成熟手册的 LaTeX 源码与精排 PDF 产物
```

---

## 🚦 三大平面职责划分

```
[ Learning / Evidence Plane ] ──(反馈/晋升)──> [ Knowledge Plane ] ──(支撑)──> [ Control Plane ]
     (80_evidence/)                              (10_, 20_, 30_)                 (01_control/)
                                                         │
                                                    (发布导出)
                                                         ▼
                                               [ Publication Plane ]
                                                   (90_publish/)
```

1. **Knowledge Plane（知识平面｜Understand）**
   - **职责**：回答“世界到底怎么运转？”构建正确而有生成力的学科心智模型。
   - **结构**：`学科总图 Atlas` $\to$ `专题手册 Topic` $\to$ `桥梁手册 Bridge` $\to$ `综合手册 Integration`。

2. **Control Plane（控制平面｜Solve & Perform）**
   - **职责**：回答“面对题目与试卷时，人应该怎样行动？”
   - **微观控制（Question Control）**：断点识别（断点/路径/执行/检查/表达）与 通用解题内核（Generic Control Kernel + Subject Adapters）。
   - **宏观控制（Exam Control）**：时间预算、首轮冲刺/二轮回撤策略、检查预算与期望分最大化 $\max \sum E[\text{Score}_i]$。

3. **Learning / Evidence Plane（学习平面｜Learn）**
   - **职责**：回答“做错一道题后，系统如何变得更强？”
   - **流水线**：`Observation` $\to$ `Diagnosis` $\to$ `Hypothesis` $\to$ `Candidate` $\to$ `Test` $\to$ `Promote/Revise/Reject`。

4. **Publication Plane（发布平面｜Publish View）**
   - **职责**：将 Markdown 层中成熟稳定（`status: K/Published`）的 Working Knowledge 导出为 LaTeX/PDF 标准精排讲义。

---

## 📦 核心控制文件与契约入口

- 📜 [系统架构说明 (`00_system/architecture.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/00_system/architecture.md)
- 📝 [手册写作契约 (`00_system/handbook_contract.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/00_system/handbook_contract.md)
- 🗺️ [概念唯一归属矩阵 (`00_system/ownership_matrix.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/00_system/ownership_matrix.md)
- 🔄 [规则晋升协议 (`00_system/evidence_promotion.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/00_system/evidence_promotion.md)
- ⚡ [通用解题内核与适配器 (`01_control/problem_solving_kernel.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/01_control/problem_solving_kernel.md)

---

## 🎯 学科驾驶舱 (Subject Cockpits)

- 🧮 [数学一驾驶舱 (`10_数学一/README.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/10_%E6%95%B0%E5%AD%A6%E4%B8%80/README.md)
- 🇬🇧 [英语一驾驶舱 (`20_英语一/README.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/20_%E8%8B%B1%E8%AF%AD%E4%B8%80/README.md)
- 💻 [408 计算机综合驾驶舱 (`30_408/README.md`)](file:///Users/xpx/Library/Mobile%20Documents/iCloud~md~obsidian/Documents/xpx/Documents/I.P.A.R.A/%E5%B7%A5%E4%BD%9C%E9%A2%86%E5%9F%9F/%E8%B5%84%E6%BA%90/common/%E8%80%83%E7%A0%94/30_408/README.md)
