# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# parameter - root : Optional['Node']
# return List[Node] -> in order from top to bottom


# set - [1, 2, 3]
# result - [2, 4, 8]
#     2 <-
#   3   4 <-
#  5   7  8 <- 

#       2 <-
#     3    4 <-
#   5 <-
# 6 <-

#   1 <-
#  2 3 <-

#  BFS - right to left
#  submethod 
#  keep track of the row - in a set <- O(1)
#  
#  variable - result []

# Time - O(n) n = the nodes within our tree
# Space - O(n) n = the nodes within our tree

# ------

class Solution:
    def rightsideview(self, root: Optional[TreeNode]) -> List[int]:
        def _bfs_traversal(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            queue = [node]

            while queue:
                level_len = len(queue)

                for index in range(level_len):
                    curr_node = queue.pop(0)

                    if index == 0 or index == level_len - 1:
                        self.result.append(curr_node.val)
                    
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
        
        self.result = []
        _bfs_traversal(root)
        return self.result
        


# Variant - return the nodes if you were looking at it from either side


def both_side_view(self, root: Optional[TreeNode]) -> List[int]:
    def _bfs_traversal(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        queue = [node]

        while queue:
            queue_len = len(queue)
            for index in range(queue_len):
                curr_node = queue.pop(0)

                if index == 0 or index == queue_len - 1:
                    self.result.append(node.val)

                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

    self.result = []
    _bfs_traversal(root)
    return self.result                
                


# Variant - Print Both Views

# Same as above except we want to print the values instead of returning them in a list
# print out all the values on the left from top to bottom and then all the values on the right from top to bottom

class Solution:
    def tree_print_both_sides(root: Optional[TreeNode]) -> None:
        if not root:
            return 
        
        queue = [root]
        left_side_view = []
        right_side_view = []

        while queue:
            queue_len = len(queue)

            for index in range(queue_len):
                node = queue.pop(0)
                if index == 0:
                    left_side_view.append(node)
                if index == queue_len - 1:
                    right_side_view.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        for node in left_side_view:
            print(node)
        for node in right_side_view:
            print(node)
    