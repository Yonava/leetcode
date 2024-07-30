class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # add to hashmap if seen, del key if already exists
        tracker = {}
        for num in nums:
            if tracker.get(num,-1) < 0:
                tracker[num] = 1
            else:
                del tracker[num]
        return tracker.keys()