# 408 学科架构：Canonical Topology 设计依据

当前状态：框架已采用；本文件记录为什么这样切，不承担日常导航。日常入口见 [408 Course Atlas](../README.md)。

## 1. 最高层决策

408 使用：

```text
408 Course Atlas
├─ 4 Subject Atlas
│  └─ Topic / Internal Bridge / Internal Integration
├─ Cross-Subject Bridge / Cross-Subject Integration
└─ Atlas-owned 跨科母模型补充
```

这里最后一层是 **Course Atlas 的可展开关系层**，不是第五种 Handbook 类型。稳定 Handbook 仍只有 Atlas / Topic / Bridge / Integration；跨科母模型用独立 Markdown 承载长关系解释，是为了避免 Course Atlas README 被某一种设计模式淹没。

四科共享系统地图与 Control Language，不共享一个万能世界模型。

- 数据结构：`Workload -> Relation -> Operations -> Representation -> Invariant -> Cost`
- 计组：`ISA Semantic -> Data Movement -> Hardware Path -> Timing -> Commit`
- OS：`State -> Transition -> Bad State -> Property -> Mechanism -> Tradeoff`
- 网络：`Scope -> State -> Event -> Transition -> Feedback -> Cost`

### 1.1 逻辑架构与物理文件必须分开

Atlas、专题、桥梁、综合分别承担稳定 Handbook 职责；Course Atlas 还可以把高价值跨科关系展开为**母模型补充文档**。文件格式由认知职责决定，不再为了目录整齐强迫不同职责共用一种排版结构。

Atlas 的正文就是地图、关系和路由，因此：

```text
<Atlas Directory>/
├── README.md              # Canonical Atlas Source + Navigation Hub
└── assets/
    └── *_Poster.tex       # 可选派生视觉海报
```

Topic / Bridge / Integration 需要长机制正文，因此：

```text
<Handbook Directory>/
├── README.md          # Landing Page
├── <Handbook>.tex     # Canonical deep body
└── assets/            # 可选

90_publish/
└── *.pdf              # 阅读/视觉视图
```

因此：

- Atlas README 可以直接拥有 Mother Question、Foundation、Topic/Bridge/Integration 地图、关系和 Routing；
- Atlas 不因为缺少 `.tex` 而不成熟；可选海报只能视觉化 README 已有语义，不得产生第二份知识真相；
- Topic / Bridge / Integration 的 README 仍然不能承载长推导和完整机制正文，深度内容必须进入 `.tex`；
- **跨科母模型补充**由 Course Atlas Own，负责跨专题反复出现的设计模式、共同生成逻辑和“禁止错误类比”边界；它不是第五种 Handbook，也不要求存在 A→B 的稳定交接。当前采用 Markdown 长文，放在课程总图的 `00_统一总图/` 下；
- PDF 只是派生阅读/视觉视图，不手工维护，也不拥有知识；
- `00_system/*.md`、Rules、Inbox、架构设计文档继续使用 Markdown。

旧 `30_408/408_Course_Atlas.tex` / PDF 不再是 Owner，但在逐项 Source Diff 完成前保留为 Source。当前唯一 408 Course Atlas Owner 是 `30_408/README.md`；只有有效信息全部迁移、重复项核验且拒绝项留有理由后，旧资产才可删除。

## 2. Foundation 不是第五种 Handbook

复杂度、OS 基础概念这类内容如果只是整门学科反复使用的观察语言、度量语言或基本约定，不因“很重要”就升级成独立 Topic。

因此：

- 数据结构 complexity / asymptotic cost / cost vector 归 Data Structure Atlas Foundation；
- OS 基本概念、user/kernel、system call 基础入口、运行环境与 OS 结构归 OS Atlas Foundation；
- 物理上可以存在 supplement 文件，但它仍由 Atlas Own，不与机制 Topic 平级。

判据不是“有没有 State”，而是：它是否拥有一个需要独立解释的生成机制，还是后续 Topic 共同使用的观察/度量语言。

## 2.1 跨科母模型不是桥梁，也不是第五种 Handbook

当多个独立专题反复面对同一种系统矛盾、采用结构相似的解决手段时，Course Atlas 可以把这条关系展开成独立母模型补充文档。它回答：

```text
重复出现的问题形状
→ 共同生成模型
→ 相似机制
→ 禁止错误类比的边界
→ 路由回各自知识归属
```

晋升条件：

1. 至少跨两个学科重复出现，且不是偶然术语重名；
2. 能抽出稳定母问题、不变量或权衡，而不是只做“相似知识点列表”；
3. 统一模型能生成新的判别/迁移能力；
4. 必须同时写“禁止错误类比”，明确哪些局部机制不能强行同构；
5. 具体状态机、公式、协议和题解仍由原专题拥有。

因此五类认知职责分别是：

- 专题：解释一个本地机制；
- 桥梁：解释两个独立知识归属之间的稳定交接；
- 综合：追踪一次完整过程如何跨多个知识归属跑完；
- Atlas-owned 跨科母模型补充：解释为什么不同领域会反复采用同一种设计思想；
- 规则：把成熟模型压成考场动作。

