#ifndef IPARA_DS11_INTERNAL_SORT_HPP
#define IPARA_DS11_INTERNAL_SORT_HPP

#include <cstddef>
#include <algorithm>
#include <stdexcept>
#include <vector>

namespace ipara::ds11 {

inline void insertion_sort(std::vector<int>& values) {
  for (std::size_t i = 1; i < values.size(); ++i) {
    int value = values[i]; std::size_t j = i;
    while (j > 0 && values[j - 1] > value) { values[j] = values[j - 1]; --j; }
    values[j] = value;
  }
}

inline void selection_sort(std::vector<int>& values) {
  for (std::size_t i = 0; i < values.size(); ++i) {
    std::size_t minimum = i;
    for (std::size_t j = i + 1; j < values.size(); ++j) if (values[j] < values[minimum]) minimum = j;
    std::swap(values[i], values[minimum]);
  }
}

inline void merge(std::vector<int>& values, std::vector<int>& buffer, std::size_t left, std::size_t mid, std::size_t right) {
  std::size_t i = left, j = mid, k = left;
  while (i < mid && j < right) buffer[k++] = values[i] <= values[j] ? values[i++] : values[j++];
  while (i < mid) buffer[k++] = values[i++];
  while (j < right) buffer[k++] = values[j++];
  for (k = left; k < right; ++k) values[k] = buffer[k];
}
inline void merge_sort_impl(std::vector<int>& values, std::vector<int>& buffer, std::size_t left, std::size_t right) {
  if (right - left < 2) return;
  const auto mid = left + (right - left) / 2;
  merge_sort_impl(values, buffer, left, mid); merge_sort_impl(values, buffer, mid, right); merge(values, buffer, left, mid, right);
}
inline void merge_sort(std::vector<int>& values) { std::vector<int> buffer(values.size()); merge_sort_impl(values, buffer, 0, values.size()); }

inline std::size_t partition(std::vector<int>& values, std::size_t left, std::size_t right) {
  const int pivot = values[right - 1]; std::size_t store = left;
  for (std::size_t i = left; i + 1 < right; ++i) if (values[i] < pivot) { std::swap(values[i], values[store]); ++store; }
  std::swap(values[store], values[right - 1]); return store;
}
inline void quick_sort_impl(std::vector<int>& values, std::size_t left, std::size_t right) {
  if (right - left < 2) return;
  const auto pivot = partition(values, left, right); quick_sort_impl(values, left, pivot); quick_sort_impl(values, pivot + 1, right);
}
inline void quick_sort(std::vector<int>& values) { quick_sort_impl(values, 0, values.size()); }

inline void heap_sort(std::vector<int>& values) {
  auto sift_down = [&values](std::size_t start, std::size_t end) {
    std::size_t root = start;
    while (2 * root + 1 < end) {
      std::size_t child = 2 * root + 1;
      if (child + 1 < end && values[child] < values[child + 1]) ++child;
      if (values[root] >= values[child]) break;
      std::swap(values[root], values[child]); root = child;
    }
  };
  for (std::size_t start = values.size() / 2; start > 0; --start) sift_down(start - 1, values.size());
  for (std::size_t end = values.size(); end > 1; --end) { std::swap(values[0], values[end - 1]); sift_down(0, end - 1); }
}

inline void radix_sort_nonnegative(std::vector<int>& values) {
  if (std::any_of(values.begin(), values.end(), [](int value) { return value < 0; })) throw std::invalid_argument("radix sort requires nonnegative keys");
  int maximum = 0; for (const int value : values) maximum = std::max(maximum, value);
  std::vector<int> buffer(values.size());
  for (int place = 1; maximum / place > 0; place *= 10) {
    std::vector<std::size_t> count(10, 0);
    for (const int value : values) ++count[static_cast<std::size_t>((value / place) % 10)];
    for (std::size_t digit = 1; digit < 10; ++digit) count[digit] += count[digit - 1];
    for (std::size_t i = values.size(); i > 0; --i) { const int value = values[i - 1]; const std::size_t digit = static_cast<std::size_t>((value / place) % 10); buffer[--count[digit]] = value; }
    values.swap(buffer);
    if (place > maximum / 10) break;
  }
}
}  // namespace ipara::ds11

#endif
