class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        R1, C1 = len(mat1), len(mat1[0])
        R2, C2 = len(mat2), len(mat2[0])
        
        # Result matrix will be R1 x C2
        final_matrix = [[0] * C2 for _ in range(R1)]
        
        # Pre-process mat1 to find non-zero entries
        # Format: {row_index: [(col_index, value), ...]}
        sparse_mat1 = {}
        for r in range(R1):
            for k in range(C1):
                if mat1[r][k] != 0:
                    if r not in sparse_mat1:
                        sparse_mat1[r] = []
                    sparse_mat1[r].append((k, mat1[r][k]))
        
        # Multiply
        for r, items in sparse_mat1.items():
            for k, val1 in items:
                # Only iterate over the row in mat2 that matches our k
                for c in range(C2):
                    if mat2[k][c] != 0:
                        final_matrix[r][c] += val1 * mat2[k][c]
                        
        return final_matrix