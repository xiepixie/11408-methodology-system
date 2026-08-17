#include "ds06_union_find.hpp"

#include <cassert>
#include <stdexcept>

using ipara::ds06::UnionFind;

void test_make_set_and_bounds() {
  UnionFind sets(4);
  assert(sets.size() == 4 && sets.components() == 4 && sets.invariant());
  bool threw = false;
  try {
    sets.find(4);
  } catch (const std::out_of_range&) {
    threw = true;
  }
  assert(threw);
}

void test_union_and_duplicate_union() {
  UnionFind sets(6);
  assert(sets.unite(0, 1));
  assert(sets.unite(2, 3));
  assert(sets.unite(1, 2));
  assert(!sets.unite(0, 3));
  assert(sets.components() == 3);
  assert(sets.connected(0, 3));
  assert(!sets.connected(0, 4));
  assert(sets.invariant());
}

void test_path_compression_reaches_representative() {
  UnionFind sets(8);
  sets.unite(0, 1);
  sets.unite(2, 3);
  sets.unite(4, 5);
  sets.unite(6, 7);
  sets.unite(0, 2);
  sets.unite(4, 6);
  sets.unite(0, 4);
  const std::size_t representative = sets.find(7);
  assert(representative == sets.find(0));
  assert(sets.invariant());
}

void test_empty_universe() {
  UnionFind sets(0);
  assert(sets.components() == 0 && sets.invariant());
}

int main() {
  test_make_set_and_bounds();
  test_union_and_duplicate_union();
  test_path_compression_reaches_representative();
  test_empty_universe();
}
