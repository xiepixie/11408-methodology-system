# 仓库完整性与维护审计

本文件只负责一件事：规定脚本应该自动阻止什么、应该提醒什么，以及机器不应该替人判断什么。

## 1. 两种结果必须分开

### 硬错误（ERROR）

**硬错误**是脚本可以仅凭文件事实确定的规则违反。存在硬错误时，`check` 返回失败，稳定修改不能视为完成。

例如：

- Markdown 链接指向不存在的文件；
- README 声称正文已进入 LaTeX，但找不到唯一 `.tex`；
- 状态写着“已发布”，但对应 PDF 不存在或比 `.tex` 更旧；
- 两个不同 `.tex` 会生成同名发布 PDF；
- `ownership_matrix.md` 指向不存在的路径；
- `CURRENT.md` 缺少约定的维护区块；
- `PROGRESS.md` 没有按当前状态重新生成。

### 维护债务（AUDIT）

**维护债务**是当前允许暂时存在、不会让 `check` 失败，但长期不处理会增加判断成本的过渡状态。

典型例子：

- 旧长 Topic/Bridge/Integration README 仍保存深度正文，尚未迁入 `.tex`；
- Topic/Bridge/Integration 已有导航页，但正式 `.tex` 尚未建立；
- `.tex` 已存在，但同目录没有 README 导航页；
- Atlas 目录仍保留一份与 Canonical README 重复的根级 `.tex` 正文；
- `90_publish/` 中有旧 PDF，但当前仓库找不到同名 `.tex`；
- 两个旧 Markdown 文件使用相同标题，需要人工确认是否只是 Source 重复。

`audit` 的目的不是制造待办清单，而是让系统能持续回答：**哪里正在变得难以判断？**

## 2. `check` 只检查能确定的事实

运行：

```bash
python3 00_system/cognitive_system.py check
```

当前硬检查如下。

### E-LINK｜断链

Markdown 相对链接的目标必须存在。

### E-STATUS-TITLE｜有状态但没有 H1

任何进入进度扫描的 Markdown 如果声明 `状态：...`，必须同时有唯一 H1 标题。脚本不判断标题内容是否优美，只保证该资产能被稳定识别。

### E-STATUS-TEX｜深度 Handbook 状态与 `.tex` 不一致

本检查只作用于 Topic / Bridge / Integration。`LaTeX 工作稿 / 待人工确认 / 已采用 / 第一版正文已建立 / 完整正文已建立` 等状态要求当前目录存在唯一 Canonical `.tex`。

显式声明 `类型：Atlas` 的 README 本身就是 Canonical Atlas Source，`待人工确认 / 已采用` **不要求 `.tex`**。Atlas 缺少 `.tex` 不是错误。

“目录已建立，正文未建”“README 旧工作稿待迁移”等过渡状态也不要求已有 `.tex`。

### E-PUBLISH-MISSING｜声称已发布但 PDF 不存在

状态明确声明 `已发布` 或已有 `Published PDF` 时，`90_publish/` 必须存在与正文 `.tex` 同 stem 的 PDF。

这里的 **stem** 指文件名去掉扩展名后的部分。例如：

```text
OS_VM.tex -> stem = OS_VM -> 90_publish/OS_VM.pdf
```

### E-PUBLISH-STALE｜发布 PDF 已过期

若 `.tex` 的修改时间晚于 PDF，说明正文修改后尚未重新发布。状态不能继续保持“已发布且同步”。

### E-PUBLISH-COLLISION｜发布文件名冲突

`90_publish/` 是平铺目录。两个不同 `.tex` 如果 stem 相同，都会写成同一个 PDF，后一次发布可能覆盖前一次，因此直接报错。

### E-OWNERSHIP-LINK｜Ownership 台账悬空

`ownership_matrix.md` 中的相对链接必须存在。脚本只检查“路径存在”，不判断这个 Owner 在语义上是否正确。

### E-CURRENT｜当前焦点文件失去结构

`CURRENT.md` 必须保留：

- `# 当前焦点`
- `## 当前已完成`
- `## 下一步候选`
- `## 待人工决定`
- `## 当前阻塞`

脚本不判断里面的计划是否合理，只防止维护入口被意外清空。

### E-PROGRESS｜生成进度过期

`PROGRESS.md` 必须等于当前仓库状态重新生成的结果。修改状态后运行：

```bash
python3 00_system/cognitive_system.py progress --write
```

## 3. `audit` 只提示维护债务

运行：

```bash
python3 00_system/cognitive_system.py audit
```

默认输出优先展示需要人工处理的维护风险，并只汇总 `A-NO-TEX` 建设库存，避免大量已知骨架淹没真正异常。需要展开全部待建设目录时运行：

```bash
python3 00_system/cognitive_system.py audit --all
```

当前审计项目如下。

### A-README-LONG｜README 可能越过自己的解释粒度

行数只是启发式信号，不是知识质量判据：

- Canonical Atlas README 超过 300 行时提示：检查它是否开始展开 Topic 机制；
- Topic / Bridge / Integration Landing Page 超过 150 行时提示：检查是否把深度正文留在 README。

提示只要求人工检查解释责任，不要求机械删行。

### A-NO-TEX｜深度 Handbook 只有导航页，没有正文

只检查 Topic / Bridge / Integration。Landing Page 存在但没有可确定 `.tex` 时列入建设库存；状态明确是待建设或旧稿待迁移时仍是合法过渡态。

**Atlas 永远不进入 A-NO-TEX。** 它的 Canonical Source 就是 README。

