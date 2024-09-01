class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        
        if len(nums) == 3 and sum(nums) != 0:
            return []
     
        seen = set()
        for i in range(len(nums)):
            goal = -1 * nums[i]  # we must find the opposite value pair so sum == 0
            cache = {} # use this to cache
            for index,num in enumerate(nums):
                if index == i:
                    #  do not want to consider the same element twice
                    continue
                diff = goal - num # calculate difference 
                val = cache.get(diff,"not found") # check if difference has been bound

                if num in cache:
                    triplet = tuple(sorted([nums[i], num, cache[num]]))
                    seen.add(triplet)
                else:
                    cache[goal - num] = num
        
        return [list(triplet) for triplet in seen]