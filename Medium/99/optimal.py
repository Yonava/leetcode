# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        # List to store the in-order traversal of the tree
        inorder_nodes = []
        
        # Perform an in-order traversal and store the nodes in a list
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            inorder_nodes.append(node)  # Store the node in the list
            inorder_traversal(node.right)
        
        # Step 1: Traverse the tree and store the nodes in a list
        inorder_traversal(root)
        
        # Step 2: Find the two nodes that are out of order
        first_node, second_node = None, None
        for i in range(len(inorder_nodes) - 1):
            if inorder_nodes[i].val > inorder_nodes[i + 1].val:
                if not first_node:
                    first_node = inorder_nodes[i]   # First violation
                second_node = inorder_nodes[i + 1]  # Keep updating the second node
        
        # Step 3: Swap the values of the two misplaced nodes
        if first_node and second_node:
            first_node.val, second_node.val = second_node.val, first_node.val
