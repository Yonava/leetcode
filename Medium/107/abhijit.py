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
        
        while q:
            curr_level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr != None:
                    curr_level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if curr_level:
                returnList.append(curr_level)


    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        returnList = []
        self.bfs(root,returnList)
        return returnList[::-1]
        