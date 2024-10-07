from math import gcd
'''
I was extremely close.
missed normalisation and using gcd to avoid having to deal with fractions
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = float("-inf")
        
        if len(points) == 1:
            return 1
        
        for x1, y1 in points:
            gradients = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    # Skip the same point
                    continue
                
                # Handle vertical lines where x-coordinates are the same
                if x1 == x2:
                    gradient = 'inf'  # Vertical line
                else:
                    # Calculate dy and dx
                    dy = y2 - y1
                    dx = x2 - x1
                    # Simplify the slope using GCD
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    # Ensure slope consistency for negative values
                    if dx < 0:
                        dy, dx = -dy, -dx
                    gradient = (dy, dx)
                
                # Add the gradient to the dictionary and count occurrences
                if gradient not in gradients:
                    gradients[gradient] = 1
                else:
                    gradients[gradient] += 1

            # Find the maximum number of points on a line for the current point
            if gradients:
                max_points = max(max_points, max(gradients.values()) + 1)

        return max_points
