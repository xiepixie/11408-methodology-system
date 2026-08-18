# 英语一 学科做题控制

> 类型：Control  
> 状态：已采用；本目录拥有跨题型的考场决策、第一动作、Route、执行协调与 Verify，不拥有各 Topic 的内部机制。

## 1. Canonical Responsibility

Control 回答的是：

> 当前题目/整卷状态下，现在先做什么、走哪条 Route、何时停止、怎样验证？

Atlas 负责定位问题，Topic 负责解释机制，Control 负责把已建立机制动作化：

$$
\boxed{
\text{Atlas: Locate}
\longrightarrow
\text{Topic: Explain / Own Mechanism}
\longrightarrow
\text{Control: Act / Route / Verify}
}
$$

## 2. 题型 Route

- [10_阅读](../10_阅读/README.md)：调用证据定位与选项判定机制
- [20_完形与新题型](../20_完形与新题型/README.md)：调用词项约束满足 / 语篇结构重构机制
- [30_翻译](../30_翻译/README.md)：调用意义恢复与中文重构机制
- [40_写作](../40_写作/README.md)：调用任务到语言生成机制

各 Topic 可以拥有自己的局部 Adapter，但跨题型通用控制链、整卷时间/退出/回退规则与最终 Verify 只在本 Control 层成为 Canonical Rule。

## 3. 与 Practice / Evidence 的边界

First Breakpoint、个人错误频率、训练周期、专项训练与迁移复测属于学习证据平面。它们可以为 Control 提供更新证据，但不因一次观察直接晋升为稳定做题规则。
