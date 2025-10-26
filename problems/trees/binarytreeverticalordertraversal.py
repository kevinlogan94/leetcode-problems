# Given the root of a binary tree, return the vertical order traversal of its nodes' values. 
# (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# ------------------------------------

# parameter - root: Optional["TreeNode"]
# Return - order: List[List[int]]

# Q - Root can be null
# Q - Can have a lot of node in our tree

#      1
#   2      3
# 4   5  6   7
# 
# [[4], [2], [1,5,6], [3], [7]]
# 

#    1
# 2     3
#   4
# 
# [[2],[1,4],[3]]

# BFS
# hashmap -> {0: [1,4], -1:[2], 1:[3]}


# Time - O(nlogn) -> n = the amount of nodes in the tree
# Space - O(n) -> n = the amount of nodes in the tree


# 1. define class
# 2  define method
# 3.  define bfs_method
# 4.   traverse through tree, update hashmap for each node based on the column, maintian a column variable as we traverse through the tree
# 5. define variables - result = [], hashmap
# 6. call bfs
# 7. loop through hashmap and append to result array
# 8. return result array


class Solution:
    def verticaltraversal(self, root: Optional["TreeNode"]) -> List[List[int]]:
        def _bfs_traversal(root: Optional["TreeNode"]) -> None:
            if not root:
                return
            
            queue = [(root, 0)]
            
            while queue:
                node, column = queue.pop(0)

                self.mapp[column].append(node.val)

                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))

        result = []
        self.mapp = defaultdict(list)
        _bfs_traversal(root)
        keys = sorted(self.mapp)
        for key in keys:
            result.append(self.mapp[key])
        return result