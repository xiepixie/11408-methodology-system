#ifndef IPARA_DS08_GRAPH_ALGORITHMS_HPP
#define IPARA_DS08_GRAPH_ALGORITHMS_HPP

#include "../../06_UnionFind与集合划分/code/ds06_union_find.hpp"

#include <algorithm>
#include <cstddef>
#include <functional>
#include <limits>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

namespace ipara::ds08 {

using Distance = long long;
inline constexpr Distance kInfinity = std::numeric_limits<Distance>::max() / 4;

struct Edge {
  std::size_t from;
  std::size_t to;
  int weight;
};

inline void check_edge(std::size_t vertex_count, const Edge& edge) {
  if (edge.from >= vertex_count || edge.to >= vertex_count) {
    throw std::out_of_range("graph edge endpoint out of range");
  }
}

inline Distance prim_weight(std::size_t vertex_count, const std::vector<Edge>& edges) {
  if (vertex_count == 0) {
    return 0;
  }
  std::vector<std::vector<std::pair<std::size_t, int>>> graph(vertex_count);
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
    graph[edge.from].push_back({edge.to, edge.weight});
    graph[edge.to].push_back({edge.from, edge.weight});
  }

  std::vector<Distance> best_crossing_edge(vertex_count, kInfinity);
  std::vector<bool> fixed(vertex_count, false);
  best_crossing_edge[0] = 0;
  Distance total = 0;
  for (std::size_t step = 0; step < vertex_count; ++step) {
    std::size_t chosen = vertex_count;
    for (std::size_t vertex = 0; vertex < vertex_count; ++vertex) {
      if (!fixed[vertex] &&
          (chosen == vertex_count || best_crossing_edge[vertex] < best_crossing_edge[chosen])) {
        chosen = vertex;
      }
    }
    if (chosen == vertex_count || best_crossing_edge[chosen] == kInfinity) {
      throw std::invalid_argument("graph is disconnected");
    }
    fixed[chosen] = true;
    total += best_crossing_edge[chosen];
    for (const auto [next, weight] : graph[chosen]) {
      if (!fixed[next] && weight < best_crossing_edge[next]) {
        best_crossing_edge[next] = weight;
      }
    }
  }
  return total;
}

inline Distance kruskal_weight(std::size_t vertex_count, std::vector<Edge> edges) {
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
  }
  std::sort(edges.begin(), edges.end(),
            [](const Edge& left, const Edge& right) { return left.weight < right.weight; });
  ds06::UnionFind components(vertex_count);
  Distance total = 0;
  std::size_t chosen_edges = 0;
  for (const Edge& edge : edges) {
    if (components.unite(edge.from, edge.to)) {
      total += edge.weight;
      ++chosen_edges;
      if (chosen_edges + 1 == vertex_count) {
        break;
      }
    }
  }
  if (vertex_count > 0 && chosen_edges + 1 != vertex_count) {
    throw std::invalid_argument("graph is disconnected");
  }
  return total;
}

inline std::vector<Distance> dijkstra(std::size_t vertex_count,
                                      const std::vector<Edge>& edges,
                                      std::size_t source) {
  if (source >= vertex_count) {
    throw std::out_of_range("source vertex out of range");
  }
  std::vector<std::vector<std::pair<std::size_t, int>>> graph(vertex_count);
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
    if (edge.weight < 0) {
      throw std::invalid_argument("dijkstra requires nonnegative edges");
    }
    graph[edge.from].push_back({edge.to, edge.weight});
  }

  using Candidate = std::pair<Distance, std::size_t>;
  std::priority_queue<Candidate, std::vector<Candidate>, std::greater<Candidate>> pending;
  std::vector<Distance> distance(vertex_count, kInfinity);
  distance[source] = 0;
  pending.push({0, source});
  while (!pending.empty()) {
    const auto [current_distance, current] = pending.top();
    pending.pop();
    if (current_distance != distance[current]) {
      continue;
    }
    for (const auto [next, weight] : graph[current]) {
      const Distance candidate = current_distance + static_cast<Distance>(weight);
      if (candidate < distance[next]) {
        distance[next] = candidate;
        pending.push({candidate, next});
      }
    }
  }
  return distance;
}

