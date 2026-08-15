#ifndef IPARA_DS02_RESTRICTED_ACCESS_HPP
#define IPARA_DS02_RESTRICTED_ACCESS_HPP

#include <cstddef>
#include <memory>
#include <stdexcept>
#include <vector>

namespace ipara::ds02 {

class ArrayStack {
 public:
  explicit ArrayStack(std::size_t capacity)
      : data_(capacity == 0 ? nullptr : std::make_unique<int[]>(capacity)),
        capacity_(capacity) {}

  bool empty() const { return size_ == 0; }
  bool full() const { return size_ == capacity_; }
  std::size_t size() const { return size_; }

  void push(int value) {
    if (full()) {
      throw std::overflow_error("stack overflow");
    }
    data_[size_++] = value;
  }

  int pop() {
    if (empty()) {
      throw std::underflow_error("stack underflow");
    }
    return data_[--size_];
  }

  int top() const {
    if (empty()) {
      throw std::underflow_error("stack is empty");
    }
    return data_[size_ - 1];
  }

  bool invariant() const {
    return size_ <= capacity_ && (capacity_ == 0 || data_ != nullptr);
  }

 private:
  std::unique_ptr<int[]> data_;
  std::size_t capacity_ = 0;
  std::size_t size_ = 0;
};

class LinkedStack {
 public:
  struct Node {
    int value;
    Node* next;
  };

  LinkedStack() = default;
  LinkedStack(const LinkedStack&) = delete;
  LinkedStack& operator=(const LinkedStack&) = delete;
  ~LinkedStack() { clear(); }

  bool empty() const { return top_ == nullptr; }
  std::size_t size() const { return size_; }

  void push(int value) {
    top_ = new Node{value, top_};
    ++size_;
  }

  int pop() {
    if (empty()) {
      throw std::underflow_error("stack underflow");
    }
    Node* removed = top_;
    const int value = removed->value;
    top_ = removed->next;
    delete removed;
    --size_;
    return value;
  }

  int top() const {
    if (empty()) {
      throw std::underflow_error("stack is empty");
    }
    return top_->value;
  }

  bool invariant() const {
    std::size_t count = 0;
    Node* slow = top_;
    Node* fast = top_;
    while (fast != nullptr && fast->next != nullptr) {
      slow = slow->next;
      fast = fast->next->next;
      if (slow == fast) {
        return false;
      }
    }
    for (Node* current = top_; current != nullptr; current = current->next) {
      ++count;
    }
    return count == size_ && ((size_ == 0) == (top_ == nullptr));
  }

 private:
  void clear() {
    while (top_ != nullptr) {
      Node* removed = top_;
      top_ = top_->next;
      delete removed;
    }
    size_ = 0;
  }

  Node* top_ = nullptr;
  std::size_t size_ = 0;
};

class CircularQueue {
 public:
  explicit CircularQueue(std::size_t capacity)
      : data_(capacity == 0 ? nullptr : std::make_unique<int[]>(capacity)),
        capacity_(capacity) {}

  bool empty() const { return size_ == 0; }
  bool full() const { return size_ == capacity_; }
  std::size_t size() const { return size_; }

  void enqueue(int value) {
    if (full()) {
      throw std::overflow_error("queue overflow");
    }
    data_[rear_] = value;
    rear_ = next(rear_);
    ++size_;
  }

  int dequeue() {
    if (empty()) {
      throw std::underflow_error("queue underflow");
    }
    const int value = data_[front_];
    front_ = next(front_);
    --size_;
    return value;
  }

  int front() const {
    if (empty()) {
      throw std::underflow_error("queue is empty");
    }
    return data_[front_];
  }

  bool invariant() const {
    if (size_ > capacity_) {
      return false;
    }
    if (capacity_ == 0) {
      return data_ == nullptr && front_ == 0 && rear_ == 0 && size_ == 0;
    }
    return data_ != nullptr && front_ < capacity_ && rear_ < capacity_ &&
           rear_ == (front_ + size_) % capacity_;
  }

 private:
  std::size_t next(std::size_t index) const {
    return capacity_ == 0 ? 0 : (index + 1) % capacity_;
  }

