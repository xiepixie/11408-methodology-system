# LaTeX 视觉与布局规范

> **Owner**：本文件拥有 I.P.A.R.A LaTeX 的**具体视觉与几何参数**：字体基线、字号、版心预算、表格、代码、TikZ、图表间距与视觉迁移验收。
>
> **上位技术契约**：Family / Profile / Variant、KOMA/CTeX/IPARA 分工、Semantic API、margin/wide/fullwidth 页面状态、依赖与兼容策略统一由全局 [`infra/latex/README.md`](../../infra/latex/README.md) 拥有；本仓库的 [`latex_design_system.md`](latex_design_system.md) 只提供领域路由。
>
> **其他边界**：认知结构由 `handbook_writing_spec.md` 拥有；跨学科图示语义由 [`diagram_design_spec.md`](diagram_design_spec.md) 拥有；Handbook 物理身份由 `handbook_contract.md` 拥有；发布安全由 `repository_integrity.md` 拥有。本文件只回答：**已经确定使用某个 Family/Profile 后，具体怎样稳定、清晰、可维护地排出来。**

## 1. 总原则：统一底座，不统一每一页

本项目采用 **Forward Standard + Opportunistic Compatibility Cutover**：

1. **新建 Canonical `.tex`**：优先使用正式 `infra/latex/ipara-handbook.cls`，默认 `profile=standard`；只有确有 supplementary semantic margin 价值时才显式选择 `profile=margin`；
2. **已有 Prototype Canonical `.tex`**：可继续使用 `kaoyan/ipara-handbook.sty` 稳定编译，不为了视觉一致性批量重写；当该册本来就发生较大正文修订、Preamble 维护或明显排版/可移植性缺陷时，再切到正式 Family API；
3. **legacy / Source `.tex`**：不做样式迁移；
4. **Published PDF**：不因为样式升级单独重编；只有 Canonical Source 真实修改后才重新发布；
5. **允许局部设计差异**：数学图、状态机、协议时序图、几何图可以保留学科适配器，但字体、版心、基础色彩、表格行为、代码字体和常用语义框应共享底座。

因此目标不是“所有旧 PDF 长得完全一样”，而是：

$$
\boxed{\text{Common Typography} + \text{Common Geometry} + \text{Common Components} + \text{Local Diagram Adapter}}
$$

---

## 2. Forward Standard 与兼容入口

新建 Canonical Handbook 的最小 Preamble：

```latex
\documentclass[profile=standard,twoside=false]{ipara-handbook}

\handbooksetup
  {PDF 标题}
  {左页眉：课程 · 学科 · Topic ID}
  {右页眉：3--4 个关键词}
```

`profile=margin` 不是默认换皮主题；只有正文主链在遮住 margin 后仍完整闭合、边栏确实承载 supplementary 信息时才使用。

既有文档若仍采用：

```latex
\documentclass[UTF8,fontset=none,11pt,a4paper]{ctexart}
\usepackage{ipara-handbook}
```

则视为 **Kaoyan Prototype Compatibility Surface**。它可以继续稳定发布，但不作为新建 Handbook 的模板。

正式 `ipara-handbook.cls + ipara-core.sty` 负责：

- A4 版心与页眉页脚；
- 中英文字体、数学字体、代码字体；
- 标题层级；
- `booktabs / xltabular / longtable / array`；
- `mentalmodel / mechanism / criterion / boundary / example / warning` 六类稳定语义环境；
- `Y / L / C / R` 表格列；
- `handbooktable / handbooklongtable / boundarytable`；
- `listings` 代码基线；
- TikZ 常用节点、连线、标签样式。

Prototype 中的 `corebox / methodbox / warnbox / examplebox / boundarybox` 只属于存量兼容语法，不再写入新模板。正文只加载真正属于该册的额外包或 TikZ library；不要逐册复制颜色、页边距、列类型或语义框实现。

---

## 3. 字体契约

### 3.1 为什么不用机器本地字体

Canonical Handbook 必须能在另一台装有标准 TeX Live 的机器上复现。不要把系统安装的苹方、思源、JetBrains Mono 等字体作为编译前提。

默认全部选用 TeX Live 自带字体：

| 职责 | 字体 |
|---|---|
| 中文正文 | FandolSong |
| 中文标题 / 无衬线 | FandolHei |
| 中文强调 / 楷体语义 | FandolKai |
| 中文等宽 | FandolFang |
| 英文正文 | TeX Gyre Pagella |
| 英文无衬线 | TeX Gyre Heros |
| 数学 | TeX Gyre Pagella Math |
| 代码 | TeX Gyre Cursor |

这套组合的优先级是：**跨机器可编译 > 视觉一致 > 个性化字体**。

### 3.2 字号

- Canonical Handbook：`11pt`；
- 表格正文、图中标签、代码：通常 `\small`；
- 箭线短标签：允许 `\scriptsize`；
- 不用整页 `\footnotesize` 挽救几何超载；如果必须缩到 `\footnotesize` 才能装下，先重构表格或图的拓扑。

### 3.3 数学符号与定界符规范（全仓 Markdown 笔记与 LaTeX 通用标准）

无论是在正式 `.tex` 手册，还是在日常 Markdown 笔记（`*.md`）、题解与草稿中，**只要进入数学公式环境（`$...$` 或 `$$...$$`），必须严格遵循统一的数学符号与定界符契约**：

1. **绝对值与模长（Absolute Value / Modulus）**：
   - 统一使用 `\lvert ... \rvert`（动态伸缩使用 `\left\lvert ... \right\rvert`），写作 `\lvert x \rvert`、`\lvert f(x) \rvert`；
   - **严禁直接使用键盘单竖线 `|x|`**：因为键盘单竖线 `|` 在 $\TeX$/MathJax 中缺乏开闭定界符语义（会被识别为 `\mathord`）。当内部出现负号如 `|-x|` 时，负号会被错判为二元减号运算符，从而在左右产生异常的大间隙；
2. **范数（Norm）**：
   - 统一使用 `\lVert ... \rVert`（动态伸缩使用 `\left\lVert ... \right\rVert`），写作 `\lVert \boldsymbol{x} \rVert`；
   - **严禁双竖线拼接 `||x||`**：字符拼接会导致双线间距失真与跨平台字体渲染断裂；
