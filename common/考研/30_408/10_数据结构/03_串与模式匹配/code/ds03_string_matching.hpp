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

inline std::vector<int> prefix_function(std::string_view pattern) {
  std::vector<int> prefix(pattern.size(), 0);
  for (std::size_t i = 1; i < pattern.size(); ++i) {
    int border = prefix[i - 1];
    while (border > 0 && pattern[i] != pattern[static_cast<std::size_t>(border)]) {
      border = prefix[static_cast<std::size_t>(border) - 1];
    }
    if (pattern[i] == pattern[static_cast<std::size_t>(border)]) {
      ++border;
    }
    prefix[i] = border;
  }
  return prefix;
}

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

}  // namespace ipara::ds03

#endif
