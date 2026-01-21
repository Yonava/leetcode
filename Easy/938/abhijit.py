# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def explore(root):
            nonlocal total
            if root == None:
                return
            elif root.val > high:
                explore(root.left)
            elif root.val < low:
                explore(root.right)
            else:
                total += root.val
                explore(root.left)
                explore(root.right)
        
        explore(root)
        return total
                