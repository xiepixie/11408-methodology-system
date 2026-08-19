#include "ds01_linear_list.hpp"

#include <cassert>
#include <stdexcept>
#include <vector>

using ipara::ds01::SequentialList;
using ipara::ds01::SinglyLinkedList;

void test_sequential_list() {
  SequentialList list(2);
  assert(list.empty());
  assert(list.invariant());

  list.insert(0, 7);
  list.insert(1, 9);
  list.insert(1, 2);
  assert(list.capacity() == 4);
  assert((list.values() == std::vector<int>{7, 2, 9}));
  assert(list.find_first(2) == 1);

  assert(list.erase(1) == 2);
  assert((list.values() == std::vector<int>{7, 9}));
  assert(list.invariant());

  bool rejected = false;
  try {
    list.insert(4, 5);
  } catch (const std::out_of_range&) {
    rejected = true;
  }
  assert(rejected);
}

void test_singly_linked_list() {
  SinglyLinkedList list;
  assert(list.empty());
  assert(list.invariant());

  bool rejected = false;
  try {
    list.insert_after(nullptr, 1);
  } catch (const std::invalid_argument&) {
    rejected = true;
  }
  assert(rejected);

  list.push_back(7);
  list.push_back(2);
  list.push_back(9);
  auto* predecessor = list.find_first(2);
  list.insert_after(predecessor, 5);
  assert((list.values() == std::vector<int>{7, 2, 5, 9}));
  assert(list.invariant());

  assert(!list.erase_after(list.tail()));
  assert(list.invariant());

  assert(list.erase_after(predecessor));
  assert(list.erase_first(7));
  assert((list.values() == std::vector<int>{2, 9}));
  assert(list.tail()->value == 9);

  list.reverse();
  assert((list.values() == std::vector<int>{9, 2}));
  assert(list.head()->value == 9);
  assert(list.tail()->value == 2);
  assert(list.tail()->next == nullptr);
  assert(list.invariant());

  list.reverse();
  assert((list.values() == std::vector<int>{2, 9}));
  assert(list.invariant());

  assert(list.erase_first(9));
  assert(list.erase_first(2));
  assert(list.empty());
  assert(list.head() == nullptr && list.tail() == nullptr);
  assert(list.invariant());
}

int main() {
  test_sequential_list();
  test_singly_linked_list();
}
