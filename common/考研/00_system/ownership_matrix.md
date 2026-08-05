# 全局概念与规则唯一归属矩阵 (ownership_matrix.md)

> **核心原则**：遵从 **One Concept/Rule $\rightarrow$ One Canonical Owner**。新增或引用概念前必须查阅本表；若概念已有 Canonical Owner，其他讲义或学科只能进行引用（`Use / Reference`），严禁重复全文解释。

---

## 一、 408 计算机综合归属矩阵 (408 Matrix)

| 核心概念 / 机制 / 规则 | Canonical Owner (唯一宿主) | Used By (引用与桥梁手册) | 职责界定与说明 |
|---|---|---|---|
| **Process / Thread / Task** | `30_408/30_操作系统/` | 408 总图, CPU×OS, 所有综合册 | 定义 Task 三元组、Running/Ready/Blocked 状态 |
| **Page Table / TLB / Page Fault** | `30_408/30_操作系统/` | VM×File, mmap 综合, CPU×OS | 定义 VA$\to$PTE$\to$PA 映射、TLB 命中与 Fault 修复 |
| **DMA (Direct Memory Access)** | `30_408/20_计算机组成原理/` | CPU×OS, I/O 专题, read() 综合 | 定义总线控制权交接、DMA Controller 硬件行为 |
| **Open File Description (OFD)** | `30_408/30_操作系统/` | fork 综合, unlink 综合, read() 综合 | 定义内核 `file` 对象（offset, flags, 引用计数） |
| **Inode & Dentry** | `30_408/30_操作系统/` | Path lookup, unlink 综合, VFS | 定义文件系统对象身份、硬链接计数与磁盘映射 |
| **Blocking / Wakeup / Sleep** | `30_408/30_操作系统/` | I/O 专题, Pipe, Mutex 争用 | 定义 task 移出 run queue 进入 wait queue 的机制 |
| **COW (Copy-On-Write)** | `30_408/30_操作系统/` | fork 综合, Demand Paging | 定义写时复制 Fault 与页 Frame 重新分配 |
| **Page Cache** | `30_408/30_操作系统/` | VM, File System, read() 综合 | 定义文件 Buffer/Cache 驻留与 dirty writeback |
| **Cache Consistency / Protocol** | `30_408/20_计算机组成原理/` | CPU 缓存, 体系结构 Bridge | 定义 MESI 协议与 L1/L2 Cache 硬件刷脏 |
| **TCP State Machine / Congestion**| `30_408/40_计算机网络/` | OS Socket Bridge, 网络综合 | 定义三路握手、四次挥手与 CWND 拥塞控制 |

---

## 二、 数学一归属矩阵 (Math 1 Matrix)

| 核心概念 / 方法 / 规则 | Canonical Owner (唯一宿主) | Used By (引用手册) | 职责界定与说明 |
|---|---|---|---|
| **定义域优先与硬约束扫描** | `10_数学一/90_学科做题规则/` | 高数导数, 最值, 换元 | 规定求导/换元前必先确定初始定义域紧区间 |
| **等价转化与非零校验** | `10_数学一/90_学科做题规则/` | 导数变形, 极值驻点 | 规定提取公因式/两边同除时必须显式校验 $t=0$ |
| **分部积分预测法** | `10_数学一/10_高等数学/` | 不定积分, 定积分大题 | 规定分部积分前根据 $u, v'$ 复杂度下降趋势决策 |
| **矩阵初等行变换与秩** | `10_数学一/20_线性代数/` | 线性方程组, 特征值 | 定义矩阵降维与向量组极大线性无关组提炼 |
| **全概率公式与 Bayes 逆推** | `10_数学一/30_概率论/` | 随机变量, 条件分布 | 定义复杂事件划分与逆向概率条件推演 |

---

## 三、 规则变更协议 (Change Protocol)

1. 当需要在新讲义中引入新概念时，首先检查本表中是否存在 Owner；
2. 若不存在，在对应学科目录创建新概念或新专题，并在本表追加一行记录；
3. 若存在归属争议，召开教研审查，更新本表后再统一重构相关 Markdown/LaTeX 讲义。
