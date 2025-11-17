# Given an integer array nums of length n, you want to create an array ans of 
# length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# -----------------------------

# parameter - nums: List[int]
# Return - ans: List[int]

# Q - nums can be empty

# nums - [1,2,3] - size=3 - n=3
# ans -> size = 6
# ans - [1,2,3,]

# 0+3 = 0 -> nums[0] -> 1

# nums[0] == nums[3]
# [1,2,3,1,2,3]

# time - O(n)
# space - O(2n) -> O(n)

class solution:
    def concat_arrays(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        return nums + nums