  std::unique_ptr<int[]> data_;
  std::size_t capacity_ = 0;
  std::size_t front_ = 0;
  std::size_t rear_ = 0;
  std::size_t size_ = 0;
};

class LinkedQueue {
 public:
  struct Node {
    int value;
    Node* next;
  };

  LinkedQueue() = default;
  LinkedQueue(const LinkedQueue&) = delete;
  LinkedQueue& operator=(const LinkedQueue&) = delete;
  ~LinkedQueue() { clear(); }

  bool empty() const { return size_ == 0; }
  std::size_t size() const { return size_; }

  void enqueue(int value) {
    Node* node = new Node{value, nullptr};
    if (rear_ == nullptr) {
      front_ = rear_ = node;
    } else {
      rear_->next = node;
      rear_ = node;
    }
    ++size_;
  }

  int dequeue() {
    if (empty()) {
      throw std::underflow_error("queue underflow");
    }
    Node* removed = front_;
    const int value = removed->value;
    front_ = removed->next;
    if (front_ == nullptr) {
      rear_ = nullptr;
    }
    delete removed;
    --size_;
    return value;
  }

  int front() const {
    if (empty()) {
      throw std::underflow_error("queue is empty");
    }
    return front_->value;
  }

  bool invariant() const {
    if ((size_ == 0) != (front_ == nullptr && rear_ == nullptr)) {
      return false;
    }
    std::size_t count = 0;
    Node* last = nullptr;
    for (Node* current = front_; current != nullptr; current = current->next) {
      last = current;
      ++count;
    }
    return count == size_ && last == rear_ &&
           (rear_ == nullptr || rear_->next == nullptr);
  }

 private:
  void clear() {
    while (front_ != nullptr) {
      Node* removed = front_;
      front_ = front_->next;
      delete removed;
    }
    rear_ = nullptr;
    size_ = 0;
  }

  Node* front_ = nullptr;
  Node* rear_ = nullptr;
  std::size_t size_ = 0;
};

class CircularDeque {
 public:
  explicit CircularDeque(std::size_t capacity)
      : data_(capacity == 0 ? nullptr : std::make_unique<int[]>(capacity)),
        capacity_(capacity) {}

  bool empty() const { return size_ == 0; }
  bool full() const { return size_ == capacity_; }
  std::size_t size() const { return size_; }

  void push_front(int value) {
    require_space();
    front_ = previous(front_);
    data_[front_] = value;
    ++size_;
  }

  void push_back(int value) {
    require_space();
    data_[rear_] = value;
    rear_ = next(rear_);
    ++size_;
  }

  int pop_front() {
    require_element();
    const int value = data_[front_];
    front_ = next(front_);
    --size_;
    return value;
  }

  int pop_back() {
    require_element();
    rear_ = previous(rear_);
    const int value = data_[rear_];
    --size_;
    return value;
  }

  int front() const {
    require_element();
    return data_[front_];
  }

  int back() const {
    require_element();
    return data_[previous(rear_)];
  }

  bool invariant() const {
    if (size_ > capacity_) {
      return false;
    }
    if (capacity_ == 0) {
      return data_ == nullptr && size_ == 0 && front_ == 0 && rear_ == 0;
    }
    return data_ != nullptr && front_ < capacity_ && rear_ < capacity_ &&
           rear_ == (front_ + size_) % capacity_;
  }

 private:
  void require_space() const {
    if (full()) {
      throw std::overflow_error("deque overflow");
    }
  }

  void require_element() const {
    if (empty()) {
      throw std::underflow_error("deque underflow");
    }
  }

  std::size_t next(std::size_t index) const {
    return capacity_ == 0 ? 0 : (index + 1) % capacity_;
  }

  std::size_t previous(std::size_t index) const {
    return capacity_ == 0 ? 0 : (index + capacity_ - 1) % capacity_;
  }

  std::unique_ptr<int[]> data_;
  std::size_t capacity_ = 0;
  std::size_t front_ = 0;
  std::size_t rear_ = 0;
  std::size_t size_ = 0;
};

}  // namespace ipara::ds02

#endif
