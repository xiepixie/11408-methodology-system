# I.P.A.R.A LaTeX Design System

> **Canonical Owner**：本文件拥有 `common/` 全局 LaTeX Design System 的**技术架构、依赖边界、Document Family / Profile / Variant、Semantic API、页面状态、兼容与迁移策略**。
>
> **Scope**：覆盖 `common/ipara.sty`、`common/templates/`、`common/topics/`、`common/考研/` 及未来所有共享 LaTeX family。子目录可以拥有自己的内容/排版细则，但不得重新定义本文件已经拥有的全局架构。
>
> **不拥有**：具体某一领域的知识结构与业务语义。例如考研 Handbook 的认知结构、物理身份、图表几何和发布规则仍由 `common/考研/00_system/` 下对应合同拥有。
>
> **Research Log**：开源项目源码证据、文件位置和 Source-to-IPARA 映射见 [`reference_pool.md`](reference_pool.md)。Research Log 不是契约 Owner。
>
> **研究快照**：2026-08-11。外部版本号不是长期契约；任何依赖进入 Core 前必须重新验证当前 TeX Live、许可证和 regression specimen。

---

## 1. 总架构：一个 Design System，三个 Document Family

I.P.A.R.A 不采用“每类文档一套独立视觉系统”，也不采用“一套万能页面强迫所有文档长得一样”。

长期结构固定为：

```text
One Design Language
        +
Three Document Families
        +
Small, explicit Profiles / Variants
```

```text
I.P.A.R.A LaTeX
├── Core
│   ├── typography
│   ├── design tokens
│   ├── semantic primitives
│   ├── table / code / diagram primitives
│   └── localization / configuration
│
├── Handbook Family
│   ├── profile=standard
│   └── profile=margin
│
├── Lesson Family
│   ├── variant=student
│   └── variant=teacher
│
└── Exam Family
    ├── variant=paper
    └── variant=solution
```

Atlas Poster / standalone poster 暂不成为第四 Family。先使用 Core + 局部 TikZ/poster adapter；只有出现稳定、重复、独立的页面语法后才晋升。

### 1.1 Family 是页面任务，不是皮肤

| Family | 页面任务 | 不应被迫承担 |
|---|---|---|
| **Handbook** | 连续阅读、机制解释、章节导航、semantic margin、宽内容逃逸 | 大面积答题留白、课堂观察 |
| **Lesson** | 教学交互、学生练习、教师路线、Checkpoint、答题空间 | 长篇出版级章节 machinery |
| **Exam** | 题号、分值、答题空间、paper/solution 单源切换、评分点 | 课前唤醒、学生画像、长篇边栏解释 |

因此全局原则是：

$$
\boxed{\text{Shared Visual Language} + \text{Different Interaction Grammar}}
$$

---

## 2. 技术地基：只锁 KOMA-Script + CTeX

### 2.1 目标继承关系

```text
ipara-handbook.cls
    -> scrartcl
    -> ctex package

ipara-lesson.cls
    -> scrartcl
    -> ctex package

ipara-exam.cls
    -> scrartcl
    -> ctex package
```

这里的 `ctex` 是中文基础设施，不要求把 `ctexbook/ctexart` 当最终 base class。**Handbook 采用 `scrartcl` 是由当前 Canonical 物理身份决定的**：Topic / Bridge / Integration 都是独立小册，`section` 是正文顶层，不应该为了“像一本书”人为制造空 chapter。未来如果出现“把多册 Canonical Handbook 组装成一本完整出版卷”的真实需求，再单独建立 Volume / Publication Assembly 层并评估 `scrbook`；不要让装订视图反向改变单册 Canonical Source。

### 2.2 唯一 Owner 分工

```text
KOMA-Script
├── class mechanics
├── chapter / section mechanics
├── page styles
├── marks / headers / footers
├── TOC mechanics
└── duplex / layout public API

CTeX
├── Chinese language conventions
├── CJK infrastructure
├── Chinese heading / name conventions
└── Chinese punctuation / spacing infrastructure

I.P.A.R.A Core
├── portable typography baseline
├── design tokens
├── semantic document API
├── shared table / code / diagram primitives
└── configuration registry

I.P.A.R.A Family
├── page interaction grammar
├── profiles / variants
└── family-specific components
```