3. **条件与集合定界（Condition / Set Builder）**：
   - 条件概率与集合条件一律使用 `\mid`（如 `$P(A \mid B)$`、`$\{x \in \mathbb{R} \mid x > 0\}$`），严禁使用单竖线 `|`；
4. **微积分与变量类型**：
   - 正体微分算子使用 `\mathrm{d}`，偏导使用 `\partial`，写作 `\mathrm{d}x`、`\frac{\partial z}{\partial x}`；
   - 向量与矩阵使用粗斜体 `\boldsymbol{x}`、`\boldsymbol{A}`，严禁使用过时的 `\pmb`；
   - 基础常数与特殊函数名：自然底数使用正体 `\mathrm{e}^x`，函数名使用内置算子 `\lim`、`\sin`、`\cos`、`\ln`；
   - 不等号统一使用 `\le` 与 `\ge`。

---

## 4. 版心与“模式隔离”

### 4.1 唯一几何真值是当前 `\linewidth`

A4、左右约 `1.8cm` 边距时正文宽度约为 `17.4cm`，但这只是顶层页面的结果。进入以下环境后，可用宽度会改变：

- `tcolorbox`；
- `minipage`；
- 双栏；
- 列表环境；
- 以后可能出现的 poster 子区块。

因此：

> **任何局部图、表、规则线、minipage 的宽度预算以当前 `\linewidth` 为准，不以 `\textwidth` 或固定厘米数为准。**

`\textwidth` 只表示页面主版心，不知道当前对象是否已经处在更窄的容器里。

### 4.2 Block Object 必须显式结束前一段

用户提供的“水平/垂直模式隔离”方向正确，但需要更精确地写：

- `tabularx` 本质上可以成为行内盒子；如果直接接在尚未结束的段落后，它可能被当作当前水平列表的一部分；
- 单纯“留空行”通常可以结束段落，但直接裸用 `tabularx` 时还可能继承段首缩进；
- 因此稳定写法不是只记“空一行”，而是：**裸 block 前使用 `\par\noindent`，或者使用本身建立 block context 的环境。**

推荐：

```latex
\par\noindent
\begin{tabularx}{\linewidth}{...}
...
\end{tabularx}
```

更推荐直接使用公共环境：

```latex
\begin{handbooktable}{L{2.5cm}YY}
...
\end{handbooktable}
```

`handbooktable` 已经负责 `\par`、`\noindent`、局部分组、字号、行高和 `\linewidth` 包络。

---

## 5. 几何包络预算

### 5.1 表格

表格目标宽度：

$$
\boxed{W_{\text{table}} = \text{linewidth}}
$$

正常不需要再缩成 `0.95\linewidth`。表格天然是文字结构，充分使用当前版心通常更易读。

### 5.2 图与流程图

普通概念图推荐：

$$
0.82 \times \text{linewidth} \lesssim W_{\text{diagram}} \lesssim 0.94 \times \text{linewidth}
$$

硬上限：

$$
\boxed{W_{\text{diagram}} \le 0.96 \times \text{linewidth}}
$$

这不是要求每张图都填满 96%。它只是给节点、箭头、标注留出左右安全区。

**不采用固定 `13.6cm` 上限。** 固定厘米数无法适配 box/minipage，也会让简单图无意义地变宽。

### 5.3 自动缩放是最后手段

如果图超过版心，修复顺序：

```text
删冗余标签
→ 改节点文案
→ 重做层级/路由
→ 增加局部换行
→ 必要时拆成两张图
→ 最后才整体缩放
```

不要一开始就 `\resizebox{\linewidth}{!}{...}`。它会把本来已经偏小的文字一起缩掉，只是把“越界”伪装成“看不清”。

---

## 6. 表格规范

### 6.1 先决定列的职责，再决定列宽

表格列分三类：

1. **短标签列**：固定宽度 `L{...}` / `C{...}`；
2. **长解释列**：自适应 `Y`；
3. **符号列**：窄 `C{...}`。

优先让长解释列使用 `Y`，不要把整张表写成多个固定 `p{}`。

### 6.2 修正“p 列被 token 撑宽”的说法

`p{w}` 的列宽本身是固定的。长、不可断开的 token 更常造成：

```text
Overfull \hbox inside cell
```

而不是把 `p{w}` 自动扩成更宽的列。

真正的解决顺序：

1. 能否换成更短、语义更好的显示名；
2. 标识符能否允许断点，例如在 `/`、`-`、`→` 附近换行；
3. 该列是否本来就应该更宽；
4. 是否应该把“标识符 + 解释”拆成两列；
5. 最后才压字号。

因此不建立“最大 token 宽度 + 0.8cm”的机械公式。它可以作为人工估算，但不是 LaTeX 的列宽定律。

### 6.3 列宽预算

使用 `tabularx` / `xltabular` 时，不手算每个 `X` / `Y` 的最终宽度；只需要保证：

- 固定列总和不要吞掉绝大部分 `\linewidth`；
- 还要给列间的 `\tabcolsep` 留空间；
- 至少一个长解释列保留足够伸缩空间。

经验线：

- 3 列表：固定列总宽通常不超过 `0.35\linewidth`；
- 4 列表：固定列总宽通常不超过 `0.45\linewidth`；
- 5 列“概念边界表”：使用公共 `boundarytable`，不要每册重新猜宽度。

### 6.4 `\arraybackslash`

用户提供的规则成立，但应推广到所有带 `\RaggedRight / \Centering` 修饰的段落列，而不是只盯最后一列。

公共列类型已经封装：

```latex
Y          % ragged-right X
L{2.5cm}   % ragged-right fixed width
C{1.2cm}   % centered fixed width
R{1.8cm}   % right-aligned fixed width
```

不要在每册重复：

```latex
>{\raggedright\arraybackslash}X
```

### 6.5 行高与内边距

默认：

```latex
\arraystretch = 1.22
\tabcolsep    = 4pt
\extrarowheight = 1pt
```

允许**局部**在 `\begingroup ... \endgroup` 内调整。

