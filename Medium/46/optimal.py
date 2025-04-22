class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        def backtrack(start=0):
            if start == len(nums):
                final.append(nums[:])  # make a copy of the current permutation
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # swap back
        
        backtrack()
        return final
