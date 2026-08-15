# I.P.A.R.A LaTeX Open-Source Reference Pool

> **性质**：Research Log，不是 Design System 契约。
>
> **Canonical 决策**：全局技术 Owner 是 [`README.md`](README.md)。本文件只记录：**哪个开源项目的哪个源码面解决了什么问题，I.P.A.R.A 以 Direct Dependency / Mechanism Reference / Visual Reference 哪种方式利用。**
>
> **快照日期**：2026-08-11。版本号与外部源码位置仅用于复现本轮判断；真正进入依赖前必须重新确认当前版本、许可证和 regression specimen。

---

## 1. 采用等级

| 等级 | 含义 | 动作 |
|---|---|---|
| **A — Direct Dependency** | 使用稳定 public API，让外部包拥有底层 machinery | 声明依赖，不复制内部实现 |
| **B — Mechanism Reference** | 机制值得复用，但不值得绑定整个模板 | 抽状态模型，用 IPARA API 重实现 |
| **C — Visual / Architecture Reference** | 主要价值是信息层级、视觉或工程组织 | 借原则和测试标准，不形成 runtime dependency |

默认顺序：

```text
stable public package API
-> mechanism reimplementation
-> visual reference
-> template-level dependency only with explicit evidence
```

---

## 2. KOMA-Script — A

### 2.1 代码面

本机 TeX Live 2026 可定位：

```text
.../tex/latex/koma-script/scrbook.cls
.../tex/latex/koma-script/scrlayer-scrpage.sty
```

源码/public API 中本轮直接核到：

```latex
\RedeclareSectionCommand
\RedeclareSectionCommands
\newpairofpagestyles
\renewpairofpagestyles
```

### 2.2 我们拿什么

```text
scrbook / scrartcl
chapter / section public mechanics
scrlayer-scrpage
marks / header / footer
TOC / duplex behavior
KOMA font/page-style configuration
Ifthispageodd / addmargin* for duplex-aware local width states
```

本地源码进一步确认：`scrbook.cls` 的 `addmargin*` 会自动按 odd/even page 镜像左右 margin，并在该环境跨页时主动警告潜在错误边距。这正适合 V1 `widecontent`：把它定义成**局部宽内容状态**，而不是多页布局系统。

### 2.3 不拿什么

- 不复制 `scrbook.cls` 内部实现；
- 不再平行建设长期 `titlesec + fancyhdr + custom TOC` machinery。

### 2.4 Mapping

```text
KOMA -> document mechanics Owner
```

---

## 3. CTeX — A

### 3.1 代码面

本机 TeX Live 2026：

```text
.../tex/latex/ctex/ctex.sty
```

公共配置入口：

```latex
\ctexset
```

当前公开发行同时提供 class/package 形态，并以 XeLaTeX/LuaLaTeX 为主要 Unicode 中文引擎。

### 3.2 我们拿什么

```text
Chinese language conventions
CJK infrastructure
Chinese heading/name conventions
Chinese punctuation/spacing infrastructure
```

### 3.3 本轮源码与 specimen 结论

`ctex.sty` 源码表明：当 `heading=true` 且 base class 不是标准 `book/article/report` 时，CTeX 会显式警告 heading 可能不按预期工作。因此当前 Handbook class 采用：

```latex
\RequirePackage[UTF8,fontset=none,heading=false,scheme=chinese]{ctex}
```

这把 Owner 切开：

```text
CTeX -> Chinese infrastructure
KOMA -> chapter / section mechanics
```

该组合已经在 `profile=standard` 与 `profile=margin` 的同源 synthetic specimen 上通过两遍 XeLaTeX 零诊断回归，包括中文 TOC、页眉 marks、portable fonts、hyperref/bookmark。仍需 Real Topic Gate 验证真实长文密度，而不是继续把“组合兼容性”当成未实验假设。

### 3.4 Mapping

```text
CTeX -> Chinese infrastructure Owner
```

---

## 4. kaobook — B

