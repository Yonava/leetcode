""" The trick is to maintain both the order of the opening and the asterisk. 
It is very easy to catch if there are more closing brackets then opening.
However, the ordering is very important when we need to check if each * can act as a closing brace
"""



class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ")" or s[-1] == "(":
            # both of these are base cases to false cases
            return False
        open_count = 0
        close_count = 0
        
        asterisk_count = []
        stack = []  
        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
                stack.append(i)
            elif s[i] == ")" and stack:
                close_count += 1
                stack.pop()
            elif s[i] == ")" and len(asterisk_count) > 0 and len(stack) == 0:
                close_count += 1
                asterisk_count.pop()
            elif s[i] == "*":
                asterisk_count.append(i)
            else:
                return False    
        
        #  we might need to close some of the open braces using Asterisls
        while len(stack) > 0 and len(asterisk_count) > 0:
            unmatchedIndex = stack.pop()
            asteriskIndex = asterisk_count.pop()
            if asteriskIndex < unmatchedIndex:
                return False
        
        print("open", open_count, "close", close_count)
        return len(stack) == 0
            