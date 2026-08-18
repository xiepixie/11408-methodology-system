# I.P.A.R.A LaTeX Design System

> **Canonical Owner**：本文件唯一拥有全仓库 LaTeX Design System 的技术架构、依赖边界、Document Family / Profile / Variant、Semantic API、页面状态、兼容与迁移策略。
>
> **Scope**：`infra/latex/` 及所有使用该 Design System 的 Teaching / Kaoyan / Exam 文档。
>
> **不拥有**：具体领域知识、教学业务语义、考研 Handbook 认知结构、真题归档规则与发布策略。它们分别由 `teaching/`、`kaoyan/` 的 Domain Owner 持有。

## 0. Canonical Architecture 与合同规范

本文件是全仓库 LaTeX Design System 的唯一真相源（Single Source of Truth）。

- `infra/latex/ipara-core.sty` 拥有跨文档族的排版核心、通用颜色与语义基底；
- `infra/latex/ipara-handbook.cls` 拥有考研与工程 Handbook 的正式 Public Family 文档类；`profile=standard` 是新建 Handbook 的 Forward Default，`profile=margin` 仍是显式选择的质量候选；
- `infra/latex/ipara.sty` 作为 Thin Shim 自动加载 Lesson 兼容层；
- `kaoyan/ipara-handbook.sty` 作为独立原型包持续保障考研业务排版稳定；
- 所有文档与脚本直连 Canonical 入口，无任何外部或历史路径回退。

---

## 1. 一个 Design Language，三个 Document Family

长期模型保持不变：

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

Atlas Poster 暂不构成第四 Family。Family 是页面任务与交互语法，不是换皮主题。

---

## 2. 唯一 Owner 分工

```text
KOMA-Script
├── class mechanics
├── section/chapter mechanics
├── page styles / marks
├── headers / footers
├── TOC
└── duplex / layout public API

CTeX
├── Chinese language conventions
├── CJK infrastructure
├── Chinese heading/name conventions
└── punctuation / spacing infrastructure

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

禁止第二 Owner。外部模板默认只作为 Direct Dependency / Mechanism Reference / Visual Reference 三种角色之一进入系统。

---

## 3. 当前物理结构与公开入口

```text
infra/latex/
├── README.md                  # Canonical architecture Owner
├── reference_pool.md          # global research evidence / source reference log
├── ipara.sty                  # Lesson compatibility thin shim
├── legacy/
│   └── ipara-legacy.sty       # 历史成熟 Lesson implementation
├── ipara-core.sty             # shared Core public API
├── ipara-handbook.cls         # Handbook Family public API
└── specimens/                 # regression assets
    ├── handbook-body.tex
    ├── handbook.tex
    └── handbook-margin.tex
```

### 尚未创建的公开入口

`ipara-lesson.cls` 与 `ipara-exam.cls` **不会因为目标树里写了名字就先创建空壳**。

- Lesson class 必须由真实 Teaching regression 抽取；
- Exam class 必须由真实 paper / solution single-source 需求抽取；
- 在出现真实 API 前创建空类违反“无空抽象层”原则。

因此当前 Target Architecture 中这两项是 **planned public entrypoints**，不是已完成资产。

---

## 4. Compatibility Layer
 
### 4.1 Lesson
 
```text
\usepackage{ipara}
        ↓
infra/latex/ipara.sty
        ↓
infra/latex/legacy/ipara-legacy.sty
```
 
`legacy/ipara-legacy.sty` 为历史 Lesson 文档提供稳定的兼容底座；新跨文档族能力统一在 `ipara-core.sty` 中演进。

### 4.2 Core / Handbook
 
Canonical 入口：
 
```text
infra/latex/ipara-core.sty
infra/latex/ipara-handbook.cls
```

### 4.3 Kaoyan Handbook Compatibility Surface
 
`kaoyan/ipara-handbook.sty` 继续服务于既有 Kaoyan Handbook 的稳定编译，但它是 **Compatibility Surface**，不是新建 Handbook 的 Forward Standard。新建 Canonical Handbook 优先使用 `infra/latex/ipara-handbook.cls`；存量正文只在本来发生真实修订或出现排版/可移植性缺陷时渐进切换，避免为了样式统一制造无意义 diff。

---

## 5. Semantic API 原则

长期核心仍是：

```text
Content declares meaning;
Profile decides appearance.
```

第一阶段已有真实证据的 semantic：

- `mentalmodel`
- `mechanism`
- `criterion`
- `boundary`
- `example`
- `warning`

这些是渲染语义，不创造新的知识资产类型。Theory object 的编号/reference machinery 与 renderer 必须分层，不能让 `tcolorbox` 顺便成为所有数学对象的 counter engine。

---

## 6. Handbook Family

当前公开 Profile：

```text
profile=standard
profile=margin
```

### Standard

- 单一稳定正文阅读区；
- 当前 Real-Topic-backed candidate 主栏约 `170mm`；
- `widecontent` 安全退化为 ordinary body width。

### Margin

- `main text + outer semantic margin + local widecontent escape`；
- 当前 candidate：`116mm main + 5mm gap + 39mm semantic margin`；
- margin 只能承载 supplementary 信息，不能成为逻辑主链唯一 Owner；
- 遮住 margin 后 MainText 必须逻辑闭合。

上述数值仍是 specimen-backed Candidate，不是冻结 Design Token。

---

## 7. Dependency / Portability Boundary

Canonical baseline：

- XeLaTeX；
- KOMA-Script + CTeX；
- portable TeX Live fonts；
- 不要求 shell escape；
- package 进入 Core 前必须通过真实 specimen；
- 外部模板不能因为“好看”直接成为 runtime dependency。

当前 `xltabular` 是 Handbook 跨页自适应表的已验证薄依赖。

---

## 8. Regression Specimens

`infra/latex/specimens/` 是实现回归资产，不是 Handbook Knowledge Source。

核心不变量：

```text
handbook.tex
handbook-margin.tex
        ↓ consume
