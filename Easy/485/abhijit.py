class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        max_ones = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            else:
                max_ones = max(max_ones, r - l)
                l, r = r + 1, r + 1
        max_ones = max(max_ones, r - l)
        return max_ones