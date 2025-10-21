# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# array = [1,2,3,4] k = 2

# elements?
# return array?
# return the 2 most frequent elements?

# Time - O(nlogk)
# Space - O(n) - n = len(hashmap) + len()

class Solution:
    def frequent_elements(self, nums: List[int], k: int) -> List[int]:
# 1. Declare variables - hashmap
        mapp = {}
        heap = []
        result = []
# 2. loop through our array
        for num in nums:
# 3. hashmap - count the
            mapp[num] = mapp.get(num, 0) + 1
# 4. use min-heap and add tuples to heap with frequency in the 0 position
        for key in mapp:
            heapq.heappush(heap, (-mapp[key], key))
# 5. pop the first k elements of the min heap. Could use quickselect to speed things up.
        for _ in range(k):
            freq, key = heapq.heappop(heap)
            result.append(key)
# 6. return result
        return result