same handbook-body.tex
```

必须验证：

- 中文 + English + 数学 + code；
- section hierarchy / TOC / marks；
- semantic objects；
- ordinary / wide / long table；
- TikZ；
- standard / margin 同源；
- 无 fatal error / missing font / undefined reference；
- 无 unexplained overfull / underfull。

当前 steady-state regression 由一条可重复命令证明：

```bash
python3 infra/check_infra.py
```

该 Gate 会验证公开入口、Lesson thin shim、Standard/Margin 同源 semantic body、两种 Profile 的 strict-warning XeLaTeX 编译，以及显式 TikZ→dark/light SVG smoke test。

---

## 9. Mechanism 与 Domain Policy

LaTeX Design System 与底层编译机制分离：

```text
infra/latex/    = 页面与语义渲染机制
infra/scripts/  = 编译 / 矢量渲染机制
teaching/       = Lesson 业务语义
kaoyan/         = Handbook / Exam / Publish 业务语义
```

`infra/scripts/compile_tex.py` 不推断发布目标。Kaoyan 的 `90_publish/` 是 Kaoyan Policy，由 `cognitive_system.py` 显式传 `--publish-dir`。

TikZ→SVG 同理：共享脚本只接受显式文件/目录；“扫描哪些真题年份”属于 Kaoyan tool。

---

## 10. Steady-State Regression Gates

本 Design System 长期只维护可重复验证的不变量；统一入口为 `python3 infra/check_infra.py`：

- **Ownership Gate**：Core / Handbook Family 只由 `infra/latex/` 拥有；Domain 不建立第二套全局 Family/Profile/Semantic API。
- **Portability Gate**：synthetic specimen 必须继续在 XeLaTeX + portable TeX Live baseline 下编译。
- **Handbook Standard / Margin Gate**：`handbook.tex` 与 `handbook-margin.tex` 必须继续消费同一 `handbook-body.tex`。
- **Existing Lesson Regression**：真实 Teaching student/teacher 模板通过 `python3 teaching/check_teaching.py --compile`，验证 `ipara.sty → legacy/ipara-legacy.sty` 兼容链。
- **Mechanism / Policy Gate**：`infra/scripts/` 只拥有通用机制；Teaching / Kaoyan 决定各自验收和发布 Policy。
- **Exam Family Gate**：只有出现真实 paper/solution single-source 重复需求时才抽取 `ipara-exam.cls`；没有证据时不创建空抽象层。
- **Semantic-Margin Quality Gate**：margin 的信息价值、奇偶页密度与 MainText 独立闭合属于持续质量审计，不与物理迁移状态绑定。

---

## 11. 禁止事项

- 不把 `infra/` 变成 Teaching / Kaoyan 规则垃圾桶；
- 不在 Core 预造没有真实重复需求的环境；
- 不为目录好看创建空 `ipara-lesson.cls` / `ipara-exam.cls`；
- 不让任何历史兼容入口重新演化为第二实现 Owner；
- 不因为物理路径迁移就批量改 Canonical Handbook 正文；
- 不用缩放掩盖表格/图形结构问题；
- 不把 Publication View 当知识 Owner。

---

## 12. 一句话架构

$$
\boxed{
\text{KOMA owns mechanics}
+\text{CTeX owns Chinese infrastructure}
+\text{I.P.A.R.A owns semantics and profiles}
}
$$

长期目标不是继续制造迁移层，而是让真实 Teaching / Kaoyan 资产持续验证同一个 Design Language，并在出现真实重复需求时再抽取新的 Family API。
