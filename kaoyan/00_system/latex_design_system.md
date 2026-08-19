# 考研 LaTeX Design System 路由

> **性质**：Kaoyan Domain 路由 / Integration Stub，不是全局 Design System Owner。
>
> **全局 Canonical Owner**：[`../../infra/latex/README.md`](../../infra/latex/README.md)
>
> **开源项目源码调研**：[`../../infra/latex/reference_pool.md`](../../infra/latex/reference_pool.md)
>
> **考研 Handbook 具体视觉与几何参数**：[`latex_layout_spec.md`](latex_layout_spec.md)
>
> **Handbook 认知结构**：[`handbook_writing_spec.md`](handbook_writing_spec.md)
>
> **Handbook 物理身份**：[`handbook_contract.md`](handbook_contract.md)
>
> **发布安全**：[`repository_integrity.md`](repository_integrity.md)

---

## 1. 本域采用的全局结论

`kaoyan/` 不定义第二套 LaTeX 技术架构，直接采用 `infra/latex/` 的全局决策：

```text
One Design Language
+ Handbook / Lesson / Exam Families
+ KOMA-Script owns document mechanics
+ CTeX owns Chinese infrastructure
+ I.P.A.R.A owns semantics and profiles
```

Kaoyan 当前实际使用的是 **Handbook Family**。全局正式实现与回归资产由：

```text
infra/latex/ipara-core.sty
infra/latex/ipara-handbook.cls
infra/latex/specimens/
```

统一拥有。

## 2. Forward Standard 与 Kaoyan Prototype 的稳态身份

**新建 Canonical Handbook** 直接采用正式 Public Family：

```latex
\documentclass[profile=standard,twoside=false]{ipara-handbook}
```

`profile=margin` 只在 supplementary semantic margin 通过真实信息价值 Gate 时显式启用。

现有大量 Canonical Handbook 仍可通过：

```text
kaoyan/ipara-handbook.sty
```

稳定编译。它的身份是 **Kaoyan Handbook Prototype / Compatibility Surface**：

- 它可以继续保障既有正文稳定；
- 它不拥有全局 Family/Profile/Variant 架构，也不作为新建 Handbook 模板；
- 新的跨文档族能力只在 `infra/latex/` 的正式 Owner 中演进；
- 不为了“路径已经迁移”或“视觉更统一”批量重排既有 Handbook；
- 当某份 Canonical `.tex` 正在发生真实的大修，或出现真实排版/字体/可移植性缺陷时，再按 `infra/latex/README.md` 的正式 API 渐进迁移。

因此 Prototype 的存在不是“迁移未完成”，而是兼容策略；是否继续保留由真实回归证据决定。

## 3. 已采用的 Handbook Profile

全局 Handbook Family 当前公开：

```text
profile=standard
profile=margin
```

两种 Profile 共用同一 semantic body；具体页面几何、表格、图示与 Kaoyan 阅读密度由 `latex_layout_spec.md` 约束。

`margin` 的长期质量判断不只是“是否装得下”，还包括：

- semantic margin 是否真的承载补充信息；
- 奇偶页密度是否稳定；
- 遮住 margin 后 MainText 是否逻辑闭合。

这属于排版质量审计，不是物理架构迁移状态。

## 4. Kaoyan 层唯一补充责任

本目录只补充全局 Design System 不应该拥有的 Kaoyan 业务规则：

- `latex_layout_spec.md`：Handbook 字体、版心、表格、TikZ、代码等具体布局参数；
- `handbook_writing_spec.md`：Mental Model、Criterion、Boundary、Mechanism 等认知写作规则；
- `handbook_contract.md`：Atlas / Topic / Bridge / Integration 的物理身份；
- `repository_integrity.md`：Canonical / Published View 的发布与完整性约束。

如果这里与 `infra/latex/README.md` 在 **Family、Profile、依赖、Semantic API、页面状态或兼容架构** 上冲突，以上层 Canonical Owner 为准。

## 5. 编译与发布边界

```text
infra/scripts/compile_tex.py
    = 通用 XeLaTeX 编译机制

kaoyan/00_system/cognitive_system.py publish
    = Kaoyan Canonical Handbook 发布 Policy
```

Kaoyan 日常发布不得绕过 `publish` preflight 直接把共享编译器当业务发布入口；共享编译器本身也不得推断 `90_publish/` 或 Handbook Canonical 状态。
