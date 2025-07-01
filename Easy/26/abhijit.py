class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currVal, currPos = 0, 1
        while currPos < len(nums):
            if nums[currPos] != nums[currVal]:
                nums[currPos], nums[currVal + 1] = nums[currVal + 1], nums[currPos]
                currPos += 1
                currVal += 1
            else:
                currPos += 1
        
        return currVal + 1