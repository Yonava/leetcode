class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        we assume all are cows -> the overlap of count
        check to see if it is a bull. if it is a bull
        """

        tracker = {}
        for c in secret:
            tracker[c] = tracker.get(c,0) + 1

        
        bulls = 0 # correct pos
        cows = 0 # wrong position

        cow_index = []
        for i,c in enumerate(guess):
            if secret[i] == c:
                bulls += 1
                tracker[c] -= 1
                if tracker[c] == 0:
                    del tracker[c]
            else:
                cow_index.append(i)
        
        for i in cow_index:
            if guess[i] in tracker:
                cows +=1
                tracker[guess[i]] -= 1
                if tracker[guess[i]] == 0:
                    del tracker[guess[i]]

        
        
        return str(bulls) + "A" + str(cows) + "B"
            
