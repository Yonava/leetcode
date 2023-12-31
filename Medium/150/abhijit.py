class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # left operator right
        int_seen = []
        operators = ["-","+", "/","*"]
        for token in tokens:
            # print(int)
            if token in operators:
                right = int_seen.pop()
                left = int_seen.pop()
                if token == "*":
                    int_seen.append(int(left * right))
                if token == "/":
                    int_seen.append(int(left / right))
                if token == "+":
                    int_seen.append(left + right)
                if token == "-":
                    int_seen.append(left - right)
    
            else:
                int_seen.append(int(token))
        
        return int_seen[0]