**禁止第二 Owner。** KOMA 已经拥有的 chapter/section/header/TOC machinery，I.P.A.R.A 只通过 public API 配置，不再平行维护另一套长期实现。

### 2.3 `fancyhdr` 的定位

现有文件可以继续使用 `fancyhdr` 兼容运行；它不是长期 Family mechanics。正式 KOMA-based class 应优先使用 `scrlayer-scrpage`。

---

## 3. 开源项目采用等级

外部项目只允许落入三种角色：

```text
A. Direct Dependency
   使用稳定 public API，让它拥有底层 machinery

B. Mechanism Reference
   学习状态模型/算法，用 IPARA 语义重新实现

C. Visual / Architecture Reference
   只借信息层级、工程组织和视觉原则
```

默认优先顺序：

```text
stable public package API
-> mechanism reimplementation
-> visual reference
-> template-level runtime dependency only with explicit evidence
```

当前结论：

| 项目 | 等级 | IPARA 取用 |
|---|---|---|
| KOMA-Script | **A** | `scrbook/scrartcl`、section/chapter API、`scrlayer-scrpage`、TOC/marks/duplex |
| CTeX | **A** | 中文语言、CJK、中文标题/名称/标点基础设施 |
| kaobook | **B** | main/margin/wide/fullwidth 的页面状态机、odd/even 宽内容逻辑 |
| minimalist / simplivre | **B/C** | Core+Profile 架构、stream margin navigation、中文 course-note typography |
| ElegantBook | **B** | semantic-object factory、numbered/starred/renderer 分离、answer/noanswer 思路 |
| whatsnote | **B** | `expl3/l3keys`、内部模块化、specimen/l3build/CI 思路 |
| easybook | **C** | named style registry、中文配置 API 组织 |
| keytheorems | **Candidate A** | theorem identity/numbering/reference；先实验，不锁依赖 |
| memoir | **C** | 传统数学书排版 regression benchmark |
| xtufte | **C** | Unicode/Tufte margin 视觉 benchmark |
| ClassicThesis | **C** | typography restraint、标题比例、留白与 rule reference |

逐源码证据见 [`reference_pool.md`](reference_pool.md)。

---

## 4. 目标物理结构：公开入口少，内部可以模块化

长期目标：

```text
common/latex/
├── README.md                 # 本合同：全局 Canonical Owner
├── reference_pool.md         # Research Log
│
├── ipara-core.sty            # public
├── ipara-handbook.cls        # public
├── ipara-lesson.cls          # public
├── ipara-exam.cls            # public
│
└── ipara/                    # internal implementation
    ├── typography.code.tex
    ├── tokens.code.tex
    ├── semantic.code.tex
    ├── table.code.tex
    ├── diagram.code.tex
    ├── handbook-margin.code.tex
    ├── lesson-components.code.tex
    └── exam-components.code.tex
```

**作者稳定入口最多 4 个代码文件。** `ipara/*.code.tex` 是内部模块，不允许 Topic、课次或试卷直接 `\input`。

这解决两个冲突：

```text
“样式不能太分散”
        -> public surface small

“一个 sty 不能无限膨胀”
        -> internal implementation modular
```

---

## 5. 当前兼容层与 Prototype

当前真实资产：

```text
common/ipara.sty
    = 已成熟的 Lesson/Teaching implementation + compatibility surface

common/templates/
    = 当前 Teaching templates

common/考研/ipara-handbook.sty
    = Handbook Prototype / Transition Implementation
```

它们继续工作，不立即删除、不批量迁移。

### 5.1 `common/ipara.sty`

其中 teacher/student、答题区、课前唤醒、变式、Checkpoint、教师双栏、课堂观察等属于 **Lesson Family**，不应全部上移进 Core。

### 5.2 `common/考研/ipara-handbook.sty`

它已经证明 portable fonts、表格、基础语义框和 TikZ baseline 可行，但它不是长期全局 Owner，也不应继续承载新的 Family architecture。正式 class 通过 regression gate 前可以继续作为考研 Handbook 的过渡实现。

---

## 6. Semantic API：内容声明意义，Profile 决定外观

Canonical `.tex` 不应该稳定绑定到视觉皮肤：

```text
greenbox
bluebox
shadowbox
kaobox
streambox
```

