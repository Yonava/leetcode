"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        prev = None # this is the global pointer to maintain state 
        head = None
    

        def explore(root):
            nonlocal prev, head
            if root is None:
                return
            if root.left:
                explore(root.left)
            
            if prev == None:
                #  prev is only none when we are exploring the left most value
                head = root
                prev = root
            
            if prev != root:
                prev.right = root
                root.left = prev
                prev = root

            if root.right:
                explore(root.right)
            
            return

        if not root:
            return
        explore(root)
        head.left = prev
        prev.right = head

        return head