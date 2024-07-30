class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycles = time // (n - 1)
        remainder = time % ( n - 1 )
        if cycles % 2 == 0:
            return remainder + 1
        else:
            return n - remainder   