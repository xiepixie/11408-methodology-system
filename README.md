# README

本仓库是一个长期个人知识与教学交付系统。顶层只维护三个高内聚 Domain；任何稳定规则、知识或机制都必须有唯一 Canonical Owner。

```text
teaching/   我给别人教什么：一对一数学教学交付体系
kaoyan/     我自己学什么：11408 学习工程、Handbook、真题与证据系统
infra/      两边靠什么运行：LaTeX Design System 与通用编译/渲染机制
```

## Start Here

| 任务 | Canonical 入口 | 规则 Owner |
| ----------------- | ----------------------- | -------------------- |
| 一对一教学、题库、专题、学生课次 | [`teaching/README.md`](teaching/README.md) | [`teaching/AGENTS.md`](teaching/AGENTS.md) |
| 11408 学习、Handbook、Rules、真题 | [`kaoyan/README.md`](kaoyan/README.md) | [`kaoyan/AGENTS.md`](kaoyan/AGENTS.md) |
| Infra 共享机制总路由 | [`infra/README.md`](infra/README.md) | `infra/README.md` |
| LaTeX Family / Profile / Semantic API | [`infra/latex/README.md`](infra/latex/README.md) | `infra/latex/README.md` |
| 通用编译 / TikZ→SVG | [`infra/scripts/README.md`](infra/scripts/README.md) | `infra/scripts/README.md` |
| 全仓三域边界、Ownership、Generated State | [`AGENTS.md`](AGENTS.md) | `AGENTS.md` |

根目录只负责路由与全局不变量，不复制各 Domain 的具体业务规则。

## Physical Architecture

```text
资源/
├── AGENTS.md
├── README.md
├── teaching/
│   ├── AGENTS.md
│   ├── students/
│   ├── pool/
│   ├── topics/
│   └── templates/
├── kaoyan/
│   ├── AGENTS.md
│   ├── 00_system/
│   ├── 01_control/
│   ├── 10_数学一/
│   ├── 20_英语一/
│   ├── 30_408/
│   ├── 40_复试/
│   ├── archives/
│   ├── sources/
│   ├── 80_evidence/
│   └── 90_publish/
└── infra/
    ├── README.md
    ├── check_infra.py
    ├── latex/
    └── scripts/
```

活动代码、文档、题包、题解和 Agent 配置必须直连 Canonical 路径。

## Steady-State Invariants

1. **Single Source of Truth**：同一稳定事实、规则或机制只能有一个 Owner。
2. **单向依赖**：`teaching/`、`kaoyan/` 可以依赖 `infra/`；`infra/` 不反向拥有业务语义。
3. **Public / Private 分离**：Teaching 公共题库与专题不存学生事实；学生证据只进入 `teaching/students/`。
4. **Source / Derived 分离**：`kaoyan/90_publish/` 与 `archives/**/solutions/` 均为派生视图，不拥有知识机制。
5. **Generated State 隔离**：`.venv/`、`__pycache__/`、`tmp*`、LaTeX aux 等只属于本地运行状态，不是仓库知识资产。
6. **机制 / Policy 分离**：共享编译器只编译显式路径；Teaching / Kaoyan 自己决定业务验收与发布策略。

## Repository Gates

全仓硬门禁统一入口：

```bash
python3 infra/scripts/check_repo.py
```

需要在硬门禁之后同时查看非阻塞 Kaoyan 维护债务：

```bash
python3 infra/scripts/check_repo.py --audit
```

根脚本只拥有 **Root Wiring**（顶层路由存在、退休根不重新长出活动文件、根/Infra 路由不破链）并负责编排；不复制各 Domain 的规则实现。它随后依次调用 Infra、Teaching、Kaoyan、408 Archive、Math1 Archive 与 Math1 Canonical Source 的 Canonical Gate。单域调试时仍可直接运行各自 README 中的命令。

`check` / Domain Gate 负责阻止机器可确定的结构回归；`audit` 只报告允许暂存的维护债务。不要为了让 Gate 变绿而删除有效知识或绕过 Owner。
