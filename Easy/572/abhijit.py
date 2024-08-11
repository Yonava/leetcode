# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recurHelper(self,root,subRoot):
        # once the head is found we can proceed. 
        if root and subRoot == None:
            return False
        if not root and subRoot:
            return False
        if root == None and subRoot == None:
            return True
        if root.val == subRoot.val:
            return True and self.recurHelper(root.left,subRoot.left) and self.recurHelper(root.right,subRoot.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True
        if not root and subRoot:
            return False

        if root and subRoot == None:
            return True
        
        print("current root", root.val)

        if (root.val == subRoot.val):
            print("running search")
            r = root
            sr = subRoot
            found = self.recurHelper(r,sr)
            print("found", found)
            if found:
                return found
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        