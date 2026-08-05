# 解题控制内核与学科适配器 (problem_solving_kernel.md)

> **设计思想**：
> 做题控制（Control Plane）回答“人面对题目时怎样操作心智模型？”
> 为了避免每个学科重复编写一套做题控制话术，系统构建了 **Generic Control Kernel（通用解题内核）**，各学科只需维护自己的 **Subject Adapter（学科适配器）**。

---

## 一、 通用解题内核 (Generic Control Kernel)

无论面对数学、英语还是 408 题目，大脑在解题过程中统一执行**通用五断点模型**与**八项核心提问**：

```
[ 1. Recognition (识别) ] ──> [ 2. Planning (路径) ] ──> [ 3. Execution (转化/执行) ]
                                                                     │
[ 5. Expression (表达) ] <── [ 4. Verification (校验) ] <────────────┘
```

### 通用八问 (The 8 Kernel Questions)
1. **Target (目标)**：题目最终要求输出什么格式的答案？
2. **Objects (已知对象)**：已知包含了哪些对象与初始条件？
3. **Constraints (初始约束)**：存在哪些显式/隐式硬约束（定义域、权限、数据范围）？
4. **Structure (强结构识别)**：题面触发了什么已知强结构或定理模式？
5. **Path Candidate (候选路径)**：正推能产生什么？逆推前一步需要什么？
6. **Execution Step (转化动作)**：当前每一步计算/推导是否减少了自由度、暴露了结构？
7. **Verification / Invariant (校验与不变量)**：哪一步最危险？有没有违法不变量？
8. **Expression (得分链表达)**：卷面上不可缺少的核心得分句与步骤是否完整？

---

## 二、 408 计算机综合适配器 (408 Adapter)

408 的解题控制核心在于**状态机演化与跨子系统推演**：

\[
\boxed{
\text{Object}
\xrightarrow{E}
\text{State}
\xrightarrow{M}
\text{Allowed Transitions}
\xrightarrow{\pi}
\text{New State}
\xrightarrow{\text{Invariant \& Cost}}
\text{Answer}
}
\]

### 408 专用控制流：
1. **写出 Snapshot 状态**：列出题目中存在的对象 $O$、关系 $R$ 与队列 $Q$；
2. **捕获 Trigger Event**：识别引发变化的真正事件 $E$（Syscall, Interrupt, Fault, Timer, Reclaim）；
3. **匹配 Mechanism**：指出内核/硬件允许的受控状态转换；
4. **评估 Policy**：若存在多个合法选择，判断策略选谁；
5. **不变量与成本检验**：检查并发/崩溃不变量，区分 fast path 与 slow path 成本。

---

## 三、 数学一适配器 (Math 1 Adapter)

数学一的解题控制核心在于**目标表征与变形降维**：

\[
\boxed{
\text{Object}
\rightarrow
\text{Initial Constraint (扫描)}
\rightarrow
\text{Representation (选表征)}
\rightarrow
\text{Transformation (换元/降维)}
\rightarrow
\text{Invariant Check (非零/端点)}
\rightarrow
\text{Target}
}
\]

### 数学一专用控制流：
1. **读目标**：先看最终最值/证明目标，决定决策方向；
2. **扫初始约束（定义域优先）**：先锁死定义域紧区间（分母 $\neq 0$、根式 $\ge 0$、真数 $>0$），防止盲目求导；
3. **选表征**：对比函数、方程、图像、几何或向量五种语言，选择计算量最小的表征；
4. **做转化与换元**：利用整体换元减少自由度、消除根式/绝对值；
5. **严格非零校验**：提取公因式或同除变量时，必须显式校验 $t=0$ 的极值与单调性；
6. **写闭环**：卷面完整呈现得分句与收尾检验。

---

## 四、 英语一适配器 (English 1 Adapter)

英语一的解题控制核心在于**句法表征与文本功能定位**：

\[
\boxed{
\text{Sentence Structure}
\rightarrow
\text{Reference & Coreference}
\rightarrow
\text{Discourse Function}
\rightarrow
\text{Author Intent}
\rightarrow
\text{Evidence Option}
}
\]

### 英语一专用控制流：
1. **长难句切分**：提取主谓宾主干，隔离定从、状从与同位语插入语；
2. **指代还原**：将 `it`, `they`, `this`, `such` 准确还原为上文实体对象；
3. **篇章功能识别**：判断本段属于举例支持、转折对比、让步限定还是结论推导；
4. **作者态度定位**：区分纯客观事实描述与作者主观态度词；
5. **选项定位与反例排除**：定位原文 Evidence 句子，排除无中生有、偷换概念、强加因果与范围扩大选项。
