# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
# two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a 
# node to be a descendant of itself).”

# ----------------------------------------------

# Parameter - Root: Optional["TreeNode"], p: "TreeNode", q: "TreeNode"
# Return - Node: Optional["TreeNode"]


# Q - Given a root node
# Q - Root node can be null
# Q - Given p, q and root
# Q - any num val possible for our nodes
# Q - P and q are nodes in our tree

# p = 1, q = 3
#   1
# 2   3
# LCA -> 1 -> return node with 1

# p = 2, and q = 4
#    1
#  2   3
# 4
# LCA -> 2 -> return node with 2
# HCA -> 4 -> return node with 4

# p = 3, q = 4
#    1
#  2   3
# 4
# LCA -> 1


# DFS

# Time - O(n) n = amount nodes in our tree
# Space - O(n) n = amount nodes in our tree - due to recursive calls on the stack

# 1. def class
# 2, def method
# 3,   if not node -> return
# 4. 
# 5,   scan to the right -> did we find p/q?
# 6,   scan to the left -> did we find p/q?
# 7,   
# 8 if node = p or q return node
# 9.   if right and left both have q, then return node 
# 10 .


class solution:
    def lca_of_tree(self, root: Optional["TreeNode"],q: "TreeNode",p: "TreeNode") -> Optional["TreeNode"]:

        if not root:
            return  
        
        if root == q or root == p:
            return root

        right = self.lca_of_tree(root.right, p, q)
        left = self.lca_of_tree(root.left, p, q)

        if right and left:
            return root
        return right if right else left


