class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        cache = {}

        def distribute(available,depth):
            if (available,depth) in cache:
                return cache[(available,depth)]
            if depth == 3:
                return 0 if available else 1
            
            possible_ways = 0

            for i in range(min(available, limit) + 1):
                possible_ways += distribute(available - i, depth + 1)
            
            print("for", (available,depth), possible_ways, "of distribution")
            cache[(available,depth)] = possible_ways

            return possible_ways

        
        return distribute(n,0)
        