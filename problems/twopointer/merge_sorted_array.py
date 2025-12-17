# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the 
# array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the 
# elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# -----------------------------------------------------------------------------------------------------------------------

# nums1 - [5,6,7,0,0,0] -> [1,6,7,5,0,0] -> [1,2,7,5,6,0] -> [1,2,3,5,6,7]
# nums2 - [1,2,3]

# nums1 - [1,2,3,0,0,0]
# nums2 - [4,5,6]

# nums1 - [1,2,3,0,0,0] -> [1,2,2,3,0,0] -> []
# nums2 - [2,5,6]

# nums1 - [1,2,4,5,6,0] -> [1,2,3,5,6,4] -> 
# nums2 - [3]

# open_space = m + 1

# m = length of nums1 valid values
# m + n = the full length
# n = length of nums2

# method
#  declare - open_space = m+1, nums2_pntr, nums1_pntr
#    loop through nums1, nums2
#        run comparison on pntr. 
#            if val at nums1_pntr is less than val at nums1_pntr
#               set open_space to val at nums1_pntr
#               update nums1_pntr with val at nums2_pntr
#               increment nums2_pntr
#            increment nums1_pntr


# Time - O(k) - k = m+n
# Space - O(1)
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1 
        p2 = n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1