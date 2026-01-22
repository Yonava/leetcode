class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        tracker = nums.copy()

        max_val = float("-inf")

        for i in range(len(nums)):
            for j in range(0,i):
                if nums[i] + 1 != nums[j] and nums[i] - 1 != nums[j]:
                    tracker[i] = max(tracker[i], nums[i] + tracker[j]) 
            max_val = max(max_val, tracker[i])
    
        return max_val
            
        