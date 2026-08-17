# OS HTML Course · Readability / Style QA

Date: 2026-08-15
Scope: `30_408/30_操作系统/80_实战课程/html/`

## Motivation

15 个 Lesson 在快速建设阶段各自携带 inline CSS，视觉语言大致一致，但存在四类长期风险：

1. 大标题偏“海报化”，长时间学习时首屏信息密度偏低；
2. muted text、表格、代码块在不同页面有轻微对比度/字号漂移；
3. 长页 12–19 个 section，缺少统一定位与回顶机制；
4. 后续逐页修改容易形成 15 套 typography / panel / table 规则。

## Change

新增共享阅读层：

- `html/course.css`
- `html/course-ui.js`

并让 `index.html + 15 lessons` 全部在各自 inline style **之后**加载共享层，使共享层成为最终视觉 override，而不破坏已有页面专属交互组件。

### Typography / hierarchy

- 正文统一 `16px / 1.82`，muted text 提高对比度；
- 主解释文本使用约 `78ch` 阅读宽度，宽表/Trace/Flow 仍可使用全宽；
- Hero 标题从最高约 58–60px 收敛到最高 52px，并提高正文首屏占比；
- H2、Panel、Mini、Callout 的间距和圆角统一。

### Scanability

- Table 增加表头底色、隔行层次与 hover row；移动端宽表横向滚动；
- code / codebox 统一等宽字体、字号、行高和对比度；
- Blue / Orange / Red / Green Callout 的语义扫描统一；
- Flow node 的背景、边框、secondary text 统一。

### Long-page navigation

`course-ui.js` 自动从现有 H2 生成：

- 顶部 3px reading progress；
- Lesson 内“本页目录”：桌面默认展开、移动端默认收起，并随滚动高亮当前 H2；
- 滚动后出现的 Back-to-top；
- 不维护第二份手工 TOC，避免结构漂移；
- respect `prefers-reduced-motion`。

### Responsive / print

- grid/trace/calc/crash 在窄屏收为单列；
- 前后页导航在小屏纵向排列；
- Print mode 自动转白底、移除浮动 UI，并保留 table/panel/code 的结构层次。

## QA

- Shared `course.css` references: **16/16**
- Shared `course-ui.js` references: **16/16**
- Shared layer loads after inline CSS: **16/16 OK**
- HTML parser / local static asset paths: **16/16 OK**
- `node --check course-ui.js`: **OK**
- Chrome headless DOM smoke: **16/16 OK**
  - all pages inject `reading-progress`
  - all 15 Lesson pages inject `page-toc`
  - desktop smoke confirms TOC default-open + current-heading active state
  - Lesson pages inject `back-to-top`

## Maintenance Rule

共享视觉规则以后只在 `course.css` 演化。旧页面中已有的重复 global inline declarations 暂时作为 legacy fallback 保留，但**不得继续作为视觉 Owner 修改**；单页 inline CSS 只允许维护该页独有交互组件。待课程内容稳定后，可做第二轮 CSS debt cleanup，删除重复 global declarations，而不改变页面视觉行为。
