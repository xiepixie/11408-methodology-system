# I.P.A.R.A LaTeX Open-Source Reference Pool

> **性质**：Research Log，不是 Design System 契约。Canonical 技术决策由 [`README.md`](Documents/I.P.A.R.A/工作领域/资源/infra/latex/README.md) 唯一拥有。
>
> **迁移状态**：历史 673 行研究快照中的源码证据、版本记录、Source-to-IPARA 映射已完成核销并固化于 `infra/latex/`，已完成核销并固化于 `infra/latex/`。
>
> **新证据写入规则**：新调研只追加到本路径。如果外部版本、许可证或源码位置需要重新验证，应在本文件记录新的验证结论。

## Adopted classification

外部项目仍按三种角色处理：

| 等级 | 含义 | 动作 |
|---|---|---|
| **A — Direct Dependency** | 使用稳定 public API，让外部包拥有底层 machinery | 声明依赖，不复制内部实现 |
| **B — Mechanism Reference** | 机制值得复用，但不值得绑定整个模板 | 抽状态模型，用 IPARA API 重实现 |
| **C — Visual / Architecture Reference** | 主要价值是信息层级、视觉或工程组织 | 借原则和测试标准，不形成 runtime dependency |

完整历史证据请读取 frozen snapshot；它是迁移证据，不是第二个架构 Owner。
