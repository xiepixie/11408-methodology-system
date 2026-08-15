#include "ds09_ordered_index.hpp"

#include <cassert>
#include <vector>

int main() {
  ipara::ds09::BinarySearchTree tree;
  assert(!tree.contains(4));
  tree.insert(5); tree.insert(3); tree.insert(7); tree.insert(6); tree.insert(8); tree.insert(3);
  assert(tree.contains(6));
  assert((tree.inorder() == std::vector<int>{3, 5, 6, 7, 8}));
  assert(tree.erase(3)); assert(tree.erase(5)); assert(!tree.erase(42));
  assert((tree.inorder() == std::vector<int>{6, 7, 8}));
  ipara::ds09::AvlTree avl;
  for (int key : {30, 20, 10, 25, 28, 40, 50}) { avl.insert(key); assert(avl.invariant()); }
  assert(avl.contains(28) && !avl.contains(99));
  assert((avl.inorder() == std::vector<int>{10, 20, 25, 28, 30, 40, 50}));
  assert(avl.height() <= 3);
}
