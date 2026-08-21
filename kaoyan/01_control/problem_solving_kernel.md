# 解题控制内核与学科适配器 (problem_solving_kernel.md)

> **设计思想**：
> 做题控制（Control Plane）回答“人面对题目时怎样操作心智模型？”
> 为了避免每个学科重复编写一套通用做题控制话术，系统构建了 **Generic Control Kernel（通用解题内核）**，各学科只需维护自己的 **Subject Adapter（学科适配器）**。

---

## 一、 通用解题内核九问 (The 9 Generic Kernel Questions)

无论面对数学、英语还是 408 题目，大脑在微观解题过程（Micro Control）中统一围绕以下九个通用核心问题展开：

$$
\text{Target} \to \text{Objects} \to \text{Constraints} \to \text{Structure} \to \text{Output Shape} \to \text{Candidate Paths} \to \text{Risk Point} \to \text{Verification} \to \text{Expression}
$$

1. **Target (目标)**：目标与得分要求是什么？
2. **Objects (已知对象)**：已知对象及其类型是什么？
3. **Constraints (硬约束)**：条件、边界和隐含限制是什么？
4. **Structure (强结构识别)**：它属于什么结构或已知母题？
5. **Output Shape (输出形式)**：答案应具有什么形式、范围或量级？
6. **Candidate Paths (候选路径)**：有哪些候选路径，为什么选择当前路径？
7. **Risk Point (危险步骤)**：哪一步最危险、最容易出错或踩陷阱？
8. **Verification (及时校验)**：怎样尽早发现错误？
9. **Expression (得分链表达)**：怎样形成最小完整得分链？

这九问是检查维度，不要求机械按 1→9 写完再进入下一项。尤其 **Verification 不只发生在最后**：在选路径前就可以先预测范围、符号、数量级、单位、位宽或状态不变量，用它排除明显错误的候选；求解结束后再用尽量独立的信息做最终检查。也就是说，校验既是事前约束，也是事后确认。

当任务不是“解一道题”，而是“判断题目是否自洽、题目是否打穿模型、模型修改后怎样回测”时，不继续扩张本内核，转 [`../00_system/problem_model_validation.md`](../00_system/problem_model_validation.md)。

---

## 二、 学科适配器 (Subject Adapters)

学科 Adapter 可以扩展通用内核，但不得复制整套通用协议。

### 1. 408 计算机综合适配器 (408 Adapter)
强调**状态机演化与跨子系统推演**：
$$
\text{Object} \longrightarrow \text{State} \longrightarrow \text{Event} \longrightarrow \text{Rule} \longrightarrow \text{New State} \longrightarrow \text{Cost}
$$
- **关注点**：对象 Identity、引用关系 $R$、队列 $Q$、触发事件 $E$、机制 $M$、策略 $\pi$、不变量 $I$ 与成本 $C$。

### 2. 数学一适配器 (Math 1 Adapter)
强调**目标表征与变形降维**：
$$
\text{Object} \longrightarrow \text{Structure} \longrightarrow \text{Representation} \longrightarrow \text{Transformation} \longrightarrow \text{Invariant} \longrightarrow \text{Target}
$$
- **关注点**：定义域硬约束扫描、表征选择（函数/方程/图像/几何/向量）、整体换元、严谨非零校验（$t=0$ 极值检查）。

### 3. 英语一适配器 (English 1 Adapter)
强调**句法剖析与文本功能定位**：
$$
\text{Sentence Structure} \longrightarrow \text{Reference} \longrightarrow \text{Discourse Function} \longrightarrow \text{Author Intent} \longrightarrow \text{Evidence}
$$
- **关注点**：主谓宾主干隔离、代词上文指代还原、篇章论证功能、作者态度词、原文 Evidence 定位与反例排除。
