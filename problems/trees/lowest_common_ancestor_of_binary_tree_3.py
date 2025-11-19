# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes 
# p and q in a tree T is the lowest node that has both p and q as descendants 
# (where we allow a node to be a descendant of itself)."

# --------------------------------

# parameters - p: TreeNode, q: TreeNode
# return - LCA: TreeNode

# Q - p and q will always be valid
# Q - can p and q be the same value?

# p=3, q=2, LCA=1
#     1
#   2   3
#  4

# p = 2, q = 4, LCA = 2
#     1
#   2   3
#  4

# p=4, q=5, LCA=2
#     1
#   2   3
#  4 5


# loop up the ladder 
#  if q or p return that value
#  else - check if in visited. if so, return node else add to visited set

# Time - O(n) - n is the num of nodes
# Space - O(n) - n is the num of nodes

class Solution:
    def lowest_common_ancestor(self, p: TreeNode, q: TreeNode) -> TreeNode:
        visited = set()
        if p == q:
            return p
        
        def traverse_up(node: TreeNode, visited: set) -> TreeNode:
            node = node.parent
            while node:
                if node == q or node == p or node in visited:
                    return node
                visited.add(node)       
                node = node.parent
        
        result = traverse_up(p, visited)
        if result:
            return result
        
        return traverse_up(q, visited)
        

# Variant #1
# Char vs. Int


# This problem is literally the exact same thing 







# Variant #2
# Different Inputs

# Given two nodes of a binary tree p and q, and a list of unordered nodes return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
# }
# According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes 
# p and q in a tree T is the lowest node that has both p and q as descendants 
# (where we allow a node to be a descendant of itself)."   

# [1,2,3,4]
# p=1,q=3


# {
#  child: parent
# 4:2
# 2:1
# 3:1
# 1:None 
# }

class solution:
    def lca(self, p: Optional[TreeNode], q: Optional[TreeNode], nodes: List[TreeNode]) -> Optional[TreeNode]:
        visited = set()
        graph = {}

        def _dfs(node, visited) -> Optional[TreeNode]:
            if not node:
                return None
            if node in visited:
                return node
            if node == q or node == p:
                return node
            visited.add(node)
            if node in graph:
                parent = graph.get(node)
                return _dfs(parent, visited)
            return

        for node in nodes:
            if not node:
                continue
            graph[node.right] = node
            graph[node.left] = node
        
        result = _dfs(p, visited)
        if result:
            return result
        
        return _dfs(q, visited)


