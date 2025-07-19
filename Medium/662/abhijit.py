# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            q = deque()
            q.append((root,0))
            widest = 0
            while q:
                smallest = float("inf")
                largest = float("-inf")
                for _ in range(len(q)):
                    node, index = q.popleft()
                    if node.left:
                        q.append((node.left, 2 * index + 1))
                    if node.right:
                        q.append((node.right, 2 * index + 2))
                    smallest = min(smallest, index)
                    largest = max(largest, index)
                widest = max(widest,largest - smallest + 1)
            
            return widest
        
        return bfs(root)
        