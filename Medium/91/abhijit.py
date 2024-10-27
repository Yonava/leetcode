class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def waysToDecodeString(j: str):
            if len(j) and j[0] == "0":
                return -1
            if len(j) <= 1:
                return 1
            if j in memo:
                return memo[j]
            str1 =  waysToDecodeString(j[1:])
            str1 = 0 if str1 == -1 else str1
            str2 = 0
            if int(j[:2]) >= 10 and int(j[:2]) <= 26:
                str2 =  waysToDecodeString(j[2:])
                str2 = 0 if str2 == -1 else str2
            memo[j] =  str1 + str2
            return memo[j]
        ways = waysToDecodeString(s)
        return  0 if  ways == -1 else ways
            
