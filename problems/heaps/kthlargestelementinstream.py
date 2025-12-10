# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# -----------------------------

# parameters: nums: List[int], k: int
# return: return kth_largest_element: int

# k=2 -> return the 2nd largest element

# heap

# 12345, k = 2
# [4, 5]


# loop through nums
#    store num in min_heap until min_heap = k, 
#      if min_heap[0] < num -> heap_replace
# return min_heap[0]
# 
# 

# time - o(n) = n = len(nums)
# space - O(n) -> n = k


class Solution:
    def kth_largest_element(self, nums: List[int], k: int) -> Optional[int]:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if heap[0] < num:
                    heapq.heapreplace(heap, num)
        
        return heap[0] if heap else None
