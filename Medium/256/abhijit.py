class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        r = [costs[0][0]]
        b = [costs[0][1]]
        g = [costs[0][2]]

        for i in range(1, len(costs)):
            r.append( min(b[i-1], g[i-1]) + costs[i][0] )
            b.append( min(g[i-1], r[i-1]) + costs[i][1] )
            g.append( min(b[i-1], r[i-1]) + costs[i][2] )
        
        return min(r[-1], b[-1], g[-1])