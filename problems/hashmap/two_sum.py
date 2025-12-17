# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# ----------------------------------

# parameters: nums: List[int], target: int
# return: indices: List[int]

# Q - return a list of ints
# Q - must be different indices returned
# Q - integers can be negative
# Q - We can always find a solution

# [1,2,4], target = 3
# 

# 3 - num = new_target
# hashmap

# [1]
# { 1:0 }
# 3 - 2 = 1

# method
#   define - hashmap
#   loop through nums
#     do num - k = target
#       if target is in hashmap, return indices
#     update hashmap to include num and it's index

# Time - O(n) - n = len(nums)
# Space - O(n) - n = len(nums)


# [1,2,4] - target=3

# { 1:0,  } 
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for index, num in enumerate(nums):
            match = target - num

            if match in mapp:
                return [index, mapp[match]]

            mapp[num] = index

        return []

# Meta Variant #1
# Given an array of integers nums and an integer target, return true if there exists a pair of numbers 
# such that they add up to target. Otherwise, return false.

# Each input could have multiple such pairs, and you may not use the same element twice.


# parameters - num: List[int], target: int
# return - sum_pair_exists: bool

# set instead of hashmap

# Time - O(n)
# Space - O(n)

class Solution:
    def two_sum(self, nums: List[int], target: int) -> bool:
        seen = set()

        for num in nums:
            match = target - num

            if match in seen:
                return True
            
            seen.add(num)

        return False

# Meta Varaint #2

# Given an array of pairs called dominoes and an integer target, return the number of 
# unique domino pairs [a1,a2] and [b1,b2] where a1 + b1 = target and a2 + b2 = target.
# Note: Numbers are limited to digits 0-9. Additionally, you may not use the same pair with itself.

# parameters - dominoes: List[Tuple[int,int]], target: int
# return - number_of_unique_dominoes: int


# Q - domino values are positive and negative
# Q - We could have no dominoes provided

# [[1,2],[3,4]], target = 3

# match_1 = target - domino[0]
# match_2 = target - domino[1]

# add to set

# Time - O(n)
# Space - O(n)


class Solution:
    def two_sum(self, dominoes: List[tuple[int, int]], target: int) -> List[Tuple[int,int]]:
        store = {}
        pairs = 0

        for domino in dominoes:
            match_1 = target - domino[0]
            match_2 = target - domino[1]

            if (match_1, match_2) in store:
                pairs += store[(match_1, match_2)]
            
            store[domino] = store.get(domino, 0) + 1

        return pairs