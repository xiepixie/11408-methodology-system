# 真题与试卷 Source 转译规范

本规范用于把 **真题 PDF、扫描件或高清题图** 转换为长期可维护的 Obsidian Source。**408、数学一以及后续其他考试共用这一份转换合同，不为不同学科复制第二套转译规则。** 学科/年份差异只通过 Exam Profile、年度 `exam.json` 和题面本身表达。

执行提示词 Owner：[`exam_source_agent_prompt.md`](exam_source_agent_prompt.md)。本文件拥有真题 Source 的忠实重建、题面完整性、semantic id、答案泄露防护与 Source 验收合同；跨学科通用的视觉解释、关系编码、度量/示意区分与额外结构攻击统一调用 [`diagram_design_spec.md`](diagram_design_spec.md)，TikZ/PGF 工程调用 [`latex_layout_spec.md`](latex_layout_spec.md)。Prompt 只负责把这些规则转成每次 Agent 的执行顺序，三者不得复制出多套定义。真题原图若与一般视觉偏好冲突，**题面忠实性优先**。

本任务不是“PDF 换格式”，而是：

```text
发布态试卷（PDF / 扫描图）
-> 恢复题目结构
-> 恢复原生文本 / 数学 / 代码 / 图形
-> 校对到简单、正确、可编辑
-> 形成稳定的 Exam Source
```

最终产物服务两个下游：

1. **直接做题 / 查题**：在 Obsidian 中清楚、稳定、可搜索；
2. **后续学习加工**：可被 Evidence Mapping、错题诊断、Topic / Rules 验证直接引用。

---

## 1. 最终效果

一套已经完成的真题必须满足：

```text
Complete
+ Correct
+ Editable
+ Readable
+ Validated
```

### Complete｜完整

- 题号连续且无重复；
- 题干、选项、小问、分值、代码、表格、原题图均不遗漏；
- 图中承载解题条件的标签、数值、方向和连接关系完整。

### Correct｜正确

- 最终正文维护“正确的试题”，不是 OCR 结果，也不是扫描瑕疵的考古记录；
- 数字、符号、变量、下标、单位、代码操作符优先保证正确；
- 能确定的扫描/OCR/排版错误直接恢复为正确内容；
- 无法可靠判断时停止猜测，回到更清晰来源或请求人工确认。

### Editable｜原生可编辑

- 正文是 Markdown；
- 数学是 LaTeX；
- 程序是 fenced code block；
- 常规表格是 Markdown table；
- 结构图是 Semantic SVG；
- 不把整页试卷、代码、公式或结构图长期保存为截图代替源内容。

### Readable｜适合 Obsidian 阅读

- 默认暗色 SVG 与项目当前 Obsidian 背景协调；
- 同时提供亮色 SVG；
- 不依赖 Obsidian 对嵌入 SVG 的运行时主题继承；
- 图中文字、线条、阴影和节点在两种主题下均清楚。

### Validated｜可机器验证

- Markdown 引用的资产全部存在；
- SVG XML 可解析；
- dark / light 图形语义一致；
- 无意外嵌入整张 raster 原图；
- 题号、分值、代码围栏和资产引用通过基础检查。

---

## 2. 最终目录合同

稳定真题统一进入 `kaoyan/archives/<exam_id>/`，不再把完成态试卷留在 `80_evidence/inbox/`。其中 `<exam_id>` 由 Exam Profile 定义，例如 `math1`、`408`。默认目录合同：

```text
kaoyan/archives/<exam_id>/
└── <year>年真题/
    ├── <year> 年全国硕士研究生招生考试.md   # 核心契约：文件名与正文一级标题 1:1 完全相同
    ├── exam.json
    ├── README.md
    └── assets/
        ├── qNN_<semantic-name>.svg
        ├── ...
        └── light/
            ├── qNN_<semantic-name>.svg
            └── ...
```

### 2.0 核心排版与 LaTeX 规范（与 Handbook Design System 100% 对齐）

为了保证所有 Markdown 试卷在 Obsidian 与 LaTeX 导出中具备出版级的可读性、严密性与自洽性，严格遵守以下六大核心排版规则：

