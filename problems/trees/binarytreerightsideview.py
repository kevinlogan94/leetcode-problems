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
    def rightsideview(self, root: Optional['Node']) -> List[int]:
# 1. define our BFS submethod
#   define our set
#   traverse through our tree horizontally from right to left. keep tabs on our set of rows.
        def _bfs_traverse_tree(node: Optional['Node']) -> None:
            if not node:
                return None

            rows = set()
            queue = [(node, 1)]

            while queue:
                curr, row = queue.pop(0)
                if not row in rows:
                    self.result.append(curr.val) 
                    rows.add(row)
                
                if curr.right:
                    queue.append((curr.right, row + 1))
                if curr.left:
                    queue.append((curr.left, row + 1))

        self.result = []
        _bfs_traverse_tree(root)
        return self.result
                



# 2.
# declare variables - result array
# call BFS method
# return result array

