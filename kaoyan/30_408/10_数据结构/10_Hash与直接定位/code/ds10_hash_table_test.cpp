#include "ds10_hash_table.hpp"

#include <cassert>

int main() {
  ipara::ds10::LinearHashTable table(4);
  assert(table.insert(1)); assert(table.insert(5)); assert(!table.insert(1));
  assert(table.contains(5)); assert(table.erase(1)); assert(!table.contains(1));
  assert(table.contains(5));
  for (int value = 10; value < 20; ++value) assert(table.insert(value));
  assert(table.size() == 11);
}
