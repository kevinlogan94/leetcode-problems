# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 
# 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# --------------------------------------

# parameter - grid: List[List[int]] -> int = 0,1
# return - max_area_of_all_islands: int

# area - the sum of all points of the island
# 0 - water
# 1 - land
#

# DFS method - loop through all island pieces directionally
#    check boundaries - row out of bounds vs. col out of bounds, check if point is water
#    
#    increment our area for the island
#    convert island piece to water

#    up
#    down
#    left
#    right

#    return area for island

# max_area variable
# loop through our row-columns
#   once we hit a land(1) - trigger DFS 
#      check against current max_area


# time - O(n) n = r x c
# space - O(n) n = r x c

class Solution:
    def max_area_of_islands(self, grid: List[List[int]]) -> int:
        def _scan_island(row: int, col: int) -> int:
            # boundaries
            if (row < 0 or row >= len(grid)
                or col < 0 or col >= len(grid[0])):
                return 0 
            
            if grid[row][col] == 0:
                return 0
            
            area = 1
            grid[row][col] = 0

            # up
            area += _scan_island(row-1,col)
            # down
            area += _scan_island(row+1,col)
            # left
            area += _scan_island(row,col-1)
            # right
            area += _scan_island(row,col+1)

            return area
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = _scan_island(row, col)
                    max_area = max(max_area, area)
        
        return max_area

