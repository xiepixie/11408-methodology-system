# Kaoyan Maintenance Tools

`kaoyan/00_system/tools/` 只拥有 **Kaoyan Domain 的批处理 / Source Reconstruction / Archive Validation Policy**。底层 LaTeX/TikZ 编译机制仍由 `infra/scripts/` 拥有。

## Tool Classes

| 类型 | 脚本 | 默认语义 |
|---|---|---|
| Read-only Gate | `validate_exam_archive_spec.py` | 可直接运行；发现任意违规必须非零退出；`--quiet` 只压缩成功输出，不减少检查 |
| Read-only Gate | `check_math1_exam_source.py` | 可直接运行；只读检查现有 Math1 Archive；支持 `--quiet` 汇总模式 |
| Source Reconstructor | `scrape_408_exam_archive.py` | 必须显式 `--year` / `--all`；已有年度默认 skip，覆盖需 `--force` |
| Source Reconstructor | `scrape_math1_exam_archive.py` | 必须显式 `--year` / `--historical` / `--all`；已有 Canonical 默认 skip，覆盖需 `--force` |
| Archive Builder | `build_math1_archive.py` | 只补缺或刷新机器索引；已有 Canonical 年度正文和手工 README 默认保留 |
| Derived Asset Generator | `generate_math1_svgs.py` | 显式执行即代表允许重生成 Math1 Semantic SVG；不得由普通索引刷新隐式触发 |

## Steady-State Invariants

1. **Canonical Paths Only**：工具只读取 `kaoyan/archives/`、`kaoyan/00_system/exam_profiles/` 等当前 Owner；迁移完成后不再尝试旧目录 fallback。
2. **Profile Owns Routing**：考试科目路由、年度 override、题量结构由 `exam_profiles/<profile>.json` 拥有；scraper/builder 不维护第二份题号真值。
3. **Explicit Upstream Route**：当前抓取入口由 scraper 顶层 `BASE_URL` 显式声明：408 使用 `https://www.csgraduates.com/study_methods/408quiz`，数学一使用 `https://www.csgraduates.com/study_methods/math/math1`；早年数学卷仍按脚本中的 `math_old/<year>/1/` 特例处理。上游站点改路由时必须同步更新测试，不允许靠未定义变量或隐式拼接兜底。
4. **Explicit Mutation**：会写仓库的脚本不能在“无参数”时偷偷选择某一年或全库作为目标。
5. **Canonical Protection**：已有精校 Canonical Source 默认不可被批处理脚本覆盖；确需重建必须显式 `--force`，并先确认 Source 依据。
6. **Derived ≠ Source**：SVG、索引、solutions 等派生资产可以重生成，但不能反向成为题面或 Handbook 的知识 Owner。Math1 Semantic SVG 的实现唯一由 `generate_math1_svgs.py` 拥有，`build_math1_archive.py` 只显式委托，不复制主题/渲染实现。
7. **Machine Failure = Non-zero Exit**：验证器打印 ERROR 后必须非零退出，供 Agent/CI 可靠判定。
8. **No Hidden Cleanup**：普通检查不得删除旧文件、PDF 或 aux；清理必须属于显式、可解释的维护动作。

## Canonical Commands

```bash
# Read-only archive gates
python3 kaoyan/00_system/tools/validate_exam_archive_spec.py --exam 408
python3 kaoyan/00_system/tools/validate_exam_archive_spec.py --exam math1
python3 kaoyan/00_system/tools/check_math1_exam_source.py

# Explicit reconstruction examples
python3 kaoyan/00_system/tools/scrape_408_exam_archive.py --year 2026
python3 kaoyan/00_system/tools/scrape_math1_exam_archive.py --year 2026

# Intentional overwrite requires explicit force
python3 kaoyan/00_system/tools/scrape_math1_exam_archive.py --year 2026 --force

# Builder: fill missing canonical years / refresh machine index
python3 kaoyan/00_system/tools/build_math1_archive.py --all
python3 kaoyan/00_system/tools/build_math1_archive.py --refresh-index

# Derived SVG 全库重生成必须显式授权
python3 kaoyan/00_system/tools/build_math1_archive.py --regenerate-svg
```

执行真题 Source 重建前仍必须遵守上层 [`../exam_source_agent_prompt.md`](../exam_source_agent_prompt.md) 与 [`../exam_source_conversion_spec.md`](../exam_source_conversion_spec.md)；工具不能替代 Source/Logic Review。