### 4.1 源码面

官方仓库核心：

```text
kaobook.cls
kao.sty
```

`kaobook.cls` 的关键事实不是“有一套独立 book engine”，而是：

```text
base class = scrbook
+ kao.sty
```

并围绕文档生命周期切换页面状态：

```text
frontmatter -> wide
mainmatter  -> margin
backmatter  -> wide
```

章节实现大量利用 KOMA chapter/section/font public machinery。

`kao.sty` 里最值得拆的是：

```latex
\pagelayout{margin}
\pagelayout{wide}
\pagelayout{fullwidth}
```

以及由：

```text
textwidth + marginparsep + marginparwidth
```

形成的 `contentwidth` 思路，再配合：

```text
widepar
wideequation
fullwidthpar
odd/even page-aware addmargin
margin figure/table
sidenote/marginnote
```

### 4.2 我们拿什么

抽象成 IPARA 页面状态：

```text
main
widecontent
fullwidth
```

核心原则：宽公式/表/图优先**改变当前包络**，不是把整块文字缩小。

本轮实现没有复制 kaobook 的宽度代码，而是用 KOMA 自己的 `addmargin*` 实现 `widecontent`；双面镜像与跨页警告因此继续由 KOMA 拥有。

### 4.3 不拿什么

```text
kaobook fixed mm geometry
chapter TikZ skin
patch chain
whole dependency graph
private layout tricks
```

### 4.4 Mapping

```text
kaobook -> Handbook layout state machine reference
```

---

## 5. minimalist / simplivre — B/C

### 5.1 源码结构

公开仓库包含：

```text
minimalist.sty
minimalist-plain.sty
minimalist-default.sty
minimalist-flow.sty
minimalist-stream.sty
minimalist-classical.sty
minimalist-classicthesis.sty
minimart.cls
minimbook.cls
simplivre.cls
```

### 5.2 我们拿什么

**Profile 分层：** Core 与 `plain/flow/stream/...` 的分离验证了：

```text
Core + Family + Profile
```

比“一个巨大 sty 里到处 if”更可维护。

**stream：** 将导航编号退到 margin，让正文更安静。可用于 Handbook margin 中的：

```text
section id
local navigation
Criterion/Boundary pointer
Owner/Uses pointer
```

**flow：** course note 应形成连续故事，而不是每个组件都重新启动视觉层级。

### 5.3 不拿什么

- 不把多个 IPARA 认知类型合并成一个连续 counter；
- 不把 minimalist style files 变成 runtime dependency；
- simplivre 的额外字体要求不进入 Canonical portable baseline。

### 5.4 Mapping

```text
minimalist -> Profile/navigation reference
simplivre  -> multilingual/CJK typography reference
```

---

## 6. ElegantBook — B

### 6.1 源码面

核心：

```text
elegantbook.cls
```

最重要的不是颜色，而是 theorem/environment factory：高层 semantic type 可以统一处理：

```text
counter
numbered / starred
label prefix
visual style
simple / fancy renderer
```

### 6.2 我们拿什么

停止继续增长纯视觉 API：

```text
corebox
methodbox
warnbox
examplebox
boundarybox
...
```

长期正文声明：

```text
mentalmodel
mechanism
criterion
boundary
example
warning
```

然后 Profile 决定 renderer。

同样借鉴 `answer/noanswer` 的**单源多输出**思想给 Exam：

```text
paper / solution
```

### 6.3 Mapping

```text
ElegantBook -> semantic factory reference
```

---

## 7. whatsnote — B

### 7.1 源码面

核心工程文件：

```text
whatsnote.dtx
whatsnote.ins
build.lua
.github/
```

本轮核到的实现特征：

```latex
\keys_define:nn
```

以及 class 内部按职责拆分的 module 思路：

```text
typeset
layout
theorem
cover
```

Theorem module 使用 `keytheorems`；仓库同时有 l3build/CI 结构。

### 7.2 我们拿什么