inline std::vector<Distance> bellman_ford(std::size_t vertex_count,
                                          const std::vector<Edge>& edges,
                                          std::size_t source) {
  if (source >= vertex_count) {
    throw std::out_of_range("source vertex out of range");
  }
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
  }
  std::vector<Distance> distance(vertex_count, kInfinity);
  distance[source] = 0;
  for (std::size_t round = 1; round < vertex_count; ++round) {
    bool changed = false;
    for (const Edge& edge : edges) {
      if (distance[edge.from] == kInfinity) {
        continue;
      }
      const Distance candidate = distance[edge.from] + static_cast<Distance>(edge.weight);
      if (candidate < distance[edge.to]) {
        distance[edge.to] = candidate;
        changed = true;
      }
    }
    if (!changed) {
      break;
    }
  }
  for (const Edge& edge : edges) {
    if (distance[edge.from] != kInfinity &&
        distance[edge.from] + static_cast<Distance>(edge.weight) < distance[edge.to]) {
      throw std::invalid_argument("reachable negative cycle");
    }
  }
  return distance;
}

inline std::vector<std::vector<Distance>> floyd_warshall(
    std::size_t vertex_count, const std::vector<Edge>& edges) {
  std::vector<std::vector<Distance>> distance(
      vertex_count, std::vector<Distance>(vertex_count, kInfinity));
  for (std::size_t vertex = 0; vertex < vertex_count; ++vertex) {
    distance[vertex][vertex] = 0;
  }
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
    distance[edge.from][edge.to] =
        std::min(distance[edge.from][edge.to], static_cast<Distance>(edge.weight));
  }
  for (std::size_t middle = 0; middle < vertex_count; ++middle) {
    for (std::size_t from = 0; from < vertex_count; ++from) {
      if (distance[from][middle] == kInfinity) {
        continue;
      }
      for (std::size_t to = 0; to < vertex_count; ++to) {
        if (distance[middle][to] == kInfinity) {
          continue;
        }
        distance[from][to] = std::min(
            distance[from][to], distance[from][middle] + distance[middle][to]);
      }
    }
  }
  for (std::size_t vertex = 0; vertex < vertex_count; ++vertex) {
    if (distance[vertex][vertex] < 0) {
      throw std::invalid_argument("graph contains a negative cycle");
    }
  }
  return distance;
}

inline std::vector<std::size_t> topological_order(
    std::size_t vertex_count, const std::vector<Edge>& edges) {
  std::vector<std::vector<std::size_t>> graph(vertex_count);
  std::vector<std::size_t> indegree(vertex_count, 0);
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
    graph[edge.from].push_back(edge.to);
    ++indegree[edge.to];
  }
  std::queue<std::size_t> ready;
  for (std::size_t vertex = 0; vertex < vertex_count; ++vertex) {
    if (indegree[vertex] == 0) {
      ready.push(vertex);
    }
  }
  std::vector<std::size_t> order;
  while (!ready.empty()) {
    const std::size_t current = ready.front();
    ready.pop();
    order.push_back(current);
    for (const std::size_t next : graph[current]) {
      if (--indegree[next] == 0) {
        ready.push(next);
      }
    }
  }
  if (order.size() != vertex_count) {
    throw std::invalid_argument("directed graph contains a cycle");
  }
  return order;
}

struct CriticalPathResult {
  Distance duration = 0;
  std::vector<Distance> earliest_event;
  std::vector<Distance> latest_event;
  std::vector<std::size_t> critical_edge_indices;
};

inline CriticalPathResult critical_path(std::size_t vertex_count,
                                        const std::vector<Edge>& edges) {
  for (const Edge& edge : edges) {
    check_edge(vertex_count, edge);
    if (edge.weight < 0) {
      throw std::invalid_argument("activity duration must be nonnegative");
    }
  }
  const std::vector<std::size_t> order = topological_order(vertex_count, edges);
  CriticalPathResult result;
  result.earliest_event.assign(vertex_count, 0);
  for (const std::size_t current : order) {
    for (const Edge& edge : edges) {
      if (edge.from == current) {
        result.earliest_event[edge.to] =
            std::max(result.earliest_event[edge.to],
                     result.earliest_event[current] + edge.weight);
      }
    }
  }
  for (const Distance time : result.earliest_event) {
    result.duration = std::max(result.duration, time);
  }
  result.latest_event.assign(vertex_count, result.duration);
  for (auto current = order.rbegin(); current != order.rend(); ++current) {
    for (const Edge& edge : edges) {
      if (edge.from == *current) {
        result.latest_event[edge.from] =
            std::min(result.latest_event[edge.from],
                     result.latest_event[edge.to] - edge.weight);
      }
    }
  }
  for (std::size_t index = 0; index < edges.size(); ++index) {
    const Edge& edge = edges[index];
    const Distance earliest_start = result.earliest_event[edge.from];
    const Distance latest_start = result.latest_event[edge.to] - edge.weight;
    if (earliest_start == latest_start) {
      result.critical_edge_indices.push_back(index);
    }
  }
  return result;
}

}  // namespace ipara::ds08

#endif
