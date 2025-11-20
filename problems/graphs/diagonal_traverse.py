# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# -----------------------------

from collections import defaultdict
from typing import List

class Solution:
    def find_diagonal_order(self, mat: List[List[int]]) -> List[int]:
        """
        Traverses the matrix in a diagonal zig-zag pattern.

        Time Complexity: O(m * n) - We visit each element once to group them and once to build the result.
        Space Complexity: O(m * n) - In the worst case, the dictionary stores all elements.
        """
        if not mat or not mat[0]:
            return []

        # A dictionary to group elements by the sum of their indices (row + col).
        diagonals = defaultdict(list)
        
        # Step 1: Group elements by diagonal.
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonals[r + c].append(mat[r][c])
        
        # Step 2: Build the result, reversing even-indexed diagonals.
        result = []
        for i in range(len(diagonals)):
            diagonal_group = diagonals[i]
            if i % 2 == 0:
                # Even diagonals go up-right, so we reverse the list
                # which was populated from top-left to bottom-right.
                result.extend(diagonal_group[::-1])
            else:
                # Odd diagonals go down-left, which matches the population order.
                result.extend(diagonal_group)
                
        return result