#ifndef IPARA_DS09_ORDERED_INDEX_HPP
#define IPARA_DS09_ORDERED_INDEX_HPP

#include <algorithm>
#include <cmath>
#include <memory>
#include <vector>

namespace ipara::ds09 {

struct Node { int key; std::unique_ptr<Node> left, right; };

class BinarySearchTree {
 public:
  bool contains(int key) const { return contains(root_.get(), key); }
  void insert(int key) { insert(root_, key); }
  bool erase(int key) { return erase(root_, key); }
  std::vector<int> inorder() const { std::vector<int> result; inorder(root_.get(), result); return result; }

 private:
  std::unique_ptr<Node> root_;
  static bool contains(const Node* node, int key) { if (!node) return false; if (key == node->key) return true; return key < node->key ? contains(node->left.get(), key) : contains(node->right.get(), key); }
  static void insert(std::unique_ptr<Node>& node, int key) { if (!node) { node = std::make_unique<Node>(Node{key, nullptr, nullptr}); return; } if (key < node->key) insert(node->left, key); else if (key > node->key) insert(node->right, key); }
  static bool erase(std::unique_ptr<Node>& node, int key) {
    if (!node) return false;
    if (key < node->key) return erase(node->left, key);
    if (key > node->key) return erase(node->right, key);
    if (!node->left) { node = std::move(node->right); return true; }
    if (!node->right) { node = std::move(node->left); return true; }
    Node* successor = node->right.get(); while (successor->left) successor = successor->left.get();
    node->key = successor->key; return erase(node->right, successor->key);
  }
  static void inorder(const Node* node, std::vector<int>& result) { if (!node) return; inorder(node->left.get(), result); result.push_back(node->key); inorder(node->right.get(), result); }
};

class AvlTree {
 public:
  bool contains(int key) const { return contains(root_.get(), key); }
  void insert(int key) { root_ = insert(std::move(root_), key); }
  std::size_t height() const { return height(root_.get()); }
  std::vector<int> inorder() const { std::vector<int> result; inorder(root_.get(), result); return result; }
  bool invariant() const { int actual = 0; return check(root_.get(), nullptr, nullptr, actual); }

 private:
  struct AvlNode { int key; int height = 1; std::unique_ptr<AvlNode> left, right; };
  std::unique_ptr<AvlNode> root_;
  static int height(const AvlNode* node) { return node == nullptr ? 0 : node->height; }
  static void refresh(AvlNode* node) { node->height = 1 + std::max(height(node->left.get()), height(node->right.get())); }
  static int balance(const AvlNode* node) { return node == nullptr ? 0 : height(node->left.get()) - height(node->right.get()); }
  static std::unique_ptr<AvlNode> rotate_right(std::unique_ptr<AvlNode> node) { auto pivot = std::move(node->left); node->left = std::move(pivot->right); refresh(node.get()); pivot->right = std::move(node); refresh(pivot.get()); return pivot; }
  static std::unique_ptr<AvlNode> rotate_left(std::unique_ptr<AvlNode> node) { auto pivot = std::move(node->right); node->right = std::move(pivot->left); refresh(node.get()); pivot->left = std::move(node); refresh(pivot.get()); return pivot; }
  static std::unique_ptr<AvlNode> insert(std::unique_ptr<AvlNode> node, int key) {
    if (!node) return std::make_unique<AvlNode>(AvlNode{key, 1, nullptr, nullptr});
    if (key < node->key) node->left = insert(std::move(node->left), key);
    else if (key > node->key) node->right = insert(std::move(node->right), key);
    else return node;
    refresh(node.get()); const int factor = balance(node.get());
    if (factor > 1 && key < node->left->key) return rotate_right(std::move(node));
    if (factor < -1 && key > node->right->key) return rotate_left(std::move(node));
    if (factor > 1 && key > node->left->key) { node->left = rotate_left(std::move(node->left)); return rotate_right(std::move(node)); }
    if (factor < -1 && key < node->right->key) { node->right = rotate_right(std::move(node->right)); return rotate_left(std::move(node)); }
    return node;
  }
  static bool contains(const AvlNode* node, int key) { if (!node) return false; if (key == node->key) return true; return key < node->key ? contains(node->left.get(), key) : contains(node->right.get(), key); }
  static void inorder(const AvlNode* node, std::vector<int>& result) { if (!node) return; inorder(node->left.get(), result); result.push_back(node->key); inorder(node->right.get(), result); }
  static bool check(const AvlNode* node, const int* lower, const int* upper, int& actual_height) {
    if (!node) { actual_height = 0; return true; }
    if ((lower && node->key <= *lower) || (upper && node->key >= *upper)) return false;
    int left_height = 0, right_height = 0;
    if (!check(node->left.get(), lower, &node->key, left_height) || !check(node->right.get(), &node->key, upper, right_height)) return false;
    actual_height = 1 + std::max(left_height, right_height);
    return node->height == actual_height && std::abs(left_height - right_height) <= 1;
  }
};
}  // namespace ipara::ds09

#endif
