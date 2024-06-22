class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur_arr, iter_arr):
            if len(cur_arr) == len(nums):
                res.append(cur_arr)
                return
            
            for val in iter_arr:
                new_iter_arr = iter_arr.copy()
                new_iter_arr.remove(val)
                
                new_curr_arr = cur_arr.copy()
                new_curr_arr.append(val)
                
                backtrack(new_curr_arr,new_iter_arr)        
        
        backtrack([],nums)

        return res