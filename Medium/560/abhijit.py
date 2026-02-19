class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running_sum = 0
        freq = {0: 1}   # important

        for num in nums:
            running_sum += num
            
            if running_sum - k in freq:
                count += freq[running_sum - k]
            
            freq[running_sum] = freq.get(running_sum, 0) + 1

        return count
