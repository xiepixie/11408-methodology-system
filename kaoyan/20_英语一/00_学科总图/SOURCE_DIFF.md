# 英语 Atlas Source Diff 与 Canonical Ownership 裁决

> 状态：已裁决  
> 目的：比较两份旧版 Atlas `.tex`，确定唯一母模型、Canonical Owner 与下沉边界，为新版英语一 Atlas 提供语义冻结点。

## 1. Source

- Source A：`英语语言学习与考试_统一心智模型与方法论手册_v1.tex`
- Source B：`英语语言学习与考试统一方法论_从语言系统到任务执行_v1.tex`
- Ownership 校验源：`10_阅读/`、`20_完形与新题型/`、`30_翻译/`、`40_写作/`、`90_学科做题规则/` 下现有 README 与专题手册。

## 2. 总裁决

两份旧稿并不是两套互斥的英语理论，而是同一批核心材料的两次重新编排。真正需要裁决的，不是“选 A 还是选 B”，而是：

1. 旧稿都把 Atlas、Topic、Control、训练系统混入同一册；
2. 旧稿都把本应为并列坐标的层面画成了单一线性流程；
3. Source A 与 Source B 对“第四层”给出了不同对象，说明原“四层模型”并非稳定本体；
4. Topic 手册已经拥有大量机制，Atlas 若继续展开会造成重复 ownership。

因此，新 Atlas 不继承任何一份旧稿的顶层线性箭头，而保留双方共同且可稳定映射的核心。

## 3. 唯一母问题

> 面对任意一个英语一任务，怎样判断它正在要求学习者调用哪类语言资源、完成哪类语言活动、承受哪种处理条件，并把具体机制路由到唯一专题 Owner？

这是一张 Subject Atlas 应回答的问题：建立坐标、解释关系、告诉知识挂在哪里；它不直接拥有各题型的完整解题过程。

## 4. 唯一母模型

新版 Atlas 采用：

$$
\boxed{
\text{Task / Context}
\longrightarrow
\left[
\text{Activity}
\times
\text{Resource System}
\times
\text{Processing}
\right]
\longrightarrow
\text{Performance}
}
$$

其中：

- `Task / Context -> [...]`：表示任务规定需要调用哪些能力，不表示时间因果；
- `Activity × Resource System × Processing`：表示三个共同坐标同时参与，`×` 不是乘法，也不是先后顺序；
- `[...] -> Performance`：表示这些条件在一次具体执行中产生可观察表现；
- `Exam Adapter`：从更大的语言使用空间中选择任务、输入/输出形式、时间压力与评分方式；
- `Proficiency`：学习者能够稳定工作的任务范围，不等于某一次 `Performance` 或单次分数。

这消除了旧稿最大的模型错误：Language Resource、Activity、Processing 不是一条固定的时间流水线。

## 5. 逐项 Source Diff

| 项目 | Source A | Source B | 裁决 |
|---|---|---|---|
| 英语不是若干考试的集合 | 明确 | 明确 | **共同核心，保留 Atlas** |
| 语言资源 | Form / Lexicon-Grammar / Meaning / Discourse / Pragmatics | 同样结构 | **共同核心，Atlas 保留分类；机制下沉 Topic** |
| 沟通活动 | Reception / Production / Interaction / Mediation | 同样结构 | **共同核心，保留 Atlas** |
| 在线处理 | 放在“沟通活动”之后 | 放在“语言资源”之后 | **真正冲突：不得画成单一层级流程** |
| 第四层 | Assessment / Development | Monitoring / Repair | **真正冲突：两者不是同类对象，取消“四层流水线”** |
| Stored Knowledge 与 Accessible Performance 区分 | 有 | 有 | **共同核心，Atlas 保留边界；细节机制下沉** |
| Reception / Production 处理链 | 详细展开 | 详细展开 | **重复机制，下沉相应 Topic** |
| Interaction / Mediation | 详细展开 | 详细展开 | **共同分类留 Atlas；完整机制由专题拥有/待建** |
| Working Memory / Automaticity | 详细展开 | 详细展开 | **重复机制；应进入语言加工/熟练度 Topic，不留 Atlas 正文展开** |
| Proficiency Profile / Operating Envelope | 有 | 有 | **共同核心，保留 Atlas 高层定义** |
| CEFR A1-C2 训练重心 | 详细 | 详细 | **下沉发展/训练 Topic；英语一 Atlas 不展开** |
| Proficiency -> Performance -> Score | 有 | 有 | **共同核心，保留 Atlas 的测评边界** |
| IELTS / TOEFL / 其他考试版本细节 | 较多 | 较多 | **非英语一 Atlas 核心；删除版本型细节，仅保留 Exam Adapter 概念** |
| Task -> Meaning -> Operation/Action -> Response/Decision -> Monitor | 有 | 有 | **重复 Control；Canonical Owner = `90_学科做题规则/`** |
| First Breakpoint 故障链 | 有 | 有 | **不属于 Atlas；进入 Control / Practice System** |
| Full Task -> Breakpoint -> Isolate -> Practice -> Return | 有 | 有 | **训练系统，不属于 Atlas；进入 Practice System** |
| 学习计划与训练模式 | 大量 | 大量 | **不属于 Atlas；下沉 Practice / Topic** |
| Topic Ownership 表 | 有 | 有 | **保留 Atlas，但按现有专题重新裁决** |

