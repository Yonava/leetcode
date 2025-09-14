# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def optimiseSearch(root):
            if root is None:
                return (0,0)
            
            left_skip, left_pick = optimiseSearch(root.left)
            right_skip, right_pick = optimiseSearch(root.right)
            
            root_pick = left_skip + root.val + right_skip
            root_skip = max(left_pick + right_pick, left_skip + right_skip, left_pick + right_skip, left_skip + right_pick)
            return (root_skip, root_pick)

        r_s, r_p = optimiseSearch(root)
        print(r_s, r_p)
        return max(r_s, r_p)