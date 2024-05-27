# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recursiveHelper(self,root):
        l_height = self.recursiveHelper(root.left) if root.left else 0
        r_height = self.recursiveHelper(root.right) if root.right else 0

        print("current_node", root.val)
        print("left_val", l_height)
        print("right_val", r_height)
        if abs(l_height - r_height) > 1:
            raise Exception("tree not balanced")
        return max(l_height,r_height) + 1

    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root == None):
            return True
        try:
            val = self.recursiveHelper(root)
            return True
        except:
            return False