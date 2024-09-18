"""
Key Intuition:
The longest paths in a tree are often between leaves. The core of the tree (the "centroid") is where the Minimum Height Trees are rooted. Instead of calculating heights from every node, we iteratively remove the leaves until we're left with 1 or 2 central nodes.

Optimized Approach:
Leaves are nodes with only one connection (degree 1).
Remove leaves layer by layer. In each iteration, the new leaves are the neighbors of the previously removed leaves.
Continue this process until the remaining nodes are either 1 or 2 (these are the roots of the Minimum Height Trees).

"""
from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Build the graph
        adjacency_list = defaultdict(set)
        for u, v in edges:
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)
        
        # Find all leaves (nodes with only one connection)
        leaves = deque([i for i in range(n) if len(adjacency_list[i]) == 1])
        
        # Iteratively remove leaves until we're left with 1 or 2 nodes
        while n > 2:
            leaves_size = len(leaves)
            n -= leaves_size
            
            for _ in range(leaves_size):
                leaf = leaves.popleft()
                # There should be exactly one neighbor for a leaf
                neighbor = adjacency_list[leaf].pop()
                adjacency_list[neighbor].remove(leaf)
                
                if len(adjacency_list[neighbor]) == 1:
                    leaves.append(neighbor)
        
        # The remaining nodes are the roots of the Minimum Height Trees
        return list(leaves)
