# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveHelper(root):
        if root == None:
            # final swap and end recursion
           return None
        else:
            l,r = root.left,root.right
            new_l = Solution.recursiveHelper(l)
            new_r = Solution.recursiveHelper(r)
            root.left = new_r
            root.right = new_l
            return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        algorithm: recursively traverse the tree 
        until we reach the second last row then we just reassign pointers
        the complexity should be o(n)
        '''
        new_root = Solution.recursiveHelper(root)
        return new_root
        
        

