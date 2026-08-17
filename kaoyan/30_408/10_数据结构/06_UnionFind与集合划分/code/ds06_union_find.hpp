#ifndef IPARA_DS06_UNION_FIND_HPP
#define IPARA_DS06_UNION_FIND_HPP

#include <cstddef>
#include <stdexcept>
#include <vector>

namespace ipara::ds06 {

class UnionFind {
 public:
  explicit UnionFind(std::size_t count)
      : parent_(count), rank_(count, 0), components_(count) {
    for (std::size_t i = 0; i < count; ++i) {
      parent_[i] = i;
    }
  }

  std::size_t size() const { return parent_.size(); }
  std::size_t components() const { return components_; }

  std::size_t find(std::size_t value) {
    check(value);
    if (parent_[value] != value) {
      parent_[value] = find(parent_[value]);
    }
    return parent_[value];
  }

  bool connected(std::size_t left, std::size_t right) {
    return find(left) == find(right);
  }

  bool unite(std::size_t left, std::size_t right) {
    std::size_t root_left = find(left);
    std::size_t root_right = find(right);
    if (root_left == root_right) {
      return false;
    }
    if (rank_[root_left] < rank_[root_right]) {
      std::swap(root_left, root_right);
    }
    parent_[root_right] = root_left;
    if (rank_[root_left] == rank_[root_right]) {
      ++rank_[root_left];
    }
    --components_;
    return true;
  }

  bool invariant() const {
    if (components_ > parent_.size() || parent_.size() != rank_.size()) {
      return false;
    }
    std::size_t roots = 0;
    for (std::size_t i = 0; i < parent_.size(); ++i) {
      if (parent_[i] >= parent_.size() || rank_[i] > parent_.size()) {
        return false;
      }
      if (parent_[i] == i) {
        ++roots;
      }
    }
    return roots == components_;
  }

 private:
  void check(std::size_t value) const {
    if (value >= parent_.size()) {
      throw std::out_of_range("union-find element out of range");
    }
  }

  std::vector<std::size_t> parent_;
  std::vector<std::size_t> rank_;
  std::size_t components_ = 0;
};

}  // namespace ipara::ds06

#endif
