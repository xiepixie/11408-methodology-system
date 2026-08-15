#ifndef IPARA_DS04_TREE_BINARY_HPP
#define IPARA_DS04_TREE_BINARY_HPP

#include <functional>
#include <memory>
#include <queue>
#include <stack>
#include <string>
#include <vector>

namespace ipara::ds04 {

struct Node {
  int value;
  std::unique_ptr<Node> left;
  std::unique_ptr<Node> right;
};

inline std::unique_ptr<Node> leaf(int value) {
  return std::make_unique<Node>(Node{value, nullptr, nullptr});
}

inline void preorder_recursive(const Node* root, std::vector<int>& output) {
  if (root == nullptr) {
    return;
  }
  output.push_back(root->value);
  preorder_recursive(root->left.get(), output);
  preorder_recursive(root->right.get(), output);
}

inline void inorder_recursive(const Node* root, std::vector<int>& output) {
  if (root == nullptr) {
    return;
  }
  inorder_recursive(root->left.get(), output);
  output.push_back(root->value);
  inorder_recursive(root->right.get(), output);
}

inline void postorder_recursive(const Node* root, std::vector<int>& output) {
  if (root == nullptr) {
    return;
  }
  postorder_recursive(root->left.get(), output);
  postorder_recursive(root->right.get(), output);
  output.push_back(root->value);
}

inline std::vector<int> preorder_iterative(const Node* root) {
  std::vector<int> output;
  if (root == nullptr) {
    return output;
  }
  std::stack<const Node*> pending;
  pending.push(root);
  while (!pending.empty()) {
    const Node* current = pending.top();
    pending.pop();
    output.push_back(current->value);
    if (current->right != nullptr) {
      pending.push(current->right.get());
    }
    if (current->left != nullptr) {
      pending.push(current->left.get());
    }
  }
  return output;
}

inline std::vector<int> inorder_iterative(const Node* root) {
  std::vector<int> output;
  std::stack<const Node*> pending;
  const Node* current = root;
  while (current != nullptr || !pending.empty()) {
    while (current != nullptr) {
      pending.push(current);
      current = current->left.get();
    }
    current = pending.top();
    pending.pop();
    output.push_back(current->value);
    current = current->right.get();
  }
  return output;
}

inline std::vector<int> level_order(const Node* root) {
  std::vector<int> output;
  if (root == nullptr) {
    return output;
  }
  std::queue<const Node*> pending;
  pending.push(root);
  while (!pending.empty()) {
    const Node* current = pending.front();
    pending.pop();
    output.push_back(current->value);
    if (current->left != nullptr) {
      pending.push(current->left.get());
    }
    if (current->right != nullptr) {
      pending.push(current->right.get());
    }
  }
  return output;
}

inline std::size_t height(const Node* root) {
  if (root == nullptr) {
    return 0;
  }
  return 1 + std::max(height(root->left.get()), height(root->right.get()));
}

inline int huffman_weighted_path_length(const std::vector<int>& weights) {
  if (weights.size() < 2) {
    return 0;
  }
  std::priority_queue<int, std::vector<int>, std::greater<int>> pending(
      weights.begin(), weights.end());
  int total = 0;
  while (pending.size() > 1) {
    const int first = pending.top();
    pending.pop();
    const int second = pending.top();
    pending.pop();
    const int merged = first + second;
    total += merged;
    pending.push(merged);
  }
  return total;
}

}  // namespace ipara::ds04

#endif
