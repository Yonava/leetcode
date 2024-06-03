class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_pointer = 0
        s_pointer = 0
        while s_pointer < len(s):
            if t_pointer >= len(t):
                return 0
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                s_pointer += 1
        
        return len(t) - t_pointer