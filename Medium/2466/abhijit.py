from collections import deque

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Create a DP array of size high + 1 to store the number of ways to form strings of length i
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        
        # Base case: There's one way to make a string of length 0, which is the empty string
        dp[0] = 1
        
        # Fill the DP array
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i - zero]
            if i - one >= 0:
                dp[i] += dp[i - one]
            dp[i] %= MOD
        
        # The result is the sum of dp[i] for i in range [low, high]
        return sum(dp[low:high + 1]) % MOD