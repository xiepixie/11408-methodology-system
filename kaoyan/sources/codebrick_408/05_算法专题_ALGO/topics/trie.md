---
title: 字典树 Trie：搜索引擎的关键词提示
source: https://www.codebrick.tech/algo-blog/posts/topics/trie.html
---

# 字典树 Trie：搜索引擎的关键词提示

## 场景引入

在搜索引擎中输入"algo"，立刻弹出"algorithm"、"algebra"等提示。要从百万级词库中快速找到所有以某个前缀开头的词，哈希表做不到（它只能精确查找），但 Trie 树可以。

## 核心原理

Trie 树（前缀树）把字符串存储在树的路径上，每个节点代表一个字符。

```
插入 "cat", "car", "dog":

        root
       /    \
      c      d
      |      |
      a      o
     / \     |
    t   r    g
```

### Trie 树结构示例

插入 "cat", "car", "dog", "app", "apple" 后的 Trie 结构：

## LC 208. 实现 Trie
javascript

```
class TrieNode {
  constructor() {
    this.children = {};
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let node = this.root;
    for (const ch of word) {
      if (!node.children[ch]) {
        node.children[ch] = new TrieNode();
      }
      node = node.children[ch];
    }
    node.isEnd = true;
  }

  search(word) {
    const node = this._findNode(word);
    return node !== null && node.isEnd;
  }

  startsWith(prefix) {
    return this._findNode(prefix) !== null;
  }

  _findNode(str) {
    let node = this.root;
    for (const ch of str) {
      if (!node.children[ch]) return null;
      node = node.children[ch];
    }
    return node;
  }
}
```

## 使用示例
javascript

```
const trie = new Trie();
trie.insert("apple");
trie.search("apple");    // true
trie.search("app");      // false
trie.startsWith("app");  // true
trie.insert("app");
trie.search("app");      // true
```

## Trie vs 哈希表

|  | Trie | 哈希表 |
| --- | --- | --- |
| 精确查找 | O(L) | O(L) 平均 |
| 前缀搜索 | O(L) | 不支持 |
| 空间 | 可能较大（每个字符一个节点） | 更紧凑 |
| 排序遍历 | 支持（DFS 遍历即字典序） | 不支持 |

## 复杂度

- 插入/查找/前缀搜索：O(L)，L 为字符串长度
- 空间：O(N × L × Σ)，N 为字符串数量，Σ 为字符集大小

## LeetCode 练习

- LC 208. 实现 Trie（前缀树）⭐
- LC 211. 添加与搜索单词
- LC 212. 单词搜索 II（Trie + 回溯）