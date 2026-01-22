class Solution:
    def findMaxLength(self, nums):
        # balance -> first index where this balance occurred
        first_seen = {0: -1}
        
        balance = 0
        max_len = 0
        
        for i, v in enumerate(nums):
            # map 0 -> -1, 1 -> +1
            if v == 0:
                balance -= 1
            else:
                balance += 1
            a
            if balance in first_seen:
                max_len = max(max_len, i - first_seen[balance])
            else:
                first_seen[balance] = i
        
        return max_len
