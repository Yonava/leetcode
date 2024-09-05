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
        if not node:
            return None
        adjacency_list = {}

        def cloneBFS(node):
            if node.val not in adjacency_list:
                # create node if node doesn't exist
                adjacency_list[node.val] = Node(node.val,None)
            
            for neighbour in node.neighbors:
                if neighbour.val in adjacency_list:
                    adjacency_list[node.val].neighbors.append(adjacency_list[neighbour.val])
                else:
                    rtn_node = cloneBFS(neighbour)
                    adjacency_list[node.val].neighbors.append(rtn_node)
            
            return adjacency_list[node.val]
        
        return cloneBFS(node)



        dfs(node,None)
        return adjacency_list.values()
                    
                    
            