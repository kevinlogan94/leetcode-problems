# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# -----------------------------

# Parameters: nums1: List[int], nums2: List[int]
# Return: median: int

# median - The middle number in the array

# Binary Search

# [1, 2, 3, 4, 5]
# [1, 2, 3]

# median -> 3

# partition of both big and small arrays
# 
#    *
# [1,2,3]

#    *
# [1,2,3,4,5]
# total = 8 -> half = 4 -> 2

# 2 + 3 / 2 -> 2.5

#      *
# [1,2,3,4,5]
#    *
# [1,2,3,4]

# 9 total -> 9 + 1 // 2 -> 5 - 2 -> 3 

# 3 <= 3, 2 <= 4 

# 3 = median

# Time - O(log m+n)
# Space - O(1)

class Solution:
    def median_of_two_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        array_1, array_2 = nums1, nums2
        len1 = len(array_1)
        len2 = len(array_2)

        if len1 > len2:
            array_1, array_2 = array_2, array_1
            len1, len2 = len2, len1

        total = len1 + len2
        half = (total + 1) // 2

        left, right = 0, len1
        while True:
            mid1 = left + (right - left) // 2
            mid2 = half - mid1

            left1 = float("-inf") if mid1 < 0 else array_1[mid1 - 1]
            right1 = float("inf") if mid1 >= len1 else array_1[mid1]

            left2 = float("-inf") if mid2 < 0 else array_2[mid2 - 1]
            right2 = float("inf") if mid2 >= len2 else array_2[mid2]

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:   
                    return (max(left1, left2) + min(right1, right2)) / 2
                return max(left1,left2)
            elif left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1 

