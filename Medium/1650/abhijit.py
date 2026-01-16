class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen = set()
        
        # Climb up from p to the root and record everything
        curr = p
        while curr:
            seen.add(curr)
            curr = curr.parent
            
        # Climb up from q; the first node we see that's in 'seen' is the LCA
        curr = q
        while curr:
            if curr in seen:
                return curr
            curr = curr.parent