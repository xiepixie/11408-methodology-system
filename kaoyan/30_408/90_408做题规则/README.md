# 408 通用做题规则

状态：工作稿，通用入口已建立，规则尚待证据化。

本目录只保存四科共享的做题与考试控制规则，不复制各科学科 Adapter。

统一入口：

$$
\text{Target}
\to \text{Objects}
\to \text{Constraints}
\to \text{Structure}
\to \text{Candidate Paths}
\to \text{Execution}
\to \text{Verification}
\to \text{Expression}
$$

各科具体模拟语言分别进入对应学科的 `90_做题规则/`。

## 已采用

暂无。既有手册中的检查表需要经过真实做题验证后再纳入。

## 待验证

- 综合题先写清当前学科、作用域和状态载体，再开始计算；
- 同时出现多个 miss/fault 时，先区分它们属于哪一层、由谁处理；
- 画时间线、状态表或数据路径之前，先说明图中每一列代表什么。

### 408 首次定位链

这条链是通用九问在 408 状态/路径题中的候选适配，不替代各科 Adapter：

```text
Target
-> Subject / Scope
-> Given State
-> Event / Operation
-> Invariant / Boundary
-> Mechanism / Path
-> Cost
```

- `Target`：先确定要求数值、状态、结构选择还是完整路径；
- `Subject / Scope`：先切到数据结构、计组、OS 或网络的正确观察语言；
- `Given State`：抄出真正会变化的表、队列、寄存器、指针、窗口或缓存行；
- `Event / Operation`：没有触发依据，不擅自改变状态；
- `Invariant / Boundary`：先区分相邻但不同的状态机，再调用机制；
- `Mechanism / Path`：只画当前题实际经过的最小路径；
- `Cost`：最后把路径换算成比较、cycle、I/O、时延或吞吐。

候选停止条件：若前三步已经唯一定位到某一 Subject Topic，立即切换到该学科 Rules，不继续机械填写七项。

## 已否定

暂无。
