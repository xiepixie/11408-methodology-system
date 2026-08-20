# 系统规范索引

> 本目录只保存每日阅读系统的架构、规则与模板，不保存具体文章学习内容。

---

## 1. 规范文件

| 文件 | 负责回答的问题 |
|---|---|
| [`architecture.md`](architecture.md) | 三层各自保存什么？不同文件的长期所有者是谁？跨层内容如何通过链接而不是复制关联？ |
| [`article_spec.md`](article_spec.md) | `article.md` 与 `reading_view.tex` 如何分工？一篇文章怎样完成训练闭环？ |
| [`expression_spec.md`](expression_spec.md) | 一个长期表达节点应怎样组织？生命周期怎样由证据推动？ |
| [`prosody_guide.md`](prosody_guide.md) | 意群切分、信息重音、弱读连读与语调升降怎样进行纯文本标注？ |
| [`review_rules.md`](review_rules.md) | 次日与后续怎样先主动检索，再回看原文？ |

人机协作时还必须遵守根目录 [`../AGENTS.md`](../AGENTS.md)。

---

## 2. 模板

`templates/` 只保存训练视图模板与样式：

- [`templates/reading_view_template.tex`](templates/reading_view_template.tex)：单篇精读训练手札模板；
- [`templates/ipara-reading.sty`](templates/ipara-reading.sty)：Cornell 双栏、语音训练、输出区等排版样式。

模板负责“怎样呈现”，系统规范负责“什么内容属于这里”。不要因为模板有某个区块，就强迫每篇文章都填满该区块。

---

## 3. 一个重要边界

本系统不再假设存在一份包含所有信息的总事实源，而采用**分对象事实源**：

- 原文 → `article.md`
- 单篇训练 → `reading_view.tex`
- 长期表达 → `02_expressions/`
- 长期能力 → `03_capabilities/`

具体原则见 [`architecture.md`](architecture.md)。