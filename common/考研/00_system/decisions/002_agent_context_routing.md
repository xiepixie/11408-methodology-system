# ADR-002：按场景加载最小 Agent Context Pack

## Status

Accepted

## Context

提示词已经存在，但 Agent 如果不知道项目架构、当前已有模型和资产成熟度，仍会给出与系统无关的通用回答。让用户每次手动粘贴全部项目说明又会增加摩擦和上下文噪声。

## Options Considered

| 方案 | 优点 | 缺点 |
|---|---|---|
| 每次通读整个仓库 | 不容易漏文件 | 慢、噪声大、容易混用无关模型 |
| 用户每次手工选择文件和角色 | 控制精确 | 使用门槛高，重复劳动 |
| Agent 自动识别场景并加载最小 Context Pack | 快、上下文相关、用户输入少 | 需要维护少量学科入口映射 |

## Decision

采用自动场景路由。Agent 根据自然语言识别 `explore / model-diff / solve / wrong / adversary / practice / import / review / publish`，读取系统契约、当前状态、学科基线和任务 Topic 四层最小上下文。

## Trade-offs

- 接受少量路由误判风险；Agent 应在首屏声明场景和角色，用户可以立即纠正；
- 不自动加载全部 Handbook；跨专题需要时再逐步扩展；
- Topic 尚未形成时，只能提供显式标记的工作假设。

## Revisit Trigger

- 场景误判反复影响学习；
- Topic 数量使关键词匹配不可靠；
- 需要跨多个仓库或外部知识源自动组装上下文。
