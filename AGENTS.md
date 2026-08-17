# Repository AGENTS

> **Scope**：资源库根目录及全部后代。
>
> **系统目标**：维护一个高内聚、低耦合、空间心智模型极简自洽的个人长青知识系统。

## 0. 三域定义与顶层路由

仓库只有三个长期业务/技术 Domain：

```text
teaching/   = 我给别人教什么：一对一数学教学交付体系
kaoyan/     = 我自己学什么：11408 学习工程、Handbook、真题与证据系统
infra/      = 两边靠什么运行：跨领域 LaTeX Design System 与通用编译/渲染机制
```

任务进入某一 Domain 后，优先读取该 Domain 的局部 Owner：

- `teaching/**` → `teaching/AGENTS.md`
- `kaoyan/**` → `kaoyan/AGENTS.md`
- LaTeX Family / Profile / Variant / Semantic API → `infra/latex/README.md`
- 通用编译与渲染引擎 → `infra/scripts/README.md`

根 `AGENTS.md` 不拥有任何具体教学规则、考研 Handbook 规则或 LaTeX 实现细节；这些必须由对应 Domain Owner 持有。

## 1. 底层元准则：思想无损与密度增量

对现有笔记、知识库、代码与心智模型的修改，本质是在已有认知基石上的演进、深化与提升，不是“推倒重来”或“简化摘要”。

- 严禁借“整理/精炼/重构”删除有效推导、背景脉络、Case、边界条件、直观解释或已有行为契约；
- 原有有效认知与业务规则必须完整继承；
- 修改后的逻辑严密性、心智模型完备度、可执行性和维护性只能正向增加；
- 如果新架构尚不能无损承接旧资产，先保留兼容层，不强行迁移。

## 2. 严格渐进式演化

所有复杂修改遵循：

```text
精准定位 Where
→ 增量目标 What & Why
→ 后果评估 Consequence
→ 小步修改
→ Local Gate
→ 下一阶段
```

禁止一次性大拆大建。每一步必须允许判断：到底是旧问题、迁移问题，还是新内容修改造成的问题。

## 3. Single Source of Truth / Ownership

同一稳定事实、规则或机制只能有一个 Canonical Owner。

- `teaching/` 拥有教学业务语义、学生证据与教学公共资产；
- `kaoyan/` 拥有考研 Knowledge / Control / Learning 资产、Exam Archive Package 与 Source Diff；
- `infra/` 只拥有 Domain-Agnostic Mechanism，不拥有高中数学或考研业务知识；
- `90_publish/` 是 Derived Publication View，不拥有知识；
- `archives/**/solutions/` 是 Derived Solution Layer，不得成为新的机制 Owner；
- `sources/` 是外部原料与溯源层，不得冒充 Canonical Handbook。

如果 Owner 不明确，不建立第二份稳定真相；先保留为 Source / Candidate / Migration Note。

## 4. Generated State 与 Repository Asset 分离

以下默认属于 Generated / Local Runtime State，不得因为“有用过”就晋升为仓库资产：

```text
.venv/
__pycache__/
tmp/
tmp_*/
*.aux *.log *.out *.toc *.xdv
*.synctex *.synctex.gz *.synctex(busy)
```

PDF 是否属于 Repository Asset 由其角色决定：正式教学交付物、真题资产或 Publication View 可以保留；编译中间件和重复冲突副本不能。

## 5. 三域终极架构与资产定位

全仓物理架构已收敛至三域标准架构：

```text
teaching/   = 我给别人教什么：一对一教学交付体系 (templates, pool, topics, students)
kaoyan/     = 我自己学什么：11408 学习工程 (00_system, 10_数学一, 20_英语一, 30_408, 40_复试, archives, sources, 90_publish)
infra/      = 两边靠什么运行：LaTeX Design System (ipara-core.sty, ipara-handbook.cls, ipara.sty) 与通用脚本
```

运行与兼容规则：
1. **统一根逻辑**：所有代码、手册、题包和会话必须直连 Canonical Owner；
2. **Forward Standard**：新 Handbook 优先使用 `infra/latex/ipara-handbook.cls`；`kaoyan/ipara-handbook.sty` 只作为既有 Kaoyan Handbook 的兼容面，不再承担新架构演进；
3. **Lesson Thin Shim**：`infra/latex/ipara.sty` 只转发到 `infra/latex/legacy/ipara-legacy.sty` 保障既有 Lesson；跨文档族能力统一由 `ipara-core.sty` / Family API 演进；
4. **派生视图隔离**：`kaoyan/90_publish/` 按 `math1/`, `english1/`, `408/`, `system/` 分类组织阅读版 PDF，不拥有知识源码。

## 6. 修改前后验证

涉及稳定资产、脚本、物理路径或发布入口时，优先用根级只读编排器执行完整硬门禁：

```bash
python3 infra/scripts/check_repo.py
```

需要查看允许暂存的 Kaoyan 维护债务时显式追加：

```bash
python3 infra/scripts/check_repo.py --audit
```

`check_repo.py` 只拥有 Root Wiring（顶层路由、退休根活动文件、根级链接）并负责编排，不拥有任何 Domain 规则。失败时再进入对应 Domain README 使用单域 Gate 定位；不得为了让全仓命令变绿而在根脚本复制/放宽域内规则。

## 7. 禁止事项

- 禁止引入任何非规范或过时的历史路径；
- 禁止在业务资产源码目录内遗留 `.aux/.log/.xdv/.pdf` 等构建状态；
- 不为目录整齐而创建没有真实职责的抽象层；
- 不把 Knowledge / Control / Learning 三个逻辑 Plane 强行物理拆成三棵重复目录树；
- 不把 Domain Policy 塞进 `infra/`；
- 不用 Publication View 反向覆盖 Canonical Source；
- 不把一次题解、一次错题或一次对话直接晋升为稳定 Handbook Rule。
- 不为了“迁完了”而绕过测试、Owner 或兼容门禁。
