class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check each first index of each row to find the correct row.
        # binary search 
        first_indexes = []
        for row in matrix:
            first_indexes.append(row[0])
        
        row = 0
        for i in range(len(first_indexes)):
            if target >= first_indexes[i]:
                row = i
            else:
                break

        if target in matrix[row]:
            return True
        else:
            return False
