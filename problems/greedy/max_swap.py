# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

#  --------------


# Parameters: num: int
# return: max_num: int

# Q - no negative nums

# max_swap
# two pointers

# 12345 -> 52341
# 45231 -> 54231
# 95452 -> 95542
# 99129

# 

# swap
# potential swap 

# swap_g - num[0] + 1 and greater
# swap_l - num[end] - 1 and lesser


# 
# declare variables - swap_l, swap_r, p_swap_r, convert num to list[chars]
# first num is greatest num - p_swap_r
# loop through our nums right to left, start at len(num) - 1
#   check if num is less than p_swap_r -> if so, set swap_l and swap_r
#   check if num is greater than p_swap_r -> if so, update p_swap_r


# Time - O(n) - n is the length of num
# Space - O(n) - n is the length of num

class Solution:
    def max_swap(self, num: Optional[int]) -> int:
        # The problem constraints usually guarantee num is not None, but this is safe.
        if num is None:
            return num
        
        nums = list(str(num))
        
        # Create a map to store the last seen index of each digit.
        last_occurrence = {int(digit): i for i, digit in enumerate(nums)}

        # Iterate from left to right to find the first digit that can be swapped.
        for i, digit in enumerate(nums):
            # Check for a larger digit (from 9 down to current digit + 1).
            for d in range(9, int(digit), -1):
                # If a larger digit exists and its last occurrence is after the current index...
                if d in last_occurrence and last_occurrence[d] > i:
                    # ...we've found our optimal swap.
                    j = last_occurrence[d]
                    nums[i], nums[j] = nums[j], nums[i]
                    return int("".join(nums))

        # If no swap was made, the number is already the largest possible.
        return int("".join(nums))
    


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        max_num = nums[-1]
        max_index = len(nums) - 1

        index_l = 0
        index_g = 0

        pointer = len(nums) - 2

        while pointer >= 0:
            if nums[pointer] > max_num:
                max_num = nums[pointer]
                max_index = pointer
            elif nums[pointer] < max_num:
                index_l = pointer
                index_g = max_index
            pointer -= 1
        
        nums[index_l], nums[index_g] = nums[index_g], nums[index_l]

        return int("".join(nums))