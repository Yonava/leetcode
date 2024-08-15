class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s    
        
        result = ""
        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for index in range(r,len(s),increment):
                result += s[index]
                if r > 0 and r < (numRows - 1) and (index + increment - 2*r) < len(s):
                    result += s[index + (increment - 2*r)]
        
        return result