不把 `\\[10pt]` 当作表格行高系统。只有某一行确实需要额外语义间距时才局部使用小幅附加空间。

### 6.6 三线表优先

默认使用：

```latex
\toprule
\midrule
\bottomrule
```

不要同时混用 `booktabs` 和大量 `\hline` / 竖线。网格表只保留给真正需要“格子语义”的状态表、逐格计算表或教学填写表。

### 6.7 跨页表：优先 `handbooklongtable`，不要再手算“剩余列”

Real Topic04 验证了一个仓库级旧债：raw `longtable` 常写成

```latex
\begin{longtable}{L{3.0cm}L{4.25cm}L{\dimexpr\linewidth-7.25cm\relax}}
```

这看似正好等于 `\linewidth`，但 `L{w}` / `p{w}` 的 `w` 是**内容宽度**，列左右还有 `\tabcolsep`。三列在 `\tabcolsep=3pt` 时会额外产生约 `18pt`，因此 Topic04 原 Canonical 在旧样式下稳定 Overfull；换新 class 并不会自动修复这个数学预算错误。2026-08-11 的真实迁移已经把 Topic04 三张跨页表全部改为 `handbooklongtable + Y`，原来的 18pt / 8.04pt / 18pt 三处表格溢出全部消失，并在 transitional Prototype、KOMA standard、KOMA margin 三路回归中保持零诊断。

未来跨页表优先使用 Handbook Family 提供的：

```latex
\begin{handbooklongtable}{L{3cm}L{4.25cm}Y}
...
\end{handbooklongtable}
```

它基于 `xltabular`：保留 `longtable` 的分页能力，同时让 `Y` 像 `tabularx` 的 `X` 一样消费真正的剩余宽度。短标签列可以固定，长解释列不要再写 `\linewidth - 固定宽度和`。

迁移顺序：

```text
raw longtable exact-width arithmetic
→ 固定真正需要固定的短列
→ 长解释列改 Y
→ handbooklongtable
→ 编译检查分页与表头
```

只有表格确实需要所有列固定物理宽度时，才人工预算内容宽度 + 全部 column padding；此时必须让最终实际表宽 `<= \linewidth`。

`tabularx` 本身不跨页。预计超过约半页、或内容长度不可控时，不要等到表格整块掉到下一页再修。

### 6.8 有序过程链：用 `processchain`，不要硬塞进一行公式

当一个流程本质上是**有序离散阶段**，而不是代数公式时，不要写成：

```latex
\[
\boxed{A\to B\to C\to D\to E\to F}
\]
```

这种写法会把整个结构变成一个不可自然换行的数学对象；在 standard 宽版心里可能侥幸放得下，进入 margin 主栏后就会直接 Overfull。

未来使用：

```latex
\begin{processchain}
  \processstage{Target}
  \processstage{Auxiliary Function}
  \processstage{Qualification}
  \processstage{Boundary / Zero Design}
  \processstage{Witness}
  \processstage{Translate Back}
\end{processchain}
```

当前 `processchain` 的契约是：

- 每个 stage 保持原子性，不在阶段内部任意拆字；
- 只允许在箭头边界换行；
- standard / margin 使用同一正文源；
- 它是**结构显示组件**，不是新的 Knowledge asset type；
- 如果单个 stage 自身已经过长，先缩短 stage label，再把解释放回正文，不靠缩字号解决。

Topic04 的两条六阶段母模型已完成真实迁移。迁移后 margin profile 原有的一行流程溢出消失，同时 standard 与旧兼容入口保持零诊断。

---

## 7. 5 列概念边界表

`handbook_writing_spec.md` 已确定概念边界使用 5 列：

```text
概念 A | ≠ | 概念 B | 真正区别与题目信号 | 混淆后果
```

未来直接使用：

```latex
\begin{boundarytable}
\boundarytablehead
Routing & ≠ & Forwarding
  & Routing 负责生成可用路由状态；给出现成表做 LPM 时属于 Forwarding
  & 会把控制平面与数据平面混为一谈 \\
\bottomrule
\end{boundarytable}
```

这样“5 列长表格”的视觉和宽度不再每册重新设计。

---

## 8. 图与流程图：语义先由统一图示规范确定，本文件只负责工程落地

### 8.0 本文件只接管“怎样画清楚”

图为什么存在、对象/关系/不变量如何编码、哪些视觉变量具有语义、度量图与结构示意图怎样区分、怎样攻击额外结构，统一由 [`diagram_design_spec.md`](diagram_design_spec.md) 拥有。

本文件只接管工程呈现层：

```text
图示语义已确定
→ 拓扑
→ 端口 / 走廊
→ 几何
→ 版心与字号
→ 样式与主题
→ 工程验收
```

- Topic / Bridge / Integration 训练图的图意图、集中图审、Owner 与复用生命周期由 `topic_practice_writing_spec.md` 负责；
- 本文件拥有 TikZ/PGF 的跨学科几何工程、布局、路由与主题约束；
- `infra/latex/` 继续拥有 Family / Profile / Semantic API 与编译底座。

进入 TikZ 坐标前，必须已经完成 `diagram_design_spec.md` 的视觉解释契约与语义编码。若这些尚不清楚，先不要开始调坐标。

### 8.1 保留“Grid First”，取消“所有图必须正交”

用户提供的 **Grid-First Matrix Design** 很适合 OS 状态、协议层、流水线、存储层次等结构图。但“100% 正交、零交叉”不能变成全局铁律：

- 几何图本来就需要斜线；
- 函数/向量图需要真实方向；
- 稠密依赖图有时无法零交叉；
- 强行正交可能让路径绕得比交叉更难读。

全局规则改为：

> **先确定视觉轴的语义，再最小化交叉；正交只是状态/层次/流程图的默认路由，不是所有 TikZ 的几何定律。**

### 8.2 画图前必须先回答四件事

1. **节点是什么对象？**
2. **空间轴分别表达什么？** 时间、层级、驻留位置、抽象层、数据流方向，还是纯几何坐标？
3. **边表示什么？** 因果、状态转移、调用、数据流、映射、Use，还是仅关联？
4. **读图主路径从哪里到哪里？**

