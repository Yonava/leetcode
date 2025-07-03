class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            val = count.get(num, -1)
            if val == -1:
                count[num] = 1
            else:
                return num
        
        return -1
    
# cyclic sort solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # TODO: Write your code here
        i = 0
        while i < len(nums):
            val = nums[i]
            if i == (val - 1):
                i += 1
                continue
            elif nums[val - 1] == val:
                # before swapping the condition is satisfied
                return val
            else:
                nums[i] = nums[val -1]
                nums[val - 1] = val