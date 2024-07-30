class Solution:
    def numSteps(self, s: str) -> int:
        # trivial way: we
        carry = 0
        steps = 0
        for i in range(len(s)-1,0,-1):
            if int(s[i]) + carry == 1:
                carry = 1
                steps += 2
            else:
                steps +=1
        
        return steps + carry


'''
the constrain mentions that the most important bit is 1
hence we implement the steps + carry. If there is no carry, then we stop.
otherwise we have to do one more step of division by 2.
'''