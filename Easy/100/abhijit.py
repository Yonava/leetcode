# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recursiveCheck(self,p,q):
        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if q == None and p != None:
            return False

        if p.val != q.val:
            return False
        
        left_val = self.recursiveCheck(p.left,q.left)
        right_val = self.recursiveCheck(p.right,q.right)

        return left_val and right_val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recursiveCheck(p,q)