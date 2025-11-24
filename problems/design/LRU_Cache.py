# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# -----------------------------

# OrderedDict
# move_to_end
# pop(False)

# Q - used = interacted with
# Q - Can our capacity be less than 0?

# 1. define class
# 2. define init(capacity: int): 
# 3.    declare our capacity
# 4.    declare our ordereddict data
# 5 define get(key: int) -> int:
# 6.    check if val is not in data -> return -1
# 7.    push object to the end of our orderedDict
# 7.    return data[key]
# 8.define put(int key, int value) -> void
# 9.     if key is in data -> move to the end
# 10.       update the val
# 11.    else
# 12.       if over capacity -> drop furthest left element
# 13.       add new element


# Time - O(1)
# Space - O(n) = n = len(ordereddict)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()
    
    def get(self, key:int) -> int:
        if not key in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]
        
    def put(self, key:int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
            self.data[key] = value
        else:
            if len(self.data) >= self.capacity:
                self.data.popitem(last=False)
            self.data[key] = value


# Variant #1
# Add 2 additinal functions:
# boolean del (int key) - removes the key from the cache. Returns true if the key existed, false otherwise.
# int last() - returns the value if at least one value exists, otherwise return -1
# no capacity constraints for this variant


class LRUCache:
    def __init__(self):
        self.data = OrderedDict()
    
    def get(self, key:int) -> int:
        if not key in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]
        
    def put(self, key:int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
    
    def delete(self, key: int) -> bool:
        if not key in self.data:
            return False
        self.data.pop(key)
        return True

    def last(self) -> int:
        if not self.data:
            return -1
        # for key in reversed(self.data):
        #     return self.data[key]
        return next(reversed(self.data.values()), -1)
    
class LRUCache:
    def __init__(self):
        self.data = OrderedDict()
        self.mru = None
    
    def get(self, key:int) -> int:
        if not key in self.data:
            return -1
        self.data.move_to_end(key)
        self.mru = key
        return self.data[key]
        
    def put(self, key:int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
            self.mru = key
        self.data[key] = value
    
    def delete(self, key: int) -> bool:
        if not key in self.data:
            return False
        self.data.pop(key)
        return True

    def last(self) -> int:
        return self.data[self.mru] if self.mru else -1
        