长期原则：

$$
\boxed{\text{Content declares meaning; profile decides appearance.}}
$$

例如正文应该趋向：

```latex
\begin{mentalmodel}{局部线性化}
...
\end{mentalmodel}

\begin{criterion}{中值定理调用条件}
...
\end{criterion}

\begin{boundary}{可导 $\neq$ 导函数连续}
...
\end{boundary}
```

而不是声明“我要一个绿色盒子”。

### 6.1 第一阶段只建立有真实证据的语义

全局 Core 不预造几十种环境。第一阶段候选：

| Semantic | 作用 |
|---|---|
| `mentalmodel` | 压缩一个可生成的核心理解 |
| `mechanism` | 解释对象如何运转 / 为什么有效 |
| `criterion` | 可执行、可判定的区分条件 |
| `boundary` | A≠B、适用边界、停止边界 |
| `example` | 机制的最小运行实例 |
| `warning` | 高概率误读、非法操作、失效条件 |

它们只是**渲染语义**，不会创造新的知识资产类型。具体领域可以进一步限制哪些 semantic 真正允许进入其 Canonical Source。

### 6.2 暂不晋升的语义

Connection、Extension、Anti-Bridge、Rule、Source、Owner、Cost 等先用正文/列表/表格/已有 semantic 表达。只有出现稳定重复的渲染需求再晋升。

### 6.3 Theory object ≠ Renderer

需要严格编号和引用的数学 theorem object，不应让 `tcolorbox` 顺便成为 counter/reference engine。

候选分层：

```text
theorem machinery
        ↓
semantic mathematical object
        ↓
optional renderer (e.g. tcolorbox)
```

`keytheorems` 是当前候选 machinery，尚未锁为依赖。

---

## 7. Handbook Family：两个 Profile，不造两套正文

V1 只允许：

```text
profile=standard
profile=margin
```

### 7.1 `standard`

```text
single main reading block
ordinary body uses stable full reading width
semantic components stay in normal flow
```

适合：短 Bridge、公式/表格/图形密度高、无需持续 margin 的正文。

**当前实现状态（2026-08-11）**：Real Topic Gate 发现 KOMA `DIV=11` 给出的约 `152.7mm` 主栏对数学 Handbook 偏窄；Topic04 的正常六阶段母模型在旧约 `174.4mm` 版心中可容纳，却在 152.7mm 下新增约 40.9pt 溢出。因此 experimental `standard` 改为 `170mm` 主栏。重新编译 Topic04 后，不再产生任何新诊断，只剩原 Canonical 自己已有的 4 处表格宽度债务。`170mm` 仍是 Real-Topic-backed Candidate，不是冻结 Token。

### 7.2 `margin`

```text
main reading column
+ outer semantic margin
+ local wide-content escape
```

适合：成熟 Topic、长篇解释、交叉引用/局部导航/Boundary 指针较多的技术手册。

**当前实现状态（2026-08-11）**：`ipara-handbook.cls` 已实现 synthetic `profile=margin`，并与 `profile=standard` 共用同一 `specimens/handbook-body.tex` 通过 XeLaTeX 零诊断回归。真实 Topic04 又完成了一轮布局迁移：三张跨页固定宽表改为 `handbooklongtable + Y`，附录表改为 `handbooktable + Y`，两条六阶段硬编码单行链改为 `processchain`，必要英文复合词只在语义安全的 `/` 处增加断点。迁移后 Canonical Prototype、KOMA standard、KOMA margin 三路均达到 0 Warning / Overfull / Underfull / Undefined / Error，因此 **Margin Real Topic Layout Gate 已通过**。当前 `116mm main + 5mm gap + 39mm semantic margin` 仍只是实验候选，因为下一道 Gate 不再是“能否装下”，而是 semantic margin 是否真的提升阅读与检索。

### 7.3 Margin 的硬边界

Margin 可以承载：

- section/local navigation；
- 极短定义提醒；
- Owner / Uses / See also；
- 简短 Boundary / Warning；
- 小图、小表、caption；
- 符号回忆；
- Source / Extension 指针。

Margin 不能拥有逻辑主链：

- 核心对象第一次定义；
- 定理完整条件；
- 多步推导；
- 下一段理解必须依赖的信息；
- Canonical mechanism 唯一解释。

