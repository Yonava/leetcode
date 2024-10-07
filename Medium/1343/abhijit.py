class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) == k:
            return 1 if sum(arr) >= threshold * len(arr) else 0
        l,r = 0,k
        currSum = sum(arr[l:r])
        
        MAXSUM = threshold * k
        sub_arr_count = 0 

        while r < len(arr):
            if currSum >= MAXSUM:
                sub_arr_count += 1
        
            currSum += arr[r]
            r += 1
            currSum -= arr[l]
            l += 1    

        if currSum >= MAXSUM:
            sub_arr_count +=1

        return sub_arr_count