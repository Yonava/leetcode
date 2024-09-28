# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if root == None:
            return
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        self.inorder(root,output)

        return output