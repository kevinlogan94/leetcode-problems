# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# ------------------------------------------

# parameters: nums: List[int], k:int
# return: max_consecutive_1s: int

# Q - values are only 0 and 1
# Q - nums can be empty
# 
# [1,1,1,0,1] - k = 2
# [0,0,1,0,1] - k = 2
#
# sliding window

# declare variables - max_cnt = 0
# move our right pointer until we hit a 0 and our k is 0
#   run max_cnt comparison
#   move our left pointer until we move away from a 0 and can increase our k to k + 1
# return max_cnt


# Time - O(n)
# Space - O(1)

# [1,1,1,1]
# 
class Solution:
    def max_consecutive_ones(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        left = 0
        # The right pointer iterates through the array
        for right in range(len(nums)):
            # If we see a 0, we use one of our k flips.
            if nums[right] == 0:
                k -= 1
            
            # If k is negative, our window is invalid (too many zeros).
            # We need to shrink the window from the left until it's valid again.
            if k < 0:
                # If the element at the left pointer was a 0, we regain a flip.
                if nums[left] == 0:
                    k += 1
                # Shrink the window.
                left += 1
        
        # The final window size (right - left + 1) will be the maximum possible.
        return len(nums) - left