# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

# -------------------------------

# parameter - variable_pair_equations: List[Tuple(str, str)], values: List[int], queries: List[tuple(str, str)]
# return - query_values: List[float]

# equations = ["a", "b"], ["b", "c"]
# values = [1,2]

# a/b = 1, b/c = 2
# b/a = 1 c/b = 1/2

# queries = ["a", "c"]
# a = b * 1 -> a = (2 * c) * 1 -> a = 2c -> a/c = 2
# a/c -> a = val * c -> val * ((a * 1) * 1/2)
# a/c  -> a = val * c -> b * 1 = val * c -> 2 * c = val * c -> 2 = val -> val = 2
# 
#  
# {
# a: {b: 1},
# b: {c: 2, a: 1}
# c: {b: 1/2}
# }

# Time - O(n)
# Space - O(n)

class Solution:
    def equations(self, equations: List[Tuple[str, str]], values: List[int], queries: List[Tupe[str, str]]) -> float:

        grid = defaultdict(dict)
        for (e1, e2), val in zip(equations, values):
            grid[e1][e2] = val
            grid[e2][e1] = 1/val
        
        def _dfs_scan(start, end, visited):
            if not start in grid or not end in grid:
                return -1
            if start == end:
                return 1
            visited.add(start)
            for neighbor, val in grid[start].items():
                if neighbor in visited:
                    continue
                result = _dfs_scan(neighbor, end, visited)
                if result != -1:
                    return val * result
            return -1

        return [_dfs_scan(query[0], query[1]) for query in queries]
