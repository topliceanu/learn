# Simple implementation of a dictionary similar to the one used in python. 
# Uses open addressing (linear probing).
# See LLM discussion: https://share.gemini.google/rfs3lytxsWae
class CompactDictMock:

  def __init__(self, initial_size=8):
    self.indices = [-1] * initial_size  # -1 signifies an empty slot
    self.entries = []  # Dense list storing (hash, key, value)
    self.used = 0  # Number of active items

  def _resize_and_rehash(self, new_size):
    old_entries = self.entries
    self.indices = [-1] * new_size
    self.entries = []
    self.used = 0

    # Re-insert existing entries into the expanded index table
    for h, k, v in old_entries:
      if k is not None:
        self._insert_internal(h, k, v)

  def _insert_internal(self, h, key, value):
    mask = len(self.indices) - 1
    perturb = h
    i = h & mask

    # Open addressing with CPython's perturbation probing formula
    while True:
      if self.indices[i] == -1:
        entry_idx = len(self.entries)
        self.indices[i] = entry_idx
        self.entries.append((h, key, value))
        self.used += 1
        break
      i = (5 * i + 1 + perturb) & mask
      perturb >>= 5

  def __setitem__(self, key, value):
    h = hash(key)
    mask = len(self.indices) - 1
    perturb = h
    i = h & mask

    # 1. Search if the key already exists (Update path)
    while True:
      entry_idx = self.indices[i]
      if entry_idx == -1:
        break
      stored_h, stored_key, _ = self.entries[entry_idx]
      if stored_h == h and stored_key == key:
        self.entries[entry_idx] = (h, key, value)  # Update in-place
        return
      i = (5 * i + 1 + perturb) & mask
      perturb >>= 5

    # 2. Check resize threshold (trigger resize if capacity reaches 2/3)
    if self.used >= len(self.indices) * 2 // 3:
      self._resize_and_rehash(len(self.indices) * 2)
      self.__setitem__(key, value)  # Retry insertion after resize
      return

    # 3. Insert new key
    self._insert_internal(h, key, value)

  def __getitem__(self, key):
    h = hash(key)
    mask = len(self.indices) - 1
    perturb = h
    i = h & mask

    while True:
      entry_idx = self.indices[i]
      if entry_idx == -1:
        raise KeyError(key)
      stored_h, stored_key, stored_val = self.entries[entry_idx]
      if stored_h == h and stored_key == key:
        return stored_val
      i = (5 * i + 1 + perturb) & mask
      perturb >>= 5

  def __repr__(self):
    items = [f"{k!r}: {v!r}" for _, k, v in self.entries]
    return "{" + ", ".join(items) + "}"