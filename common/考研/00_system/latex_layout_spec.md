# LaTeX 视觉与布局规范

> **Owner**：本文件拥有 I.P.A.R.A LaTeX 的**具体视觉与几何参数**：字体基线、字号、版心预算、表格、代码、TikZ、图表间距与视觉迁移验收。
>
> **上位技术契约**：Family / Profile / Variant、KOMA/CTeX/IPARA 分工、Semantic API、margin/wide/fullwidth 页面状态、依赖与兼容策略统一由全局 [`common/latex/README.md`](../../latex/README.md) 拥有；本仓库的 [`latex_design_system.md`](latex_design_system.md) 只提供领域路由。
>
> **其他边界**：认知结构由 `handbook_writing_spec.md` 拥有；Handbook 物理身份由 `handbook_contract.md` 拥有；发布安全由 `repository_integrity.md` 拥有。本文件只回答：**已经确定使用某个 Family/Profile 后，具体怎样稳定、清晰、可维护地排出来。**

## 1. 总原则：统一底座，不统一每一页

本项目采用 **Forward Standard + Opportunistic Migration**：

1. **新建 Canonical `.tex`**：在正式 `ipara-handbook.cls` 通过回归 Gate 前，继续使用根目录 `ipara-handbook.sty` 作为过渡 Prototype；目标架构与迁移阶段见全局 `../../latex/README.md`；
2. **已有 Canonical `.tex`**：不为了视觉一致性批量重写；当该册本来就发生较大正文修订、Preamble 维护或明显排版缺陷时，再顺手迁移；
3. **legacy / Source `.tex`**：不做样式迁移；
4. **Published PDF**：不因为样式升级单独重编；只有 Canonical Source 真实修改后才重新发布；
5. **允许局部设计差异**：数学图、状态机、协议时序图、几何图可以保留学科适配器，但字体、版心、基础色彩、表格行为、代码字体和常用语义框应共享底座。

因此目标不是“所有旧 PDF 长得完全一样”，而是：

$$
\boxed{\text{Common Typography} + \text{Common Geometry} + \text{Common Components} + \text{Local Diagram Adapter}}
$$

---

## 2. 当前过渡样式入口

在目标 `ipara-handbook.cls` 落地前，当前 Handbook Prototype 的最小 Preamble：

```latex
\documentclass[UTF8,fontset=none,11pt,a4paper]{ctexart}
\usepackage{ipara-handbook}

\handbooksetup
  {PDF 标题}
  {左页眉：课程 · 学科 · Topic ID}
  {右页眉：3--4 个关键词}
```

当前 Prototype 负责：

- A4 版心与页眉页脚；
- 中英文字体、数学字体、代码字体；
- 标题层级；
- `booktabs / tabularx / longtable / array`；
- `corebox / methodbox / warnbox / examplebox / boundarybox`；
- `Y / L / C / R` 表格列；
- `handbooktable / boundarytable`；
- `listings` 代码基线；
- TikZ 常用节点、连线、标签样式。

正文只加载真正属于该册的额外包或 TikZ library。不要再逐册复制颜色、页边距、列类型和四类 `tcolorbox`。

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
\boxed{W_{table}=\linewidth}
$$

正常不需要再缩成 `0.95\linewidth`。表格天然是文字结构，充分使用当前版心通常更易读。

### 5.2 图与流程图

普通概念图推荐：

$$
0.82\linewidth \lesssim W_{diagram}\lesssim 0.94\linewidth
$$

硬上限：

$$
\boxed{W_{diagram}\le 0.96\linewidth}
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

## 8. 图与流程图：先设计拓扑，再画节点

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

## 14. 迁移策略

### Level 0：不动

满足以下条件时不迁移旧册：

- 已发布、无明显排版错误；
- 当前没有内容修改需求；
- 只是颜色/字体与新规范略有差异。

### Level 1：顺手收口

在正式 class 尚未通过回归 Gate 前，当某册本来就要修改 1--2 个 section 时，可先只替换：

- `documentclass` 切到 `fontset=none`，由当前 Prototype 唯一设置 CJK 字体；
- 旧公共 Preamble → `\usepackage{ipara-handbook}`；
- 保留该册特有 TikZ style。

正式 `ipara-handbook.cls` 稳定后，再按全局 `../../latex/README.md` 的迁移阶段更新此处入口；不要在过渡期维护两套新 API。

### Level 2：完整迁移

只有以下情况值得完整迁移：

- Preamble 已经产生明显重复/冲突；
- 表格或图频繁溢出；
- 字体导致跨机器编译失败；
- 该册正在进行大规模 Canonical 重写。

迁移不等于内容升级；不要因为视觉迁移擅自改变 Handbook 状态。

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

- 视觉轴有明确语义；
- 主路径一眼可追踪；
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
