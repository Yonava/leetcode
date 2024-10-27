class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        let the OPT be the maximum product so far. The subarray must be contiguous and have no breaks within them
        OPT(0) = nums[0]
        OPT(j) = max(val(j) * OPT(j-1), OPT(j))
        '''
        memo = [None] * len(nums) # (positive, negative)]
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
    
''' Abhijit iterative'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        let the OPT be the maximum product so far. The subarray must be contiguous and have no breaks within them
        OPT(0) = nums[0]
        OPT(j) = max(val(j) * OPT(j-1), OPT(j))
        '''
        memo = [None] * len(nums) # (positive, negative)
        MAXPROD = float(-inf)
        for index, num in enumerate(nums):
            if index == 0:
                if num > MAXPROD:
                    MAXPROD = num
                memo[index] = num,num
            else:
                maxProd, minProd = memo[index -1]
                maxMult = nums[index] * maxProd
                minMult =  nums[index] * minProd
                maxSoFar = max(maxMult, minMult, nums[index])
                minSoFar = min(maxMult, minMult, nums[index])
                if maxSoFar > MAXPROD:
                    MAXPROD = maxSoFar
                memo[index] = maxSoFar,minSoFar
            
        return MAXPROD

''' Suggested solution'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = nums[0]
        
        for n in nums:
            vals = (n, n * curMax, n * curMin)
            curMax, curMin = max(vals), min(vals)
			
            res = max(res, curMax)
            
        return res