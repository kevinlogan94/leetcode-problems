# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

# LFUCache(int capacity) Initializes the object with the capacity of the data structure.

# int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.

# void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. 
# When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting 
# a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently 
# used key would be invalidated.

# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the 
# smallest use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter 
# for a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = {}  # Stores {key: (value, freq)}
        self.freq_to_keys = defaultdict(OrderedDict) # Stores {freq: OrderedDict of keys}
        self.min_freq = 0

    def _update_freq(self, key: int):
        """
        Moves a key from its current frequency group to the next one.
        This is the core logic for updating the cache when a key is accessed.
        """
        value, freq = self.values[key]

        # 1. Remove key from its old frequency group's OrderedDict
        del self.freq_to_keys[freq][key]

        # 2. If the old frequency group is now empty and it was the min_freq, update min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        # 3. Update the key's frequency and add it to the new frequency group
        new_freq = freq + 1
        self.values[key] = (value, new_freq)
        self.freq_to_keys[new_freq][key] = None # Value in OrderedDict doesn't matter
    
    def get(self, key: int) -> int:
        """
        Gets the value of the key if it exists, and updates its frequency.
        """
        if key not in self.values:
            return -1
        
        # Update the key's frequency since it was accessed
        self._update_freq(key)
        return self.values[key][0]

    def put(self, key: int, value: int) -> None:
        """
        Updates the value of a key if it exists, or adds a new key.
        Evicts the LFU/LRU item if capacity is reached.
        """
        if self.capacity == 0:
            return

        if key in self.values:
            # Key exists: Update value and frequency
            freq = self.values[key][1]
            self.values[key] = (value, freq) # Update value, freq is handled by _update_freq
            self._update_freq(key)
        else:
            # Key is new: Check capacity and add
            if len(self.values) >= self.capacity:
                # Evict the LFU/LRU item
                lfu_keys = self.freq_to_keys[self.min_freq]
                key_to_evict, _ = lfu_keys.popitem(last=False)
                del self.values[key_to_evict]

            # Add the new key
            # A new key always has a frequency of 1
            self.values[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
            
    
    

    