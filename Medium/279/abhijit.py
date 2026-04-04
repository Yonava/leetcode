class Solution:
    def numSquares(self, n: int) -> int:
        """
        step sizes: all the possible perfect squares less than n.

        This then becomes a depth first search problem given all 
        the possible steps that can be taken. 
        steps = arr of all possible step sizes

        for x in steps:
            f(n) = min(f(n), 1 + f(n-x))
        
        """

        steps = []

        x = 1
        while True:
            if x ** 2 <= n:
                steps.append(x ** 2)
                x += 1
            else:
                break
        print('possible steps',steps)

        cache = [float("inf")] * (n + 1)
        for s in steps:
            cache[s] = 1

        for i in range(1,n+1):
            # print(i,cache)
            for s in steps:
                if s <= i:
                    # print(f"{s} is less than {i}")
                    cache[i] = min(cache[i], 1 + cache[i - s])
                else:
                    break
        return cache[-1]