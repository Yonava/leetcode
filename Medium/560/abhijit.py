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

"""
Try to ask what happens if

prefix[j] = prefix[i] - k
So instead of scanning all j, we just count how many times
prefix[i] - k has appeared before.

instead od doing prefix[i] - prefix[j] == k,
we now look for prefix[i] - k == prefix[j]
"""




# not optimal
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        contiguous subarray: we either start a new subarray or continue the subarray at each point
        this can't be solved with expanding window.
        """
        count = 0

        prefix_sum = []
        sum_so_far = 0
        for i in nums:
            prefix_sum.append(sum_so_far)
            sum_so_far += i
        prefix_sum.append(sum_so_far)
        
        print(prefix_sum)

        for i in range(len(nums)):
            for j in range(i+1):
                if prefix_sum[i+1] - prefix_sum[j] == k:
                    count += 1

    
        return count
