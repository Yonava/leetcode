# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recurSoln(self,root,min,max):
        l,r = root.left, root.right
        
        if l == None and r == None:
            return True
        elif l == None:
            if root.val < r.val and r.val < max:
                return True and self.recurSoln(r,root.val,max)
            else:
                return False
        elif r == None:
            if root.val > l.val and l.val > min:
                return True and self.recurSoln(l,min,root.val)
            else:
                return False
        else:
            if root.val < r.val and r.val < max  and root.val > l.val and l.val > min:
                return True and self.recurSoln(r,root.val,max) and self.recurSoln(l,min,root.val)
            else:
                return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurSoln(root,float("-inf"),float("inf"))
        