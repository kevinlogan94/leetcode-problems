# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# Parameter - intervals: List[List[int]]
# Return - non-overlapping intervals: List[List[int]]

# Q - [[0,1],[1,2]]
# Q - Negative numbers allowed
# Q - [[1,-1]] - No
# Q - Always pass an array
# Q - [[3,4],[0,2]]

# tc - [[0,1],[1,2]]
# ret - [[0,2]]

# sorted
# tc - [[0,4],[1,2],[3,4]]
# ret - [[0,4]]


# tc - [[0,1],[2,4],[5,6]]
# ret - [[0,1],[2,4],[5,6]]

# tc - [[0,4],[2,5],[6,7]]
# ret - [[0,5],[6,7]]

# if last right > last left -> replace else append to result
# 1. are we appending are we replacing?
#  
# 

# Time - O(nlogn) n = len(intervals) 
# Space - O(n) = len(n)

# 1. def class
# 2. def method
# 3.   sort intervals
#    
# 4.   declare result list -> add first interval
# 5.   loop through intervals starting at second interval
# 6          compare lastleft to curr_right -> if lastleft > curr_right replace else append
# 7.  return non-overlapping intervals



class solution:
    def merge_intervals(self, intervals: List[List[int]]) -> List[List[int]]:

        sorted_intervals = sorted(intervals, key=lambda i : i[0])

        result = [sorted_intervals[0]]

        for interval in sorted_intervals[1:]:
            right = interval[1]
            left = interval[0]
            lastright = interval[-1][1]

            if lastright > left:
                interval[-1][1] = lastright if lastright > right else right
            else:
                result.append([left, right])

        return result