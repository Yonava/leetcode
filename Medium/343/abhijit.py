class Solution:
    def integerBreak(self, n: int) -> int:
        """
        max_product(2) = 1
        max_product(3) = 1 * max_product(2)
        max_product(4) = 1 * max_product(3) or 2 * max_product(2) 
        """

        arr = [1] * (n+2)
        arr[0], arr[1], arr[2] = 1, 1, 1

        for i in range(2, n + 1):
            for j in range(1, i):
                arr[i] = max(
                    arr[i],
                    max(j, arr[j]) * max(i - j, arr[i - j]))
        
        return arr[-2]

"""
I was always focusing on breaking j by using arr[j]. When we could also break (i-j) such as arr[i-j]


class Solution:
    def integerBreak(self, n: int) -> int:
        max_product(2) = 1
        max_product(3) = 1 * max_product(2)
        max_product(4) = 1 * max_product(3) or 2 * max_product(2) 

        arr = [1] * (n+2)
        arr[0], arr[1], arr[2] = 1, 1, 1

        for i in range(2, n + 2):
            print(arr)
            for j in range(i):
                arr[i] = max((i - j) * arr[j], arr[i])
        
        return arr[-2]
"""
    