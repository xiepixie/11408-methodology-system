# 真题源重建执行提示词

本文件是 `exam-source` 场景的**执行提示词唯一 Owner**。规则与验收合同由 [`exam_source_conversion_spec.md`](exam_source_conversion_spec.md) 统一拥有；本文件只规定 Agent 每次执行真题源重建时的读取顺序、判断顺序和停止条件，不复制第二套规范。

## 1. 角色与目标

你承担**真题源重建者 + 编辑者**角色。

你的任务不是解题、写答案或做 OCR 展示，而是把 PDF、扫描件、网页抓取、高清题图恢复成：

```text
Complete + Correct + Editable + Readable + Validated
```

的 Canonical Exam Source（规范化真题源）。

**408、数学一和其他考试执行同一套转译方法。** 考试结构差异由 `exam_profiles/<profile_id>.json` 与年度 `exam.json` 表达，不另起一套提示词或规则。

## 2. 开工前最小读取顺序

进入 `exam-source` 场景后按顺序读取：

1. `exam_source_conversion_spec.md`；
2. 对应 `exam_profiles/<profile_id>.json`；
3. 目标真题归档目录的 `README.md` / `exam.json` / 已有正式版（若存在）；
4. 用户本轮指定的最高质量原题材料；
5. 只有发生冲突时，再读网页抓取、旧 PDF、解析站等辅助来源。

不要为了“全面”先扫完整个学习仓库。

## 3. Source Authority

来源优先级默认是：

```text
用户明确指定的权威高清原题 / 官方高清原卷
> 官方或可信原版 PDF / 扫描件
> 保留结构的原始网页 HTML / 图片
> 结构化题库转写
> 答案解析站 / 二次整理
```

若用户说“以这批图片为准”，这批图片覆盖到的区域立即成为该区域的最高依据。

明显 OCR、公式扁平化、代码漏字符、图标签错位可以结合题意直接修复；**无法可靠恢复的局部进入复核清单，但不得因此停止整套或整批试卷处理。**

## 4. 批量执行纪律

对多年份、多套试卷：

```text
先完成 Coverage
-> 批量恢复正文
-> 批量恢复原生公式/代码/表格
-> 重建必要 SVG
-> Question-Driven Logic Review
-> Fidelity Pass
-> Validation
-> 汇总少量 unresolved items
```

局部有疑点时：

- 能从上下文和题目逻辑唯一恢复：直接改正；
- 不能唯一恢复：保留最可靠内容并登记复核；
- **不要因为一题缺图、一个选项模糊或一个字符冲突而停下其余年份。**

正式题面禁止混入“疑似 OCR”“来源 A/B 冲突”等诊断文字。

## 5. 原生格式

优先级固定：

```text
普通文字 -> Markdown
数学结构 -> LaTeX
代码/汇编 -> fenced code
规则表格 -> Markdown table
结构关系图 -> Semantic SVG
复杂且不适合重建的视觉材料 -> raster asset
```

能用文本/LaTeX/表格表达的，不为了还原版面硬做 SVG。

## 6. 题图执行顺序

本提示词不再复制第二套 SVG 规则。真正开始重建题图时按下面顺序执行：

```text
先确认原题图在题面中的真实位置与作用
→ 按 exam_source_conversion_spec.md 恢复题面对象、标签、数值、方向与后续小问需要的全部条件
→ 若需要重新设计可编辑语义图，调用 diagram_design_spec.md 检查关系编码、度量/示意边界与额外误读
→ 若采用 TikZ/PGF，调用 latex_layout_spec.md 处理版心、图层、主题、SVG 与真实视觉自检
→ 把图放回原题位置，再拿后续小问逐项反推
```

真题 Source 与训练/Handbook 配图有一个重要区别：**题图插入位置由原试卷决定，不由 Agent 重新选择。** Agent 可以优化重建后的排版与可编辑性，但不能为了视觉叙事移动图、增删条件或把答案画进图中。

Question-Driven Logic Review 继续是执行门禁：网络图检查路径/邻接/边界，协议图检查方向与序号，数据通路检查位宽与控制信号，Cache/页表检查字段与映射，图算法检查边方向与权值，数学图检查坐标、端点、交点、渐近线、阴影区域与开闭性。**图能够正确驱动后续小问，才算完成。**

## 7. 数学真题额外注意

数学并不使用另一套流程，只在 Fidelity Pass 中额外强化：

- 上下标与幂；
- 积分上下限和被积变量；
- 极限方向与趋近点；
- 矩阵维数、转置、逆；
- 分式、根号、绝对值/范数范围；
- 定义域、参数范围、区间端点；
- 函数/几何图中的关键坐标与区域。

任何可能改变题意的 Unicode 扁平化都要恢复成 LaTeX 结构。

## 8. 408 真题额外注意

408 同样只是在通用 Fidelity Pass 中强化：

- C/C++/汇编逐字符；
- 十六进制、二进制、地址与位段；
- Cache/页表位宽；
- 单位与数量级；
- 网络地址、端口、seq/ack/window；
- 箭头、控制信号、拓扑连接；
- Exam Profile 的年度路由 override。

不要相信网页文件名中的学科标签覆盖 Profile。

## 9. 规范化落盘位置

完成态试卷必须进入当前仓库对应的真题归档目录：

```text
archives/<exam_id>/<year>年真题/
```

其中 `<exam_id>` 由 Exam Profile 确定，例如 `math1`、`408`。不得再使用旧的 `资源/<Exam_Archive>/...` 抽象路径作为实际落盘位置。

`80_evidence/inbox/` 只用于临时输入/兼容入口，不拥有成熟真题 Canonical Source。

同一套试卷只能有一个可修改正文 Owner。迁移后旧位置只允许保留 redirect / legacy pointer。

## 10. 完成前检查

Agent 不得仅凭“文件已写入”声称完成。至少验证：

```text
题号 Coverage
分值与 Profile / exam.json
代码围栏
Markdown asset refs
SVG XML
Semantic SVG 关键关系
Dark / light 一致性
Question-Driven Logic Review
无答案/解析污染正式题面
无第二份 Canonical 正文
```

最终只向用户报告：完成范围、真正修正的重要错误、仍需人工/高清源确认的少量 unresolved items。
