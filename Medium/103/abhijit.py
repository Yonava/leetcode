# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,root,returnList):
        q = deque()
        q.append(root)
        layer = 0
        
        while q:
            layer_arr = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr != None:
                    layer_arr.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if layer % 2 != 0:
                layer_arr = layer_arr[::-1]
            if layer_arr:
                returnList.append(layer_arr)
            layer += 1




    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        returnList = []
        self.bfs(root,returnList)
        return returnList