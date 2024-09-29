# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found_leaf = None
        def recurSolution(root,prevSum):
            nonlocal found_leaf
            if root == None and prevSum != targetSum:
                return False
            elif root == None and prevSum == targetSum:
                print("found one end child")
                return True

            currSum = prevSum + root.val    
            left_child = recurSolution(root.left,currSum)
            right_child = recurSolution(root.right,currSum)

            if left_child and right_child:
                found_leaf = True

            return False 
        
        if not root:
            return False
        recurSolution(root,0)
        return found_leaf if found_leaf else False
            