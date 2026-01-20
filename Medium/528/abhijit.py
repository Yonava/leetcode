class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.arr = []
        i = 0
        curr_prob_sum = 0
        # appending the cumulative probability helps create "buckets"
        while i < len(w):
            weight = w[i] / self.total
            curr_prob_sum += weight
            self.arr.append((curr_prob_sum,i))
            i += 1

        self.arr.sort(key=lambda x: x[0])

    def pickIndex(self) -> int:
        random_val = random.random()
        l,r = 0, len(self.arr) - 1
        
        while r > l:
            mid = (l + r) // 2
            if self.arr[mid][0] > random_val:
                r = mid 
            else:
                l = mid + 1
        
        return self.arr[l][1]
            
            
"""
bucket logic explained here.

probability = [(0.1 , 0), (0.2, 1), (0.7, 2)]
if we get a value of 0.25. we know it must be in the bucket of 0.2, 1.
because 0.25 is in the range of 0 - 0.3 (0.1 + 0.2)
-> if we do not do the sum we are looking for the exact point of 0.2 rather than the bucket of 0.2
"""