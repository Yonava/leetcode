"""
can't break into the same house.
we want to find the maximum number of money we can steal

rob house or don't rob house.

recursive idea:

if we rob house we can add to sum
if we do not rob the house we continue with the sum so far

we only rob the house if the value we get from robbing the next house 
is less than robbing the current house.

then we recurse as we are left with the same choices.

2,1,1,2,3,4

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def valueRobbed(pos: int, amt: int) -> int:
            if pos >= len(nums):
                return amt
            
            skip = valueRobbed(pos + 1, amt)
            rob = valueRobbed(pos + 2,amt + nums[pos])

            if skip > rob:
                return skip 
            else:
                return rob
        
        return valueRobbed(0,0)

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def valueRobbed(pos: int) -> int:
            if pos >= len(nums):
                return 0  # No more houses left to rob
            
            # Option 1: Skip the current house
            skip = valueRobbed(pos + 1)
            
            # Option 2: Rob the current house and move to pos + 2
            rob = nums[pos] + valueRobbed(pos + 2)
            
            # Return the max between robbing or skipping the current house
            return max(skip, rob)
        
        # Start from position 0
        return valueRobbed(0)