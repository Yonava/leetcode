class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        tracker = {0: 1}
        multiplier = x if n > 1 else 1/x

        if n >= 1:
            tracker[1] = x
        else:
            tracker[1] = 1/x
    
    
        def calculate(x):
            if x in tracker:
                return tracker[x]
            else:
                m = x // 2
                if m * 2 == x:
                    val =  calculate(m) * calculate(m)
                    tracker[x] = val
                else:
                    # this is a neat trick to reduce the number of calls. 
                    val = calculate(m) * calculate(m) * multiplier
                    tracker[x] = val
                
                return tracker[x]
        
        return calculate(n if n >= 1 else -1 * n)