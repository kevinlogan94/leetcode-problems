# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# -------------------


# parameters: intervals: List[Tuple[int,int]]
# return: non_overlap_intervals: List[Tuple[int,int]]


# Q - intervals are ints
# Q - Intervals will be provided
# Q - intervals aren't ordered - [[2,3],[1,2]]

# [[1,2],[2,3]] -> [[1,3]]
# [[1,2]] -> [[1,2]]
# [[1,3],[2,4],[6,7]] -> [[1,4],[6,7]]

# sort -> [0] -> is in order
# [[2,3],[1,2]] -> [[1,2],[2,3]]

# [[1,4],[6,7]]


# class
# method
#   declare - new_intervals, 
#   push first entry in intervals to new_intervals
#   loop through intervals starting at 2nd interval
#      compare curr_interval to the last interval in new_intervals
#        compare new_intervals[last] and curr[first] element 
#           if new_interval is >= curr then... 
#             compare last to last -> update new intervals if necessary
#           else
#             push curr to new_intervals

#   return new_intervals



# Time - O(nlogn) - n = len(s)
# Space - O(n) - n = len(s)



class Solution:
    def merge_intervals(self, intervals: List[Tuple[int,int]]) -> List[Tuple[int, int]]:
        if not intervals:
            return []
        
        intervals = sorted(intervals, key=lambda i: i[0])

        new_intervals = [intervals[0]]

        for index in range(1, len(intervals)):
            last = new_intervals[-1]
            curr = intervals[index]

            if last[1] >= curr[0]:
                new_intervals[-1][1] = last[1] if last[1] >= curr[1] else curr[1]
            else:
                new_intervals.append(curr)
            
        return new_intervals


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
