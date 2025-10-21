# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


class Solution:
    def copy_graph(self, node: Optional['ListNode']) -> Optional['ListNode']:
        def _dfs_clone(node: Optional['ListNode']):
            if not node:
                return None
            if node in mapp:
                return mapp[node]
            
            copy = Node(node.val)
            mapp[node] = copy
            for neigbor in node.neighbors:
                copy.neighbors.append(_dfs_clone(neighbor))
            
            return copy
        
        mapp = {}
        copy = _dfs_clone(node)

        return copy