如果这四件事没有答案，先不要写 TikZ 坐标。

### 8.3 先按语义给边分类

流程/状态/架构图至少区分三类边：

- **Primary Flow**：主要控制顺序、时间顺序或推理顺序；占据主阅读轴；
- **Support / Dependency**：调用、依赖、补充说明；不得抢占主流程视觉中心；
- **Feedback / Fallback**：失败回退、条件不足、重新检查、重新构造。

Feedback / Fallback 再按拓扑作用区分：

- **Local Feedback**：只返回相邻或局部阶段，不需要逆穿主阅读轴，也不需要跨过无关主流程节点；
- **Long-range / Backward Feedback**：返回更早阶段，需要逆向跨越主流程或绕过一个以上无关阶段。

这一区分依据的是**拓扑关系**，不是厘米距离。短的局部回退不必为了“像反馈”而绕整张图；真正会破坏主阅读路径的长距离/逆向反馈才应优先外围化。

“横向/纵向代表什么”仍是**图内契约**。例如七态进程模型可以规定 X 为运行生命周期、Y 为驻留/挂起层级，此时垂直边自然可以表示 swap；但不把“垂直 = swap、水平 = 逻辑演进”升级为全仓 TikZ 规则。

### 8.4 节点按包络处理，并先完成 Port Allocation

TikZ 节点不是一个坐标点，而是一个占据空间的对象。任何连线路由都必须把节点的矩形/形状包络当作不可穿越区域。

对每条非平凡连线，先确定三件事：

1. **Source Port**：从源节点哪一侧离开；
2. **Target Port**：从目标节点哪一侧接入；
3. **Route Corridor**：主要沿主轴、局部空隙还是外围通道行进。

对节点的 `north / south / east / west` 四侧，再根据**当前图布局**判断：

- **free side**：附近没有其他节点、标签或主流程占据，接入后归属清楚；
- **blocked side**：接入会造成遮挡、净距不足或“看起来像连到另一个节点”的归属歧义。

free / blocked 是 layout-local 状态，不是节点的永久属性。换一张图或重排节点后必须重新判断。

执行硬约束：

1. 连线不得穿越无关节点包络；
2. 连线不得贴近无关节点到足以造成归属误判；
3. 次级边不得长期占据主流程最重要的阅读走廊；
4. 某一侧即使几何距离最近，只要是 blocked side，就不得为了少一个折点强行接入；
5. 若找不到语义清楚的 Source Port、Target Port 或 Route Corridor，先重排节点，不靠增加复杂曲线补救。

因此“最短路径”不是最高优先级；**语义归属清楚**高于几何距离最短。

### 8.5 路由优先级由边类型决定

Primary Flow：

$$
\boxed{Direct \rightarrow One\ Bend \rightarrow Orthogonal \rightarrow Outer\ Route}
$$

Local Feedback：

$$
\boxed{Direct/One\ Bend \rightarrow Orthogonal \rightarrow Outer\ Route}
$$

Long-range / Backward Feedback：

$$
\boxed{Outer\ Route \rightarrow Orthogonal \rightarrow One\ Bend \rightarrow Direct}
$$

Support / Dependency 不设机械排序：选择**不抢占主路径、端点归属清楚、总转折最少**的可读路线。

对应 TikZ：

- 直线：`--`；
- 简单折线：`|-` / `-|`；
- 复杂正交：增加 routing coordinate；
- 外围反馈：先离开源节点包络，进入外围 corridor，再从目标节点的 free side 接入。

默认避免自由手画长曲线，因为它很难稳定表达端口、走廊和其他节点之间的关系。

这里的稳定视觉语义是：

> **主流程优先占据中心；只有会干扰主流程的长距离/逆向反馈优先走外围。**

### 8.6 图表拓扑验收

每张流程/状态图至少通过以下检查：

1. **主路径一眼可见**：读者不看正文也能判断主要推进方向；
2. **端点无歧义**：每条非平凡边都能明确看出从哪个节点离开、接入哪个节点；
3. **反馈路由匹配语义**：Local Feedback 没有无意义大绕行，Long-range / Backward Feedback 没有逆穿主流程核心区；
4. **无包络穿越**：任何边都没有穿过无关节点；
5. **无归属歧义**：任何一条边都不会因为入射位置而看起来像连到旁边、上方或下方的节点；
6. **不用缩字逃避拓扑问题**：若必须整体缩小字体才能避免碰撞，先重排图。

只要第 2 或第 5 项存在明显误读可能，就视为图未通过验收，即使 LaTeX 能正常编译。

---

## 9. 连线标注

### 9.1 Clearance 是预算，不是精确公式

“边框净长 ≥ 标签宽度 + 安全余量”这个思想成立：

$$
Gap_{border} \gtrsim Width_{label} + Clearance
$$

但不需要把每条边都换算成厘米。我们的执行标准更直接：

- 边标签优先控制在 **2--6 个中文字符**或 **1--3 个英文词**；
- 标签用 `\scriptsize`，白底 `ipara label`；
- 标签两侧应肉眼保留明显净空；
- 一旦标签开始解释“为什么”，它就不该继续留在箭线上，应移到图注、legend 或正文。

### 9.2 标签层级

边上只放：

- 事件名；
- 动作名；
- 极短条件；
- 数据/控制信号名。

不要放完整句子或中英双语解释。

例如：

```text
preempt / time slice (抢占/时间片)
```

在图上应压成：

```text
抢占 / 时间片
```

英文术语在正文首次定义即可。

### 9.3 双向边

不把 `.15 / .165 / .240` 等固定角度锚点写成公共铁律。它们过度依赖节点大小，节点文案一改就可能失效。

优先顺序：

1. 单条 `<->`，如果两个方向没有不同语义；
2. `bend left / bend right`，如果方向标签不同；
3. 两条轻微 `xshift / yshift` 的平行正交边；
4. 最后才使用显式角度 anchor。

双向标签分别放 `above / below` 或 `left / right`，不要压在同一中心线上。

---

## 10. TikZ 公共视觉语言

当前 Prototype `ipara-handbook.sty` 提供：

```latex
ipara node
ipara state
ipara process
ipara edge
ipara ref
ipara emphasis
ipara label
```

