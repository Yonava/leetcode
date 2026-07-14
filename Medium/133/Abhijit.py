"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:    
        if node is None:
            return None

        seen = {}
        def recurse(n):
            nonlocal seen
            clone = Node(n.val)
            seen[n] = clone

            for nbr in n.neighbors:
                if nbr not in seen:
                    recurse(nbr)

        recurse(node)
    
        visited = set()
        def copy(n):
            nonlocal seen, visited
            clone = seen[n]
            visited.add(n)
            for nbr in n.neighbors:
                if nbr not in visited:
                    clone.neighbors.append(seen[nbr])
                    copy(nbr)
                else:
                    clone.neighbors.append(seen[nbr])


        copy(node)

        return seen[node]

"""
improvement. Improving the solution by reducing the space complexity and reducing the number of passes
overall complexity is still o(v+e) but we are reducing the space complexity by not storing the entire graph in memory 
and reducing the number of passes to 1
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Maps: Original Node -> Cloned Node
        cloned_map = {}
        
        def dfs(curr_node):
            # If we already cloned this node, just return its clone
            if curr_node in cloned_map:
                return cloned_map[curr_node]
            
            # 1. Create the clone for the current node
            clone = Node(curr_node.val)
            cloned_map[curr_node] = clone
            
            # 2. Recursively clone and attach all neighbors
            for nbr in curr_node.neighbors:
                clone.neighbors.append(dfs(nbr))
                
            return clone

        return dfs(node)