#### 规则 1：文件名与一级标题 1:1 绝对一致（Zero-Deviation H1 Contract）
- 每一个真题 Markdown 文件的文件名与正文首行一级标题（H1）必须 **100% 字符级相同**（如 `1990 年全国硕士研究生招生考试.md` $\iff$ `# 1990 年全国硕士研究生招生考试`）；
- 目录内仅允许保留唯一一份主 Markdown 文件，**严禁存在任何冗余、镜像或历史别名副本**。

#### 规则 2：大纲层级与题目结构节奏（Strict Hierarchy & Question Outlining）
- **大题分区（H2）**：统一使用标准大写题型标头，如 `## 一、填空题`、`## 二、选择题`、`## 三、解答题`、`## 七、（本题满分 6 分）`；
- **小题独占标头（H3）**：每个小题必须独占一行 `### <num>`，严禁题号与题干正文粘连，确保 Obsidian 大纲树（Outline）折叠、定位与双链引用顺畅；
- **选择题选项规范**：选项必须强制独立成行（行尾保留 Markdown 双空格换行）：
  ```markdown
  A. $-\mathrm{e}^{-x}f(\mathrm{e}^{-x}) - f(x)$  
  B. $-\mathrm{e}^{-x}f(\mathrm{e}^{-x}) + f(x)$  
  C. $\mathrm{e}^{-x}f(\mathrm{e}^{-x}) - f(x)$  
  D. $\mathrm{e}^{-x}f(\mathrm{e}^{-x}) + f(x)$  
  ```
- **填空题横线规范**：统一使用标准下划线 `______。` 或 `\underline{\quad\quad\quad\quad}.`。

#### 规则 3：独立行间公式块规范（Clean Display Math Block `$$ ... $$`）
- `$$` 必须独立成行，前后保留空行隔开；
- **完整性与抗碎裂**：同一次定义、并列矩阵（如 $\boldsymbol{B} = \begin{bmatrix}...\end{bmatrix}, \quad \boldsymbol{C} = \begin{bmatrix}...\end{bmatrix}$）或联立方程组必须封装在**同一个完整的 `$$ ... $$` 块**内；
- **严禁语法碎裂**：严禁将赋值符号（如 `\boldsymbol{B} = `）留在正文行而将矩阵单独包裹在 `$$` 中，严禁出现 `$$ ... $$ , \quad \boldsymbol{C} = $$ ... $$` 这种断裂语法；
- **严禁段落吞噬**：严禁将中文题干、选择题选项或 Markdown 标题吞入 `$$` 内部。

#### 规则 4：数学符号与变量类型严密性（Mathematical Type System）
- **绝对值与模长（Absolute Value / Modulus）**：一律使用 `\lvert ... \rvert`（动态伸缩使用 `\left\lvert ... \right\rvert`），写作 `\lvert x \rvert`、`\lvert f(x) \rvert`。
  - *严禁直接使用键盘单竖线 `|`*：因为单个 `|` 在 TeX/MathJax 中缺乏开闭语义（会被识别为 `\mathord`），遇到负号如 `\lvert -x \rvert` 时若写成 `|-x|` 会导致负号被错判为二元减号而产生异常的大间隙；
- **范数（Norm）**：一律强制使用 `\lVert ... \rVert`（动态伸缩使用 `\left\lVert ... \right\rVert`），写作 `\lVert \boldsymbol{x} \rVert`。
  - *严禁使用键盘双竖线拼接 `||x||`*：拼接双竖线会导致双线间距失真、断裂；
- **微分与偏导算子**：一律使用正体微分算子 $\mathrm{d}$ 与偏导符号 $\partial$，写作 `\mathrm{d}x`、`\mathrm{d}y`、`\frac{\partial z}{\partial x}`；
- **常数与特殊函数**：自然底数使用正体 `\mathrm{e}^x`，特殊函数写作 `\lim`、`\sin`、`\cos`、`\ln`；
- **向量与矩阵**：粗斜体使用 `\boldsymbol{\alpha}`、`\boldsymbol{\beta}`、`\boldsymbol{A}`、`\boldsymbol{B}`，严禁使用过时的 `\pmb`；
- **不等号标准化**：统一使用 `\le` 与 `\ge`。

