class Solution:

    def recurSoln(self,curr_index, curr_subset_str,curr_subset,nums,cache,result):
        if curr_index == len(nums):
            return
        consider = curr_subset_str + str(nums[curr_index])
        ignore = curr_subset_str
        curr_subset.append(nums[curr_index])
        
        if consider not in cache:
            cache.add(consider)
            result.append(curr_subset.copy())
            self.recurSoln(curr_index+1,consider,curr_subset.copy(),nums,cache,result)
        else:
            self.recurSoln(curr_index+1,consider,curr_subset.copy(),nums,cache,result)
        
        curr_subset.pop()
        if ignore not in cache:
            cache.add(ignore)
            result.append(curr_subset.copy())
            self.recurSoln(curr_index+1,ignore,curr_subset.copy(),nums,cache,result)
        else:
            self.recurSoln(curr_index+1,ignore,curr_subset.copy(),nums,cache,result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cache = set()
        result = []
        nums.sort()
        self.recurSoln(0,"",[],nums,cache,result)
        return result