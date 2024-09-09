'''
we don't need to use a deque. we can just use another min stack. 
The idea is that if anything less is than the minimum has already been considered.

5 , 2 , 3, -1 , 5, 6

min stack : [5,2,-1]

5 is added as on substantiation, the min stack is empty and we must populate it
2 is a smaller value. Hence, we add 2.
3 is greater so we skip it. We add -1 as its lower than 2.
We've seen the least value so far as we uterate throiugh the stack.

'''

class MinStack:

    def __init__(self):
        self.stack = []     # Stack to store all values
        self.minStack = []  # Stack to store the minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If minStack is empty or the current value is smaller than or equal to the current minimum, push it onto minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # If the popped value is equal to the current minimum, pop from minStack as well
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]  # The current minimum is at the top of minStack
