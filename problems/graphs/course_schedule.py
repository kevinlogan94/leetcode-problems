# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# ------------------


# [last, first]
# parameters - prerequisities: List[Tuple[int, int]]
# return - can_finish_courses: bool


# [[0,1],[1,0],[2,0]]

# {
#   0: [1,2],
#   1: [0]
# }
# 
# 

# 0: [1]
# 1: [0]
# 2: [0]

# set called checked
# 



# declare - checked: set

# declare submethod - pass the course to check for prereq
#    mark course as checked
#       loop through pre req. See if it's already checked if not, recursively pass through submethod otherwise return False
#       return true if successfully looped through all options.

# loop through our tuples
#  build out our adjacency list graph

# loop through our graph
#   call sub_method
#     

# V = vertices, E = edges
# Time - O(V + E)
# Space - O (V + E)

class Solution:
    def course_schedule(self, prerequisites: List[Tuple[int, int]]) -> bool:
        def check_pre_req(course: int) -> bool:
            if course in checked:
                return False
            
            checked.add(course)
            for pre_req in mapp[course]:
                check_pre_req(pre_req)
            checked.remove(course)
            mapp[course] = []
            
            return True


        checked = set()
        mapp = defaultdict(List)

        for item in prerequisites:
            mapp[item[0]].append(item[1])
        
        for course in mapp:
            result = check_pre_req(course)
            if not result:
                return False
        
        return True
        
