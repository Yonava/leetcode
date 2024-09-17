class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        big_coins_first = sorted(coins, reverse=True)

        seen = {}
        MAX_INT = 2147483647  
        minCoin = MAX_INT
        def dfs(sumTilNow,coinCount):
            nonlocal minCoin

            if sumTilNow > amount:
                return

            if sumTilNow == amount:
                print("foundCoin",coinCount)
                minCoin = min(minCoin,coinCount)
                return

            # If we have already visited this sum with fewer or equal coins, skip
            if sumTilNow in seen and seen[sumTilNow] <= coinCount:
                return
            # Mark the current state as seen with the current coin count
            seen[sumTilNow] = coinCount

            # Explore further by adding each coin
            for coin in big_coins_first:
                dfs(sumTilNow + coin, coinCount + 1)
                    
                
    
        dfs(0,0)
        
        return -1 if minCoin == MAX_INT else minCoin
    


                    
            



        return 0