class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def recurse(arr, n):
            if n == 0:
                return arr
            else:
                l,r = 0,1
                new_arr = []
                while r < len(arr[-1]):
                    new_arr.append(arr[-1][l] + arr[-1][r])
                    l += 1
                    r +=1
                new_arr = [1] + new_arr + [1]
                arr.append(new_arr)
                return recurse(arr,n-1)
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            return recurse([[1], [1,1]], numRows -2)
        



            