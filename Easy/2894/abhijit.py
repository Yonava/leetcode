class Solution:
    # without loop
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_integers = n // m
        sum_of_divisible_integers = m * ((divisible_integers) * (divisible_integers + 1))//2
        sum_of_total = (n * (n + 1)) // 2
        sum_of_non_divisible = sum_of_total - sum_of_divisible_integers
        return sum_of_non_divisible -sum_of_divisible_integers
    
    # loop
    def _differenceOfSums(self, n: int, m: int) -> int:
      for i in range(1,n+1):
            if i % m == 0:
                divisible += i
            else:
                non_divisible += i
        return non_divisible - divisible