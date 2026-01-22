class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tracker = [1] * len(nums)
        max_length = 1


        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    tracker[i] = max(tracker[i], tracker[j] + 1)
            
            max_length = max(max_length, tracker[i])
        
        return max_length
