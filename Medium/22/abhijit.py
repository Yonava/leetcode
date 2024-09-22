class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        returnSet = set()
        
        def close(string):
            pad = 0
            for i in range(len(string)-1,-1,-1):
                if string[i] == "(":
                    pad += 1
                else:
                    pad -= 1
    
            return string + pad * ")" 
        
        def search(curr_str,opening_paren_count,closing_paren_count):
            
            if opening_paren_count == n :
                returnSet.add(close(curr_str))
                return
            search(curr_str + "(",opening_paren_count+1,closing_paren_count)
            if len(curr_str) and opening_paren_count > closing_paren_count:
                search(curr_str + ")",opening_paren_count,closing_paren_count + 1) #

        search("",0,0)
        # print("testing",close("()()("))
        return returnSet