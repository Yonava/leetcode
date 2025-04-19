# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tracker = []
        def inOrderTraversal(node):
            nonlocal tracker
            if node == None:
                return
            left = inOrderTraversal(node.left)
            tracker.append(node.val)
            right = inOrderTraversal(node.right)
        
        inOrderTraversal(root)
        return tracker[k-1]

#  this is a faster way of doing the same traversal. 
# As we know we are going inorder,we just need to find the kth inorder traveral
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.result = None

        def inOrder(node):
            if not node or self.result is not None:
                return
            
            inOrder(node.left)
            
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            inOrder(node.right)