# 系统规范索引

> 本目录只维护每日阅读系统的架构、规则和模板，不保存具体文章的学习内容。

---

## 1. 规则文件

| 文件 | 负责的问题 |
|---|---|
| [`architecture.md`](architecture.md) | 三层分别拥有哪类对象？跨层信息怎样连接而不重复维护？ |
| [`session_protocol.md`](session_protocol.md) | 一篇文章的人机交互按什么顺序推进？什么时候必须处理标记、给参考复述、停止重复并进入间隔复习？ |
| [`article_spec.md`](article_spec.md) | `article.md` 与 `reading_view.tex` 怎样分工？一篇文章怎样完成训练闭环？ |
| [`obsidian_interaction.md`](obsidian_interaction.md) | 学习者怎样在 Obsidian 中首读、标记和精确回链？ |
| [`expression_spec.md`](expression_spec.md) | 什么表达值得进入长期网络？节点怎样组织和晋级？ |
| [`prosody_guide.md`](prosody_guide.md) | 怎样用可靠声音、IPA、意群和重音完成语音训练？ |
| [`study_rhythm.md`](study_rhythm.md) | 每次训练怎样分配新学、复习和输出时间？ |
| [`review_rules.md`](review_rules.md) | 复习时怎样主动检索？什么证据可以推动表达生命周期变化？ |

AI 协作时还必须遵守根目录 [`../AGENTS.md`](../AGENTS.md)。`AGENTS.md` 只保留执行约束和路由规则，具体细节以本目录对应规范为准。

---

## 2. 模板
 
`templates/` 只负责提供稳定的工作起点：

- [`templates/article_template.md`](templates/article_template.md)：Obsidian 原文阅读与首读标记模板；
- [`templates/reading_view_template.tex`](templates/reading_view_template.tex)：单篇精读训练手札模板，明确区分学习者原始输出、AI 参考复述、对照反馈与下一次冷检索；
- [`templates/ipara-reading.sty`](templates/ipara-reading.sty)：Cornell 双栏、语音训练和输出区的排版样式。

模板中的区块是可选工具，不是完成清单。文章不需要为了“填满模板”而生成没有真实价值的内容。

---

## 3. 编译与门禁工具

`tools/` 维护领域专有的编译与完整性门禁：

- [`tools/compile_daily_reading.py`](tools/compile_daily_reading.py)：单篇/模板/全量批量编译调度器，自动装配环境并清理中间件；
- [`tools/check_daily_reading.py`](tools/check_daily_reading.py)：五维静态与动态硬门禁（结构规范、双栏超链接闭环、无剧透检查、构建清洁度、模板冒烟测试）。

---

## 4. 分对象事实源

本系统不维护一份包含所有内容的总文件，而是让不同对象各有唯一长期所有者：

| 对象 | 所有者 |
|---|---|
| 原文、来源、学习者首读痕迹 | `article.md` |
| 单篇文章的训练现场 | `reading_view.tex` |
| 跨文章表达节点 | `02_expressions/` |
| 跨文章能力状态 | `03_capabilities/` |
| 系统规则与模板 | `00_system/` |

跨层关系优先通过块链接、表达 ID 和证据链接建立。需要引用时可以保留一句当前语境说明，但不要复制完整定义。
