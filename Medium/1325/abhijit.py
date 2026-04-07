# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def recurse(node):
            if node.left is None and node.right is None:
                if node.val == target:
                    return None
                else:
                    return node
            
            node.left = recurse(node.left) if node.left else None
            node.right = recurse(node.right) if node.right else None
            if node.left is None and node.right is None:
                if node.val == target:
                    return None
            return node
        return recurse(root)