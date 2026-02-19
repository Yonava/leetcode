class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def helper(node, parent):
            if not node:
                return
            node.parent = parent
            helper(node.left, node)
            helper(node.right, node)
            
        helper(root, None)
        ans = []
        seen = set()
        
        def trav(node, dist):
            if not node or node in seen or dist > k:
                return
            seen.add(node)
            if dist == k:
                ans.append(node.val)
                return
            if dist+1 <= k:
                trav(node.parent, dist+1)
                trav(node.left, dist+1)
                trav(node.right, dist+1)
        
        trav(target, 0)
        return ans