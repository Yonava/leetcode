class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seenSet = set(nums) # enable o(1) check to see if string is within set
        mySet = set()

        def bfs(currStr):
            if len(currStr) == len(nums[0]):
                if currStr not in seenSet:
                    return currStr
                else:
                    return None

            foundStr1 = bfs(currStr + "0")
            if foundStr1:
                return foundStr1
            foundStr2 = bfs(currStr + "1")
            if foundStr2:
                return foundStr2
        
        return bfs("")

