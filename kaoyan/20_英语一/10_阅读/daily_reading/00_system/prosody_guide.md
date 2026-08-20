# 语调与韵律标记规范

> **核心原则**：音标主要解决“单词怎么发”，意群、重音与语调解决“整句话的语言节奏”。本规范聚焦于**纯文本语音语调标记体系**，通过直观的视觉符号重塑句子节奏与意群边界，不依赖外部音频设备或录音比对流程。

---

## 1. 为什么需要文本语音语调标记

阅读时如果只靠视觉逐词解码，容易导致：

- 长句在口头表达或朗读时断裂；
- 每个单词平均用力、缺乏信息主次；
- 停顿位置与句法结构脱节；
- 形成机械的“中式等距字音节奏”，难以内化地道英语语流。

因此，每篇文章精选少量具有迁移价值的“黄金句”进行语调与韵律剖析，而非全篇机械标注。

---

## 2. 黄金句筛选标准

黄金句数量自适应，优先满足：

1. **含核心表达**：包含本篇最值得积累的表达或句型；
2. **句法结构典型**：意群边界清晰，具有句法迁移价值；
3. **节奏特征鲜明**：存在典型的信息重音、功能词弱读、连读或语调升降变化；
4. **长度适中**：由 2~4 个自然意群构成，便于脱稿朗读与内化。

---

### 3.1 国际音标与词重音（IPA & Word Stress）

在剖析整句节奏前，先明确句中生词、易错词或核心表达的标准国际音标（IPA）与主副重音位置：

- **LaTeX 宏**：`\ipa{/ˈhjuːmɪd/}`（使用 Charis SIL 语言学音标字体渲染）；
- **重点音标标注**：`\prosodyipa{\textbf{humid} \ipa{/ˈhjuːmɪd/} \quad$\bm{\cdot}$\quad \textbf{escape} \ipa{/ɪˈskeɪp/}}`。

### 3.2 意群切分与停顿（Sense Groups & Pauses）

- **` / `（`\chunk`）**：自然意群边界（轻短呼吸停顿，通常基于短语、主谓宾核心或状语从句边界）；
- **` // `（`\majorpause`）**：句间、明显转折或较长插入语前后的显著停顿。

> 示例：
> `At this point in the summer / my favorite thing to do / is to read on the beach. ↓`

### 3.3 信息重音（Information Stress）

标出承担新信息、对比、否定或核心谓语动作的词汇：

- **Markdown 标记**：`**CAPITALIZED**` 或 `**Bold**`；
- **LaTeX 宏**：`\stress{WORD}`（高亮为醒目的焦点色彩）。

> 示例：
> `There's \stress{NOTHING LIKE} a \stress{GOOD BOOK} / to help me \stress{ESCAPE} ...`

### 3.4 功能词弱读（Weak Forms）

英语中的介词、冠词、助动词、连词等功能词通常弱化（元音弱化为 `/ə/` 或 `/ɪ/`）：

- **Markdown 标记**：斜体或括号标注；
- **LaTeX 宏**：`\weak{word}`（以灰度微缩字体呈现）。

> 示例：
> `\weak{in order to} \stress{READ IT}`

### 3.5 连读与音变（Linking & Smooth Transition）

- **`\phonlink{A}{B}`**：辅音接元音或平滑过渡（如 `bailed` 接 `on` 连为 `bailed~on`）。

### 3.6 语调轮廓（Intonation Contours）

- **`↓`（`\tonefall`）**：降调。用于陈述句收束、特指问句结尾或确定判断；
- **`↑`（`\tonerise`）**：升调。用于一般疑问句、列举未完项或表示不确定；
- **`↘↗`（`\tonefallrise`）**：降升调。用于让步、含蓄保留或对比语境。

---

## 4. 黄金句记录结构

在 `reading_view.tex` 中采用标准的 `prosodybox` 呈现：

```latex
\begin{prosodybox}[黄金句 1 · 意群与信息重音]
  \prosodyorig{There's nothing like a good book to help me escape when the weather is too hot and humid to enjoy doing anything else.}
  \prosodyipa{\textbf{humid} \ipa{/ˈhjuːmɪd/} \quad$\bm{\cdot}$\quad \textbf{escape} \ipa{/ɪˈskeɪp/}}
  \prosodychunks{There's \stress{NOTHING LIKE} a \stress{GOOD BOOK} \chunk to help me \stress{ESCAPE} \chunk when the weather is \stress{TOO HOT} and \stress{HUMID} \chunk to enjoy doing \stress{ANYTHING ELSE}. \tonefall}
  \prosodyfocus{nothing like, good book, escape, too hot, humid, anything else}
  \prosodyflaws{
    \item \texttt{humid} \ipa{/ˈhjuːmɪd/} 的主重音在第一音节；先保证词本身清楚，再放入整句节奏。
    \item \texttt{nothing like a} 保持平滑衔接，避免在功能词处人为卡顿。
  }
\end{prosodybox}
```

---

## 5. 训练执行动作（五步纯文本自练法）

1. **音标对齐**：先确认生词与核心词的 IPA 音标及主重音音节；
2. **静读断句**：划出意群斜杠 ` / `（`\chunk`）；
3. **定位焦点**：圈出整句承担核心信息的重音词（`\stress{...}`）；
4. **轻重与连读**：读出重音词的饱满度，同时压低并弱化功能词（`\weak{...}`），衔接连读（`\phonlink`）；
5. **语调收束与脱稿**：赋予自然的降调 `↓` 或升调 `↑`，脱离视线连贯诵出整句节奏。
