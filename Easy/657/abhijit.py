class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        we can use an array to track position
        [U,D,L,R]
        """
        tracker = [0,0,0,0]

        for m in moves:
            if m == "U":
                if tracker[1] >= 1:
                    tracker[1] -= 1
                else:
                    tracker[0] += 1
            elif m == "D":
                if tracker[0] >= 1:
                    tracker[0] -= 1
                else:
                    tracker[1] += 1
            elif m == "L":
                if tracker[3] >= 1:
                    tracker[3] -= 1
                else:
                    tracker[2] += 1
            elif m == "R":
                if tracker[2] >= 1:
                    tracker[2] -= 1
                else:
                    tracker[3] += 1



        return tracker == [0,0,0,0]