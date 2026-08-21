# 每日阅读与表达习得系统

> **一句话定位**：让真实文章保持真实，让单篇训练保持具体，让可复用表达进入长期网络，让能力判断只由真实调用证据推动。

---

## 1. 系统由三层组成

```text
真实文章
   ↓
文章层：保存原文，并完成这一篇文章的精读、声音与输出训练
   ↓ 萃取值得长期保留的内容
表达层：保存可跨文章复用的语言工具
   ↓ 在真实任务中调用
能力层：维护跨文章的长期能力状态、稳定问题与证据
   ↓ 暴露新的表达需求
表达层继续生长
```

三层的对象不同，因此不要把同一套内容复制到三个地方：

- **文章层**关心“这篇文章是什么、这篇文章怎么练”；
- **表达层**关心“这个表达以后还能怎么用”；
- **能力层**关心“经过多篇训练后，我现在真正会什么、还稳定卡在哪里”。

完整职责边界见 [`00_system/architecture.md`](00_system/architecture.md)。

---

## 2. 当前目录结构

```text
daily_reading/
├── README.md
├── AGENTS.md                         # AI 协作与对象归属规则
│
├── 00_system/                        # 系统层：只放规则与模板
│   ├── README.md
│   ├── architecture.md               # 三层职责、文件所有权、跨层引用原则
│   ├── article_spec.md               # 文章层与单篇训练手札规范
│   ├── obsidian_interaction.md       # Obsidian 首读标记与块引用规范
│   ├── study_rhythm.md               # 每日学习时间与巩固节奏
│   ├── expression_spec.md            # 表达节点与生命周期规范
│   ├── prosody_guide.md              # 语音与韵律训练规范
│   ├── review_rules.md               # 主动检索与后续复习规则
│   └── templates/
│       ├── article_template.md       # Obsidian 原文阅读模板
│       ├── reading_view_template.tex
│       └── ipara-reading.sty
│
├── 01_articles/                      # 文章层
│   ├── README.md                     # 文章目录与单篇文件职责
│   └── YYYY/
│       └── YYYY-MM-DD_short_title/
│           ├── article.md            # 原文阅读副本 + 来源 + 学习者首读标记
│           ├── reading_view.tex      # 本篇精读训练手札
│           ├── reading_view.pdf      # 编译后的训练阅读版
│           └── assets/               # 原页、音频、附图等（按需）
│
├── 02_expressions/                   # 表达层
│   ├── README.md                     # 表达网络索引与生命周期
│   └── *.md                          # 按沟通功能聚合的表达节点
│
└── 03_capabilities/                  # 能力层
    ├── README.md                     # 能力维度与稳定问题索引
    └── *.md                          # 各能力维度的长期状态与证据
```

目录中不存在的分类文件不提前创建。只有真实内容出现后，再决定是否增加新的分类或能力维度。

---

## 3. 最重要的不是“一个总事实源”，而是“每个对象有唯一所有者”

本系统采用**分对象事实源**：

| 对象 | 长期所有者 |
|---|---|
| 原文、来源与学习者首读痕迹 | `article.md` |
| 某一篇文章的精读、语音、复述与对谈训练 | `reading_view.tex` |
| 某个可复用表达的完整定义 | `02_expressions/*.md` |
| 某项长期能力状态或稳定问题 | `03_capabilities/*.md` |
| 系统规则 | `00_system/*.md` |

因此，不再要求把所有文章训练数据都塞进 `article.md`。

TeX 中为了 Cornell 排版再次呈现部分原文属于**展示性重复**；表达卡、能力结论等长期事实则不应在多个地方各维护一份。

---

## 4. 单篇文章目录如何使用

### 第一步：先读并标记 `article.md`

这里尽量接近真实阅读环境。来源信息放在 Obsidian Properties 中，正文只保留原文、稳定段落块标识和学习者自己的首读痕迹。

推荐直接在 Live Preview 中标记最小文本跨度：`==...== [?]`、`==...== [!]`、`==...== [★]`、`==...== [~]`。AI 不提前给答案，也不擅自替学习者制造断点。

### 第二步：训练进入 `reading_view.tex`

独立首读后，先按 [`00_system/session_protocol.md`](00_system/session_protocol.md) 做**标记握手**：回显全部标记、处理数量冲突、逐条解决 `[?] [!] [~] [★]`。然后再在 TeX 手札中处理：

- 真正卡住的地方；
- 文章结构；
- 值得练的语音训练句；
- 学习者第一次真实复述、观点和对谈；
- AI 参考复述与差异对照；
- 本篇产生的表达需求；
- 下一次先不看答案的冷检索目标。

### 第三步：只把长期价值内容向外沉淀

- 可复用表达进入 `02_expressions/`；
- 稳定能力状态或代表性证据进入 `03_capabilities/`。

其余内容留在本篇，不需要升级成长期资产。

---

## 5. 每天约一小时怎样运行

默认先处理旧内容，再推进当前文章，最后完成主动输出：

```text
旧内容主动检索
   ↓
当前文章独立阅读 / 标记
   ↓
AI 标记反馈与定点诊断
   ↓
学习者真实输出
   ↓
AI 参考复述 + 差异对照
   ↓
必要的短修复 / 语音 / 对谈
   ↓
收尾并留下下一次冷检索目标
```

时间比例不锁死。一篇高质量长文可以跨多个训练时段；旧内容开始大量遗忘时，应主动减少新输入、增加深化与整合，而不是继续追求“一天一篇”。

完整节奏见 [`00_system/study_rhythm.md`](00_system/study_rhythm.md)。

---

## 6. 训练密度采用自适应原则

不同文章的篇幅、语言质量和训练价值差异很大，因此不规定每篇必须：

- 提取固定数量的表达；
- 精讲固定数量的长句；
- 练固定数量的黄金句；
- 做固定轮数的对谈；
- 写固定长度的摘要。

判断标准改为：

> **这篇文章最值得练什么，就练什么；练到能够完成理解、声音、表达和输出闭环即可。**

短文自然少取，长而高质量的文章可以多取；重复度高、迁移价值低的内容不为凑数入库。

---

## 7. 快速导航

- 系统职责与数据边界：[`00_system/architecture.md`](00_system/architecture.md)
- 单篇交互状态机：[`00_system/session_protocol.md`](00_system/session_protocol.md)
- AI 协作规则：[`AGENTS.md`](AGENTS.md)
- 单篇文章规范：[`00_system/article_spec.md`](00_system/article_spec.md)
- Obsidian 阅读交互：[`00_system/obsidian_interaction.md`](00_system/obsidian_interaction.md)
- 每日学习节奏：[`00_system/study_rhythm.md`](00_system/study_rhythm.md)
- 表达节点规范：[`00_system/expression_spec.md`](00_system/expression_spec.md)
- 语音训练规范：[`00_system/prosody_guide.md`](00_system/prosody_guide.md)
- 主动复习规则：[`00_system/review_rules.md`](00_system/review_rules.md)
- 表达网络：[`02_expressions/README.md`](02_expressions/README.md)
- 能力层：[`03_capabilities/README.md`](03_capabilities/README.md)