验收判据：

> **把 margin 临时遮住，MainText 仍必须是一条完整可读、逻辑闭合的推理链。**

---

## 8. Handbook 页面状态协议

借 kaobook 的机制思想，不继承它的固定几何和皮肤。

### 8.1 `main`

默认阅读状态：

```text
main text | gap | semantic margin
```

在 `standard` profile 中没有持续 margin，`main` 等价于普通正文状态。

### 8.2 `widecontent`

用于：

- 大表；
- 长公式；
- 宽流程图；
- 需要 main + margin 可用包络的比较结构。

目标 API：

```latex
\begin{widecontent}
...
\end{widecontent}
```

在 `profile=standard` 下必须安全退化为 ordinary body width，从而同一 Canonical Source 不需要维护两份。

### 8.3 `fullwidth`

用于真正特殊的全景对象：章节总图、大型 Integration overview、特殊页面。V1 不鼓励频繁使用；普通宽表/宽图优先 `widecontent`。

### 8.4 禁止用缩放冒充布局

```text
先减语义密度
-> 修列/节点职责
-> widecontent
-> 必要时拆图/拆表
-> 最后才整体缩放
```

`\resizebox{\linewidth}{!}{...}` 不是主策略。

---

## 9. Design Tokens：全系统只有一个 Owner

Core 将来唯一拥有：

```text
Typography tokens
Color tokens
Spacing tokens
Rule weights
Radius
Table rhythm
Code typography
Base TikZ node/edge/label vocabulary
```

Family 只能：

- 选择 token；
- 在明确作用域调整密度；
- 增加场景特有组件。

Family 不重新定义第二套字体、颜色或基础 table/diagram vocabulary。

具体数值必须由相应的全局/领域视觉规范经过 specimen 后确定；不能因为某个开源模板用了某组数值就直接进入 Core。

---

## 10. Family API 边界

### 10.1 Handbook owns

```text
section hierarchy
TOC / local navigation
header / footer
profile=standard|margin
main / widecontent / fullwidth
margin note / margin figure / margin table
Handbook semantic renderers
```

### 10.2 Lesson owns

现有 `common/ipara.sty` 中以下属于 Lesson：

```text
student / teacher
answer grid / blank
problem header
multiple-choice layout
prehint
variant practice
teacher route
checkpoint
live observation
teacher columns
```

### 10.3 Exam owns

```text
paper / solution
exam metadata
question / subquestion
score
choice layout
answer area
solution
marking point
page allocation
```

Exam 不继承 Lesson 全部组件，只共享 Core。

---

## 11. 配置接口：key-value，不扩散 public booleans

长期公开配置使用 `expl3/l3keys` 或等价稳定 key-value 接口。

目标形态：

```latex
\documentclass[
  profile=margin,
  twoside=true
]{ipara-handbook}
```

```latex
\documentclass[
  variant=teacher
]{ipara-lesson}
```

```latex
\documentclass[
  variant=solution
]{ipara-exam}
```

避免公共 API 无限增长：

```text
\ifteacher
\ifstudent
\ifmargin
\ifsolution
\ifprint
...
```

布尔值可以存在内部，不应该成为分散的作者语言。

---

## 12. 字体与编译器边界

Canonical baseline：

- 官方发布引擎当前仍以 XeLaTeX 为准；
- Core 不要求 shell escape；
- 默认字体必须能在标准 TeX Live 环境中解析；
- 机器本地字体可以实验，但不能成为 Canonical 默认依赖。

当前 Fandol + TeX Gyre 的 portable baseline 可以继续作为实验基线，最终 token 数值由 specimen 决定。

LuaLaTeX 可以作为未来 regression target，例如测试 `lua-widow-control` 和更高级 Unicode/microtypography；在发布链正式迁移前，不把“Lua 下可编”写成 Canonical 已支持。

---

## 13. Dependency Policy

### 13.1 Core 包进入条件

进入 Core 的 package 至少要满足：

1. 提供难以合理自行维护的基础 machinery；
2. 被多个 Family 真实共享，或拥有一个 Family 的关键底层能力；
3. 当前 TeX Live 稳定可获得；
4. 不要求额外外部运行时 / shell escape；
5. 与 XeLaTeX + CTeX + KOMA + specimen 通过回归。

