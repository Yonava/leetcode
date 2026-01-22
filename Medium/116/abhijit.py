"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def traverse(root):
            q = deque()
            q.append(root)
            
            next_val = None
            while q:
                curr_len = len(q)
                for _ in range(curr_len):
                    curr = q.popleft()
                    curr.next = next_val
                    next_val = curr
                    if curr.right and curr.left:
                        q.append(curr.right)
                        q.append(curr.left)
                next_val = None
                
        if not root:
            return None
        traverse(root)
        return root




    
        