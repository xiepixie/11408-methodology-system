# 表达网络总索引

> **定位**：表达层保存可跨文章、跨主题复用的语言工具。所有表达按**沟通功能**组织，而不是按来源文章堆放。

每个成熟节点应尽量具备：来源语境、触发情境、声音形式、语体映射、句型骨架和调用证据。具体规则见 [`../00_system/expression_spec.md`](../00_system/expression_spec.md)。

---

## 1. 沟通功能分类

| 编号 | 分类 | 核心功能 | 当前状态 |
|---|---|---|---|
| 01 | [`01_opinions_and_stances.md`](01_opinions_and_stances.md) | 表达观点、立场、评价与推崇 | 已建立 |
| 02 | [`02_causes_and_attribution.md`](02_causes_and_attribution.md) | 解释原因、归因、责任与机制 | 已建立 |
| 03 | 比较与转折 | 对比、权衡、让步、反差 | 待出现真实表达后建立 |
| 04 | [`04_uncertainty_and_judgement.md`](04_uncertainty_and_judgement.md) | 不确定、审慎判断、暂缓定论 | 已建立 |
| 05 | [`05_trends_and_dynamics.md`](05_trends_and_dynamics.md) | 趋势、变化、兴起、延续与成熟 | 已建立 |
| 06 | 澄清与举例 | 重述、具体化、举例、消除歧义 | 待出现真实表达后建立 |
| 07 | [`07_daily_actions_and_habits.md`](07_daily_actions_and_habits.md) | 日常动作、互动、习惯与生活场景 | 已建立 |

分类不是永久固定的。若某一类长期过大，可以按沟通功能继续拆分；若两个分类长期高度重叠，则应合并，避免为目录整齐而制造边界。

---

## 2. 生命周期速查

| 等级 | 含义 |
|---|---|
| `L0 · 捕获` | 已建立候选节点，但尚未验证理解与使用 |
| `L1 · 理解` | 再次看到或听到时能准确理解，并能解释沟通功能 |
| `L2 · 提示使用` | 给出目标表达或句型骨架后能够正确造句 |
| `L3 · 主动生成` | 只给沟通情境，不给英文目标表达，也能自己检索出来 |
| `L4 · 无提示调用` | 自由复述或真实对谈中自然出现 |
| `L5 · 跨语境迁移` | 在明显不同的主题或任务中仍能无提示自然调用 |

生命周期可以升也可以降。一次成功使用只是一条证据，不代表永久掌握。

---

## 3. 当前表达索引

| 表达 ID | 核心表达 | 分类 | 当前状态 | 来源 |
|---|---|---|---|---|
| `EXP-001` | **bail on (plans / someone)** | 07 日常动作 | `L3 · 主动生成`* | [《The Magic of Summer Reading》P5](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p5) |
| `EXP-002` | **counter the summer slide / learning loss** | 07 日常动作 | `L2 · 提示使用` | [《The Magic of Summer Reading》P4](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p4) |
| `EXP-003` | **curl up in a cozy nook** | 07 日常动作 | `L2 · 提示使用` | [《The Magic of Summer Reading》P5](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p5) |
| `EXP-004` | **live up to the hype** | 07 日常动作 | `L2 · 提示使用` | [《The Magic of Summer Reading》P7](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p7) |
| `EXP-005` | **keep the magic of ... alive** | 05 趋势与变化 | `L2 · 提示使用` | [《The Magic of Summer Reading》P6](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p6) |
| `EXP-006` | **There's nothing like... to...** | 01 观点与立场 | `L3 · 主动生成`* | [《The Magic of Summer Reading》P1](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p1) |
| `EXP-007` | **amid the boom of...** | 05 趋势与变化 | `L2 · 提示使用` | [《The Magic of Summer Reading》P8](../01_articles/2026/2026-08-20_the_magic_of_summer_reading/article.md#p8) |
| `EXP-008` | **(remain) an open question** | 04 不确定与判断 | `L1 · 理解` | 《A New Replication Crisis?》 |
| `EXP-009` | **attribute A to B** | 02 因果与归因 | `L1 · 理解` | 《A New Replication Crisis?》 |
| `EXP-010` | **a big reason for this is...** | 02 因果与归因 | `L2 · 提示使用` | 口语训练 |

\* `EXP-001`、`EXP-006` 目前沿用已有训练记录中的 L3 标记，但后续应继续核对当时是否真正满足“没有英文目标提示、由情境主动检索”的新口径。若证据不足，应回调到 L2。

---

## 4. 索引维护规则

新增或修改表达时：

1. 先更新对应分类文件中的完整节点；
2. 再更新本页索引；
3. 来源文章存在 `article.md` 锚点后，再把纯文本来源替换为可点击链接；
4. 生命周期变化必须同时留下代表性调用证据；
5. 不要为了凑数量创建空分类文件或低价值表达节点。

本页只负责导航和状态概览，表达的完整语义以分类文件为准。