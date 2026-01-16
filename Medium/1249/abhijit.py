class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        
        use a stack to store the valid possible 
        
        
        """
        left_paren_pos = deque()# index of the left parents
        final_s = []
        for i,c in enumerate(s):
            if c == ")" and len(left_paren_pos) == 0:
                continue
            elif c == ")" and len(left_paren_pos) != 0:
                left_paren_pos.popleft()
                final_s.append(c)
            elif c == "(":
                final_s.append(c)
                left_paren_pos.append(len(final_s) - 1)
            else:
                final_s.append(c)
        
        for i in left_paren_pos:
            final_s[i] = ""
        
        return "".join(final_s)
                