推荐：

```latex
\begin{handbookdiagram}
\begin{tikzpicture}[node distance=16mm and 20mm]
  \node[ipara node] (a) {输入};
  \node[ipara process,right=of a] (b) {机制};
  \node[ipara state,right=of b] (c) {稳定状态};

  \draw[ipara edge] (a) -- node[ipara label,above]{处理} (b);
  \draw[ipara edge] (b) -- node[ipara label,above]{提交} (c);
\end{tikzpicture}
\diagramcaption{最小流程示意}
\end{handbookdiagram}
```

学科可以在此基础上定义局部 style，例如 `cacheline`、`probnode`、`geom`，但不要重新定义全仓字体和色彩系统。

### 10.3 TikZ 数学可视化与图表工程化通用规范

数学与系统图表的**正文插入位置、图中内容规划、认知职责、一般性、关系符号、对照原则和额外结构攻击**统一由 [`diagram_design_spec.md`](diagram_design_spec.md) 维护。本节只保留 TikZ/PGF 落地时的工程与样式约束，避免语义规则在两处漂移。

样式优化必须发生在图前内容规划之后。布局、颜色、卡片、留白和分层只能**重排已经确定的信息**，不得因为某种版式“看起来好看”就新增正文没有定义的对象、删除必要关系，或改变图原本的解释责任。

#### 1. 舒展画幅与保角保距几何真实性
- **舒展画幅原则**：
  - **宁愿画幅舒展，绝不让几何要素与注记拥挤挨靠**。图的第一宽度基准永远是当前容器的 `\linewidth`，与 §5.2 一致：普通单图优先落在约 $0.82\sim0.94\,\linewidth$，硬上限约 $0.96\,\linewidth$；窄而简单的图可以明显更小，不能为了“占满版心”无意义拉宽；
  - 固定厘米数只允许作为独立 SVG 预览时的**局部初始猜测**，不得覆盖 `\linewidth` 预算，也不得成为跨 Profile、Markdown、PDF 的全局尺寸契约；
  - 曲线极值、折转点与视口外框之间必须预留约 $15\%\sim20\%$ 的呼吸留白，严禁坐标轴端点箭头触碰或穿透标题与注记；
- **几何真实长宽比**：
  - 涉及垂直正交、保角变换、斜率 $\pm 1$ 折线、关于 $y=x$ 镜像对称时，坐标轴必须保持等比例（`axis equal image` 或真实长宽比），严禁纵向/横向过度压扁导致几何直觉失真。

#### 2. 物理分层与零干涉排布
- **PGF 显式三层图层栈**：
  - TikZ 默认按声明顺序压盖渲染。凡图中同时存在背景填充/辅助线、主体几何和文字标签，统一声明三层图层栈；极简单图也建议沿用同一模板，减少后续扩图时的遮挡回归：
    ```latex
    \pgfdeclarelayer{background}
    \pgfdeclarelayer{foreground}
    \pgfsetlayers{background,main,foreground}
    ```
  - **`background`**：网格、区域填充、辅助虚线、渐近线等不应压住主体的背景信息；
  - **`main`**：主曲线、主向量、核心结构、主要映射与连接关系；
  - **`foreground`**：必须盖过线条才能保持可读性的关键文字、公式标签、端点标记和必要前景注记。真正需要前景保证的对象应明确放入 `pgfonlayer{foreground}`，不能只声明图层却仍全部画在 `main`；
  - “文字优先可读”不等于允许大面积遮住关键几何。若标签必须靠大遮罩才能读清，先移动标签、调整走线或扩大画幅。
- **轴刻度与文字物理避让**：
  - 严禁在已有刻度数值的坐标轴点上叠加相同坐标的文字节点；
  - 严禁将总结性说明文字放置在坐标轴刻度数字区域（如 $x$ 轴正负刻度区）；
- **边界线标注引至最外侧空白端**：
  - 上下界（$y=M, y=m$）、水平渐近线等标注文本，统一引到图表最右侧空白端，不堆叠在 $y$ 轴刻度上；
- **背景遮罩作为安全防护，而非排版遮丑**：
  - 数据区内的关键注记必须添加背景遮罩 `fill=themebg, inner sep=1.5pt` 隔离背景线条；
  - 但**遮罩绝不能作为掩盖拥挤排版的借口**，严禁遮罩切断轴刻度、关键连线或相邻文字。

#### 2.1 项目默认样式：轻量、舒展、少框，但不牺牲结构边界

这是项目的**默认视觉偏好**，不是无条件覆盖语义的装饰规则：

- **总结文字默认去框化**：图底部或图旁的解释性总结优先使用无框、高对比度、短句式排印，避免厚重圆角框层层套叠；
- **有真实边界语义时保留框**：状态、存储单元、集合区域、协议字段、矩阵块等对象若“边界本身就是知识”，可以也应该使用边框，不能为了追求无框风格把结构边界删掉；
- **图内短、正文长**：图内保留对象名、数学符号、极短动作或结论；完整因果解释留给紧邻正文和图注；
- **优先留白而不是缩字**：内容拥挤时先扩大画幅、调整子图编排、移动注记或拆图，最后才考虑缩字号；
- **局部说明归属明确**：多子图的局部说明限定在各自子图包络内，不跨过中线借用相邻空间；
- **全图总结与局部说明分开**：若确实需要全图总结，放在所有子图之后并留出明显净空，不机械重复子图公式。

A4 宽版心下，全图总结与上方局部说明之间约 $0.8\text{cm}\sim1.0\text{cm}$ 可作为常见起始参考；窄栏、单子图或字号不同的场景应按真实文字包络调整。**验收目标是视觉分层明确、没有碰撞，而不是机械满足某个厘米数。**

#### 2.2 简单标签就近，复杂说明外置

