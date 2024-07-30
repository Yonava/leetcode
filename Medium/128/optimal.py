class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        while nums_set:
            curr = nums_set.pop()
            up, down = curr+1, curr-1
            sequence_len = 1
            
            while up in nums_set: 
                nums_set.remove(up)
                up += 1
            sequence_len += (up-curr-1)

            while down in nums_set:
                nums_set.remove(down)
                down -= 1
            sequence_len += (curr-down-1)

            res = max(res, sequence_len)
        return res
    
# as the values are being removed in the inner while loop, it is O(n)