# This solution is not optimal and only passes 40/48 test cases.
# However, the margin of error is small.

# Optimal solution:
def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)

class Solution:

    def merge(self,arr1,arr2):
        arr1_len = len(arr1)
        # merge the array
        newArr = arr1 + arr2  
        
        if newArr[arr1_len - 1][0] == newArr[arr1_len][0]:
            # we do not need to really check anything here as it doesn't really matter
            return newArr
        elif newArr[arr1_len - 1][0] > newArr[arr1_len][0] and newArr[arr1_len - 1][1] <= newArr[arr1_len][1]:
            # fix the mismatch
            newArr[arr1_len - 1][1] = newArr[arr1_len ][1] + 1
            i = arr1_len - 1
            while i >= 1:
                if newArr[i-1][0] > newArr[i][0]:
                    newArr[i-1][1] = newArr[i][1] + 1
                i -= 1
        elif newArr[arr1_len - 1][0] < newArr[arr1_len][0] and newArr[arr1_len - 1][1] >= newArr[arr1_len][1]:
            # fix the mismatch
            newArr[arr1_len][1] = newArr[arr1_len - 1 ][1] + 1
            i = arr1_len
            while i <= len(newArr) - 2:
                if newArr[i + 1][0] > newArr[i][0]:
                    newArr[i+1][1] = newArr[i][1] + 1
                i += 1
       
        return newArr
        
    def recurHelper(self,arr):
        if len(arr) == 1:
            return arr
        arr1 = self.recurHelper(arr[:len(arr)//2])
        arr2 = self.recurHelper(arr[len(arr)//2:])
        newArr = self.merge(arr1,arr2)
        return newArr

    def candy(self, ratings: List[int]) -> int:
        candy = []
        for r in ratings:
            candy.append([r,1])

        self.recurHelper(candy)
        return sum(int(candy) for rating,candy in candy)
            