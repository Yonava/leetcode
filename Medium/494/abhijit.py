#abhijit
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        
        def recurHelper(index,sum,possibleChoices):
            if index == 0:
                dp[(index,sum)] = 1 if sum == 0 else 0
                return 1 if sum == 0 else 0
            
            if (index,sum) in dp:
                return dp[(index,sum)]

            for i in range(len(possibleChoices)):
                val = possibleChoices[i]
                newChoices = possibleChoices[:i] + possibleChoices[i+1:]
                add = recurHelper(index - 1, sum - val , newChoices)
                minus = recurHelper(index -1 , sum + val, newChoices)
                
                dp[(index, sum)] = add + minus
                return add + minus
        
        return recurHelper(len(nums),target,nums)


#Optimal
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def recurHelper(index, sum):
            if index == len(nums):
                return 1 if sum == target else 0
            
            if (index, sum) in dp:
                return dp[(index, sum)]
            
            # Explore adding and subtracting the current number
            add = recurHelper(index + 1, sum + nums[index])
            minus = recurHelper(index + 1, sum - nums[index])
            
            dp[(index, sum)] = add + minus
            return dp[(index, sum)]
        
        return recurHelper(0, 0)
