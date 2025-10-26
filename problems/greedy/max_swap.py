# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

#  --------------


# parameter - num: int
# return - max_num: int

# Q - num is always a valid int
# Q - num can't be negative
# Q - leading 0 in num isn't going to be passed

# num = 1234
# return = 4231

# num = 9123
# return = 9321

# num = 918123

# max_num - max num
# max_i - index of the max num that we will potentially want to swap

# swap_g - greater value to swap
# swap_l - lesser value to swap

#  update swap pointers when you find a number less than the current max_num

# 1 define class
# 2 define method
# 3 convert num to list of strings
# 4 loop backwards through list of strings
# 5   check if max num
# 6.  check if num less than max num


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
        


