# AI-I04｜现代 LLM 应用系统：Context、Retrieval、RAG、Memory、Agent、Workflow 与 MCP

> 类型：Integration（综合专题）  
> 状态：待人工确认；Canonical LaTeX 正文与配图已建立，当前已补齐 Long-term Memory、Agent Harness、Durable Session/Context 分离、Brain--Hands--Session 解耦、Loop/Graph、Skill/Tool/MCP/Subagent、Multi-Agent/Deep Research、Containment 与 Agent Eval/LLMOps 回归闭环

## 这本手册解决什么问题

一个语言模型本身只负责根据当前输入生成输出。真实 LLM 应用还要处理私有知识、实时业务数据、工具调用、多步状态、权限、失败恢复和质量评估。

本册追踪一条完整运行链：

```text
用户任务
→ 组装当前 Context
→ 按需检索外部证据
→ 模型生成或提出 Tool Call
→ Runtime 校验并执行工具
→ Observation / State 回到下一轮
→ 输出结果
→ Evaluation / Security / Observability 验证整条链
```

## 本册负责什么

本册只 Own **Composition / Runtime Contract**：

- Context、Retrieval、RAG、Tool Calling、Agent、Workflow、MCP 怎样接成一次完整任务；
- Model 与 Agent Harness 怎样分责，Context、Tools、Loop、State、Memory、Permissions、Trace/Eval Hooks 怎样组成可运行代理；
- 为什么长时程任务必须把 Durable Session 与当前 Context Window 分开，并把 Model/Harness（Brain）与 Sandbox/Tools（Hands）解耦；
- Loop 与 Graph/Workflow 怎样分配控制权，以及怎样在同一系统中嵌套组合；
- Skill、Tool、MCP、Subagent 分别解决什么问题，为什么不能都叫“Agent 能力”；
- Multi-Agent / orchestrator-worker 什么时候值得使用，Deep Research 怎样作为开放研究的 Integration 模式；
- 每一步传递什么对象，谁拥有控制权；
- Graph State、Checkpoint、Long-term Memory、Vector Store 为什么必须分开；
- Long-term Memory 怎样完成写入决策、持久化、检索、时间更新、合并/失效与 Context 注入；
- LangChain 与 LangGraph 在当前版本下怎样分工；
- Tool / MCP 接入以后权限、重试、副作用、环境级 containment、观测与评测怎样补齐；
- Agent Eval 为什么必须区分 Task / Trial / Grader / Transcript，并把 Runtime 资源条件视为实验变量；
- 什么时候普通代码、单次模型调用、RAG、固定 Workflow 已经足够，不需要继续提高 Agent 自主性。

Transformer、概率、优化、生成建模、搜索、决策等单点机制仍回到各自 Core Area。

## Canonical 正文与配图

- [Canonical LaTeX 正文](AI-I04_现代LLM应用系统_Context_RAG_Agent_Workflow_MCP.tex)
- [阶段性阅读版 PDF](../../../../90_publish/interview/AI-I04_现代LLM应用系统_Context_RAG_Agent_Workflow_MCP.pdf)
- 配图：
  - `现代LLM应用系统总架构`
  - `RAG索引路径与请求路径`
  - `Agent受控运行时循环`
  - `MCP主机客户端服务器边界`
  - `Agent长期记忆生命周期`
  - `AgentHarness边界`
  - `Loop与Graph混合控制`
  - `长时程Agent解耦架构`

## 主要 Owner

- Transformer / Attention → `../../60_深度学习/`
- Autoregressive generation → `../../80_生成模型/`
- Learning / evaluation contract → `../../40_机器学习/`
- Optimization / AutoDiff → `../../50_优化与学习计算/`
- Search → `../../10_问题求解/`
- Sequential decision / RL → `../../70_决策_控制与强化学习/`

## 阅读后应该能回答

1. 模型这一轮真正能看到什么？
2. 外部证据从哪里来，为什么不是把所有文档都塞进 Context？
3. Retrieval 与 RAG 的边界在哪里？结构化事实、语义证据和实时副作用分别应该走 SQL/API、Retrieval 还是 Tool？
4. Tool Call 是谁提出、谁校验、谁真正执行？
5. Agent 为什么是受控循环，而不是“更聪明的 LLM”？
6. Agent Harness 在模型之外究竟负责哪些运行时责任？为什么 Harness workaround 必须随模型升级重新做 ablation？
7. Session 与 Context Window 为什么不是同一个对象，Harness/Sandbox crash 后怎样恢复？
8. Skill、Tool、MCP、Subagent 为什么是四种不同接口？
9. State、Checkpoint、Memory、Vector Store 分别存什么？
10. Long-term Memory 应该记什么、什么时候写、怎样检索、怎样处理过时事实？
11. Loop 与 Graph/Workflow 怎样选择，为什么二者可以嵌套而不是互相替代？
12. 什么时候值得拆成多个 Agent，orchestrator-worker 与 planner-generator-evaluator 分别解决什么问题？
13. 为什么安全不能只靠 permission prompt，而要从 Sandbox、Credential 与 Egress 层限制 Blast Radius？
14. MCP 标准化了哪一层，它为什么既不是 Agent 也不是安全边界？
15. 怎样通过 repeated Trials + Trace → Eval → Diagnose → Change → Replay/Regression 持续维护系统？

## Stop Boundary

本册到“一个现代 LLM 应用怎样可靠完成一次外部知识/工具增强任务”为止。模型训练、Transformer 内部机制、Embedding 模型训练、具体向量索引算法、OAuth/OIDC 细节、分布式数据库实现和各业务 API 的内部协议回各自 Owner 或工程专题。
