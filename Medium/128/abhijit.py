class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        unsorted array
        use a hashmap to store the value and the consecutive length so far
        for example: we encounter 1, we add 1 : the consecutive val into the nums
        if we encounter 2, we pull the value from 2 and add 3 with the value pulled from 2 + 1
        '''
        tracker = {}
        nums.sort() # n * log(n)
        for num in nums: #n
            if tracker.get(num,-1) == -1:
                tracker[num + 1] = 1
            else:
                tracker[num + 1] = tracker[num] + 1
        if(not len(tracker.values())):
            return 0
        
        return max(tracker.values())

# n * log(n) solution