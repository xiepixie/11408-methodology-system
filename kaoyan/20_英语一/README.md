# 英语一 Course / Subject System

## 学科母问题

面对任意一个英语一任务，怎样判断它正在要求学习者调用哪类语言资源、完成哪类语言活动、承受哪种处理条件，并把具体机制路由到唯一专题 Owner？

当前唯一母模型：

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

这里 `Activity × Resource System × Processing` 表示联合坐标，不是固定先后顺序。考试题型只是在这个能力空间中规定不同 Task，并通过具体材料、时间和评分条件进行取样。

## 文档身份与 Canonical Ownership

| 模块 | 类型 | 当前状态 | 主要责任 |
|---|---|---|---|
| [00_学科总图](00_学科总图/README.md) | Atlas | 已采用 | 学科坐标、母模型、专题位置与 Ownership |
| [10_阅读](10_阅读/README.md) | Topic | 已采用 | 题干 $\to$ 证据 $\to$ 选项判定 |
| [20_完形与新题型](20_完形与新题型/README.md) | Topic Group | 已采用 | 完形词项恢复；新题型语篇结构重构 |
| [30_翻译](30_翻译/README.md) | Topic | 已采用 | 英文意义恢复与中文重构 |
| [40_写作](40_写作/README.md) | Topic | 已采用 | Task $\to$ Meaning $\to$ Discourse $\to$ Language $\to$ Delivery |
| [90_学科做题规则](90_学科做题规则/README.md) | Control | 已采用 | 跨题型题目信号、第一动作、Route、执行与 Verify |

遵守：

$$
\boxed{\text{One Concept / Rule} \to \text{One Canonical Owner}}
$$

Atlas 只回答 `Why + Where + Relationship`；Topic 回答 `How + State + Mechanism + Boundary + Cost`；Control 回答“现在该做什么”。

## 当前结构缺口

以下能力在 Atlas 中已有位置，但尚无独立 Canonical Topic：

1. 通用词汇 / 搭配资源机制；
2. 通用句法 / 长难句 / Meaning Structure；
3. Processing / Automaticity / Proficiency formation；
4. 独立 Practice / Evidence System，用于 First Breakpoint、错题证据与迁移复测。

这些缺口在建立独立 Owner 以前，不应由现有题型 Topic 或 Atlas 临时重复拥有。

## Source Diff

两份旧版总图的共同核心、真正冲突、重复机制与下沉裁决见：

- [英语一总图 Source Diff 对照](00_学科总图/SOURCE_DIFF.md)