## 6. 共同核心

新版 Atlas 保留以下稳定内容：

1. 英语一不是五种互不相关的题型，而是对同一语言系统的不同任务取样；
2. 语言资源至少需要区分 `Form / Lexicon-Grammar / Meaning / Discourse-Pragmatics`；
3. 任务活动至少需要区分 `Reception / Production / Interaction / Mediation`；
4. “拥有知识”与“在任务中及时调用”必须区分；
5. 熟练度应理解为可稳定完成任务的范围，而不是单一词汇量或一次分数；
6. 考试是有限取样，题型应通过 Adapter 挂接到语言能力空间；
7. 不同专题的差异来自它们恢复、判断或生成的对象不同，而不是存在五套英语。

## 7. 真正冲突

### 7.1 顶层箭头冲突

Source A：

`Resource -> Activity -> Processing -> Assessment/Development`

Source B：

`Resource -> Processing -> Activity -> Monitor/Repair`

两条链都把不同本体层面误写成单一先后关系。处理并不是永远发生在“Activity 之后”，Activity 也不是永远发生在“Processing 之后”。新版改为多坐标联合调用。

### 7.2 “第四层”冲突

`Assessment/Development` 是观察与发展视角；`Monitoring/Repair` 是任务执行内部机制。两者不能占据同一抽象位置。新版不再维持“四层”名义统一。

### 7.3 文档身份冲突

两份旧稿都自称 Subject Map，却同时完整拥有：

- 题目执行协议；
- 故障定位；
- 训练闭环；
- A1-C2 训练策略；
- 多个题型机制。

这违反 Atlas 只拥有 `Why + Where + Relationship` 的边界。新版将这些内容下沉。

## 8. 重复机制

以下内容在两份旧稿中实质重复，且已由专题手册进一步展开，因此不再由 Atlas 解释两遍：

- `Form -> Lexical Recognition -> Structure -> Meaning -> Discourse` 接收链；
- `Intent -> Meaning -> Discourse -> Retrieval -> Form` 产出链；
- Mediation 的 `Source -> Meaning -> Reorganisation -> Target`；
- Working Memory / Automaticity；
- `Task -> Meaning -> Action -> Decision -> Monitor`；
- First Breakpoint 与故障表；
- `Full Task -> Breakpoint -> Isolate -> Practice -> Return`；
- Proficiency Profile / Operating Envelope 的多次重复解释；
- Exam Adapter 的多次重复定义。

新版 Atlas 每个概念只保留一处地图级定义，其余改为 Owner 指针。

## 9. 应下沉 Topic

