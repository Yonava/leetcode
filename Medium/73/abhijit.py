class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # --> neat trick to save on space
        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
        
        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        we use a zero-out-set for axis x and y.
        if any values are seen in these sets then we can zero out.
        This is an o(m + n) space solution.

        seen set -> O(mn) space. This is bad.
        """

        zero_x = set()
        zero_y = set()

        # populate the sets of rows and columns to zero out
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    zero_x.add(x)
                    zero_y.add(y)

        # zero-out in place
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x in zero_x:
                    matrix[x][y] = 0
                if y in zero_y:
                    matrix[x][y] = 0
        
        return matrix