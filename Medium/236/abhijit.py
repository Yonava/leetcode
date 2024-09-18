class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent_node = None
        def recurHelper(node):
            nonlocal parent_node
            if node == None:
                return False

            left = recurHelper(node.left)
            right = recurHelper(node.right)
            
            isCurrNode = False

            if node.val == p.val or node.val == q.val:
                isCurrNode = True
        
            if left and right:
                parent_node = node
                return True
            elif isCurrNode and (left or right):
                parent_node = node
                return True
            else:
                return isCurrNode or left or right  

        recurHelper(root)
        return parent_node