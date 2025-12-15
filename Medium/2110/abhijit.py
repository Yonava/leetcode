class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l, r = 0, 1
        period_cnt = 0
        while r <= len(prices):
            if  r != len(prices) and prices[r] == prices[r-1] - 1:
                # expand the window
                r += 1
            else:
                # we want to calculate all the periods
                window_length = r - l

                # add periods less than length of 1
                for x in range(window_length - 1,1, -1):
                    period_cnt += (window_length - x + 1)
                # add all the individual dates 
                period_cnt += window_length

                # adding the actual entire window.
                if window_length > 1:
                    period_cnt += 1

                l , r = r , r + 1

        return period_cnt



class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l, r = 0, 1
        period_cnt = 0
        while r <= len(prices):
            if  r != len(prices) and prices[r] == prices[r-1] - 1:
                # expand the window
                r += 1
            else:
                # we want to calculate all the periods
                window_length = r - l

                period_cnt += window_length * (window_length + 1) // 2
                l , r = r , r + 1

        return period_cnt
