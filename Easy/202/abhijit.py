class Solution:
    def recurHelper(self,num,seen):
        if num == 1:
            return True
        
        if num in seen:
            return False

        seen.add(num)
        sum = 0
        for char in str(num):
            sum += int(char) ** 2
    
        return self.recurHelper(sum,seen)

    
    def isHappy(self, n: int) -> bool:
        seen = set()
        return self.recurHelper(n,seen)