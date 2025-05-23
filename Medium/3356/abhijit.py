class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def canSatisyZeroArr(arr,seq):
            diff_arr = [0] * (len(arr) + 1)
            for start,end,deduction in seq:
                diff_arr[start] += deduction
                diff_arr[end + 1] -= deduction
            
            for i in range(1,len(diff_arr)):
                diff_arr[i] += diff_arr[i-1]
            
            for i in range(len(arr)):
                if arr[i] > diff_arr[i]:
                    return False
            
            return True

        if canSatisyZeroArr(nums,[]):
            return 0

        l,r = 0, len(queries) - 1
        while r >= l:
            mid = (r + l) // 2
            satisfied  = canSatisyZeroArr(nums,queries[:mid+1])
            if satisfied:
                r = mid - 1
            else:
                l = mid + 1
        
        if l == len(queries):
            return -1
        return l + 1
