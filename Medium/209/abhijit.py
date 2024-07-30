class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        res = float('inf')
        l,r = 0,0
        while r < len(nums):
            sum += nums[r]
            r +=1
            while sum >= target:
                res = min(res, r - l)
                sum -= nums[l]
                l += 1
        
        if res == float('inf'):
            return 0
        else:
            return res