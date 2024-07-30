# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recurSoln(self, root):
        if root == None:
            # reached the end of the tree
            return 0
        return 1 + max(self.recurSoln(root.left), self.recurSoln(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurSoln(root)