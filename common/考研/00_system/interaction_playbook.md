# 可重复交互入口

本文件只提供最短入口。完整场景和更新规则见 [人机协作工作流](collaboration_workflow.md)。

## 学完后检查理解

```bash
python3 00_system/cognitive_system.py prompt model-diff
```

先提供自己的解释和对应 Handbook。目标是暴露模型差异，不是让 AI 重讲整章。

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

## 导入手册

```bash
python3 00_system/cognitive_system.py prompt import-handbook
```

提供来源文件和你认为它可能属于的位置。AI 先做 Handbook Diff，不直接覆盖现有 Owner。

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

