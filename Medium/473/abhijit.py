class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        since we cannot break a match stick into smaller pieces, 
        we should try to use the longer match sticks to form edges first. 
        The idea being that there might be smaller match sticks available that might help with it.
        it would make sense to sort matchsticks first. 
        we can then find a set of values that equal to the length we are trying to find, 
        if we can find 4 such sets then we can create a square (4 equal sum  subsets)
        -> we want to divide it into groups of 4
        """
        
        # interesting pruning idea. Did not think of this
        total = sum(matchsticks) 
        if total % 4 != 0:
            return False
        target = total // 4


        matchsticks.sort(reverse=True) # this helps speed up the greedy and prune quickly

        def dfs(i,square):
            if i == len(matchsticks):
                return square[0] == square[1] == square[2] == square[3]


            if square[0] + matchsticks[i] <= target and dfs(i + 1, (square[0] + matchsticks[i], square[1], square[2], square[3])):
                return True
    
            if square[1] + matchsticks[i] <= target and dfs(i + 1, (square[0], square[1] + matchsticks[i], square[2], square[3])):
                return True
    
            if square[2] + matchsticks[i] <= target and dfs(i + 1, (square[0], square[1], square[2] + matchsticks[i], square[3])):
                return True

            if square[3] + matchsticks[i]  <= target and dfs(i + 1, (square[0], square[1], square[2], square[3] + matchsticks[i])):
                return True
            
            return False
        
        return dfs(0,(0,0,0,0))