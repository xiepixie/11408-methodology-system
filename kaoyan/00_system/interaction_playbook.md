# 场景启动速查

> 本文件只提供命令速查，不拥有场景定义、角色行为或写入规则。
>
> 场景与最小上下文由 [`agent_context_protocol.md`](agent_context_protocol.md) 统一定义；场景结束后的文件更新由 [`collaboration_workflow.md`](collaboration_workflow.md) 统一定义。

统一入口：

```bash
python3 00_system/cognitive_system.py start <scenario> --subject <subject> [--topic <topic>]
```

常用场景：

| 场景 | 用途 |
|---|---|
| `explore` | 尚未形成稳定模型，探索母问题与最小模型 |
| `model-diff` | 对照已有模型检查自己的理解 |
| `solve` | 按现有心智模型讲解单题 |
| `wrong` | 保留原始过程并定位第一次偏离 |
| `adversary` | 攻击候选理解或规则 |
| `practice` | 针对已确认断点设计诊断练习 |
| `import` | 导入旧稿、外部材料或 Handbook Source |
| `exam-source` | 重建 PDF、扫描卷或高清题图为 Canonical Exam Source |
| `exam-solution` | 基于 Canonical Exam Source 与现有模型撰写真题题解 |
| `review` | 复盘 Inbox、候选 Rules 与真实表现 |
| `publish` | 发布 Topic / Bridge / Integration 阅读版 |

示例：

```bash
python3 00_system/cognitive_system.py start wrong --subject calculus --topic 极限
python3 00_system/cognitive_system.py start exam-source --subject math
python3 00_system/cognitive_system.py start exam-solution --subject 408
```

不要再使用已淘汰的 `cognitive_system.py prompt ...` 接口。需要执行细节时读取对应场景 Owner，不在本速查页复制第二套提示词。
