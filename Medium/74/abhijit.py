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


# a log(m * n) solution:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check each first index of each row to find the correct row.
        # binary search 
        high_r = len(matrix) -1
        low_r = 0
        row_found = -1
        print(high_r)
        print(low_r)
        while high_r >= low_r :
            mid = (high_r + low_r) // 2
            first_val = matrix[mid][0]
            last_val = matrix[mid][-1]
            print("mid val:", mid)
            print("first val:", first_val)
            print("last_val:", last_val)
            if target >= first_val and target <= last_val:
                row_found = mid
                break
            if target < first_val:
                high_r = mid -1
            if target > last_val:
                low_r = mid + 1
        
        if row_found == -1:
            print("out here?")
            return False

        high = len(matrix[row_found]) -1
        low = 0

        while high >= low:
            mid = (high + low) // 2
            if target == matrix[row_found][mid]:
                return True
            elif target > matrix[row_found][mid]:
                low = mid + 1
            else:
                high = mid -1
        
        return False
            
