#include "ds12_external_sort.hpp"

#include <cassert>
#include <stdexcept>
#include <vector>

using ipara::ds12::make_initial_runs;
using ipara::ds12::merge_passes;
using ipara::ds12::merge_sorted_runs;

int main() {
  const std::vector<int> input{9, 1, 7, 3, 5, 2, 8, 4, 6};
  const auto runs = make_initial_runs(input, 3);
  assert((runs == std::vector<std::vector<int>>{{1, 7, 9}, {2, 3, 5}, {4, 6, 8}}));
  assert((merge_sorted_runs(runs) == std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9}));
  assert((merge_sorted_runs({{}, {1, 4}, {}, {2, 3}}) == std::vector<int>{1, 2, 3, 4}));
  assert(merge_passes(1, 2) == 0);
  assert(merge_passes(10, 3) == 3);
  bool capacity_error = false;
  try { (void)make_initial_runs(input, 0); } catch (const std::invalid_argument&) { capacity_error = true; }
  assert(capacity_error);
  bool fan_in_error = false;
  try { (void)merge_passes(2, 1); } catch (const std::invalid_argument&) { fan_in_error = true; }
  assert(fan_in_error);
}
