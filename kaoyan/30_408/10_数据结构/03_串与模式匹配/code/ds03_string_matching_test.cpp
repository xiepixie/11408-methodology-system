#include "ds03_string_matching.hpp"

#include <cassert>
#include <string>
#include <string_view>
#include <vector>

using ipara::ds03::kmp_search;
using ipara::ds03::kmp_search_nextval_sentinel;
using ipara::ds03::kmp_search_sentinel;
using ipara::ds03::naive_search;
using ipara::ds03::next_sentinel;
using ipara::ds03::nextval_sentinel;
using ipara::ds03::prefix_function;

void test_empty_and_boundary_patterns() {
  assert(naive_search("abc", "") == 0);
  assert(kmp_search("abc", "") == 0);
  assert(kmp_search_sentinel("abc", "") == 0);
  assert(kmp_search_nextval_sentinel("abc", "") == 0);
  assert(naive_search("abc", "abcd") == std::string_view::npos);
  assert(kmp_search("abc", "abcd") == std::string_view::npos);
  assert(kmp_search_sentinel("abc", "abcd") == std::string_view::npos);
  assert(kmp_search_nextval_sentinel("abc", "abcd") == std::string_view::npos);
  assert(naive_search("", "a") == std::string_view::npos);
  assert(kmp_search("", "a") == std::string_view::npos);
  assert(kmp_search_sentinel("", "a") == std::string_view::npos);
  assert(kmp_search_nextval_sentinel("", "a") == std::string_view::npos);
}

void test_naive_and_kmp_agree() {
  const std::vector<std::pair<std::string_view, std::string_view>> cases = {
      {"abcabcabcd", "abcabcd"}, {"aaaaab", "aaab"}, {"mississippi", "issi"},
      {"abcdef", "gh"}, {"abababab", "ababa"}};
  for (const auto& [text, pattern] : cases) {
    const std::size_t expected = naive_search(text, pattern);
    assert(expected == kmp_search(text, pattern));
    assert(expected == kmp_search_sentinel(text, pattern));
    assert(expected == kmp_search_nextval_sentinel(text, pattern));
  }
}

void test_prefix_reuse_information() {
  assert((prefix_function("ababaca") == std::vector<int>{0, 0, 1, 2, 3, 0, 1}));
  assert((prefix_function("aaaa") == std::vector<int>{0, 1, 2, 3}));
  assert((prefix_function("aabaaab") == std::vector<int>{0, 1, 0, 1, 2, 2, 3}));
}

void test_408_next_and_nextval_encodings() {
  assert((next_sentinel("aabaaab") == std::vector<int>{-1, 0, 1, 0, 1, 2, 2}));
  assert((nextval_sentinel("aabaaab") == std::vector<int>{-1, -1, 1, -1, -1, 2, 1}));

  assert((next_sentinel("aabaab") == std::vector<int>{-1, 0, 1, 0, 1, 2}));
  assert((nextval_sentinel("aabaab") == std::vector<int>{-1, -1, 1, -1, -1, 1}));

  assert((next_sentinel("ababaaababaa") ==
          std::vector<int>{-1, 0, 0, 1, 2, 3, 1, 1, 2, 3, 4, 5}));
  assert((nextval_sentinel("ababaaababaa") ==
          std::vector<int>{-1, 0, -1, 0, -1, 3, 1, 0, -1, 0, -1, 3}));
}

void test_repeated_mismatch_does_not_lose_text_progress() {
  assert(kmp_search("ababababca", "abababca") == 2);
  assert(kmp_search("aaaaaaaaab", "aaab") == 6);
}

std::size_t count_sentinel_comparisons(std::string_view text,
                                       std::string_view pattern,
                                       bool use_nextval) {
  if (pattern.empty()) return 0;
  const std::vector<int> failure =
      use_nextval ? nextval_sentinel(pattern) : next_sentinel(pattern);

  std::size_t i = 0;
  std::ptrdiff_t j = 0;
  std::size_t comparisons = 0;
  const std::ptrdiff_t m = static_cast<std::ptrdiff_t>(pattern.size());

  while (i < text.size() && j < m) {
    if (j == -1) {
      ++i;
      ++j;
      continue;
    }

    ++comparisons;
    if (text[i] == pattern[static_cast<std::size_t>(j)]) {
      ++i;
      ++j;
    } else {
      j = failure[static_cast<std::size_t>(j)];
    }
  }
  return comparisons;
}

void test_comparison_count_and_nextval_optimization() {
  assert(count_sentinel_comparisons("abaabaabcabaabc", "abaabc", false) == 10);

  const std::size_t next_count =
      count_sentinel_comparisons("aaaacaaaaab", "aaaaab", false);
  const std::size_t nextval_count =
      count_sentinel_comparisons("aaaacaaaaab", "aaaaab", true);
  assert(next_count == 15);
  assert(nextval_count == 11);
  assert(nextval_count < next_count);
}

std::vector<std::string> binary_strings(std::size_t maximum_length) {
  std::vector<std::string> strings{""};
  for (std::size_t length = 1; length <= maximum_length; ++length) {
    const std::size_t count = std::size_t{1} << length;
    for (std::size_t mask = 0; mask < count; ++mask) {
      std::string value(length, 'a');
      for (std::size_t bit = 0; bit < length; ++bit) {
        if ((mask & (std::size_t{1} << bit)) != 0) value[bit] = 'b';
      }
      strings.push_back(value);
    }
  }
  return strings;
}

void test_exhaustive_agreement_on_short_binary_strings() {
  const auto texts = binary_strings(6);
  const auto patterns = binary_strings(4);
  for (const std::string& text : texts) {
    for (const std::string& pattern : patterns) {
      const std::size_t expected = naive_search(text, pattern);
      assert(kmp_search(text, pattern) == expected);
      assert(kmp_search_sentinel(text, pattern) == expected);
      assert(kmp_search_nextval_sentinel(text, pattern) == expected);
    }
  }
}

int main() {
  test_empty_and_boundary_patterns();
  test_naive_and_kmp_agree();
  test_prefix_reuse_information();
  test_408_next_and_nextval_encodings();
  test_repeated_mismatch_does_not_lose_text_progress();
  test_comparison_count_and_nextval_optimization();
  test_exhaustive_agreement_on_short_binary_strings();
}