```text
Public surface small
Internal implementation modular
expl3/l3keys configuration
real specimen before CI
l3build/CI after interfaces stabilize
```

不复制其 cover/chapter skin，也不因为它用了 `keytheorems` 就自动锁依赖。

### 7.3 Mapping

```text
whatsnote -> engineering architecture + regression reference
```

---

## 8. xltabular / tabularray — A/B after Real Table Evidence

### 8.1 触发原因不是“换新表格框架”

Real Topic04 与仓库搜索共同确认了一个重复缺陷：大量 raw `longtable` 用固定 `p/L` 列，并把内容宽度直接写成 `\linewidth - 固定列宽`。这会漏掉列间 `\tabcolsep`；Topic04 原 Canonical 就稳定出现 18pt/8pt 一类 Overfull。

### 8.2 xltabular — 当前 Handbook 薄依赖

本机 TeX Live 2026 已包含 `xltabular.sty`。它把 longtable 的分页能力与 tabularx 的 `X` 列结合，同时不要求把现有短表 `tabularx` 改写成另一套语法。

I.P.A.R.A 当前因此只在 **Handbook Family** 引入它，并暴露：

```latex
\begin{handbooklongtable}{L{2.5cm}YY}
...
\end{handbooklongtable}
```

目标：

```text
short fixed label columns
+ flexible Y explanation columns
+ page breaks when needed
```

而不是继续：

```text
L{3cm} L{4.25cm} L{\linewidth-7.25cm}
```

Synthetic standard/margin 两 Profile 已通过该 environment 的两遍 XeLaTeX 零诊断回归。

### 8.3 tabularray — 暂不引入

`tabularray` 的语义/样式分离与 LaTeX3 key-value 架构很有吸引力，但它是一整套新的表格 engine。当前问题只需要“longtable + X column”，若现在引入会把现有几十篇 table syntax 变成一次不必要的大迁移。

因此：

```text
xltabular -> current thin Handbook dependency

tabularray -> reference/candidate only;
              revisit only if xltabular cannot express a concrete future table need
```

---

## 9. keytheorems — Candidate A

### 8.1 代码面

本机 TeX Live 2026 存在：

```text
.../tex/latex/keytheorems/keytheorems.sty
```

公开 API：

```latex
\newkeytheorem
\renewkeytheorem
\newkeytheoremstyle
\renewkeytheoremstyle
```

其定位适合承接：

```text
theorem identity
numbering
parent/sibling counters
starred form
reference-related metadata
```

`tcolorbox` 则只负责 renderer。

### 8.2 进入 Core 前必须测

```text
scrbook + ctex
Chinese theorem names
numbered / unnumbered
shared counters
hyperref/bookmark
cross references
tcolorbox renderer
page breaks
```

### 8.3 Mapping

```text
keytheorems -> theorem machinery candidate; NOT locked yet
```

---

## 10. easybook / easybase — C

### 9.1 源码面

核心源：

```text
easybook.dtx
```

生成面包含：

```text
easybook.cls
easybase.sty
eb-tcolorbox.cfg
```

最值得借的不是 class，而是 named registry API，例如：

```latex
\SetTocStyle
\UseTocStyle
```

本质：

```text
register named style
-> store implementation
-> select/use by key/name
```

### 9.2 我们拿什么

用于设计：

```text
profile=standard|margin
variant=teacher|student
variant=paper|solution
renderer registry
```

不直接依赖 `easybase`，避免在 CTeX + KOMA 之外再引入第二个 meta-framework。

---

## 11. memoir / xtufte / ClassicThesis — C

### memoir

只保留传统数学书：

```text
chapter/page layout
traditional publishing typography
```

作为 regression benchmark，不再做完整 IPARA prototype。

### xtufte

只保留 Unicode/Tufte margin 视觉 benchmark；真实 margin mechanics 由 KOMA + kaobook mechanism reference + IPARA semantic contract 自己实现。

### ClassicThesis

只参考：

