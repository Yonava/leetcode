class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 1
        max = float("-inf")
        sum = 0
        while end < len(prices):
            print("curr window & max", prices[start:end+1], max, f"{start}-{end}")
            if prices[end] < prices[start]:
                start += 1
            else:
                profit = prices[end] - prices[start]
                if profit > max:
                    max = profit
                    end +=1
                else:
                    sum += max
                    max = float("-inf")
                    start = end

        if max != float("-inf"):
            sum += max
        return sum