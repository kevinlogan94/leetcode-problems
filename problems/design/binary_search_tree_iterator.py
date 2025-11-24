# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part 
# of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

# boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise 
# returns false.

# int next() Moves the pointer to the right, then returns the number at the pointer.

# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() 
# will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number 
# in the in-order traversal when next() is called.

# ----------------------

#    4
#   2
#  1 3

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.sorted_nodes = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        self._inorder(node.left)
        self.sorted_nodes.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        self.index += 1
        val = self.sorted_nodes[self.index]
        return val

    def hasNext(self) -> bool:
        return self.index < len(self.sorted_nodes) - 1