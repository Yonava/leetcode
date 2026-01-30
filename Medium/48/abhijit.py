class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # number_of_layers should be n // 2
        number_of_layers = n // 2

        def swap(i, j):
            # i is the current layer, j is the moving index
            # Save the top-left value
            val = matrix[i][j]

            # Move Bottom-Left into Top-Left
            matrix[i][j] = matrix[n - 1 - j][i]

            # Move Bottom-Right into Bottom-Left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            # Move Top-Right into Bottom-Right
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            # Move Top-Left (saved in val) into Top-Right
            matrix[j][n - 1 - i] = val

        # In your original, 'count' served as the offset. 
        # Using 'layer' directly in the range is cleaner.
        for layer in range(number_of_layers):
            # We stop at n - 1 - layer to avoid double-swapping the corners
            for j in range(layer, n - 1 - layer):
                swap(layer, j)