# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        
        def recurHelper(root, prevPath, prevSum):
            if root == None and prevSum == targetSum:
                return True
            elif root == None:
                return False
            print('currNode',root.val,prevPath)
            currSum = prevSum + root.val
            
            # add current node to path
            newPath = prevPath.copy()
            newPath.append(root.val)

            left = recurHelper(root.left,newPath,currSum)
            right = recurHelper(root.right,newPath,currSum)

            if left and right:
                all_paths.append(newPath)
            return 
        
        if not root:
            return []
        recurHelper(root,[],0)
        return all_paths