class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # While last digit in stack is larger than current AND we can still remove digits
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If still need to remove digits, remove from the end
        while k > 0:
            stack.pop()
            k -= 1
        
        # Build result and remove leading zeros
        result = "".join(stack).lstrip("0")
        
        return result if result else "0"