当前第一份跨科母模型是[缓冲与有限中间态](跨科母模型_缓冲与有限中间态.md)。它统一“有限中间态、空满边界、所有权、反压、调度”的生成逻辑，但不把队列、缓存、窗口、直接存储器访问、假脱机等强行视为同一个状态机。

## 3. Topic 规划

### 数据结构：12 Topic

1. 线性关系与存储表示
2. 栈、队列与受限访问
3. 串与模式匹配
4. 树与二叉树
5. Heap 与优先队列
6. Union-Find 与集合划分
7. 图的表示与遍历
8. 图上的结构算法
9. 查找与有序索引
10. Hash 与直接定位
11. 内部排序
12. 外部排序

原“编码、集合与优先级”不成立为单一 Topic：Huffman 是树的应用，Heap 与 Union-Find 分属不同母问题。

### 计组：8 Topic

保留现有切分：数据表示、ISA、CPU、流水线、主存、Cache、地址翻译、I/O。

### OS：5 Core Topic + Atlas Foundation

1. 执行实体、调度与控制权
2. 并发、同步与死锁
3. 虚拟内存与页生命周期
4. I/O 请求、等待与完成
5. 文件系统与持久化

原 OS-00 降为 Atlas-owned Foundation supplement。

### 网络：8 Topic

保留现有切分：通信基础、单跳交付、可靠传输、IP 转发、路由、传输层、拥塞、应用层。

## 4. Bridge 两道 Gate

### Gate 1｜Bridge Validity

真 Bridge 必须有两个独立 Owner，并存在稳定 handoff：

```text
A output
-> translation/shared structure
-> B input
```

如果只是 B 调用 A 的既有机制，记为 `Use`；如果只是一个完整问题里多个模块合作，归 Integration。

### Gate 2｜Standalone Promotion

真接口不自动获得独立 Handbook。还要检查：

1. Ownership Pressure；
2. Reuse；
3. Current-Scope Relevance；
4. New Inference。

漂亮类比、跨学科、经常一起出现都不是充分理由。

## 5. Internal Bridge 规划

### 数据结构

- DS-B01 Frontier Traversal
- DS-B02 Index Strategy × Workload
- DS-B03 Heap / Union-Find × Graph Algorithm

### 计组

- CO-B01 ISA Semantic × Datapath
- CO-B02 Address Translation × Cache Access

`C -> ISA` 由 ISA Topic Own，不再把 `C × ISA × CPU` 放到跨科层。

### OS

- OS-B01 Wait / Block / Wakeup
- OS-B02 Process × Virtual Memory
- OS-B03 Process × File Reference
- OS-B04 VM × File × I/O

### 网络

- NET-B01 IP Forwarding × Single-Hop Delivery
- NET-B02 Routing × Forwarding
- NET-B03 Reliable Transfer × TCP
- NET-B04 Flow Control × Congestion Control

## 6. Cross-Subject Bridge 规划

### Core

- X-B01 Privilege / Exception / System Call × OS Control
- X-B02 Hardware Address Translation × OS Virtual Memory
- X-B03 Interrupt / DMA × OS I/O

它们都存在明确的状态/控制权 handoff，且不独立建册会造成两侧责任长期混淆。

### Candidate Core

- X-B04 Process / Socket × Transport Endpoint

结构身份已确认是真接口，但是否作为 408 Core Bridge 的优先级仍需真题/覆盖证据验证。工程细节只作 Extension。

### 当前不独立建册

- Graph Algorithm × Routing：真实连接，但当前优先作为 Network Routing 对 DS Graph Algorithm 的 `Use`；
- External-Memory Algorithm × Block I/O：先由 DS Topic 使用 block-I/O cost model；
- Data Structure × Systems：过宽，拆成具体 Use，不建大桥。

## 7. Integration 规划

### Data Structure

DS-I01：从 Workload 到数据结构选择。

### Computer Organization

CO-I01：一条指令的一生，优先用 LOAD 检验慢路径。

### Operating System

- OS-I01：一次 Blocking `read()`；
- OS-I02：`fork()` + COW + resource reference。

### Network

NET-I01：一个网络请求的一生。

### Cross-Subject

- X-I01：一次 LOAD / Memory Access 的完整慢路径；
- X-I02：一次 Blocking File `read()` 的完整生命周期。

网络数据从 NIC 到用户进程的完整路径当前为 Extension，等待 X-B04 核心优先级与相关 Topic 成熟后再决定。

## 8. Anti-Bridge

至少长期阻断：

```text
Hardware Cache != OS Page Cache
TLB miss != Cache miss != Page Fault
Routing algorithm use != Routing protocol identity
Data structure used by a system != automatic cross-subject Bridge
```

## 9. 当前建设原则

本轮只锁定 Topology、Owner 和空框架，不把工作稿自动晋升为“已采用正文”。后续逐科进行 Source Diff / Model Diff，确认每个 Topic 的母模型、边界、反例、Rules 分流和 Coverage。
