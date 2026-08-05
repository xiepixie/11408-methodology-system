# 手册契约与结构规范 (handbook_contract.md)

> **目标**：规范每一本正式方法论手册（Topic / Bridge / Integration）的必要槽位与呈现格式，确保全系统所有讲义结构统一、防重且具备高可读性。

---

## 一、 手册必要槽位契约 (The 14 Mandatory Sections)

每一本进入 `Published Handbook`（或编写 `.tex`）的方法论手册，必须显式包含以下 14 个核心结构槽位：

```text
1. Position (系统定位)
2. Boundary (边界与非目标)
3. Mother Problem (母题重述)
4. Mother Model (母模型/形式化描述)
5. Objects (核心存在对象及其状态)
6. Mechanisms (受控状态转换机制)
7. Lifecycle (对象与关系的生命周期)
8. Invariants (安全、隔离与一致性不变量)
9. Trade-offs (成本与性能折衷)
10. Interfaces (对外暴露与依赖接口)
11. Exam Map (考题地图与考点识别信号)
12. Decision Tree (一页式考场决策树)
13. Pitfalls (典型陷阱与常见易错点)
14. Compression Page (1 页纸极简复盘/一界一页)
```

---

## 二、 三类手册的侧重点区别

| 手册类型 | 核心关注槽位 | 典型呈现特征 |
|---|---|---|
| **Topic Manual (专题手册)** | Objects, Mechanisms, Invariants | 深入打穿单一局部机制（如 VM 的页表与 Fault 修复） |
| **Bridge Manual (桥梁手册)** | Interfaces, Boundary, Trade-offs | 专门研究两个专题交接处的接口语义（如 `mmap` 的 VM $\leftrightarrow$ File 边界） |
| **Integration Manual (综合手册)** | Mother Model, Event-driven Flow, Decision Tree | 追踪多机制协同下的完整事件与状态流转链（如 `read()` 操作） |

---

## 三、 LaTeX 排版与 4 页精排约束 (The 4-Page Principle)

在导出为 LaTeX 讲义 (`.tex`) 时，教案与学案必须遵循以下物理约束：

1. **一界一页 (4-Page Layout for Teacher Guides)**：
   - **第 1 页：课堂教学导引**（元信息 + 3 项可观察成功标准 + 120min 路线表 + 动态 Checkpoint & 分支路由）；
   - **第 2 页：备课知识库与几何/拓扑模型**（2–3 个经典 TikZ 结构图 + 核心推导链）；
   - **第 3 页：核心题目精讲与诊断**（单栏干净题面 + 双栏 `paracol (0.68/0.32)` 得分板书与追问梯度）；
   - **第 4 页：课后总结与复练落实**（`5.5cm` 独立高对比手写框 `tcolorbox` + 吸底课后任务）。

2. **计算机/拓扑流程图黄金五原则**：
   - 连线优先级：Direct $\to$ One-bend $\to$ Orthogonal multi-bend $\to$ Outer routing；
   - 矩阵先于节点：先设 Column/Row 网格再填充逻辑；
   - 包络盒预算：整图宽度 $W_{\text{figure}} \le \min(13.6\text{cm}, 0.90\linewidth)$，绝不挤压边框；
   - 固定尺寸与文案分层：节点尺寸 $2.55\text{cm} \times 0.92\text{cm}$，第一行对象/动作，第二行状态/语义；
   - 统一线型：实线控制流、粗实线 Main Path、虚线静态引用、点线 Fast Path/Cache、双线框 `persistent` 对象。

3. **零编译 Warning/Error 约束**：
   - 统一使用 `python3 common/scripts/compile_tex.py <target.tex>` 编译，确保多遍编译后 `\zpageref{LastPage}` 正确，无 `??` 问号与未决引用。
