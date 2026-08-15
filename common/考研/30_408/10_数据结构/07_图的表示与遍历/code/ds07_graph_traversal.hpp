#ifndef IPARA_DS07_GRAPH_TRAVERSAL_HPP
#define IPARA_DS07_GRAPH_TRAVERSAL_HPP

#include <cstddef>
#include <queue>
#include <stack>
#include <stdexcept>
#include <vector>

namespace ipara::ds07 {

class Graph {
 public:
  explicit Graph(std::size_t vertices, bool directed = false)
      : adjacency_(vertices), matrix_(vertices, std::vector<bool>(vertices, false)), directed_(directed) {}
  std::size_t size() const { return adjacency_.size(); }
  void add_edge(std::size_t from, std::size_t to) {
    check(from); check(to);
    adjacency_[from].push_back(to);
    matrix_[from][to] = true;
    if (!directed_) adjacency_[to].push_back(from);
    if (!directed_) matrix_[to][from] = true;
  }
  const std::vector<std::size_t>& neighbors(std::size_t vertex) const {
    check(vertex); return adjacency_[vertex];
  }
  bool has_edge(std::size_t from, std::size_t to) const {
    check(from); check(to); return matrix_[from][to];
  }
  std::vector<std::size_t> bfs(std::size_t start) const {
    check(start); std::vector<bool> seen(size()); std::vector<std::size_t> order;
    std::queue<std::size_t> frontier; frontier.push(start); seen[start] = true;
    while (!frontier.empty()) {
      auto vertex = frontier.front(); frontier.pop(); order.push_back(vertex);
      for (auto next : adjacency_[vertex]) if (!seen[next]) { seen[next] = true; frontier.push(next); }
    }
    return order;
  }
  std::vector<std::size_t> dfs(std::size_t start) const {
    check(start); std::vector<bool> seen(size()); std::vector<std::size_t> order;
    std::stack<std::size_t> frontier; frontier.push(start); seen[start] = true;
    while (!frontier.empty()) {
      auto vertex = frontier.top(); frontier.pop();
      order.push_back(vertex);
      for (auto it = adjacency_[vertex].rbegin(); it != adjacency_[vertex].rend(); ++it) {
        if (!seen[*it]) {
          seen[*it] = true;
          frontier.push(*it);
        }
      }
    }
    return order;
  }

 private:
  std::vector<std::vector<std::size_t>> adjacency_;
  std::vector<std::vector<bool>> matrix_;
  bool directed_;
  void check(std::size_t vertex) const {
    if (vertex >= size()) throw std::out_of_range("graph vertex");
  }
};

}  // namespace ipara::ds07

#endif
