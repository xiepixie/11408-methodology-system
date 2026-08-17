# 数据结构 DS02 Source-Diff 第一轮

日期：2026-08-12

## 1. 判定

- 类型：Canonical Update
- Knowledge Owner：`30_408/10_数据结构/02_栈队列与受限访问/DS02_栈队列与受限访问_方法论手册.tex`
- Landing：`30_408/10_数据结构/02_栈队列与受限访问/README.md`
- 代码证据：`code/ds02_restricted_access.hpp` 与 `code/ds02_restricted_access_test.cpp`

## 2. 旧材料吸收

- 吸收归档总册中“减少自由度换取过程语义”的主线，把 LIFO/FIFO 从端点限制生成出来。
- 吸收“循环队列的关键是空、满消歧与 front/rear 语义，不只是取模公式”的判断。
- 吸收 Frontier 视角，但将树/图遍历正确性继续路由到 DS-B01、DS04、DS07。
- BFS/DFS、括号、表达式与单调结构保留为 Use，不提升为 DS02 所有的机制。

## 3. 新增深度

- 建立 `Access Restriction -> Temporal Order -> State Transition -> Invariant -> Application Contract` 母模型。
- 区分 ADT 契约与顺序/链接表示，展开顺序栈、链栈、循环队列、链队列、循环双端队列的完整状态生命周期。
- 对循环队列三种空满消歧协议给出边界，并把本册实现固定为长度计数协议。
- 增加复杂度前提、六组概念边界、应用 Owner 停止点与做题控制协议。

## 4. 代码机制证据

- 完整 C++17 实现覆盖顺序栈、链栈、循环队列、链队列与循环双端队列。
- 正文通过 `\lstinputlisting` 直接抽取同一源文件，解释字段语义、更新顺序、不变量修复与边界分支。
- 测试覆盖容量为 0、上溢/下溢、循环回绕、FIFO/LIFO、链队列单节点删空后复用、双端交错操作及结构不变量。
- 已使用严格警告编译和 Address/UndefinedBehavior Sanitizer 验证。

## 5. 未提升内容

- 递归语义、表达式文法、树/图遍历正确性：已有其他 Owner。
- 单调栈/单调队列的候选淘汰机制：不等于普通受限访问契约，留给相应算法专题。
- 动态扩容顺序栈：本册实现采用固定容量，正文只作为明确标注的表示变体讨论。
