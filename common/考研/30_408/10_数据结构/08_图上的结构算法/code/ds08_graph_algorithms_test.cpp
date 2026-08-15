#include "ds08_graph_algorithms.hpp"

#include <cassert>
#include <stdexcept>
#include <vector>

using ipara::ds08::Distance;
using ipara::ds08::Edge;
using ipara::ds08::bellman_ford;
using ipara::ds08::critical_path;
using ipara::ds08::dijkstra;
using ipara::ds08::floyd_warshall;
using ipara::ds08::kInfinity;
using ipara::ds08::kruskal_weight;
using ipara::ds08::prim_weight;
using ipara::ds08::topological_order;

template <class Action>
void assert_invalid(Action action) {
  bool thrown = false;
  try {
    action();
  } catch (const std::invalid_argument&) {
    thrown = true;
  }
  assert(thrown);
}

void test_mst_algorithms_share_the_same_goal() {
  const std::vector<Edge> edges{{0, 1, 1}, {1, 2, 2}, {2, 3, 1}, {0, 3, 8}};
  assert(prim_weight(4, edges) == 4);
  assert(kruskal_weight(4, edges) == 4);
  assert_invalid([&] { (void)prim_weight(5, edges); });
  assert_invalid([&] { (void)kruskal_weight(5, edges); });
}

void test_shortest_path_algorithms_and_boundaries() {
  const std::vector<Edge> nonnegative{
      {0, 1, 4}, {0, 2, 1}, {2, 1, 2}, {1, 3, 1}, {2, 3, 5}};
  const std::vector<Distance> expected{0, 3, 1, 4, kInfinity};
  assert(dijkstra(5, nonnegative, 0) == expected);
  assert(bellman_ford(5, nonnegative, 0) == expected);

  const std::vector<Edge> with_negative{{0, 1, 4}, {1, 2, -3}, {0, 2, 5}};
  assert((bellman_ford(3, with_negative, 0) == std::vector<Distance>{0, 4, 1}));
  assert_invalid([&] { (void)dijkstra(3, with_negative, 0); });
  assert_invalid([&] { (void)bellman_ford(2, {{0, 1, -1}, {1, 0, -1}}, 0); });

  const auto all_pairs = floyd_warshall(4, nonnegative);
  assert(all_pairs[0][3] == 4);
  assert(all_pairs[3][0] == kInfinity);
  assert_invalid([&] { (void)floyd_warshall(2, {{0, 1, -1}, {1, 0, -1}}); });

  const std::vector<Edge> large_weights{{0, 1, 2'000'000'000}, {1, 2, 2'000'000'000}};
  assert(dijkstra(3, large_weights, 0)[2] == 4'000'000'000LL);
}

void test_topology_and_critical_path() {
  const std::vector<Edge> activities{
      {0, 1, 3}, {0, 2, 2}, {1, 3, 4}, {2, 3, 3}, {2, 4, 2}, {3, 5, 2}, {4, 5, 3}};
  const auto order = topological_order(6, activities);
  assert(order.front() == 0 && order.back() == 5);

  const auto result = critical_path(6, activities);
  assert(result.duration == 9);
  assert((result.earliest_event == std::vector<Distance>{0, 3, 2, 7, 4, 9}));
  assert((result.latest_event == std::vector<Distance>{0, 3, 4, 7, 6, 9}));
  assert((result.critical_edge_indices == std::vector<std::size_t>{0, 2, 5}));

  assert_invalid([&] { (void)topological_order(2, {{0, 1, 1}, {1, 0, 1}}); });
  assert_invalid([&] { (void)critical_path(2, {{0, 1, -1}}); });
}

int main() {
  test_mst_algorithms_share_the_same_goal();
  test_shortest_path_algorithms_and_boundaries();
  test_topology_and_critical_path();
}
