class Solution:
    def minCost(self, colours: str, neededTime: list[int]) -> int:
        if len(colours) < 2:
            return 0
        
        time_taken = 0
        l, r = 0, 1

        while r < len(colours):
            if colours[l] == colours[r]:
                time_taken += min(neededTime[l], neededTime[r])
                
                neededTime[r] = max(neededTime[l], neededTime[r])
            
            l += 1
            r += 1
        
        return time_taken