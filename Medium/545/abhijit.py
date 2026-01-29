# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]

        def is_leaf(node):
            return node.left is None and node.right is None

        # 1. Left boundary (excluding leaves)
        def add_left_boundary(node):
            curr = node
            while curr:
                if not is_leaf(curr):
                    res.append(curr.val)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right

        # 2. Add all leaves
        def add_leaves(node):
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        # 3. Right boundary (excluding leaves, bottom-up)
        def add_right_boundary(node):
            stack = []
            curr = node
            while curr:
                if not is_leaf(curr):
                    stack.append(curr.val)
                if curr.right:
                    curr = curr.right
                else:
                    curr = curr.left
            while stack:
                res.append(stack.pop())

        add_left_boundary(root.left)
        add_leaves(root.left)
        add_leaves(root.right)
        add_right_boundary(root.right)

        return res
