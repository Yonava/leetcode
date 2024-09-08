class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        hash = {}

        for val in nums:
            if val in hash and hash[val] != 0:
                hash[val] -= 1
                count += 1
            else:
                diff = k - val
                hash[diff] = hash.get(diff,0) + 1

        return count

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        print(nums)
        l,r = 0, len(nums) - 1
        count = 0
        
        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] == k:
                count += 1
                l += 1
                r -= 1
        
        return count

        