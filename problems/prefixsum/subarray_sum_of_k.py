# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# ---------------------------------------

# parameters: nums: list[int], k: int
# return: total_amount_of_subarrays: int

# Q - nums can be empty
# Q - k is not null
# Q - nums can have negative values


# [1,2,3], k = 3

# [1,3,6]
# target = k - prefix_sum

# [1,2,3]
# [1, 3, 6]
# { 0:1, 1:1, 3:1 }
# 3 - 6 = 3
# sum = 2

# prefixsum[right] - prefixsum[left - 1] = subarray sum
# prefixsum[right] - k = prefixsum[left - 1]



# Time - O(n) - n = len(nums)
# Space - O(n) - n = len(nums)

# class solution
#   method
#    declare variables - prefix_sum, sum, Hashmap
#    loop through our nums
#       increment our prefix_sum by num
#         do k - prefix_sum = target
#            check if target is in hashmap, if so increment sum by amount
#         add prefix_sum to hashmap
#    return sum


# [1,2,3], k = 3
# 3 - 1 = 2
# sum = 0
# prefix_sum = 1
# mapp = { 1:1 }
class Solution:
    def total_subarrays(self, nums: List[int], k: int) -> int:
        sub_array_sum = prefix_sum = 0
        mapp = {0:1}

        for num in nums:
            prefix_sum += num

            target = k - prefix_sum
            
            sub_array_sum = mapp.get(target, 0)
            mapp[target] = mapp.get(prefix_sum) + 1

        return sub_array_sum
    


# Variant 1

# Given an array of integers nums and an integer k, return true if there exists a subarray whose sum equals k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# ---------------------------------------


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        seen = set([0])

        for num in nums:
            prefix_sum += num

            target = prefix_sum - k

            if target in seen:
                return True
        
            seen.add(prefix_sum)

        return False


# Variant 2 

# Given an array of ONLY POSIVITE integers nums and an integer k, return true if there exists a subarray whose sum equals k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# ---------------------------------------

class Solution:
    def subarray_sum(self, nums: List[int], k:int) -> bool:
        if not nums:
            return False
        prefix_sum = 0
        prefix_sums = set([0])

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k

            if target in prefix_sums:
                return True
            
            prefix_sums.add(prefix_sum)

        return False
    
# [1,2,3,4] k=3
# [1,4,2,3]
# Time - O(n)
# Space - O(1)

class Solution:
    def subarray_exists(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        end = len(nums) - 1
        left = right = 0

        total = 0
        while right <= end:

            total += nums[right]
            while total > k and left <= right:
                total -= nums[left]
                left += 1
            
            if total == k:
                return True

            right += 1
        return False
