#ifndef IPARA_DS03_STRING_MATCHING_HPP
#define IPARA_DS03_STRING_MATCHING_HPP

#include <cstddef>
#include <string_view>
#include <vector>

namespace ipara::ds03 {

inline std::size_t naive_search(std::string_view text, std::string_view pattern) {
  if (pattern.empty()) {
    return 0;
  }
  if (pattern.size() > text.size()) {
    return std::string_view::npos;
  }
  for (std::size_t start = 0; start + pattern.size() <= text.size(); ++start) {
    std::size_t matched = 0;
    while (matched < pattern.size() && text[start + matched] == pattern[matched]) {
      ++matched;
    }
    if (matched == pattern.size()) {
      return start;
    }
  }
  return std::string_view::npos;
}

// pattern 是模式串。
// prefix[pos] 保存 pattern[0..pos] 的最长相等真前后缀长度。
inline std::vector<int> prefix_function(std::string_view pattern) {
  std::vector<int> prefix(pattern.size(), 0);
  for (std::size_t pos = 1; pos < pattern.size(); ++pos) {
    int border = prefix[pos - 1];  // 先尝试延长前一个位置的最长边界。
    while (border > 0 &&
           pattern[pos] != pattern[static_cast<std::size_t>(border)]) {
      // 当前候选无法延长，改试“当前边界自己的最长边界”。
      border = prefix[static_cast<std::size_t>(border) - 1];
    }
    if (pattern[pos] == pattern[static_cast<std::size_t>(border)]) {
      ++border;
    }
    prefix[pos] = border;
  }
  return prefix;
}

// text 是主串，pattern 是模式串。
// matched 表示当前已经匹配成功的模式字符数。
inline std::size_t kmp_search(std::string_view text, std::string_view pattern) {
  if (pattern.empty()) {
    return 0;
  }
  const std::vector<int> prefix = prefix_function(pattern);
  std::size_t matched = 0;
  for (std::size_t i = 0; i < text.size(); ++i) {
    while (matched > 0 && text[i] != pattern[matched]) {
      matched = static_cast<std::size_t>(prefix[matched - 1]);
    }
    if (text[i] == pattern[matched]) {
      ++matched;
    }
    if (matched == pattern.size()) {
      return i + 1 - pattern.size();
    }
  }
  return std::string_view::npos;
}

// 408 常见的零起始下标 + -1 哨兵编码：
// next[0] = -1，next[j] = prefix[j - 1] (j > 0)。
inline std::vector<int> next_sentinel(std::string_view pattern) {
  if (pattern.empty()) {
    return {};
  }
  const std::vector<int> prefix = prefix_function(pattern);
  std::vector<int> next(pattern.size(), -1);
  for (std::size_t j = 1; j < pattern.size(); ++j) {
    // pattern[j] 失配时，真正已经匹配完成的是 pattern[0..j-1]。
    // 所以下一状态取这个已匹配部分的最长边界长度。
    next[j] = prefix[j - 1];
  }
  return next;
}

// nextval 只优化“下一次要比较哪个模式状态”的编码；
// 它不改变前缀函数所描述的最长边界结构。
inline std::vector<int> nextval_sentinel(std::string_view pattern) {
  if (pattern.empty()) {
    return {};
  }
  const std::vector<int> next = next_sentinel(pattern);
  std::vector<int> nextval(pattern.size(), -1);
  for (std::size_t j = 1; j < pattern.size(); ++j) {
    const int fallback = next[j];  // 本约定下 j > 0 时必有 fallback >= 0。
    const std::size_t k = static_cast<std::size_t>(fallback);
    if (pattern[j] == pattern[k]) {
      // 当前字符和回退后的字符相同：若当前比较失败，回退后必然再次失败。
      nextval[j] = nextval[k];
    } else {
      // 回退后的字符不同，仍可能和当前主串字符匹配，保留这个状态。
      nextval[j] = fallback;
    }
  }
  return nextval;
}

// 与 408 手算完全同构的教材版 KMP：
// i 指向当前文本字符，j 指向当前模式字符；普通失配只修改 j。
inline std::size_t kmp_search_sentinel(std::string_view text, std::string_view pattern) {
  if (pattern.empty()) {
    return 0;
  }

  const std::vector<int> next = next_sentinel(pattern);
  std::size_t i = 0;    // 当前准备比较的主串 text 下标
  std::ptrdiff_t j = 0; // 当前准备比较的模式串 pattern 下标
  const std::ptrdiff_t m = static_cast<std::ptrdiff_t>(pattern.size());

  while (i < text.size() && j < m) {
    if (j == -1 || text[i] == pattern[static_cast<std::size_t>(j)]) {
      // j == -1：当前主串字符没有可继续尝试的模式状态；
      // 字符相等：当前比较已经成功。
      // 两种情况都会消费当前 text[i]，因此 i 和 j 同时前进。
      ++i;
      ++j;
    } else {
      // 普通失配只缩短模式状态；当前 text[i] 仍要继续参与比较。
      j = next[static_cast<std::size_t>(j)];
    }
  }

  return (j == m) ? (i - pattern.size()) : std::string_view::npos;
}

inline std::size_t kmp_search_nextval_sentinel(std::string_view text,
                                                std::string_view pattern) {
  if (pattern.empty()) {
    return 0;
  }

  const std::vector<int> nextval = nextval_sentinel(pattern);
  std::size_t i = 0;
  std::ptrdiff_t j = 0;
  const std::ptrdiff_t m = static_cast<std::ptrdiff_t>(pattern.size());

  while (i < text.size() && j < m) {
    if (j == -1 || text[i] == pattern[static_cast<std::size_t>(j)]) {
      ++i;
      ++j;
    } else {
      // 与普通 next 版唯一的差别：直接跳过字符相同、已知必败的状态。
      j = nextval[static_cast<std::size_t>(j)];
    }
  }

  return (j == m) ? (i - pattern.size()) : std::string_view::npos;
}

}  // namespace ipara::ds03

#endif
