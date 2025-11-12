# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the 
# permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater 
# permutation of its integer. More formally, if all the permutations of the array are sorted in one 
# container according to their lexicographical order, then the next permutation of that array is the 
# permutation that follows it in the sorted container. If such arrangement is not possible, the array 
# must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

# --------------------------------

# Parameter - nums: List[int]
# Return - None

# [1,2,3] -> [1,3,2]
# [1,2,3,1] -> [1,3,2,1]
# [1,2,3,2,1] -> [1,3,2,2,1] -> [1,3,1,2,2]
# [1,2,3,2,2,1] -> [1,3,2,2,2,1] -> [1,3,1,2,2,2]

# [1,2,4,3,2] -> [1,3,2,2,4]

# [3,2,1] -> [1,2,3]
# [1]

# 1 define class
# 2. define method
# 3.  swap_index = -1
# 4.  right = end
# 5.  loop to the left and check for a num that's prev num is greater than it 
# 6.    if match, perform swap, then rotate

# Time - O(n)
# Space - O(1)

class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        swap_index = -1
        num_size = len(nums)
        if num_size < 2:
            return 
        
        right = num_size - 2

        while 0 <= right and nums[right] >= nums[right + 1]:
            right -= 1
        swap_index = right

        if swap_index == -1:
            nums.reverse()
            return

        right = num_size - 1
        while swap_index < right and nums[right] <= nums[swap_index]:
            right -= 1
        
        right_swap_index = right

        nums[swap_index], nums[right_swap_index] = nums[swap_index], nums[right_swap_index]
        
        nums[swap_index + 1:] = nums[swap_index+1:][::-1]


# Variant 1
# What is the previous permutation?

# [1,2,3] -> [3,2,1]
# [1] -> [1]
# [1,2] -> [2,1]
# [1,3,2] -> [1,2,3] 
# [1,3,2,1,5] -> [1,3,1,2,5]
# [1,4,3,4,1] -> [1,4,3,1,4]
# [1,4,1,2,3] -> [1,3,1,2,4] -> [1,3,4,2,1]

# 1 define class
# 2 define method
# 3. declare variables - right, swap_index
# 4.    if nums_length < 2, return
# 5.  loop to the right until the value is less than the prev value
# 6.     if we don't find this, just reverse
# 7.  if we do find it.
# 8.     search right to left till we find value that is greater than num[swap_index]
# 9.     run reversal on swap_index+1 values in place


class Solution:
    def prev_premutation(self, nums:List[int]) -> None:
        num_len = len(nums)
        if num_len < 2:
            return
        
        right = num_len - 2
        while 0 <= right and nums[right] <= nums[right + 1]:
            right -= 1
        
        swap_index = right

        if swap_index == -1:
            nums.reverse()
            return
        
        right = num_len - 1

        while nums[swap_index] <= nums[right]:
            right -= 1

        swap_index_right = right

        nums[swap_index], nums[swap_index_right] = nums[swap_index_right], nums[swap_index]
        nums[swap_index+1:] = nums[swap_index+1:][::-1] 
        
