class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        
        # Track the last seen index of each digit 0-9
        last = {int(d): i for i, d in enumerate(digits)}
        
        # Scan from left to right
        for i, d in enumerate(digits):
            # Look for a larger digit (9 down to current+1) that appears later
            for bigger_digit in range(9, int(d), -1):
                if last.get(bigger_digit, -1) > i:
                    # Found the best swap!
                    digits[i], digits[last[bigger_digit]] = digits[last[bigger_digit]], digits[i]
                    return int("".join(digits))
        
        return num