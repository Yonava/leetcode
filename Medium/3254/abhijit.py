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


