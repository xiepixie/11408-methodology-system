# 数据结构 DS01 Source Diff 第一轮

> 日期：2026-08-11
>
> 性质：Evidence 层 Source Diff / Model Diff 记录，不是新的知识 Owner。

## 1. Context Used

- 数据结构 Subject Atlas：`30_408/10_数据结构/README.md`；
- Atlas Foundation / Deep Map 旧稿：`30_408/10_数据结构/00_学科总图/README.md`；
- DS01 Landing Page：`30_408/10_数据结构/01_线性关系与存储表示/README.md`；
- 归档 Source：`学习领域/归档/数据结构/_数据结构 MOC.md`、`学习领域/归档/数据结构/算法时间复杂度：统一分析框架.md`；
- 相关算法 Source：算法笔记归档中的列表、队列、哈希和遍历材料，仅作实现/调用证据，不改变 DS01 Owner。

## 2. Source Facts

旧笔记已经包含四类可复用事实：

1. 复杂度必须先固定问题规模、基本操作和单次成本，再讨论 $O/\Omega/\Theta$、循环、递归、分治和空间峰值；
2. 数据结构 MOC 覆盖顺序表、链表、栈队列、串、树、图、查找、Hash 和排序，但仍是章节清单，没有统一“逻辑对象—物理表示—不变量—操作成本”解释；
3. 算法笔记里 `list`、`deque`、`dict`、队列和建图写法主要是语言实现经验，不应直接成为 408 的结构定义；
4. 旧材料没有稳定区分“按位访问”“按值定位”“已知前驱后的局部插入”三种不同操作契约。

## 3. Model Diff

### 旧模型的可保留部分

```text
问题规模 / 基本操作 / 单次成本 -> 总成本
```

以及顺序表的地址计算、链表的指针连接、边界状态和基本操作复杂度。

### 旧模型的缺口

- 逻辑线性表与顺序/链式存储混在一起；
- “链表插入删除 $O(1)$”没有绑定“节点或前驱已定位”的前提；
- 长度、容量、头尾指针和有效节点集合没有被写成同一个合法状态；
- 插入/删除常被压缩成代码动作，缺少 `Locate -> Update -> Repair -> Verify` 生命周期；
- 复杂度常被写成孤立数字，没有拆出定位、移动/跳转、维护和额外空间；
- Python 容器 API、工程实现和 408 抽象边界没有分层。

## 4. Canonical Update

新建唯一正文：

`30_408/10_数据结构/01_线性关系与存储表示/DS01_线性关系与存储表示_方法论手册.tex`

母模型固定为：

```text
Linear Relation
-> Operation Contract
-> Representation
-> Local Update
-> Invariant
-> Cost Vector
```

正文已补入：顺序表地址映射与容量、链式节点与可达性、单/双链表局部修改、按值删除的两阶段成本、空/首/尾/重复值边界、五列概念边界、做题控制协议和跨册 handoff。

## 4.1 代码增补（2026-08-12）

用户确认“每一专题的相关代码也是重要内容”后，本轮将代码从实现例子提升为数据结构 Topic 的机制证据：

```text
Operation Contract
-> State Fields
-> Core Transition
-> Invariant Repair
-> Boundary Branches
-> Complexity
-> Executable Tests
```

DS01 新增：

- `code/ds01_linear_list.hpp`：顺序表与单链表的完整 C++17 伴随实现；
- `code/ds01_linear_list_test.cpp`：扩容、非法位置、空表、非法前驱、尾后删除、首尾删除和删除至空表的断言测试；
- Canonical `.tex` 直接用 `\lstinputlisting` 引用上述真实代码的关键行，解释操作顺序、不变量和成本前提，避免正文摘录与实现漂移。

验证：普通严格编译和 `AddressSanitizer + UndefinedBehaviorSanitizer` 两路均通过。伴随代码是 Canonical 正文的可执行证据，不成为第二知识 Owner。

## 5. Facts vs Hypotheses

### 当前事实

- DS01 目录已有唯一 Canonical `.tex` 和 Landing Page；
- DS01 已有可编译伴随实现和断言测试，正文直接引用同一源文件；
- 该正文没有把栈、队列、树、图、Hash 或排序机制复制进来；
- 复杂度分析仍由 Atlas Foundation Own，DS01 只使用局部成本向量。

### 待验证假设

- `Locate -> Update -> Repair -> Verify` 是否能减少线性表真题中漏改 head/tail/length 的错误；
- “操作输入契约先于容器名称”是否能稳定区分数组/链表题的实际复杂度；
- 顺序/链接表示的成本向量能否作为后续 DS02、DS09 的共同接口。

## 6. 结果分类

**Canonical Candidate + Candidate Rules；未升级为已采用。**

下一最小验证：用 3 道不同输入契约的线性表题（按位插入、已知前驱插入、按值删除）检查学生是否能先写表示、再写不变量和分项成本。
