# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_traversal = []
        q = deque([root])

        while q:
            # Determine the number of nodes at the current level
            level_size = len(q)
            current_level = []

            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)

                # Add children to the queue for the next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Append the current level to the result
            level_traversal.append(current_level)

        return level_traversal