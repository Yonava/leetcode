class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        r = 1
        while r < len(strs[0]) + 1:
            print(f"r {r}")
            curr_str = strs[0][:r]
            print("curr_str", curr_str)
            for string in strs[1:]:
                print(f"current: {string[:r]} | expected: {curr_str} ")
                if string[:r] != curr_str and r != 0:
                    return string[:r-1]
            r +=1
        
        if r == len(strs[0]) + 1:
            return strs[0]
           
        return ""
            
                                
       
            
        