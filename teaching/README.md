# Teaching Domain

`teaching/` 是一对一数学教学交付体系的 Canonical Domain。

## Ownership

```text
teaching/
├── AGENTS.md       # Teaching 业务合同
├── students/       # 学生证据、课次与交付物
├── pool/           # 可复用公共题库
├── topics/         # 可复用专题课
└── templates/      # 新增教学资产的 Forward Standard 模板
```

跨领域 LaTeX 与编译机制不在本域拥有，统一使用：

```text
infra/latex/
infra/scripts/compile_tex.py
```

## Domain Assets

Teaching 域采用高内聚分层架构：

1. **Templates (`teaching/templates/`)**：核心一对一学案/教案与 `questions.tex` 以及 samples 样例；模板题包固定命中 root-logical `teaching/pool`。
2. **Question Pool (`teaching/pool/`)**：初始稳态快照覆盖 9 大专题、138 道标准逻辑题；后续允许新增专题/题目，但不得跌破 no-loss floor。Canonical Public Pool 中无学生姓名、得分率或 `qLYB* / qTJW*` 学生命名 API。
3. **Students (`teaching/students/`)**：学生专属档案与课次业务资产（刘亚博/、谭俊文/），active sessions 采用 `\usepackage{ipara}` 并直连 `teaching/pool`。
4. **Topics (`teaching/topics/`)**：初始稳态 no-loss floor 为 31 个 active topic entry + 1 个 `legacy` quarantine entry，共 90 个源资产；后续允许正常增长，Steady-State Gate 只阻止既有 floor 静默下降。
5. **Compat Bridge (`teaching/compat/`)**：`legacy_pool_aliases.tex` 通过 `\let` 为历史学生宏提供兼容桥梁，不污染公共题库。

## Forward Standard

新建学案/教案只使用标准包名，不写任何历史相对路径：

```latex
\usepackage[student]{ipara}
\usepackage[teacher]{ipara}
```

统一通过：

```bash
python3 infra/scripts/compile_tex.py <目标.tex>
```

解析 `infra/latex/ipara.sty`。

Teaching 业务验收由本域常态门禁唯一持有：

```bash
python3 teaching/check_teaching.py            # 静态分析门禁
python3 teaching/check_teaching.py --compile  # 完整真实 XeLaTeX 4页编译 smoke test
python3 teaching/audit_pool.py                # 题库 no-loss floor + taxonomy / 宏名 / 隐私
python3 teaching/audit_topics.py              # Topic no-loss floor + 路径 / 隐私 / input 完整性
python3 teaching/audit_hygiene.py             # 仓储整洁与隐私防泄漏审计
```

`check_teaching.py` 统一集成 Agent 配置、Pool、Topics 与 Hygiene 审计；`--compile` 使用共享编译器的 strict-warning 模式真实编译核心一对一学案/教案模板，要求二者均为 4 页且最终零 warning。

## Templates & Samples

- **核心模板**：`teaching/templates/一对一错题课_学案模板.tex`、`教案模板.tex`、`questions.tex`。
- **历史样例**：`teaching/templates/samples/`（作为匿名排版参考样例隔离保存，不拥有公共机制）。
