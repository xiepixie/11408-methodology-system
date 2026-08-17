#ifndef IPARA_DS01_LINEAR_LIST_HPP
#define IPARA_DS01_LINEAR_LIST_HPP

#include <algorithm>
#include <cstddef>
#include <memory>
#include <optional>
#include <stdexcept>
#include <vector>

namespace ipara::ds01 {

class SequentialList {
 public:
  explicit SequentialList(std::size_t initial_capacity = 1)
      : data_(std::make_unique<int[]>(std::max<std::size_t>(1, initial_capacity))),
        length_(0),
        capacity_(std::max<std::size_t>(1, initial_capacity)) {}

  std::size_t size() const { return length_; }
  std::size_t capacity() const { return capacity_; }
  bool empty() const { return length_ == 0; }

  int at(std::size_t index) const {
    require_index(index);
    return data_[index];
  }

  void insert(std::size_t index, int value) {
    if (index > length_) {
      throw std::out_of_range("insert position is outside [0, length]");
    }

    ensure_capacity(length_ + 1);
    for (std::size_t i = length_; i > index; --i) {
      data_[i] = data_[i - 1];
    }
    data_[index] = value;
    ++length_;
  }

  int erase(std::size_t index) {
    require_index(index);
    const int removed = data_[index];
    for (std::size_t i = index; i + 1 < length_; ++i) {
      data_[i] = data_[i + 1];
    }
    --length_;
    return removed;
  }

  std::optional<std::size_t> find_first(int value) const {
    for (std::size_t i = 0; i < length_; ++i) {
      if (data_[i] == value) {
        return i;
      }
    }
    return std::nullopt;
  }

  bool invariant() const {
    return data_ != nullptr && capacity_ >= 1 && length_ <= capacity_;
  }

  std::vector<int> values() const {
    return std::vector<int>(data_.get(), data_.get() + length_);
  }

 private:
  void require_index(std::size_t index) const {
    if (index >= length_) {
      throw std::out_of_range("index is outside [0, length)");
    }
  }

  void ensure_capacity(std::size_t required) {
    if (required <= capacity_) {
      return;
    }

    std::size_t new_capacity = capacity_;
    while (new_capacity < required) {
      new_capacity *= 2;
    }

    auto replacement = std::make_unique<int[]>(new_capacity);
    std::copy_n(data_.get(), length_, replacement.get());
    data_ = std::move(replacement);
    capacity_ = new_capacity;
  }

  std::unique_ptr<int[]> data_;
  std::size_t length_;
  std::size_t capacity_;
};

class SinglyLinkedList {
 public:
  struct Node {
    int value;
    Node* next;
  };

  SinglyLinkedList() = default;
  SinglyLinkedList(const SinglyLinkedList&) = delete;
  SinglyLinkedList& operator=(const SinglyLinkedList&) = delete;
  ~SinglyLinkedList() { clear(); }

  std::size_t size() const { return length_; }
  bool empty() const { return length_ == 0; }
  Node* head() const { return head_; }
  Node* tail() const { return tail_; }

  void push_front(int value) {
    head_ = new Node{value, head_};
    if (tail_ == nullptr) {
      tail_ = head_;
    }
    ++length_;
  }

  void push_back(int value) {
    Node* node = new Node{value, nullptr};
    if (tail_ == nullptr) {
      head_ = tail_ = node;
    } else {
      tail_->next = node;
      tail_ = node;
    }
    ++length_;
  }

  Node* find_first(int value) const {
    for (Node* current = head_; current != nullptr; current = current->next) {
      if (current->value == value) {
        return current;
      }
    }
    return nullptr;
  }

  Node* insert_after(Node* predecessor, int value) {
    if (predecessor == nullptr) {
      throw std::invalid_argument("insert_after requires a predecessor");
    }

    Node* node = new Node{value, predecessor->next};
    predecessor->next = node;
    if (tail_ == predecessor) {
      tail_ = node;
    }
    ++length_;
    return node;
  }

  bool erase_after(Node* predecessor) {
    if (predecessor == nullptr || predecessor->next == nullptr) {
      return false;
    }

    Node* removed = predecessor->next;
    predecessor->next = removed->next;
    if (tail_ == removed) {
      tail_ = predecessor;
    }
    delete removed;
    --length_;
    return true;
  }

  bool erase_first(int value) {
    Node* predecessor = nullptr;
    Node* current = head_;
    while (current != nullptr && current->value != value) {
      predecessor = current;
      current = current->next;
    }
    if (current == nullptr) {
      return false;
    }

    if (predecessor == nullptr) {
      head_ = current->next;
      if (tail_ == current) {
        tail_ = nullptr;
      }
      delete current;
      --length_;
      return true;
    }
    return erase_after(predecessor);
  }

  bool invariant() const {
    if ((length_ == 0) != (head_ == nullptr && tail_ == nullptr)) {
      return false;
    }

    Node* slow = head_;
    Node* fast = head_;
    while (fast != nullptr && fast->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
      if (slow == fast) {
        return false;
      }
    }

    std::size_t count = 0;
    Node* last = nullptr;
    for (Node* current = head_; current != nullptr; current = current->next) {
      last = current;
      ++count;
    }
    return count == length_ && last == tail_ &&
           (tail_ == nullptr || tail_->next == nullptr);
  }

  std::vector<int> values() const {
    std::vector<int> result;
    result.reserve(length_);
    for (Node* current = head_; current != nullptr; current = current->next) {
      result.push_back(current->value);
    }
    return result;
  }

 private:
  void clear() {
    while (head_ != nullptr) {
      Node* removed = head_;
      head_ = head_->next;
      delete removed;
    }
    tail_ = nullptr;
    length_ = 0;
  }

  Node* head_ = nullptr;
  Node* tail_ = nullptr;
  std::size_t length_ = 0;
};

}  // namespace ipara::ds01

#endif
