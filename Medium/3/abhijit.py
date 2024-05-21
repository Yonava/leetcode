class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # explanation
        # abca 
        # // first case. where the incoming character s at the start of the seen string
        # // we truncate remoiving index 0 and continue to move forward
        # pwwkew
        # pww
        # // second case. were the incoming character is at the end of the seen string. 
        # // we discard everything that comes before and start fresh as there will be a gap
        # // we are looking substrings and not subsequences
        
        # we could just slice the string from where we last saw the element and then continue from there

        seen = []
        current = []
        if len(s) == 0:
            #simple base case to handle empty string 
            return 0
        
        for i in s:
            print(i)
            print(current)
            if i in current:
                if(i == current[0]):
                    seen.append("".join(current))
                    current = current[1:]
                    current.append(i)
                else:
                    index = current.index(i)
                    seen.append("".join(current))
                    current = current[index + 1:]
                    current.append(i)
            else:
                current.append(i)
        
        # handles the final string that we end on
        seen.append("".join(current))

        print(seen)
        lengths = [len(s) for s in seen]
        print("lengths",lengths)
        print(max(lengths))
        return max(lengths)
     