#### 规则 5：多行环境平衡与定界符规范（LaTeX Environment Balance）
- 所有多行数学环境（`pmatrix`、`bmatrix`、`cases`、`aligned`）必须保证 `\begin` 与 `\end` 1:1 成对闭合；
- 联立方程组与分段函数统一使用 `\begin{cases} ... \end{cases}`，严禁使用圆括号矩阵 `pmatrix` 替代；
- 括号匹配严格自洽，集合与数列符号必须完全转义闭合（如 `\{f(x_n)\}`、`\{x_n\}`），严禁写出单侧不转义的 `\{f(x_n)}`；
- 条件概率统一使用 `\mid`（如 `$P\{Z \le \frac{1}{2} \mid X = 0\}$`），概率测度外层统一使用转义花括号 `$P\{ ... \}$`。

#### 规则 6：数学解析几何图形与 TikZ 编译标准（Analytic Geometry & Dual-Theme TikZ Pipeline）
数学图形（高数旋转体、空间二次曲面、二重/三重积分区域、参数曲线、概率分布曲线）具有高度的解析严格性，**绝不允许使用手工随意拉伸的贝塞尔曲线 SVG**。必须严格遵循以下标准：
1. **解析方程精确驱动**：
   - 所有函数曲线、外轮廓线、渐近线必须由严谨的数学解析方程（如 `plot (\x, {0.6*sqrt((\x/1.3)*(\x/1.3) - 1)})`）计算绘制，保证极值点、切线斜率与曲率严格准确；
2. **前实后虚与空间遮挡原则（Occlusion Principle）**：
   - 严格遵循 `AGENTS.md` 规范：背面被遮挡的几何轮廓、纬线后半弧、坐标轴穿过曲面内部部分一律使用虚线（`dashed`），前方可见轮廓与前截面使用实线；
   - 三维空间采用标准斜二测投影（$x$ 轴水平向右，$z$ 轴铅直向上，$y$ 轴斜 45 度投影）；
3. **源码资产留存契约（Source Asset Preservation）**：
   - 每一个数学矢量图必须在对应年份资产目录下建立源码文件：`assets/src/<semantic_name>.tex`（或 `assets/tikz/<semantic_name>.tex`），严禁丢弃 TikZ 源码；
4. **全平台免字体依赖矢量编译（`dvisvgm --no-fonts`）**：
   - 统一使用 `infra/scripts/compile_tikz_to_svg.py` 执行底层 TikZ→SVG 渲染；具体年份/题图批处理范围由 Kaoyan domain tool 决定；
   - 强制使用 `--no-fonts --exact-bbox` 将数学公式与坐标字符（$x, y, z, 0, \theta$）直接栅格化为纯矢量 `<path>` 路径，彻底消除跨平台（Obsidian macOS/iOS/Windows）字体缺失或字体排版错位；
5. **1:1 纯净双主题输出（Dark & Light Pair）**：
   - 默认暗色版：`assets/<name>.svg`（底色 `#30362d`，线条/文字 `#edf4e8`，辅助线 `#9ea897`）；
   - 亮色版本：`assets/light/<name>.svg`（底色 `#fafaf7`，线条/文字 `#111111`，辅助线 `#666666`）。

```text
kaoyan/archives/math1/2008年真题/
├── 2008 年全国硕士研究生招生考试 数学（一）真题.md  # 核心契约：文件名与正文一级标题 1:1 完全相同
├── exam.json
├── README.md
├── q01_高等数学.md ~ q23_概率论与数理统计.md
└── assets/
    ├── q06_two_sheet_hyperboloid.svg           # 暗色标准矢量图
    ├── light/
    │   └── q06_two_sheet_hyperboloid.svg     # 亮色标准矢量图
    └── src/
        └── q06_two_sheet_hyperboloid.tex     # 官方 TikZ 解析几何源码
```

数学一真题归档（`kaoyan/archives/math1/`）与 408（`kaoyan/archives/408/`）均执行本规范；不要为了数学另复制一份 `exam_source_conversion_spec`。

### README 只做目录说明

README 保持短小，只说明：

- 主文件；
- `exam.json`；
- 默认 SVG 主题；
- `assets/light/` 的用途；
- “只维护题面，不放答案与解析”的边界。

最终 Pack **不维护长篇 OCR 日志、历史争议、Primary/Secondary 考古或诊断结论**。

