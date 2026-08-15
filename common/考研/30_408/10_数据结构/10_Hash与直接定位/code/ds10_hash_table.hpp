#ifndef IPARA_DS10_HASH_TABLE_HPP
#define IPARA_DS10_HASH_TABLE_HPP

#include <cstddef>
#include <optional>
#include <stdexcept>
#include <vector>

namespace ipara::ds10 {

class LinearHashTable {
 public:
  explicit LinearHashTable(std::size_t capacity = 8) : slots_(capacity ? capacity : 1) {}
  bool insert(int key) { if ((size_ + 1) * 10 >= slots_.size() * 7) rehash(slots_.size() * 2); return place(key); }
  bool contains(int key) const { return locate(key).has_value(); }
  bool erase(int key) { auto index = locate(key); if (!index) return false; slots_[*index] = Slot::deleted(); --size_; return true; }
  std::size_t size() const { return size_; }

 private:
  struct Slot { std::optional<int> value; bool tombstone = false; static Slot deleted() { return Slot{std::nullopt, true}; } };
  std::vector<Slot> slots_; std::size_t size_ = 0;
  std::size_t hash(int key) const { return static_cast<std::size_t>(key >= 0 ? key : -static_cast<long long>(key)) % slots_.size(); }
  bool place(int key) { std::size_t first_deleted = slots_.size(); for (std::size_t step = 0; step < slots_.size(); ++step) { auto i = (hash(key) + step) % slots_.size(); if (slots_[i].value && *slots_[i].value == key) return false; if (!slots_[i].value) { if (first_deleted != slots_.size()) i = first_deleted; slots_[i].value = key; slots_[i].tombstone = false; ++size_; return true; } if (slots_[i].tombstone && first_deleted == slots_.size()) first_deleted = i; } return false; }
  std::optional<std::size_t> locate(int key) const { for (std::size_t step = 0; step < slots_.size(); ++step) { auto i = (hash(key) + step) % slots_.size(); if (!slots_[i].value && !slots_[i].tombstone) return std::nullopt; if (slots_[i].value && *slots_[i].value == key) return i; } return std::nullopt; }
  void rehash(std::size_t capacity) { auto old = std::move(slots_); slots_.assign(capacity, Slot{}); size_ = 0; for (const auto& slot : old) if (slot.value) place(*slot.value); }
};
}  // namespace ipara::ds10

#endif
