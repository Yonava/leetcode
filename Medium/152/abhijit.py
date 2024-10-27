class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        let the OPT be the maximum product so far. The subarray must be contiguous and have no breaks within them
        OPT(0) = nums[0]
        OPT(j) = max(val(j) * OPT(j-1), OPT(j))
        '''
        memo = [None] * len(nums) # (positive, negative)
        def maxProductSoFar(index):
            if index == 0:
                memo[index] = nums[0],nums[0]
                return nums[0], nums[0]
            if memo[index] != None:
                return memo[index]
            
            maxPossible, minPossible = maxProductSoFar(index-1)
            maxMult = nums[index] * maxPossible
            minMult =  nums[index] * minPossible
            maxSoFar = max(maxMult, minMult, nums[index])
            minSoFar = min(maxMult, minMult, nums[index])
            memo[index] = maxSoFar, minSoFar

        for n in range(len(nums)):
            maxProductSoFar(n)
        
        return max([x[0] for x in memo])