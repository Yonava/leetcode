from typing import (
    List,
)

class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # write your code here
        l,r = 0,0
        zero_pos = -1

        max_ones = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and zero_pos == -1:
                zero_pos = r
                r += 1
            else:
                window_length = r - l
                max_ones = max(max_ones, window_length)
                l = zero_pos + 1
                zero_pos = -1

        return max_ones      

