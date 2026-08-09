# 快速开始一次学习协作

不需要记 AI 角色，也不需要自己找更新文件。直接用下面任一句开场。

## 还没有形成模型

> 我还没有形成【专题】的心智模型。下面是我目前的直觉和困惑。先和我讨论，不要直接写完整讲义。

Agent 会进入 `explore`，先读学科复习总览与导航和 Atlas，再通过母问题、例子、反例和复述帮助形成工作模型。

## 这题不会，希望按已有模型讲

> 这道【学科/专题】题我不会。请先读取我们已有的心智模型，再给出模型锚点、解题链和校验方法。题目是：……我卡在：……

Agent 会进入 `solve`。如果 Topic 尚无成熟正文，它会明确说明，而不是假装仓库已有答案。

## 做错了，想找真正原因

> 这是题目、我的原始过程和答案。先不要重做，请找 First Divergence，并判断是模型没形成、没触发、误用，还是执行/考试决策问题。

Agent 会进入 `wrong`，优先保护原始过程并给出最小复测。

## 刚学完，检查理解

> 这是我刚学完后自己的解释。请对照现有 Handbook 做 Model Diff，只指出主干、混淆、缺口和边界。

## 攻击一个理解或规则

> 我怀疑下面这条理解/规则成立。请找最小反例、失效条件、成本和更简单的竞争解释。

## 针对弱点训练

> 已确认我的断点是……请只设计少量能区分“会不会调用模型”的诊断题，并说明每题观察什么。

## 导入手册

> 这是新手册/旧稿。先判断产品类型和 Canonical Owner，做 Handbook Diff，列出需要我确认的冲突，不要直接覆盖现有模型。

## 周复盘

> 这是本周 Inbox、待验证 Rules 和真实表现。请帮我删除噪声、攻击候选规则、找模型冲突，并提出下一轮最小训练。

## 命令行入口

Codex 可以自行运行；其他场景也可以手动生成启动包：

```bash
python3 00_system/cognitive_system.py start solve --subject network --topic 可靠传输
python3 00_system/cognitive_system.py start wrong --subject os --topic 虚拟内存
python3 00_system/cognitive_system.py start explore --subject data-structure --topic 图
```

完整路由规则见 [Agent 场景路由与 Context Pack 协议](00_system/agent_context_protocol.md)。

