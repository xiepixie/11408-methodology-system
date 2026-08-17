# Teaching Domain Evergreen Hygiene & Lifecycle Policy

> **目标**：维护教学体系（`teaching/`）在三域架构下的长期整洁、低耦合与资产可追溯性。

---

## 1. 核心资产分层与 Ownership

同一教学事实或规则只有唯一 Canonical Owner：

| 资产层级 | Canonical 路径 | 核心职责 | 隐私与生命周期规则 |
|---|---|---|---|
| **模板层** | `teaching/templates/` | 一对一错题课学案/教案 4 页模板、`questions.tex` 题包 | 公共资产，零学生姓名，精排 4 页无溢出 |
| **公共题库** | `teaching/pool/` | 按 `[专题]/[难度]/q_*.tex` 组织的可增长 Canonical 题库；初始 no-loss floor 为 138 题 | 公共资产，零学生姓名/得分率，宏名全局唯一 |
| **专题库** | `teaching/topics/` | 可增长的系统化专题讲义与备课教案；初始 no-loss floor 为 90 个源资产 | 公共资产，零学生个人事实泄露，`\input` 规范解析 |
| **学生业务** | `teaching/students/` | 学生档案（`profile.md`）、课次会话（`sessions/`）、交付 PDF | 专属资产，拥有具体学生学情、历史诊断与课堂表现 |
| **兼容层** | `teaching/compat/` | 历史学生宏 alias 与必要兼容路由；学生事实本体已回归 `teaching/students/` | 只做薄转发/指针，不拥有新的题目实现或学生事实 |

---

## 2. 自动化门禁与校验契约 (Steady-State Gates)

每次修改或新增教学资产，必须执行以下常态门禁：

```bash
# 1. 教学域核心综合门禁（含静态分析与模板真实 XeLaTeX 4页编译 smoke test）
python3 teaching/check_teaching.py --compile

# 2. 公共题库 no-loss floor、taxonomy 与宏名唯一性审计
python3 teaching/audit_pool.py

# 3. 专题库 no-loss floor、路径与隐私边界审计
python3 teaching/audit_topics.py

# 4. 仓储生成物与整洁度审计
python3 teaching/audit_hygiene.py
```

---

## 3. 生成物隔离与清理策略 (Quarantine & Clean)

1. **编译辅助文件严格隔离**：
   - `.aux`, `.log`, `.out`, `.toc`, `.xdv`, `.synctex.gz`, `.fls`, `.fdb_latexmk` 必须在临时构建目录中隔离或由 `infra/scripts/compile_tex.py` 自动清理；
   - 严禁将编译中间件提交至源码目录。
2. **派生 PDF 生命周期**：
   - 学生交付 PDF 保留在对应 `teaching/students/<学生>/sessions/<课次>/` 目录；
   - 专题与模板的验证性编译产物在测试后即时清理，不与 `.tex` 源码混杂；
   - 考研手册阅读视图统一位于 `kaoyan/90_publish/<category>/`。
3. **临时运行时隔离**：
   - `__pycache__`、`tmp/`、`.venv` 严禁出现在业务资产目录内。

---

## 4. 隐私保护与“去学生化”资产提炼流程

当从真实教学会话中提炼新的公共题库或专题讲义时，严格遵守：

```text
真实学生课次记录 (teaching/students/<学生>/sessions/)
  ├── 课堂证据与个性化卡点 -> 沉淀入 students/<学生>/profile.md
  └── 优秀通用题目/推导
        ├── 剥离学生姓名与专属得分率
        ├── 提取标准数学命题与通用诊断逻辑
        └── 晋升至 teaching/pool/ 或 teaching/topics/
```

确保公共资产可无缝复用于任何后续学生，且绝不反向泄露过往学生隐私。
