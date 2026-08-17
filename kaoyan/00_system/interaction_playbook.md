# 可重复交互入口

本文件只提供最短入口。完整场景和更新规则见 [人机协作工作流](collaboration_workflow.md)。

## 尚未形成模型，探索性讨论

```bash
python3 00_system/cognitive_system.py prompt explore
```

提供学科/专题 + 目前的直觉或最困惑的问题。AI 从母问题开始，不直接交付完整讲义。

## 学完后检查理解

```bash
python3 00_system/cognitive_system.py prompt model-diff
```

先提供自己的解释和对应 Handbook。目标是暴露模型差异，不是让 AI 重讲整章。

## 题目不会，按现有模型讲解

```bash
python3 00_system/cognitive_system.py prompt solve
```

提供题目 + 卡住的位置。AI 沿已有心智模型给出解答，不脱离项目语言。

## 错题诊断

```bash
python3 00_system/cognitive_system.py prompt first-divergence
```

提供题目、原始过程、答案和用时。缺失过程保持未知。

## 攻击候选规则

```bash
python3 00_system/cognitive_system.py prompt adversary
```

提供规则、适用范围以及已经观察到的成功/失败场景。

## 针对断点设计训练题

```bash
python3 00_system/cognitive_system.py prompt practice
```

提供已确认断点 + 希望训练的难度/时间。AI 只设计少量有区分力的诊断题。

## 导入手册

```bash
python3 00_system/cognitive_system.py prompt import-handbook
```

提供来源文件和你认为它可能属于的位置。AI 先做 Handbook Diff，不直接覆盖现有 Owner。

## 转译真题 / PDF / 高清题图

提供考试科目、年份和原始材料；若某批高清图应作为最高依据，直接说明“以这批图为准”。AI 进入 `exam-source` 场景后统一读取 `exam_source_agent_prompt.md` → `exam_source_conversion_spec.md` → 对应 Exam Profile。408 与数学一共用这一个入口，完成态写入对应 Exam Archive，并在 SVG 重建后执行 Question-Driven Logic Review。

## 周复盘

```bash
python3 00_system/cognitive_system.py prompt weekly-review
```

提供 Inbox、待验证 Rules 和本周真实表现。

## 发布

```bash
python3 00_system/cognitive_system.py prompt publish
```

发布前先确认 Canonical 内容和依赖已经稳定。


