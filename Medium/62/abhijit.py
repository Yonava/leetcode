class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        start position: (0,0)
        end position: (m-1,n-1)

        two possible moves are : (0,+1) or (+1,0)
        at every single point, the number of ways to reach that point is initialised to zero.
        now we procedd with our traversal and we keep track of the number of ways we can reach a certain point. 
        and we return the different number of ways we can reach the same point. 
        if we take multiple steps and reach a point, we have traversed a path to that point and we can say it is unique. 
        how do we eliminate the same path. in a sense we don't have to as at each point we can only take 2 paths. and 
        if we have traversed that path, we know that we can't get there again as we can only go down or right. 
        
        let point p = (x,y)
        if we skip to p' = (x + 1, y), there is no way that we can reach (x,y) unless we are at a point before (x,y) as 
        the only possible moves are taking a right or going down. this is the same intuition for why it applies to the (x,y + 1)
        
        OPT((0,0)) = 1
        OPT((x,y)) = OPT((x-1),y) + OPT((x,y-1))
        '''

        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        
        def recurSoln(x,y):
            if x < 0 or y < 0:
                return 0

            if dp[y][x] != 0:
                return dp[y][x]

            left = recurSoln(x-1,y)
            top = recurSoln(x,y-1)

            dp[y][x] = left + top 

            return dp[y][x]
        recurSoln(n-1, m-1)
        print(dp)
        return dp[m-1][n-1]
            
                