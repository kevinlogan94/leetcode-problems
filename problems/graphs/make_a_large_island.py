# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

# Return the size of the largest island in grid after applying this operation.

# An island is a 4-directionally connected group of 1s.

# --------------------------------------

# Parameter - grid: List[List[int]] -> int -> 1,0
# Return - largest_island_size: int


# declare vars - island_map, island_label, max_area

# 2 sub-methods
# _dfs -> scan island, get area, update island values to new label
# _check_island -> check perimeter of island 

# 2 pass throughs
# Loop through our row-columns
#   if we hit a 1, scan the grid from that location using DFS sub-method
#      calc area of each island and update island label for island

# loop through row-columns
#   if we hit a 0, run sub-method to calculate largest island by flipping 0 to 1
#      compare to max_area

# return max_area


# Time - O(n) = n = r x c
# Space - O(n) = island_map


class Solution:
    def make_a_large_island(self, grid: List[List[int]]) -> int:
        def _dfs_scan_island(row: int, col: int, label: int):
            # boudanries
            if row <= 0 or row > len(grid) or col <= 0 or col > len(grid[0]):
                return 0
            
            if grid[row][col] != 1:
                return 0
            
            grid[row][col] = label

            area = 1

            # up
            area += _dfs_scan_island(row-1,col)
            # down
            area += _dfs_scan_island(row+1,col)
            # left
            area += _dfs_scan_island(row,col-1)
            # right
            area += _dfs_scan_island(row,col+1)

            return area


        def _check_potential_island(row: int, col: int):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            max_area = 0
            islands_checked = set()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                    island = grid[new_row][new_col]
                    if not island in islands_checked and island != 0:
                        area = island_map.get(grid[new_row][new_col], 0)
                        max_area += area
                        islands_checked.add(island)

            return max_area + 1

        island_map = {}
        island_label = 2
        max_area = 0

        # pass 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = _dfs_scan_island(row, col, island_label)
                    island_map[island_label] = area
                    island_label += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    potential_max_area = _check_potential_island(row, col)
                    max_area = max(max_area, potential_max_area)
        
        return max_area
