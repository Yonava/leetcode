class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_val = 0
        for index,val in enumerate(nums):
            if max_val < 0:
                # edging fr
                return False
                
            if val > max_val:
                max_val = max(val,max_val)

            max_val -= 1
        return True