### 13.2 不因为“漂亮模板用了”就引入

`kaobook / minimalist / ElegantBook / whatsnote / easybook` 默认不是 runtime dependency。

Handbook 的跨页表是一个已经被 Real Topic 证明的具体例外：旧 Canonical 中大量 `longtable` 用“固定列宽之和 = \linewidth”的写法，漏算 `\tabcolsep`，Topic04 原稿因此稳定出现 18pt/8pt 一类 Overfull。`ipara-handbook.cls` 现阶段引入薄依赖 `xltabular`，并提供 `handbooklongtable`，让跨页表继续使用 `X/Y` 自适应解释列，而不是逐册重算厘米数。若后续 regression 暴露冲突，再降级为 Candidate；当前 synthetic standard/margin 均已通过。

### 13.3 许可证边界

直接复制外部实现前必须确认：

- 源文件许可证；
- 版权/许可证保留义务；
- 修改与分发条件；
- 是否真的比“使用 public API / 按机制重实现”更值得。

默认：

> **依赖 public API；机制自己实现；视觉只参考。**

---

## 14. Regression Specimens：不是“编译过”就算稳定

最终至少维护：

```text
common/latex/specimens/
├── handbook.tex
├── lesson.tex
└── exam.tex
```

Handbook specimen 同一语义源必须能覆盖：

```text
handbook-standard
handbook-margin
```

### 14.1 Handbook 必测

- 中文 + English + 数学 + code；
- section hierarchy / TOC；
- long equation；
- ordinary table / 5-column boundary table / longtable；
- TikZ flow；
- semantic objects；
- margin note / figure；
- `widecontent`；
- odd/even pages；
- cross-reference；
- heading near page bottom / widow-orphan 边界。

### 14.2 Lesson 必测

- student / teacher；
- answer grid；
- multiple-choice layout；
- teacher two-column；
- Checkpoint；
- black-and-white print readability。

### 14.3 Exam 必测

- paper / solution single source；
- score + question numbering；
- choice + free response；
- answer area；
- solution / marking point visibility；
- predictable page allocation。

### 14.4 Regression Gate

```text
XeLaTeX compile success
0 fatal error
0 missing font
0 undefined reference after required passes
no unexplained overfull box
public API specimen unchanged unless migration is intentional
```

`l3build/CI` 在 specimen 稳定后再引入，不为了“有 CI”先增加空工程层。

---

## 15. Migration：Forward Standard + Compatibility Layer

### Phase 0 — 当前

```text
common/ipara.sty
    = existing Lesson implementation + compatibility

common/考研/ipara-handbook.sty
    = Handbook Prototype
```

- 不批量迁旧文档；
- Prototype 只修真实 bug，不继续承载新的全局 architecture；
- 先锁 Owner 与 specimen。

### Phase 1 — Core extraction

建立：

```text
common/latex/ipara-core.sty
```

第一轮只抽真正共享的：

- portable fonts；
- tokens；
- base table columns；
- code；
- base TikZ；
- semantic renderer primitives。

**禁止顺手重写 Lesson 业务组件。**

### Phase 2 — Handbook class

```text
ipara-handbook.cls -> scrartcl + ctex
```

实现顺序仍是 `profile=standard` → `profile=margin`；该顺序已经在 synthetic engine experiment 中实际执行，而不是并行开发。

**当前状态**：两 Profile 已进入 experimental class，并且同一 semantic body 的双 Profile XeLaTeX 回归均为零诊断。真实高数 Topic04 已完成第一轮布局迁移：跨页表、附录表和六阶段过程链均改用 forward Family API，迁移后 Canonical Prototype、KOMA standard、KOMA margin 三路全部零诊断。因此 Standard / Margin 的 **Real Topic Layout Gate 均已通过**。Phase 2 仍未结束：下一道 Margin Gate 改为验证 semantic margin 的信息价值、奇偶页密度与 MainText 独立闭合，而不是继续证明几何可容纳性。只有这道信息架构 Gate 通过，才考虑把 margin 从 experimental profile 提升为 Canonical 可选 profile。

### Phase 3 — Lesson class

从现有 `common/ipara.sty` 提取共享 Core，再组织 `ipara-lesson.cls`。旧调用必须有兼容期，不要求 `common/topics/` 历史文档立即迁移。

