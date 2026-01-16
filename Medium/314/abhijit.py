from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # tracker[column_index] = [list of values]
        tracker = defaultdict(list)
        # queue stores (node, column_index)
        queue = deque([(root, 0)])
        
        # Track min and max to avoid sorting keys at the end
        min_col = max_col = 0

        while queue:
            node, col = queue.popleft()
            
            if node:
                tracker[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                # Left child goes to col - 1
                if node.left:
                    queue.append((node.left, col - 1))
                # Right child goes to col + 1
                if node.right:
                    queue.append((node.right, col + 1))
        
        # Build the result using the range of columns we found
        return [tracker[i] for i in range(min_col, max_col + 1)]

"""
I was originally using string as keys to get the columns.
we add a "r" when taking a step to the right.
we add a "l" when taking a step to the left.

however, that is similar to using numbers. +1 for right and -1 for left. 
this is useful as we can sort on the index val!!!! (follow left to right order)
"""
