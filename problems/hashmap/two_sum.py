# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



# parameter - nums: int, target: int
# return - indices: List[int]

# hashmap - { value: index }

# Loop through the nums - enumerate
# target - num approach -> match

# if match in hashmap
# if no match, add the num to our hashmap
# otherwise return the indices

# Time - O(n) - n = length of nums
# Space - O(n) - n = length of nums

# Q - empty nums is possible
# target = 99, nums = [1,2,3]

# 1 define class
# 2. define method
# 3.  declare variables -> hashmap, result:List[]
# 4.  loop through our nums array
# 5.   do match logic and comparison and return indices if match
# 6.  return []


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

class Solution:
    def two_sum(self, nums: List[int], target: int) -> bool:
        prev_nums = set()

        for num in nums:
            match = target - num
            if match in prev_nums:
                return True
            
            prev_nums.add(num)

        return False

# Meta Varaint #2

# Given an array of pairs called dominoes and an integer target, return the number of 
# unique domino pairs [a1,a2] and [b1,b2] where a1 + b1 = target and a2 + b2 = target.
# Note: Numbers are limited to digits 0-9. Additionally, you may not use the same pair with itself.

class Solution:
    def two_sum(self, dominoes: List[List[int]], target: int) -> int:
        mapp = {}
        pairs = 0

        for domino in dominoes:
            value1 = target - domino[0]
            value2 = target - domino[1]
            pairs += mapp.get((value1, value2), 0)

            keyToStore = (domino[0], domino[1])
            mapp[keyToStore] = mapp.get(keyToStore, 0) + 1

        return pairs