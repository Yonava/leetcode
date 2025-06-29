class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        The number of subsequence with a sorted array and not sorted array would be the same. 
        This is because we only care about the minimum and the maximum value.
        """
        nums.sort()
        res = 0
        mod = (10 ** 9 + 7)
        r = len(nums) - 1
        for i, left in enumerate(nums):
            while (left + nums[r]) > target and i <= r:
                r -= 1
            
            if i <= r:
                res += 1 << ( r - i)

        return res % mod