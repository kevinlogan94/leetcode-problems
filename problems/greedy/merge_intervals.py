# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# -------------------

# parameters - intervals: Optional[List[Tuple(int, int)]]
# return - new_intervals: Optional[List[Tuple(int, int)]]

# [()]

# Q - interval values are ints
# Q - These are not sorted

# [(0,1),(1,2),(0,2)]
# [(0,1),(0,2),(1,2)]

# [(0,3),(0,2)] -> [(0,3)]
# [(0,3)]

# sort our list by tuple[0]
# declare variable - merge_intervals = []
# loop through our tuples starting at list[i + 1]
#    do comparison - 
#       if prev last int is > than curr_first_int
#           create new tuple that is (0, max(right_int))
#           append merge_intervals
#       else append i-1 to merge intervals

# Time - O(nlogn) - n = len(intervals)
# Space - O(n) - n = len(intervals)


# [(0,1),(2,4)(3,4)]
class Solution:
    def merge_intervals(self, intervals: Optional[List[Tuple[int, int]]]) -> Optional[List[Tuple[int, int]]]:
        if not intervals:
            return intervals
        
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        merged_intervals = [sorted_intervals[0]]

        for interval in sorted_intervals[:1]:
            last_merge_interval = merged_intervals[-1]
            if last_merge_interval[1] > interval[0]:
                right_spot = max(last_merge_interval[1], interval[1])
                left_spot = last_merge_interval[0]
                new_interval = (left_spot, right_spot)

                merged_intervals[-1] = new_interval
            else:
                merged_intervals.append(interval)
        
        return merged_intervals


# Variant
# Given two array of intervals A and B, where intervals in A have no overlap in A and intervals in B have no overlap in B. 
# Furthermore, A[i], B[i] = [start_i, end_i], merge all overlapping intervals between the two interval lists, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.Note: Both $A$ and $B$ 
# are sorted by their start in ascending order.

# -------------------

# parameters - A: Optional[List[Tuple(int, int)]], B: Optional[List[Tuple(int, int)]]
# return - new_intervals: Optional[List[Tuple(int, int)]]

# 

# A - [(1,2),(3,5)]
# B - [(1,4),(2,5)]

# merge them together

class Solution:
    def merge_two_interval_lists(self, A: Optional[List[Tuple[int, int]]], B: Optional[List[Tuple[int, int]]]) -> Optional[List[Tuple[int, int]]]:
        intervals = A + B
        if not intervals:
            return []

        sorted_intervals = sorted(intervals, key=lambda i : i[0])
        merged_intervals = [sorted_intervals[0]]

        for interval in sorted_intervals[1:]:
            last_interval_merged = merged_intervals[-1]

            # Check for overlap (or if intervals are touching)
            if last_interval_merged[1] >= interval[0]:
                # Merge by creating a new tuple
                right = max(last_interval_merged[1], interval[1])
                merged_intervals[-1] = (last_interval_merged[0], right)
            else:
                # No overlap, add the new interval
                merged_intervals.append(interval)
        
        return merged_intervals
