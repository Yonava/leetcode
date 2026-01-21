# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        def totalSum(root):
            if root is None:
                return 0
            return root.val + totalSum(root.left) + totalSum(root.right)
        
        total = totalSum(root)
        product = float("-inf")

        def findMaxProduct(root):
            nonlocal total, product
            if root is None:
                return 0
            else:
                curr_sum = root.val + findMaxProduct(root.left) + findMaxProduct(root.right)
                diff = total - curr_sum
                product = max(diff * curr_sum, product)
                return curr_sum
        
        findMaxProduct(root)

        return product % (10**9 + 7)
