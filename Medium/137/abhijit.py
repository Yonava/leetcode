class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        we can sort the array and use pointers that are spaced out by 3. 
        first == last (we know 3 available)
        if last > len(array), we can return 
        """
        nums.sort()
        first , last = 0 , 2
        while last < len(nums):
            if nums[first] != nums[last]:
                return nums[first]
            else:
                first += 3
                last += 3
        
        return nums[first]