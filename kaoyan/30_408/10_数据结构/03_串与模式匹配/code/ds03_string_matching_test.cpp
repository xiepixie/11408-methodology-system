#include "ds03_string_matching.hpp"

#include <cassert>
#include <string>
#include <string_view>
#include <vector>

using ipara::ds03::kmp_search;
using ipara::ds03::naive_search;
using ipara::ds03::prefix_function;

void test_empty_and_boundary_patterns() {
  assert(naive_search("abc", "") == 0);
  assert(kmp_search("abc", "") == 0);
  assert(naive_search("abc", "abcd") == std::string_view::npos);
  assert(kmp_search("abc", "abcd") == std::string_view::npos);
  assert(naive_search("", "a") == std::string_view::npos);
  assert(kmp_search("", "a") == std::string_view::npos);
}

void test_naive_and_kmp_agree() {
  const std::vector<std::pair<std::string_view, std::string_view>> cases = {
      {"abcabcabcd", "abcabcd"}, {"aaaaab", "aaab"}, {"mississippi", "issi"},
      {"abcdef", "gh"}, {"abababab", "ababa"}};
  for (const auto& [text, pattern] : cases) {
    assert(naive_search(text, pattern) == kmp_search(text, pattern));
  }
}

void test_prefix_reuse_information() {
  assert((prefix_function("ababaca") == std::vector<int>{0, 0, 1, 2, 3, 0, 1}));
  assert((prefix_function("aaaa") == std::vector<int>{0, 1, 2, 3}));
  assert((prefix_function("aabaaab") == std::vector<int>{0, 1, 0, 1, 2, 2, 3}));
}

void test_repeated_mismatch_does_not_lose_text_progress() {
  assert(kmp_search("ababababca", "abababca") == 2);
  assert(kmp_search("aaaaaaaaab", "aaab") == 6);
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
      assert(kmp_search(text, pattern) == naive_search(text, pattern));
    }
  }
}

int main() {
  test_empty_and_boundary_patterns();
  test_naive_and_kmp_agree();
  test_prefix_reuse_information();
  test_repeated_mismatch_does_not_lose_text_progress();
  test_exhaustive_agreement_on_short_binary_strings();
}
