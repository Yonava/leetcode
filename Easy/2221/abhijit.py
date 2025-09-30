class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        curr = nums
        new = []
        for rep in range(len(nums) -1):
            i = 0
            while i < len(curr):
                if i == len(curr) - 1:
                    break
                else:
                    new.append((curr[i] + curr[i + 1]) % 10)
                    i += 1
            curr = new
            new = []
        return curr[0]
        