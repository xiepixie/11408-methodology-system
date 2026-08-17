# 高数 B05/B08 Bridge Source Diff

日期：2026-08-11
场景：import

## Gate 判断

| Bridge | Bridge Validity | Standalone Promotion | Owner 决策 |
|---|---|---|---|
| B05 一点 + Kernel | 线代 $Ax=b$ 与 ODE $L[y]=f$ 都是线性算子逆像：一个特解平移齐次核 | 多个方程组、ODE 和定解问题反复调用，且两侧责任容易重复 | Canonical Bridge Update |
| B08 Fourier 与正交基 | Fourier 系数是函数与正交基函数的内积投影 | 反复用于展开、对称简化、特殊点求和；接口有独立合法性与 Anti-Bridge | Canonical Bridge Update |

## 两侧 Owner

- B05 使用线代 Topic04 `线性方程组_可达性与解空间.tex` 与高数 Topic12 `常微分方程_局部规律与整体轨迹.tex`。
- B08 使用线代 Topic01/B00 与高数 Topic11 `函数展开_幂级数Taylor与Fourier.tex`。
- 本 Bridge 不复制两侧完整求解步骤，只维护“输出—翻译—输入—不变量”。

## 待验证

- 陌生线性方程组/ODE 是否都能先写成“一点 + Kernel”；
- Fourier 系数题能否从内积投影而非死记积分公式复原；
- 是否能阻断“写出系数 = 已证明逐点恢复”和“正交 = 概率独立”两种伪推理。
