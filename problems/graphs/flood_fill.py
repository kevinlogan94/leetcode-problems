# You are given an image represented by an m x n grid of integers image, where image[i][j] 
# represents the pixel value of the image. You are also given three integers sr, sc, and color. 
# Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side 
# with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

#  --------------------------

# parameter - image: List[List[int]], sr: int, sc: int, color: int
# Return - modified_image: List[List[int]]
# 
#  
# DFS
# boundaries - outside the chart, chart values that have diff color.

# 1.  run DFS at position 
# 2.   check all the boundaries - diff color, outside the bounaries of chart
# 3.   conver color to new color
# 4.   recursively call dfs on neighboring cells
# 5.  return chart

# DFS

class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def _dfs_fill(sr, sc):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != curr_color:
                return 
            
            image[sr][sc] = color

            # up
            _dfs_fill(sr - 1, sc)
            # down
            _dfs_fill(sr + 1, sc)
            # left
            _dfs_fill(sr, sc - 1)
            # right
            _dfs_fill(sr, sc + 1)
            
        curr_color = image[sr][sc]
        if curr_color == color:
            return image
        
        _dfs_fill(sr, sc)
        return image
            

# BFS

class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]

        if color == curr_color:
            return image
        
        queue = [(sr, sc)]
        directions = [(0,-1), (0,1), (1,0), (-1,0)]

        while queue:
            curr_row, curr_col = queue.pop(0)

            image[curr_row][curr_col] = color

            for row, col in directions:
                new_row = curr_row + row
                new_col = curr_col + col

                if new_row >= 0 and new_row < len(image) and new_col >= 0 and new_col < len(image[0]) and curr_color == image[new_row][new_col]:
                    queue.append((new_row, new_col))
        return image







