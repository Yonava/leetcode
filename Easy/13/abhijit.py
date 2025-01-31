class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0  
        
       
        for index in range(len(s) - 1):  
            if mapping[s[index]] < mapping[s[index + 1]]:  
                total -= mapping[s[index]]  
            else:
                total += mapping[s[index]]  

        total += mapping[s[-1]]  
        return total
