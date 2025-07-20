# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            q = deque()
            q.append(root)
            max_sum, max_level = float("-inf"), 0
            currLevel = 0
            while q:
                currSum = 0
                currLevel += 1
                for _ in range(len(q)):
                    currNode = q.popleft()
                    currSum += currNode.val
                    if currNode.left:
                        q.append(currNode.left)
                    if currNode.right:
                        q.append(currNode.right)
                print(currSum,max_sum)
                if currSum > max_sum:
                    max_sum = currSum
                    max_level = currLevel
            return max_level
        
        return bfs(root)