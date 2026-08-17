#include "ds05_heap.hpp"

#include <cassert>
#include <stdexcept>

using ipara::ds05::MinHeap;

int main() {
  MinHeap empty;
  assert(empty.empty());
  try { (void)empty.top(); assert(false); } catch (const std::out_of_range&) {}

  MinHeap heap({7, 2, 9, 1, 2});
  assert(heap.invariant());
  heap.push(0);
  assert(heap.top() == 0 && heap.invariant());
  assert(heap.pop() == 0);
  assert(heap.pop() == 1);
  heap.push(3);
  assert(heap.invariant());
  assert(heap.pop() == 2);
  assert(heap.pop() == 2);
  assert(heap.pop() == 3);
  assert(heap.pop() == 7);
  assert(heap.pop() == 9);
  assert(heap.empty());
}
