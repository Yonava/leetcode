class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = None
        max_profit = None
        for val in prices:
            # O(n)
            if minSoFar == None:
                minSoFar = val
            if val < minSoFar:
                minSoFar = val
            profit = val - minSoFar
            
            if max_profit == None:
                max_profit = profit
            
            elif profit > max_profit:
                max_profit = profit

        
        return max_profit