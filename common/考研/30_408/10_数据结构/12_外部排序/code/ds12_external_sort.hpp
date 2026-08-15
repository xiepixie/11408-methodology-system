#ifndef IPARA_DS12_EXTERNAL_SORT_HPP
#define IPARA_DS12_EXTERNAL_SORT_HPP

#include <algorithm>
#include <cmath>
#include <cstddef>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

namespace ipara::ds12 {

inline std::vector<std::vector<int>> make_initial_runs(const std::vector<int>& values,
                                                        std::size_t memory_capacity) {
  if (memory_capacity == 0) throw std::invalid_argument("memory capacity must be positive");
  std::vector<std::vector<int>> runs;
  for (std::size_t begin = 0; begin < values.size(); begin += memory_capacity) {
    const std::size_t end = std::min(values.size(), begin + memory_capacity);
    runs.emplace_back(values.begin() + static_cast<std::ptrdiff_t>(begin),
                      values.begin() + static_cast<std::ptrdiff_t>(end));
    std::sort(runs.back().begin(), runs.back().end());
  }
  return runs;
}

inline std::vector<int> merge_sorted_runs(const std::vector<std::vector<int>>& runs) {
  struct Candidate { int value; std::size_t run; std::size_t index; };
  auto greater = [](const Candidate& left, const Candidate& right) {
    return left.value > right.value;
  };
  std::priority_queue<Candidate, std::vector<Candidate>, decltype(greater)> pending(greater);
  std::size_t total = 0;
  for (std::size_t run = 0; run < runs.size(); ++run) {
    total += runs[run].size();
    if (!runs[run].empty()) pending.push(Candidate{runs[run].front(), run, 0});
  }
  std::vector<int> output;
  output.reserve(total);
  while (!pending.empty()) {
    const Candidate current = pending.top();
    pending.pop();
    output.push_back(current.value);
    const std::size_t next = current.index + 1;
    if (next < runs[current.run].size()) {
      pending.push(Candidate{runs[current.run][next], current.run, next});
    }
  }
  return output;
}

inline std::size_t merge_passes(std::size_t run_count, std::size_t fan_in) {
  if (fan_in < 2) throw std::invalid_argument("fan-in must be at least two");
  std::size_t passes = 0;
  while (run_count > 1) {
    run_count = (run_count + fan_in - 1) / fan_in;
    ++passes;
  }
  return passes;
}

}  // namespace ipara::ds12

#endif
