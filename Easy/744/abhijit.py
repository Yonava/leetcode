class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        
        # binary search for the smallest letter greater than target
        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) > ord(target):
                r = mid - 1
            else:
                l = mid + 1
        
        # since letters wrap around circularly, return letters[l % len(letters)]
        return letters[l % len(letters)]