---
title: Cache 综合大题（已拆分并入前四篇）
source: https://www.codebrick.tech/co-full/posts/storage/cache-comprehensive.html
---

# Cache 综合大题（已拆分并入前四篇）

本文原是一道 Cache 综合大题的逐问演算。内容已按性质拆开：

| 原内容 | 去向 |
| --- | --- |
| 数组占几个主存块（首址不对齐要多算一块） | [[03_计算机组成原理_CO/storage/cache-mapping.md|Cache 地址映射]] |
| 虚拟地址能否直接切出 Cache 组号 | [[03_计算机组成原理_CO/storage/cache-mapping.md|Cache 地址映射]] |
| 局部性怎么判、读改写算几次访存 | [[03_计算机组成原理_CO/storage/cache-concept.md|Cache 基本概念]] |
| 具体真题的逐问演算 | 题库（各题自带完整解析） |

**拆分原因**：真题的完整解答在题库里已经有，博客再写一遍就是第二个副本。博客负责讲清方法与边界，具体某道题怎么解请到题库看。

如果页面没有自动跳转，请点击上方链接。

### 相关文章

- [[03_计算机组成原理_CO/storage/memory-overview.md|存储器的分类]]
- [[03_计算机组成原理_CO/storage/memory-hierarchy.md|层次化存储器的基本结构]]
- [[03_计算机组成原理_CO/storage/sram-dram.md|半导体随机存取存储器]]
- [DRAM 芯片与内存条](https://www.codebrick.tech/co-full/posts/storage/dram-memory-module)
- [[03_计算机组成原理_CO/storage/memory-interleave.md|多模块存储器]]
- [[03_计算机组成原理_CO/storage/memory-expansion.md|主存和 CPU 之间的连接]]
- [[03_计算机组成原理_CO/storage/external-storage.md|外部存储器]]
- [[03_计算机组成原理_CO/storage/cache-concept.md|Cache 的基本原理]]
- [[03_计算机组成原理_CO/storage/cache-mapping.md|Cache 和主存之间的映射方式]]
- [[03_计算机组成原理_CO/storage/cache-replace.md|Cache 中主存块的替换算法]]
- [[03_计算机组成原理_CO/storage/cache-write-policy.md|Cache 写策略]]
- [[03_计算机组成原理_CO/storage/virtual-memory-hw.md|虚拟存储器]]
- [[03_计算机组成原理_CO/storage/memory-hierarchy-simulator.md|存储层次全景（模拟器）]]