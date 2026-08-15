#ifndef IPARA_DS05_HEAP_HPP
#define IPARA_DS05_HEAP_HPP

#include <stdexcept>
#include <utility>
#include <vector>

namespace ipara::ds05 {

class MinHeap {
 public:
  MinHeap() = default;
  explicit MinHeap(std::vector<int> values) : data_(std::move(values)) {
    build();
  }

  bool empty() const { return data_.empty(); }
  std::size_t size() const { return data_.size(); }
  int top() const {
    if (empty()) throw std::out_of_range("top on empty heap");
    return data_.front();
  }
  void push(int value) {
    data_.push_back(value);
    sift_up(data_.size() - 1);
  }
  int pop() {
    const int result = top();
    data_.front() = data_.back();
    data_.pop_back();
    if (!empty()) sift_down(0);
    return result;
  }
  bool invariant() const {
    for (std::size_t i = 1; i < data_.size(); ++i) {
      if (data_[parent(i)] > data_[i]) return false;
    }
    return true;
  }

 private:
  std::vector<int> data_;
  static std::size_t parent(std::size_t i) { return (i - 1) / 2; }
  static std::size_t left(std::size_t i) { return 2 * i + 1; }

  void sift_up(std::size_t i) {
    while (i > 0 && data_[parent(i)] > data_[i]) {
      std::swap(data_[parent(i)], data_[i]);
      i = parent(i);
    }
  }
  void sift_down(std::size_t i) {
    while (left(i) < data_.size()) {
      std::size_t child = left(i);
      if (child + 1 < data_.size() && data_[child + 1] < data_[child]) ++child;
      if (data_[i] <= data_[child]) break;
      std::swap(data_[i], data_[child]);
      i = child;
    }
  }
  void build() {
    if (data_.empty()) return;
    for (std::size_t i = data_.size() / 2; i-- > 0;) sift_down(i);
  }
};

}  // namespace ipara::ds05

#endif