工作过程中可以临时比较多个来源，但这些中间过程不应污染完成后的真题正文。

### 2.1 两层元数据：Exam Profile + Exam Instance

真题元数据分为两层，避免每一年重复维护考试制度本身的稳定结构。

```text
Exam Profile
= 一类考试长期稳定的结构

Exam Instance
= 某一年 / 某一套试卷自己的事实
```

#### Exam Profile｜考试结构 Owner

位置：

```text
00_system/exam_profiles/<profile_id>.json
```

Profile 只保存**稳定不变**的考试结构，例如：

- 总分、题量、考试时长；
- 题型区间；
- 固定学科题号区间；
- 固定学科分值配额；
- 可由题号直接推出的路由规则。

如果考试结构发生真实变化，应建立新的 Profile ID，而不是在一个旧 Profile 中堆大量年份例外。

#### Exam Instance｜年度试卷元数据

每套完成后的 Source Pack 必须有：

```text
exam.json
```

它只保存该套试卷自己的事实，例如：

```json
{
  "schema_version": 1,
  "exam_id": "408-2025",
  "profile_id": "408",
  "year": 2025,
  "title": "...",
  "main_file": "...md",
  "status": "ready",
  "question_count": 47,
  "total_score": 150,
  "question_scores": {"41": 13},
  "content_features": {
    "figures": [33],
    "code": [1],
    "tables": [11]
  },
  "figure_assets": {
    "33": "assets/q33_example.svg"
  }
}
```

年度实例**不要重复保存可以从 Profile 推出的信息**。例如 408 的 Q33 属于计算机网络、Q43 属于计算机组成原理，应由 `408` Profile 根据题号路由，而不是每一年再写 47 份 `subject` 标签。

#### 主 Markdown Frontmatter｜只保留最小身份

主试卷 Markdown 顶部只放常用检索字段：

```yaml
---
type: exam-source
exam_id: 408-2025
exam_profile: 408
year: 2025
status: ready
total_score: 150
question_count: 47
metadata_file: exam.json
---
```

不要把完整 `exam.json` 再复制进 Frontmatter。

#### 稳定 Question ID

题目稳定 ID 由元数据推导：

```text
<exam_id>-Q<两位题号>
```

例如：

```text
408-2025-Q01
408-2025-Q33
408-2025-Q47
```

这样后续答案、错题、Evidence Mapping、统计与 Topic 路由都可以引用稳定 Question ID，而不需要污染真题正文。

#### Source 元数据禁止承载的内容

以下内容不属于 Exam Source Metadata：

- 正确答案；
- 难度评价；
- AI 解析；
- Topic / Bridge / Rule 标签；
- 错题状态；
- 用户掌握度。

这些属于后续派生层，不能反向成为试卷 Source 的属性。

### 2.2 固定题号考试：优先用 Profile 路由

如果一门考试的学科位置长期固定，应显式写入 Exam Profile。

以 408 为例，Q1～Q40 的客观题路由长期稳定；综合应用题使用 Profile 的 **default routing + year override**，不能把常见年份的位置写成永恒事实。典型默认路由是：

```text
数据结构       Q1–Q11   + 默认 Q41–Q42
计算机组成原理 Q12–Q22  + 默认 Q43–Q44
操作系统       Q23–Q32  + 默认 Q45–Q46
计算机网络     Q33–Q40  + 默认 Q47
```

因此任何下游程序只需：

```text
exam_id + question_number
-> profile
-> subject / question type / 固定分值结构
```

不需要逐题重复人工标学科。

对于数学等可能存在历史结构变化的考试，应使用**版本化 Profile**；只有真正稳定的结构才进入 Profile，年份特有的信息仍留在 `exam.json`。

---

## 3. Source 选择与纠错原则

### 3.1 来源优先级

默认优先级：

```text
用户明确指定的高清原题 / 官方高清页
>
官方或可信原版 PDF
>
低清扫描 PDF
>
网页题库 / 他人转写 / 解析页
```

如果用户明确说“以这批图片为准”，立即以该批材料作为当前最高来源，不再让低清旧材料覆盖它。

### 3.2 最终维护“正确试题”，不是原始噪声

必须区分：

