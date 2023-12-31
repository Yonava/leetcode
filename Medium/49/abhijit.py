from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list) # you can provide a call back function that sets the default value
        for index,string in enumerate(strs):
            chars = list(string)
            chars.sort()
            anagram = "".join(chars)
            seen[anagram].append(strs[index])
            # print(sorted(chars))
            # sorted.append(list(string).sort().join(""))
        
        rtnList = []
        for indexlist in seen:
            rtnList.append(seen[indexlist])
                
        return rtnList