- 点名式标签（例如支撑集 $D$、端点、特征方向、状态名）优先放在对应对象附近的空白区，让读者能立刻建立归属；
- 两行以上解释、长公式、积分限展开、条件列表等复杂内容，不要硬塞进几何中心。优先移到图旁说明区、独立卡片或正文；
- 卡片只在它确实能把“几何主体”和“较长代数说明”分开时使用，不把所有图统一做成卡片式布局；
- 卡片宽度由当前 `\linewidth` 与内容决定，以**标准术语不被生硬拆词、关键公式不出现难读断行**为硬目标。当前 A4 宽版心下，约 `7.2cm` 可作为较宽代数卡片的初始参考，不是跨 Profile 的硬下限；
- 卡片之间保留清楚净空。约 $0.5\text{cm}$ 可作为当前 A4 场景的起始参考，最终仍以实际文字包络和阅读隔离为准。

#### 3. 视觉主次层级契约（Visual Hierarchy）
- **主体前景（Primary Subject）**：当前考察的函数曲线、主值区间、可逆分支 —— 采用主题前景色或强调色（`blue!70!themefg` / `red!70!themefg`）、加粗实线（`line width=2.0pt~2.5pt`）；
- **全域背景（Context / Inactive）**：全域未限制曲线、周期延拓分支 —— 采用次级中性灰（`themegray`）、细线（`1.2pt~1.5pt`）、虚线（`dashed`）；
- **几何基准与动作连接（Guides & Mappings）**：对称轴、渐近线使用中性灰虚线（`dashed`）；投影垂线、正交连接使用细点线（`dotted`）或引导箭头。

#### 4. 多子图隔离契约
- 多子图之间必须保留足够的**视觉隔离带**，使相邻坐标轴、标题、标签、箭头和结论不会被误认为属于另一子图。默认先按当前总 `\linewidth` 预算子图宽度，再给隔离带留空间；
- $1.8\text{cm}\sim2.2\text{cm}$ 可作为 A4 宽版心下两幅中等尺寸坐标图的常见参考值，但**不是全仓硬阈值**。窄栏、较小子图或无坐标轴结构图应按实际标签包络与净空验收；
- 各子图的子标题、局部结论必须独立对齐于各自图框，互不跨界干扰；
- 如果三列或更多子图在满足可读字号、真实几何与安全隔离后会突破总画幅预算，优先改成 `2+1`、`2+2` 或纵向分组，不允许靠缩字、压轴或牺牲净空硬塞。

#### 5. 双主题与 Markdown 嵌入管线（Theme & Asset Contract）
- 严格使用 `themebg`、`themefg`、`themegray` 语义色彩宏；
- 由 `compile_tikz_to_svg.py` 编译生成暗色（`assets/*.svg`）与亮色（`assets/light/*.svg`）纯路径矢量文件；
- Markdown 正文统一采用原生图片链接：`!` + `[说明]` + `(./assets/图名.svg)`，严禁嵌入 HTML `<picture>` 或 `<img>` 标签。

#### 6. 图解注释语义色彩与高对比排版契约（Semantic Diagrammatic Palette）
数学与系统图表避免使用刺眼的高饱和原生红/蓝/绿，默认使用项目统一的高对比度语义色系；颜色只承担辅助编码，不能成为唯一信息通道：
1. **核心主体曲线（Primary Curve & Function）**：
   - **语义**：函数主曲线 $y=f(x)$、正向映射轨迹、正确收敛分支；
   - **宏写法**：`blue!75!themefg` 或十六进制（暗色 `#7EB6FF` / 亮色 `#1D63B8`）；
   - **线型**：加粗实线 `line width=2.0pt~2.5pt`。
2. **结论焦点 / 反例证伪 / 边界渐近线（Focus, Counterexamples & Traps）**：
   - **语义**：反例离散点、不可逆断点、渐近线 $y=M$、证伪算子；
   - **宏写法**：`red!75!themefg` 或十六进制（暗色 `#FF7B7B` / 亮色 `#C53030`）；
   - **线型**：加粗实线或带外框标记（如 `\draw[red!75!themefg, fill=themebg, line width=1.5pt] circle (2.5pt);`）。
3. **辅助算子 / 切线导数 / 中间状态（Operators, Tangents & Guides）**：
   - **语义**：切线斜率、中间变量 $u=g(x)$、极值点投影引导线；
   - **宏写法**：`orange!80!yellow` 或十六进制（暗色 `#F5B942` / 亮色 `#B86E00`）；
   - **线型**：细线 `1.2pt~1.5pt` 或虚线 `densely dashed`。
4. **区域填充 / 值域水平带（Bands & Area Fills）**：
   - **语义**：值域水平带 $[m, M]$、积分区域 $D$、不可逆信息债务区域；
   - **安全混色契约（严禁纯白混色陷阱）**：在 LaTeX `xcolor` 中，`color!N` 默认与**纯白（#FFFFFF）**混合，会导致暗色模式下生成刺眼白色亮斑！必须显式混合底色宏：
     - **暗色标准写法**：`fill=themecurve!20!themebg` 或 `fill=themecurve, fill opacity=0.25`；
     - **亮色标准写法**：`fill=themecurve!15!themebg` 或 `fill=themecurve, fill opacity=0.15`；
     - **全仓门禁强制**：`infra/scripts/compile_tikz_to_svg.py --lint` 会自动静态检查并拦截任何未混合 `!themebg` 的独立 `color!N`。
   - **要求**：绝不允许使用高不透明度深色直接大面积平涂遮挡主曲线。
5. **文字背景遮罩（Text Masking）与黑洞避坑契约**：
   - **单线穿字遮断**：仅在坐标轴或网格细线穿过字迹时使用 `\node[text=..., fill=themebg, inner sep=0.8pt] at (...) {注记};`；
   - **禁忌（黑洞补丁陷阱）**：严禁在已填充的几何区域（如积分带、极坐标微元、矩形）上方使用 `fill=themebg`，否则会在填充色块上抠出难看的黑色矩形方块；
   - **多行定理框定位**：多行定理、结论公式框一律移至图形外部纯净留白空间（如左上/右上无曲线走廊），不施加任何背景遮罩，保持字迹自然融入。

#### 7. TikZ 独立源文件标准开发模版（Standalone TikZ Template）
全仓所有新绘制的 TikZ 数学与计算机图表，必须保存于 `assets/src/<图名>.tex`，统一采用以下标准模板骨架：

