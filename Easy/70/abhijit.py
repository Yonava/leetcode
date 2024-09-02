class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def recurHelper(curr):
            if curr == 0:
                memo[0] = 1
                return 1
            elif curr < 0:
                return 0
            elif memo[curr] != -1:
                return memo[curr]

            n_min_one = recurHelper(curr - 1)
            n_min_two = recurHelper(curr - 2)
            
            memo[curr] = n_min_one + n_min_two
            
            return n_min_one + n_min_two
            
        recurHelper(n)

        return memo[-1]
            

