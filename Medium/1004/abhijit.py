from collections import deque
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zero_count = 0
        max_ones = 0
        
       
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                
                l += 1
            
            current_window_length = r - l + 1
            max_ones = max(max_ones, current_window_length)
            
        return max_ones