```text
题目内容
vs
扫描噪声 / OCR 错误 / 明显排版 typo
```

例如高清图把 `int` 扫成 `in`，且上下文能高度确定其为 C 声明，则最终题面应恢复为：

```c
int x, d[2048], i;
```

而不是在主文件里长期加入：

```text
[warning] 原图显示 in，疑似应为 int ...
```

### 3.3 不确定时不猜

以下情况必须重新查看高清区域或请求确认：

- 一个字符改变题意；
- 数字或单位模糊；
- 数学上下标无法区分；
- 代码比较符、括号或操作数不清楚；
- 图中箭头方向、标签归属不清楚；
- 两个可信来源给出不同且都合理的题面。

**宁可暂停一题，也不要把低置信内容批量写入最终 Source。**

---

## 4. PDF / 图片预检（Preflight）

开始批量转译前，先判断输入类型。

### A. Text-native PDF

特征：正文可选中，有可靠 text layer。

策略：

```text
text layer -> 初始文本
页面视觉 -> 校对版式、公式、上下标、图形和特殊符号
```

不要对可靠 text layer 再做整页 OCR。

### B. Scanned PDF

特征：页面本质是图片，没有可靠文本层。

策略：

```text
高分辨率页面图
-> 视觉转写
-> 结构恢复
-> 精校
```

OCR 只能作为粗候选或定位工具，不能直接成为最终题面。

### C. Hybrid PDF

正文、公式、图形分别使用最可靠来源：

- 文本层可靠的正文直接提取；
- 公式以视觉核对为准；
- 内嵌矢量图尽量利用原矢量信息；
- 扫描图或复杂题图重新构造成 SVG / raster asset。

### Preflight 必须得到的清单

至少确认：

```text
页数
题号范围
选择题 / 综合题边界
每题分值
包含图的题号
包含代码的题号
包含表格的题号
公式密集页
可能跨页的题目
```

**先建立 Coverage，再开始批量写文件。**

---

## 5. 页面不是输出单位，题目才是

禁止最终生成：

```text
page01.md
page02.md
page03.md
```

页面只是输入载体。输出应恢复考试的逻辑结构：

```markdown
## 一、单项选择题

### 1
...

### 2
...

## 二、综合应用题

### 41（本题 13 分）
...
```

跨页题必须合并回同一题，不保留无意义的 PDF 分页断点。

---

## 6. 内容类型到原生格式的映射

| 原题内容 | Canonical 转译格式 |
|---|---|
| 标题、说明、题干、选项、小问 | Markdown |
| 数学公式、矩阵、上下标、极限、积分 | LaTeX |
| C / C++ / Python 等程序 | fenced code block |
| 汇编 / 指令序列 | `asm` code block |
| 规则表格 | Markdown table |
| 网络拓扑、时序图、流程、数据通路、内存布局、几何结构图 | Semantic SVG |
| 数学函数图像 / 坐标图 | 优先 Semantic SVG；必要时由数学源生成 SVG |
| 照片、真实场景、无法合理语义重建的复杂图 | PNG / WebP |

### 核心判据

```text
能成为文本 -> 不做图片
能成为 LaTeX -> 不截图公式
能成为可维护 SVG -> 不截图结构图
```

但不要为了“全矢量”而重画价值很低的真实照片或复杂纹理图。

---

## 7. 文本转写规范

### 7.1 不做无意义润色

保持原题术语和问法。允许：

- Markdown 所需的空格规范；
- 统一代码围栏；
- 统一 LaTeX 写法；
- 修复明确的扫描/OCR/排版错误。

不允许：

- 把题干改写成自己的解释；
- 为了“更好懂”增加条件；
- 把题干摘要化；
- 把答案线索写进题面。

### 7.2 高风险字符优先复核

批量校对时，优先检查：

```text
I / l / 1
0 / O
< / <= / ≤
> / >= / ≥
- / −
[] / () / {}
_ / -
μ / u
B / b
Mb/s / MB/s / kb/s
十六进制 0 / O
变量上下标
矩阵转置、逆、幂
积分上下限
区间开闭
```

### 7.3 数字与单位单独做一遍 Validation Pass

数字、地址、时间、速率、容量、页大小、Cache 大小、概率、角度等是最高优先级输入。

例如：

