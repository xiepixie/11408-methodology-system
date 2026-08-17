#include "ds02_restricted_access.hpp"

#include <cassert>
#include <stdexcept>

using ipara::ds02::ArrayStack;
using ipara::ds02::CircularDeque;
using ipara::ds02::CircularQueue;
using ipara::ds02::LinkedQueue;
using ipara::ds02::LinkedStack;

template <class Exception, class Action>
void assert_throws(Action action) {
  bool thrown = false;
  try {
    action();
  } catch (const Exception&) {
    thrown = true;
  }
  assert(thrown);
}

void test_array_stack() {
  ArrayStack zero_capacity(0);
  assert(zero_capacity.empty() && zero_capacity.full());
  assert_throws<std::overflow_error>([&] { zero_capacity.push(1); });
  assert(zero_capacity.invariant());

  ArrayStack stack(2);
  assert_throws<std::underflow_error>([&] { stack.pop(); });
  stack.push(1);
  stack.push(2);
  assert(stack.top() == 2);
  assert_throws<std::overflow_error>([&] { stack.push(3); });
  assert(stack.pop() == 2 && stack.pop() == 1);
  assert(stack.empty() && stack.invariant());
}

void test_linked_stack() {
  LinkedStack stack;
  assert_throws<std::underflow_error>([&] { stack.pop(); });
  stack.push(1);
  stack.push(2);
  stack.push(3);
  assert(stack.pop() == 3 && stack.pop() == 2 && stack.pop() == 1);
  assert(stack.empty() && stack.invariant());
}

void test_circular_queue_wraparound() {
  CircularQueue zero_capacity(0);
  assert(zero_capacity.empty() && zero_capacity.full());
  assert_throws<std::overflow_error>([&] { zero_capacity.enqueue(1); });
  assert(zero_capacity.invariant());

  CircularQueue queue(3);
  queue.enqueue(10);
  queue.enqueue(20);
  queue.enqueue(30);
  assert_throws<std::overflow_error>([&] { queue.enqueue(40); });
  assert(queue.dequeue() == 10);
  queue.enqueue(40);
  assert(queue.front() == 20);
  assert(queue.dequeue() == 20);
  assert(queue.dequeue() == 30);
  assert(queue.dequeue() == 40);
  assert(queue.empty() && queue.invariant());
}

void test_linked_queue_singleton() {
  LinkedQueue queue;
  assert_throws<std::underflow_error>([&] { queue.dequeue(); });
  queue.enqueue(7);
  assert(queue.dequeue() == 7);
  assert(queue.empty() && queue.invariant());
  queue.enqueue(8);
  queue.enqueue(9);
  assert(queue.dequeue() == 8 && queue.dequeue() == 9);
  assert(queue.invariant());
}

void test_circular_deque_both_ends() {
  CircularDeque zero_capacity(0);
  assert(zero_capacity.empty() && zero_capacity.full());
  assert_throws<std::overflow_error>([&] { zero_capacity.push_back(1); });
  assert(zero_capacity.invariant());

  CircularDeque deque(4);
  deque.push_back(2);
  deque.push_front(1);
  deque.push_back(3);
  deque.push_front(0);
  assert(deque.front() == 0 && deque.back() == 3);
  assert_throws<std::overflow_error>([&] { deque.push_back(4); });
  assert(deque.pop_front() == 0);
  assert(deque.pop_back() == 3);
  assert(deque.pop_front() == 1);
  assert(deque.pop_back() == 2);
  assert_throws<std::underflow_error>([&] { deque.pop_front(); });
  assert(deque.invariant());
}

int main() {
  test_array_stack();
  test_linked_stack();
  test_circular_queue_wraparound();
  test_linked_queue_singleton();
  test_circular_deque_both_ends();
}
