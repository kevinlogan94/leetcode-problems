# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# parameter - nums: List[int], k: int
# return - an int - kth largest element in array - 

# [1,2,3,4,5] k = 2
# return 4

# is nums array sorted? - No
# Heap

# 1. loop through nums
# 2. push each num to our heap - heap is going to sort the nums
# arr - [1,7,4,5,8]
# max heap - [8,7,5,4,1] - O(logk) - k = len(heap)
# 3. pop our heap k times. run a loop that runs k times.
# 4. return final result

# max heap - [-8,-7,-5,-4,-1]
# min heap - [1,4,5,7,8]

# Time - O(nlogn) - n = len(nums)
# Space - O(n) - n = len(nums)

# Edge cases - can nums be empty?

class Solution:
    def kthlargestelement(self, nums: List[int], k: int) -> int:
        result = 0
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k):
            result = heapq.heappop(heap)
            result = -result

        return result