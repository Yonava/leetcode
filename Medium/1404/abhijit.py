class Solution:
    def recursiveSol(self,num):
        if(int(num,2) == 1):
            return 0
        if num[-1] == "0":
            #even
            return 1 + self.recursiveSol(str(bin(int(num,2) // 2))[2:])
        else:
            return 1 + self.recursiveSol(str(bin(int(num,2) + 1))[2:])

    def numSteps(self, s: str) -> int:
        # trivial way: we
        val = self.recursiveSol(s)
        return val