# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while end > start:
            mid_val = (start + end) // 2
            if not isBadVersion(mid_val):
                start = mid_val + 1
            else:
                end = mid_val
        return end
    
'''
My intuition:
- a modification of binary search. to find the first value.
- if the middle value is false, we can disregard all the values before as nothing has failed till then
- if the middle value is true, we cannot ascertain that it is the lowest so we continue looking
'''