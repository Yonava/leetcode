# correct:
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        current_num = 0
        last_operator = '+'
        operators = {'+', '-', '*', '/'}
        
        for i, char in enumerate(s):
            # Build the multidigit number
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # If char is an operator OR we reached the end of the string
            if char in operators or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(current_num)
                elif last_operator == '-':
                    stack.append(-current_num)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_num)
                elif last_operator == '/':
                    # In Python, // rounds towards negative infinity. 
                    # We need to truncate towards zero as per LeetCode requirements.
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // current_num))
                    else:
                        stack.append(prev // current_num)
                
                # Update for the next round
                last_operator = char
                current_num = 0
        
        return sum(stack)


#  very close to the above solution but I was trying to do it with two stacks and it got a bit messy.
# should have tried to reason a little more. it wasn't very obvious for me
class Solution:
    def calculate(self, s: str) -> int:
        """
        pemdas

        multiplcation, division first -> adition and subtraction
        """

        op = deque([])
        numbers = deque([])
        operators = set(["+", "*", "/","-"])

        def eval(symbol, n1, n2):
            if symbol == "+":
                return n1 + n2
            elif symbol == "-":
                return n1 - n2
            elif symbol == "/":
                return n1 // n2
            else:
                return n1 * n2

        l,r = 0 ,0 
        
        while r < len(s):
            if s[r] in operators:
                # we want to evaluate if possible

                # first we store the number we parsed
                numbers.append(int(s[l:r]))
                # evaluate
                if op:
                    curr = op[-1]
                    new = s[r]
                    evaluated_val = None

                    if curr in set(["-","+"]) and new in set(["-","+"]):
                        # we should evaluate
                        evaluated_val = eval(curr, numbers[-2], numbers[-1])
                        op.pop()
                        numbers.pop()
                        numbers.pop()
                        numbers.append(evaluated_val)
                    elif curr in set(["*","/"]) and new in set(["*","/","+","-"]):
                        # we should evaluate
                        evaluated_val = eval(curr, numbers[-2], numbers[-1])
                        op.pop()
                        numbers.pop()
                        numbers.pop()
                        numbers.append(evaluated_val)

                op.append(s[r])
                r += 1
                l = r
            else:
                r += 1

        # clean up at the end
        # parse the number
        numbers.append(int(s[l:r]))
        print("the end", numbers, op)
        # 1. Final check for a trailing * or /
        # (Example: 1 + 2 * 3 -> the 2 * 3 needs to be squashed now)
        if op and op[-1] in "*/":
            symbol = op.pop()
            n2 = numbers.pop()
            n1 = numbers.pop()
            numbers.append(eval(symbol, n1, n2))

        # 2. Now the stack ONLY contains + and -
        # We must process these from LEFT to RIGHT
        while op:
            symbol = op.popleft()
            n1 = numbers.popleft()
            n2 = numbers.popleft()
            result = eval(symbol, n1, n2)
            numbers.appendleft(result) # Keep pushing to front to maintain order

        print(numbers,op)
        return numbers[-1]



