class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = [-1]*len(cost)
        def dp(i):
            if i >= len(cost):
                return 0
            if d[i] == -1:
                d[i] = cost[i] + min(dp(i+1),dp(i+2))
            return d[i]

        dp(0)
        return min(d[0], d[1])