```latex
\documentclass[dvisvgm,tikz,border=3pt]{standalone}
\usepackage{amsmath,amssymb}
\usepackage{pgfplots}
\usepackage{CJKutf8}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,calc,positioning,decorations.pathreplacing,patterns}

% ── 双主题语义色彩定义 (由编译管线自动注入与映射) ──
\definecolor{themebg}{HTML}{30362d}     % 背景底色 (暗色墨绿 / 亮色米白)
\definecolor{themefg}{HTML}{edf4e8}     % 主体前景 (暗色柔白 / 亮色炭黑)
\definecolor{themegray}{HTML}{9ea897}   % 中性网格与辅助虚线
\definecolor{themecurve}{HTML}{7eb6ff}  % 主体曲线与正向映射 (晶蓝 / 皇家蓝)
\definecolor{themealert}{HTML}{ff7b7b}  % 焦点/反例/边界渐近线 (珊瑚红 / 朱砂红)
\definecolor{themeamber}{HTML}{f5b942}  % 导数切线/中间算子 (暖金 / 金褐)

% ── 声明显式图层栈（强制文字与点标记处于 foreground 最顶层）──
\pgfdeclarelayer{background}
\pgfdeclarelayer{foreground}
\pgfsetlayers{background,main,foreground}

\begin{document}
\begin{CJK*}{UTF8}{gbsn}
\pagecolor{themebg}
\begin{tikzpicture}[color=themefg, text=themefg]

% 在此处编写你的 pgfplots 坐标系或 tikz 图形...

\end{tikzpicture}
\end{CJK*}
\end{document}
```

##### 编译与引用操作闭环：
1. **执行编译**：`python3 infra/scripts/compile_tikz_to_svg.py assets/src/<图名>.tex`；
2. **生成资产**：自动输出 `assets/<图名>.svg`（带自适应暗色）与 `assets/light/<图名>.svg`；
3. **Markdown 引用**：正文统一采用标准相对链接语法：`!` + `[说明文本]` + `(./assets/图名.svg)`。

#### 7.1 从手册内容到真实阅读视图的六步闭环

编译成功只说明“文件能生成”，不说明“图放在手册里真的好读”。新图按下面六步执行：

```text
第 1 步：回读具体手册并确定插入位置
        按 diagram_design_spec.md 读目标小节，写清前文已知、后文用途、图中必须出现/不得出现的内容。
→ 第 2 步：语义与拓扑设计
        决定对象、关系、不变量、图型、子图数量和标签；术语必须能从当前手册直接复原。
→ 第 3 步：按项目样式偏好做 TikZ/PGF 工程实现
        先服从当前 \linewidth，再采用轻量少框、充足留白、局部说明归位、关键标签前景可读等默认偏好；
        当前 A4 的厘米数只作为起始参考，不能反过来支配信息结构。
→ 第 4 步：生成暗色 / 亮色 SVG
        运行 python3 infra/scripts/compile_tikz_to_svg.py assets/src/<图名>.tex。
→ 第 5 步：视觉自检——既看孤立图，也看插回原文后的效果
        检查文字重合、线条穿字、端点遮挡、异常换行、边缘截断、子图归属、图与正文间距，以及深浅主题一致性。
→ 第 6 步：按使用范围做端到端验证
        Markdown 图至少检查实际 Obsidian/阅读视图；若同时嵌入 Handbook，再通过项目正式编译/发布入口检查目标 PDF、Overfull 警告与图文衔接；
        稳定改动最后按 AGENTS.md 运行相应 repository check / audit，不为了单张 Markdown 图机械执行无关的全仓重编。
```

**视觉自检必须看真实图像，不得只看 TikZ 源码或编译日志。** 在当前 macOS 环境，可用 `qlmanage -t -s 1600` 生成较高分辨率预览；其他环境使用等价 SVG/PDF 渲染器即可。`1600px` 适合作为复杂图的常用检查尺寸，但不是唯一合格分辨率。验收标准是实际阅读尺度下所有关键内容清楚、无碰撞、无误读。

如果工具支持直接打开 SVG/PDF，就直接检查；如果需要栅格化，再生成临时 PNG。不要把某个特定图像查看工具名称写成语义完成条件。

##### 同一几何图同时服务手册正文与 SVG 时的共享规则：

若某张图既要作为 Markdown 的暗/亮 SVG，又要直接嵌入规范手册 `.tex`，**严禁把完整的 `standalone` 图源直接 `\input` 到手册正文**。完整图源含 `\documentclass`、`\usepackage`、`\begin{document}`，嵌入正文会造成导言区命令越界；若正文外层还包了 `tikzpicture`，再输入一个自带 `tikzpicture` 的 body 还会形成嵌套 TikZ，可能触发字体选择递归或输入栈爆炸。

统一采用“正式图源包装器 + 单一几何 body”模式：

```text
assets/src/<中文语义图名>.tex          # 正式 standalone 图源，供 SVG 编译链调用
assets/src/<ascii_name>_body.tikz     # 唯一几何正文，只保存 tikzpicture 本体
```

- `<中文语义图名>.tex` 仍是对外唯一图源入口，负责主题色、CJK 环境与独立文档包装；
- `<ascii_name>_body.tikz` 只负责几何与标注，不另立知识/图形 Owner；正式图源与手册正文都引用这一份 body，禁止复制两套坐标；
- **内部 body 文件名必须使用 ASCII**。SVG 管线使用传统 `latex → dvisvgm`，其 `\input{中文文件名}` 在部分 TeX 环境下会解析失败；中文语义命名保留在正式 `.tex` 与派生 SVG stem 上即可；
- 若 body 已经包含 `\begin{tikzpicture}...\end{tikzpicture}`，手册正文应直接 `\input`，不得再额外套一层 `tikzpicture`；若选择只共享 picture 内部语句，则包装器与正文必须各自只包一层，二者择一并保持全仓一致；
- 修改图形时只改共享 body，再同时重编 SVG 与手册 PDF，确认两种视图没有发生语义漂移。

