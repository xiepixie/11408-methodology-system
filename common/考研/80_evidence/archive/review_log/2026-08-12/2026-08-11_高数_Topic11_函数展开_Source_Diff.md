# Topic11 函数展开 Source Diff

日期：2026-08-11  
场景：import

## Source

- `学习领域/归档/高等数学/II-09_无穷级数敛散性分析核心笔记.md` §6、附录 C：幂级数、半径、端点、母函数与逐项运算。
- `学习领域/归档/高等数学/II-11_傅里叶级数.md`：Fourier 和函数、奇偶延拓、半区间展开、正交性与积分策略。

## 迁移结果

| Source 内容 | Canonical Owner / 处理 |
|---|---|
| 幂级数定义、Abel 半径与三种收敛情形 | Topic11 正文“幂级数” |
| 端点分别代入、代换条件与逐项微积分 | Topic11 正文“端点审计、母函数” |
| Taylor 系数与余项资格 | Topic11 接口；有限误差仍由 Topic03 Own |
| Fourier 和函数的连续值/左右平均 | Topic11 正文“恢复规则” |
| 奇偶延拓、正弦/余弦系数、三角正交性 | Topic11 正文“Fourier” |
| 复分析、Hilbert 空间与 PDE 谱理论 | No Update，留在 Extension |
| 正交投影统一解释 | 转 B08 Bridge，不在本册重复展开 |

## Owner 决策

- **Canonical Update**：新建 `10_数学一/10_高等数学/11_函数展开_幂级数Taylor与Fourier/函数展开_幂级数Taylor与Fourier.tex`。
- **Control Update**：在《高等数学做题规则》中增加 H-R86 至 H-R96。
- **No Update**：不复制 Topic10 的数项级数证明，不把有限 Taylor 误差或个人例题写入公共 Owner。

## 待验证

- 陌生幂级数能否稳定执行“半径—端点”二段式；
- 逐项积分/微分是否同步检查下标、初值与端点；
- Fourier 跳跃点、周期端点和延拓类型是否能在不画图时仍正确判定。
