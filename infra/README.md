# Infra Domain

`infra/` 是 I.P.A.R.A 三域架构中的共享机制层。它只回答“底层机制怎样稳定运行”，不拥有 Teaching 或 Kaoyan 的业务语义。

## Ownership Router

| 子系统 | Canonical Owner | 责任 |
|---|---|---|
| LaTeX Design System | [`latex/README.md`](latex/README.md) | Core、Handbook Family、Profile、Semantic API、Lesson compatibility surface |
| Build / Render Mechanism | [`scripts/README.md`](scripts/README.md) | XeLaTeX 隔离编译、显式 PDF handoff、TikZ→dark/light SVG |
| Infra Steady-State Gate | [`check_infra.py`](check_infra.py) | 只编排并验证 Infra 自己的机器可判定不变量 |

## Dependency Boundary

允许：

```text
teaching/ ─┐
           ├──> infra/
kaoyan/  ──┘
```

禁止：

```text
infra/ ──> teaching/ 业务规则
infra/ ──> kaoyan/ Handbook / Exam / Publish Policy
```

共享脚本可以接受显式路径、输出目录和通用严格度参数，但不能自行决定“哪些学生课次要编译”“哪个 Handbook 是 Canonical”“某张真题图应该属于哪一年”。这些决定必须留在对应 Domain。

## Forward Standard

- 新建 Handbook：优先 `infra/latex/ipara-handbook.cls`，默认 `profile=standard`；
- 既有 Lesson：通过 `infra/latex/ipara.sty` thin shim 兼容；
- 既有 Kaoyan Prototype Handbook：可继续稳定编译，但不把 Prototype 当作新架构 Owner；
- 新的共享能力只有出现真实跨资产重复需求并通过 regression 后才进入 Core/Family API。

## Gate

从仓库根运行：

```bash
python3 infra/check_infra.py
```

该命令会在临时目录完成 Handbook Standard/Margin strict-warning XeLaTeX 回归和 TikZ dark/light SVG smoke test，不在源码目录留下 Generated State。

全仓验证使用：

```bash
python3 infra/scripts/check_repo.py
```
