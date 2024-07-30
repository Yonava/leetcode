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
    
    