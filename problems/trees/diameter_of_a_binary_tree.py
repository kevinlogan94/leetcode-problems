# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

# ----------------------


# parameters - root: TreeNode
# return - length_of_diameter: int


# Q - can root be null - yes
# Q - binary tree means there is generally a left and right child of each node.


# DFS

#   1
# 2   3 


#    1
#  3   4
#    2   5
# 


# calculate the height


# class
#   method
#     sub_method -> diameter:
#        if not root - return diameter 
#        
#        trigger right and left node recursively and return each height
#        add up right and left height to get diameter
#          if diameter is greater then existing, up it.
# 
#        height to return, l_height or r_height, which is greater + 1
#        

#     declare diameter
#     call method
#     return diameter



# Time - O(n) = n = size of the tree
# Space - O(n) = n = size of the tree


class Solution:
    def diameter_of_tree(self, root: Optional[TreeNode]) -> int:
        
        def _dfs_check_diameter(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            l_height = _dfs_check_diameter(node.left) # 1
            r_height = _dfs_check_diameter(node.right)

            curr_diameter = l_height + r_height
            self.diameter = max(curr_diameter, self.diameter)

            height = r_height if r_height > l_height else l_height

            return height + 1


        self.diameter = 0
        _dfs_check_diameter(root)
        return self.diameter





















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