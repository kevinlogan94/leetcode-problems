# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# ---------------------------------------

# parameters - nums: list[int], k:int
# return - total_subarrays: int

# Q - negative numbers allowed

# [1,2,3,4]
# [1,3,6,10]
# prefix[3] - prefix[0] -> 10 - 1 -> 9
# prefix[right] - prefix[left - 1] = k
# prefix[right] = k - prefix[left - 1]
# prefix[right] - k = prefix[left - 1]



class Solution:
    def subarray_sum(self, nums: List[int], k:int) -> int:
        if not nums:
            return 0
        total = prefix_sum = 0
        mapp = {0:1}

        for num in nums:
            prefix_sum += num

            target = prefix_sum - k
            total += mapp.get(target, 0)

            mapp[prefix_sum] = mapp.get(prefix_sum, 0) + 1
        
        return total
    


# Variant 1

# Given an array of integers nums and an integer k, return true if there exists a subarray whose sum equals k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# ---------------------------------------

class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        prefix_sum = 0
        seen = {0}

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
