class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiver = 0
        tenner = 0 
        for bill in bills:
            print(f"currently on {bill}, fiver: {fiver} tenner: {tenner}")
            if bill == 5:
                fiver += 1
            if bill == 10:
                if fiver == 0:
                    return False
                else:
                    fiver -= 1
                    tenner += 1
            if bill == 20:
                if tenner >= 1:
                    if fiver >= 1:
                        tenner -= 1
                        fiver -= 1
                    else:
                        return False
                else:
                    if fiver >= 3:
                        fiver -= 3
                    else:
                        return False

        return True

            