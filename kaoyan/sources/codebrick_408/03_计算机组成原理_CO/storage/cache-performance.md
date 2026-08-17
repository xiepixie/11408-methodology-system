---
title: Cache 性能分析（已并入「Cache 基本概念」）
source: https://www.codebrick.tech/co-full/posts/storage/cache-performance.html
---

# Cache 性能分析（已并入「Cache 基本概念」）

本文的内容——命中率、平均访问时间的两种模型、效率与加速比、多级 Cache 的局部命中率与全局命中率——已全部并入 **[[03_计算机组成原理_CO/storage/cache-concept.md|Cache 基本概念与工作原理]]**。

**合并原因**：这些内容与考纲「三（六）1　Cache 的基本原理」是同一条，拆成两篇会让同一组公式出现两遍。

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