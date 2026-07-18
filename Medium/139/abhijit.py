class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        The idea here is that if we have reached a certain index
        we want to proceed from there.
        """


        wordSet = set(wordDict)
    
        tracker = {}
        def find(prev, current):
            if current > len(s):
                return False
            if current == len(s):
                return True
            
            if (prev,current) in tracker:
                return tracker[(prev,current)]

            for w in wordSet:
                if s[current:current + len(w)] == w:
                    found = find(current,current + len(w))
                    if found:
                        tracker[(prev,current)] = True
                        return True
            
            tracker[(prev,current)] = False
            return False
            
        return find(-1,0)