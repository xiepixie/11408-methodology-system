# Infra Scripts

`infra/scripts/` 是跨领域、Domain-Agnostic 的执行机制 Owner，只回答“如何编译 / 渲染一种底层资产”，不拥有 Teaching 或 Kaoyan 的业务语义。

## Canonical Entrypoints

- `check_repo.py`：全仓只读编排器；检查 Root Wiring 并依次编排 Infra、Teaching 与 Kaoyan 局部 Gate。
- `compile_tex.py`：XeLaTeX 多遍编译、诊断解析、隔离式 Generated State 与**显式** PDF handoff。
- `compile_tikz_to_svg.py`：显式 TikZ 文件/目录到 Dark + Light 纯 Path SVG 的渲染机制。
- `../check_infra.py`：Infra steady-state Gate；真实回归上述机制与 `infra/latex/` Public API，不承载任何 Domain Policy。

## Boundary

`compile_tex.py` 每次都在系统临时目录生成 `.aux/.log/.xdv/PDF`，普通验证不会扫描、删除或覆盖源目录中的既有资产。未指定 handoff 时只把最终 PDF 复制回源码目录；指定 `--publish-dir` 时只复制到显式目标，因此验证/发布不会把已有 Repository PDF 当临时文件移走。历史辅助文件只在用户显式调用 `--clean-all` 时清理；`--keep-aux` 则保留本次隔离构建目录供诊断。需要把最终 XeLaTeX pass 的 warning 也视为失败时使用 `--warnings-as-errors`；严格模式在 PDF handoff 前失败，不会发布带未解释 warning 的产物。

`compile_tex.py` 不自行推断“某个 PDF 应发布到哪里”。调用方若需要交付到特定目录，必须显式传：

```bash
python3 infra/scripts/compile_tex.py <source.tex> --publish-dir <target-dir>
```

例如 `kaoyan/00_system/cognitive_system.py` 拥有考研 Handbook 的发布策略，并把 `kaoyan/90_publish/` 作为参数传给共享编译器。

`compile_tikz_to_svg.py` 也不拥有“扫描哪些数学一/408 年份”的规则；它只处理显式文件或目录。编译时统一暴露 `source dir + infra/latex + repository root` 到 `TEXINPUTS`，因此可解析合法的 Source-local 与 root-logical 输入，但不会替 Domain 推断资产 Owner。考试归档批处理策略归 `kaoyan/00_system/tools/`。

## Steady-State Gate

```bash
python3 infra/check_infra.py
```

该命令使用临时目录完成 Standard/Margin Handbook strict-warning 编译和 TikZ dark/light SVG smoke test；不会在源码目录创建 PDF 或 aux。

## Architecture Invariants

1. **单向依赖**：`teaching/` 与 `kaoyan/` 均向下依赖 `infra/scripts/`，`infra/` 内部代码绝不反向引用 `teaching/` 或 `kaoyan/` 业务逻辑。
2. **纯粹机制**：脚本只处理传入的显式路径与标准参数，不拥有任何学科或教学判定规则。
3. **输出隔离**：默认在独立临时目录构建，自动清理中间产物；支持 `--publish-dir` / `--outdir` 显式交付。
4. **严格模式可选**：共享机制允许普通编译保留 warning 信息，也允许调用方用 `--warnings-as-errors` 提升为业务 Gate；严格程度由 Domain Policy 决定。