```text
32 μs
400 B
10 Mb/s
36 000 km
300 000 km/s
0180 0020H
10.10.10.0/24
```

一个普通虚词错误可能不改变题目；一个数字错误往往直接改变整题。

---

## 8. 数学真题专项规范

数学题比普通正文更依赖符号精度。

### 必须重点保护

- 定义域与区间端点；
- 极限趋向方向；
- 上下标；
- 导数阶数；
- 积分上下限；
- 被积变量；
- 分式层级；
- 根号覆盖范围；
- 绝对值 / 范数；
- 向量、矩阵、转置、逆；
- 行列式竖线与绝对值竖线；
- 概率条件符号；
- 参数范围；
- 图中坐标、交点、渐近线和阴影区域。

### 数学公式

正文中的公式统一使用 LaTeX，不把公式保存成 SVG 或截图，除非公式本身就是原题图形的一部分。

### 数学图形

函数图、几何图、坐标系应优先恢复“结构语义”，例如：

```xml
<g id="axis-x">...</g>
<g id="axis-y">...</g>
<g id="curve-f">...</g>
<g id="point-a">...</g>
<g id="region-d">...</g>
```

不要仅生成不可理解的一长串匿名 path。

---

## 9. 代码与计算机真题专项规范

代码是高风险内容，最终 code block 必须逐字符检查：

- 关键字；
- 变量名；
- 数组下标；
- 括号层级；
- 指针符号；
- 比较符；
- 自增/自减；
- 常量；
- 注释；
- 汇编操作数；
- 地址和十六进制数。

例如：

```c
for(i=1; i*i<=n; i++)
```

不能被转成：

```c
for(i=1; i*i<n; i++)
```

汇编同理：

```asm
idiv R1, R2
```

不能漏成：

```asm
idiv R1
```

---

# 10. Semantic SVG 规范

SVG 的目标不是像素级复刻，而是：

```text
语义正确
> 结构正确
> 标签正确
> 视觉接近
> 像素一致
```

## 10.1 什么必须做成独立对象

只要对象在题目中承担语义，就应尽量有独立元素或 `<g>`：

```xml
<g id="host-h">...</g>
<g id="router-r1">...</g>
<g id="link-h-r1">...</g>
<g id="activity-b">...</g>
<g id="cache-index">...</g>
```

### 必须保留的图形信息

- 对象是谁；
- 谁与谁连接；
- 箭头方向；
- 标签属于谁；
- 数值与单位；
- 相对位置中有题意的部分；
- 阴影/虚线/区域边界的语义。

### 可以优化的视觉信息

- 像素级坐标；
- 字体替换；
- 线条粗细；
- 图标造型；
- 留白；
- 对齐；
- 不承载题意的局部比例。

### 禁止

- 把整张扫描图包进 `<image>` 冒充 SVG；
- 把所有文字转成 path；
- 为了美观新增题目没有的机制、节点或解释；
- 在图中直接标出题目正在询问的答案；
- dark / light 两版出现不同的连接关系或标签。

---

## 10.2 SVG 命名

使用：

```text
qNN_<semantic-name>.svg
```

例如：

```text
q36_dhcp_exchange.svg
q38_tcp_sequence.svg
q42_aoe_network.svg
q44_divider_datapath.svg
```

不要使用：

```text
image1.svg
figure-final2.svg
page7pic.svg
```

`id` 也使用稳定语义名，不使用随机导出 ID。

---

## 10.3 SVG 颜色与主题策略

### 决策：不依赖运行时自动换肤

虽然 SVG 可以使用 CSS、`currentColor`、媒体查询等机制，但 Obsidian 中 SVG 常作为独立图片资源嵌入，宿主主题变量和颜色继承不应被视为稳定合同。

因此本项目采用：

```text
一套图形语义 / 几何
-> 确定性生成 dark
-> 确定性生成 light
```

而不是：

```text
一个 SVG
-> 运行时猜 Obsidian 当前主题
```

### 默认暗色主题固定为当前 Obsidian 背景

```text
background  #30362d   RGB(48,54,45)
foreground  #edf4e8
node        #3b4337
soft        #394136
muted       #596452
```

默认文件：

```text
assets/qNN_xxx.svg
```

### 亮色主题

