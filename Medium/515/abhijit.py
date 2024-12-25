# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        rtnList = []
        q = deque()
        q.append(root)
        while q:
            maxVal = float("-inf")
            
            for i in range(len(q)):
                curr = q.popleft()
                if curr is None:
                    # handle edge case of None values
                    continue
                maxVal = max(curr.val,maxVal)
                q.append(curr.left)
                q.append(curr.right)
            
            if maxVal != float("-inf"):
                rtnList.append(maxVal)

        return rtnList

