# On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

# Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function 
# call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being 
# executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

# You are given a list logs, where logs[i] represents the ith log message formatted as a string 
# "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at 
# the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note 
# that a function can be called multiple times, possibly recursively.

# A function's exclusive time is the sum of execution times for all function calls in the program. For example, 
# if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive 
# time is 2 + 1 = 3.

# Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the 
# function with ID i.

# n = 3
# 1, 2, 3

# given a list of logs
# These can be in any order?
# 

# [
#   "1:start:2",
#   "1:end:3",
#   "2:start:4",
#   "2:end:5",
# ]

#  strip(":")
#  loop through this - ["1", "start", "2"]
# ["1", "end", "3"]
# ["2", "start", "4"]
# ["2", "end", "5"]
# 
#  build out a hashmap = { 1: 50 }
#  hashmap
# 1. loop through logs:
# 2.  perform strip on log:
#  ["id", "start", "end"]
# 3. if start - add to hashmap for the key id
# 4. if end - subtract from hashmap from the key id    
# 5. 
# 6. Add to a heap. each key value pair.
# 7. pop from the heap into an array
# return the array
#           
#     hashmap[log[0]] = hashmap.get(log[0], 0)

# Time - O(L) L = function count
# Space - O(n) n = function count

class Solution:
    def exclusivetimeoffunction(logs: List[str]) -> List[int]:
        mapp = {}
        heap = []

        for log in logs:
            parts = log.strip(":")
            if parts[1] == "start":
                mapp[parts[0]] = mapp.get(parts[0], 0) + parts[2]
            else:
                mapp[parts[0]] = mapp.get(parts[0], 0) - parts[2]
            
        for key, value in mapp.items():
            heapq.heappush(heap, (key, value))

        result = []
        for _ in range(len(logs)):
            _, time = heapq.heappop(heap)
            result.append(time)
        
        return result