```text
title hierarchy
number/title proportions
rules
white space
text-block proportion
typographic restraint
```

用于防止 IPARA 滑向 Office/培训机构式的高噪声视觉。

---

## 12. Source-to-IPARA Mapping

| IPARA 问题 | 首要源码/项目 | 采用方式 | 目标 Owner |
|---|---|---|---|
| Book mechanics | KOMA `scrbook.cls` | Public API | KOMA |
| Header/Footer | `scrlayer-scrpage.sty` | Public API | KOMA |
| 中文基础 | `ctex.sty` | Public API | CTeX |
| 页面状态 | kaobook `kao.sty` | 机制重实现 | Handbook |
| Chapter 生命周期 | kaobook `kaobook.cls` | 机制参考 | Handbook |
| Profile 分层 | minimalist styles | 架构参考 | Family registry |
| 左 margin 导航 | minimalist `stream` | 视觉/机制参考 | Handbook margin |
| Semantic factory | ElegantBook | 机制重实现 | Core semantic layer |
| Cross-page table with flexible columns | xltabular | Public API via `handbooklongtable` | Handbook table layer |
| Full alternative table engine | tabularray | Candidate/reference only | none yet |
| Theorem identity | keytheorems | Candidate Public API | theorem layer |
| Internal modules | whatsnote | 工程参考 | implementation only |
| Key-value config | whatsnote/easybook | 机制参考 | Core config |
| Named style registry | easybook | API 参考 | profile/renderer registry |
| CI/regression | whatsnote | 工程参考 | test system |
| 传统书籍 benchmark | memoir | regression | none |
| Tufte benchmark | xtufte | regression | none |
| Typography restraint | ClassicThesis | regression | token/profile review |

---

## 13. 本轮已经验证的实现范围

### 12.1 已直接使用稳定 package API

```text
scrbook
scrlayer-scrpage
ctex package (heading=false)
fontspec / unicode-math portable baseline
booktabs / tabularx / longtable / array
xltabular (Handbook cross-page flexible tables)
TikZ / tcolorbox / listings existing baseline
marginnote (margin profile only)
```

### 12.2 已实现的薄 Adapter

```text
profile=standard|margin
semantic renderer primitives
semanticmargin: inline <-> outer margin
widecontent: identity <-> KOMA addmargin* outer expansion
```

`fullwidth` 仍未实现；不要因为已经有 `widecontent` 就把两者混为一谈。

### 12.3 实验后再决定

```text
keytheorems
specific sidenote/margin-note engine
scrlayer-notecolumn
LuaLaTeX / lua-widow-control
l3build CI
```

### 12.4 不再投入完整整书 Prototype

```text
memoir full IPARA prototype
xtufte full IPARA prototype
simplivre full IPARA prototype
ElegantBook full IPARA prototype
whatsnote full IPARA prototype
```

它们已经从“候选底座”降为 reference source。

---

## 14. 第一轮 Engine / Real Topic Experiment 的失败清单

固定同一内容，只验证：

```text
scrbook
+ ctex package
+ portable typography
+ KOMA page style
+ IPARA semantic primitives
```

先 standard，再 margin。

必须主动找：

```text
CTeX/KOMA section ownership conflict
chapter/TOC Chinese naming conflict
hyperref/bookmark warning
missing font
heading orphan
boundary table overflow
long equation overflow
TikZ diagram overflow
margin collision
odd/even offset error
widecontent wrong-side offset
```

---

## 15. Research Stop Rule

Reference Pool 已经支撑并完成 synthetic engine 第一轮实现：`ipara-core.sty + ipara-handbook.cls` 的 standard/margin 两个 Profile 可以消费同一 semantic body，并在 TeX Live 2026 + XeLaTeX 下两遍编译零诊断。

除非 Real Topic Gate 暴露一个当前机制解决不了的**具体技术缺口**，否则不再搜索“更漂亮的整书模板”。下一步的价值来自真实数学/408 内容的视觉和密度回归，而不是扩大候选池。
