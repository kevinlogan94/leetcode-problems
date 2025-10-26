# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

#  --------------------------

# Parameter - nums:List[int], k: int
# Return - most_frequent_elements: List[int]

# k = 2
# return the 2 most frequent elements
# most frequent elements
# [1,2,2,4,4,5] - return [2, 4]

# hashmap - {1:1. 2:2, 4:2, 5:1}
# arr - [-1,-2,-2,-1]

# heapify - arr -> [-2,-2,-1,-1] - Max heap

# loop k times -> pull from heap and into res array -> [2,2]
# loop through hashmap -> [2,4]

# time - O(nlogn) -> n = the len(nums)
# space - O(n) -> n = the len(nums)


# 1. def class
# 2. def method
# 3.   loop through array and store count in hashmap
# 4.   loop through values in hashmap and put into heap
# 5.   loop through our heap k times and 
# 6.        insert corresponding key from hashmap into our result 
# 7.   return result

# {1:1. 2:2, 4:2, 5:1}

class Solution:
    def top_frequent_k(self, nums: List[int], k: int) -> List[int]:
        heap = []
        mapp = {}
        result = []

        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1
        
        for key in mapp:
            heapq.heappush(heap, (-mapp[key], key))
        
        for _ in range(k):
            _, key = heapq.heappop(heap)
            result.append(key)
        
        return result