class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for i,val in enumerate(nums):
            if val not in hash:
                hash[val] = i
            else:
                if abs(hash[val] - i) <= k:
                    return True
                else:
                    hash[val] = i
        return False