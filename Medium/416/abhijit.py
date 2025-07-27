class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2 
        memo = {}
        
        def canReachTarget(currSum, currIndex):
            if currSum == target:
                return True
            
            if currIndex >= len(nums) or currSum > target:
                return False
            
            if (currIndex, currSum) in memo:
                return memo[(currIndex, currSum)]
            
            include = canReachTarget(currSum + nums[currIndex], currIndex + 1)
        
            exclude = canReachTarget(currSum, currIndex + 1)
            
            memo[(currIndex, currSum)] = include or exclude
            return memo[(currIndex, currSum)]
        
        return canReachTarget(0, 0)
