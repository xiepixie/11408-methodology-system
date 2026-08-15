# 考研 LaTeX Design System 路由

> **性质**：领域路由 / Integration Stub，不是全局 Design System Owner。
>
> **全局 Canonical Owner**：[`../../latex/README.md`](../../latex/README.md)
>
> **开源项目源码调研**：[`../../latex/reference_pool.md`](../../latex/reference_pool.md)
>
> **考研 Handbook 具体视觉与几何参数**：[`latex_layout_spec.md`](latex_layout_spec.md)
>
> **Handbook 认知结构**：[`handbook_writing_spec.md`](handbook_writing_spec.md)
>
> **Handbook 物理身份**：[`handbook_contract.md`](handbook_contract.md)
>
> **发布安全**：[`repository_integrity.md`](repository_integrity.md)

---

## 本子项目采用结论

`common/考研/` 不再定义第二套 LaTeX 技术架构。它直接采用上层 Design System 的以下全局决策：

```text
One Design Language
+ Handbook / Lesson / Exam Families
+ KOMA-Script owns document mechanics
+ CTeX owns Chinese infrastructure
+ IPARA owns semantics and profiles
```

对于本仓库，当前只实际使用 **Handbook Family**。全局 experimental class 已完成：

```text
profile=standard
profile=margin
```

两个 Profile 已在同一 synthetic semantic body 上通过 XeLaTeX 零诊断回归。真实高数 Topic04 也已完成第一轮布局迁移：三张跨页固定宽表改为 `handbooklongtable + Y`，附录表改为 `handbooktable + Y`，两条六阶段单行链改为 `processchain`，迁移后 transitional Canonical、KOMA standard、KOMA margin 三路全部零诊断。因此 `margin` 已通过 **Real Topic Layout Gate**，但仍属于 Experimental：下一道 Gate 是 semantic margin 的信息价值、奇偶页密度与 MainText 独立闭合，而不是继续验证“是否装得下”。

当前 Canonical Handbook 的过渡实现仍是：

```text
common/考研/ipara-handbook.sty
```

它是 **Prototype / Transition Implementation**，不是长期全局入口。虽然 `common/latex/ipara-handbook.cls` 已通过 synthetic standard/margin Gate，但在 Real Topic Gate 通过前仍**不批量迁移旧 Canonical `.tex`**，也不继续向旧 Prototype 堆新的全局 Family architecture。

---

## 考研层唯一补充责任

本目录只补充全局 Design System 不应该拥有的考研 Handbook 规则：

- `latex_layout_spec.md`：考研 Handbook 的字体/版心/表格/TikZ/代码等具体布局参数；
- `handbook_writing_spec.md`：Mental Model、Criterion、Boundary、Mechanism 等认知写作规则；
- `handbook_contract.md`：Atlas / Topic / Bridge / Integration 的物理身份；
- `repository_integrity.md`：Canonical / Published View 的发布与完整性约束。

如果这里的规则与 `common/latex/README.md` 在 **Family、Profile、依赖、Semantic API、页面状态或迁移架构** 上冲突，以上层 Canonical Owner 为准；本文件只负责把 Agent 路由到正确 Owner。
