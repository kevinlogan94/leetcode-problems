# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

# ------------------------------

# time - O(m*n) m = rows, n = cols
# space - O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        len_row = len(matrix)
        len_col = len(matrix[0])

        for row in range(1, len_row):
            for col in range(1, len_col):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False

        return True
