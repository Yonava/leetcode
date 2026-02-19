class Solution:
    def customSortString(self, order: str, s: str) -> str:
        tracker = {}
        for c in s:
            tracker[c] = tracker.get(c,0) + 1 
        
        final_string = ""
        for c in order:
            if c in tracker:
                final_string += c * tracker[c]
                del tracker[c]
        
        if tracker:
            for k,v in tracker.items():
                final_string += k * v
        
        return final_string