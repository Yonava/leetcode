class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def recurHelper(currShift, original, goal,count):
            print("currShift",currShift)
            if currShift == goal:
                return True
            if currShift == original and count > 0:
                return False
            newShift = currShift[1:] + currShift[0]
            return r(newShift, original, goal,count +1)
        
        return recurHelper(s,s,goal,0)
        