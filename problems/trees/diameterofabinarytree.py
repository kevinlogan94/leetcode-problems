# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# ----------------------

# paremeter - root: Optional["Node"]
# return - diameter: int


# Q - root can be none

# binary tree - each node has at most 2 children

# Diameter 3
#       1
#    2     3
#  4   5

# diameter = height of our left node + height of our right node

# diameter 2
#    1
#  2   3

# DFS

# Time - O(n) n = the node of the tree
# Space - O(n) n = the nodes of the tree - due to recursive behavior of DFS


# 1. def class
# 2. def method
# 3. def submethod - DFS - int
# 4.   check if node is none - return 0
# 5.   call left node - return left height
# 6.   call right node - return right height
# 7.   organize the diameter - lheight + rheight
# 8.   compare max diameter and update it
# 9.   height = lheight if its bigger otherwise rheight
# 9.   return 1 + max
# 9. def max_diameter on our scope
# 10. DFS
# 11. return max diameter


class solution:
    def diameter(self, root: Optional["Node"]) -> int:
        def _dfs_traverse_tree(node: Optional["Node"]) -> int:
            if not node:
                return 0
            
            rheight = _dfs_traverse_tree(node.right)
            lheight = _dfs_traverse_tree(node.left)

            diameter = lheight + rheight
            self.max_diameter = max(self.max_diameter, diameter)

            height = lheight if lheight > rheight else rheight
            return 1 + height

        
        self.max_diameter = 0
        _dfs_traverse_tree(root)
        return self.max_diameter