# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder and not inorder:
            return None
        root_val = postorder[-1]
        inorder_index = inorder.index(root_val)

        root_node = TreeNode(root_val)
        left_node = self.buildTree(inorder[:inorder_index],postorder[:inorder_index])
        right_node = self.buildTree(inorder[inorder_index+1:], postorder[inorder_index:-1])
        
        root_node.left = left_node
        root_node.right = right_node
        return root_node