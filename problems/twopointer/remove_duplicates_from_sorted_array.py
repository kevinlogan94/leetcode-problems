# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


# ------------------------------------

# parameter : nums: List[int]
# return: unique_elements: int

# Q - No deleting only moving values
# Q - We only care about values up to k
# Q - Array can be empty

# [1,2,2,3] -> [1,2,3,3]
# [1,2,2,3,3,4] -> [1,2,3,3,3,4] -> [1,2,3,4,3,4]

# 1 pointer that generates a new pointer when we hit duplicates
# loop through nums - start at 1 index
#  do comparison between index and index-1 to see if they match
#   if they match, generate new index at index+1 and loop until we hit the end of the end OR we hit a new val
#    if we hit new val, update index to be that val 
#   else k += 1


# Time - O(n) = n is len(nums)
# Space - O(1)

class Solution:
    def handle_duplicates(self, nums: List[int]) -> int:
        index = 1
        end = len(nums) - 1
        k = 1

        if not nums:
            return 0

        while index <= end:
            if nums[index] != nums[k-1]:
                nums[k] = nums[index]
                k += 1
            index += 1
        
        return k
    
# we use k through the algorithm and our core pointer. This way
# we return k at the end and it's used to help us update values

# K is your anchor



class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        k = 1

        while index in range(1, nums):
            if nums[k-1] != nums[index]:
                nums[k] = nums[index]
                k += 1
            index += 1
        
        return k