### Phase 4 — Exam class

从真实试卷提取 Exam API，不从 Lesson components 猜需求。

### Phase 5 — l3build / CI

三 Family specimen 稳定后，再纳入自动回归。

---

## 16. 旧文件迁移触发条件

旧 `.tex` 只在以下情况迁移：

1. 本来就发生较大正文修订；
2. 旧 preamble 产生真实包冲突；
3. 字体不可复现；
4. 表格/图形确实需要新 `widecontent`；
5. 新 Family API 能显著删除重复实现。

**“新版更漂亮”本身不是迁移理由。**

---

## 17. 暂不锁定

在 specimen 证据出现前，不锁：

- margin 固定厘米宽度；
- `keytheorems` 为正式依赖；
- `scrlayer-notecolumn` 为 margin engine；
- LuaLaTeX 为正式发布引擎；
- Poster 为第四 Family；
- screen / print 为新的公开 Profile；
- 大量预造 semantic environments。

这些保持 Candidate。

---

## 18. 第一轮实现验收 Gate

### G1 — Ownership

- Core / Handbook / Lesson / Exam 无重复 Owner；
- Topic/lesson/exam 不直接依赖内部 `.code.tex`；
- semantic content 与 renderer 分离。

### G2 — Portability

- 标准 TeX Live + XeLaTeX 可编；
- 无机器私有字体前提；
- 无 shell escape 前提。

### G3 — Handbook Standard

- `scrartcl + ctex + ipara-core` 编译稳定；
- section hierarchy / TOC / headers / references / tables / TikZ 无冲突。

### G4 — Handbook Margin

- odd/even margin 正确；
- MainText 遮掉 margin 后仍逻辑完整；
- `widecontent` 能解决大表/大图，不靠缩字；
- margin object 不与正文/footer 冲突。

### G5 — Existing Lesson Regression

- 现有 teacher/student 样例在兼容层下继续编译；
- Core extraction 不改变教学语义。

### G6 — Exam Single Source

- 同一题源生成 paper/solution；
- 不维护学生卷与答案卷两份内容源。

### G7 — Maintenance

- Public API 文件保持少；
- 每个内部 module 能说明唯一职责；
- 同一能力不会因来自不同开源项目而出现两个实现。

---

## 19. 下一步：从 Real Topic Layout Gate 进入 Semantic-Margin Gate

不再做 kaobook / simplivre / memoir 三套整书 Prototype。

Synthetic engine gate 与 Topic04 real-layout gate 现在都已经完成：

```text
KOMA + CTeX + IPARA Core
        ↓
profile=standard / profile=margin
        ↓
same semantic body clean
        ↓
real Topic04 layout migration
        ↓
Canonical Prototype / standard / margin all clean
```

这轮真实迁移没有改知识语义，只把旧版式假设替换成 `handbooklongtable`、`handbooktable`、`processchain` 与少量合法断点。它证明了 116mm margin 主栏在正确 structural API 下可以承载真实数学正文，也证明旧固定列宽和单行 boxed process 才是主要机械故障源。

下一步仍使用 Topic04，但实验问题已经变化：**margin 是否值得存在？** 只增加少量真正 supplementary 的 `semanticmargin` 对象，并验证：

- 遮住 margin 后 MainText 是否仍完整闭合；
- margin 是否降低 Owner / Uses / Boundary / local navigation 的检索成本；
- odd/even 页面位置与连续密度是否自然；
- margin 是否挤压正文却没有产生相应信息收益；
- standard 与 margin 两 Profile 是否仍共享同一 Canonical knowledge source；
- 三路编译继续保持零 unexplained diagnostics。

只有 Semantic-Margin Gate 通过，才考虑把 `profile=margin` 从 experimental 提升为 Canonical 可选 Profile；在此之前 `profile=standard` 仍是安全默认。

---

## 20. 一句话架构

$$
\boxed{
\text{KOMA owns mechanics}
+\text{CTeX owns Chinese infrastructure}
+\text{I.P.A.R.A owns semantics and profiles}
}
$$

外部项目负责告诉我们成熟机制在哪里；I.P.A.R.A 只维护自己的 Design Language，不重新发明排版引擎，也不把内容语义绑定到某一套视觉皮肤。
