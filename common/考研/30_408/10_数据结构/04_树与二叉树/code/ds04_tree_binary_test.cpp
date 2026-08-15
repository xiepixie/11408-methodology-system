#include "ds04_tree_binary.hpp"

#include <cassert>
#include <vector>

using ipara::ds04::Node;
using ipara::ds04::huffman_weighted_path_length;
using ipara::ds04::height;
using ipara::ds04::inorder_iterative;
using ipara::ds04::inorder_recursive;
using ipara::ds04::level_order;
using ipara::ds04::leaf;
using ipara::ds04::postorder_recursive;
using ipara::ds04::preorder_iterative;
using ipara::ds04::preorder_recursive;

std::unique_ptr<Node> sample_tree() {
  auto root = leaf(1);
  root->left = leaf(2);
  root->right = leaf(3);
  root->left->left = leaf(4);
  root->left->right = leaf(5);
  return root;
}

void test_empty_and_singleton() {
  std::vector<int> output;
  preorder_recursive(nullptr, output);
  assert(output.empty());
  assert(level_order(nullptr).empty());
  auto root = leaf(9);
  assert(height(root.get()) == 1);
  assert((preorder_iterative(root.get()) == std::vector<int>{9}));
  assert((inorder_iterative(root.get()) == std::vector<int>{9}));
}

void test_traversal_orders() {
  auto root = sample_tree();
  std::vector<int> preorder;
  std::vector<int> inorder;
  std::vector<int> postorder;
  preorder_recursive(root.get(), preorder);
  inorder_recursive(root.get(), inorder);
  postorder_recursive(root.get(), postorder);
  assert((preorder == std::vector<int>{1, 2, 4, 5, 3}));
  assert((preorder_iterative(root.get()) == preorder));
  assert((inorder == std::vector<int>{4, 2, 5, 1, 3}));
  assert((inorder_iterative(root.get()) == inorder));
  assert((postorder == std::vector<int>{4, 5, 2, 3, 1}));
  assert((level_order(root.get()) == std::vector<int>{1, 2, 3, 4, 5}));
  assert(height(root.get()) == 3);
}

void test_huffman_merge_cost() {
  assert(huffman_weighted_path_length({5, 9, 12, 13, 16, 45}) == 224);
  assert(huffman_weighted_path_length({7}) == 0);
  assert(huffman_weighted_path_length({}) == 0);
}

int main() {
  test_empty_and_singleton();
  test_traversal_orders();
  test_huffman_merge_cost();
}
