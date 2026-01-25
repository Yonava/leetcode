class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(k):
            if k == 0:
                return 0
            
            tracker = {}
            l = 0
            count = 0
            
            for r in range(len(nums)):
                tracker[nums[r]] = tracker.get(nums[r], 0) + 1
                
                # Shrink window while we have more than k distinct
                while len(tracker) > k:
                    tracker[nums[l]] -= 1
                    if tracker[nums[l]] == 0:
                        del tracker[nums[l]]
                    l += 1
                
                # All subarrays ending at r with start from l to r are valid
                count += r - l + 1
            
            return count
        
        return atMostK(k) - atMostK(k - 1)