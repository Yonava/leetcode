class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        arr = sorted(nums)
        increments = 0
        for i in range(1,len(nums)):
            if arr[i -1] >= arr[i]:
                diff = abs(arr[i-1] - arr[i])
                arr[i] += diff + 1
                increments += diff + 1
        
        return increments