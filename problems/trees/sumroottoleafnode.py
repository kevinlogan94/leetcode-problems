# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

# Parameters - root: Optional["TreeNode"] -> val= 0 -> 9
# return - sum: int

# Q - Root can be none
# Q - 


# Arr - Paths -> []
#       1
#    2     3
#  4   6
# 

# [124, 126, 13]

# 1 -> return 1 if only 1 node

# 1->2->4 = 124
# 1->2->6 = 126
# 1->3 = 13

# 124+126+13 = 263

# DFS

# Time - O(n) -> n = the amount of nodes in the tree
# Space - O(n) -> n = the amount of nodes in the tree


# 1 - def class
# 2 - def method for algorithm
# 3 -   def dfs method
# 4 -     traverse down tree and keep appending to an int called path
# 5 -     Once we hit our leaf node, append to our paths array

# 6 - define array on class scope
# 7 - call dfs method
# 8 - return sum(array)


# 
class Solution:
    def sum_path_to_leaf_node(self, root: Optional["TreeNode"]) -> int:
        def _dfs_traverse_tree(node: Optional["TreeNode"], path: int) -> None:
            if not node:
                return
            
            path = path * 10 + node.val

            if not node.right and not node.left:
                self.paths.append(path)
                return

            _dfs_traverse_tree(node.left, path)
            _dfs_traverse_tree(node.right, path)


        self.paths = []
        _dfs_traverse_tree(root, 0)
        return sum(self.paths)    