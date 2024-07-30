class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0]

        def climb(number):
            if number == 2:
                ways[0] += 2
                return
            if number == 1:
                ways[0] + 1
                return
            
            
            climb(number - 1)
            climb(number - 2)
        
        climb(n)
        return ways[0]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2
        current = 0
        for i in range(2,n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        
        return current