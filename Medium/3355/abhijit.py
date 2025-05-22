class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        calculations = [0] * (len(nums) + 1)

        for start, end in queries:
            calculations[start] += 1
            calculations[end + 1] -= 1

        for i in range(1,len(calculations)):
            calculations[i] += calculations[i-1]
        
        for i in range(len(nums)):
            if nums[i] > calculations[i]:
                return False
        return True
