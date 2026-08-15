#include "ds07_graph_traversal.hpp"

#include <cassert>
#include <stdexcept>
#include <vector>

using ipara::ds07::Graph;

int main() {
  Graph graph(6);
  graph.add_edge(0, 1); graph.add_edge(0, 2); graph.add_edge(1, 3);
  graph.add_edge(2, 4);
  assert(graph.has_edge(0, 1) && graph.has_edge(1, 0));
  assert(!graph.has_edge(0, 5));
  assert((graph.bfs(0) == std::vector<std::size_t>{0, 1, 2, 3, 4}));
  assert((graph.dfs(0) == std::vector<std::size_t>{0, 1, 3, 2, 4}));
  assert(graph.bfs(5).size() == 1);

  Graph diamond(4, true);
  diamond.add_edge(0, 1); diamond.add_edge(0, 2);
  diamond.add_edge(1, 3); diamond.add_edge(2, 3);
  assert((diamond.bfs(0) == std::vector<std::size_t>{0, 1, 2, 3}));
  assert((diamond.dfs(0) == std::vector<std::size_t>{0, 1, 3, 2}));

  Graph directed(2, true); directed.add_edge(0, 1);
  assert(directed.neighbors(1).empty());
  assert(directed.has_edge(0, 1) && !directed.has_edge(1, 0));
  bool threw = false; try { graph.add_edge(6, 0); } catch (const std::out_of_range&) { threw = true; }
  assert(threw);
}
