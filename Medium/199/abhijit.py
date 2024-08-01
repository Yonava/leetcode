# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def recurHelper(self,node,height,hashset):
        if node == None:
            return
        if hashset.get(height, "False") == "False":
            hashset[height] = node.val
        self.recurHelper(node.right,height + 1, hashset)
        self.recurHelper(node.left, height + 1, hashset)


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        hashSet = {}
        self.recurHelper(root,0,hashSet)
        return hashSet.values()