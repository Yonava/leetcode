class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        isNeg = True if s[0] == '-' else False
        isPos = True if s[0] == "+" else False
        isNonDigit = 0
        numSoFar = ""
        
        i = 1 if isNeg or isPos else 0
        while i < len(s) and s[i].isdigit():
            numSoFar += s[i]
            i += 1
        
        if numSoFar == "":
            return 0

        final_number = -1 * int(numSoFar) if isNeg else int(numSoFar)

        if final_number > ( 2**31 - 1):
            return 2**31 - 1
        elif final_number < (-2**31):
            return -2**31


        return final_number
            
