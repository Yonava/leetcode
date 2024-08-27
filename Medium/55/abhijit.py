class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        
        for i in range(len(nums)):
            # If we are at a point where we cannot proceed
            if i > farthest:
                return False
            
            # Update the farthest we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or exceed the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        return False