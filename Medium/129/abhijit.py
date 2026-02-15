# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        curr_sum = 0

        def explore(root,number):
            nonlocal curr_sum
            if root.left is None and root.right is None:
                number.append(root.val)
                num = 0
                for digit in number:
                    num = num * 10 + digit

                curr_sum += num
                return
            number.append(root.val)

            if root.left:
                explore(root.left, number.copy())
            if root.right:
                explore(root.right,number.copy())
        
        explore(root,[])
        return curr_sum