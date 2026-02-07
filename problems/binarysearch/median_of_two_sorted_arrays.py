# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# -----------------------------

# parameters: nums1: List[int], nums2: List[int]
# return: median: int

# Q - nums1 and nums2 is valid
# Q - positive and negative numbers
# 

#      *
# [1,2,3,4]
#    *
# [2,3,4,5]
# [1,2,2,3,3,4,4,5] -> 3

# Left Partition Strategy
# binary search

# left = 0, right = 3 -> 0 + 3 // 2 = 1
# total = len(nums1) + len(nums1) = 8 + 1 // 2 = 3 - 2 = 1


#      *
# [1,2,3,4]
#    *
# [1,2,3,4,5]

# 10 // 2 = 9
# total = 9 // 2 = 3 - 2 = 1
# min to the right of both pointers is the value

# 



# find the smaller array

# while left <= right:
#    a_mid = left + right // 2
#    b_mid = half - a_mid


#  a_max = float("inf")
#  b_max = 

#   if a[a_mid + 1] <= b[b_mid + 1] and b[b_mid + 1] <= a[a_mid + 1]:
#       check total
#   elif a[a_mid + 1] < b[b_mid + 1]:
#      left = mid + 1
#   else:
#      right = mid - 1

# 







class Solution:
    def median_of_two_arrays(self, nums1: list[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2
        A_len = len(A)
        B_len = len(B)

        if A_len > B_len:
            A, B = B, A
            A_len, B_len = B_len, A_len
        
        total = A_len + B_len
        half = total + 1 // 2

        left = 0
        right = A_len - 1

        while left <= right:
            A_mid = right + left // 2
            B_mid = half - A_mid

            A_max = float("inf") if A_mid >= A_len else A[A_mid + 1]
            B_max = float("inf") if B_mid >= B_len else B[B_mid + 1]

            A_min = float("-inf") if A_mid < 0 else A[A_mid]
            B_min = float("-inf") if B_mid < 0 else B[B_mid]

            if A_min <= B_max and B_min <= A_max:
                if total % 2 == 0:
                    return A_min + B_min / 2
                else:
                    return min(A_min, B_min)
            elif A_min > B_max:
                right = A_mid - 1
            else:
                left = A_mid + 1
            
        






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

