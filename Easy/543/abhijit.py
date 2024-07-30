# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0 # stores the maximum diameter calculated

    def depth(self, node):
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0

        self.diameter = max(self.diameter, left + right)

        return 1 + max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        algorithm. 
        at each tree:
        - find the node with the maximum depths from the right tree and the maximum depth of the left tree
        the longest path would be from the. and we recursively pass it up     

        - we reach end of the tree
        - as we recurse back up, we get the depth of the left side and the right side. we keep adding these sums and comparing with the max value
        ''' 
  
        self.depth(root)
        return self.diameter