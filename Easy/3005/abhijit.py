class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        max_num = float("-inf")
        max_set = 0

        for num, count in count.items():
            if count == max_num:
                max_set += 1
            elif count > max_num:
                max_set = 1
                max_num = count
        
            
        return max_set * max_num
            