| 机制 | Canonical Owner |
|---|---|
| 缺失词项在多层约束下恢复 | `20_完形与新题型/英语一_完形填空_多层语言约束下的词项恢复方法论手册_v1.tex` |
| 语篇单元、关系、功能与结构重构 | `20_完形与新题型/英语一_新题型_衔接连贯与语篇结构重构方法论手册_v1.tex` |
| 题干 -> 证据 -> 选项判定 | `10_阅读/英语一_阅读理解_证据定位与选项判定方法论手册_v1.tex` |
| 英文形式 -> 意义结构 -> 中文重构与不变量 | `30_翻译/英语一_翻译_意义结构恢复与中文重构方法论手册_v1.tex` |
| Task -> Meaning -> Discourse -> Language -> Delivery | `40_写作/英语一_写作总方法论_从任务到语言的生成系统_v1.tex` |
| 一般词汇/搭配资源的系统机制 | **待建 Language Resource Topic**；现有完形仅在“候选词恢复”问题下 Use，不拥有通用词汇学 |
| 一般句法/长难句机制 | **待建 Syntax / Meaning Topic**；现有阅读、完形、翻译均只在各自问题下 Use |
| Working Memory / Automaticity / 熟练度形成机制 | **待建 Processing / Proficiency Topic**；Atlas 只保留接口 |

## 10. 应进入 Control / Practice

### Control Owner：`90_学科做题规则/`

统一拥有跨题型的考试执行控制，例如：

`Task -> Build/Recover Meaning -> Select Route/Operation -> Produce Decision/Response -> Verify`

它回答的是“现在做什么”，不是“英语是什么”。各 Topic 可以提供自己的 Adapter，但不再各自重新发明总控制协议。

### Practice System：暂不伪装成 Atlas

以下内容应从 Atlas 移出：

- First Breakpoint 记录；
- Full Task -> Isolate -> Practice -> Return；
- 错题首次偏离点；
- 个人训练瓶颈；
- 学习周期与迁移验证。

这些属于学习/证据平面。若后续建立独立 Practice System，应由它拥有；在此之前可以由 `90_学科做题规则/` 只保存与执行复盘直接相关的接口。

## 11. 应保留 Atlas

新版 Atlas 只 Own：

1. 英语一的研究对象与学科母问题；
2. `Task/Context -> [Activity × Resource × Processing] -> Performance` 坐标模型；
3. Resource / Activity / Processing / Task Context 之间的关系；
4. Proficiency、Performance、Score 的边界；
5. Exam Adapter 的定义；
6. 英语一各题型在能力空间中的位置；
7. Canonical Ownership 与 Topic / Control 接口；
8. 新知识进入系统时的路由规则。

## 12. Canonical Ownership Matrix

| 概念/规则 | Owner | Atlas 如何处理 |
|---|---|---|
| 英语一学科坐标系 | `00_学科总图` | **Own** |
| 语言资源的四层分类 | `00_学科总图` | **Own 分类 / 不展开机制** |
| Reception / Production / Interaction / Mediation 分类 | `00_学科总图` | **Own 分类 / 不展开执行链** |
| Exam Adapter / Proficiency vs Performance vs Score | `00_学科总图` | **Own** |
| 完形约束满足 | `20_完形与新题型/完形` | Use / Route |
| 新题型语篇重构 | `20_完形与新题型/新题型` | Use / Route |
| 阅读证据判定 | `10_阅读` | Use / Route |
| 翻译意义重构 | `30_翻译` | Use / Route |
| 写作生成系统 | `40_写作` | Use / Route |
| 跨题型考试执行协议 | `90_学科做题规则` | Bridge / Route |
| 通用词汇/搭配机制 | 待建 Language Resource Topic | Atlas 仅保留位置 |
| 通用句法/长难句机制 | 待建 Syntax / Meaning Topic | Atlas 仅保留位置 |
| 自动化/工作记忆/熟练度形成 | 待建 Processing / Proficiency Topic | Atlas 仅保留位置 |
| 个人错题与训练闭环 | 待建 Practice System | 不进入稳定理论正文 |

## 13. 文档身份修正

- `00_学科总图/`：唯一 Subject Atlas。
- `10_阅读/`：Topic。
- `20_完形与新题型/`：**Topic Group**，不是 Atlas；内部两册分别是 Topic。
- `30_翻译/`：Topic。
- `40_写作/`：Topic。
- `90_学科做题规则/`：Control。

## 14. 语义冻结点

新版 `.tex` 的正文不得重新拥有已经下沉的完整机制。若需要解释专题，只允许：

- 给出它解决的核心对象；
- 给出它与母模型的坐标位置；
- 给出 Canonical Owner；
- 给出进入专题的接口问题。

不得在 Atlas 中再次展开完整做题步骤、故障表、训练闭环或题型技巧。
