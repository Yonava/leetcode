from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        output = []

        while top <= bottom and left <= right:
            # 1. traverse top row (left → right)
            for c in range(left, right + 1):
                output.append(matrix[top][c])
            top += 1

            # 2. traverse right column (top → bottom)
            for r in range(top, bottom + 1):
                output.append(matrix[r][right])
            right -= 1

            # 3. traverse bottom row (right → left)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    output.append(matrix[bottom][c])
                bottom -= 1

            # 4. traverse left column (bottom → top)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    output.append(matrix[r][left])
                left += 1

        return output