### A-ATLAS-DUPLICATE-TEX｜Atlas 旁仍有根级 `.tex`

若 `类型：Atlas` 的 README 同目录仍存在 `.tex`，脚本提示人工确认它是不是旧的重复正文。真正的 Atlas 视觉海报应放在 `assets/`，并且只重复 README 已有的地图语义。

### A-TEX-NO-README｜只有正文，没有导航页

`.tex` 所在目录缺少 README。正文仍可存在，但学生和 Agent 缺少稳定入口。

### A-ORPHAN-PDF｜发布区 PDF 找不到当前 `.tex`

通常表示旧发布物尚未纳管。它不等于内容错误。

### A-PUBLISH-NOT-BUILT / A-PUBLISH-STALE｜深度正文与阅读版不同步

当 Topic / Bridge / Integration README 已明确声明当前存在可维护的 Canonical LaTeX 正文，但没有声明“已发布”时，`audit` 仍会根据文件事实检查阅读版：

- 没有同 stem PDF：`A-PUBLISH-NOT-BUILT`；
- PDF 早于 `.tex`：`A-PUBLISH-STALE`。

这两项只属于维护债务，不阻止继续编辑工作稿。需要同步阅读版时使用安全 `publish` 入口。

### A-DUPLICATE-TITLE｜Markdown 标题重复

只提示人工查看。标题相同不能证明出现两个 Canonical Owner，因此不能作为硬错误。

## 4. `publish` 是考研项目唯一安全发布入口

运行：

```bash
python3 00_system/cognitive_system.py publish "<target.tex>"
```

本项目不直接调用上层共享 `compile_tex.py`。原因不是重新实现 LaTeX 编译，而是共享脚本属于 `common` 级工具，它不知道当前 `.tex` 是否真的是考研项目的 Canonical Handbook，也不会替本项目检查 Owner、stem 冲突和 Landing Page。

`publish` 只发布 Topic / Bridge / Integration 的 Canonical 深度正文。调用共享编译器之前必须确认：

1. 目标 `.tex` 位于 `common/考研/` 内；
2. 同目录存在 README Landing Page 和状态行；
3. 该 README 不是 `类型：Atlas`；
4. 状态明确表示当前已经存在可维护的 Canonical LaTeX 正文，而不是 Source / legacy / 正文待建；
5. 同一 Handbook 目录只能确定一个当前 `.tex`；
6. 全项目没有另一个 `.tex` 使用相同 stem；
7. `90_publish/` 与共享编译脚本都真实存在。

调用共享编译器时，项目安全入口会把 `common/考研/` 根目录加入 `TEXINPUTS`，因此当前过渡期任意深度的 Canonical `.tex` 都可以直接 `\usepackage{ipara-handbook}`，不需要维护脆弱的多层 `../../` 路径。`ipara-handbook.sty` 目前属于 Handbook Prototype；正式 Core/Class 架构与迁移 Gate 由全局 [`common/latex/README.md`](../../latex/README.md) 拥有，本仓库的发布/搜索路径安全仍由本文件拥有。共享编译器继续加入目标目录与 `common/` 级搜索路径。

编译返回成功后继续验证：

- `90_publish/<same-stem>.pdf` 真实存在；
- PDF 不旧于当前 `.tex`；
- 源码目录没有残留同名 PDF。

`publish` 不自动修改 Handbook 正文、README 状态、Ownership 或 `PROGRESS.md`。这些仍按稳定写入工作流由人决定。

### Atlas 视觉海报：`publish-view`

Atlas 不使用普通 `publish`。可选海报必须放在：

```text
<Atlas>/assets/<name>_Poster.tex
```

并使用：

```bash
python3 00_system/cognitive_system.py publish-view "<Atlas>/assets/<name>_Poster.tex"
```

`publish-view` 会确认上级 README 明确声明 `类型：Atlas`、海报源位于 `assets/`、stem 不冲突，并阻止把根级 Atlas `.tex` 重新当成第二份正文。若 Canonical README 比海报源更新，也会要求先人工确认视觉稿已经同步。

## 5. 机器明确不做的判断

脚本不得自动决定：

- 一个机制应该归哪个 Topic；
- 两段内容是否在语义上重复；
- 一座 Bridge 是否值得独立建册；
- 某条 Rule 是否已经得到足够证据；
- 某个模型是否“理解得足够深”。

这些判断需要阅读内容和人工决策。自动化的职责是保护文件事实，不是替代认知判断。

## 6. 修改脚本时的约束

新增自动规则前先问：

1. 机器能否仅凭仓库事实稳定判断？
2. 误报会不会逼迫人长期忽略 `check`？
3. 这条规则已有唯一文档 Owner 吗？
4. 它应该是 ERROR，还是只应该进入 `audit`？
5. 报错是否说明了具体文件、违反的事实和修复动作？

如果答案不清楚，先做审计提示，不做硬错误。

## 7. 稳定修改后的固定动作

如果修改了 `cognitive_system.py`，先运行：

```bash
python3 -m py_compile 00_system/cognitive_system.py
python3 -m unittest discover -s 00_system/tests -p 'test_*.py'
```

随后执行稳定仓库验收：

```bash
python3 00_system/cognitive_system.py progress --write
python3 00_system/cognitive_system.py check
python3 00_system/cognitive_system.py audit
```

其中：

- 单元测试锁住状态解析等已知回归边界；
- `progress` 更新状态快照；
- `check` 阻止确定的结构错误；
- `audit` 展示允许存在的维护债务。
