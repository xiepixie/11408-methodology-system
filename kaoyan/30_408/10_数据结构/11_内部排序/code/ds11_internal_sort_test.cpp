#include "ds11_internal_sort.hpp"

#include <cassert>
#include <vector>
#include <stdexcept>

int main() {
  const std::vector<int> input{4, 1, 3, 2, 2};
  for (auto sorter : {ipara::ds11::insertion_sort, ipara::ds11::selection_sort, ipara::ds11::merge_sort, ipara::ds11::quick_sort, ipara::ds11::heap_sort}) {
    auto values = input; sorter(values); assert((values == std::vector<int>{1, 2, 2, 3, 4}));
  }
  std::vector<int> empty; ipara::ds11::merge_sort(empty); assert(empty.empty());
  std::vector<int> sorted{1, 2, 3}; ipara::ds11::quick_sort(sorted); assert((sorted == std::vector<int>{1, 2, 3}));
  std::vector<int> nonnegative{170, 45, 75, 90, 802, 24, 2, 66}; ipara::ds11::radix_sort_nonnegative(nonnegative); assert((nonnegative == std::vector<int>{2, 24, 45, 66, 75, 90, 170, 802}));
  bool negative = false; std::vector<int> with_negative{1, -1}; try { ipara::ds11::radix_sort_nonnegative(with_negative); } catch (const std::invalid_argument&) { negative = true; } assert(negative);
}
