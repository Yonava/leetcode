from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        l = 0
        max_window = 0
        
        for r in range(n):
            # Shrink window until condition is satisfied
            while nums[r] > k * nums[l]:
                l += 1
            
            # Update largest valid window
            max_window = max(max_window, r - l + 1)
        
        return n - max_window
