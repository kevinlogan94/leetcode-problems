# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# parameter - nums:List[int] , k: int
# return - int - 

# Q - nums can be empty
# Q - k can equal 0
# Q - Negative numbers are allowed

# [1,2,3,4,5] , k = 3
# 2 total subarrays - return 2

# [1,3,6,10,15]

# [1,2,3,-3,5], k = 3
# [1,3,6,3]
# {0:1, 1:1, 3:2, 8:1}
# sum - k = target
# 
# result = 3

# 1. loop through nums
# 2. build out prefix sum
# 3. on each index, run sum - k = target
# 4. check if target is in our hashmap, if so add the count
# 5. add to our hashmap
# 6. return our result

# Time - O(n) n = len(nums)
# Space - O(n)


# [1,2,3,-3,5]
class Solution:
    def subarraysum(self, nums: List[int], k: int) -> int:
        result = 0
        curr_sum = 0
        mapp = { 0:1 }

        for num in nums:
            curr_sum += num
            
            target = curr_sum - k
            result += mapp.get(target, 0)

            mapp[curr_sum] = mapp.get(curr_sum, 0) + 1

        return result