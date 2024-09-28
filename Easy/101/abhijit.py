# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        for the tree to be symmetric, the left tree from the root must be a mirror image of the right tree

        - we could a inorder traversal (L, self, R) for the left tree
        - a post order traversal (R, self, L) for the right subtree
        - We compare nodes as we see them and if there is a discrepancy we return False
        '''

        if not root:
            return True
        if root.right == root.left == None:
            return True

        left_tree = root.left
        right_tree = root.right

        def recurHelper(left,right):
            if left == right == None:
                return True
            if left == None and right:
                return False
            if right == None and left:
                return False
            left_val = recurHelper(left.left,right.right)
            curr = left.val == right.val
            right_val = recurHelper(left.right, right.left)

            return left_val and curr and right_val

        return recurHelper(left_tree, right_tree)
        