```text
background  #fafaf7
foreground  #111111
node        #ffffff
soft        #f7f6f1
muted       #eceee8
```

放在：

```text
assets/light/qNN_xxx.svg
```

### 颜色不得散落在图形逻辑中

推荐所有图从统一 token 生成：

```css
.t    { fill: var(--fg); }
.line { stroke: var(--fg); }
.node { fill: var(--node); stroke: var(--fg); }
.soft { fill: var(--soft); stroke: var(--fg); }
```

如果未来实现 SVG builder，输入应是：

```text
geometry / semantic source
+ theme tokens
-> rendered SVG
```

**不要人工维护两份不同 geometry 的 dark / light SVG。**

### 如果以后用户更换 Obsidian 背景色

不要逐图手改。应：

1. 更新 theme token；
2. 根据新背景重新选择高对比 foreground / node / muted；
3. 批量重新生成所有 dark SVG；
4. 运行 SVG validation。

当前没有 builder 时，仍按同一组 token 批量替换，禁止每张图自行选色。

---

## 10.4 SVG 字体与线条

默认字体栈：

```css
font-family: Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif;
```

建议：

- 普通文字：18–24 px；
- 重要标签：22–28 px；
- 主线：约 2.2–2.6 px；
- 辅助线：约 1.7–2.2 px；
- 箭头必须与当前 foreground 同色；
- 圆角只作为视觉优化，不改变结构边界含义。

最终以“在 Obsidian 正常宽度下无需放大即可辨认”为验收标准，不机械追求某个字号。

---

## 10.5 Exam Profile 的年度路由例外

Exam Profile 只编码**长期稳定的考试制度**，不能把某一年的常见题号分布误写成永恒规则。

以 408 为例：Q1～Q40 的四科客观题区间长期稳定，但综合应用题历史上存在年度路由变体。Profile 因此必须支持：

```text
default routing
+
year routing override
```

执行年度导入时顺序固定为：

```text
question number
-> apply year override if present
-> otherwise use profile default
-> derive subject / section
```

禁止因为文件名、网页标签或上一年的题号位置与 Profile 冲突就直接覆盖 Profile。若发现真实考试结构变化，应先核对题目内容，再把它登记为年度 override；只有制度长期变化时才建立新的 Profile version。

当前 408 的 2016 年综合题就是已知例外，具体配置见 `exam_profiles/408.json`。

---

## 11. 推荐批量工作流

### Phase 0｜Intake

```text
收到 PDF / 高清题图
-> 确定 / 建立 Exam Profile
-> 创建 exam.json 年度实例元数据
-> 判断 text-native / scan / hybrid
-> 建立题号与页面 Coverage
-> 列出图 / 代码 / 表格 / 公式密集题
```

### Phase 1｜Initial Extraction

目标：先完整，不先美化。

```text
可靠 text layer -> 初稿
扫描页 -> 视觉转写初稿
```

形成一份连续 Exam Markdown 草稿。

### Phase 2｜Structural Reconstruction

恢复：

```text
考试标题
-> 大题区
-> 题号
-> 题干
-> 选项
-> 小问
-> 分值
-> code / table / figure slot
```

跨页题在此阶段合并。

### Phase 3｜Native Conversion

```text
Text    -> Markdown
Math    -> LaTeX
Code    -> fenced code
Table   -> Markdown table
Diagram -> Semantic SVG
```

### Phase 4｜Figure Reconstruction

先保证：

```text
对象
连接
方向
标签
数值
```

再调整布局和主题。

### Phase 4.5｜Question-Driven Logic Review

**每一张新建或重构的题图都必须做逻辑审阅，不能只做视觉对照。** 读取该题后续小问，反向检查图是否保留了完成计算/推理所必需的语义。

至少逐项问：

```text
这条边/箭头方向是否会改变答案？
标签是否挂在正确对象上？
字段边界/位宽是否与后续编码计算一致？
拓扑是否支持题目要求的路径、传播或收敛推理？
时序先后是否与 ACK/窗口/状态计算一致？
数据通路的输入、输出和控制信号方向是否正确？
坐标图的端点、交点、开闭区间、阴影区域是否足以支持数学推理？
```

通过标准不是“看起来像原图”，而是：

