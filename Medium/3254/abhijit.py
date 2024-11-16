class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
            we have to find the maximum bumber of a subarray (if it is sorted)
            -1 if it not sorted


            brute force approach:
            O(nk)
            we can carry out a window based approach (traverse each window of size k)
            -> check if it is sorted  (O(k) traversal)
            -> return the end integer if we reach the end of the inner window traversal otherwise return 1
            
        """
        # produce the right sized windows
        start_window, end_window = 0, 0 + k-1
        rtn_arr = []
        while start_window < len(nums) - k + 1:
            i = start_window + 1
            reject = False
            while i <= end_window:
                # carry out stuff
                if nums[i - 1] + 1 != nums[i]:
                   rtn_arr.append(-1)
                   reject = True
                   break
                i += 1
            if not reject and i - 1 == end_window:
                rtn_arr.append(nums[end_window])
            start_window +=1
            end_window +=1 
    
        return rtn_arr


# clean sliding window solution (I could not code it out but I had the rough idea)
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """Find the Power of K-Size Subarrays"""
        # Skip if k is 1
        if k == 1:
            return nums
            
        n = len(nums)
        result = []
        left = 0
        right = 1
        
        while right < n:
            # Check if current sequence is not consecutive
            is_not_consecutive = nums[right] - nums[right-1] != 1
            
            if is_not_consecutive:
                # Mark invalid sequences
                while left < right and left + k - 1 < n:
                    result.append(-1)
                    left += 1
                left = right
            # Found valid k-length sequence
            elif right - left == k - 1:
                result.append(nums[right])
                left += 1
                
            right += 1
            