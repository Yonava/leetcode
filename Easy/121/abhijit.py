class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        best = 0

        while end < len(prices) and start <= end:
            if prices[end] >= prices[start]:
                best = max(prices[end] - prices[start], best)
                end +=1
            else:
                start +=1
            
        return best
            