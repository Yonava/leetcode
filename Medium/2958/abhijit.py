class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        counter = {}
        l = 0
        max_len = 0
        
        for r in range(len(nums)):
            counter[nums[r]] = counter.get(nums[r], 0) + 1
            
            # Shrink window while invalid
            while counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1
            
            # Window is now valid, update max length
            max_len = max(max_len, r - l + 1)
        
        return max_len