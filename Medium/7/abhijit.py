class Solution:
    def reverse(self, x: int) -> int:
        def rev(x, place):
            val = x % 10
            if place == 0:
                return val
            return val * (10 ** place) + rev(x // 10, place - 1)
    

        if x > 0:
            place = len(str(x))
            reversed_x = rev(x,place-1)
            if reversed_x > 2 ** 31 -1:
                return 0
            return reversed_x
        else: 
            place = len(str(x * -1))
            reversed_x = -1 *  rev(-1 * x, place-1)
            if reversed_x < -2 ** 31:
                return 0
            return reversed_x
        