#### 8. 视图呈现与多媒体排版控制契约（Presentation & Sizing Contract）
在 Markdown / Obsidian / Web 视图与打印介质中，图表呈现严格遵循以下自适应与居中契约：
1. **全景居中（Universal Centering）**：所有多媒体图表默认采用 `display: block; margin-left: auto; margin-right: auto;` 保证在段落与版心中轴线上居中呈现；
2. **智能尺寸分流（Non-Destructive Sizing）**：
   - 严禁对所有图片无差别施加 `width: 100%` 强行拉伸；
   - 默认采用 `width: auto; max-width: 94%;`，使单概念窄图保持紧凑原生清晰度，多子图宽图（$\ge 2/3$ 版心）舒展延展并预留呼吸留白；
3. **打印与 PDF 导出防护（Print Mode Safety）**：
   - 触发 `@media print` 时，图表强制设置 `break-inside: avoid; max-width: 90%;`，防止图表被打印机从中间跨页切割；
   - 配合 SVG 内置媒体查询，背景色自动切为 `#FAFAF7` 纸质米白，文字与曲线切为高对比度印刷色。

---

## 11. 代码排版

### 11.1 统一字体

行内代码：

```latex
\code{fork()}
\code{RIB}
```

长路径 / URL-like token：

```latex
\codepath{/proc/<pid>/maps}
```

代码块默认 `listings` + 当前 Core baseline 的 TeX Gyre Cursor。未来字体 token 的最终 Owner 仍是本文件；不使用 `minted` 作为基础依赖，因为它需要 shell escape / Pygments，会增加发布链条件。

### 11.2 代码块原则

- 默认 `\small`；
- 自动换长行，但算法/程序示例应主动在语义断点换行；
- 不依靠彩虹式 syntax highlight 承担语义；
- 代码里的重点通过正文解释、注释或少量粗体，而不是很多颜色。

---

## 12. 图表标题与浮动

Handbook 的图表主要服务“读到这里就理解这里”，不是论文式统一收集。

默认：

- 小型概念图可用 `handbookdiagram` 固定在当前位置；
- 需要正式编号时用 `\diagramcaption{...}`；
- 大图或跨段复用图可以使用 `figure[htbp]`；
- 不滥用 `[H]` 强锁浮动，否则容易制造大块页底空白。

图注写**读图结论**，不要只重复图名。

---

## 13. 视觉密度与分页

一页出现以下情况时，优先拆结构而不是继续压缩：

- 3 个以上大 `tcolorbox` 连续堆叠；
- 一张图同时承担对象地图、生命周期和题目路由三种职责；
- 表格行高已经低于默认值仍然放不下；
- 图中文字普遍缩到 `\footnotesize`；
- 一个 section 标题被留在页尾，只剩 1--2 行正文。

可用 `\Needspace{4\baselineskip}` 保护需要和后文绑定的关键小标题/组件。

---

## 14. Compatibility Cutover 策略

### Level 0：稳定存量不动

满足以下条件时，既有 Prototype Handbook 不切换 Family API：

- 已发布、无明显排版错误；
- 当前没有内容修改需求；
- 只是颜色/字体与新规范略有差异。

### Level 1：真实修订时切到正式 Standard

当某册本来就要修改正文、Preamble 或修复排版/可移植性问题时，优先把入口收敛为：

```latex
\documentclass[profile=standard,twoside=false]{ipara-handbook}
```

同时：

- 删除被 Class/Core 已拥有的重复 Preamble；
- 保留该册真正特有的 TikZ / domain adapter；
- 用 `python3 infra/check_infra.py` 先证明全局 Family Gate，再通过 Kaoyan `publish` 验证该册自身。

### Level 2：只有真实信息架构收益才启用 Margin

`profile=margin` 只有以下条件同时成立时才采用：

- supplementary 信息有稳定语义，不是为了“页面更像书”；
- 遮住 margin 后 MainText 仍逻辑闭合；
- 奇偶页、widecontent、长表和图形已经过真实阅读回归。

Compatibility Cutover 不等于内容升级；不要因为 Family API 切换擅自改变 Handbook 状态。

---

## 15. 发布前视觉验收

新样式 Handbook 发布前至少检查：

### Typography

- 中文、英文、数学、代码字体是否统一；
- 是否出现系统字体缺失警告；
- 标题/正文层级是否明显但不过度装饰。

### Tables

- 使用 `\linewidth` 而非 box 内的 `\textwidth`；
- 无 `Overfull \hbox`；
- 固定列没有吞掉长解释列；
- 三线表没有混入无意义的竖线；
- 5 列边界表能快速扫描 A / B / Signal / Failure。

### Diagrams

- 已在 `diagram_design_spec.md` 中明确目标手册、准确插入位置、前后文职责与图中内容；
- 视觉轴有明确语义，主路径一眼可追踪；
- 背景 / 主体 / 前景需要分层时已真正使用 PGF layer，关键文字与端点不会被后画线条压住；
- 默认采用轻量少框排印；只有边界本身有语义时保留框；
- 多子图局部说明归属于各自子图，不跨界、不异常换行；
- 复杂说明区或卡片宽度由当前 `\linewidth` 和内容决定，没有为了守固定厘米数牺牲整体布局；
- 已检查暗色与亮色实际图像；复杂图使用足够高分辨率预览，无文字重合、字线相穿、端点遮挡或边缘截断；
- 图插回 Markdown / Handbook 后仍与上下文衔接自然，尺寸、留白和图注不会打断阅读；
- 非平凡边的 Source Port / Target Port 与 Route Corridor 清楚；
- Long-range / Backward Feedback 没有逆穿主流程核心区，Local Feedback 没有无意义大绕行；
- 无节点包络穿越、无端点归属歧义，交叉已最小化；
- 边标签短，且没有压到节点；
- 图没有靠整体缩小字体来逃避拓扑问题。

### Page envelope

- 无对象越出当前 `\linewidth`；
- 无标题孤零零留在页尾；
- 没有为了塞满一页而把文字压得明显小于全书基线。

---

## 16. 一句话标准

$$
\boxed{
\text{先统一可维护的底座}
\;\to\;
\text{再让每张表和每张图服从自己的信息结构}
}
$$

统一字体、版心和组件；不统一所有学科的图形语法。先预算 `\linewidth`，再预算列和节点；先修拓扑，最后才缩尺寸。
