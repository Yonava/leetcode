class Solution:
   ''' we use the intuition of the substring until index j
   opt(len(s)) == True
   opt(j) = opt(j+len(vj)) or opt(j)'''
   
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {} 

        def findSubString(j):
            if j == len(s): 
                return True
            if j in memo:  
                return memo[j]

            returnVal = False
            for w in wordDict:
                
                if s[j: j + len(w)] == w:
                   
                    val = findSubString(j + len(w))
                    returnVal = val or returnVal
                    if returnVal: 
                        break

            memo[j] = returnVal  
            return returnVal

        return findSubString(0)