```text
原图语义一致
+
题目逻辑可由该图正确运行
+
没有额外泄露答案
```

若视觉近似与题意语义冲突，优先修复题意语义。

### Phase 5｜Fidelity Pass

逐题检查：

```text
题号
分值
题干
选项
数字
单位
变量
公式
代码
图
小问
```

优先级：

```text
数字 / 数学符号 / 代码
>
图连接关系
>
普通措辞
>
像素级版式
```

### Phase 6｜Visual Pass

只有内容已经基本正确后才做：

- dark / light；
- SVG 线宽；
- 字号；
- 图宽；
- 对齐与留白。

不要在题面还错的时候优先“画漂亮”。

### Phase 7｜Automated Validation

检查：

```text
Profile / exam.json 一致性
题号覆盖
重复 / 缺失题号
固定题号路由是否符合 Profile
综合题分值是否与整卷总分一致
content_features 与正文实际内容是否一致
代码围栏
资产引用（只引用实际存在且由题面确认的资产；不得按 `fig1..figN` 连号猜测）
SVG XML
暗亮版本数量
禁止嵌入 raster image
```

### Phase 8｜Clean

删除或不进入最终 Pack：

- OCR 草稿；
- 临时截图；
- 比对日志；
- 诊断 callout；
- 测试 SVG；
- 重复资产；
- 旧错误版本。

### Phase 9｜Freeze

只有同时满足：

```text
Complete + Correct + Editable + Readable + Validated
```

才视为该套真题整理完成。

之后答案、解析、Evidence Mapping、错题诊断从对应 Exam Archive 的 Canonical Source 读取，但不把分析写回题面。

---

## 12. 单题 Fidelity Checklist

每题至少检查一次：

```text
[ ] 题号正确
[ ] 题号对应的题型 / 学科符合 Exam Profile（若 Profile 固定）
[ ] 分值正确（如有）
[ ] 题干完整
[ ] 数字正确
[ ] 单位正确
[ ] 数学符号 / 上下标正确
[ ] 变量名正确
[ ] 代码逐字符正确（如有）
[ ] 选项 A-D 完整且顺序正确（如有）
[ ] 小问完整且顺序正确（如有）
[ ] 图存在（如有）
[ ] 图中标签 / 箭头 / 数值 / 关系正确
[ ] 无答案或解析混入 Source
```

---

## 13. 整卷自动检查建议

后续如果实现 `check_exam_source`，只检查机器可以确定的事实。

### ERROR 候选

- `exam.json` 缺失、JSON 不合法或引用不存在的 Profile；
- `exam.json` 与主 Markdown 的 `exam_id / year / question_count / total_score` 不一致；
- 题号缺失或重复；
- 固定题号考试出现违反 Profile 的 section / subject 结构；
- 综合题逐题分值与 Profile / 整卷总分不一致；
- `content_features.figures` 与 `figure_assets` / Markdown 实际 SVG 引用不一致；
- Markdown 引用资产不存在；
- SVG XML 无法解析；
- fenced code block 未闭合；
- dark 有图但 light 缺同名图；
- SVG 包含 `<image>` 指向整张原题截图；
- 主 Markdown 中出现已知的诊断模板或答案区块。

### AUDIT 候选

- SVG 没有语义 `id`；
- 图中文字过小；
- 单张 SVG 使用大量非 token 硬编码颜色；
- 题目图仍是 raster，但可能适合重建 SVG；
- 数学题中出现大量 Unicode 数学符号而非 LaTeX。

机器不判断：

- 题目内容本身是否学术正确；
- 某个图是否“足够漂亮”；
- 一个疑似 typo 应如何纠正。

这些仍需要视觉核对或人工确认。

---

## 14. 最终验收问句

完成一套卷前只问五个问题：

1. **Complete**：学生能否只看这份文件拿到完整题面？
2. **Correct**：是否还有一个数字、符号、代码字符或图关系可能改变题意？
3. **Editable**：需要改一个变量、标签或箭头时，能否直接修改原生源？
4. **Readable**：在当前 Obsidian 暗色背景和亮色环境中是否都清楚？
5. **Validated**：文件引用、SVG、题号覆盖是否已经机器检查？

五项都通过，停止继续“优化”。

> **过程可以复杂，最终 Source 必须简单。**
